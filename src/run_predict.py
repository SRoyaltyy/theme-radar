"""Stage PREDICT: assemble rubric + memory + Channel 1, call DeepSeek with
web_search, write daily prediction file, update scoreboard.

CLI: python -m src.run_predict [--date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from . import config, deepseek_client, memory, scoreboard


def _channel1_placeholder() -> str:
    """Lightweight Channel 1 until real fetchers are wired."""
    return (
        "=== CHANNEL 1: PRE-FETCHED DATA ===\n"
        "(Placeholder — pipeline will later inject sector ETF performance, "
        "breadth, key commodity moves, and valuation snapshots.)\n"
        "For this run the model must rely primarily on live web_search "
        "for discovery and validation.\n"
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None)
    args = ap.parse_args()
    date_str = args.date or datetime.now(ZoneInfo(config.TZ)).date().isoformat()

    if not config.DEEPSEEK_API_KEY:
        raise SystemExit("DEEPSEEK_API_KEY not set")

    # 1. Rubric
    rubric_path = config.GROUNDING / "master_rubric.md"
    with open(rubric_path, encoding="utf-8") as fh:
        rubric = fh.read()

    # 2. Memory + Channel 1
    mem = memory.prediction_context()
    ch1 = _channel1_placeholder()

    user_msg = (
        f"TODAY: {date_str} (America/New_York)\n\n"
        f"{mem}\n\n"
        f"{ch1}\n\n"
        "Execute the full Theme Radar research process now "
        "(Stage 1 Discovery → Stage 2 Trigger Filter → Stage 3 Five-Layer Scoring). "
        "You must perform live web_search for all required categories before scoring."
    )

    # 3. LLM call with tool loop
    transcript = str(config.DAILY / "_transcripts" / f"{date_str}_predict.json")
    trace = str(config.DAILY / f"{date_str}_predict_trace.md")

    print(f"[predict] {date_str} — calling DeepSeek (tools=True)...")
    text = deepseek_client.chat(
        [
            {"role": "system", "content": rubric},
            {"role": "user", "content": user_msg},
        ],
        model=config.MODEL_PREDICT,
        tools=True,
        max_tokens=10000,
        transcript_path=transcript,
        trace_path=trace,
        stage_label=f"THEME PREDICT {date_str}",
    )

    # 4. Write prediction file
    config.DAILY.mkdir(parents=True, exist_ok=True)
    out_path = config.DAILY / f"{date_str}_predict.md"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(f"# Theme Radar Prediction — {date_str}\n\n")
        fh.write(text)
        fh.write("\n")

    # 5. Scoreboard
    board = scoreboard.load()
    entry = scoreboard.get_or_create(board, date_str, config.TOPIC)
    entry["status"] = "predicted"
    entry["has_output"] = True
    scoreboard.save(board)

    print(f"[predict] wrote {out_path}")
    print(f"[predict] transcript → {transcript}")
    print(f"[predict] trace → {trace}")


if __name__ == "__main__":
    main()
