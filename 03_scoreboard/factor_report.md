# Factor report — multi-date aggregate

_Generated 2026-09-11 18:56 EDT from 24 scan dates._

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
| 2026-09-09 | 2026-09-08 | 2026-09-10 | 2026-09-11 | — | 11599 |
| 2026-09-10 | 2026-09-09 | 2026-09-11 | — | — | 11616 |

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
| 2026-09-09 | -0.0163 | +0.0188 | — |
| 2026-09-10 | -0.0932 | — | — |
- **1d**: mean IC **-0.0301**, ICIR -0.40, sign consistency 75% over 24 dates
- **2d**: mean IC **-0.0405**, ICIR -0.49, sign consistency 57% over 23 dates
- **3d**: mean IC **-0.0418**, ICIR -0.40, sign consistency 64% over 22 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -19733784847061448.00 | 100% | 24 | -6.28% | ✅ consistent |
| short_fwd_2d | -0.6211 | -8.39 | 100% | 23 | -5.15% | ✅ consistent |
| short_fwd_3d | -0.4876 | -4.51 | 100% | 22 | -4.54% | ✅ consistent |
| d_Performance (Week) | -0.0681 | -0.67 | 68% | 22 | -0.71% | ✅ consistent |
| Volatility (Month) | -0.0650 | -0.51 | 57% | 23 | +0.66% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0538 | -0.49 | 55% | 22 | -0.65% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0531 | -0.50 | 59% | 22 | -0.64% | ⚠️ flips / too few dates |
| true_ret | -0.0503 | -0.47 | 55% | 22 | -0.76% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0493 | -0.45 | 55% | 22 | -0.82% | ⚠️ flips / too few dates |
| Profit Margin | +0.0488 | +0.51 | 67% | 24 | -2.73% | ✅ consistent |
| Beta | -0.0457 | -0.24 | 57% | 23 | -1.39% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0455 | -0.46 | 55% | 22 | -0.46% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0449 | +0.67 | 67% | 24 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0432 | -0.47 | 68% | 22 | -0.99% | ✅ consistent |
| n_pos | -0.0429 | -0.57 | 67% | 24 | n/a | ✅ consistent |
| d_Price | -0.0389 | -0.35 | 55% | 22 | -0.76% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0382 | -0.55 | 68% | 22 | -0.88% | ✅ consistent |
| exit_price_2d | +0.0382 | +0.63 | 65% | 23 | n/a | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0376 | -0.36 | 68% | 22 | -0.22% | ✅ consistent |
| exit_price_3d | +0.0373 | +0.60 | 64% | 22 | n/a | ⚠️ flips / too few dates |
| Forward P/E | -0.0371 | -0.40 | 67% | 24 | n/a | ✅ consistent |
| w_pos | -0.0342 | -0.43 | 67% | 24 | n/a | ✅ consistent |
| Average Volume | -0.0341 | -0.53 | 67% | 24 | n/a | ✅ consistent |
| Performance (Week) | -0.0339 | -0.26 | 58% | 24 | -1.52% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0312 | -0.25 | 55% | 22 | -0.91% | ⚠️ flips / too few dates |
| Market Cap | +0.0310 | +0.52 | 67% | 24 | n/a | ✅ consistent |
| total_score | -0.0301 | -0.40 | 75% | 24 | -0.73% | ✅ consistent |
| valuation_score | -0.0295 | -0.32 | 67% | 24 | +1.15% | ✅ consistent |
| Price | +0.0288 | +0.42 | 62% | 24 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0288 | +0.42 | 62% | 24 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16326935166580028.00 | 100% | 23 | -9.89% | ✅ consistent |
| short_fwd_3d | -0.7265 | -8.92 | 100% | 22 | -8.72% | ✅ consistent |
| short_fwd_1d | -0.6211 | -8.39 | 100% | 23 | -5.82% | ✅ consistent |
| Volatility (Month) | -0.0828 | -0.65 | 73% | 22 | +1.24% | ✅ consistent |
| Beta | -0.0663 | -0.36 | 73% | 22 | -2.79% | ✅ consistent |
| Profit Margin | +0.0650 | +0.81 | 78% | 23 | -5.08% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0576 | -0.46 | 71% | 21 | -1.39% | ✅ consistent |
| Forward P/E | -0.0575 | -0.65 | 70% | 23 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0566 | -0.43 | 57% | 21 | -0.73% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0565 | -0.42 | 62% | 21 | -1.60% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0561 | -0.58 | 71% | 21 | -2.17% | ✅ consistent |
| exit_price_2d | +0.0540 | +0.91 | 83% | 23 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0512 | -0.39 | 67% | 21 | -1.98% | ✅ consistent |
| true_ret | -0.0503 | -0.39 | 57% | 21 | -1.74% | ⚠️ flips / too few dates |
| n_pos | -0.0494 | -0.56 | 74% | 23 | n/a | ✅ consistent |
| d_Price | -0.0484 | -0.37 | 62% | 21 | -1.74% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0481 | +0.87 | 77% | 22 | n/a | ✅ consistent |
| d_Market Cap | -0.0468 | -0.56 | 71% | 21 | -2.74% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0460 | -0.37 | 57% | 21 | -1.12% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0456 | -0.40 | 67% | 21 | -0.37% | ✅ consistent |
| w_pos | -0.0446 | -0.55 | 65% | 23 | n/a | ⚠️ flips / too few dates |
| Average Volume | -0.0444 | -0.73 | 74% | 23 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0431 | -0.40 | 52% | 21 | -1.49% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0428 | +0.71 | 74% | 23 | n/a | ✅ consistent |
| Short Float | -0.0406 | -0.37 | 57% | 23 | n/a | ⚠️ flips / too few dates |
| total_score | -0.0405 | -0.49 | 57% | 23 | -1.40% | ⚠️ flips / too few dates |
| valuation_score | -0.0392 | -0.49 | 61% | 23 | +2.02% | ⚠️ flips / too few dates |
| price_score | -0.0380 | -0.38 | 48% | 21 | -2.56% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0355 | +0.37 | 65% | 23 | -3.53% | ⚠️ flips / too few dates |
| Market Cap | +0.0347 | +0.65 | 70% | 23 | n/a | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -14936750169972328.00 | 100% | 22 | -12.44% | ✅ consistent |
| short_fwd_2d | -0.7265 | -8.92 | 100% | 22 | -8.89% | ✅ consistent |
| short_fwd_1d | -0.4876 | -4.51 | 100% | 22 | -4.81% | ✅ consistent |
| Volatility (Month) | -0.0984 | -0.78 | 71% | 21 | +2.17% | ✅ consistent |
| Beta | -0.0768 | -0.43 | 57% | 21 | -4.26% | ⚠️ flips / too few dates |
| Profit Margin | +0.0751 | +1.01 | 86% | 22 | -6.60% | ✅ consistent |
| d_Performance (Week) | -0.0747 | -0.57 | 80% | 20 | -0.45% | ✅ consistent |
| Forward P/E | -0.0669 | -0.77 | 64% | 22 | n/a | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0610 | -0.53 | 80% | 20 | -1.56% | ✅ consistent |
| exit_price_3d | +0.0591 | +1.04 | 86% | 22 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0539 | -0.45 | 70% | 20 | -1.30% | ✅ consistent |
| Average Volume | -0.0532 | -0.88 | 73% | 22 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0522 | -0.40 | 65% | 20 | -1.49% | ⚠️ flips / too few dates |
| Short Float | -0.0504 | -0.47 | 68% | 22 | n/a | ✅ consistent |
| w_pos | -0.0504 | -0.51 | 64% | 22 | n/a | ⚠️ flips / too few dates |
| exit_price_2d | +0.0498 | +0.86 | 86% | 22 | n/a | ✅ consistent |
| n_pos | -0.0496 | -0.49 | 64% | 22 | n/a | ⚠️ flips / too few dates |
| valuation_score | -0.0478 | -0.59 | 73% | 22 | +2.73% | ✅ consistent |
| price_score | -0.0475 | -0.42 | 65% | 20 | -2.72% | ⚠️ flips / too few dates |
| true_ret | -0.0466 | -0.37 | 70% | 20 | -1.93% | ✅ consistent |
| d_Performance (YTD) | -0.0466 | -0.36 | 70% | 20 | -2.05% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0426 | -0.36 | 65% | 20 | -0.83% | ⚠️ flips / too few dates |
| total_score | -0.0418 | -0.40 | 64% | 22 | -1.44% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0416 | -0.54 | 75% | 20 | -2.91% | ✅ consistent |
| Performance (YTD) | +0.0407 | +0.39 | 68% | 22 | -4.71% | ✅ consistent |
| exit_price_1d | +0.0407 | +0.69 | 77% | 22 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0389 | -0.43 | 70% | 20 | -2.23% | ✅ consistent |
| d_Forward P/E | -0.0382 | -0.36 | 70% | 20 | -0.39% | ✅ consistent |
| d_Price | -0.0375 | -0.29 | 70% | 20 | -1.93% | ✅ consistent |
| Market Cap | +0.0358 | +0.75 | 77% | 22 | n/a | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

