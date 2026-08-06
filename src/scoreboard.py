"""Simple JSON scoreboard for theme prediction cycles."""
from __future__ import annotations

import json
from . import config

SCOREBOARD_PATH = config.SCOREBOARD_DIR / "scoreboard.json"


def load() -> dict:
    if SCOREBOARD_PATH.exists():
        with open(SCOREBOARD_PATH, encoding="utf-8") as fh:
            return json.load(fh)
    return {"runs": []}


def save(board: dict) -> None:
    config.SCOREBOARD_DIR.mkdir(parents=True, exist_ok=True)
    with open(SCOREBOARD_PATH, "w", encoding="utf-8") as fh:
        json.dump(board, fh, indent=2, default=str)


def get_or_create(board: dict, date_str: str, topic: str) -> dict:
    for r in board["runs"]:
        if r.get("date") == date_str and r.get("topic") == topic:
            return r
    entry = {"date": date_str, "topic": topic, "graded": False}
    board["runs"].append(entry)
    return entry
