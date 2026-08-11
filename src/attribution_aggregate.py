"""Aggregate factor report — pools factor ICs across ALL scan dates.

Single-date attribution (src/attribution.py) is provisional by design; this
module answers the durable questions:
  1. Which Finviz columns (levels AND day-over-day deltas) are most
     correlated with UP moves and with DOWN moves, consistently across dates?
  2. Is the composite score getting better or worse, per horizon, per date?

Method (per horizon h in 1d/2d/3d):
  * for each scan date with >=30 valid labels: Spearman IC of every numeric
    feature column vs fwd_<h>d, plus the mean forward return when the
    feature is positive vs negative (the "spread")
  * across dates: IC mean, IC std, ICIR (= mean/std), sign consistency
    (fraction of dates where the IC sign matches the mean sign)
  * a factor is only called "consistent" when n_dates >= 2 and sign
    consistency >= 2/3 — anything else is explicitly labelled noise-prone.

Outputs:
  03_scoreboard/factor_report.json   full machine-readable tables
  03_scoreboard/factor_report.md     human report with exact date spans

CLI: python -m src.attribution_aggregate
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from . import config

FEATURES_DIR = config.DATA / "features"
LABELS_DIR = config.DATA / "labels"
OUT_DIR = config.SCOREBOARD_DIR
HORIZONS = ("1d", "2d", "3d")
MIN_ROWS = 30

# columns never treated as factors
NON_FACTOR = {"Ticker", "Company", "Sector", "Industry", "Index", "scan_date",
              "pair_date", "n_universe", "price_then", "true_ret_dir",
              "score_100", "confidence", "ret_H", "status_extension",
              "status_trend", "status_short", "status_street", "kill_flags",
              "mcap_bucket", "beta_bucket"}
# suffixes that are direction labels, not values
EXCLUDE_PREFIXES = ("dir_",)


def _spearman(a: pd.Series, b: pd.Series) -> float:
    m = a.notna() & b.notna()
    if m.sum() < MIN_ROWS:
        return float("nan")
    return float(a[m].rank().corr(b[m].rank()))


def _factor_cols(df: pd.DataFrame) -> list[str]:
    cols = []
    for c in df.columns:
        if c in NON_FACTOR or c.startswith(EXCLUDE_PREFIXES):
            continue
        if df[c].dtype == object:
            continue
        if c.startswith("fwd_") or c.startswith("label_date_") \
                or c.startswith("price_T") or c in ("up_3d", "down_3d"):
            continue
        cols.append(c)
    return cols


def _per_date_ics(scan_date: str) -> dict | None:
    fp = FEATURES_DIR / f"{scan_date}_1d.csv"
    lp = LABELS_DIR / f"{scan_date}_fwd.csv"
    if not fp.exists() or not lp.exists():
        return None
    f = pd.read_csv(fp, low_memory=False)
    l = pd.read_csv(lp, low_memory=False)
    j = f.merge(l, on="Ticker", how="inner", suffixes=("", "_lbl"))
    cols = _factor_cols(j)
    pair_date = (j["pair_date"].mode().iloc[0]
                 if "pair_date" in j.columns and j["pair_date"].notna().any()
                 else None)
    out = {"scan_date": scan_date, "pair_date": pair_date, "horizons": {}}
    for h in HORIZONS:
        lab = f"fwd_{h}"
        ldc = f"label_date_{h[-2]}"
        y = j[lab] if lab in j.columns else pd.Series(dtype=float)
        if y.notna().sum() < MIN_ROWS:
            continue
        label_date = (j[ldc].mode().iloc[0]
                      if ldc in j.columns and j[ldc].notna().any() else None)
        feats = {}
        for c in cols:
            ic = _spearman(j[c], y)
            if ic != ic:
                continue
            pos = (j[c] > 0) & y.notna()
            neg = (j[c] < 0) & y.notna()
            feats[c] = {
                "ic": ic,
                "mean_fwd_pos": float(y[pos].mean()) if pos.sum() else float("nan"),
                "mean_fwd_neg": float(y[neg].mean()) if neg.sum() else float("nan"),
            }
        out["horizons"][h] = {
            "label_date": label_date, "n": int(y.notna().sum()),
            "n_up": int((y > 0).sum()), "n_down": int((y < 0).sum()),
            "features": feats,
        }
    return out


def _aggregate(per_date: list[dict]) -> dict:
    """feature -> horizon -> {mean_ic, std, icir, sign_consistency, ...}"""
    agg: dict[str, dict[str, dict]] = {}
    for h in HORIZONS:
        by_feat: dict[str, list[dict]] = {}
        for pd_ in per_date:
            hz = pd_["horizons"].get(h)
            if not hz:
                continue
            for feat, st in hz["features"].items():
                by_feat.setdefault(feat, []).append(st)
        table = {}
        for feat, rows in by_feat.items():
            ics = np.array([r["ic"] for r in rows], dtype=float)
            ics = ics[~np.isnan(ics)]
            if len(ics) == 0:
                continue
            mean = float(ics.mean())
            std = float(ics.std(ddof=0))
            if mean == 0:
                sign_cons = 0.0
            else:
                sign_cons = float((np.sign(ics) == np.sign(mean)).mean())
            spreads = [r["mean_fwd_pos"] - r["mean_fwd_neg"] for r in rows
                       if r["mean_fwd_pos"] == r["mean_fwd_pos"]
                       and r["mean_fwd_neg"] == r["mean_fwd_neg"]]
            table[feat] = {
                "mean_ic": mean,
                "std_ic": std,
                "icir": (mean / std) if std > 0 else float("nan"),
                "sign_consistency": sign_cons,
                "n_dates": int(len(ics)),
                "mean_spread": float(np.mean(spreads)) if spreads else float("nan"),
                "consistent": bool(len(ics) >= 2 and sign_cons >= 2 / 3),
            }
        agg[h] = table
    return agg


def _md(report: dict) -> str:
    L = ["# Factor report — multi-date aggregate", "",
         f"_Generated {datetime.now(ZoneInfo(config.TZ)).strftime('%Y-%m-%d %H:%M %Z')} "
         f"from {report['n_scan_dates']} scan dates._", "",
         "How to read: **IC** = Spearman rank correlation between the factor "
         "and the forward return, computed per scan date then averaged "
         "(mean IC). **ICIR** = mean/std across dates — the consistency "
         "score; |ICIR| above ~0.5 with sign consistency ≥ 2/3 is what we "
         "call a real signal. **spread** = average forward return when the "
         "factor is positive minus when negative. Factors marked ⚠️ flips "
         "sign between dates — treat as noise.", ""]

    L += ["## Coverage (exact date spans)", "",
          "| Scan date (features) | Deltas vs | 1d label | 2d label | "
          "3d label | Stocks |", "|---|---|---|---|---|---|"]
    for d in report["per_date"]:
        hz = d["horizons"]
        def ld(h):
            return hz.get(h, {}).get("label_date") or "—"
        n = max((hz.get(h, {}).get("n", 0) for h in HORIZONS), default=0)
        L.append(f"| {d['scan_date']} | {d.get('pair_date') or '—'} | "
                 f"{ld('1d')} | {ld('2d')} | {ld('3d')} | {n} |")
    L.append("")

    L += ["## Composite score effectiveness (total_score IC)", "",
          "| Scan date | 1d IC | 2d IC | 3d IC |", "|---|---|---|---|"]
    for d in report["per_date"]:
        row = [d["scan_date"]]
        for h in HORIZONS:
            st = d["horizons"].get(h, {}).get("features", {}).get("total_score")
            row.append(f"{st['ic']:+.4f}" if st else "—")
        L.append("| " + " | ".join(row) + " |")
    for h in HORIZONS:
        ts = report["aggregate"].get(h, {}).get("total_score")
        if ts:
            L.append(f"- **{h}**: mean IC **{ts['mean_ic']:+.4f}**, "
                     f"ICIR {ts['icir'] if ts['icir']==ts['icir'] else float('nan'):+.2f}, "
                     f"sign consistency {ts['sign_consistency']*100:.0f}% "
                     f"over {ts['n_dates']} dates")
    L.append("")

    for h in HORIZONS:
        table = report["aggregate"].get(h, {})
        if not table:
            continue
        rows = sorted(table.items(), key=lambda kv: abs(kv[1]["mean_ic"]),
                      reverse=True)
        L += [f"## Factor ranking — {h} forward returns", "",
              "| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | "
              "Verdict |", "|---|---|---|---|---|---|---|"]
        for feat, st in rows[:30]:
            verdict = ("✅ consistent" if st["consistent"]
                       else "⚠️ flips / too few dates")
            sp = st["mean_spread"]
            sp_s = f"{sp * 100:+.2f}%" if sp == sp else "n/a"
            L.append(
                f"| {feat} | {st['mean_ic']:+.4f} | "
                f"{st['icir'] if st['icir']==st['icir'] else float('nan'):+.2f} | "
                f"{st['sign_consistency']*100:.0f}% | {st['n_dates']} | "
                f"{sp_s} | {verdict} |")
        L.append("")

    L += ["## What to do with this", "",
          "- ✅ consistent factors with positive IC → candidates to ADD or "
          "UP-WEIGHT in the rubric (weight_learner handles rubric fields "
          "automatically).",
          "- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or "
          "invert.",
          "- ⚠️ flips → leave alone; single-date heroes are usually noise.",
          "- `d_*` columns are day-over-day deltas; bare names are levels; "
          "`cat_*` are catalyst keyword flags (0/1).", ""]
    return "\n".join(L)


def main() -> None:
    feat_dates = sorted(p.stem.replace("_1d", "")
                        for p in FEATURES_DIR.glob("*_1d.csv"))
    per_date = []
    for d in feat_dates:
        r = _per_date_ics(d)
        if r and r["horizons"]:
            per_date.append(r)
            print(f"[agg] {d}: horizons {list(r['horizons'])}")
    if not per_date:
        print("[agg] no labeled dates yet — nothing to aggregate")
        return

    report = {"generated_at": datetime.now(ZoneInfo(config.TZ)).isoformat(),
              "n_scan_dates": len(per_date),
              "per_date": per_date,
              "aggregate": _aggregate(per_date)}

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "factor_report.json").write_text(
        json.dumps(report, indent=2, default=str), encoding="utf-8")
    (OUT_DIR / "factor_report.md").write_text(_md(report) + "\n",
                                              encoding="utf-8")
    print(f"[agg] wrote {OUT_DIR / 'factor_report.md'} "
          f"({len(per_date)} dates)")


if __name__ == "__main__":
    main()
