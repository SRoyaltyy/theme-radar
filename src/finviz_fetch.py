"""Fetch Finviz Elite screener CSV via the official export endpoint.

Elite export API (no browser):
  GET https://elite.finviz.com/export.ashx
      ?v=152          # Custom view
      &c=1,2,3,...    # column IDs
      &auth=API_KEY

Auth: set FINVIZ_API_KEY in env / GitHub Secrets

Daily workflow writes:
  data/snapshots/YYYY-MM-DD.csv
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


def fetch_csv(api_key: str | None = None, extra_params: dict | None = None) -> bytes:
    key = (api_key or os.environ.get("FINVIZ_API_KEY", "")).strip()
    if not key:
        raise SystemExit(
            "FINVIZ_API_KEY not set. Get it from Finviz Elite account settings."
        )

    override = os.environ.get("FINVIZ_EXPORT_URL", "").strip()
    if override:
        sep = "&" if "?" in override else "?"
        if "auth=" not in override:
            override = f"{override}{sep}auth={key}"
        url = override
        params = None
    else:
        url = EXPORT_URL
        params = {
            "v": os.environ.get("FINVIZ_VIEW", "152"),
            "c": os.environ.get("FINVIZ_COLS", DEFAULT_COLS),
            "auth": key,
        }
        if extra_params:
            params.update(extra_params)

    headers = {
        "User-Agent": "theme-radar/1.0 (+github.com/SRoyaltyy/theme-radar)",
    }
    r = requests.get(url, params=params, headers=headers, timeout=120)
    r.raise_for_status()
    if not r.content or b"Ticker" not in r.content[:500]:
        raise RuntimeError(
            "Finviz export did not return a CSV with Ticker header. "
            "Check API key and column list / FINVIZ_EXPORT_URL."
        )
    return r.content


def save_dated_snapshot(
    content: bytes,
    as_of: str | None = None,
    tz: str = "America/New_York",
) -> Path:
    import json
    import pandas as pd

    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = as_of or datetime.now(ZoneInfo(tz)).date().isoformat()
    raw_path = SNAPSHOT_DIR / f"{date_str}.raw.csv"
    path = SNAPSHOT_DIR / f"{date_str}.csv"

    raw_path.write_bytes(content)
    df = pd.read_csv(raw_path, low_memory=False)
    norm = normalize_frame(df)
    norm.to_csv(path, index=False)

    current = SNAPSHOT_DIR / "current.csv"
    previous = SNAPSHOT_DIR / "previous.csv"
    if current.exists():
        if previous.exists():
            previous.unlink()
        shutil.copy(current, previous)
    shutil.copy(path, current)

    man = SNAPSHOT_DIR / "manifest.json"
    data = {"dates": [], "files": {}}
    if man.exists():
        data = json.loads(man.read_text())
    dates = data.get("dates", [])
    if date_str not in dates:
        dates.append(date_str)
        dates.sort()
    data["dates"] = dates
    data["latest"] = dates[-1] if dates else None
    data.setdefault("files", {})[date_str] = path.name
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
    ap.add_argument("--date", default=None)
    args = ap.parse_args()
    print("[finviz_fetch] downloading export...")
    content = fetch_csv()
    path = save_dated_snapshot(content, as_of=args.date)
    print(f"[finviz_fetch] wrote {path}")
    print(f"[finviz_fetch] dates on disk: {list_snapshot_dates()}")


if __name__ == "__main__":
    main()
