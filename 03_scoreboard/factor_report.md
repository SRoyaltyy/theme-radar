# Factor report — multi-date aggregate

_Generated 2026-09-09 18:52 EDT from 22 scan dates._

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
| 2026-09-04 | 2026-09-03 | 2026-09-08 | 2026-09-09 | — | 11593 |
| 2026-09-08 | — | 2026-09-09 | — | — | 11595 |

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
| 2026-09-04 | -0.0292 | -0.0659 | — |
| 2026-09-08 | -0.0849 | — | — |
- **1d**: mean IC **-0.0279**, ICIR -0.36, sign consistency 73% over 22 dates
- **2d**: mean IC **-0.0391**, ICIR -0.47, sign consistency 57% over 21 dates
- **3d**: mean IC **-0.0365**, ICIR -0.33, sign consistency 60% over 20 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -24391610887908072.00 | 100% | 22 | -6.36% | ✅ consistent |
| short_fwd_2d | -0.6174 | -8.09 | 100% | 21 | -5.08% | ✅ consistent |
| short_fwd_3d | -0.4796 | -4.35 | 100% | 20 | -4.15% | ✅ consistent |
| Volatility (Month) | -0.0611 | -0.47 | 52% | 21 | +0.66% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0580 | -0.57 | 65% | 20 | -0.68% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0562 | -0.53 | 55% | 20 | -0.68% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0559 | -0.55 | 60% | 20 | -0.69% | ⚠️ flips / too few dates |
| true_ret | -0.0542 | -0.54 | 55% | 20 | -0.81% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0514 | -0.50 | 55% | 20 | -0.87% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0493 | -0.52 | 55% | 20 | -0.47% | ⚠️ flips / too few dates |
| Beta | -0.0480 | -0.26 | 57% | 21 | -1.37% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0444 | -0.46 | 70% | 20 | -1.06% | ✅ consistent |
| Profit Margin | +0.0432 | +0.44 | 64% | 22 | -2.72% | ⚠️ flips / too few dates |
| n_pos | -0.0417 | -0.53 | 64% | 22 | n/a | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0412 | -0.33 | 55% | 20 | -0.92% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0405 | -0.38 | 70% | 20 | -0.21% | ✅ consistent |
| d_Market Cap | -0.0396 | -0.56 | 70% | 20 | -0.90% | ✅ consistent |
| exit_price_1d | +0.0386 | +0.61 | 64% | 22 | n/a | ⚠️ flips / too few dates |
| exit_price_3d | +0.0377 | +0.60 | 65% | 20 | n/a | ⚠️ flips / too few dates |
| d_Price | -0.0365 | -0.34 | 55% | 20 | -0.81% | ⚠️ flips / too few dates |
| Forward P/E | -0.0357 | -0.39 | 68% | 22 | n/a | ✅ consistent |
| exit_price_2d | +0.0355 | +0.56 | 62% | 21 | n/a | ⚠️ flips / too few dates |
| Average Volume | -0.0322 | -0.48 | 64% | 22 | n/a | ⚠️ flips / too few dates |
| w_pos | -0.0311 | -0.38 | 64% | 22 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0310 | -0.23 | 59% | 22 | -1.56% | ⚠️ flips / too few dates |
| total_score | -0.0279 | -0.36 | 73% | 22 | -0.75% | ✅ consistent |
| price_score | -0.0275 | -0.31 | 65% | 20 | -0.96% | ⚠️ flips / too few dates |
| valuation_score | -0.0271 | -0.28 | 64% | 22 | +1.16% | ⚠️ flips / too few dates |
| Market Cap | +0.0260 | +0.48 | 68% | 22 | n/a | ✅ consistent |
| Short Float | -0.0252 | -0.21 | 50% | 22 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16850926812823186.00 | 100% | 21 | -9.84% | ✅ consistent |
| short_fwd_3d | -0.7208 | -8.66 | 100% | 20 | -8.29% | ✅ consistent |
| short_fwd_1d | -0.6174 | -8.09 | 100% | 21 | -5.74% | ✅ consistent |
| Volatility (Month) | -0.0670 | -0.56 | 70% | 20 | +1.24% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0595 | -0.47 | 70% | 20 | -1.47% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0579 | -0.42 | 60% | 20 | -1.66% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0550 | -0.40 | 55% | 20 | -0.71% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0549 | -0.55 | 70% | 20 | -2.27% | ✅ consistent |
| true_ret | -0.0530 | -0.40 | 60% | 20 | -1.82% | ⚠️ flips / too few dates |
| Profit Margin | +0.0529 | +0.74 | 76% | 21 | -5.25% | ✅ consistent |
| Forward P/E | -0.0529 | -0.58 | 67% | 21 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0526 | -0.39 | 65% | 20 | -2.07% | ⚠️ flips / too few dates |
| Beta | -0.0508 | -0.28 | 70% | 20 | -2.80% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0484 | -0.38 | 60% | 20 | -1.15% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0476 | -0.41 | 65% | 20 | -0.37% | ⚠️ flips / too few dates |
| n_pos | -0.0475 | -0.52 | 71% | 21 | n/a | ✅ consistent |
| d_Price | -0.0470 | -0.35 | 60% | 20 | -1.82% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0467 | -0.54 | 70% | 20 | -2.84% | ✅ consistent |
| exit_price_2d | +0.0466 | +0.83 | 81% | 21 | n/a | ✅ consistent |
| exit_price_3d | +0.0464 | +0.82 | 75% | 20 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0450 | -0.41 | 50% | 20 | -1.58% | ⚠️ flips / too few dates |
| price_score | -0.0416 | -0.42 | 50% | 20 | -2.72% | ⚠️ flips / too few dates |
| w_pos | -0.0409 | -0.50 | 62% | 21 | n/a | ⚠️ flips / too few dates |
| total_score | -0.0391 | -0.47 | 57% | 21 | -1.46% | ⚠️ flips / too few dates |
| Average Volume | -0.0377 | -0.65 | 71% | 21 | n/a | ✅ consistent |
| exit_price_1d | +0.0353 | +0.62 | 71% | 21 | n/a | ✅ consistent |
| Market Cap | +0.0321 | +0.62 | 67% | 21 | n/a | ✅ consistent |
| valuation_score | -0.0311 | -0.40 | 57% | 21 | +2.10% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0293 | +0.30 | 62% | 21 | -3.67% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0287 | -0.21 | 57% | 21 | -2.66% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -14241632491976356.00 | 100% | 20 | -11.99% | ✅ consistent |
| short_fwd_2d | -0.7208 | -8.66 | 100% | 20 | -8.60% | ✅ consistent |
| short_fwd_1d | -0.4796 | -4.35 | 100% | 20 | -4.60% | ✅ consistent |
| Volatility (Month) | -0.0792 | -0.67 | 68% | 19 | +2.17% | ✅ consistent |
| d_Performance (Week) | -0.0709 | -0.53 | 79% | 19 | -0.36% | ✅ consistent |
| Forward P/E | -0.0695 | -0.77 | 65% | 20 | n/a | ⚠️ flips / too few dates |
| Profit Margin | +0.0634 | +0.93 | 85% | 20 | -6.85% | ✅ consistent |
| d_Performance (Month) | -0.0588 | -0.50 | 79% | 19 | -1.55% | ✅ consistent |
| Beta | -0.0560 | -0.32 | 53% | 19 | -4.27% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0552 | -0.45 | 68% | 19 | -1.34% | ✅ consistent |
| exit_price_3d | +0.0535 | +1.00 | 85% | 20 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0533 | -0.40 | 63% | 19 | -1.53% | ⚠️ flips / too few dates |
| true_ret | -0.0477 | -0.37 | 68% | 19 | -1.95% | ✅ consistent |
| d_Performance (YTD) | -0.0477 | -0.36 | 68% | 19 | -2.08% | ✅ consistent |
| price_score | -0.0462 | -0.40 | 63% | 19 | -2.54% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0440 | +0.81 | 85% | 20 | n/a | ✅ consistent |
| Average Volume | -0.0435 | -0.80 | 70% | 20 | n/a | ✅ consistent |
| n_pos | -0.0421 | -0.41 | 60% | 20 | n/a | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0418 | -0.34 | 63% | 19 | -0.85% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0413 | -0.52 | 74% | 19 | -2.97% | ✅ consistent |
| w_pos | -0.0407 | -0.42 | 60% | 20 | n/a | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0391 | -0.42 | 68% | 19 | -2.27% | ✅ consistent |
| d_Price | -0.0387 | -0.29 | 68% | 19 | -1.95% | ✅ consistent |
| d_Forward P/E | -0.0381 | -0.35 | 68% | 19 | -0.43% | ✅ consistent |
| total_score | -0.0365 | -0.33 | 60% | 20 | -1.44% | ⚠️ flips / too few dates |
| Market Cap | +0.0357 | +0.75 | 80% | 20 | n/a | ✅ consistent |
| exit_price_1d | +0.0349 | +0.63 | 75% | 20 | n/a | ✅ consistent |
| Gross Margin | +0.0347 | +0.51 | 75% | 20 | -2.18% | ✅ consistent |
| Performance (YTD) | +0.0341 | +0.32 | 65% | 20 | -4.83% | ⚠️ flips / too few dates |
| valuation_score | -0.0341 | -0.48 | 70% | 20 | +2.75% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

