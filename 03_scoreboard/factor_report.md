# Factor report — multi-date aggregate

_Generated 2026-10-12 16:57 EDT from 45 scan dates._

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
| 2026-10-07 | 2026-10-06 | 2026-10-08 | 2026-10-09 | 2026-10-12 | 11704 |
| 2026-10-08 | 2026-10-07 | 2026-10-09 | 2026-10-12 | — | 11704 |
| 2026-10-09 | 2026-10-08 | 2026-10-12 | — | — | 11699 |

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
| 2026-10-07 | +0.0543 | +0.0495 | +0.0717 |
| 2026-10-08 | -0.0831 | +0.1042 | — |
| 2026-10-09 | -0.1863 | — | — |
- **1d**: mean IC **-0.0254**, ICIR -0.31, sign consistency 69% over 45 dates
- **2d**: mean IC **-0.0174**, ICIR -0.19, sign consistency 52% over 44 dates
- **3d**: mean IC **-0.0193**, ICIR -0.17, sign consistency 60% over 43 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -17442366354791862.00 | 100% | 45 | -5.76% | ✅ consistent |
| short_fwd_2d | -0.6216 | -8.02 | 100% | 44 | -4.67% | ✅ consistent |
| short_fwd_3d | -0.5014 | -4.73 | 100% | 43 | -4.22% | ✅ consistent |
| Volatility (Month) | -0.0753 | -0.62 | 68% | 44 | +0.45% | ✅ consistent |
| exit_price_1d | +0.0645 | +0.85 | 76% | 45 | n/a | ✅ consistent |
| Profit Margin | +0.0616 | +0.59 | 73% | 45 | -2.19% | ✅ consistent |
| exit_price_2d | +0.0608 | +0.83 | 75% | 44 | n/a | ✅ consistent |
| exit_price_3d | +0.0595 | +0.81 | 74% | 43 | n/a | ✅ consistent |
| upside_pct | -0.0526 | -0.39 | 67% | 45 | +0.78% | ✅ consistent |
| upside_pct_lvl | -0.0526 | -0.39 | 67% | 45 | +0.78% | ✅ consistent |
| Market Cap | +0.0509 | +0.64 | 71% | 45 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0495 | -0.46 | 63% | 43 | -0.45% | ⚠️ flips / too few dates |
| Price | +0.0490 | +0.64 | 67% | 45 | n/a | ✅ consistent |
| entry_price | +0.0490 | +0.64 | 67% | 45 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0441 | -0.42 | 58% | 43 | -0.48% | ⚠️ flips / too few dates |
| n_pos | -0.0440 | -0.51 | 67% | 45 | n/a | ✅ consistent |
| valuation_score | -0.0440 | -0.55 | 76% | 45 | +0.83% | ✅ consistent |
| Performance (YTD) | +0.0432 | +0.48 | 67% | 45 | -1.34% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0429 | +0.51 | 64% | 45 | -1.29% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0422 | -0.41 | 60% | 43 | -0.46% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0420 | -0.41 | 60% | 43 | -0.31% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0413 | +0.55 | 78% | 45 | n/a | ✅ consistent |
| Average Volume | -0.0412 | -0.72 | 76% | 45 | n/a | ✅ consistent |
| w_pos | -0.0400 | -0.43 | 69% | 45 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0390 | -0.38 | 58% | 43 | -0.58% | ⚠️ flips / too few dates |
| true_ret | -0.0381 | -0.38 | 56% | 43 | -0.58% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0369 | -0.27 | 60% | 43 | -0.58% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0349 | -0.39 | 63% | 43 | -0.66% | ⚠️ flips / too few dates |
| Beta | -0.0347 | -0.18 | 52% | 44 | -2.02% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0328 | -0.55 | 72% | 43 | -0.57% | ✅ consistent |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16570836500501750.00 | 100% | 44 | -8.82% | ✅ consistent |
| short_fwd_3d | -0.7389 | -10.97 | 100% | 43 | -7.82% | ✅ consistent |
| short_fwd_1d | -0.6216 | -8.02 | 100% | 44 | -5.22% | ✅ consistent |
| Volatility (Month) | -0.0984 | -0.83 | 79% | 43 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0858 | +1.10 | 86% | 44 | n/a | ✅ consistent |
| exit_price_3d | +0.0820 | +1.09 | 84% | 43 | n/a | ✅ consistent |
| Profit Margin | +0.0778 | +0.83 | 80% | 44 | -4.04% | ✅ consistent |
| exit_price_1d | +0.0748 | +0.95 | 80% | 44 | n/a | ✅ consistent |
| upside_pct | -0.0701 | -0.53 | 64% | 44 | +1.37% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0701 | -0.53 | 64% | 44 | +1.37% | ⚠️ flips / too few dates |
| Market Cap | +0.0642 | +0.75 | 77% | 44 | n/a | ✅ consistent |
| Price | +0.0636 | +0.80 | 77% | 44 | n/a | ✅ consistent |
| entry_price | +0.0636 | +0.80 | 77% | 44 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0610 | +0.66 | 75% | 44 | -2.38% | ✅ consistent |
| valuation_score | -0.0596 | -0.84 | 75% | 44 | +1.45% | ✅ consistent |
| Performance (YTD) | +0.0570 | +0.60 | 73% | 44 | -2.48% | ✅ consistent |
| Average Volume | -0.0542 | -1.00 | 82% | 44 | n/a | ✅ consistent |
| Institutional Ownership | +0.0496 | +0.61 | 70% | 44 | n/a | ✅ consistent |
| Beta | -0.0449 | -0.24 | 65% | 43 | -3.45% | ⚠️ flips / too few dates |
| Gross Margin | +0.0421 | +0.59 | 75% | 44 | -4.17% | ✅ consistent |
| n_pos | -0.0408 | -0.43 | 66% | 44 | n/a | ⚠️ flips / too few dates |
| w_pos | -0.0401 | -0.43 | 66% | 44 | n/a | ⚠️ flips / too few dates |
| Target Price | +0.0389 | +0.52 | 70% | 44 | n/a | ✅ consistent |
| EPS Surprise | +0.0363 | +0.75 | 68% | 44 | -0.37% | ✅ consistent |
| d_Performance (Week) | -0.0344 | -0.26 | 57% | 42 | -0.54% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0343 | +0.38 | 70% | 44 | -1.94% | ✅ consistent |
| Short Float | -0.0334 | -0.35 | 64% | 44 | n/a | ⚠️ flips / too few dates |
| Analyst Recom | +0.0332 | +0.36 | 66% | 44 | n/a | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0312 | -0.26 | 62% | 42 | -0.89% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0305 | -0.24 | 57% | 42 | -0.96% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -19688051796367616.00 | 100% | 43 | -11.21% | ✅ consistent |
| short_fwd_2d | -0.7389 | -10.97 | 100% | 43 | -8.00% | ✅ consistent |
| short_fwd_1d | -0.5014 | -4.73 | 100% | 43 | -4.68% | ✅ consistent |
| Volatility (Month) | -0.1177 | -1.01 | 79% | 42 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0976 | +1.24 | 91% | 43 | n/a | ✅ consistent |
| Profit Margin | +0.0899 | +0.94 | 84% | 43 | -5.30% | ✅ consistent |
| exit_price_2d | +0.0884 | +1.11 | 91% | 43 | n/a | ✅ consistent |
| upside_pct | -0.0824 | -0.62 | 74% | 43 | +1.79% | ✅ consistent |
| upside_pct_lvl | -0.0824 | -0.62 | 74% | 43 | +1.79% | ✅ consistent |
| exit_price_1d | +0.0796 | +0.99 | 84% | 43 | n/a | ✅ consistent |
| valuation_score | -0.0702 | -1.04 | 86% | 43 | +1.90% | ✅ consistent |
| Market Cap | +0.0701 | +0.80 | 79% | 43 | n/a | ✅ consistent |
| Price | +0.0701 | +0.86 | 77% | 43 | n/a | ✅ consistent |
| entry_price | +0.0701 | +0.86 | 77% | 43 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0679 | +0.71 | 72% | 43 | -3.20% | ✅ consistent |
| Performance (YTD) | +0.0641 | +0.65 | 79% | 43 | -3.31% | ✅ consistent |
| Average Volume | -0.0635 | -1.23 | 84% | 43 | n/a | ✅ consistent |
| Beta | -0.0571 | -0.32 | 62% | 42 | -4.68% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0547 | +0.65 | 70% | 43 | n/a | ✅ consistent |
| w_pos | -0.0475 | -0.45 | 70% | 43 | n/a | ✅ consistent |
| Gross Margin | +0.0458 | +0.68 | 74% | 43 | -5.40% | ✅ consistent |
| n_pos | -0.0448 | -0.43 | 67% | 43 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0425 | -0.29 | 71% | 41 | -0.40% | ✅ consistent |
| Target Price | +0.0424 | +0.53 | 70% | 43 | n/a | ✅ consistent |
| EPS Surprise | +0.0423 | +0.83 | 72% | 43 | -0.38% | ✅ consistent |
| Short Float | -0.0410 | -0.47 | 67% | 43 | n/a | ✅ consistent |
| Analyst Recom | +0.0405 | +0.42 | 67% | 43 | n/a | ✅ consistent |
| 50-Day Simple Moving Average | +0.0388 | +0.45 | 58% | 43 | -2.55% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0358 | +0.38 | 60% | 43 | n/a | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0305 | +0.64 | 67% | 43 | -2.57% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

