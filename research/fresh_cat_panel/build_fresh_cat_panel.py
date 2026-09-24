"""Research panel: dated catalyst flags (fresh_cat_*) vs live cat_* per ticker-day.

Read-only w.r.t. the live pipeline: recomputes flags from data/snapshots with
src.finviz_delta._add_catalyst_flags; never writes data/features or scores.

Run from repo root:
  python -m research.fresh_cat_panel.build_fresh_cat_panel [--start 2026-08-13] [--end 2026-09-24]
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from src import finviz_delta as fd

OUT = Path(__file__).resolve().parent


def build(start: str, end: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    names = list(fd.CATALYST_PATTERNS)
    cat = [f"cat_{n}" for n in names]
    fresh = [f"{fd.FRESH_PREFIX}{n}" for n in names]
    dates = sorted(p.stem for p in fd.SNAPSHOT_DIR.glob("20??-??-??.csv") if start <= p.stem <= end)
    panels, summ = [], []
    for d in dates:
        df = fd.load_snapshot(fd.SNAPSHOT_DIR / f"{d}.csv")
        asof = fd.snapshot_anchor(df)
        prev = fd.previous_snapshot_anchor(asof)
        lower = prev if prev is not None else asof - pd.Timedelta(hours=fd.FRESH_FALLBACK_H)
        df = fd._add_catalyst_flags(df)
        # fresh_cat_* must be a subset of cat_* (headline is part of the cat_ text)
        for c, f in zip(cat, fresh):
            assert not (df[f] & ~df[c]).any(), (d, f)
        hit = df[df[cat].any(axis=1)].copy()
        hit.insert(0, "scan_date", d)
        hit["snapshot_anchor_et"] = str(asof)
        hit["anchor_source"] = "scrape_ts" if "scrape_ts" in df.columns else "max_news_time"
        hit["fresh_lower_bound_et"] = str(lower)
        hit["lower_bound_source"] = "prev_trading_day_snapshot" if prev is not None else f"fallback_{int(fd.FRESH_FALLBACK_H)}h"
        keep = ["scan_date", "Ticker", "News Time", "news_age_h", "snapshot_anchor_et",
                "anchor_source", "fresh_lower_bound_et", "lower_bound_source"] + cat + fresh
        hit = hit[keep].rename(columns={"News Time": "news_time"})
        hit[cat + fresh] = hit[cat + fresh].astype(int)
        panels.append(hit)
        row = {"scan_date": d, "n_universe": len(df), "snapshot_anchor_et": str(asof),
               "fresh_lower_bound_et": str(lower),
               "lower_bound_source": hit["lower_bound_source"].iloc[0] if len(hit) else ""}
        for n, c, f in zip(names, cat, fresh):
            row[f"{c}"] = int(df[c].sum())
            row[f"{f}"] = int(df[f].sum())
        summ.append(row)
    return pd.concat(panels, ignore_index=True), pd.DataFrame(summ)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="2026-08-13")
    ap.add_argument("--end", default="2026-09-24")
    a = ap.parse_args()
    panel, summ = build(a.start, a.end)
    tag = f"{a.start}_{a.end}"
    panel.to_csv(OUT / f"fresh_cat_panel_{tag}.csv", index=False)
    summ.to_csv(OUT / f"fresh_cat_daily_counts_{tag}.csv", index=False)
    print(f"panel rows={len(panel)} dates={summ.scan_date.nunique()} -> {OUT}")


if __name__ == "__main__":
    main()
