"""Stage PREDICT: assemble rubric + memory + Channel 1, call DeepSeek,
parse THEME_SCORES blocks, write daily prediction file, update scoreboard.

CLI: python -m src.run_predict [--date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from . import config, memory, scoreboard


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None)
    args = ap.parse_args()
    date_str = args.date or datetime.now(ZoneInfo(config.TZ)).date().isoformat()

    if not config.DEEPSEEK_API_KEY:
        raise SystemExit("DEEPSEEK_API_KEY not set")

    # 1. Load rubric
    rubric_path = config.GROUNDING / "master_rubric.md"
    with open(rubric_path, encoding="utf-8") as fh:
        rubric = fh.read()

    # 2. Memory context
    mem = memory.prediction_context()

    # 3. Channel 1 placeholder (to be replaced by real pre-fetched data)
    channel1 = (
        "=== CHANNEL 1: PRE-FETCHED DATA ===\n"
        "(Pipeline will inject sector ETF performance, breadth, "
        "commodity moves, valuation snapshots, recent CapEx language, etc.)\n"
    )

    user_msg = (
        f"TODAY: {date_str} (America/New_York)\n\n"
        f"{mem}\n\n"
        f"{channel1}\n\n"
        "Execute the full Theme Radar rubric now. "
        "You must perform live searches for all required Channel 2 categories "
        "before producing any THEME_SCORES blocks."
    )

    print(f"[predict] {date_str} — rubric + memory assembled.")
    print("[predict] DeepSeek client + tool loop not yet wired in this skeleton.")
    print("[predict] Next steps: implement deepseek_client.py + Channel 1 fetchers.")

    # Placeholder write so the folder structure is usable
    config.DAILY.mkdir(parents=True, exist_ok=True)
    out_path = config.DAILY / f"{date_str}_predict.md"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(f"# Theme Radar Prediction — {date_str}\n\n")
        fh.write("## Memory Context\n\n")
        fh.write(mem)
        fh.write("\n\n## Channel 1\n\n")
        fh.write(channel1)
        fh.write("\n\n## Status\n\nSkeleton only — full LLM call pending.\n")

    board = scoreboard.load()
    entry = scoreboard.get_or_create(board, date_str, config.TOPIC)
    entry["status"] = "skeleton"
    scoreboard.save(board)
    print(f"[predict] wrote {out_path}")


if __name__ == "__main__":
    main()
