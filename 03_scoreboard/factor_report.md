# Factor report — multi-date aggregate

_Generated 2026-10-08 17:37 EDT from 43 scan dates._

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
| 2026-10-05 | 2026-10-02 | 2026-10-06 | 2026-10-07 | 2026-10-08 | 11690 |
| 2026-10-06 | 2026-10-05 | 2026-10-07 | 2026-10-08 | — | 11695 |
| 2026-10-07 | 2026-10-06 | 2026-10-08 | — | — | 11704 |

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
| 2026-10-05 | -0.1002 | -0.0538 | -0.0885 |
| 2026-10-06 | -0.0979 | -0.0822 | — |
| 2026-10-07 | +0.0543 | — | — |
- **1d**: mean IC **-0.0203**, ICIR -0.26, sign consistency 67% over 43 dates
- **2d**: mean IC **-0.0218**, ICIR -0.24, sign consistency 55% over 42 dates
- **3d**: mean IC **-0.0213**, ICIR -0.19, sign consistency 61% over 41 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -17808512907718362.00 | 100% | 43 | -5.80% | ✅ consistent |
| short_fwd_2d | -0.6217 | -7.87 | 100% | 42 | -4.74% | ✅ consistent |
| short_fwd_3d | -0.4957 | -4.74 | 100% | 41 | -4.29% | ✅ consistent |
| Volatility (Month) | -0.0722 | -0.60 | 67% | 42 | +0.45% | ✅ consistent |
| exit_price_1d | +0.0600 | +0.81 | 74% | 43 | n/a | ✅ consistent |
| exit_price_3d | +0.0589 | +0.80 | 73% | 41 | n/a | ✅ consistent |
| exit_price_2d | +0.0578 | +0.78 | 74% | 42 | n/a | ✅ consistent |
| Profit Margin | +0.0565 | +0.57 | 72% | 43 | -2.24% | ✅ consistent |
| d_Performance (Week) | -0.0490 | -0.45 | 61% | 41 | -0.48% | ⚠️ flips / too few dates |
| upside_pct | -0.0461 | -0.36 | 65% | 43 | +0.81% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0461 | -0.36 | 65% | 43 | +0.80% | ⚠️ flips / too few dates |
| Market Cap | +0.0449 | +0.59 | 70% | 43 | n/a | ✅ consistent |
| Price | +0.0444 | +0.59 | 65% | 43 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0444 | +0.59 | 65% | 43 | n/a | ⚠️ flips / too few dates |
| valuation_score | -0.0418 | -0.51 | 74% | 43 | +0.85% | ✅ consistent |
| Performance (YTD) | +0.0408 | +0.44 | 65% | 43 | -1.38% | ⚠️ flips / too few dates |
| Average Volume | -0.0404 | -0.69 | 74% | 43 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0385 | +0.46 | 63% | 43 | -1.33% | ⚠️ flips / too few dates |
| n_pos | -0.0383 | -0.46 | 65% | 43 | n/a | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0377 | -0.37 | 56% | 41 | -0.44% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0371 | +0.51 | 77% | 43 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0357 | -0.35 | 59% | 41 | -0.41% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0350 | -0.35 | 59% | 41 | -0.29% | ⚠️ flips / too few dates |
| w_pos | -0.0340 | -0.38 | 67% | 43 | n/a | ✅ consistent |
| Beta | -0.0337 | -0.18 | 52% | 42 | -1.98% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0325 | -0.32 | 56% | 41 | -0.54% | ⚠️ flips / too few dates |
| true_ret | -0.0324 | -0.33 | 54% | 41 | -0.58% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0310 | -0.51 | 71% | 41 | -0.51% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0285 | -0.33 | 61% | 41 | -0.63% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0282 | -0.28 | 66% | 41 | -0.13% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16189846802652106.00 | 100% | 42 | -8.93% | ✅ consistent |
| short_fwd_3d | -0.7364 | -10.86 | 100% | 41 | -7.96% | ✅ consistent |
| short_fwd_1d | -0.6217 | -7.87 | 100% | 42 | -5.30% | ✅ consistent |
| Volatility (Month) | -0.0961 | -0.80 | 78% | 41 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0803 | +1.06 | 86% | 42 | n/a | ✅ consistent |
| exit_price_3d | +0.0794 | +1.05 | 83% | 41 | n/a | ✅ consistent |
| Profit Margin | +0.0712 | +0.79 | 79% | 42 | -4.20% | ✅ consistent |
| exit_price_1d | +0.0692 | +0.91 | 79% | 42 | n/a | ✅ consistent |
| upside_pct | -0.0620 | -0.48 | 62% | 42 | +1.45% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0620 | -0.48 | 62% | 42 | +1.45% | ⚠️ flips / too few dates |
| valuation_score | -0.0587 | -0.82 | 74% | 42 | +1.53% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0584 | +0.64 | 74% | 42 | -2.48% | ✅ consistent |
| Price | +0.0579 | +0.75 | 76% | 42 | n/a | ✅ consistent |
| entry_price | +0.0579 | +0.75 | 76% | 42 | n/a | ✅ consistent |
| Average Volume | -0.0561 | -1.06 | 83% | 42 | n/a | ✅ consistent |
| Performance (YTD) | +0.0554 | +0.58 | 71% | 42 | -2.58% | ✅ consistent |
| Market Cap | +0.0550 | +0.72 | 76% | 42 | n/a | ✅ consistent |
| Institutional Ownership | +0.0432 | +0.55 | 69% | 42 | n/a | ✅ consistent |
| Beta | -0.0429 | -0.23 | 63% | 41 | -3.52% | ⚠️ flips / too few dates |
| n_pos | -0.0416 | -0.43 | 67% | 42 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0406 | -0.31 | 60% | 40 | -0.53% | ⚠️ flips / too few dates |
| w_pos | -0.0405 | -0.42 | 64% | 42 | n/a | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0380 | -0.32 | 65% | 40 | -0.91% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0366 | -0.29 | 60% | 40 | -0.99% | ⚠️ flips / too few dates |
| Gross Margin | +0.0364 | +0.54 | 74% | 42 | -4.42% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0356 | -0.30 | 57% | 40 | -0.76% | ⚠️ flips / too few dates |
| EPS Surprise | +0.0346 | +0.71 | 67% | 42 | -0.25% | ✅ consistent |
| Target Price | +0.0339 | +0.46 | 69% | 42 | n/a | ✅ consistent |
| 50-Day Simple Moving Average | +0.0339 | +0.38 | 71% | 42 | -2.00% | ✅ consistent |
| Short Float | -0.0333 | -0.34 | 64% | 42 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -19224738619806380.00 | 100% | 41 | -11.37% | ✅ consistent |
| short_fwd_2d | -0.7364 | -10.86 | 100% | 41 | -8.11% | ✅ consistent |
| short_fwd_1d | -0.4957 | -4.74 | 100% | 41 | -4.72% | ✅ consistent |
| Volatility (Month) | -0.1140 | -0.96 | 78% | 40 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0933 | +1.21 | 90% | 41 | n/a | ✅ consistent |
| exit_price_2d | +0.0841 | +1.08 | 90% | 41 | n/a | ✅ consistent |
| Profit Margin | +0.0825 | +0.92 | 83% | 41 | -5.57% | ✅ consistent |
| exit_price_1d | +0.0753 | +0.96 | 83% | 41 | n/a | ✅ consistent |
| upside_pct | -0.0739 | -0.57 | 73% | 41 | +1.91% | ✅ consistent |
| upside_pct_lvl | -0.0739 | -0.57 | 73% | 41 | +1.91% | ✅ consistent |
| valuation_score | -0.0704 | -1.01 | 85% | 41 | +2.03% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0683 | +0.70 | 71% | 41 | -3.34% | ✅ consistent |
| Average Volume | -0.0667 | -1.32 | 85% | 41 | n/a | ✅ consistent |
| Price | +0.0658 | +0.83 | 76% | 41 | n/a | ✅ consistent |
| entry_price | +0.0658 | +0.83 | 76% | 41 | n/a | ✅ consistent |
| Performance (YTD) | +0.0650 | +0.65 | 78% | 41 | -3.47% | ✅ consistent |
| Market Cap | +0.0617 | +0.78 | 78% | 41 | n/a | ✅ consistent |
| Beta | -0.0492 | -0.27 | 60% | 40 | -4.86% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0478 | +0.61 | 68% | 41 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0477 | -0.33 | 72% | 39 | -0.42% | ✅ consistent |
| w_pos | -0.0454 | -0.42 | 68% | 41 | n/a | ✅ consistent |
| n_pos | -0.0440 | -0.41 | 66% | 41 | n/a | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0427 | +0.49 | 61% | 41 | -2.60% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0423 | +0.46 | 63% | 41 | n/a | ⚠️ flips / too few dates |
| Short Float | -0.0419 | -0.47 | 66% | 41 | n/a | ⚠️ flips / too few dates |
| EPS Surprise | +0.0403 | +0.78 | 71% | 41 | -0.33% | ✅ consistent |
| Gross Margin | +0.0393 | +0.63 | 73% | 41 | -5.78% | ✅ consistent |
| Target Price | +0.0378 | +0.48 | 68% | 41 | n/a | ✅ consistent |
| d_Performance (Quarter) | -0.0354 | -0.26 | 56% | 39 | -0.89% | ⚠️ flips / too few dates |
| Analyst Recom | +0.0343 | +0.37 | 66% | 41 | n/a | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

