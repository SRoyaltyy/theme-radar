# Factor report — multi-date aggregate

_Generated 2026-08-13 17:36 EDT from 5 scan dates._

How to read: **IC** = Spearman rank correlation between the factor and the forward return, computed per scan date then averaged (mean IC). **ICIR** = mean/std across dates — the consistency score; |ICIR| above ~0.5 with sign consistency ≥ 2/3 is what we call a real signal. **spread** = average forward return when the factor is positive minus when negative. Factors marked ⚠️ flips sign between dates — treat as noise.

## Coverage (exact date spans)

| Scan date (features) | Deltas vs | 1d label | 2d label | 3d label | Stocks |
|---|---|---|---|---|---|
| 2026-08-06 | — | 2026-08-07 | 2026-08-10 | 2026-08-11 | 11543 |
| 2026-08-07 | 2026-08-06 | 2026-08-10 | 2026-08-11 | 2026-08-12 | 11525 |
| 2026-08-10 | 2026-08-07 | 2026-08-11 | 2026-08-12 | 2026-08-13 | 11533 |
| 2026-08-11 | 2026-08-10 | 2026-08-12 | 2026-08-13 | — | 11543 |
| 2026-08-12 | 2026-08-11 | 2026-08-13 | — | — | 11553 |

## Composite score effectiveness (total_score IC)

| Scan date | 1d IC | 2d IC | 3d IC |
|---|---|---|---|
| 2026-08-06 | +0.0958 | +0.0636 | +0.0815 |
| 2026-08-07 | -0.0339 | -0.0242 | -0.0009 |
| 2026-08-10 | -0.0491 | -0.0596 | -0.1054 |
| 2026-08-11 | +0.1007 | +0.0174 | — |
| 2026-08-12 | -0.0472 | — | — |
- **1d**: mean IC **+0.0133**, ICIR +0.19, sign consistency 40% over 5 dates
- **2d**: mean IC **-0.0007**, ICIR -0.02, sign consistency 50% over 4 dates
- **3d**: mean IC **-0.0083**, ICIR -0.11, sign consistency 67% over 3 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -20140709820486304.00 | 100% | 5 | -6.23% | ✅ consistent |
| short_fwd_2d | -0.6138 | -19.08 | 100% | 4 | -5.17% | ✅ consistent |
| short_fwd_3d | -0.4856 | -13.95 | 100% | 3 | -4.87% | ✅ consistent |
| d_Performance (Week) | -0.0615 | -0.77 | 75% | 4 | -2.04% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0517 | -1.32 | 75% | 4 | -3.06% | ✅ consistent |
| d_Forward P/E | -0.0505 | -1.94 | 100% | 4 | -0.26% | ✅ consistent |
| true_ret | -0.0494 | -1.04 | 75% | 4 | -2.68% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0479 | -1.11 | 75% | 4 | -2.85% | ✅ consistent |
| d_Performance (YTD) | -0.0478 | -0.93 | 75% | 4 | -2.45% | ✅ consistent |
| exit_price_1d | +0.0475 | +0.89 | 80% | 5 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0435 | -0.79 | 75% | 4 | -2.94% | ✅ consistent |
| d_Performance (Quarter) | -0.0421 | -0.57 | 75% | 4 | -3.87% | ✅ consistent |
| d_Market Cap | -0.0420 | -1.96 | 100% | 4 | -3.58% | ✅ consistent |
| exit_price_2d | +0.0418 | +0.72 | 75% | 4 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0377 | -1.49 | 100% | 4 | -3.46% | ✅ consistent |
| Sales Year Over Year TTM | +0.0369 | +1.72 | 80% | 5 | +0.52% | ✅ consistent |
| d_Price | -0.0358 | -0.65 | 75% | 4 | -2.68% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0348 | +1.26 | 80% | 5 | -0.74% | ✅ consistent |
| Short Float | +0.0345 | +0.43 | 80% | 5 | n/a | ✅ consistent |
| Price | +0.0306 | +0.57 | 60% | 5 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0306 | +0.57 | 60% | 5 | n/a | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0302 | +0.29 | 40% | 5 | -2.30% | ⚠️ flips / too few dates |
| d_Performance (Month) | +0.0295 | +0.42 | 50% | 4 | -1.00% | ⚠️ flips / too few dates |
| d_Short Float | -0.0293 | -1.92 | 100% | 3 | +0.11% | ✅ consistent |
| upside_pct_lvl | +0.0284 | +0.39 | 60% | 5 | +1.24% | ⚠️ flips / too few dates |
| upside_pct | +0.0284 | +0.39 | 60% | 5 | +1.25% | ⚠️ flips / too few dates |
| Market Cap | +0.0270 | +0.80 | 80% | 5 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0265 | +0.34 | 40% | 5 | -2.28% | ⚠️ flips / too few dates |
| Beta | +0.0261 | +0.23 | 75% | 4 | -0.27% | ✅ consistent |
| w_pos | +0.0220 | +0.34 | 60% | 5 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -12738103345051544.00 | 100% | 4 | -9.27% | ✅ consistent |
| short_fwd_3d | -0.7281 | -16.95 | 100% | 3 | -8.55% | ✅ consistent |
| short_fwd_1d | -0.6138 | -19.08 | 100% | 4 | -4.42% | ✅ consistent |
| d_Performance (Week) | -0.1304 | -3.76 | 100% | 3 | -2.84% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0883 | -1.38 | 100% | 3 | -4.79% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0803 | -1.37 | 100% | 3 | -4.68% | ✅ consistent |
| d_Performance (YTD) | -0.0803 | -1.21 | 100% | 3 | -3.91% | ✅ consistent |
| d_Price | -0.0802 | -1.11 | 67% | 3 | -4.37% | ✅ consistent |
| true_ret | -0.0776 | -1.29 | 100% | 3 | -4.37% | ✅ consistent |
| d_Forward P/E | -0.0749 | -2.15 | 100% | 3 | -0.59% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0738 | -1.08 | 67% | 3 | -4.46% | ✅ consistent |
| Performance (YTD) | +0.0636 | +0.71 | 50% | 4 | -4.46% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0635 | +1.13 | 100% | 4 | n/a | ✅ consistent |
| d_Performance (Quarter) | -0.0630 | -0.96 | 67% | 3 | -5.28% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0592 | -1.44 | 100% | 3 | -5.33% | ✅ consistent |
| Sales Year Over Year TTM | +0.0559 | +5.30 | 100% | 4 | +0.81% | ✅ consistent |
| d_Market Cap | -0.0537 | -1.95 | 100% | 3 | -5.60% | ✅ consistent |
| exit_price_1d | +0.0522 | +0.94 | 75% | 4 | n/a | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0505 | +4.02 | 100% | 4 | -1.23% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0501 | +0.70 | 50% | 4 | -4.44% | ⚠️ flips / too few dates |
| d_Beta | -0.0486 | -1.02 | 100% | 2 | -0.81% | ✅ consistent |
| Analyst Recom | -0.0417 | -0.71 | 75% | 4 | n/a | ✅ consistent |
| Beta | +0.0414 | +0.40 | 67% | 3 | -0.15% | ✅ consistent |
| Price | +0.0397 | +0.70 | 50% | 4 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0397 | +0.70 | 50% | 4 | n/a | ⚠️ flips / too few dates |
| exit_price_3d | +0.0362 | +0.95 | 100% | 3 | n/a | ✅ consistent |
| upside_pct_lvl | +0.0336 | +0.46 | 75% | 4 | +2.19% | ✅ consistent |
| upside_pct | +0.0336 | +0.46 | 75% | 4 | +2.20% | ✅ consistent |
| d_Institutional Ownership | +0.0301 | +0.94 | 67% | 3 | +0.45% | ✅ consistent |
| 20-Day Simple Moving Average | +0.0300 | +0.42 | 75% | 4 | -5.10% | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -15600926743107926.00 | 100% | 3 | -10.82% | ✅ consistent |
| short_fwd_2d | -0.7281 | -16.95 | 100% | 3 | -9.60% | ✅ consistent |
| short_fwd_1d | -0.4856 | -13.95 | 100% | 3 | -3.62% | ✅ consistent |
| d_Performance (Week) | -0.1372 | -1.58 | 100% | 2 | -3.62% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.1064 | -1.23 | 100% | 2 | -6.57% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.1021 | -1.19 | 100% | 2 | -6.46% | ✅ consistent |
| d_Price | -0.0977 | -1.09 | 100% | 2 | -6.05% | ✅ consistent |
| true_ret | -0.0966 | -1.19 | 100% | 2 | -6.05% | ✅ consistent |
| d_Performance (YTD) | -0.0943 | -1.00 | 100% | 2 | -5.37% | ✅ consistent |
| Performance (Week) | +0.0924 | +1.15 | 100% | 3 | -7.92% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0914 | -1.74 | 100% | 2 | -7.23% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0912 | -1.07 | 100% | 2 | -6.25% | ✅ consistent |
| d_Performance (Month) | -0.0873 | -1.92 | 100% | 2 | -3.01% | ✅ consistent |
| Performance (YTD) | +0.0812 | +1.15 | 67% | 3 | -5.77% | ✅ consistent |
| price_score | -0.0741 | -1.27 | 100% | 2 | -7.68% | ✅ consistent |
| d_Market Cap | -0.0697 | -1.70 | 100% | 2 | -7.22% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0689 | +2.61 | 100% | 3 | -1.42% | ✅ consistent |
| d_Forward P/E | -0.0679 | -3.36 | 100% | 2 | -0.50% | ✅ consistent |
| Sales Year Over Year TTM | +0.0675 | +5.51 | 100% | 3 | +1.10% | ✅ consistent |
| exit_price_3d | +0.0670 | +1.64 | 100% | 3 | n/a | ✅ consistent |
| Beta | +0.0663 | +0.71 | 50% | 2 | -0.08% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0600 | +1.01 | 67% | 3 | -5.73% | ✅ consistent |
| exit_price_2d | +0.0583 | +1.47 | 100% | 3 | n/a | ✅ consistent |
| d_Performance (Quarter) | -0.0582 | -0.51 | 50% | 2 | -7.41% | ⚠️ flips / too few dates |
| Analyst Recom | -0.0582 | -1.10 | 67% | 3 | n/a | ✅ consistent |
| Volatility (Month) | +0.0576 | +1.49 | 100% | 2 | n/a | ✅ consistent |
| 20-Day Simple Moving Average | +0.0516 | +0.92 | 67% | 3 | -6.38% | ✅ consistent |
| exit_price_1d | +0.0490 | +1.21 | 67% | 3 | n/a | ✅ consistent |
| upside_pct_lvl | +0.0453 | +0.68 | 67% | 3 | +2.87% | ✅ consistent |
| upside_pct | +0.0453 | +0.68 | 67% | 3 | +2.88% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

