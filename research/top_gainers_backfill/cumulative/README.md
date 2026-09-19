# Theme Radar — Cumulative top-G/L (2d / 3d / 5d)

Research-only for Trading Bot Taskforce. Source: Finviz raw snapshots `data/snapshots/{date}.raw.csv` (local copies under `theme-radar-top-gainers/raw/`).

Session dates T: **2026-08-13 → 2026-09-18** (theme-radar snapshot calendar in `dates.txt`).

## Filters (clean midcap — same as 1d backfill)

1. Drop ETF Type non-null / warrant / fund / shell / blank-check noise (company & industry patterns).
2. **Price ≥ $5**
3. **Average Volume ≥ 500** (Finviz column is **thousands** → ≥ 500k shares)
4. **Market Cap ≥ 200** (Finviz column is **millions** → ≥ $200M); keep rows with missing MCap
5. Rank by forward cumulative return; keep **top 25 gainers** + **top 15 losers** per (T, H)

## Cumulative return

For horizon H ∈ {2, 3, 5}:

- Require `T+H` exists on the snapshot calendar.
- `cum_ret = Price[T+H] / Price[T] − 1` (prefer price path over chaining Change%).
- Reported as `cum_ret_pct`.

Tickers must be in the clean universe **at T** and have a price print at both T and T+H.

## Two clocks (open-knowable vs after-T)

### Clock B — enter **open of T**

Only fields from snapshot **T−1** (after-close of prior session) are open-knowable:

- `knowable_relvol_Tm1`, `knowable_gap_Tm1`, `knowable_change_Tm1`, `news_Tm1`

Snapshot **T** Gap / RelVol / Change / News are **after-T** — do **not** treat them as open-knowable for predicting T’s own session.

### Clock A — enter **next open after T close** (open of T+1)

After seeing session T close, snapshot-T fields are knowable for a multi-day hold T → T+H:

- `after_T_relvol`, `after_T_change`, `after_T_gap`
- Window extras: `after_window_max_relvol`, `news_peak` (news on the peak single-day Change% day in T..T+H)

### Column map vs taskforce ask

| Ask | Columns |
|-----|---------|
| open-knowable tells at T (Clock B) | `knowable_*_Tm1`, `news_Tm1` |
| after-T tells | `after_T_*`, `after_window_max_relvol`, `news_peak` |

## Lag flag

`lag_flag=true` if the ticker is **not** in the 1d clean top-25 gainers on day T, but **is** in the 1d top-25 on some day T+k for k∈{1..H}. Marks multi-day winners that “lagged” the day-1 spike list.

## Outputs

- `cum_{H}d_all.csv` — long format gainers+losers for horizon H
- `SUMMARY_{H}d.md` — per-T top5 cumulative gainers with 1-line tell
- `SUMMARY_all.md` — roll-up
- This README

## Not prediction

These tables are outcome maps + tell attachments. They do not assert that T−1 RelVol “predicts” H-day returns.
