# Factor report — multi-date aggregate

_Generated 2026-09-29 16:50 EDT from 36 scan dates._

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
| 2026-09-25 | 2026-09-24 | 2026-09-28 | 2026-09-29 | — | 11665 |
| 2026-09-28 | 2026-09-25 | 2026-09-29 | — | — | 11668 |

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
| 2026-09-25 | -0.1114 | -0.0598 | — |
| 2026-09-28 | -0.0477 | — | — |
- **1d**: mean IC **-0.0228**, ICIR -0.28, sign consistency 72% over 36 dates
- **2d**: mean IC **-0.0285**, ICIR -0.30, sign consistency 57% over 35 dates
- **3d**: mean IC **-0.0251**, ICIR -0.21, sign consistency 62% over 34 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -17089958990371628.00 | 100% | 36 | -6.13% | ✅ consistent |
| short_fwd_2d | -0.6197 | -7.31 | 100% | 35 | -5.08% | ✅ consistent |
| short_fwd_3d | -0.4941 | -4.48 | 100% | 34 | -4.22% | ✅ consistent |
| Volatility (Month) | -0.0674 | -0.53 | 63% | 35 | +0.45% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0617 | -0.56 | 68% | 34 | -0.59% | ✅ consistent |
| exit_price_2d | +0.0503 | +0.74 | 71% | 35 | n/a | ✅ consistent |
| exit_price_1d | +0.0503 | +0.74 | 72% | 36 | n/a | ✅ consistent |
| exit_price_3d | +0.0488 | +0.72 | 71% | 34 | n/a | ✅ consistent |
| Profit Margin | +0.0459 | +0.47 | 69% | 36 | -2.57% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0454 | -0.43 | 53% | 34 | -0.54% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0437 | -0.42 | 56% | 34 | -0.51% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0410 | -0.39 | 56% | 34 | -0.67% | ⚠️ flips / too few dates |
| Average Volume | -0.0407 | -0.68 | 72% | 36 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0406 | -0.40 | 53% | 34 | -0.35% | ⚠️ flips / too few dates |
| valuation_score | -0.0405 | -0.47 | 72% | 36 | +0.97% | ✅ consistent |
| true_ret | -0.0404 | -0.39 | 53% | 34 | -0.67% | ⚠️ flips / too few dates |
| n_pos | -0.0388 | -0.45 | 67% | 36 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0375 | -0.42 | 65% | 34 | -0.76% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0356 | +0.40 | 67% | 36 | -1.60% | ✅ consistent |
| Price | +0.0344 | +0.50 | 64% | 36 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0344 | +0.50 | 64% | 36 | n/a | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0336 | -0.35 | 68% | 34 | -0.16% | ✅ consistent |
| d_Price | -0.0332 | -0.31 | 56% | 34 | -0.67% | ⚠️ flips / too few dates |
| upside_pct | -0.0331 | -0.26 | 61% | 36 | +0.91% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0331 | -0.26 | 61% | 36 | +0.91% | ⚠️ flips / too few dates |
| Market Cap | +0.0330 | +0.54 | 69% | 36 | n/a | ✅ consistent |
| Beta | -0.0329 | -0.17 | 54% | 35 | -2.41% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0324 | -0.51 | 71% | 34 | -0.62% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0324 | +0.41 | 61% | 36 | -1.54% | ⚠️ flips / too few dates |
| w_pos | -0.0315 | -0.34 | 67% | 36 | n/a | ✅ consistent |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16066728310142374.00 | 100% | 35 | -9.50% | ✅ consistent |
| short_fwd_3d | -0.7352 | -10.08 | 100% | 34 | -8.21% | ✅ consistent |
| short_fwd_1d | -0.6197 | -7.31 | 100% | 35 | -5.55% | ✅ consistent |
| Volatility (Month) | -0.0912 | -0.72 | 74% | 34 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0675 | +1.04 | 83% | 35 | n/a | ✅ consistent |
| exit_price_3d | +0.0660 | +1.02 | 79% | 34 | n/a | ✅ consistent |
| Profit Margin | +0.0591 | +0.65 | 74% | 35 | -4.75% | ✅ consistent |
| exit_price_1d | +0.0563 | +0.86 | 77% | 35 | n/a | ✅ consistent |
| valuation_score | -0.0553 | -0.72 | 69% | 35 | +1.74% | ✅ consistent |
| Average Volume | -0.0551 | -0.98 | 83% | 35 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0481 | +0.56 | 71% | 35 | -2.88% | ✅ consistent |
| upside_pct | -0.0476 | -0.36 | 57% | 35 | +1.64% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0476 | -0.36 | 57% | 35 | +1.64% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0475 | +0.54 | 71% | 35 | -2.98% | ✅ consistent |
| n_pos | -0.0469 | -0.48 | 71% | 35 | n/a | ✅ consistent |
| Beta | -0.0466 | -0.24 | 65% | 34 | -4.28% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0465 | -0.33 | 61% | 33 | -0.66% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0455 | -0.35 | 67% | 33 | -1.11% | ✅ consistent |
| Price | +0.0448 | +0.67 | 74% | 35 | n/a | ✅ consistent |
| entry_price | +0.0448 | +0.67 | 74% | 35 | n/a | ✅ consistent |
| w_pos | -0.0437 | -0.45 | 69% | 35 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0436 | -0.32 | 61% | 33 | -1.20% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0393 | -0.31 | 58% | 33 | -0.92% | ⚠️ flips / too few dates |
| Market Cap | +0.0392 | +0.63 | 71% | 35 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0387 | -0.37 | 64% | 33 | -1.60% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0374 | -0.28 | 64% | 33 | -1.47% | ⚠️ flips / too few dates |
| true_ret | -0.0370 | -0.29 | 58% | 33 | -1.42% | ⚠️ flips / too few dates |
| d_Price | -0.0364 | -0.28 | 61% | 33 | -1.42% | ⚠️ flips / too few dates |
| Short Float | -0.0362 | -0.35 | 63% | 35 | n/a | ⚠️ flips / too few dates |
| Gross Margin | +0.0343 | +0.50 | 71% | 35 | -5.26% | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -17506848520560386.00 | 100% | 34 | -11.77% | ✅ consistent |
| short_fwd_2d | -0.7352 | -10.08 | 100% | 34 | -8.20% | ✅ consistent |
| short_fwd_1d | -0.4941 | -4.48 | 100% | 34 | -4.58% | ✅ consistent |
| Volatility (Month) | -0.1076 | -0.87 | 73% | 33 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0764 | +1.18 | 88% | 34 | n/a | ✅ consistent |
| Profit Margin | +0.0678 | +0.75 | 79% | 34 | -6.02% | ✅ consistent |
| exit_price_2d | +0.0672 | +1.02 | 88% | 34 | n/a | ✅ consistent |
| valuation_score | -0.0670 | -0.90 | 82% | 34 | +2.28% | ✅ consistent |
| Average Volume | -0.0661 | -1.23 | 82% | 34 | n/a | ✅ consistent |
| exit_price_1d | +0.0580 | +0.87 | 79% | 34 | n/a | ✅ consistent |
| upside_pct | -0.0550 | -0.41 | 68% | 34 | +2.15% | ✅ consistent |
| upside_pct_lvl | -0.0550 | -0.41 | 68% | 34 | +2.14% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0543 | +0.58 | 68% | 34 | -3.80% | ✅ consistent |
| Beta | -0.0539 | -0.29 | 61% | 33 | -5.06% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0529 | +0.56 | 76% | 34 | -3.90% | ✅ consistent |
| d_Performance (Week) | -0.0490 | -0.31 | 72% | 32 | -0.35% | ✅ consistent |
| Price | +0.0484 | +0.71 | 71% | 34 | n/a | ✅ consistent |
| entry_price | +0.0484 | +0.71 | 71% | 34 | n/a | ✅ consistent |
| w_pos | -0.0463 | -0.42 | 71% | 34 | n/a | ✅ consistent |
| Short Float | -0.0461 | -0.48 | 68% | 34 | n/a | ✅ consistent |
| n_pos | -0.0453 | -0.40 | 68% | 34 | n/a | ✅ consistent |
| Market Cap | +0.0405 | +0.67 | 74% | 34 | n/a | ✅ consistent |
| Relative Strength Index (14) | +0.0380 | +0.43 | 59% | 34 | n/a | ⚠️ flips / too few dates |
| Gross Margin | +0.0365 | +0.58 | 74% | 34 | -5.49% | ✅ consistent |
| Short Ratio | -0.0322 | -0.41 | 62% | 34 | n/a | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0320 | -0.22 | 62% | 32 | -0.86% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0319 | +0.39 | 56% | 34 | -2.93% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0296 | -0.20 | 62% | 32 | -0.94% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0286 | -0.36 | 69% | 32 | -2.15% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0285 | -0.26 | 66% | 32 | -1.48% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

