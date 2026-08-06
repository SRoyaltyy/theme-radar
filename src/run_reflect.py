"""Stage REFLECT: turn graded outcome into a candidate lesson.

CLI: python -m src.run_reflect --predict-date 2026-08-06
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from . import config, deepseek_client, memory, scoreboard


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def _parse_lesson(text: str) -> dict:
    m = re.search(r"LESSON_BEGIN(.*?)LESSON_END", text, re.S)
    block = m.group(1) if m else ""
    out = {}
    for line in block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--predict-date", required=True)
    args = ap.parse_args()
    date_str = args.predict_date

    if not config.DEEPSEEK_API_KEY:
        raise SystemExit("DEEPSEEK_API_KEY not set")

    board = scoreboard.load()
    entry = scoreboard.get_or_create(board, date_str, config.TOPIC)
    if not entry.get("graded"):
        raise SystemExit(f"[reflect] {date_str}: run outcome first")

    predict_md = _read(config.DAILY / f"{date_str}_predict.md")
    outcome_md = _read(config.DAILY / f"{date_str}_outcome.md")
    prompt = _read(config.GROUNDING / "reflect_prompt.md") or "Write a lesson."

    user = (
        f"PREDICT_DATE: {date_str}\n\n"
        f"=== PREDICTION ===\n{predict_md[:10000]}\n\n"
        f"=== OUTCOME ===\n{outcome_md[:8000]}\n\n"
        f"=== SCOREBOARD ===\nhits={entry.get('theme_hits')} "
        f"misses={entry.get('theme_misses')} theme_hit={entry.get('theme_hit')}\n\n"
        f"=== MEMORY ===\n{memory.scoreboard_summary()}\n\n"
        f"{memory.active_lessons()}\n\n"
        "Execute the five checks and emit LESSON_BEGIN/END."
    )

    text = deepseek_client.chat(
        [{"role": "system", "content": prompt},
         {"role": "user", "content": user}],
        model=getattr(config, "MODEL_REFLECT", config.MODEL_PREDICT),
        tools=False,
        max_tokens=8000,
        stage_label=f"THEME REFLECT {date_str}",
    )

    lb = _parse_lesson(text)
    cand_dir = config.ROOT / "02_lessons" / "candidate"
    cand_dir.mkdir(parents=True, exist_ok=True)
    lesson_path = cand_dir / f"{date_str}_lesson.md"
    lesson_path.write_text(
        "---\n"
        f'trigger_pattern: "{lb.get("TRIGGER_PATTERN", "")}"\n'
        f'current_behavior: "{lb.get("CURRENT_BEHAVIOR", "")}"\n'
        f'corrected_behavior: "{lb.get("CORRECTED_BEHAVIOR", "")}"\n'
        f'error_category: "{lb.get("ERROR_CATEGORY", "none")}"\n'
        f'falsifier: "{lb.get("FALSIFIER", "")}"\n'
        f'date: "{date_str}"\n'
        'status: "candidate"\n'
        "---\n\n"
        f"# Reflection — {date_str}\n\n"
        + text
        + "\n",
        encoding="utf-8",
    )

    entry["reflection_lesson_ref"] = str(lesson_path)
    entry["error_category"] = lb.get("ERROR_CATEGORY")
    scoreboard.save(board)
    print(f"[reflect] {date_str} → {lesson_path} category={lb.get('ERROR_CATEGORY')}")


if __name__ == "__main__":
    main()
