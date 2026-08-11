"""Full-universe factor attribution vs forward returns.

Uses data/features/*_1d.csv + data/labels/*_fwd.csv (ALL tickers).
Writes:
  data/attribution/YYYY-MM-DD_ic.csv
  01_daily/YYYY-MM-DD_attribution.md
  02_lessons/candidate/YYYY-MM-DD_lesson.md (provisional)

CLI: python -m src.attribution [--scan-date YYYY-MM-DD] [--horizon 1d|2d|3d|auto]

Every report states EXPLICITLY: the scan date whose features were used, the
prior snapshot the deltas were computed against, which forward horizon was
graded, and the exact calendar dates that horizon covers.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from . import config

FEATURES_DIR = config.DATA / "features"
LABELS_DIR = config.DATA / "labels"
ATTR_DIR = config.DATA / "attribution"
LESSONS_CAND = config.ROOT / "02_lessons" / "candidate"


def _spearman(a: pd.Series, b: pd.Series) -> float:
    m = a.notna() & b.notna()
    if m.sum() < 30:
        return float("nan")
    return float(a[m].rank().corr(b[m].rank()))


def _load_joined(scan_date: str) -> pd.DataFrame | None:
    fp = FEATURES_DIR / f"{scan_date}_1d.csv"
    lp = LABELS_DIR / f"{scan_date}_fwd.csv"
    if not fp.exists() or not lp.exists():
        return None
    f = pd.read_csv(fp, low_memory=False)
    l = pd.read_csv(lp, low_memory=False)
    j = f.merge(l, on="Ticker", how="inner", suffixes=("", "_lbl"))
    return j


def _feature_cols(df: pd.DataFrame) -> list[str]:
    cols = []
    if "true_ret" in df.columns:
        cols.append("true_ret")
    if "total_score" in df.columns:
        cols.append("total_score")
    for c in df.columns:
        if c.startswith("d_") and df[c].dtype != object:
            cols.append(c)
    for c in ("Relative Volume", "Relative Strength Index (14)",
              "Performance (Week)", "Performance (Month)", "Short Float",
              "Institutional Transactions", "upside_pct_lvl"):
        if c in df.columns:
            cols.append(c)
    return cols


def pick_label(df: pd.DataFrame, horizon: str = "auto") -> str:
    """horizon: '1d'/'2d'/'3d' forces fwd_<horizon>; 'auto' keeps the legacy
    deepest-label-with-data preference (3d → 2d → 1d)."""
    if horizon in ("1d", "2d", "3d"):
        return f"fwd_{horizon}"
    if df["fwd_3d"].notna().sum() >= 30:
        return "fwd_3d"
    if df.get("fwd_2d", pd.Series(dtype=float)).notna().sum() >= 30:
        return "fwd_2d"
    return "fwd_1d"


def analyze(scan_date: str, df: pd.DataFrame, horizon: str = "auto") -> dict:
    label = pick_label(df, horizon)
    y = df[label]
    n = int(y.notna().sum())
    hnum = label[-2]  # '1' | '2' | '3'
    pair_date = (df["pair_date"].mode().iloc[0]
                 if "pair_date" in df.columns and df["pair_date"].notna().any()
                 else "?")
    label_date = (df[f"label_date_{hnum}"].mode().iloc[0]
                  if f"label_date_{hnum}" in df.columns
                  and df[f"label_date_{hnum}"].notna().any() else "?")
    result = {"scan_date": scan_date, "label": label, "n": n,
              "pair_date": pair_date, "label_date": label_date,
              "features": []}

    # score calibration
    if "total_score" in df.columns:
        ic = _spearman(df["total_score"], y)
        result["score_ic"] = ic
        q = pd.qcut(df.loc[y.notna(), "total_score"], 5, labels=False, duplicates="drop")
        cal = []
        sub = df.loc[y.notna()].copy()
        sub["_q"] = q.values
        for qi, g in sub.groupby("_q"):
            cal.append({
                "quintile": int(qi) + 1,
                "mean_fwd": float(g[label].mean()),
                "hit_up": float((g[label] > 0.015).mean()),
                "n": int(len(g)),
            })
        result["score_calibration"] = cal

    # univariate ICs (overall + within up-movers / within down-movers)
    y_up = y > 0
    y_dn = y < 0
    for col in _feature_cols(df):
        if col == "total_score":
            continue
        ic = _spearman(df[col], y)
        if ic != ic:
            continue
        # direction buckets
        up = df[col] > 0
        dn = df[col] < 0
        mean_up = float(y[up & y.notna()].mean()) if (up & y.notna()).sum() else float("nan")
        mean_dn = float(y[dn & y.notna()].mean()) if (dn & y.notna()).sum() else float("nan")
        result["features"].append({
            "feature": col,
            "ic": ic,
            "ic_within_up": _spearman(df[col][y_up], y[y_up]),
            "ic_within_down": _spearman(df[col][y_dn], y[y_dn]),
            "mean_fwd_when_pos": mean_up,
            "mean_fwd_when_neg": mean_dn,
            "n_pos": int((up & y.notna()).sum()),
            "n_neg": int((dn & y.notna()).sum()),
        })
    result["features"].sort(key=lambda r: abs(r["ic"]), reverse=True)

    # tandem / interaction probes
    interactions = []
    if "true_ret" in df.columns and "status_trend" in df.columns:
        for trend in ("DOWNTREND", "UPTREND", "MIXED"):
            m = (df["status_trend"] == trend) & df["true_ret"].notna() & y.notna()
            m_up = m & (df["true_ret"] > 0.03)
            if m_up.sum() >= 20:
                interactions.append({
                    "name": f"true_ret>3% & {trend}",
                    "n": int(m_up.sum()),
                    "mean_fwd": float(y[m_up].mean()),
                    "hit_up": float((y[m_up] > 0.015).mean()),
                })
    if "d_Performance (Month)" in df.columns and "Performance (Month)" in df.columns:
        m = y.notna() & df["d_Performance (Month)"].notna()
        a = m & (df["d_Performance (Month)"] > 1.5) & (df["Performance (Month)"] < 0)
        b = m & (df["d_Performance (Month)"] > 1.5) & (df["Performance (Month)"] > 0)
        for name, mask in (("MonthΔ+ & Month<0", a), ("MonthΔ+ & Month>0", b)):
            if mask.sum() >= 20:
                interactions.append({
                    "name": name,
                    "n": int(mask.sum()),
                    "mean_fwd": float(y[mask].mean()),
                    "hit_up": float((y[mask] > 0.015).mean()),
                })
    result["interactions"] = interactions

    # risk dominance
    risk = []
    if "Performance (Week)" in df.columns:
        for thr, name in ((40, "Week>40%"), (25, "Week>25%"), (100, "Week>100%")):
            m = (df["Performance (Week)"] > thr) & y.notna()
            if m.sum() >= 15:
                risk.append({
                    "name": name,
                    "n": int(m.sum()),
                    "mean_fwd": float(y[m].mean()),
                    "mean_fwd_if_score_top": float(
                        y[m & (df["total_score"] > df["total_score"].quantile(0.8))].mean()
                    ) if "total_score" in df.columns and (m & (df["total_score"] > df["total_score"].quantile(0.8))).sum() else float("nan"),
                })
    if "Relative Strength Index (14)" in df.columns:
        m = (df["Relative Strength Index (14)"] > 75) & y.notna()
        if m.sum() >= 15:
            risk.append({
                "name": "RSI>75",
                "n": int(m.sum()),
                "mean_fwd": float(y[m].mean()),
                "mean_fwd_if_score_top": float("nan"),
            })
    result["risk"] = risk
    return result


def write_ic_csv(scan_date: str, result: dict) -> Path:
    ATTR_DIR.mkdir(parents=True, exist_ok=True)
    rows = result.get("features", [])
    path = ATTR_DIR / f"{scan_date}_ic.csv"
    pd.DataFrame(rows).to_csv(path, index=False)
    (ATTR_DIR / f"{scan_date}_summary.json").write_text(
        json.dumps(result, indent=2, default=str), encoding="utf-8")
    return path


def write_md(result: dict) -> Path:
    d = result["scan_date"]
    L = [f"# Factor attribution — {d}", ""]
    L.append(f"**What this report measures, exactly:** features computed from "
             f"the **{d}** Finviz snapshot (deltas vs the **{result.get('pair_date', '?')}** "
             f"snapshot), graded against `{result['label']}` = the return from "
             f"**{d}** to **{result.get('label_date', '?')}** "
             f"(n={result['n']} stocks with valid labels).")
    L.append("Provisional until multiple scan dates agree.")
    L.append("")
    L.append("_Column guide: **IC** = Spearman rank correlation between the "
             "feature and the forward return (whole universe); **IC↑** = IC "
             "computed only among stocks that went UP; **IC↓** = IC only "
             "among stocks that went DOWN. A high IC↑ means the feature "
             "ranks winners among winners._")
    L.append("")
    if "score_ic" in result:
        L.append(f"## Score calibration")
        L.append(f"- Spearman IC(total_score, {result['label']}) = **{result['score_ic']:.4f}**")
        L.append("")
        L.append("| Quintile | Mean fwd | Hit up>1.5% | n |")
        L.append("|---|---|---|---|")
        for c in result.get("score_calibration", []):
            L.append(f"| {c['quintile']} | {c['mean_fwd']*100:.2f}% | {c['hit_up']*100:.1f}% | {c['n']} |")
        L.append("")
    L.append("## Top |IC| features (full universe)")
    L.append("")
    L.append("| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |")
    L.append("|---|---|---|---|---|---|---|")

    def _ic_s(v: float) -> str:
        return f"{v:+.4f}" if v == v else "n/a"

    def _pct_s(v: float) -> str:
        return f"{v * 100:.2f}%" if v == v else "n/a"

    for r in result.get("features", [])[:25]:
        L.append(
            f"| {r['feature']} | {_ic_s(r['ic'])} | "
            f"{_ic_s(r.get('ic_within_up', float('nan')))} | "
            f"{_ic_s(r.get('ic_within_down', float('nan')))} | "
            f"{_pct_s(r['mean_fwd_when_pos'])} | "
            f"{_pct_s(r['mean_fwd_when_neg'])} | "
            f"{r['n_pos']}/{r['n_neg']} |"
        )
    L.append("")
    if result.get("interactions"):
        L.append("## Combinations")
        L.append("")
        L.append("| Pattern | n | Mean fwd | Hit up |")
        L.append("|---|---|---|---|")
        for r in result["interactions"]:
            L.append(f"| {r['name']} | {r['n']} | {r['mean_fwd']*100:.2f}% | {r['hit_up']*100:.1f}% |")
        L.append("")
    if result.get("risk"):
        L.append("## Risk dominance probes")
        L.append("")
        L.append("| State | n | Mean fwd | Mean fwd if score top quintile |")
        L.append("|---|---|---|---|")
        for r in result["risk"]:
            mt = r.get("mean_fwd_if_score_top")
            mts = f"{mt*100:.2f}%" if mt == mt else "n/a"
            L.append(f"| {r['name']} | {r['n']} | {r['mean_fwd']*100:.2f}% | {mts} |")
        L.append("")
    path = config.DAILY / f"{d}_attribution.md"
    config.DAILY.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(L), encoding="utf-8")
    return path


def write_candidate_lesson(result: dict) -> Path | None:
    """Emit one provisional candidate if clear signals exist."""
    if result["n"] < 100:
        return None
    bullets = []
    ic = result.get("score_ic")
    if ic == ic:
        bullets.append(f"Score IC vs {result['label']}: {ic:+.4f} (n={result['n']})")
    for r in result.get("features", [])[:5]:
        bullets.append(f"{r['feature']} IC={r['ic']:+.4f}")
    for r in result.get("interactions", []):
        bullets.append(f"Combo {r['name']}: mean_fwd={r['mean_fwd']*100:.2f}% n={r['n']}")
    for r in result.get("risk", []):
        bullets.append(f"Risk {r['name']}: mean_fwd={r['mean_fwd']*100:.2f}% n={r['n']}")
    if not bullets:
        return None

    # pick a stable trigger pattern string for promote clustering
    top = result.get("features", [None])[0]
    trigger = f"attr:{result['label']}:top={top['feature'] if top else 'none'}:score_ic={ic}"
    body = {
        "trigger_pattern": trigger[:200],
        "current_behavior": "baseline rubric weights unchanged",
        "corrected_behavior": "review top IC features and interactions; consider weight/gate tweaks after repeats",
        "evidence_cited": "; ".join(bullets)[:500],
        "error_category": "ATTRIBUTION",
        "date": result["scan_date"],
        "status": "candidate",
    }
    LESSONS_CAND.mkdir(parents=True, exist_ok=True)
    path = LESSONS_CAND / f"{result['scan_date']}_lesson.md"
    fm = "---\n" + "\n".join(f'{k}: "{str(v).replace(chr(34), "")}"' for k, v in body.items()) + "\n---\n\n"
    path.write_text(fm + "# Attribution lesson (provisional)\n\n" + "\n".join(f"- {b}" for b in bullets) + "\n",
                    encoding="utf-8")
    return path


def run(scan_date: str, horizon: str = "auto") -> None:
    df = _load_joined(scan_date)
    if df is None:
        print(f"[attr] {scan_date}: need features + labels — skip")
        return
    if df["fwd_1d"].notna().sum() < 30 and df.get("fwd_3d", pd.Series(dtype=float)).notna().sum() < 30:
        print(f"[attr] {scan_date}: insufficient labeled rows")
        return
    result = analyze(scan_date, df, horizon=horizon)
    if result["n"] < 30:
        print(f"[attr] {scan_date}: label {result['label']} has only "
              f"{result['n']} valid rows — skip")
        return
    write_ic_csv(scan_date, result)
    md = write_md(result)
    les = write_candidate_lesson(result)
    print(f"[attr] wrote {md}" + (f" + {les}" if les else ""))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan-date", default=None)
    ap.add_argument("--horizon", default="auto",
                    choices=["auto", "1d", "2d", "3d"],
                    help="which forward return to grade against; "
                         "auto = deepest label with >=30 rows")
    args = ap.parse_args()
    if args.scan_date:
        run(args.scan_date, horizon=args.horizon)
        return
    for p in sorted(FEATURES_DIR.glob("*_1d.csv")):
        run(p.stem.replace("_1d", ""), horizon=args.horizon)


if __name__ == "__main__":
    main()
