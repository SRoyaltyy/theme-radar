"""Human-readable daily scan.md — explicit dates for lay readers.

Used by score_engine after scoring. Explains:
  - which two Finviz CSV files were compared
  - what Ret% means (from day A to day B)
  - what Top drivers means (same A→B window, or levels on B only)
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from . import config


def _fname(dates: dict | None, d: str | None) -> str:
    if not d:
        return "(none)"
    if dates and d in dates:
        return Path(str(dates[d])).name
    return f"{d}.csv"


def brief(date_str: str, per_horizon, pairs, segments, dates: dict | None = None) -> str:
    """Build scan.md body.

    date_str = signal as-of = the *newer* snapshot in each pair ("today" in the export).
    pairs[h] = older snapshot used only to compute deltas / Ret% into date_str.
    """
    dates = dates or {}
    run_at = datetime.now(ZoneInfo(getattr(config, "TZ", "America/New_York"))).isoformat()
    cur_file = _fname(dates, date_str)

    L = [
        f"# Daily Universe Scan — as-of **{date_str}**",
        "",
        f"Generated: {run_at}",
        "",
        "## Read this first (plain English)",
        "",
        f"This report scores every stock using the Finviz export from **{date_str}** "
        f"(`data/snapshots/{cur_file}`).",
        "",
        "For each horizon we **compare two snapshot files**:",
        "",
        "| Name | Meaning |",
        "|------|---------|",
        f"| **As-of / newer file** | `{cur_file}` dated **{date_str}** — prices and fields *now* |",
        "| **Pair / older file** | An earlier Finviz export — used only to see *what changed* into the as-of day |",
        "",
        "**Important:** `pair: YYYY-MM-DD` means the **older** file is that date. "
        "It does **not** mean we compared 8/10 vs 8/7. "
        "It means we compared **that pair date → the as-of date** above.",
        "",
        "Example: as-of **2026-08-11**, `pair: 2026-08-10` ⇒ "
        "we used **`2026-08-10.csv` and `2026-08-11.csv` only** for that horizon. "
        "The 8/7 file is **not** used in the 1d block (it may appear only under the 1w block if that pair is 8/7).",
        "",
        "| Column | Exact meaning |",
        "|--------|----------------|",
        "| **Score** | Model points for this horizon (higher = more bullish evidence under the rubric) |",
        "| **Ret%** | Price return **from the pair (older) date close → as-of (newer) date close** for that row’s horizon. "
        "If pair is none, Ret% is blank/N/A (levels only). |",
        "| **Top drivers** | Which rubric inputs contributed most to the Score. "
        "When a pair exists, **delta drivers** (e.g. Price, Relative Volume change) are measured **older → newer** "
        "(same window as Ret%). Level-only inputs (e.g. RSI standing) are taken from the **as-of** file. |",
        "| **Status / Flags** | Buckets from the **as-of** snapshot (extended, short float, etc.) |",
        "",
        "Full machine tables (every ticker): `data/scores/` and `data/features/`. "
        "Tables below are only top/bottom for reading.",
        "",
        f"Trace one name: `python -m src.score_engine --date {date_str} --trace TICKER --horizon 1d`",
        "",
        "## Files used per horizon",
        "",
        "| Horizon | Older file (pair) | Newer file (as-of) | Ret% window |",
        "|---------|-------------------|--------------------|-------------|",
    ]

    for h in ("1d", "1w", "1m"):
        pair = pairs.get(h) if pairs else None
        if pair:
            L.append(
                f"| **{h}** | `{_fname(dates, pair)}` (**{pair}**) | "
                f"`{cur_file}` (**{date_str}**) | **{pair} → {date_str}** |"
            )
        else:
            L.append(
                f"| **{h}** | *(none — not enough history)* | "
                f"`{cur_file}` (**{date_str}**) | **n/a (levels only)** |"
            )

    L.append("")

    for h in ("1d", "1w", "1m"):
        df = per_horizon.get(h) if per_horizon else None
        pair = pairs.get(h) if pairs else None
        if pair:
            L.append(f"## Horizon {h}")
            L.append("")
            L.append(
                f"- **Older snapshot (pair):** `{_fname(dates, pair)}` (**{pair}**)"
            )
            L.append(
                f"- **Newer snapshot (as-of):** `{cur_file}` (**{date_str}**)"
            )
            L.append(
                f"- **Ret%:** price change from **{pair} → {date_str}** "
                f"(not any other pair of days)."
            )
            L.append(
                f"- **Top drivers:** mainly what changed from **{pair} → {date_str}** "
                f"(+ some levels read on **{date_str}**)."
            )
        else:
            L.append(f"## Horizon {h}")
            L.append("")
            L.append(
                f"- **No older pair file** — scores use **levels on {date_str} only**."
            )
            L.append("- **Ret%:** not applicable (shown as empty / None).")
            L.append(
                f"- **Top drivers:** levels on **{date_str}** only (e.g. RSI, distance to 50-day MA)."
            )

        if df is None:
            L.append("")
            continue

        L.append("")
        L.append(
            f"Scored **{len(df)}** tickers. "
            f"Bullish (score > +2): {(df['total_score'] > 2).sum()} | "
            f"Bearish (score < −2): {(df['total_score'] < -2).sum()}"
        )
        L.append("")

        if pair:
            ret_hdr = f"Ret% ({pair}→{date_str})"
            drv_hdr = f"Top drivers ({pair}→{date_str} + levels on {date_str})"
            neg_hdr = f"Top negatives ({pair}→{date_str} + levels on {date_str})"
        else:
            ret_hdr = "Ret% (n/a)"
            drv_hdr = f"Top drivers (levels on {date_str} only)"
            neg_hdr = f"Top negatives (levels on {date_str} only)"

        L.append("**Top 15 (highest score):**")
        L.append("")
        L.append(
            f"| Ticker | Industry | Score | {ret_hdr} | Status | Flags | {drv_hdr} |"
        )
        L.append("|---|---|---|---|---|---|---|")
        for _, r in df.head(15).iterrows():
            L.append(
                f"| {r['Ticker']} | {str(r['Industry'])[:24]} | "
                f"{r['total_score']:+.1f} | {r['ret_H']} | "
                f"{r['status_extension']}/{r['status_trend']}/{r['status_short']} | "
                f"{r['kill_flags'] or '—'} | {str(r['top_pos'])[:60]} |"
            )
        L.append("")
        L.append("**Bottom 10 (lowest score):**")
        L.append("")
        L.append(
            f"| Ticker | Industry | Score | {ret_hdr} | Status | {neg_hdr} |"
        )
        L.append("|---|---|---|---|---|---|")
        for _, r in df.tail(10).iloc[::-1].iterrows():
            L.append(
                f"| {r['Ticker']} | {str(r['Industry'])[:24]} | "
                f"{r['total_score']:+.1f} | {r['ret_H']} | "
                f"{r['status_extension']}/{r['status_trend']}/{r['status_short']} | "
                f"{str(r['top_neg'])[:60]} |"
            )
        L.append("")

    if segments is not None and len(segments):
        pair_1w = pairs.get("1w") if pairs else None
        L.append("## Industry segments (from 1w scores)")
        L.append("")
        if pair_1w:
            L.append(
                f"Median **Ret%** below is the median stock return **{pair_1w} → {date_str}** "
                f"inside that industry."
            )
        L.append("")
        L.append("| Industry | n | Median score | % positive | Median ret% |")
        L.append("|---|---|---|---|---|")
        for name, r in segments.head(20).iterrows():
            L.append(
                f"| {str(name)[:34]} | {int(r['n'])} | {r['med_total']:+.1f} | "
                f"{r['pct_positive']}% | {r['med_ret']} |"
            )
        L.append("")

    return "\n".join(L)
