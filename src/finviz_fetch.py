"""Fetch Finviz Elite screener CSV via the official export endpoint.

Preferred: set secret FINVIZ_EXPORT to the full export URL that already
includes your auth key (the single link Finviz gives you).

Writes (append-only history):
  data/snapshots/YYYY-MM-DD.csv          ← canonical snapshot for that ET date
  data/snapshots/archive/YYYY-MM-DD_HHMMSS.csv  ← prior version if same day re-run
  data/snapshots/current.csv / previous.csv     ← convenience pointers only
  data/snapshots/manifest.json

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
    "49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70"
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

    # Preserve any existing same-day files before overwrite
    archived_norm = _archive_if_exists(path, stamp)
    archived_raw = _archive_if_exists(raw_path, stamp)
    if archived_norm:
        print(f"[finviz_fetch] archived prior {path.name} → {archived_norm.name}")
    if archived_raw:
        print(f"[finviz_fetch] archived prior {raw_path.name} → {archived_raw.name}")

    raw_path.write_bytes(content)
    df = pd.read_csv(raw_path, low_memory=False)
    norm = normalize_frame(df)
    norm.to_csv(path, index=False)

    # Also keep a uniquely named copy in archive for this run (immutable history)
    run_archive = ARCHIVE_DIR / f"{date_str}_{stamp}.csv"
    shutil.copy2(path, run_archive)

    current = SNAPSHOT_DIR / "current.csv"
    previous = SNAPSHOT_DIR / "previous.csv"
    if current.exists():
        # archive outgoing current before rotating previous
        _archive_if_exists(previous, stamp)
        if previous.exists():
            previous.unlink()
        shutil.copy2(current, previous)
    shutil.copy2(path, current)

    man = SNAPSHOT_DIR / "manifest.json"
    data = {"dates": [], "files": {}, "runs": []}
    if man.exists():
        data = json.loads(man.read_text())
    dates = data.get("dates", [])
    if date_str not in dates:
        dates.append(date_str)
        dates.sort()
    data["dates"] = dates
    data["latest"] = dates[-1] if dates else None
    data.setdefault("files", {})[date_str] = path.name
    runs = data.setdefault("runs", [])
    runs.append(
        {
            "date": date_str,
            "stamp": stamp,
            "canonical": path.name,
            "archive": run_archive.name,
            "bytes": len(content),
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
