"""Stage OUTCOME: grade past theme predictions against Finviz snapshot baskets.

CLI: python -m src.run_outcome --predict-date 2026-08-06 [--as-of 2026-09-05]
"""
from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from . import config, deepseek_client, finviz_delta, scoreboard


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def _parse_themes(predict_md: str) -> list[dict]:
    themes = []
    blocks = re.findall(
        r"THEME_SCORES_BEGIN(.*?)THEME_SCORES_END",
        predict_md,
        flags=re.S | re.I,
    )
    for block in blocks:
        entry: dict[str, str] = {}
        for line in block.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                entry[k.strip().upper()] = v.strip()
        if not entry.get("THEME"):
            for m in re.finditer(
                r"(THEME|OVERALL|CONFIDENCE|HORIZON|PURE_PLAY_HINTS)\s*:\s*([^:]+?)(?=\s(?:THEME|NARRATIVE|TRIGGER|SCARCITY|INSTITUTIONAL|MOMENTUM|KILL_SWITCHES|OVERALL|CONFIDENCE|HORIZON|RATIONALE|PURE_PLAY_HINTS)\s*:|$)",
                block,
                re.I,
            ):
                entry[m.group(1).upper()] = m.group(2).strip()
        if entry.get("THEME"):
            hints = entry.get("PURE_PLAY_HINTS", "")
            entry["_tickers"] = [
                h.strip().upper()
                for h in re.split(r"[,/\s]+", hints)
                if h.strip() and h.strip().isalpha() and 1 < len(h.strip()) <= 5
            ]
            themes.append(entry)
    for m in re.finditer(r"\*\*Core \(less extended\):\*\*\s*(.+)", predict_md):
        tickers = [t.strip().upper() for t in m.group(1).split(",") if t.strip()]
        if tickers and themes:
            for t in themes:
                if not t.get("_core"):
                    t["_core"] = tickers
                    break
    return themes


def _price_map(df: pd.DataFrame) -> dict[str, float]:
    if "Ticker" not in df.columns or "Price" not in df.columns:
        return {}
    out = {}
    for _, r in df.iterrows():
        try:
            out[str(r["Ticker"]).upper()] = float(r["Price"])
        except (TypeError, ValueError):
            continue
    return out


def _basket_return(
    tickers: list[str],
    start_prices: dict[str, float],
    end_prices: dict[str, float],
) -> tuple[float | None, list[str]]:
    rets = []
    used = []
    for t in tickers:
        a, b = start_prices.get(t), end_prices.get(t)
        if a and b and a > 0:
            rets.append((b / a) - 1.0)
            used.append(t)
    if not rets:
        return None, []
    return sum(rets) / len(rets) * 100.0, used


def _benchmark_return(start_df: pd.DataFrame, end_df: pd.DataFrame) -> float | None:
    sp, ep = _price_map(start_df), _price_map(end_df)
    common = [t for t in sp if t in ep and sp[t] > 0]
    if len(common) < 50:
        return None
    common = common[:: max(1, len(common) // 400)]
    rets = [(ep[t] / sp[t]) - 1.0 for t in common]
    return float(pd.Series(rets).median() * 100.0)


def grade_themes(
    themes: list[dict],
    start_df: pd.DataFrame,
    end_df: pd.DataFrame,
) -> list[dict]:
    sp, ep = _price_map(start_df), _price_map(end_df)
    bench = _benchmark_return(start_df, end_df)
    graded = []
    for th in themes:
        tickers = th.get("_core") or th.get("_tickers") or []
        ret, used = _basket_return(tickers, sp, ep)
        hit = None
        if ret is not None and bench is not None:
            hit = ret > bench + 1.0
        graded.append(
            {
                "theme": th.get("THEME"),
                "overall": th.get("OVERALL"),
                "confidence": th.get("CONFIDENCE"),
                "horizon": th.get("HORIZON"),
                "tickers_used": used,
                "basket_return_pct": None if ret is None else round(ret, 2),
                "benchmark_return_pct": None if bench is None else round(bench, 2),
                "basket_hit": hit,
            }
        )
    return graded


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--predict-date", required=True)
    ap.add_argument("--as-of", default=None)
    ap.add_argument("--min-days", type=int, default=14)
    args = ap.parse_args()

    pred_date = args.predict_date
    as_of = args.as_of or datetime.now(ZoneInfo(config.TZ)).date().isoformat()

    pred_path = config.DAILY / f"{pred_date}_predict.md"
    predict_md = _read(pred_path)
    if not predict_md:
        raise SystemExit(f"No prediction file at {pred_path}")

    d0 = datetime.strptime(pred_date, "%Y-%m-%d").date()
    d1 = datetime.strptime(as_of, "%Y-%m-%d").date()
    if (d1 - d0).days < args.min_days:
        print(
            f"[outcome] only {(d1 - d0).days}d since predict "
            f"(min {args.min_days}) — still writing partial file"
        )

    themes = _parse_themes(predict_md)
    if not themes:
        raise SystemExit("No THEME_SCORES blocks parsed from prediction")

    dates = finviz_delta.list_dates()
    start_label = pred_date if pred_date in dates else (
        max([d for d in dates if d <= pred_date], default=None)
    )
    end_label = as_of if as_of in dates else (
        max([d for d in dates if d <= as_of], default=None)
    )
    if not start_label or not end_label:
        raise SystemExit(
            f"Need Finviz snapshots covering {pred_date} and {as_of}. Have: {dates}"
        )

    start_df = finviz_delta.load_by_date(start_label)
    end_df = finviz_delta.load_by_date(end_label)
    graded = grade_themes(themes, start_df, end_df)

    lines = [
        f"# Theme Outcome — predict {pred_date} → as-of {as_of}",
        f"Snapshots: {start_label} → {end_label}",
        "",
        "## Deterministic basket grades",
        "",
    ]
    hits = misses = 0
    for g in graded:
        if g["basket_hit"] is True:
            hits += 1
        elif g["basket_hit"] is False:
            misses += 1
        lines.append(
            f"- **{g['theme']}** overall={g['overall']} | "
            f"basket={g['basket_return_pct']}% vs bench={g['benchmark_return_pct']}% | "
            f"hit={g['basket_hit']} | tickers={','.join(g['tickers_used'][:8])}"
        )
    lines.append("")
    lines.append(f"Hits={hits} Misses={misses} Ungraded={len(graded)-hits-misses}")
    lines.append("")
    det_md = "\n".join(lines)

    llm_text = ""
    if config.DEEPSEEK_API_KEY:
        prompt = _read(config.GROUNDING / "outcome_prompt.md") or "Grade the themes."
        user = (
            f"PREDICT_DATE: {pred_date}\nAS_OF: {as_of}\n\n"
            f"=== PREDICTION ===\n{predict_md[:12000]}\n\n"
            f"=== DETERMINISTIC GRADES ===\n{det_md}\n"
        )
        try:
            llm_text = deepseek_client.chat(
                [{"role": "system", "content": prompt},
                 {"role": "user", "content": user}],
                model=config.MODEL_PREDICT,
                tools=False,
                max_tokens=6000,
                stage_label=f"THEME OUTCOME {pred_date}",
            )
        except Exception as e:  # noqa: BLE001
            llm_text = f"(LLM outcome skipped: {e})"

    out_path = config.DAILY / f"{pred_date}_outcome.md"
    out_path.write_text(det_md + "\n\n## LLM review\n\n" + llm_text + "\n", encoding="utf-8")

    board = scoreboard.load()
    entry = scoreboard.get_or_create(board, pred_date, config.TOPIC)
    entry["status"] = "outcome"
    entry["outcome_as_of"] = as_of
    entry["theme_hits"] = hits
    entry["theme_misses"] = misses
    entry["theme_grades"] = graded
    entry["graded"] = True
    entry["theme_hit"] = hits > misses
    scoreboard.save(board)

    print(f"[outcome] wrote {out_path} | hits={hits} misses={misses}")


if __name__ == "__main__":
    main()
