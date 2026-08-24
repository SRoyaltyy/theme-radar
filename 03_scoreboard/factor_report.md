# Factor report — multi-date aggregate

_Generated 2026-08-24 17:21 EDT from 12 scan dates._

How to read: **IC** = Spearman rank correlation between the factor and the forward return, computed per scan date then averaged (mean IC). **ICIR** = mean/std across dates — the consistency score; |ICIR| above ~0.5 with sign consistency ≥ 2/3 is what we call a real signal. **spread** = average forward return when the factor is positive minus when negative. Factors marked ⚠️ flips sign between dates — treat as noise.

## Coverage (exact date spans)

| Scan date (features) | Deltas vs | 1d label | 2d label | 3d label | Stocks |
|---|---|---|---|---|---|
| 2026-08-06 | — | 2026-08-07 | 2026-08-10 | 2026-08-11 | 11543 |
| 2026-08-07 | 2026-08-06 | 2026-08-10 | 2026-08-11 | 2026-08-12 | 11525 |
| 2026-08-10 | 2026-08-07 | 2026-08-11 | 2026-08-12 | 2026-08-13 | 11533 |
| 2026-08-11 | 2026-08-10 | 2026-08-12 | 2026-08-13 | 2026-08-14 | 11543 |
| 2026-08-12 | 2026-08-11 | 2026-08-13 | 2026-08-14 | 2026-08-17 | 11553 |
| 2026-08-13 | 2026-08-12 | 2026-08-14 | 2026-08-17 | 2026-08-18 | 11566 |
| 2026-08-14 | 2026-08-13 | 2026-08-17 | 2026-08-18 | 2026-08-19 | 11551 |
| 2026-08-17 | 2026-08-14 | 2026-08-18 | 2026-08-19 | 2026-08-20 | 11559 |
| 2026-08-18 | 2026-08-17 | 2026-08-19 | 2026-08-20 | 2026-08-21 | 11572 |
| 2026-08-19 | 2026-08-18 | 2026-08-20 | 2026-08-21 | 2026-08-24 | 11587 |
| 2026-08-20 | 2026-08-19 | 2026-08-21 | 2026-08-24 | — | 11599 |
| 2026-08-21 | 2026-08-20 | 2026-08-24 | — | — | 11602 |

## Composite score effectiveness (total_score IC)

| Scan date | 1d IC | 2d IC | 3d IC |
|---|---|---|---|
| 2026-08-06 | +0.0958 | +0.0636 | +0.0815 |
| 2026-08-07 | -0.0339 | -0.0242 | -0.0009 |
| 2026-08-10 | -0.0491 | -0.0596 | -0.1054 |
| 2026-08-11 | +0.1007 | +0.0174 | +0.0639 |
| 2026-08-12 | -0.0472 | +0.0520 | +0.0878 |
| 2026-08-13 | -0.0908 | -0.1428 | -0.1672 |
| 2026-08-14 | +0.1577 | -0.1560 | -0.1404 |
| 2026-08-17 | -0.2097 | -0.1365 | -0.1034 |
| 2026-08-18 | +0.0486 | +0.0270 | +0.0058 |
| 2026-08-19 | +0.0108 | +0.0519 | +0.1772 |
| 2026-08-20 | -0.0007 | +0.0530 | — |
| 2026-08-21 | -0.0802 | — | — |
- **1d**: mean IC **-0.0082**, ICIR -0.09, sign consistency 58% over 12 dates
- **2d**: mean IC **-0.0231**, ICIR -0.28, sign consistency 45% over 11 dates
- **3d**: mean IC **-0.0101**, ICIR -0.09, sign consistency 50% over 10 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -31201853486215852.00 | 100% | 12 | -6.23% | ✅ consistent |
| short_fwd_2d | -0.6046 | -8.99 | 100% | 11 | -4.67% | ✅ consistent |
| short_fwd_3d | -0.4909 | -4.14 | 100% | 10 | -4.15% | ✅ consistent |
| d_Performance (Quarter) | -0.0700 | -0.55 | 64% | 11 | -1.27% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0630 | -0.64 | 64% | 11 | -1.11% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0597 | -0.61 | 64% | 11 | -1.14% | ⚠️ flips / too few dates |
| true_ret | -0.0592 | -0.64 | 64% | 11 | -1.11% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0560 | -0.58 | 64% | 11 | -1.03% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0558 | -0.56 | 64% | 11 | -0.89% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0552 | -0.60 | 64% | 11 | -0.76% | ⚠️ flips / too few dates |
| Beta | -0.0523 | -0.31 | 55% | 11 | -1.31% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0461 | -0.39 | 73% | 11 | -0.18% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0447 | -0.44 | 73% | 11 | -1.37% | ✅ consistent |
| Volatility (Month) | -0.0439 | -0.38 | 45% | 11 | +0.66% | ⚠️ flips / too few dates |
| d_Price | -0.0437 | -0.44 | 64% | 11 | -1.11% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0412 | -0.57 | 82% | 11 | -1.46% | ✅ consistent |
| Gross Margin | +0.0398 | +0.51 | 58% | 12 | +0.50% | ⚠️ flips / too few dates |
| Profit Margin | +0.0356 | +0.37 | 67% | 12 | -3.94% | ✅ consistent |
| exit_price_1d | +0.0323 | +0.66 | 67% | 12 | n/a | ✅ consistent |
| Market Cap | +0.0281 | +0.70 | 75% | 12 | n/a | ✅ consistent |
| exit_price_2d | +0.0278 | +0.57 | 64% | 11 | n/a | ⚠️ flips / too few dates |
| Forward P/E | -0.0278 | -0.38 | 58% | 12 | n/a | ⚠️ flips / too few dates |
| exit_price_3d | +0.0271 | +0.54 | 60% | 10 | n/a | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0257 | +0.73 | 80% | 10 | +0.62% | ✅ consistent |
| technical_score | -0.0194 | -0.29 | 67% | 12 | -3.44% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0176 | +0.35 | 58% | 12 | -1.52% | ⚠️ flips / too few dates |
| n_pos | -0.0175 | -0.22 | 50% | 12 | n/a | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0158 | +0.36 | 83% | 12 | n/a | ✅ consistent |
| Short Ratio | +0.0153 | +0.20 | 75% | 12 | n/a | ✅ consistent |
| Price | +0.0151 | +0.30 | 58% | 12 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -21123754668153500.00 | 100% | 11 | -9.38% | ✅ consistent |
| short_fwd_3d | -0.7167 | -9.19 | 100% | 10 | -8.01% | ✅ consistent |
| short_fwd_1d | -0.6046 | -8.99 | 100% | 11 | -5.41% | ✅ consistent |
| Beta | -0.0542 | -0.36 | 70% | 10 | -3.09% | ✅ consistent |
| Gross Margin | +0.0481 | +0.63 | 64% | 11 | +0.61% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0469 | -0.38 | 70% | 10 | -1.80% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0452 | -0.40 | 70% | 10 | -2.52% | ✅ consistent |
| d_Forward P/E | -0.0451 | -0.34 | 60% | 10 | -0.26% | ⚠️ flips / too few dates |
| Volatility (Month) | -0.0423 | -0.42 | 70% | 10 | +1.24% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0402 | -0.30 | 70% | 10 | -2.17% | ✅ consistent |
| d_Performance (Month) | -0.0399 | -0.44 | 50% | 10 | -1.72% | ⚠️ flips / too few dates |
| Profit Margin | +0.0397 | +0.56 | 73% | 11 | -7.63% | ✅ consistent |
| exit_price_2d | +0.0383 | +0.64 | 73% | 11 | n/a | ✅ consistent |
| true_ret | -0.0378 | -0.30 | 60% | 10 | -1.96% | ⚠️ flips / too few dates |
| Forward P/E | -0.0364 | -0.55 | 64% | 11 | n/a | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0358 | -0.28 | 70% | 10 | -2.08% | ✅ consistent |
| d_Performance (Quarter) | -0.0353 | -0.31 | 40% | 10 | -1.54% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0347 | -0.28 | 50% | 10 | -1.36% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0340 | +0.57 | 70% | 10 | n/a | ✅ consistent |
| d_Market Cap | -0.0337 | -0.40 | 60% | 10 | -3.55% | ⚠️ flips / too few dates |
| Market Cap | +0.0329 | +0.76 | 73% | 11 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0327 | -0.23 | 60% | 10 | -0.69% | ⚠️ flips / too few dates |
| price_score | -0.0323 | -0.38 | 50% | 10 | -3.29% | ⚠️ flips / too few dates |
| d_Price | -0.0314 | -0.25 | 60% | 10 | -1.96% | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0285 | +0.56 | 67% | 9 | +0.95% | ✅ consistent |
| exit_price_1d | +0.0263 | +0.43 | 64% | 11 | n/a | ⚠️ flips / too few dates |
| n_pos | -0.0250 | -0.25 | 64% | 11 | n/a | ⚠️ flips / too few dates |
| total_score | -0.0231 | -0.28 | 45% | 11 | -1.74% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0229 | +0.45 | 73% | 11 | -3.22% | ✅ consistent |
| 50-Day Simple Moving Average | +0.0226 | +0.26 | 55% | 11 | -3.80% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -16444820705884542.00 | 100% | 10 | -11.76% | ✅ consistent |
| short_fwd_2d | -0.7167 | -9.19 | 100% | 10 | -8.59% | ✅ consistent |
| short_fwd_1d | -0.4909 | -4.14 | 100% | 10 | -4.68% | ✅ consistent |
| Beta | -0.0799 | -0.47 | 56% | 9 | -4.76% | ⚠️ flips / too few dates |
| Volatility (Month) | -0.0606 | -0.56 | 56% | 9 | +2.17% | ⚠️ flips / too few dates |
| Gross Margin | +0.0532 | +0.88 | 80% | 10 | +1.57% | ✅ consistent |
| Profit Margin | +0.0488 | +0.63 | 80% | 10 | -9.62% | ✅ consistent |
| d_Performance (Week) | -0.0466 | -0.30 | 67% | 9 | -0.34% | ✅ consistent |
| exit_price_3d | +0.0424 | +0.66 | 70% | 10 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0418 | -0.36 | 67% | 9 | -1.91% | ✅ consistent |
| Forward P/E | -0.0378 | -0.53 | 50% | 10 | n/a | ⚠️ flips / too few dates |
| Market Cap | +0.0344 | +0.88 | 80% | 10 | n/a | ✅ consistent |
| exit_price_2d | +0.0322 | +0.49 | 70% | 10 | n/a | ✅ consistent |
| Performance (Month) | -0.0317 | -0.47 | 70% | 10 | -5.05% | ✅ consistent |
| 20-Day Simple Moving Average | -0.0276 | -0.24 | 50% | 10 | -5.56% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0272 | +0.46 | 60% | 10 | -4.72% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0259 | +0.47 | 60% | 10 | -1.63% | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0234 | +0.41 | 50% | 8 | +1.44% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0233 | -0.19 | 67% | 9 | -0.31% | ✅ consistent |
| Average Volume | -0.0233 | -0.61 | 60% | 10 | n/a | ⚠️ flips / too few dates |
| exit_price_1d | +0.0229 | +0.34 | 60% | 10 | n/a | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0202 | -0.14 | 56% | 9 | -1.93% | ⚠️ flips / too few dates |
| Short Ratio | +0.0194 | +0.54 | 70% | 10 | n/a | ✅ consistent |
| price_score | -0.0189 | -0.17 | 56% | 9 | -3.36% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0183 | -0.23 | 67% | 9 | -3.93% | ✅ consistent |
| w_pos | -0.0175 | -0.18 | 40% | 10 | n/a | ⚠️ flips / too few dates |
| Analyst Recom | -0.0172 | -0.32 | 60% | 10 | n/a | ⚠️ flips / too few dates |
| Total Debt/Equity | -0.0172 | -0.29 | 67% | 9 | n/a | ✅ consistent |
| Insider Transactions | +0.0164 | +0.27 | 40% | 10 | +0.40% | ⚠️ flips / too few dates |
| d_Institutional Transactions | -0.0158 | -1.60 | 100% | 2 | +1.56% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

