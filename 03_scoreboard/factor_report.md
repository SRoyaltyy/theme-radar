# Factor report — multi-date aggregate

_Generated 2026-09-30 20:19 EDT from 37 scan dates._

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
| 2026-09-28 | 2026-09-25 | 2026-09-29 | 2026-09-30 | — | 11668 |
| 2026-09-29 | 2026-09-28 | 2026-09-30 | — | — | 11673 |

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
| 2026-09-28 | -0.0477 | -0.0469 | — |
| 2026-09-29 | -0.0367 | — | — |
- **1d**: mean IC **-0.0232**, ICIR -0.29, sign consistency 73% over 37 dates
- **2d**: mean IC **-0.0290**, ICIR -0.31, sign consistency 58% over 36 dates
- **3d**: mean IC **-0.0271**, ICIR -0.23, sign consistency 63% over 35 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -17325693698494290.00 | 100% | 37 | -6.06% | ✅ consistent |
| short_fwd_2d | -0.6203 | -7.41 | 100% | 36 | -5.04% | ✅ consistent |
| short_fwd_3d | -0.4966 | -4.52 | 100% | 35 | -4.56% | ✅ consistent |
| Volatility (Month) | -0.0687 | -0.55 | 64% | 36 | +0.45% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0589 | -0.53 | 66% | 35 | -0.57% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0501 | +0.74 | 71% | 35 | n/a | ✅ consistent |
| exit_price_2d | +0.0497 | +0.74 | 72% | 36 | n/a | ✅ consistent |
| exit_price_1d | +0.0478 | +0.70 | 70% | 37 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0445 | -0.42 | 54% | 35 | -0.52% | ⚠️ flips / too few dates |
| Profit Margin | +0.0437 | +0.45 | 68% | 37 | -2.52% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0431 | -0.42 | 57% | 35 | -0.49% | ⚠️ flips / too few dates |
| Average Volume | -0.0419 | -0.71 | 73% | 37 | n/a | ✅ consistent |
| valuation_score | -0.0417 | -0.49 | 73% | 37 | +0.94% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0405 | -0.41 | 54% | 35 | -0.33% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0401 | -0.39 | 57% | 35 | -0.64% | ⚠️ flips / too few dates |
| true_ret | -0.0396 | -0.39 | 54% | 35 | -0.65% | ⚠️ flips / too few dates |
| n_pos | -0.0394 | -0.46 | 68% | 37 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0370 | -0.42 | 66% | 35 | -0.74% | ⚠️ flips / too few dates |
| Beta | -0.0351 | -0.18 | 56% | 36 | -2.35% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0344 | +0.39 | 65% | 37 | -1.57% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0333 | -0.35 | 69% | 35 | -0.16% | ✅ consistent |
| d_Performance (Quarter) | -0.0325 | -0.26 | 60% | 35 | -0.66% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0323 | +0.41 | 62% | 37 | -1.51% | ⚠️ flips / too few dates |
| Price | +0.0321 | +0.46 | 62% | 37 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0321 | +0.46 | 62% | 37 | n/a | ⚠️ flips / too few dates |
| d_Price | -0.0319 | -0.31 | 54% | 35 | -0.65% | ⚠️ flips / too few dates |
| w_pos | -0.0317 | -0.35 | 68% | 37 | n/a | ✅ consistent |
| d_Market Cap | -0.0312 | -0.49 | 69% | 35 | -0.59% | ✅ consistent |
| Market Cap | +0.0310 | +0.50 | 68% | 37 | n/a | ✅ consistent |
| upside_pct | -0.0307 | -0.24 | 59% | 37 | +0.89% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16294636549060720.00 | 100% | 36 | -9.41% | ✅ consistent |
| short_fwd_3d | -0.7362 | -10.20 | 100% | 35 | -8.46% | ✅ consistent |
| short_fwd_1d | -0.6203 | -7.41 | 100% | 36 | -5.53% | ✅ consistent |
| Volatility (Month) | -0.0920 | -0.73 | 74% | 35 | +0.97% | ✅ consistent |
| exit_price_3d | +0.0669 | +1.04 | 80% | 35 | n/a | ✅ consistent |
| exit_price_2d | +0.0657 | +1.01 | 83% | 36 | n/a | ✅ consistent |
| Profit Margin | +0.0584 | +0.65 | 75% | 36 | -4.67% | ✅ consistent |
| valuation_score | -0.0569 | -0.74 | 69% | 36 | +1.70% | ✅ consistent |
| Average Volume | -0.0561 | -1.01 | 83% | 36 | n/a | ✅ consistent |
| exit_price_1d | +0.0547 | +0.83 | 75% | 36 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0483 | +0.57 | 72% | 36 | -2.82% | ✅ consistent |
| d_Performance (Week) | -0.0471 | -0.34 | 62% | 34 | -0.62% | ⚠️ flips / too few dates |
| Beta | -0.0471 | -0.25 | 66% | 35 | -4.19% | ⚠️ flips / too few dates |
| n_pos | -0.0468 | -0.48 | 72% | 36 | n/a | ✅ consistent |
| Performance (YTD) | +0.0464 | +0.53 | 72% | 36 | -2.93% | ✅ consistent |
| upside_pct | -0.0457 | -0.35 | 56% | 36 | +1.60% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0457 | -0.35 | 56% | 36 | +1.60% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0451 | -0.36 | 68% | 34 | -1.08% | ✅ consistent |
| Price | +0.0432 | +0.65 | 72% | 36 | n/a | ✅ consistent |
| entry_price | +0.0432 | +0.65 | 72% | 36 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0432 | -0.33 | 62% | 34 | -1.16% | ⚠️ flips / too few dates |
| w_pos | -0.0431 | -0.45 | 69% | 36 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0405 | -0.39 | 65% | 34 | -1.57% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0394 | -0.31 | 59% | 34 | -0.87% | ⚠️ flips / too few dates |
| Market Cap | +0.0384 | +0.62 | 72% | 36 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0372 | -0.29 | 65% | 34 | -1.44% | ⚠️ flips / too few dates |
| Short Float | -0.0366 | -0.36 | 64% | 36 | n/a | ⚠️ flips / too few dates |
| Gross Margin | +0.0364 | +0.53 | 72% | 36 | -5.15% | ✅ consistent |
| true_ret | -0.0363 | -0.29 | 59% | 34 | -1.39% | ⚠️ flips / too few dates |
| d_Price | -0.0357 | -0.28 | 62% | 34 | -1.39% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -17762436471107704.00 | 100% | 35 | -11.99% | ✅ consistent |
| short_fwd_2d | -0.7362 | -10.20 | 100% | 35 | -8.45% | ✅ consistent |
| short_fwd_1d | -0.4966 | -4.52 | 100% | 35 | -4.84% | ✅ consistent |
| Volatility (Month) | -0.1114 | -0.90 | 74% | 34 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0759 | +1.19 | 89% | 35 | n/a | ✅ consistent |
| valuation_score | -0.0687 | -0.92 | 83% | 35 | +2.29% | ✅ consistent |
| Profit Margin | +0.0681 | +0.77 | 80% | 35 | -6.17% | ✅ consistent |
| Average Volume | -0.0673 | -1.26 | 83% | 35 | n/a | ✅ consistent |
| exit_price_2d | +0.0668 | +1.03 | 89% | 35 | n/a | ✅ consistent |
| Beta | -0.0586 | -0.32 | 62% | 34 | -5.83% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0578 | +0.88 | 80% | 35 | n/a | ✅ consistent |
| upside_pct | -0.0562 | -0.43 | 69% | 35 | +2.16% | ✅ consistent |
| upside_pct_lvl | -0.0562 | -0.43 | 69% | 35 | +2.16% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0557 | +0.61 | 69% | 35 | -3.81% | ✅ consistent |
| Performance (YTD) | +0.0533 | +0.57 | 77% | 35 | -3.92% | ✅ consistent |
| d_Performance (Week) | -0.0512 | -0.33 | 73% | 33 | -0.45% | ✅ consistent |
| w_pos | -0.0488 | -0.44 | 71% | 35 | n/a | ✅ consistent |
| Price | +0.0481 | +0.72 | 71% | 35 | n/a | ✅ consistent |
| entry_price | +0.0481 | +0.72 | 71% | 35 | n/a | ✅ consistent |
| n_pos | -0.0477 | -0.43 | 69% | 35 | n/a | ✅ consistent |
| Short Float | -0.0468 | -0.50 | 69% | 35 | n/a | ✅ consistent |
| Market Cap | +0.0406 | +0.69 | 74% | 35 | n/a | ✅ consistent |
| Gross Margin | +0.0395 | +0.62 | 74% | 35 | -6.74% | ✅ consistent |
| Relative Strength Index (14) | +0.0389 | +0.45 | 60% | 35 | n/a | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0347 | -0.25 | 64% | 33 | -0.90% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0338 | +0.42 | 57% | 35 | -2.94% | ⚠️ flips / too few dates |
| Short Ratio | -0.0334 | -0.43 | 63% | 35 | n/a | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0322 | -0.22 | 64% | 33 | -1.02% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0312 | -0.24 | 73% | 33 | -1.04% | ✅ consistent |
| d_Market Cap | -0.0297 | -0.38 | 70% | 33 | -2.14% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

