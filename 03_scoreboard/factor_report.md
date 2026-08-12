# Factor report — multi-date aggregate

_Generated 2026-08-12 17:36 EDT from 4 scan dates._

How to read: **IC** = Spearman rank correlation between the factor and the forward return, computed per scan date then averaged (mean IC). **ICIR** = mean/std across dates — the consistency score; |ICIR| above ~0.5 with sign consistency ≥ 2/3 is what we call a real signal. **spread** = average forward return when the factor is positive minus when negative. Factors marked ⚠️ flips sign between dates — treat as noise.

## Coverage (exact date spans)

| Scan date (features) | Deltas vs | 1d label | 2d label | 3d label | Stocks |
|---|---|---|---|---|---|
| 2026-08-06 | — | 2026-08-07 | 2026-08-10 | 2026-08-11 | 11543 |
| 2026-08-07 | 2026-08-06 | 2026-08-10 | 2026-08-11 | 2026-08-12 | 11525 |
| 2026-08-10 | 2026-08-07 | 2026-08-11 | 2026-08-12 | — | 11533 |
| 2026-08-11 | 2026-08-10 | 2026-08-12 | — | — | 11543 |

## Composite score effectiveness (total_score IC)

| Scan date | 1d IC | 2d IC | 3d IC |
|---|---|---|---|
| 2026-08-06 | +0.0958 | +0.0636 | +0.0815 |
| 2026-08-07 | -0.0339 | -0.0242 | -0.0009 |
| 2026-08-10 | -0.0491 | -0.0596 | — |
| 2026-08-11 | +0.1007 | — | — |
- **1d**: mean IC **+0.0284**, ICIR +0.40, sign consistency 50% over 4 dates
- **2d**: mean IC **-0.0067**, ICIR -0.13, sign consistency 67% over 3 dates
- **3d**: mean IC **+0.0403**, ICIR +0.98, sign consistency 50% over 2 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -18014398509481984.00 | 100% | 4 | -6.63% | ✅ consistent |
| short_fwd_2d | -0.6233 | -19.51 | 100% | 3 | -5.90% | ✅ consistent |
| short_fwd_3d | -0.4969 | -13.11 | 100% | 2 | -6.07% | ✅ consistent |
| d_Performance (Week) | -0.1064 | -5.96 | 100% | 3 | -2.58% | ✅ consistent |
| d_Performance (Quarter) | -0.0792 | -1.89 | 100% | 3 | -5.05% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0588 | -1.37 | 67% | 3 | -3.95% | ✅ consistent |
| true_ret | -0.0535 | -0.99 | 67% | 3 | -3.44% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0526 | -0.86 | 67% | 3 | -3.83% | ✅ consistent |
| d_Performance (YTD) | -0.0517 | -0.88 | 67% | 3 | -3.11% | ✅ consistent |
| Analyst Recom | -0.0514 | -3.75 | 100% | 4 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0506 | -1.02 | 67% | 3 | -3.84% | ✅ consistent |
| upside_pct_lvl | +0.0492 | +0.73 | 75% | 4 | +1.48% | ✅ consistent |
| upside_pct | +0.0492 | +0.73 | 75% | 4 | +1.48% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0470 | +3.30 | 100% | 4 | -0.71% | ✅ consistent |
| Sales Year Over Year TTM | +0.0462 | +3.96 | 100% | 4 | +0.36% | ✅ consistent |
| d_Performance (Month) | +0.0435 | +0.58 | 67% | 3 | -1.60% | ✅ consistent |
| exit_price_1d | +0.0430 | +0.73 | 75% | 4 | n/a | ✅ consistent |
| d_Price | -0.0428 | -0.69 | 67% | 3 | -3.44% | ✅ consistent |
| Performance (YTD) | +0.0412 | +0.36 | 50% | 4 | -2.54% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0385 | -2.13 | 100% | 3 | -0.21% | ✅ consistent |
| w_pos | +0.0382 | +0.61 | 75% | 4 | n/a | ✅ consistent |
| catalyst_score | +0.0379 | +1.15 | 75% | 4 | -0.40% | ✅ consistent |
| n_catalysts | +0.0379 | +1.15 | 75% | 4 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0371 | -1.27 | 100% | 3 | -4.45% | ✅ consistent |
| Forward P/E | +0.0356 | +0.91 | 75% | 4 | n/a | ✅ consistent |
| 20-Day Simple Moving Average | +0.0335 | +0.52 | 50% | 4 | -3.02% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0334 | -1.89 | 100% | 3 | -4.74% | ✅ consistent |
| Short Float | +0.0324 | +0.36 | 75% | 4 | n/a | ✅ consistent |
| d_Beta | -0.0289 | -0.55 | 50% | 2 | -0.73% | ⚠️ flips / too few dates |
| total_score | +0.0284 | +0.40 | 50% | 4 | -1.89% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -11031521092846172.00 | 100% | 3 | -10.21% | ✅ consistent |
| short_fwd_3d | -0.7445 | -16.81 | 100% | 2 | -10.45% | ✅ consistent |
| short_fwd_1d | -0.6233 | -19.51 | 100% | 3 | -4.64% | ✅ consistent |
| d_Price | -0.1260 | -3.25 | 100% | 2 | -6.29% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.1240 | -2.57 | 100% | 2 | -6.94% | ✅ consistent |
| d_Performance (YTD) | -0.1183 | -2.52 | 100% | 2 | -5.52% | ✅ consistent |
| d_Performance (Week) | -0.1172 | -3.27 | 100% | 2 | -3.90% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.1164 | -2.97 | 100% | 2 | -6.62% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.1144 | -2.78 | 100% | 2 | -6.86% | ✅ consistent |
| true_ret | -0.1126 | -2.71 | 100% | 2 | -6.29% | ✅ consistent |
| d_Performance (Quarter) | -0.0972 | -1.77 | 100% | 2 | -7.88% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0795 | -2.22 | 100% | 2 | -7.64% | ✅ consistent |
| Analyst Recom | -0.0749 | -4.73 | 100% | 3 | n/a | ✅ consistent |
| d_Forward P/E | -0.0722 | -1.71 | 100% | 2 | -0.49% | ✅ consistent |
| upside_pct_lvl | +0.0684 | +1.43 | 100% | 3 | +2.73% | ✅ consistent |
| upside_pct | +0.0684 | +1.43 | 100% | 3 | +2.74% | ✅ consistent |
| Performance (Week) | +0.0669 | +0.79 | 67% | 3 | -8.13% | ✅ consistent |
| d_Market Cap | -0.0621 | -2.04 | 100% | 2 | -7.61% | ✅ consistent |
| Sales Year Over Year TTM | +0.0586 | +5.38 | 100% | 3 | +0.66% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0578 | +39.74 | 100% | 3 | -1.44% | ✅ consistent |
| price_score | -0.0545 | -1.40 | 100% | 2 | -7.60% | ✅ consistent |
| 20-Day Simple Moving Average | +0.0526 | +0.77 | 100% | 3 | -6.26% | ✅ consistent |
| Performance (YTD) | +0.0412 | +0.44 | 33% | 3 | -5.65% | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0402 | +nan | 100% | 1 | +0.49% | ⚠️ flips / too few dates |
| Profit Margin | -0.0394 | -0.85 | 67% | 3 | -13.52% | ✅ consistent |
| catalyst_score | +0.0392 | +1.98 | 100% | 3 | -1.24% | ✅ consistent |
| n_catalysts | +0.0392 | +1.98 | 100% | 3 | n/a | ✅ consistent |
| Institutional Transactions | +0.0388 | +2.29 | 100% | 3 | +6.71% | ✅ consistent |
| Total Debt/Equity | -0.0385 | -0.75 | 50% | 2 | n/a | ⚠️ flips / too few dates |
| exit_price_2d | +0.0374 | +0.98 | 100% | 3 | n/a | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -12738103345051544.00 | 100% | 2 | -12.37% | ✅ consistent |
| short_fwd_2d | -0.7445 | -16.81 | 100% | 2 | -11.83% | ✅ consistent |
| short_fwd_1d | -0.4969 | -13.11 | 100% | 2 | -3.81% | ✅ consistent |
| Performance (Week) | +0.1318 | +1.86 | 100% | 2 | -11.62% | ✅ consistent |
| Analyst Recom | -0.0947 | -6.89 | 100% | 2 | n/a | ✅ consistent |
| 20-Day Simple Moving Average | +0.0853 | +2.30 | 100% | 2 | -9.00% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0838 | +4.29 | 100% | 2 | -2.12% | ✅ consistent |
| upside_pct | +0.0807 | +1.52 | 100% | 2 | +3.79% | ✅ consistent |
| upside_pct_lvl | +0.0807 | +1.52 | 100% | 2 | +3.76% | ✅ consistent |
| Sales Year Over Year TTM | +0.0728 | +6.06 | 100% | 2 | +0.99% | ✅ consistent |
| Performance (YTD) | +0.0653 | +0.80 | 50% | 2 | -8.12% | ⚠️ flips / too few dates |
| Total Debt/Equity | -0.0594 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| d_Performance (Quarter) | +0.0561 | +nan | 100% | 1 | -14.21% | ⚠️ flips / too few dates |
| Forward P/E | +0.0547 | +5.56 | 100% | 2 | n/a | ✅ consistent |
| Profit Margin | -0.0541 | -0.90 | 50% | 2 | -19.70% | ⚠️ flips / too few dates |
| catalyst_score | +0.0536 | +101.96 | 100% | 2 | -1.63% | ✅ consistent |
| n_catalysts | +0.0536 | +94.41 | 100% | 2 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0502 | +nan | 100% | 1 | -6.92% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0481 | +1.28 | 100% | 2 | n/a | ✅ consistent |
| d_Forward P/E | -0.0477 | +nan | 100% | 1 | -0.41% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0470 | +3.07 | 100% | 2 | n/a | ✅ consistent |
| technical_score | +0.0469 | +1.62 | 100% | 2 | -16.75% | ✅ consistent |
| w_pos | +0.0461 | +1.23 | 100% | 2 | n/a | ✅ consistent |
| Institutional Transactions | +0.0453 | +1114.22 | 100% | 2 | +9.83% | ✅ consistent |
| d_Performance (Month) | -0.0417 | +nan | 100% | 1 | -5.05% | ⚠️ flips / too few dates |
| n_neg | -0.0413 | -1.69 | 100% | 2 | n/a | ✅ consistent |
| d_Sales Growth Quarter Over Quarter | +0.0406 | +nan | 100% | 1 | +1.92% | ⚠️ flips / too few dates |
| total_score | +0.0403 | +0.98 | 50% | 2 | -4.77% | ⚠️ flips / too few dates |
| cat_copper_metals | +0.0400 | +2.09 | 100% | 2 | n/a | ✅ consistent |
| exit_price_2d | +0.0399 | +1.08 | 100% | 2 | n/a | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

