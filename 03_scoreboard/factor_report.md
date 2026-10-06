# Factor report — multi-date aggregate

_Generated 2026-10-06 16:57 EDT from 41 scan dates._

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
| 2026-10-02 | 2026-10-01 | 2026-10-05 | 2026-10-06 | — | 11685 |
| 2026-10-05 | 2026-10-02 | 2026-10-06 | — | — | 11690 |

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
| 2026-10-02 | +0.0316 | +0.0757 | — |
| 2026-10-05 | -0.1002 | — | — |
- **1d**: mean IC **-0.0202**, ICIR -0.25, sign consistency 68% over 41 dates
- **2d**: mean IC **-0.0195**, ICIR -0.21, sign consistency 52% over 40 dates
- **3d**: mean IC **-0.0200**, ICIR -0.17, sign consistency 59% over 39 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -18238188437997000.00 | 100% | 41 | -5.88% | ✅ consistent |
| short_fwd_2d | -0.6212 | -7.75 | 100% | 40 | -4.84% | ✅ consistent |
| short_fwd_3d | -0.4987 | -4.71 | 100% | 39 | -4.37% | ✅ consistent |
| Volatility (Month) | -0.0670 | -0.56 | 65% | 40 | +0.45% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0596 | +0.80 | 73% | 41 | n/a | ✅ consistent |
| exit_price_2d | +0.0577 | +0.77 | 72% | 40 | n/a | ✅ consistent |
| exit_price_3d | +0.0543 | +0.75 | 72% | 39 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0540 | -0.51 | 62% | 39 | -0.52% | ⚠️ flips / too few dates |
| Profit Margin | +0.0516 | +0.54 | 71% | 41 | -2.38% | ✅ consistent |
| Price | +0.0440 | +0.58 | 66% | 41 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0440 | +0.58 | 66% | 41 | n/a | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0436 | +0.47 | 66% | 41 | -1.45% | ⚠️ flips / too few dates |
| Market Cap | +0.0432 | +0.62 | 71% | 41 | n/a | ✅ consistent |
| Average Volume | -0.0423 | -0.75 | 76% | 41 | n/a | ✅ consistent |
| valuation_score | -0.0423 | -0.52 | 76% | 41 | +0.91% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0421 | -0.42 | 56% | 39 | -0.47% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0410 | -0.42 | 59% | 39 | -0.44% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0407 | +0.48 | 63% | 41 | -1.38% | ⚠️ flips / too few dates |
| upside_pct | -0.0406 | -0.32 | 63% | 41 | +0.86% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0406 | -0.32 | 63% | 41 | +0.86% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0397 | -0.42 | 59% | 39 | -0.32% | ⚠️ flips / too few dates |
| true_ret | -0.0365 | -0.38 | 54% | 39 | -0.61% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0364 | -0.37 | 56% | 39 | -0.58% | ⚠️ flips / too few dates |
| n_pos | -0.0359 | -0.42 | 63% | 41 | n/a | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0340 | -0.40 | 64% | 39 | -0.67% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0339 | +0.49 | 76% | 41 | n/a | ✅ consistent |
| d_Forward P/E | -0.0332 | -0.35 | 67% | 39 | -0.14% | ✅ consistent |
| d_Market Cap | -0.0311 | -0.50 | 69% | 39 | -0.53% | ✅ consistent |
| w_pos | -0.0295 | -0.33 | 66% | 41 | n/a | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0293 | -0.24 | 59% | 39 | -0.59% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16444820705884542.00 | 100% | 40 | -9.09% | ✅ consistent |
| short_fwd_3d | -0.7381 | -10.69 | 100% | 39 | -8.13% | ✅ consistent |
| short_fwd_1d | -0.6212 | -7.75 | 100% | 40 | -5.36% | ✅ consistent |
| Volatility (Month) | -0.0894 | -0.75 | 77% | 39 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0801 | +1.04 | 85% | 40 | n/a | ✅ consistent |
| exit_price_3d | +0.0762 | +1.02 | 82% | 39 | n/a | ✅ consistent |
| exit_price_1d | +0.0691 | +0.89 | 78% | 40 | n/a | ✅ consistent |
| Profit Margin | +0.0672 | +0.75 | 78% | 40 | -4.42% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0614 | +0.67 | 75% | 40 | -2.58% | ✅ consistent |
| Performance (YTD) | +0.0596 | +0.62 | 75% | 40 | -2.70% | ✅ consistent |
| upside_pct | -0.0579 | -0.44 | 60% | 40 | +1.50% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0579 | -0.44 | 60% | 40 | +1.50% | ⚠️ flips / too few dates |
| Price | +0.0578 | +0.73 | 75% | 40 | n/a | ✅ consistent |
| entry_price | +0.0578 | +0.73 | 75% | 40 | n/a | ✅ consistent |
| valuation_score | -0.0576 | -0.79 | 72% | 40 | +1.59% | ✅ consistent |
| Average Volume | -0.0564 | -1.06 | 85% | 40 | n/a | ✅ consistent |
| Market Cap | +0.0541 | +0.70 | 75% | 40 | n/a | ✅ consistent |
| Institutional Ownership | +0.0414 | +0.53 | 68% | 40 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0394 | -0.29 | 58% | 38 | -0.57% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0383 | -0.31 | 63% | 38 | -0.96% | ⚠️ flips / too few dates |
| n_pos | -0.0380 | -0.39 | 65% | 40 | n/a | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0376 | +0.43 | 72% | 40 | -2.05% | ✅ consistent |
| Relative Strength Index (14) | +0.0369 | +0.40 | 70% | 40 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0365 | -0.28 | 58% | 38 | -1.04% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0350 | -0.29 | 55% | 38 | -0.80% | ⚠️ flips / too few dates |
| w_pos | -0.0348 | -0.37 | 62% | 40 | n/a | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0338 | -0.33 | 61% | 38 | -1.41% | ⚠️ flips / too few dates |
| Gross Margin | +0.0333 | +0.50 | 72% | 40 | -4.76% | ✅ consistent |
| EPS Surprise | +0.0329 | +0.67 | 65% | 40 | -0.29% | ⚠️ flips / too few dates |
| Target Price | +0.0326 | +0.44 | 68% | 40 | n/a | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -18749980439011012.00 | 100% | 39 | -11.58% | ✅ consistent |
| short_fwd_2d | -0.7381 | -10.69 | 100% | 39 | -8.23% | ✅ consistent |
| short_fwd_1d | -0.4987 | -4.71 | 100% | 39 | -4.75% | ✅ consistent |
| Volatility (Month) | -0.1076 | -0.91 | 76% | 38 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0906 | +1.16 | 90% | 39 | n/a | ✅ consistent |
| exit_price_2d | +0.0815 | +1.03 | 90% | 39 | n/a | ✅ consistent |
| Profit Margin | +0.0771 | +0.87 | 82% | 39 | -5.82% | ✅ consistent |
| exit_price_1d | +0.0726 | +0.91 | 82% | 39 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0703 | +0.71 | 72% | 39 | -3.47% | ✅ consistent |
| upside_pct | -0.0692 | -0.53 | 72% | 39 | +1.95% | ✅ consistent |
| upside_pct_lvl | -0.0692 | -0.53 | 72% | 39 | +1.94% | ✅ consistent |
| valuation_score | -0.0691 | -0.98 | 85% | 39 | +2.07% | ✅ consistent |
| Performance (YTD) | +0.0684 | +0.67 | 79% | 39 | -3.61% | ✅ consistent |
| Average Volume | -0.0669 | -1.32 | 85% | 39 | n/a | ✅ consistent |
| Price | +0.0631 | +0.78 | 74% | 39 | n/a | ✅ consistent |
| entry_price | +0.0631 | +0.78 | 74% | 39 | n/a | ✅ consistent |
| Market Cap | +0.0572 | +0.73 | 77% | 39 | n/a | ✅ consistent |
| Relative Strength Index (14) | +0.0481 | +0.55 | 64% | 39 | n/a | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0453 | +0.53 | 62% | 39 | -2.67% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0446 | -0.30 | 70% | 37 | -0.39% | ✅ consistent |
| Institutional Ownership | +0.0444 | +0.56 | 67% | 39 | n/a | ✅ consistent |
| w_pos | -0.0410 | -0.38 | 67% | 39 | n/a | ✅ consistent |
| Beta | -0.0408 | -0.22 | 58% | 38 | -5.11% | ⚠️ flips / too few dates |
| n_pos | -0.0408 | -0.38 | 64% | 39 | n/a | ⚠️ flips / too few dates |
| Short Float | -0.0407 | -0.44 | 64% | 39 | n/a | ⚠️ flips / too few dates |
| EPS Surprise | +0.0383 | +0.74 | 69% | 39 | -0.35% | ✅ consistent |
| Gross Margin | +0.0362 | +0.58 | 72% | 39 | -6.15% | ✅ consistent |
| Target Price | +0.0344 | +0.43 | 67% | 39 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0323 | -0.24 | 62% | 37 | -0.73% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0320 | +0.65 | 67% | 39 | -2.88% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

