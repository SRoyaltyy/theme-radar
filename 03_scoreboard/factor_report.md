# Factor report — multi-date aggregate

_Generated 2026-10-01 17:29 EDT from 38 scan dates._

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
| 2026-09-01 | 2026-08-31 | 2026-09-02 | 2026-09-03 | 2026-09-04 | 11620 |
| 2026-09-02 | 2026-09-01 | 2026-09-03 | 2026-09-04 | 2026-09-08 | 11629 |
| 2026-09-03 | 2026-09-02 | 2026-09-04 | 2026-09-08 | 2026-09-09 | 11630 |
| 2026-09-04 | 2026-09-03 | 2026-09-08 | 2026-09-09 | 2026-09-10 | 11593 |
| 2026-09-08 | — | 2026-09-09 | 2026-09-10 | 2026-09-11 | 11595 |
| 2026-09-09 | 2026-09-08 | 2026-09-10 | 2026-09-11 | 2026-09-14 | 11599 |
| 2026-09-10 | 2026-09-09 | 2026-09-11 | 2026-09-14 | 2026-09-15 | 11616 |
| 2026-09-11 | 2026-09-10 | 2026-09-14 | 2026-09-15 | 2026-09-16 | 11598 |
| 2026-09-14 | 2026-09-11 | 2026-09-15 | 2026-09-16 | 2026-09-17 | 11604 |
| 2026-09-15 | 2026-09-14 | 2026-09-16 | 2026-09-17 | 2026-09-18 | 11621 |
| 2026-09-16 | 2026-09-15 | 2026-09-17 | 2026-09-18 | 2026-09-21 | 11627 |
| 2026-09-17 | 2026-09-16 | 2026-09-18 | 2026-09-21 | 2026-09-22 | 11636 |
| 2026-09-18 | 2026-09-17 | 2026-09-21 | 2026-09-22 | 2026-09-23 | 11629 |
| 2026-09-21 | 2026-09-18 | 2026-09-22 | 2026-09-23 | 2026-09-24 | 11629 |
| 2026-09-22 | 2026-09-21 | 2026-09-23 | 2026-09-24 | 2026-09-25 | 11637 |
| 2026-09-23 | 2026-09-22 | 2026-09-24 | 2026-09-25 | 2026-09-28 | 11653 |
| 2026-09-24 | 2026-09-23 | 2026-09-25 | 2026-09-28 | 2026-09-29 | 11660 |
| 2026-09-25 | 2026-09-24 | 2026-09-28 | 2026-09-29 | 2026-09-30 | 11665 |
| 2026-09-28 | 2026-09-25 | 2026-09-29 | 2026-09-30 | 2026-10-01 | 11668 |
| 2026-09-29 | 2026-09-28 | 2026-09-30 | 2026-10-01 | — | 11673 |
| 2026-09-30 | 2026-09-29 | 2026-10-01 | — | — | 11682 |

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
| 2026-09-01 | -0.0847 | -0.2394 | -0.2756 |
| 2026-09-02 | -0.0842 | -0.1304 | -0.1700 |
| 2026-09-03 | -0.0656 | -0.0607 | -0.1049 |
| 2026-09-04 | -0.0292 | -0.0659 | -0.1272 |
| 2026-09-08 | -0.0849 | -0.1276 | -0.0619 |
| 2026-09-09 | -0.0163 | +0.0188 | -0.0591 |
| 2026-09-10 | -0.0932 | +0.1308 | +0.1827 |
| 2026-09-11 | -0.0419 | -0.0676 | -0.1072 |
| 2026-09-14 | -0.0250 | -0.1114 | -0.2010 |
| 2026-09-15 | -0.0616 | -0.1290 | -0.1450 |
| 2026-09-16 | -0.0722 | -0.0629 | -0.0266 |
| 2026-09-17 | +0.0987 | +0.2454 | +0.3070 |
| 2026-09-18 | +0.0668 | +0.0651 | +0.1188 |
| 2026-09-21 | +0.1709 | -0.0452 | -0.0110 |
| 2026-09-22 | -0.1323 | -0.1167 | -0.0566 |
| 2026-09-23 | +0.0928 | +0.0398 | +0.0444 |
| 2026-09-24 | -0.0345 | +0.0435 | +0.0182 |
| 2026-09-25 | -0.1114 | -0.0598 | -0.0952 |
| 2026-09-28 | -0.0477 | -0.0469 | -0.0752 |
| 2026-09-29 | -0.0367 | +0.0392 | — |
| 2026-09-30 | +0.0026 | — | — |
- **1d**: mean IC **-0.0225**, ICIR -0.29, sign consistency 71% over 38 dates
- **2d**: mean IC **-0.0272**, ICIR -0.30, sign consistency 57% over 37 dates
- **3d**: mean IC **-0.0285**, ICIR -0.24, sign consistency 64% over 36 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -17558263751735406.00 | 100% | 38 | -6.02% | ✅ consistent |
| short_fwd_2d | -0.6190 | -7.47 | 100% | 37 | -4.97% | ✅ consistent |
| short_fwd_3d | -0.4969 | -4.59 | 100% | 36 | -4.52% | ✅ consistent |
| Volatility (Month) | -0.0679 | -0.55 | 65% | 37 | +0.45% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0599 | -0.55 | 67% | 36 | -0.55% | ✅ consistent |
| exit_price_1d | +0.0516 | +0.72 | 71% | 38 | n/a | ✅ consistent |
| exit_price_3d | +0.0496 | +0.74 | 72% | 36 | n/a | ✅ consistent |
| Profit Margin | +0.0474 | +0.48 | 68% | 38 | -2.49% | ✅ consistent |
| exit_price_2d | +0.0473 | +0.70 | 70% | 37 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0443 | -0.43 | 56% | 36 | -0.49% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0428 | -0.42 | 58% | 36 | -0.46% | ⚠️ flips / too few dates |
| valuation_score | -0.0416 | -0.49 | 74% | 38 | +0.93% | ✅ consistent |
| Average Volume | -0.0412 | -0.71 | 74% | 38 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0411 | -0.42 | 56% | 36 | -0.31% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0396 | -0.39 | 58% | 36 | -0.60% | ⚠️ flips / too few dates |
| true_ret | -0.0388 | -0.39 | 56% | 36 | -0.63% | ⚠️ flips / too few dates |
| n_pos | -0.0383 | -0.45 | 66% | 38 | n/a | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0373 | +0.42 | 66% | 38 | -1.54% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0365 | -0.42 | 67% | 36 | -0.69% | ✅ consistent |
| upside_pct | -0.0360 | -0.28 | 61% | 38 | +0.88% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0360 | -0.28 | 61% | 38 | +0.88% | ⚠️ flips / too few dates |
| Price | +0.0359 | +0.50 | 63% | 38 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0359 | +0.50 | 63% | 38 | n/a | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0356 | +0.45 | 63% | 38 | -1.47% | ⚠️ flips / too few dates |
| Market Cap | +0.0345 | +0.53 | 68% | 38 | n/a | ✅ consistent |
| Beta | -0.0326 | -0.17 | 54% | 37 | -2.27% | ⚠️ flips / too few dates |
| d_Price | -0.0320 | -0.31 | 56% | 36 | -0.63% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0316 | -0.51 | 69% | 36 | -0.54% | ✅ consistent |
| d_Performance (Quarter) | -0.0314 | -0.26 | 58% | 36 | -0.63% | ⚠️ flips / too few dates |
| w_pos | -0.0311 | -0.35 | 68% | 38 | n/a | ✅ consistent |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -15816122105150720.00 | 100% | 37 | -9.32% | ✅ consistent |
| short_fwd_3d | -0.7357 | -10.33 | 100% | 36 | -8.37% | ✅ consistent |
| short_fwd_1d | -0.6190 | -7.47 | 100% | 37 | -5.48% | ✅ consistent |
| Volatility (Month) | -0.0923 | -0.75 | 75% | 36 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0671 | +1.04 | 84% | 37 | n/a | ✅ consistent |
| exit_price_3d | +0.0652 | +1.02 | 81% | 36 | n/a | ✅ consistent |
| Profit Margin | +0.0599 | +0.67 | 76% | 37 | -4.60% | ✅ consistent |
| valuation_score | -0.0576 | -0.76 | 70% | 37 | +1.67% | ✅ consistent |
| Average Volume | -0.0564 | -1.02 | 84% | 37 | n/a | ✅ consistent |
| exit_price_1d | +0.0560 | +0.86 | 76% | 37 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0508 | +0.60 | 73% | 37 | -2.76% | ✅ consistent |
| upside_pct | -0.0481 | -0.37 | 57% | 37 | +1.57% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0481 | -0.37 | 57% | 37 | +1.57% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0480 | +0.55 | 73% | 37 | -2.87% | ✅ consistent |
| Beta | -0.0463 | -0.25 | 67% | 36 | -4.06% | ✅ consistent |
| n_pos | -0.0453 | -0.47 | 70% | 37 | n/a | ✅ consistent |
| Price | +0.0446 | +0.67 | 73% | 37 | n/a | ✅ consistent |
| entry_price | +0.0446 | +0.67 | 73% | 37 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0430 | -0.31 | 60% | 35 | -0.57% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0429 | -0.34 | 66% | 35 | -1.01% | ⚠️ flips / too few dates |
| w_pos | -0.0418 | -0.44 | 68% | 37 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0408 | -0.31 | 60% | 35 | -1.09% | ⚠️ flips / too few dates |
| Market Cap | +0.0400 | +0.65 | 73% | 37 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0384 | -0.37 | 63% | 35 | -1.49% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0378 | -0.30 | 57% | 35 | -0.81% | ⚠️ flips / too few dates |
| Short Float | -0.0364 | -0.36 | 65% | 37 | n/a | ⚠️ flips / too few dates |
| Gross Margin | +0.0358 | +0.53 | 73% | 37 | -5.03% | ✅ consistent |
| d_Performance (YTD) | -0.0346 | -0.27 | 63% | 35 | -1.37% | ⚠️ flips / too few dates |
| true_ret | -0.0337 | -0.27 | 57% | 35 | -1.31% | ⚠️ flips / too few dates |
| d_Price | -0.0332 | -0.26 | 60% | 35 | -1.31% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -18014398509481984.00 | 100% | 36 | -11.90% | ✅ consistent |
| short_fwd_2d | -0.7357 | -10.33 | 100% | 36 | -8.43% | ✅ consistent |
| short_fwd_1d | -0.4969 | -4.59 | 100% | 36 | -4.86% | ✅ consistent |
| Volatility (Month) | -0.1117 | -0.91 | 74% | 35 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0770 | +1.22 | 89% | 36 | n/a | ✅ consistent |
| Profit Margin | +0.0698 | +0.79 | 81% | 36 | -6.07% | ✅ consistent |
| valuation_score | -0.0697 | -0.95 | 83% | 36 | +2.24% | ✅ consistent |
| exit_price_2d | +0.0679 | +1.05 | 89% | 36 | n/a | ✅ consistent |
| Average Volume | -0.0676 | -1.28 | 83% | 36 | n/a | ✅ consistent |
| exit_price_1d | +0.0589 | +0.90 | 81% | 36 | n/a | ✅ consistent |
| upside_pct | -0.0581 | -0.45 | 69% | 36 | +2.11% | ✅ consistent |
| upside_pct_lvl | -0.0581 | -0.45 | 69% | 36 | +2.10% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0580 | +0.63 | 69% | 36 | -3.73% | ✅ consistent |
| Beta | -0.0573 | -0.32 | 63% | 35 | -5.67% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0543 | +0.59 | 78% | 36 | -3.86% | ✅ consistent |
| d_Performance (Week) | -0.0517 | -0.34 | 74% | 34 | -0.44% | ✅ consistent |
| Price | +0.0493 | +0.74 | 72% | 36 | n/a | ✅ consistent |
| entry_price | +0.0493 | +0.74 | 72% | 36 | n/a | ✅ consistent |
| w_pos | -0.0486 | -0.44 | 72% | 36 | n/a | ✅ consistent |
| n_pos | -0.0476 | -0.43 | 69% | 36 | n/a | ✅ consistent |
| Short Float | -0.0467 | -0.50 | 69% | 36 | n/a | ✅ consistent |
| Market Cap | +0.0426 | +0.71 | 75% | 36 | n/a | ✅ consistent |
| Relative Strength Index (14) | +0.0406 | +0.47 | 61% | 36 | n/a | ⚠️ flips / too few dates |
| Gross Margin | +0.0398 | +0.63 | 75% | 36 | -6.60% | ✅ consistent |
| 50-Day Simple Moving Average | +0.0371 | +0.45 | 58% | 36 | -2.87% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0360 | -0.26 | 65% | 34 | -0.86% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0356 | -0.27 | 74% | 34 | -1.09% | ✅ consistent |
| Short Ratio | -0.0346 | -0.45 | 64% | 36 | n/a | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0338 | -0.23 | 65% | 34 | -0.96% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0318 | -0.30 | 68% | 34 | -1.46% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

