#!/usr/bin/env python3
"""DST-safe gate for the nightly chain (finviz -> score_delta -> composite).

GitHub cron is UTC-only, so each workflow has a summer slot and a slot one hour
later (winter). Every slot runs this gate; at most one slot per ET day does
real work, the other is a no-op:

  finviz     trading day, ET now >= 16:00 (real close), and today's snapshot is
             not already in with a post-close scrape time (close_is_in).
  score      trading day, today's snapshot is in after the close, and today has
             not been scored yet (data/features/<today>_1d.csv absent).
  composite  trading day, today's snapshot is in after the close, and today's
             composite is not recorded yet (01_daily/<today>_composite_rank.md).

Manual runs (workflow_dispatch): finviz keeps only the trading-day gate (as
before); score and composite always run.

Summer (EDT): finviz 20:30 UTC = 16:30 ET runs; 21:30 UTC sees today's
snapshot and skips. Winter (EST): 20:30 UTC = 15:30 ET skips (pre-close);
21:30 UTC = 16:30 ET runs; score/composite follow in their later slots.

Prints the decision and writes trading=true|false (+ et_date) to $GITHUB_OUTPUT.
Usage: python scripts/schedule_gate.py finviz|score|composite --event EVENT
"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, time
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src import history_guard as hg  # noqa: E402
from src.trading_calendar import is_trading_day  # noqa: E402


def decide(job: str, event: str, now_et: datetime, root: Path = ROOT) -> tuple[bool, str]:
    d = now_et.date()
    day = d.isoformat()
    manual = event != "schedule"
    if manual and job in ("score", "composite"):
        return True, f"{event}: manual run always proceeds"
    if not is_trading_day(d):
        return False, f"{day} is not a US trading day"
    if manual:
        return True, f"{event}: trading day"
    snap_ok, why = hg.close_is_in(root / "data/snapshots", day)
    if job == "finviz":
        if now_et.time() < time(16, 0):
            return False, f"{now_et:%H:%M} ET is before the 16:00 close (other slot fetches)"
        if snap_ok:
            return False, f"today's snapshot already in after the close ({why})"
        return True, f"fetch: {why}"
    if not snap_ok:
        return False, f"today's snapshot not in after the close yet ({why})"
    done = (root / f"data/features/{day}_1d.csv" if job == "score"
            else root / f"01_daily/{day}_composite_rank.md")
    if done.exists():
        return False, f"{done.relative_to(root)} already recorded today (other slot ran)"
    return True, f"run: {why}"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("job", choices=["finviz", "score", "composite"])
    ap.add_argument("--event", default="schedule")
    a = ap.parse_args(argv)
    now = datetime.now(ZoneInfo("America/New_York"))
    run, why = decide(a.job, a.event, now)
    print(f"[gate] {a.job} event={a.event} ET={now:%Y-%m-%d %H:%M} run={run}: {why}")
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a") as fh:
            fh.write(f"trading={str(run).lower()}\n")
            fh.write(f"et_date={now.date().isoformat()}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
