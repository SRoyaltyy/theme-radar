# Clock-B Gap + RelVol Opportunity Set

**Research-only.** Theme Radar / Taskforce Excel panel feed.

## Clock B definition

- `join_morning` = **T** = open of morning session (decision time).
- `finviz_asof` = **T−1** = prior trading session in the theme-radar date list.
- All features come from the after-close raw Finviz snapshot dated `finviz_asof`.
- Do **not** use same-day Gap / RelVol / Change from snapshot T (those are after-T outcomes).

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
