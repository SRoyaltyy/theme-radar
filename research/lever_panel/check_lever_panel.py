#!/usr/bin/env python3
"""Clock check for the 09:30-knowable Finviz lever panel. Exit 0 = pass.

For EVERY row asserts:
  * trade_date is an NYSE trading day, snapshot_date == previous trading day;
  * 16:00 ET(snapshot_date) < scrape_ts_utc < 09:30 ET(trade_date);
  * snapshot_commit_ts_utc and every tr_*_commit_ts_utc (when present)
    < 09:30 ET(trade_date), i.e. the data was in the repo before the open;
  * where the source snapshot has a scrape_ts column, scrape_ts_utc equals it;
  * one row per (Ticker, trade_date); no outcome / forward-return columns;
  * file sha256 matches panel_meta.json.
Run: python -m research.lever_panel.check_lever_panel
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import date, datetime, time
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from src.trading_calendar import is_trading_day, previous_trading_day  # noqa: E402

ET = ZoneInfo("America/New_York")
HERE = Path(__file__).resolve().parent
FORBIDDEN = re.compile(r"(^|_)(fwd|forward_ret|label|outcome|exit_|entry_|future|next_)", re.I)


def main() -> int:
    meta = json.loads((HERE / "panel_meta.json").read_text())
    fails: list[str] = []
    n_rows = 0
    dates: set[str] = set()
    for f in meta["files"]:
        p = ROOT / f["file"]
        sha = hashlib.sha256(p.read_bytes()).hexdigest()
        if sha != f["sha256"]:
            fails.append(f"{p.name}: sha256 {sha} != meta {f['sha256']}")
        df = pd.read_csv(p, dtype=str, keep_default_na=False, na_values=[""])
        n_rows += len(df)
        bad_cols = [c for c in df.columns if FORBIDDEN.search(c)]
        if bad_cols:
            fails.append(f"{p.name}: outcome-like columns {bad_cols}")
        if df.duplicated(["Ticker", "trade_date"]).any():
            fails.append(f"{p.name}: duplicate (Ticker, trade_date)")
        scrape = pd.to_datetime(df["scrape_ts_utc"], utc=True, errors="coerce")
        if scrape.isna().any():
            fails.append(f"{p.name}: {int(scrape.isna().sum())} rows without scrape_ts_utc")
        commit_cols = ["snapshot_commit_ts_utc"] + [c for c in df.columns
                                                     if c.startswith("tr_") and c.endswith("_commit_ts_utc")]
        for td, g in df.groupby("trade_date"):
            dates.add(td)
            T = date.fromisoformat(td)
            if not is_trading_day(T):
                fails.append(f"{td}: not a trading day")
            D = previous_trading_day(T)
            if set(g["snapshot_date"]) != {D.isoformat()}:
                fails.append(f"{td}: snapshot_date {sorted(set(g['snapshot_date']))} != {D}")
            lo = pd.Timestamp(datetime.combine(D, time(16, 0), ET))
            hi = pd.Timestamp(datetime.combine(T, time(9, 30), ET))
            s = scrape.loc[g.index]
            nb = int(((s <= lo) | (s >= hi)).sum())
            if nb:
                fails.append(f"{td}: {nb} rows scrape_ts outside ({lo}, {hi})")
            for c in commit_cols:
                ct = pd.to_datetime(g[c], utc=True, errors="coerce").dropna()
                nb = int((ct >= hi).sum())
                if nb:
                    fails.append(f"{td}: {nb} rows {c} not before {hi}")
            if g["snapshot_commit_ts_utc"].isna().any():
                fails.append(f"{td}: missing snapshot_commit_ts_utc")
            snap = ROOT / "data" / "snapshots" / f"{D.isoformat()}.csv"
            hdr = pd.read_csv(snap, nrows=0).columns
            if "scrape_ts" in hdr:
                st = pd.to_datetime(pd.read_csv(snap, usecols=["scrape_ts"])["scrape_ts"], utc=True).max()
                if not (s == st).all():
                    fails.append(f"{td}: scrape_ts_utc != scrape_ts column in {snap.name}")
    if n_rows != meta["rows"]:
        fails.append(f"row count {n_rows} != meta {meta['rows']}")
    skipped = {s["trade_date"] for s in meta["skipped"]}
    if dates & skipped:
        fails.append(f"skipped dates present: {sorted(dates & skipped)}")
    if fails:
        print("[check_lever_panel] FAIL")
        for x in fails:
            print("  -", x)
        return 1
    print(f"[check_lever_panel] PASS: {n_rows} rows, {len(dates)} trade dates "
          f"{min(dates)}..{max(dates)}; every scrape_ts_utc is after 16:00 ET of the prior "
          f"trading day and before 09:30 ET of trade_date; all source commits precede 09:30 ET; "
          f"skipped (no snapshot, not filled): {sorted(skipped)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
