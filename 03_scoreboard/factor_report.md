# Factor report — multi-date aggregate

_Generated 2026-09-28 16:45 EDT from 35 scan dates._

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
| 2026-09-24 | 2026-09-23 | 2026-09-25 | 2026-09-28 | — | 11660 |
| 2026-09-25 | 2026-09-24 | 2026-09-28 | — | — | 11665 |

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
| 2026-09-24 | -0.0345 | +0.0435 | — |
| 2026-09-25 | -0.1114 | — | — |
- **1d**: mean IC **-0.0221**, ICIR -0.27, sign consistency 71% over 35 dates
- **2d**: mean IC **-0.0276**, ICIR -0.29, sign consistency 56% over 34 dates
- **3d**: mean IC **-0.0264**, ICIR -0.22, sign consistency 64% over 33 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -17762436471107704.00 | 100% | 35 | -6.18% | ✅ consistent |
| short_fwd_2d | -0.6174 | -7.27 | 100% | 34 | -4.74% | ✅ consistent |
| short_fwd_3d | -0.4949 | -4.42 | 100% | 33 | -4.27% | ✅ consistent |
| Volatility (Month) | -0.0674 | -0.52 | 62% | 34 | +0.45% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0599 | -0.53 | 67% | 33 | -0.64% | ✅ consistent |
| exit_price_1d | +0.0509 | +0.74 | 71% | 35 | n/a | ✅ consistent |
| exit_price_2d | +0.0491 | +0.72 | 71% | 34 | n/a | ✅ consistent |
| Profit Margin | +0.0455 | +0.46 | 69% | 35 | -2.62% | ✅ consistent |
| exit_price_3d | +0.0446 | +0.69 | 70% | 33 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0442 | -0.41 | 52% | 33 | -0.57% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0425 | -0.40 | 55% | 33 | -0.54% | ⚠️ flips / too few dates |
| Average Volume | -0.0406 | -0.67 | 71% | 35 | n/a | ✅ consistent |
| valuation_score | -0.0398 | -0.45 | 71% | 35 | +0.99% | ✅ consistent |
| d_Performance (YTD) | -0.0396 | -0.37 | 55% | 33 | -0.68% | ⚠️ flips / too few dates |
| n_pos | -0.0396 | -0.45 | 66% | 35 | n/a | ⚠️ flips / too few dates |
| true_ret | -0.0395 | -0.38 | 52% | 33 | -0.69% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0390 | -0.38 | 52% | 33 | -0.39% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0360 | +0.40 | 66% | 35 | -1.63% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0352 | -0.39 | 64% | 33 | -0.77% | ⚠️ flips / too few dates |
| Price | +0.0349 | +0.50 | 63% | 35 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0349 | +0.50 | 63% | 35 | n/a | ⚠️ flips / too few dates |
| Beta | -0.0349 | -0.18 | 56% | 34 | -2.47% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0332 | -0.25 | 60% | 35 | +0.93% | ⚠️ flips / too few dates |
| upside_pct | -0.0332 | -0.25 | 60% | 35 | +0.93% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0329 | -0.34 | 67% | 33 | -0.17% | ✅ consistent |
| d_Market Cap | -0.0325 | -0.50 | 70% | 33 | -0.63% | ✅ consistent |
| d_Price | -0.0324 | -0.30 | 55% | 33 | -0.69% | ⚠️ flips / too few dates |
| Market Cap | +0.0323 | +0.52 | 69% | 35 | n/a | ✅ consistent |
| w_pos | -0.0323 | -0.35 | 66% | 35 | n/a | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0316 | +0.39 | 60% | 35 | -1.57% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -15835540310260184.00 | 100% | 34 | -9.25% | ✅ consistent |
| short_fwd_3d | -0.7343 | -9.94 | 100% | 33 | -8.06% | ✅ consistent |
| short_fwd_1d | -0.6174 | -7.27 | 100% | 34 | -5.30% | ✅ consistent |
| Volatility (Month) | -0.0871 | -0.69 | 73% | 33 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0666 | +1.01 | 82% | 34 | n/a | ✅ consistent |
| exit_price_3d | +0.0624 | +1.00 | 79% | 33 | n/a | ✅ consistent |
| Profit Margin | +0.0573 | +0.62 | 74% | 34 | -4.58% | ✅ consistent |
| exit_price_1d | +0.0553 | +0.83 | 76% | 34 | n/a | ✅ consistent |
| Average Volume | -0.0545 | -0.96 | 82% | 34 | n/a | ✅ consistent |
| valuation_score | -0.0540 | -0.69 | 68% | 34 | +1.71% | ✅ consistent |
| n_pos | -0.0462 | -0.46 | 71% | 34 | n/a | ✅ consistent |
| Performance (YTD) | +0.0458 | +0.52 | 71% | 34 | -2.95% | ✅ consistent |
| d_Performance (Week) | -0.0457 | -0.32 | 59% | 32 | -0.58% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0456 | +0.53 | 71% | 34 | -2.85% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0450 | -0.35 | 66% | 32 | -1.08% | ⚠️ flips / too few dates |
| upside_pct | -0.0442 | -0.33 | 56% | 34 | +1.61% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0442 | -0.33 | 56% | 34 | +1.61% | ⚠️ flips / too few dates |
| Price | +0.0438 | +0.65 | 74% | 34 | n/a | ✅ consistent |
| entry_price | +0.0438 | +0.65 | 74% | 34 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0432 | -0.32 | 59% | 32 | -1.14% | ⚠️ flips / too few dates |
| w_pos | -0.0420 | -0.43 | 68% | 34 | n/a | ✅ consistent |
| Beta | -0.0419 | -0.22 | 64% | 33 | -3.46% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0403 | -0.38 | 66% | 32 | -1.59% | ⚠️ flips / too few dates |
| Market Cap | +0.0378 | +0.60 | 71% | 34 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0376 | -0.29 | 56% | 32 | -0.88% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0374 | -0.28 | 62% | 32 | -1.42% | ⚠️ flips / too few dates |
| d_Price | -0.0369 | -0.28 | 59% | 32 | -1.36% | ⚠️ flips / too few dates |
| true_ret | -0.0368 | -0.28 | 56% | 32 | -1.36% | ⚠️ flips / too few dates |
| Short Float | -0.0353 | -0.34 | 62% | 34 | n/a | ⚠️ flips / too few dates |
| d_Market Cap | -0.0334 | -0.42 | 69% | 32 | -2.17% | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -17247473462903424.00 | 100% | 33 | -11.69% | ✅ consistent |
| short_fwd_2d | -0.7343 | -9.94 | 100% | 33 | -8.12% | ✅ consistent |
| short_fwd_1d | -0.4949 | -4.42 | 100% | 33 | -4.70% | ✅ consistent |
| Volatility (Month) | -0.1039 | -0.84 | 72% | 32 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0735 | +1.16 | 88% | 33 | n/a | ✅ consistent |
| valuation_score | -0.0659 | -0.87 | 82% | 33 | +2.28% | ✅ consistent |
| Average Volume | -0.0657 | -1.20 | 82% | 33 | n/a | ✅ consistent |
| Profit Margin | +0.0651 | +0.72 | 79% | 33 | -5.92% | ✅ consistent |
| exit_price_2d | +0.0643 | +0.99 | 88% | 33 | n/a | ✅ consistent |
| exit_price_1d | +0.0551 | +0.84 | 79% | 33 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0526 | -0.33 | 74% | 31 | -0.34% | ✅ consistent |
| Beta | -0.0523 | -0.28 | 59% | 32 | -4.34% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0516 | +0.56 | 67% | 33 | -3.81% | ✅ consistent |
| upside_pct | -0.0508 | -0.38 | 67% | 33 | +2.14% | ✅ consistent |
| upside_pct_lvl | -0.0508 | -0.38 | 67% | 33 | +2.14% | ✅ consistent |
| Performance (YTD) | +0.0508 | +0.53 | 76% | 33 | -3.90% | ✅ consistent |
| w_pos | -0.0458 | -0.40 | 70% | 33 | n/a | ✅ consistent |
| Price | +0.0454 | +0.68 | 70% | 33 | n/a | ✅ consistent |
| entry_price | +0.0454 | +0.68 | 70% | 33 | n/a | ✅ consistent |
| n_pos | -0.0451 | -0.40 | 67% | 33 | n/a | ✅ consistent |
| Short Float | -0.0450 | -0.47 | 67% | 33 | n/a | ✅ consistent |
| Market Cap | +0.0374 | +0.64 | 73% | 33 | n/a | ✅ consistent |
| Relative Strength Index (14) | +0.0368 | +0.41 | 58% | 33 | n/a | ⚠️ flips / too few dates |
| Gross Margin | +0.0348 | +0.56 | 73% | 33 | -4.26% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0332 | -0.23 | 65% | 31 | -0.80% | ⚠️ flips / too few dates |
| Short Ratio | -0.0325 | -0.41 | 61% | 33 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0307 | -0.23 | 48% | 33 | -2.33% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0303 | +0.37 | 55% | 33 | -2.93% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0302 | -0.20 | 61% | 31 | -0.92% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0293 | -0.22 | 74% | 31 | -0.98% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

