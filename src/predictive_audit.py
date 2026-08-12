"""Cross-date predictive audit: accuracy + factor ICs + pairwise combinations.

Pools every signal date that has labels. Answers:
  1. Overall score direction accuracy (full universe)
  2. Which single factors (levels / deltas) correlate with forward returns
  3. Which simple combinations (A up & B down, etc.) show a return edge

CLI: python -m src.predictive_audit [--horizon 1d]

Writes:
  03_scoreboard/predictive_audit.md
  03_scoreboard/predictive_audit_<horizon>.md
  03_scoreboard/predictive_audit.json
"""
from __future__ import annotations

import argparse
import itertools
import json
from datetime import datetime
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from . import config

FEATURES_DIR = config.DATA / "features"
LABELS_DIR = config.DATA / "labels"
OUT_DIR = config.SCOREBOARD_DIR
MIN_N = 50

SKIP = {
    "Ticker", "Company", "Sector", "Industry", "Index", "scan_date", "pair_date",
    "n_universe", "price_then", "true_ret_dir", "score_100", "confidence", "ret_H",
    "status_extension", "status_trend", "status_short", "status_street", "kill_flags",
    "mcap_bucket", "beta_bucket", "entry_price", "signal_asof", "_signal",
}

SKIP_PREFIXES = (
    "fwd_", "label_date_", "price_T", "prediction_day", "exit_price",
    "short_fwd", "dir_",
)


def _spearman(a: pd.Series, b: pd.Series) -> float:
    a = pd.to_numeric(a, errors="coerce")
    b = pd.to_numeric(b, errors="coerce")
    m = a.notna() & b.notna()
    if m.sum() < MIN_N:
        return float("nan")
    aa, bb = a[m], b[m]
    if aa.nunique(dropna=True) < 2 or bb.nunique(dropna=True) < 2:
        return float("nan")
    try:
        return float(aa.rank().corr(bb.rank()))
    except Exception:
        return float("nan")


def _is_usable_numeric(s: pd.Series) -> bool:
    if s.dtype == object or str(s.dtype) == "string":
        # try coerce — keep only if enough numbers
        num = pd.to_numeric(s, errors="coerce")
        return int(num.notna().sum()) >= MIN_N and num.nunique(dropna=True) >= 2
    if not np.issubdtype(s.dtype, np.number):
        return False
    return int(s.notna().sum()) >= MIN_N and s.nunique(dropna=True) >= 2


def _factor_cols(df: pd.DataFrame) -> list[str]:
    cols = []
    for c in df.columns:
        if c in SKIP:
            continue
        if any(c.startswith(p) for p in SKIP_PREFIXES):
            continue
        if c in ("up_3d", "down_3d"):
            continue
        try:
            if _is_usable_numeric(df[c]):
                cols.append(c)
        except Exception:
            continue
    return cols


def _num(df: pd.DataFrame, col: str) -> pd.Series:
    return pd.to_numeric(df[col], errors="coerce")


def _load_joined(signal: str) -> pd.DataFrame | None:
    fp = FEATURES_DIR / f"{signal}_1d.csv"
    lp = LABELS_DIR / f"{signal}_fwd.csv"
    if not fp.exists() or not lp.exists():
        return None
    f = pd.read_csv(fp, low_memory=False)
    l = pd.read_csv(lp, low_memory=False)
    j = f.merge(l, on="Ticker", how="inner", suffixes=("", "_lbl"))
    # single assign avoids fragmentation warning from repeated inserts
    j = j.assign(_signal=signal)
    return j


def _score_accuracy(j: pd.DataFrame, y: pd.Series) -> dict:
    if "total_score" not in j.columns:
        return {}
    score = _num(j, "total_score")
    y = pd.to_numeric(y, errors="coerce")
    m = y.notna() & score.notna()
    score, y2 = score[m], y[m]
    exp_up = score > 2
    exp_dn = score < -2
    act = exp_up | exp_dn
    hit = pd.Series(np.nan, index=score.index, dtype=float)
    hit.loc[exp_up] = (y2.loc[exp_up] > 0).astype(float)
    hit.loc[exp_dn] = (y2.loc[exp_dn] < 0).astype(float)
    h = hit.loc[act].dropna()
    return {
        "n": int(m.sum()),
        "n_actionable": int(act.sum()),
        "accuracy": float(h.mean()) if len(h) else float("nan"),
        "accuracy_long": float(hit.loc[exp_up].mean()) if exp_up.any() else float("nan"),
        "accuracy_short": float(hit.loc[exp_dn].mean()) if exp_dn.any() else float("nan"),
        "ic": _spearman(score, y2),
    }


def _combo_edge(df: pd.DataFrame, a: str, b: str, y: pd.Series) -> list[dict]:
    out = []
    sa = _num(df, a)
    sb = _num(df, b)
    y = pd.to_numeric(y, errors="coerce")
    for sga, sgb, name in (
        (1, 1, f"{a}↑ & {b}↑"),
        (1, -1, f"{a}↑ & {b}↓"),
        (-1, 1, f"{a}↓ & {b}↑"),
        (-1, -1, f"{a}↓ & {b}↓"),
    ):
        ma = sa > 0 if sga > 0 else sa < 0
        mb = sb > 0 if sgb > 0 else sb < 0
        m = ma & mb & y.notna()
        if int(m.sum()) < MIN_N:
            continue
        yy = y[m]
        out.append({
            "combo": name,
            "n": int(m.sum()),
            "mean_fwd": float(yy.mean()),
            "hit_up": float((yy > 0).mean()),
            "hit_down": float((yy < 0).mean()),
        })
    return out


def run(horizon: str = "1d") -> dict:
    lab = f"fwd_{horizon}"
    signals = sorted(p.name.replace("_fwd.csv", "") for p in LABELS_DIR.glob("*_fwd.csv"))
    frames = []
    per_date_acc = []
    for s in signals:
        j = _load_joined(s)
        if j is None or lab not in j.columns:
            continue
        y = pd.to_numeric(j[lab], errors="coerce")
        if int(y.notna().sum()) < MIN_N:
            continue
        acc = _score_accuracy(j, y)
        acc["signal_asof"] = s
        per_date_acc.append(acc)
        frames.append(j)

    if not frames:
        print("[audit] no labeled joins")
        return {}

    all_df = pd.concat(frames, ignore_index=True, copy=False)
    y_all = pd.to_numeric(all_df[lab], errors="coerce")
    overall = _score_accuracy(all_df, y_all)

    fcols = _factor_cols(all_df)
    factor_rows = []
    for c in fcols:
        series = _num(all_df, c)
        ic = _spearman(series, y_all)
        if ic != ic:
            continue
        pos = (series > 0) & y_all.notna()
        neg = (series < 0) & y_all.notna()
        mu = float(y_all[pos].mean()) if int(pos.sum()) else float("nan")
        md = float(y_all[neg].mean()) if int(neg.sum()) else float("nan")
        spread = (mu - md) if (mu == mu and md == md) else float("nan")
        factor_rows.append({
            "factor": c,
            "ic": ic,
            "n": int((series.notna() & y_all.notna()).sum()),
            "mean_fwd_when_up": mu,
            "mean_fwd_when_down": md,
            "spread": spread,
        })
    factor_rows.sort(key=lambda r: abs(r["ic"]), reverse=True)

    cand = [r["factor"] for r in factor_rows[:12]]
    preferred = [
        c for c in cand
        if c.startswith("d_") or c in (
            "total_score", "Relative Volume", "true_ret",
            "Relative Strength Index (14)",
        )
    ]
    if len(preferred) < 4:
        preferred = cand[:8]
    combo_rows = []
    for a, b in itertools.combinations(preferred[:8], 2):
        combo_rows.extend(_combo_edge(all_df, a, b, y_all))
    for r in combo_rows:
        r["score"] = abs(r["mean_fwd"]) * float(np.sqrt(r["n"]))
    combo_rows.sort(key=lambda r: r["score"], reverse=True)

    report = {
        "generated_at": datetime.now(ZoneInfo(config.TZ)).isoformat(),
        "horizon": horizon,
        "n_signal_dates": len(per_date_acc),
        "signal_dates": [p["signal_asof"] for p in per_date_acc],
        "overall_score_accuracy": overall,
        "per_date_accuracy": per_date_acc,
        "top_factors": factor_rows[:40],
        "top_combinations": combo_rows[:30],
    }
    _write_md(report)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"predictive_audit_{horizon}.json").write_text(
        json.dumps(report, indent=2, default=str), encoding="utf-8")
    if horizon == "1d":
        (OUT_DIR / "predictive_audit.json").write_text(
            json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(f"[audit] wrote predictive_audit_{horizon}.md "
          f"(factors={len(factor_rows)} combos={len(combo_rows)})")
    return report


def _pct(x) -> str:
    if x is None or (isinstance(x, float) and x != x):
        return "n/a"
    return f"{100 * float(x):.1f}%"


def _write_md(report: dict) -> None:
    o = report.get("overall_score_accuracy") or {}
    h = report["horizon"]
    L = [
        f"# Predictive audit — horizon **{h}**",
        "",
        f"Generated: {report['generated_at']}",
        f"Signal dates pooled: **{report['n_signal_dates']}** "
        f"(`{', '.join(report['signal_dates'])}`)",
        "",
        "## 1. Prediction accuracy (composite `total_score`, full universe)",
        "",
        "Rule: score > +2 → expect UP; score < −2 → expect DOWN; else neutral.",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Names graded | {o.get('n')} |",
        f"| Actionable (|score|>2) | {o.get('n_actionable')} |",
        f"| **Accuracy (actionable)** | **{_pct(o.get('accuracy'))}** |",
        f"| Long accuracy | {_pct(o.get('accuracy_long'))} |",
        f"| Short accuracy | {_pct(o.get('accuracy_short'))} |",
        f"| Spearman IC(score, fwd) | "
        + (f"{o['ic']:+.4f}" if o.get("ic") == o.get("ic") else "n/a") + " |",
        "",
        "### Per signal date",
        "",
        "| Signal | n | Actionable | Accuracy | Long | Short | IC |",
        "|--------|---|------------|----------|------|-------|----|",
    ]
    for p in report["per_date_accuracy"]:
        ic = p.get("ic")
        ic_s = f"{ic:+.4f}" if ic == ic else "n/a"
        L.append(
            f"| {p['signal_asof']} | {p.get('n')} | {p.get('n_actionable')} | "
            f"{_pct(p.get('accuracy'))} | {_pct(p.get('accuracy_long'))} | "
            f"{_pct(p.get('accuracy_short'))} | {ic_s} |"
        )

    L += [
        "",
        "## 2. Top correlating factors (pooled across dates)",
        "",
        "IC = Spearman(factor, forward return). Ranked by |IC|. "
        "Spread = mean fwd when factor>0 minus mean fwd when factor<0.",
        "",
        "| Rank | Factor | IC | n | Mean fwd if ↑ | Mean fwd if ↓ | Spread |",
        "|------|--------|----|---|---------------|---------------|--------|",
    ]
    for i, r in enumerate(report["top_factors"][:25], 1):
        if r.get("spread") == r.get("spread"):
            L.append(
                f"| {i} | {r['factor']} | {r['ic']:+.4f} | {r['n']} | "
                f"{r['mean_fwd_when_up']*100:+.2f}% | "
                f"{r['mean_fwd_when_down']*100:+.2f}% | "
                f"{r['spread']*100:+.2f}% |"
            )
        else:
            L.append(
                f"| {i} | {r['factor']} | {r['ic']:+.4f} | {r['n']} | n/a | n/a | n/a |"
            )

    L += [
        "",
        "## 3. Factor combinations (sign quadrants)",
        "",
        "Among stronger single factors: A↑B↑ / A↑B↓ / A↓B↑ / A↓B↓. "
        "**Score** = |mean_fwd| × √n (ranking aid only).",
        "",
        "| Rank | Combination | n | Mean fwd | % up | % down | Score |",
        "|------|-------------|---|----------|------|--------|-------|",
    ]
    for i, r in enumerate(report["top_combinations"][:20], 1):
        L.append(
            f"| {i} | {r['combo']} | {r['n']} | {r['mean_fwd']*100:+.2f}% | "
            f"{r['hit_up']*100:.1f}% | {r['hit_down']*100:.1f}% | {r['score']:.3f} |"
        )

    L += [
        "",
        "## Notes",
        "",
        "- With few signal dates, treat rankings as **exploratory**.",
        "- `d_*` = day-over-day delta on the signal pair; bare names = levels.",
        f"- JSON: `03_scoreboard/predictive_audit_{h}.json`",
        "",
    ]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    body = "\n".join(L)
    (OUT_DIR / f"predictive_audit_{h}.md").write_text(body, encoding="utf-8")
    if h == "1d":
        (OUT_DIR / "predictive_audit.md").write_text(body, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--horizon", default="1d", choices=["1d", "2d", "3d"])
    args = ap.parse_args()
    run(horizon=args.horizon)


if __name__ == "__main__":
    main()
