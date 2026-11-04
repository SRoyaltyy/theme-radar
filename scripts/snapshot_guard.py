#!/usr/bin/env python3
"""Safety net for the daily Finviz snapshot (finviz_daily + finviz_alarm).

  exists  Has data/snapshots/<D>.raw.csv (D = today's NY session date) already
          landed on origin/main (or the checkout)? Writes exists=true|false to
          $GITHUB_OUTPUT. finviz_daily runs this FIRST and stops if true: the
          snapshot rotates current.csv -> previous.csv, so it must never run
          twice for the same day (backup cron slots rely on this).
  alarm   On a US trading day at/after 18:00 ET, exit 1 if <D>.raw.csv is
          missing, or byte-identical to the previous trading day's raw file.
          Non-trading days / earlier slots are a no-op (exit 0).

Usage: python scripts/snapshot_guard.py exists|alarm [--date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import sys
from datetime import date, datetime, time
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.trading_calendar import is_trading_day, previous_trading_day  # noqa: E402

ALARM_AFTER = time(17, 55)


def raw_rel(day: str) -> str:
    return f"data/snapshots/{day}.raw.csv"


def _git_blob(root: Path, rel: str, ref: str = "origin/main") -> bytes | None:
    try:
        r = subprocess.run(["git", "-C", str(root), "show", f"{ref}:{rel}"],
                           capture_output=True, check=False)
    except FileNotFoundError:
        return None
    return r.stdout if r.returncode == 0 else None


def read_raw(root: Path, day: str) -> bytes | None:
    """Bytes of <day>.raw.csv from origin/main, else the working tree, else None."""
    blob = _git_blob(root, raw_rel(day))
    if blob is not None:
        return blob
    p = root / raw_rel(day)
    return p.read_bytes() if p.exists() else None


def snapshot_exists(root: Path, day: str) -> bool:
    return read_raw(root, day) is not None


def alarm_check(root: Path, now_et: datetime) -> tuple[bool, str]:
    """(ok, message). ok=False means the alarm should fire."""
    d = now_et.date()
    day = d.isoformat()
    if not is_trading_day(d):
        return True, f"{day} is not a US trading day"
    if now_et.time() < ALARM_AFTER:
        return True, f"{now_et:%H:%M} ET is before 18:00 (other slot checks)"
    cur = read_raw(root, day)
    if cur is None:
        return False, f"{raw_rel(day)} is MISSING on main at {now_et:%H:%M} ET"
    prev_day = previous_trading_day(d).isoformat()
    prev = read_raw(root, prev_day)
    if prev is not None and hashlib.sha256(prev).digest() == hashlib.sha256(cur).digest():
        return False, (f"{raw_rel(day)} is byte-identical to {raw_rel(prev_day)} "
                       "(frozen feed?)")
    return True, f"{raw_rel(day)} present ({len(cur)} bytes), differs from {prev_day}"


def _out(**kv: str) -> None:
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a") as fh:
            for k, v in kv.items():
                fh.write(f"{k}={v}\n")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["exists", "alarm"])
    ap.add_argument("--date", help="override NY date (testing)")
    a = ap.parse_args(argv)
    now = datetime.now(ZoneInfo("America/New_York"))
    if a.date:
        now = datetime.combine(date.fromisoformat(a.date), time(18, 0),
                               tzinfo=ZoneInfo("America/New_York"))
    day = now.date().isoformat()
    if a.cmd == "exists":
        ex = snapshot_exists(ROOT, day)
        print(f"[guard] {raw_rel(day)} on main: {ex}"
              + (" -> skipping, never snapshot twice" if ex else ""))
        _out(exists=str(ex).lower(), et_date=day)
        return 0
    ok, msg = alarm_check(ROOT, now)
    print(f"[alarm] {'OK' if ok else 'FAIL'}: {msg}")
    _out(ok=str(ok).lower(), message=msg, et_date=day)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
