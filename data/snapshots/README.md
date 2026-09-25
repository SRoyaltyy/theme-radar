# Finviz snapshots (date-stamped archive)

```
data/snapshots/
  YYYY-MM-DD.csv     ← one file per export day
  manifest.json      ← list of available dates
  current.csv        ← latest (compat pointer)
  previous.csv       ← prior latest (compat pointer)
```

## Tail columns (appended; earlier column positions never change)

Dated `YYYY-MM-DD.csv` end with `News URL`, `scrape_ts` (export time, UTC ISO), `Open`, in that order.
- `News URL`, `scrape_ts`: present from the 2026-09-24 rerun on, absent before.
- `Open` (Finviz day open price, custom-screener column id 86): present from 2026-09-25 on, absent before (no backfill; past files are hash-locked).

## Automated daily fetch (Elite API)

1. In Finviz Elite, open your **Custom** screener with the columns you want.
2. Copy the export URL from the browser (or use API key only).
3. Add GitHub secrets:
   - `FINVIZ_API_KEY` — from Elite account
   - `FINVIZ_EXPORT_URL` (optional) — full export URL with your column set; auth appended if missing
4. Workflow: **Finviz Daily Snapshot** (weekdays + manual)

```bash
python -m src.finviz_fetch
python -m src.finviz_fetch --date 2026-08-06
```

## Manual ingest

```bash
python -m src.promote_snapshot /path/to/export.csv --as-of 2026-06-15
```

## Delta between arbitrary dates

```python
from src.finviz_delta import load_by_date, compute_delta, format_delta_brief
cur = load_by_date("2026-08-06")
prev = load_by_date("2026-06-15")
print(format_delta_brief(compute_delta(cur, prev),
      cur_label="2026-08-06", prev_label="2026-06-15"))
```

Predict auto-picks latest vs ~30d earlier from the manifest.

## History hash manifest (past days are immutable-by-check)

`HASHES.json` holds the sha256 + first-recorded date of every dated file in
`data/snapshots/` (`YYYY-MM-DD.csv`, `.raw.csv`), `data/features/` and `data/scores/`.
The snapshot and score workflows run `python scripts/check_history_hashes.py verify`
before writing (job fails if any recorded file changed or was deleted) and
`add-new --today <ET date>` after writing. Only today's entries may be replaced
(same-day rerun). A deliberate fix to a past file needs
`add-new --restate FILE --reason "..."`, which is logged to `RESTATEMENTS.log`.
