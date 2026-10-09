# Factor report — multi-date aggregate

_Generated 2026-10-09 16:54 EDT from 44 scan dates._

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
| 2026-10-06 | 2026-10-05 | 2026-10-07 | 2026-10-08 | 2026-10-09 | 11695 |
| 2026-10-07 | 2026-10-06 | 2026-10-08 | 2026-10-09 | — | 11704 |
| 2026-10-08 | 2026-10-07 | 2026-10-09 | — | — | 11704 |

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
| 2026-10-06 | -0.0979 | -0.0822 | -0.0286 |
| 2026-10-07 | +0.0543 | +0.0495 | — |
| 2026-10-08 | -0.0831 | — | — |
- **1d**: mean IC **-0.0217**, ICIR -0.28, sign consistency 68% over 44 dates
- **2d**: mean IC **-0.0202**, ICIR -0.22, sign consistency 53% over 43 dates
- **3d**: mean IC **-0.0214**, ICIR -0.19, sign consistency 62% over 42 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -17247473462903424.00 | 100% | 44 | -5.75% | ✅ consistent |
| short_fwd_2d | -0.6225 | -7.96 | 100% | 43 | -4.72% | ✅ consistent |
| short_fwd_3d | -0.4975 | -4.78 | 100% | 42 | -4.24% | ✅ consistent |
| Volatility (Month) | -0.0710 | -0.60 | 67% | 43 | +0.45% | ✅ consistent |
| exit_price_1d | +0.0613 | +0.83 | 75% | 44 | n/a | ✅ consistent |
| exit_price_2d | +0.0596 | +0.81 | 74% | 43 | n/a | ✅ consistent |
| exit_price_3d | +0.0577 | +0.78 | 74% | 42 | n/a | ✅ consistent |
| Profit Margin | +0.0557 | +0.57 | 73% | 44 | -2.19% | ✅ consistent |
| d_Performance (Week) | -0.0500 | -0.46 | 62% | 42 | -0.48% | ⚠️ flips / too few dates |
| Market Cap | +0.0470 | +0.62 | 70% | 44 | n/a | ✅ consistent |
| Price | +0.0457 | +0.61 | 66% | 44 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0457 | +0.61 | 66% | 44 | n/a | ⚠️ flips / too few dates |
| upside_pct | -0.0454 | -0.36 | 66% | 44 | +0.78% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0454 | -0.36 | 66% | 44 | +0.77% | ⚠️ flips / too few dates |
| valuation_score | -0.0427 | -0.53 | 75% | 44 | +0.82% | ✅ consistent |
| Performance (YTD) | +0.0417 | +0.46 | 66% | 44 | -1.34% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0415 | -0.40 | 57% | 42 | -0.44% | ⚠️ flips / too few dates |
| Average Volume | -0.0409 | -0.71 | 75% | 44 | n/a | ✅ consistent |
| n_pos | -0.0406 | -0.48 | 66% | 44 | n/a | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0402 | +0.48 | 64% | 44 | -1.29% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0396 | -0.38 | 60% | 42 | -0.41% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0390 | -0.38 | 60% | 42 | -0.29% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0376 | +0.52 | 77% | 44 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0365 | -0.36 | 57% | 42 | -0.54% | ⚠️ flips / too few dates |
| true_ret | -0.0358 | -0.36 | 55% | 42 | -0.57% | ⚠️ flips / too few dates |
| w_pos | -0.0352 | -0.39 | 68% | 44 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0334 | -0.37 | 62% | 42 | -0.62% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0324 | -0.54 | 71% | 42 | -0.51% | ✅ consistent |
| Gross Margin | +0.0303 | +0.43 | 64% | 44 | -2.49% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0301 | -0.30 | 67% | 42 | -0.14% | ✅ consistent |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16381449292106388.00 | 100% | 43 | -8.86% | ✅ consistent |
| short_fwd_3d | -0.7372 | -10.97 | 100% | 42 | -7.89% | ✅ consistent |
| short_fwd_1d | -0.6225 | -7.96 | 100% | 43 | -5.27% | ✅ consistent |
| Volatility (Month) | -0.0961 | -0.81 | 79% | 42 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0824 | +1.09 | 86% | 43 | n/a | ✅ consistent |
| exit_price_3d | +0.0797 | +1.06 | 83% | 42 | n/a | ✅ consistent |
| Profit Margin | +0.0742 | +0.81 | 79% | 43 | -4.07% | ✅ consistent |
| exit_price_1d | +0.0715 | +0.93 | 79% | 43 | n/a | ✅ consistent |
| upside_pct | -0.0654 | -0.50 | 63% | 43 | +1.39% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0654 | -0.50 | 63% | 43 | +1.39% | ⚠️ flips / too few dates |
| Price | +0.0602 | +0.77 | 77% | 43 | n/a | ✅ consistent |
| entry_price | +0.0602 | +0.77 | 77% | 43 | n/a | ✅ consistent |
| Market Cap | +0.0598 | +0.73 | 77% | 43 | n/a | ✅ consistent |
| valuation_score | -0.0578 | -0.81 | 74% | 43 | +1.47% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0576 | +0.64 | 74% | 43 | -2.42% | ✅ consistent |
| Performance (YTD) | +0.0552 | +0.58 | 72% | 43 | -2.51% | ✅ consistent |
| Average Volume | -0.0537 | -0.98 | 81% | 43 | n/a | ✅ consistent |
| Institutional Ownership | +0.0466 | +0.58 | 70% | 43 | n/a | ✅ consistent |
| Beta | -0.0441 | -0.23 | 64% | 42 | -3.41% | ⚠️ flips / too few dates |
| n_pos | -0.0421 | -0.44 | 67% | 43 | n/a | ✅ consistent |
| w_pos | -0.0410 | -0.43 | 65% | 43 | n/a | ⚠️ flips / too few dates |
| Gross Margin | +0.0392 | +0.57 | 74% | 43 | -4.25% | ✅ consistent |
| d_Performance (Week) | -0.0383 | -0.29 | 59% | 41 | -0.52% | ⚠️ flips / too few dates |
| Target Price | +0.0360 | +0.49 | 70% | 43 | n/a | ✅ consistent |
| EPS Surprise | +0.0351 | +0.72 | 67% | 43 | -0.23% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0349 | -0.29 | 63% | 41 | -0.87% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0342 | -0.28 | 59% | 41 | -0.95% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0325 | -0.27 | 56% | 41 | -0.73% | ⚠️ flips / too few dates |
| Short Float | -0.0321 | -0.33 | 63% | 43 | n/a | ⚠️ flips / too few dates |
| Analyst Recom | +0.0315 | +0.34 | 65% | 43 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -19457774262956300.00 | 100% | 42 | -11.26% | ✅ consistent |
| short_fwd_2d | -0.7372 | -10.97 | 100% | 42 | -8.06% | ✅ consistent |
| short_fwd_1d | -0.4975 | -4.78 | 100% | 42 | -4.71% | ✅ consistent |
| Volatility (Month) | -0.1160 | -0.99 | 78% | 41 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0942 | +1.24 | 90% | 42 | n/a | ✅ consistent |
| exit_price_2d | +0.0851 | +1.10 | 90% | 42 | n/a | ✅ consistent |
| Profit Margin | +0.0846 | +0.94 | 83% | 42 | -5.42% | ✅ consistent |
| upside_pct | -0.0764 | -0.59 | 74% | 42 | +1.84% | ✅ consistent |
| upside_pct_lvl | -0.0764 | -0.59 | 74% | 42 | +1.84% | ✅ consistent |
| exit_price_1d | +0.0761 | +0.98 | 83% | 42 | n/a | ✅ consistent |
| valuation_score | -0.0705 | -1.03 | 86% | 42 | +1.95% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0677 | +0.70 | 71% | 42 | -3.26% | ✅ consistent |
| Price | +0.0667 | +0.84 | 76% | 42 | n/a | ✅ consistent |
| entry_price | +0.0667 | +0.84 | 76% | 42 | n/a | ✅ consistent |
| Average Volume | -0.0654 | -1.29 | 86% | 42 | n/a | ✅ consistent |
| Market Cap | +0.0642 | +0.81 | 79% | 42 | n/a | ✅ consistent |
| Performance (YTD) | +0.0636 | +0.64 | 79% | 42 | -3.38% | ✅ consistent |
| Beta | -0.0538 | -0.30 | 61% | 41 | -4.74% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0502 | +0.63 | 69% | 42 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0466 | -0.32 | 72% | 40 | -0.41% | ✅ consistent |
| w_pos | -0.0465 | -0.43 | 69% | 42 | n/a | ✅ consistent |
| n_pos | -0.0442 | -0.42 | 67% | 42 | n/a | ✅ consistent |
| Gross Margin | +0.0429 | +0.65 | 74% | 42 | -5.56% | ✅ consistent |
| EPS Surprise | +0.0412 | +0.80 | 71% | 42 | -0.30% | ✅ consistent |
| Short Float | -0.0412 | -0.46 | 67% | 42 | n/a | ✅ consistent |
| 50-Day Simple Moving Average | +0.0407 | +0.47 | 60% | 42 | -2.56% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0390 | +0.41 | 62% | 42 | n/a | ⚠️ flips / too few dates |
| Target Price | +0.0389 | +0.50 | 69% | 42 | n/a | ✅ consistent |
| Analyst Recom | +0.0367 | +0.39 | 67% | 42 | n/a | ✅ consistent |
| d_Performance (Quarter) | -0.0347 | -0.26 | 57% | 40 | -0.86% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

