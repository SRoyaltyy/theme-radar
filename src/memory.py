"""Memory-tier context assembly for Theme Radar.

Every prediction run reads:
  - 00_grounding/master_rubric.md (handled by caller)
  - 04_archive/consolidated_memory.md
  - 02_lessons/active/*
  - 03_scoreboard summary
  - recent 01_daily prediction + reflect files
"""
from __future__ import annotations

import glob
import os
import re
from pathlib import Path

from . import config, scoreboard


def _read(path: str | Path) -> str:
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


def consolidated_memory() -> str:
    return _read(config.CONSOLIDATED_MEMORY).strip() or "(empty — first cycle)"


def active_lessons() -> str:
    parts = []
    pattern = str(config.LESSONS_ACTIVE / "*.md")
    for p in sorted(glob.glob(pattern)):
        parts.append(f"### {os.path.basename(p)}\n{_read(p).strip()}")
    return "\n\n".join(parts) or "(no standing lessons yet)"


def scoreboard_summary() -> str:
    board = scoreboard.load()
    runs = board.get("runs", [])
    # Placeholder accuracy helpers — will be fleshed out
    n = len([r for r in runs if r.get("graded")])
    hits = len([r for r in runs if r.get("theme_hit")])
    rate = f"{hits}/{n}" if n else "n/a"
    lines = [
        f"Graded theme cycles: {n}",
        f"Theme-level hit rate: {rate}",
        "Recent runs:",
    ]
    for r in runs[-8:]:
        lines.append(
            f"- {r.get('date')}: themes={r.get('themes', [])} "
            f"hit={r.get('theme_hit')} graded={r.get('graded')}"
        )
    return "\n".join(lines)


def recent_daily_logs() -> str:
    preds = sorted(glob.glob(str(config.DAILY / "*_predict.md")))
    dates = [re.sub(r"_predict\.md$", "", os.path.basename(p)) for p in preds]
    dates = dates[-config.MEMORY_WINDOW_DAYS:]
    parts = []
    for d in dates:
        pp = config.DAILY / f"{d}_predict.md"
        rp = config.DAILY / f"{d}_reflect.md"
        parts.append(f"===== {d} PREDICT =====\n{_read(pp)}")
        if rp.exists():
            parts.append(f"===== {d} REFLECT =====\n{_read(rp)}")
    return "\n\n".join(parts) or "(no prior daily logs — this is the first run)"


def prediction_context() -> str:
    """Full memory block injected into the theme prediction prompt."""
    return (
        "=== MEMORY CONTEXT ===\n\n"
        f"[SCOREBOARD]\n{scoreboard_summary()}\n\n"
        f"[CONSOLIDATED MEMORY]\n{consolidated_memory()}\n\n"
        f"[STANDING ACTIVE LESSONS]\n{active_lessons()}\n\n"
        f"[LAST {config.MEMORY_WINDOW_DAYS} CYCLES]\n{recent_daily_logs()}"
    )
