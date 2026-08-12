"""Snapshot date index — shared by score_engine, label_backfill, attribution."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pandas as pd

from .finviz_delta import SNAPSHOT_DIR, normalize_frame
from .score_rubric import HORIZON_WINDOWS


def snapshot_dates() -> dict[str, Path]:
    out = {}
    man = SNAPSHOT_DIR / "manifest.json"
    if man.exists():
        data = json.loads(man.read_text())
        for d, fname in data.get("files", {}).items():
            p = SNAPSHOT_DIR / fname
            if p.exists():
                out[d] = p
    for p in SNAPSHOT_DIR.glob("????-??-??.csv"):
        out.setdefault(p.stem, p)
    return dict(sorted(out.items()))


def find_prior(dates: dict[str, Path], target: date, horizon: str):
    lo, hi = HORIZON_WINDOWS[horizon]
    best = None
    for d in dates:
        try:
            dd = date.fromisoformat(d)
        except ValueError:
            continue
        gap = (target - dd).days
        if lo <= gap <= hi:
            if best is None or dd > best:
                best = dd
    return best.isoformat() if best else None


def load_dated(path: Path) -> pd.DataFrame:
    return normalize_frame(pd.read_csv(path, low_memory=False))
