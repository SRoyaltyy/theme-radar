# Factor report — multi-date aggregate

_Generated 2026-09-03 18:56 EDT from 19 scan dates._

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
| 2026-08-20 | 2026-08-19 | 2026-08-21 | 2026-08-24 | 2026-08-25 | 11599 |
| 2026-08-21 | 2026-08-20 | 2026-08-24 | 2026-08-25 | 2026-08-26 | 11602 |
| 2026-08-24 | 2026-08-21 | 2026-08-25 | 2026-08-26 | 2026-08-28 | 11605 |
| 2026-08-25 | 2026-08-24 | 2026-08-26 | 2026-08-28 | 2026-08-31 | 11611 |
| 2026-08-26 | 2026-08-25 | 2026-08-28 | 2026-08-31 | 2026-09-01 | 11620 |
| 2026-08-28 | 2026-08-26 | 2026-08-31 | 2026-09-01 | 2026-09-02 | 11611 |
| 2026-08-31 | 2026-08-28 | 2026-09-01 | 2026-09-02 | 2026-09-03 | 11617 |
| 2026-09-01 | 2026-08-31 | 2026-09-02 | 2026-09-03 | — | 11620 |
| 2026-09-02 | 2026-09-01 | 2026-09-03 | — | — | 11629 |

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
| 2026-08-20 | -0.0007 | +0.0530 | +0.0387 |
| 2026-08-21 | -0.0802 | +0.0158 | -0.0723 |
| 2026-08-24 | +0.0056 | -0.0285 | -0.0880 |
| 2026-08-25 | -0.0503 | -0.1093 | -0.0661 |
| 2026-08-26 | -0.0710 | -0.0146 | -0.0019 |
| 2026-08-28 | -0.0442 | +0.0258 | +0.0108 |
| 2026-08-31 | -0.0065 | +0.0398 | +0.1004 |
| 2026-09-01 | -0.0847 | -0.2394 | — |
| 2026-09-02 | -0.0842 | — | — |
- **1d**: mean IC **-0.0228**, ICIR -0.28, sign consistency 68% over 19 dates
- **2d**: mean IC **-0.0314**, ICIR -0.36, sign consistency 50% over 18 dates
- **3d**: mean IC **-0.0106**, ICIR -0.11, sign consistency 53% over 17 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -22667621032929524.00 | 100% | 19 | -6.25% | ✅ consistent |
| short_fwd_2d | -0.6098 | -8.10 | 100% | 18 | -4.99% | ✅ consistent |
| short_fwd_3d | -0.4785 | -4.05 | 100% | 17 | -4.35% | ✅ consistent |
| d_Performance (Week) | -0.0639 | -0.68 | 67% | 18 | -0.77% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0619 | -0.63 | 61% | 18 | -0.78% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0590 | -0.57 | 56% | 18 | -0.78% | ⚠️ flips / too few dates |
| true_ret | -0.0569 | -0.57 | 56% | 18 | -0.89% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0544 | -0.53 | 56% | 18 | -0.96% | ⚠️ flips / too few dates |
| Volatility (Month) | -0.0535 | -0.42 | 50% | 18 | +0.66% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0533 | -0.57 | 56% | 18 | -0.53% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0463 | -0.37 | 56% | 18 | -1.05% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0448 | -0.48 | 72% | 18 | -1.17% | ✅ consistent |
| Forward P/E | -0.0447 | -0.51 | 68% | 19 | n/a | ✅ consistent |
| d_Forward P/E | -0.0443 | -0.41 | 72% | 18 | -0.24% | ✅ consistent |
| Profit Margin | +0.0421 | +0.44 | 68% | 19 | -2.87% | ✅ consistent |
| exit_price_1d | +0.0419 | +0.65 | 68% | 19 | n/a | ✅ consistent |
| d_Market Cap | -0.0402 | -0.55 | 72% | 18 | -0.98% | ✅ consistent |
| d_Price | -0.0399 | -0.38 | 56% | 18 | -0.89% | ⚠️ flips / too few dates |
| Beta | -0.0381 | -0.21 | 56% | 18 | -1.51% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0345 | -0.25 | 63% | 19 | -1.76% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0336 | +0.59 | 67% | 18 | n/a | ✅ consistent |
| Market Cap | +0.0332 | +0.62 | 74% | 19 | n/a | ✅ consistent |
| Gross Margin | +0.0331 | +0.51 | 63% | 19 | -0.93% | ⚠️ flips / too few dates |
| n_pos | -0.0327 | -0.41 | 58% | 19 | n/a | ⚠️ flips / too few dates |
| exit_price_3d | +0.0314 | +0.54 | 65% | 17 | n/a | ⚠️ flips / too few dates |
| price_score | -0.0307 | -0.33 | 67% | 18 | -1.15% | ✅ consistent |
| d_Volatility (Month) | +0.0266 | +0.52 | 65% | 17 | +0.97% | ⚠️ flips / too few dates |
| Price | +0.0256 | +0.39 | 63% | 19 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0256 | +0.39 | 63% | 19 | n/a | ⚠️ flips / too few dates |
| Average Volume | -0.0255 | -0.40 | 63% | 19 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -17089958990371628.00 | 100% | 18 | -9.76% | ✅ consistent |
| short_fwd_3d | -0.7150 | -8.23 | 100% | 17 | -8.46% | ✅ consistent |
| short_fwd_1d | -0.6098 | -8.10 | 100% | 18 | -5.71% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0710 | -0.54 | 76% | 17 | -1.38% | ✅ consistent |
| Volatility (Month) | -0.0683 | -0.57 | 71% | 17 | +1.24% | ✅ consistent |
| Forward P/E | -0.0683 | -0.80 | 72% | 18 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0649 | -0.45 | 65% | 17 | -1.60% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0602 | -0.43 | 71% | 17 | -2.03% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0601 | -0.59 | 76% | 17 | -2.27% | ✅ consistent |
| true_ret | -0.0597 | -0.44 | 65% | 17 | -1.72% | ⚠️ flips / too few dates |
| Beta | -0.0595 | -0.35 | 71% | 17 | -3.28% | ✅ consistent |
| d_Performance (Week) | -0.0589 | -0.42 | 59% | 17 | -0.48% | ⚠️ flips / too few dates |
| d_Price | -0.0565 | -0.41 | 65% | 17 | -1.72% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0564 | -0.43 | 65% | 17 | -1.02% | ⚠️ flips / too few dates |
| Profit Margin | +0.0548 | +0.74 | 78% | 18 | -5.42% | ✅ consistent |
| d_Market Cap | -0.0502 | -0.55 | 71% | 17 | -2.76% | ✅ consistent |
| d_Forward P/E | -0.0499 | -0.40 | 65% | 17 | -0.41% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0472 | +0.84 | 83% | 18 | n/a | ✅ consistent |
| Gross Margin | +0.0467 | +0.73 | 72% | 18 | -1.79% | ✅ consistent |
| exit_price_3d | +0.0414 | +0.78 | 76% | 17 | n/a | ✅ consistent |
| n_pos | -0.0394 | -0.43 | 67% | 18 | n/a | ✅ consistent |
| price_score | -0.0388 | -0.38 | 47% | 17 | -2.60% | ⚠️ flips / too few dates |
| Market Cap | +0.0368 | +0.72 | 72% | 18 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0367 | -0.34 | 41% | 17 | -1.58% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0358 | +0.64 | 72% | 18 | n/a | ✅ consistent |
| d_Volatility (Month) | +0.0326 | +0.58 | 69% | 16 | +1.69% | ✅ consistent |
| w_pos | -0.0325 | -0.39 | 56% | 18 | n/a | ⚠️ flips / too few dates |
| Average Volume | -0.0315 | -0.54 | 67% | 18 | n/a | ✅ consistent |
| total_score | -0.0314 | -0.36 | 50% | 18 | -1.57% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0276 | -0.23 | 47% | 17 | -1.24% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -13130136390420290.00 | 100% | 17 | -12.15% | ✅ consistent |
| short_fwd_2d | -0.7150 | -8.23 | 100% | 17 | -8.97% | ✅ consistent |
| short_fwd_1d | -0.4785 | -4.05 | 100% | 17 | -5.01% | ✅ consistent |
| Volatility (Month) | -0.0931 | -0.84 | 69% | 16 | +2.17% | ✅ consistent |
| Beta | -0.0843 | -0.54 | 56% | 16 | -5.22% | ⚠️ flips / too few dates |
| Forward P/E | -0.0782 | -0.94 | 71% | 17 | n/a | ✅ consistent |
| Profit Margin | +0.0660 | +0.91 | 82% | 17 | -7.14% | ✅ consistent |
| Gross Margin | +0.0549 | +1.12 | 88% | 17 | -2.15% | ✅ consistent |
| exit_price_3d | +0.0515 | +0.91 | 82% | 17 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0461 | -0.37 | 75% | 16 | +0.06% | ✅ consistent |
| exit_price_2d | +0.0420 | +0.73 | 82% | 17 | n/a | ✅ consistent |
| Average Volume | -0.0418 | -0.81 | 71% | 17 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0379 | -0.32 | 62% | 16 | -1.07% | ⚠️ flips / too few dates |
| Market Cap | +0.0366 | +0.81 | 82% | 17 | n/a | ✅ consistent |
| valuation_score | -0.0352 | -0.54 | 71% | 17 | +2.75% | ✅ consistent |
| Short Float | -0.0346 | -0.40 | 65% | 17 | n/a | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0346 | +0.43 | 47% | 17 | -4.37% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0343 | +0.40 | 59% | 17 | n/a | ⚠️ flips / too few dates |
| exit_price_1d | +0.0332 | +0.56 | 71% | 17 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0304 | -0.33 | 75% | 16 | -1.33% | ✅ consistent |
| d_Market Cap | -0.0299 | -0.40 | 69% | 16 | -2.82% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0292 | +0.30 | 65% | 17 | -5.08% | ⚠️ flips / too few dates |
| w_pos | -0.0283 | -0.29 | 53% | 17 | n/a | ⚠️ flips / too few dates |
| upside_pct | -0.0281 | -0.34 | 71% | 17 | +2.57% | ✅ consistent |
| upside_pct_lvl | -0.0281 | -0.34 | 71% | 17 | +2.56% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0280 | -0.24 | 56% | 16 | -1.26% | ⚠️ flips / too few dates |
| n_pos | -0.0280 | -0.28 | 53% | 17 | n/a | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0265 | -0.28 | 62% | 16 | -2.05% | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0261 | +0.51 | 67% | 15 | +2.37% | ✅ consistent |
| n_catalysts | -0.0257 | -0.54 | 71% | 17 | n/a | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

