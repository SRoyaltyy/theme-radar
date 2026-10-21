"""Fetch Finviz Elite screener CSV via the official export endpoint.

Preferred: set secret FINVIZ_EXPORT to the full export URL that already
includes your auth key (the single link Finviz gives you).

Writes (append-only history):
  data/snapshots/YYYY-MM-DD.csv          ← canonical snapshot for that ET date
  data/snapshots/archive/YYYY-MM-DD_HHMMSS.csv  ← every run (dated file is add-only; pre-close runs archive only)
  data/snapshots/current.csv / previous.csv     ← convenience pointers only
  data/snapshots/manifest.json                  ← runs[].scrape_ts_utc = export time

Dated CSV columns: META + numeric fields, then News URL, scrape_ts (UTC), Open
appended at the end, in that order. News URL/scrape_ts are present from the
2026-09-24 rerun; Open (Finviz day open, column id 86) from 2026-09-25 on.
Older files lack them. The FINVIZ_EXPORT secret URL already exports "Open"
(seen in every committed *.raw.csv); DEFAULT_COLS below is only the fallback.

IMPORTANT: dated files are NEVER deleted. Same-day re-fetch archives the
old file under archive/ before replacing YYYY-MM-DD.csv.
"""
from __future__ import annotations

import os
import shutil
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

from .finviz_delta import SNAPSHOT_DIR, normalize_frame

DEFAULT_COLS = (
    "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,"
    "26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,"
    "49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,"
    "86"  # 86 = Open (day open price)
)

EXPORT_URL = "https://elite.finviz.com/export.ashx"
ARCHIVE_DIR = SNAPSHOT_DIR / "archive"


def fetch_csv(api_key: str | None = None, extra_params: dict | None = None) -> bytes:
    full = (
        os.environ.get("FINVIZ_EXPORT", "")
        or os.environ.get("FINVIZ_EXPORT_URL", "")
    ).strip()

    key = (api_key or os.environ.get("FINVIZ_API_KEY", "")).strip()

    if full:
        url = full
        if key and "auth=" not in url:
            sep = "&" if "?" in url else "?"
            url = f"{url}{sep}auth={key}"
        params = None
    else:
        if not key:
            raise SystemExit(
                "Set FINVIZ_EXPORT (full link+auth) or FINVIZ_API_KEY."
            )
        url = EXPORT_URL
        params = {
            "v": os.environ.get("FINVIZ_VIEW", "152"),
            "c": os.environ.get("FINVIZ_COLS", DEFAULT_COLS),
            "auth": key,
        }
        if extra_params:
            params.update(extra_params)

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (compatible; theme-radar/1.0; "
            "+https://github.com/SRoyaltyy/theme-radar)"
        ),
    }
    r = requests.get(url, params=params, headers=headers, timeout=180)
    r.raise_for_status()
    head = r.content[:800]
    if not r.content or (b"Ticker" not in head and b"ticker" not in head):
        raise RuntimeError(
            "Finviz export did not return a CSV with Ticker header. "
            f"Status={r.status_code}, bytes={len(r.content)}, "
            f"start={head[:120]!r}"
        )
    return r.content


def _archive_if_exists(path: Path, stamp: str) -> Path | None:
    """If path exists, copy to archive/ with timestamp. Never delete the original
    until the caller replaces it; archive is the safety copy."""
    if not path.exists():
        return None
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    dest = ARCHIVE_DIR / f"{path.stem}_{stamp}{path.suffix}"
    # avoid clobbering archive too
    n = 1
    while dest.exists():
        dest = ARCHIVE_DIR / f"{path.stem}_{stamp}_{n}{path.suffix}"
        n += 1
    shutil.copy2(path, dest)
    return dest


def save_dated_snapshot(
    content: bytes,
    as_of: str | None = None,
    tz: str = "America/New_York",
) -> Path:
    import json
    import pandas as pd

    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    now = datetime.now(ZoneInfo(tz))
    date_str = as_of or now.date().isoformat()
    stamp = now.strftime("%Y%m%d_%H%M%S")

    raw_path = SNAPSHOT_DIR / f"{date_str}.raw.csv"
    path = SNAPSHOT_DIR / f"{date_str}.csv"

    # Add-only dated files. data/<date>.csv / .raw.csv are written at most once
    # and never overwritten (point-in-time rule: first-committed version counts).
    # A run before the 16:00 ET close of <date> holds the PRIOR session's close,
    # so it never creates the dated file; it goes to archive only. That way the
    # dated file is D's close in normal operation (first post-close run wins).
    close_dt = datetime.fromisoformat(date_str).replace(
        hour=16, tzinfo=ZoneInfo(tz))
    pre_close = now < close_dt
    exists = path.exists() or raw_path.exists()
    write_dated = not exists and not pre_close

    scrape_ts = datetime.now(ZoneInfo("UTC")).isoformat(timespec="seconds")
    run_archive = ARCHIVE_DIR / f"{date_str}_{stamp}.csv"
    run_archive_raw = ARCHIVE_DIR / f"{date_str}_{stamp}.raw.csv"
    run_archive_raw.write_bytes(content)
    df = pd.read_csv(run_archive_raw, low_memory=False)
    # Explicit export time (UTC ISO) on every row; normalize_frame puts
    # News URL, scrape_ts, Open (TAIL) at the END of the column list.
    df["scrape_ts"] = scrape_ts
    norm = normalize_frame(df)
    norm.to_csv(run_archive, index=False)

    if write_dated:
        shutil.copy2(run_archive_raw, raw_path)
        shutil.copy2(run_archive, path)
    elif exists:
        print(f"[finviz_fetch] {date_str} already saved; not overwriting. "
              f"This run kept as archive/{run_archive.name}")
    else:
        print(f"[finviz_fetch] run is before {date_str} 16:00 ET close; dated "
              f"file not written. This run kept as archive/{run_archive.name}")

    current = SNAPSHOT_DIR / "current.csv"
    previous = SNAPSHOT_DIR / "previous.csv"
    if current.exists():
        # archive outgoing current before rotating previous
        _archive_if_exists(previous, stamp)
        if previous.exists():
            previous.unlink()
        shutil.copy2(current, previous)
    shutil.copy2(run_archive, current)

    man = SNAPSHOT_DIR / "manifest.json"
    data = {"dates": [], "files": {}, "runs": []}
    if man.exists():
        data = json.loads(man.read_text())
    dates = data.get("dates", [])
    if path.exists() and date_str not in dates:
        dates.append(date_str)
        dates.sort()
    data["dates"] = dates
    data["latest"] = dates[-1] if dates else None
    if path.exists():
        data.setdefault("files", {})[date_str] = path.name
    runs = data.setdefault("runs", [])
    runs.append(
        {
            "date": date_str,
            "stamp": stamp,
            "canonical": path.name if write_dated else None,
            "dated_written": write_dated,
            "pre_close": pre_close,
            "archive": run_archive.name,
            "bytes": len(content),
            "scrape_ts_utc": scrape_ts,
        }
    )
    data["runs"] = runs[-90:]  # keep last ~90 runs in manifest
    man.write_text(json.dumps(data, indent=2))
    return path


def list_snapshot_dates() -> list[str]:
    import json
    man = SNAPSHOT_DIR / "manifest.json"
    if man.exists():
        return json.loads(man.read_text()).get("dates", [])
    return sorted(p.stem for p in SNAPSHOT_DIR.glob("????-??-??.csv"))


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="Override ET calendar date label")
    args = ap.parse_args()
    print("[finviz_fetch] downloading export...")
    content = fetch_csv()
    path = save_dated_snapshot(content, as_of=args.date)
    print(f"[finviz_fetch] wrote {path} ({len(content):,} bytes)")
    print(f"[finviz_fetch] dates on disk: {list_snapshot_dates()}")


if __name__ == "__main__":
    main()
