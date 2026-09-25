# Factor report — multi-date aggregate

_Generated 2026-09-25 16:49 EDT from 34 scan dates._

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
| 2026-09-23 | 2026-09-22 | 2026-09-24 | 2026-09-25 | — | 11653 |
| 2026-09-24 | 2026-09-23 | 2026-09-25 | — | — | 11660 |

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
| 2026-09-23 | +0.0928 | +0.0398 | — |
| 2026-09-24 | -0.0345 | — | — |
- **1d**: mean IC **-0.0194**, ICIR -0.24, sign consistency 71% over 34 dates
- **2d**: mean IC **-0.0298**, ICIR -0.31, sign consistency 58% over 33 dates
- **3d**: mean IC **-0.0287**, ICIR -0.23, sign consistency 66% over 32 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -18568816959140892.00 | 100% | 34 | -5.84% | ✅ consistent |
| short_fwd_2d | -0.6203 | -7.33 | 100% | 33 | -4.81% | ✅ consistent |
| short_fwd_3d | -0.4935 | -4.35 | 100% | 32 | -4.34% | ✅ consistent |
| Volatility (Month) | -0.0628 | -0.49 | 61% | 33 | +0.45% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0602 | -0.53 | 66% | 32 | -0.61% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0496 | +0.72 | 71% | 34 | n/a | ✅ consistent |
| exit_price_2d | +0.0449 | +0.69 | 70% | 33 | n/a | ✅ consistent |
| Profit Margin | +0.0436 | +0.44 | 68% | 34 | -2.29% | ✅ consistent |
| exit_price_3d | +0.0434 | +0.66 | 69% | 32 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0421 | -0.39 | 50% | 32 | -0.49% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0405 | -0.38 | 53% | 32 | -0.50% | ⚠️ flips / too few dates |
| Average Volume | -0.0402 | -0.66 | 71% | 34 | n/a | ✅ consistent |
| valuation_score | -0.0387 | -0.44 | 71% | 34 | +0.93% | ✅ consistent |
| d_Performance (YTD) | -0.0379 | -0.35 | 53% | 32 | -0.60% | ⚠️ flips / too few dates |
| true_ret | -0.0377 | -0.36 | 50% | 32 | -0.60% | ⚠️ flips / too few dates |
| n_pos | -0.0376 | -0.43 | 65% | 34 | n/a | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0361 | -0.35 | 50% | 32 | -0.35% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0356 | -0.39 | 62% | 32 | -0.75% | ⚠️ flips / too few dates |
| Price | +0.0336 | +0.48 | 62% | 34 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0336 | +0.48 | 62% | 34 | n/a | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0335 | +0.37 | 65% | 34 | -1.53% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0327 | -0.23 | 56% | 34 | -1.15% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0324 | -0.49 | 69% | 32 | -0.65% | ✅ consistent |
| d_Forward P/E | -0.0323 | -0.33 | 66% | 32 | -0.17% | ⚠️ flips / too few dates |
| d_Price | -0.0311 | -0.29 | 53% | 32 | -0.60% | ⚠️ flips / too few dates |
| Market Cap | +0.0310 | +0.50 | 68% | 34 | n/a | ✅ consistent |
| w_pos | -0.0292 | -0.32 | 65% | 34 | n/a | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0290 | +0.36 | 59% | 34 | -1.48% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0284 | -0.22 | 59% | 34 | +0.87% | ⚠️ flips / too few dates |
| upside_pct | -0.0284 | -0.22 | 59% | 34 | +0.87% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -15600926743107926.00 | 100% | 33 | -9.13% | ✅ consistent |
| short_fwd_3d | -0.7356 | -9.85 | 100% | 32 | -8.17% | ✅ consistent |
| short_fwd_1d | -0.6203 | -7.33 | 100% | 33 | -5.45% | ✅ consistent |
| Volatility (Month) | -0.0829 | -0.65 | 72% | 32 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0630 | +1.00 | 82% | 33 | n/a | ✅ consistent |
| exit_price_3d | +0.0584 | +0.99 | 78% | 32 | n/a | ✅ consistent |
| Profit Margin | +0.0544 | +0.59 | 73% | 33 | -4.34% | ✅ consistent |
| Average Volume | -0.0540 | -0.94 | 82% | 33 | n/a | ✅ consistent |
| valuation_score | -0.0532 | -0.68 | 67% | 33 | +1.68% | ✅ consistent |
| d_Performance (Week) | -0.0518 | -0.37 | 61% | 31 | -0.55% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0517 | +0.81 | 76% | 33 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0482 | -0.37 | 68% | 31 | -1.01% | ✅ consistent |
| n_pos | -0.0464 | -0.46 | 70% | 33 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0458 | -0.33 | 61% | 31 | -1.11% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0430 | +0.48 | 70% | 33 | -2.89% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0428 | +0.50 | 70% | 33 | -2.81% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0421 | -0.39 | 68% | 31 | -1.53% | ✅ consistent |
| w_pos | -0.0414 | -0.42 | 67% | 33 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0402 | -0.31 | 58% | 31 | -0.81% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0401 | -0.30 | 65% | 31 | -1.35% | ⚠️ flips / too few dates |
| Price | +0.0401 | +0.62 | 73% | 33 | n/a | ✅ consistent |
| entry_price | +0.0401 | +0.62 | 73% | 33 | n/a | ✅ consistent |
| true_ret | -0.0398 | -0.30 | 58% | 31 | -1.28% | ⚠️ flips / too few dates |
| upside_pct | -0.0390 | -0.30 | 55% | 33 | +1.58% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0390 | -0.30 | 55% | 33 | +1.57% | ⚠️ flips / too few dates |
| Beta | -0.0389 | -0.20 | 62% | 32 | -2.31% | ⚠️ flips / too few dates |
| d_Price | -0.0385 | -0.29 | 61% | 31 | -1.28% | ⚠️ flips / too few dates |
| Market Cap | +0.0345 | +0.57 | 70% | 33 | n/a | ✅ consistent |
| d_Market Cap | -0.0343 | -0.43 | 68% | 31 | -2.00% | ✅ consistent |
| Short Float | -0.0342 | -0.32 | 61% | 33 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -16984137793402062.00 | 100% | 32 | -11.62% | ✅ consistent |
| short_fwd_2d | -0.7356 | -9.85 | 100% | 32 | -8.36% | ✅ consistent |
| short_fwd_1d | -0.4935 | -4.35 | 100% | 32 | -4.83% | ✅ consistent |
| Volatility (Month) | -0.1000 | -0.81 | 71% | 31 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0700 | +1.14 | 88% | 32 | n/a | ✅ consistent |
| Average Volume | -0.0646 | -1.17 | 81% | 32 | n/a | ✅ consistent |
| valuation_score | -0.0641 | -0.84 | 81% | 32 | +2.30% | ✅ consistent |
| Profit Margin | +0.0619 | +0.69 | 78% | 32 | -5.80% | ✅ consistent |
| exit_price_2d | +0.0608 | +0.97 | 88% | 32 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0565 | -0.36 | 77% | 30 | -0.39% | ✅ consistent |
| exit_price_1d | +0.0515 | +0.81 | 78% | 32 | n/a | ✅ consistent |
| Beta | -0.0496 | -0.26 | 58% | 31 | -3.44% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0468 | +0.50 | 75% | 32 | -3.91% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0466 | +0.52 | 66% | 32 | -3.83% | ⚠️ flips / too few dates |
| n_pos | -0.0459 | -0.40 | 66% | 32 | n/a | ⚠️ flips / too few dates |
| w_pos | -0.0457 | -0.40 | 69% | 32 | n/a | ✅ consistent |
| Short Float | -0.0447 | -0.46 | 66% | 32 | n/a | ⚠️ flips / too few dates |
| upside_pct | -0.0441 | -0.34 | 66% | 32 | +2.16% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0441 | -0.34 | 66% | 32 | +2.16% | ⚠️ flips / too few dates |
| Price | +0.0417 | +0.65 | 69% | 32 | n/a | ✅ consistent |
| entry_price | +0.0417 | +0.65 | 69% | 32 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0376 | -0.26 | 67% | 30 | -0.79% | ✅ consistent |
| Market Cap | +0.0347 | +0.61 | 72% | 32 | n/a | ✅ consistent |
| Relative Strength Index (14) | +0.0342 | +0.38 | 56% | 32 | n/a | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0336 | -0.22 | 63% | 30 | -0.89% | ⚠️ flips / too few dates |
| Short Ratio | -0.0333 | -0.41 | 59% | 32 | n/a | ⚠️ flips / too few dates |
| Gross Margin | +0.0329 | +0.52 | 72% | 32 | -2.81% | ✅ consistent |
| Performance (Week) | -0.0321 | -0.24 | 50% | 32 | -2.31% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0312 | -0.23 | 77% | 30 | -0.94% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0288 | -0.20 | 63% | 30 | -0.46% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

