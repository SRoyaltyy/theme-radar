# Factor report — multi-date aggregate

_Generated 2026-10-07 16:47 EDT from 42 scan dates._

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
| 2026-09-29 | 2026-09-28 | 2026-09-30 | 2026-10-01 | 2026-10-02 | 11673 |
| 2026-09-30 | 2026-09-29 | 2026-10-01 | 2026-10-02 | 2026-10-05 | 11682 |
| 2026-10-01 | 2026-09-30 | 2026-10-02 | 2026-10-05 | 2026-10-06 | 11693 |
| 2026-10-02 | 2026-10-01 | 2026-10-05 | 2026-10-06 | 2026-10-07 | 11685 |
| 2026-10-05 | 2026-10-02 | 2026-10-06 | 2026-10-07 | — | 11690 |
| 2026-10-06 | 2026-10-05 | 2026-10-07 | — | — | 11695 |

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
| 2026-09-29 | -0.0367 | +0.0392 | +0.0858 |
| 2026-09-30 | +0.0026 | +0.0403 | +0.0472 |
| 2026-10-01 | +0.0950 | +0.1090 | +0.1116 |
| 2026-10-02 | +0.0316 | +0.0757 | -0.0028 |
| 2026-10-05 | -0.1002 | -0.0538 | — |
| 2026-10-06 | -0.0979 | — | — |
- **1d**: mean IC **-0.0220**, ICIR -0.28, sign consistency 69% over 42 dates
- **2d**: mean IC **-0.0204**, ICIR -0.22, sign consistency 54% over 41 dates
- **3d**: mean IC **-0.0196**, ICIR -0.17, sign consistency 60% over 40 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -18459265460503784.00 | 100% | 42 | -5.84% | ✅ consistent |
| short_fwd_2d | -0.6204 | -7.81 | 100% | 41 | -4.79% | ✅ consistent |
| short_fwd_3d | -0.4982 | -4.76 | 100% | 40 | -4.34% | ✅ consistent |
| Volatility (Month) | -0.0710 | -0.59 | 66% | 41 | +0.45% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0591 | +0.80 | 73% | 41 | n/a | ✅ consistent |
| exit_price_1d | +0.0583 | +0.78 | 74% | 42 | n/a | ✅ consistent |
| exit_price_3d | +0.0575 | +0.77 | 72% | 40 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0543 | -0.51 | 62% | 40 | -0.50% | ⚠️ flips / too few dates |
| Profit Margin | +0.0515 | +0.54 | 71% | 42 | -2.33% | ✅ consistent |
| valuation_score | -0.0437 | -0.54 | 76% | 42 | +0.88% | ✅ consistent |
| Average Volume | -0.0433 | -0.77 | 76% | 42 | n/a | ✅ consistent |
| Price | +0.0427 | +0.57 | 64% | 42 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0427 | +0.57 | 64% | 42 | n/a | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0423 | -0.43 | 57% | 40 | -0.46% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0417 | +0.45 | 64% | 42 | -1.42% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0413 | -0.43 | 60% | 40 | -0.43% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0408 | -0.44 | 60% | 40 | -0.31% | ⚠️ flips / too few dates |
| upside_pct | -0.0408 | -0.33 | 64% | 42 | +0.83% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0408 | -0.33 | 64% | 42 | +0.83% | ⚠️ flips / too few dates |
| Market Cap | +0.0407 | +0.57 | 69% | 42 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0405 | +0.48 | 64% | 42 | -1.35% | ⚠️ flips / too few dates |
| n_pos | -0.0377 | -0.45 | 64% | 42 | n/a | ⚠️ flips / too few dates |
| true_ret | -0.0370 | -0.39 | 55% | 40 | -0.60% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0368 | -0.37 | 57% | 40 | -0.57% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0340 | -0.36 | 68% | 40 | -0.14% | ✅ consistent |
| Institutional Ownership | +0.0331 | +0.48 | 76% | 42 | n/a | ✅ consistent |
| w_pos | -0.0325 | -0.36 | 67% | 42 | n/a | ✅ consistent |
| d_Performance (Quarter) | -0.0325 | -0.27 | 60% | 40 | -0.59% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0320 | -0.38 | 62% | 40 | -0.65% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0314 | -0.51 | 70% | 40 | -0.52% | ✅ consistent |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16649112025868112.00 | 100% | 41 | -9.00% | ✅ consistent |
| short_fwd_3d | -0.7370 | -10.76 | 100% | 40 | -8.05% | ✅ consistent |
| short_fwd_1d | -0.6204 | -7.81 | 100% | 41 | -5.33% | ✅ consistent |
| Volatility (Month) | -0.0930 | -0.77 | 78% | 40 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0799 | +1.05 | 85% | 41 | n/a | ✅ consistent |
| exit_price_3d | +0.0796 | +1.04 | 82% | 40 | n/a | ✅ consistent |
| exit_price_1d | +0.0690 | +0.90 | 78% | 41 | n/a | ✅ consistent |
| Profit Margin | +0.0681 | +0.76 | 78% | 41 | -4.33% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0600 | +0.66 | 76% | 41 | -2.53% | ✅ consistent |
| valuation_score | -0.0591 | -0.82 | 73% | 41 | +1.58% | ✅ consistent |
| upside_pct | -0.0584 | -0.45 | 61% | 41 | +1.49% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0584 | -0.45 | 61% | 41 | +1.49% | ⚠️ flips / too few dates |
| Price | +0.0577 | +0.74 | 76% | 41 | n/a | ✅ consistent |
| entry_price | +0.0577 | +0.74 | 76% | 41 | n/a | ✅ consistent |
| Average Volume | -0.0575 | -1.09 | 85% | 41 | n/a | ✅ consistent |
| Performance (YTD) | +0.0573 | +0.59 | 73% | 41 | -2.65% | ✅ consistent |
| Market Cap | +0.0535 | +0.70 | 76% | 41 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0414 | -0.31 | 59% | 39 | -0.56% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0408 | +0.53 | 68% | 41 | n/a | ✅ consistent |
| n_pos | -0.0401 | -0.41 | 66% | 41 | n/a | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0387 | -0.32 | 64% | 39 | -0.94% | ⚠️ flips / too few dates |
| w_pos | -0.0376 | -0.40 | 63% | 41 | n/a | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0371 | +0.43 | 73% | 41 | -2.02% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0367 | -0.29 | 59% | 39 | -1.01% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0360 | -0.30 | 56% | 39 | -0.78% | ⚠️ flips / too few dates |
| Beta | -0.0356 | -0.19 | 62% | 40 | -3.59% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0352 | +0.38 | 68% | 41 | n/a | ✅ consistent |
| Gross Margin | +0.0339 | +0.51 | 73% | 41 | -4.60% | ✅ consistent |
| Short Float | -0.0338 | -0.34 | 63% | 41 | n/a | ⚠️ flips / too few dates |
| EPS Surprise | +0.0334 | +0.68 | 66% | 41 | -0.28% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -18988843322635144.00 | 100% | 40 | -11.47% | ✅ consistent |
| short_fwd_2d | -0.7370 | -10.76 | 100% | 40 | -8.18% | ✅ consistent |
| short_fwd_1d | -0.4982 | -4.76 | 100% | 40 | -4.74% | ✅ consistent |
| Volatility (Month) | -0.1107 | -0.94 | 77% | 39 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0924 | +1.19 | 90% | 40 | n/a | ✅ consistent |
| exit_price_2d | +0.0833 | +1.06 | 90% | 40 | n/a | ✅ consistent |
| Profit Margin | +0.0787 | +0.90 | 82% | 40 | -5.73% | ✅ consistent |
| exit_price_1d | +0.0745 | +0.94 | 82% | 40 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0710 | +0.73 | 72% | 40 | -3.41% | ✅ consistent |
| valuation_score | -0.0704 | -1.00 | 85% | 40 | +2.06% | ✅ consistent |
| upside_pct | -0.0704 | -0.54 | 72% | 40 | +1.94% | ✅ consistent |
| upside_pct_lvl | -0.0704 | -0.54 | 72% | 40 | +1.93% | ✅ consistent |
| Average Volume | -0.0679 | -1.34 | 85% | 40 | n/a | ✅ consistent |
| Performance (YTD) | +0.0676 | +0.67 | 80% | 40 | -3.55% | ✅ consistent |
| Price | +0.0650 | +0.81 | 75% | 40 | n/a | ✅ consistent |
| entry_price | +0.0650 | +0.81 | 75% | 40 | n/a | ✅ consistent |
| Market Cap | +0.0594 | +0.76 | 78% | 40 | n/a | ✅ consistent |
| Relative Strength Index (14) | +0.0481 | +0.56 | 65% | 40 | n/a | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0464 | +0.55 | 62% | 40 | -2.62% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0458 | +0.58 | 68% | 40 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0441 | -0.30 | 71% | 38 | -0.41% | ✅ consistent |
| Beta | -0.0429 | -0.24 | 59% | 39 | -4.98% | ⚠️ flips / too few dates |
| w_pos | -0.0416 | -0.39 | 68% | 40 | n/a | ✅ consistent |
| Short Float | -0.0411 | -0.45 | 65% | 40 | n/a | ⚠️ flips / too few dates |
| n_pos | -0.0409 | -0.38 | 65% | 40 | n/a | ⚠️ flips / too few dates |
| EPS Surprise | +0.0394 | +0.76 | 70% | 40 | -0.35% | ✅ consistent |
| Gross Margin | +0.0378 | +0.61 | 72% | 40 | -6.02% | ✅ consistent |
| Target Price | +0.0358 | +0.45 | 68% | 40 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0327 | -0.25 | 63% | 38 | -0.74% | ⚠️ flips / too few dates |
| Short Ratio | -0.0321 | -0.43 | 62% | 40 | n/a | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

