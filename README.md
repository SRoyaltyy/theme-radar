# Theme Radar

Closed-loop **theme / sector / stock** radar on daily Finviz Elite snapshots.

## What runs daily (US trading days, America/New_York)

1. **Finviz snapshot** (`finviz_daily.yml` ~20:30 UTC) — full universe export, date-stamped under `data/snapshots/`
2. **Score + feature log** (`score_delta.yml` ~21:00 UTC)
   - Preliminary rubric scores for **every** ticker → `data/scores/YYYY-MM-DD_{1d,1w,1m}.csv`
   - Human brief (top/bottom only) → `01_daily/YYYY-MM-DD_scan.md`
   - **Full-universe** levels + deltas + scores → `data/features/YYYY-MM-DD_1d.csv`
3. **Label backfill** — when later snapshots exist, attach `fwd_1d/2d/3d` → `data/labels/`
4. **Attribution** — score IC, per-delta IC, combinations, risk probes on **all** labeled rows → `data/attribution/` + `01_daily/YYYY-MM-DD_attribution.md` + candidate lessons

Weekly: **promote** repeated lessons → `02_lessons/active/`

Scoring weights are **not** auto-edited; lessons propose changes after repeats.

## Local commands

```bash
pip install -r requirements.txt

# Full score + feature log (all tickers)
python -m src.score_engine --date 2026-08-07

# Per-ticker audit
python -m src.score_engine --date 2026-08-07 --trace MP,OKLO --horizon 1d --skip-universe

# Forward labels (needs later snapshots)
python -m src.label_backfill

# Attribution (needs features + labels)
python -m src.attribution --scan-date 2026-08-07

# Promote repeated lessons
python -m src.promote_lessons
```

## Full universe rule

Markdown tables may show top/bottom 15. **CSV feature/score/label files always contain every ticker** in the snapshot. Attribution statistics use the full cross-section.

## Secrets

- `FINVIZ_EXPORT` (or URL/key variants) for daily fetch
- `DEEPSEEK_API_KEY` / `SEARXNG_URL` only for theme *predict* workflow (optional)

## Timezones

All market-day decisions use **America/New_York**. HKT is display-only; do not gate jobs on Hong Kong weekdays alone. NYSE holidays are listed in `src/trading_calendar.py`.
