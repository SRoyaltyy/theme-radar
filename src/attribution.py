"""Full-universe factor attribution vs forward returns.

Uses data/features/*_1d.csv + data/labels/*_fwd.csv (ALL tickers).

Wording:
  signal_asof (scan_date) = day features/scores were formed
  prediction_day          = day the trade is for (exit snapshot)
  entry_price             = Price at signal_asof
  exit_price              = Price on prediction_day
  fwd_*                   = long return entry -> exit

Writes:
  data/attribution/YYYY-MM-DD_ic.csv
  01_daily/YYYY-MM-DD_attribution.md
  02_lessons/candidate/YYYY-MM-DD_lesson.md (provisional)

CLI: python -m src.attribution [--scan-date YYYY-MM-DD] [--horizon 1d|2d|3d|auto]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

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
    return f.merge(l, on="Ticker", how="inner", suffixes=("", "_lbl"))


def _feature_cols(df: pd.DataFrame) -> list[str]:
    cols = []
    for c in df.columns:
        if c.startswith("d_") and df[c].dtype != object:
            cols.append(c)
    for c in ("Relative Volume", "Relative Strength Index (14)",
              "Performance (Week)", "Performance (Month)", "Short Float",
              "Institutional Transactions", "upside_pct_lvl", "total_score",
              "true_ret"):
        if c in df.columns:
            cols.append(c)
    return cols


def pick_label(df: pd.DataFrame, horizon: str = "auto") -> str:
    if horizon in ("1d", "2d", "3d"):
        return f"fwd_{horizon}"
    if "fwd_3d" in df.columns and df["fwd_3d"].notna().sum() >= 30:
        return "fwd_3d"
    if "fwd_2d" in df.columns and df["fwd_2d"].notna().sum() >= 30:
        return "fwd_2d"
    return "fwd_1d"


def analyze(scan_date: str, df: pd.DataFrame, horizon: str = "auto") -> dict:
    label = pick_label(df, horizon)
    y = df[label]
    n = int(y.notna().sum())
    hnum = label.replace("fwd_", "").replace("d", "")  # '1' | '2' | '3'
    pair_date = (
        df["pair_date"].mode().iloc[0]
        if "pair_date" in df.columns and df["pair_date"].notna().any()
        else "?"
    )
    pred_col = f"prediction_day_{hnum}d"
    leg_col = f"label_date_{hnum}"
    if pred_col in df.columns and df[pred_col].astype(str).str.len().gt(0).any():
        label_date = str(df[pred_col].mode().iloc[0])
    elif leg_col in df.columns and df[leg_col].notna().any():
        label_date = str(df[leg_col].mode().iloc[0])
    else:
        label_date = "?"

    result = {
        "scan_date": scan_date,
        "signal_asof": scan_date,
        "prediction_day": label_date,
        "label": label,
        "n": n,
        "pair_date": pair_date,
        "label_date": label_date,
        "entry_field": "entry_price (Price on signal_asof)",
        "exit_field": f"exit_price_{hnum}d (Price on prediction_day)",
        "features": [],
    }

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

    y_up = y > 0
    y_dn = y < 0
    for col in _feature_cols(df):
        if col == "total_score":
            continue
        ic = _spearman(df[col], y)
        if ic != ic:
            continue
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
    result["interactions"] = interactions

    risk = []
    if "status_extension" in df.columns:
        for state in ("EXTENDED", "EXTREME", "WASHED"):
            m = (df["status_extension"] == state) & y.notna()
            if m.sum() < 20:
                continue
            top = m & (df["total_score"] >= df.loc[m, "total_score"].quantile(0.8)) if "total_score" in df.columns else m
            risk.append({
                "name": state,
                "n": int(m.sum()),
                "mean_fwd": float(y[m].mean()),
                "mean_fwd_if_score_top": float(y[top].mean()) if top.sum() else float("nan"),
            })
    result["risk"] = risk
    return result


def write_ic_csv(scan_date: str, result: dict) -> Path:
    ATTR_DIR.mkdir(parents=True, exist_ok=True)
    path = ATTR_DIR / f"{scan_date}_ic.csv"
    pd.DataFrame(result.get("features") or []).to_csv(path, index=False)
    (ATTR_DIR / f"{scan_date}_summary.json").write_text(
        json.dumps(result, indent=2, default=str), encoding="utf-8")
    return path


def write_md(result: dict) -> Path:
    signal = result.get("signal_asof") or result["scan_date"]
    pred = result.get("prediction_day") or result.get("label_date") or "?"
    pair = result.get("pair_date") or "?"
    L = [
        f"# Factor attribution — signal {signal} → prediction day {pred}",
        "",
        "## Trade window (read this first)",
        "",
        f"| Role | Date | Meaning |",
        f"|------|------|---------|",
        f"| **Signal as-of** | **{signal}** | Features/scores formed from this snapshot "
        f"(and deltas vs **{pair}**). Only data on/before this date. |",
        f"| **Prediction day** | **{pred}** | The trading day the forward return is for "
        f"(exit snapshot). |",
        f"| **Entry price** | Price @ {signal} | Long: buy here; short: sell here. |",
        f"| **Exit price** | Price @ {pred} | Close proxy on prediction day. |",
        f"| **Return column** | `{result['label']}` | Long: exit/entry − 1; short = opposite. |",
        "",
        f"Graded **n={result['n']}** names with valid entry and exit prices.",
        "",
        "Provisional until multiple signal dates agree.",
        "",
        "_Column guide: **IC** = Spearman(feature, long forward return); "
        "**IC↑** / **IC↓** = IC among names that went up / down._",
        "",
    ]
    if "score_ic" in result:
        L.append("## Score calibration (long fwd)")
        L.append(
            f"- Spearman IC(total_score, {result['label']}) = **{result['score_ic']:.4f}**"
        )
        L.append("")
        L.append("| Quintile | Mean long fwd | Hit up>1.5% | n |")
        L.append("|---|---|---|---|")
        for c in result.get("score_calibration", []):
            L.append(
                f"| {c['quintile']} | {c['mean_fwd']*100:.2f}% | "
                f"{c['hit_up']*100:.1f}% | {c['n']} |"
            )
        L.append("")

    L.append("## Top |IC| features")
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
        L.append("| Pattern | n | Mean long fwd | Hit up |")
        L.append("|---|---|---|---|")
        for r in result["interactions"]:
            L.append(
                f"| {r['name']} | {r['n']} | {r['mean_fwd']*100:.2f}% | "
                f"{r['hit_up']*100:.1f}% |"
            )
        L.append("")
    if result.get("risk"):
        L.append("## Risk dominance probes")
        L.append("")
        L.append("| State | n | Mean long fwd | Mean fwd if score top quintile |")
        L.append("|---|---|---|---|")
        for r in result["risk"]:
            mt = r.get("mean_fwd_if_score_top")
            mts = f"{mt*100:.2f}%" if mt == mt else "n/a"
            L.append(
                f"| {r['name']} | {r['n']} | {r['mean_fwd']*100:.2f}% | {mts} |"
            )
        L.append("")

    path = config.DAILY / f"{signal}_attribution.md"
    config.DAILY.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(L), encoding="utf-8")
    return path


def write_candidate_lesson(result: dict) -> Path | None:
    if result["n"] < 100:
        return None
    bullets = []
    ic = result.get("score_ic")
    if ic == ic:
        bullets.append(f"score IC vs {result['label']} = {ic:+.4f}")
    for r in (result.get("features") or [])[:5]:
        bullets.append(f"{r['feature']}: IC={r['ic']:+.4f}")
    if not bullets:
        return None
    LESSONS_CAND.mkdir(parents=True, exist_ok=True)
    path = LESSONS_CAND / f"{result['scan_date']}_lesson.md"
    fm = (
        "---\n"
        f"date: \"{result['scan_date']}\"\n"
        f"signal_asof: \"{result.get('signal_asof')}\"\n"
        f"prediction_day: \"{result.get('prediction_day')}\"\n"
        "status: \"candidate\"\n"
        "---\n\n"
    )
    path.write_text(
        fm + "# Attribution lesson (provisional)\n\n"
        + "\n".join(f"- {b}" for b in bullets) + "\n",
        encoding="utf-8",
    )
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
        print(f"[attr] {scan_date}: label {result['label']} has only {result['n']} rows")
        return
    write_ic_csv(scan_date, result)
    md = write_md(result)
    les = write_candidate_lesson(result)
    print(
        f"[attr] signal_asof={result['signal_asof']} prediction_day={result['prediction_day']} "
        f"label={result['label']} n={result['n']} -> {md}"
        + (f" lesson={les}" if les else "")
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan-date", default=None,
                    help="Signal as-of date (features day), not prediction day")
    ap.add_argument("--horizon", default="auto", choices=["auto", "1d", "2d", "3d"])
    args = ap.parse_args()
    if args.scan_date:
        run(args.scan_date, horizon=args.horizon)
        return
    for lp in sorted(LABELS_DIR.glob("*_fwd.csv")):
        d = lp.name.replace("_fwd.csv", "")
        run(d, horizon=args.horizon)


if __name__ == "__main__":
    main()
