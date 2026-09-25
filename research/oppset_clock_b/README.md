# Clock-B Gap + RelVol Opportunity Set

**Research-only.** Theme Radar / Taskforce Excel panel feed.

## Clock B definition

- `join_morning` = **T** = open of morning session (decision time).
- `finviz_asof` = **T−1** = prior trading session in the theme-radar date list.
- Latest: `join_morning=2026-09-25` uses `finviz_asof=2026-09-24` (T−1 close).
- Also includes `join_morning=2026-09-24` with `finviz_asof=2026-09-23`, `join_morning=2026-09-23` with `finviz_asof=2026-09-22`, and `join_morning=2026-09-22` with `finviz_asof=2026-09-21`.
- All features come from the after-close raw Finviz snapshot dated `finviz_asof`.
- Do **not** use same-day Gap / RelVol / Change from snapshot T (those are after-T outcomes).

## Append-only (since 2026-09-25)

- Built by `research/oppset_clock_b/build_oppset_clock_b.py` (the old
  `/workspace/theme-radar-top-gainers/build_oppset_clock_b.py` is now a wrapper
  around it). Each refresh appends only the new `join_morning` (T = next US
  trading day after the latest `data/snapshots/<asof>.raw.csv`), one day at a time.
- Day T is built only from the single raw file dated `finviz_asof` = T−1.
  That snapshot must be the real close: taken after 16:00 ET on T−1 and before
  09:30 ET on T (`scrape_ts`, else the git commit time of the on-disk file;
  `history_guard.close_is_in`). Otherwise the build is refused, logged in
  `APPEND_LOG.tsv` as `refused: ...`, and nothing is appended. No later file
  is read.
- Past rows are never recomputed. `FINGERPRINTS.json` holds a row-level sha256
  per `join_morning` for `oppset_all.csv`, `oppset_flagged.csv` and
  `oppset_0916_0918.csv`; the refresh and `scripts/check_history_hashes.py verify`
  fail if any committed row changes. Only the morning whose `finviz_asof` is
  today (ET) may be rebuilt (same-day rerun).
- Outcome-grade columns added later (e.g. forward returns) are fill-once: once a
  morning's cells are set, they are fingerprinted and may never change.
- `APPEND_LOG.tsv` records when each morning was built (`built_late=1` if built
  after its own 09:30 ET, e.g. catch-up of a missed night).
- Rows recorded before 2026-09-25 are kept as committed. Note: join_morning
  2026-09-24 / 2026-09-25 were built from an earlier fetch of the 2026-09-23 /
  2026-09-24 raw files than the ones now in `data/snapshots/` (those were
  re-fetched by the ~23:00 UTC cron); the committed rows are the record.
- Restored 2026-09-25 (War room, logged in `data/snapshots/RESTATEMENTS.log`):
  join_morning 2026-09-22 rows back to 22d9eda (committed 2026-09-21 17:04 ET)
  and 2026-09-23 rows back to dea3ff6 (2026-09-22 16:48 ET), i.e. the last
  version committed before each morning's 09:30 ET open; the full-rebuild
  rewrites in dea3ff6 / 69d7c6b are superseded.

## Features (from T−1)

| Column | Finviz field |
|--------|----------------|
| `rvol` | Relative Volume |
| `change_pct` | Change |
| `chg_open_pct` | Change from Open |
| `gap_pct` | Gap (yesterday's gap — still a tell) |
| `ah_change_pct` | After-Hours Change (if parseable) |
| `pweek` | Performance (Week) |
| `sector` | Sector |
| `price` | Price |
| `avg_vol` | Average Volume (**thousands**) |
| `mcap` | Market Cap (**millions**) |

## Clean midcap filters

- Drop rows with non-null `ETF Type`
- Drop company/industry noise: ETF / Fund / Trust / Warrant / Acquisition Corp / Blank Check / SPAC / Unit / Preferred / Exchange Traded Fund / Closed-End Fund / Shell Company
- `price ≥ 5`
- `avg_vol ≥ 500` (thousands)
- `mcap ≥ 200` (millions)

## Flags (int 0/1)

- `flag_rvol_ge_2`, `_3`, `_5`
- `flag_abs_chg_ge_5`, `_8`, `_10`
- `flag_abs_gap_ge_3`, `_5` (from T−1 Gap)
- `flag_abs_ah_chg_ge_2`, `_5` (T−1 After-Hours Change if parseable)
- `flag_pweek_ge_15`, `_40`
- `any_opp` = OR of rvol≥2 **or** abs_chg≥5 **or** abs_gap≥3 **or** abs_ah≥2 **or** pweek≥15

## Files

| File | Contents |
|------|----------|
| `oppset_all.csv` | Full clean midcap, all join mornings |
| `oppset_flagged.csv` | `any_opp == 1` only |
| `oppset_0916_0918.csv` | Clean midcap for join_morning ∈ {2026-09-16, 2026-09-17, 2026-09-18} |
| `OPPSET_SUMMARY.md` | Per-morning n_clean / n_flagged / top5 |

No fullscan edits. Not a KEEP edge — opportunity-set for panel / Excel proof only.
