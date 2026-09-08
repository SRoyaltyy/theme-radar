# Factor report — multi-date aggregate

_Generated 2026-09-08 19:05 EDT from 21 scan dates._

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
| 2026-09-03 | 2026-09-02 | 2026-09-04 | 2026-09-08 | — | 11630 |
| 2026-09-04 | 2026-09-03 | 2026-09-08 | — | — | 11593 |

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
| 2026-09-03 | -0.0656 | -0.0607 | — |
| 2026-09-04 | -0.0292 | — | — |
- **1d**: mean IC **-0.0252**, ICIR -0.32, sign consistency 71% over 21 dates
- **2d**: mean IC **-0.0378**, ICIR -0.44, sign consistency 55% over 20 dates
- **3d**: mean IC **-0.0329**, ICIR -0.30, sign consistency 58% over 19 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -23830809237250984.00 | 100% | 21 | -6.28% | ✅ consistent |
| short_fwd_2d | -0.6107 | -8.50 | 100% | 20 | -4.85% | ✅ consistent |
| short_fwd_3d | -0.4804 | -4.25 | 100% | 19 | -4.12% | ✅ consistent |
| d_Performance (Week) | -0.0580 | -0.57 | 65% | 20 | -0.68% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0562 | -0.53 | 55% | 20 | -0.68% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0559 | -0.55 | 60% | 20 | -0.69% | ⚠️ flips / too few dates |
| true_ret | -0.0542 | -0.54 | 55% | 20 | -0.81% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0514 | -0.50 | 55% | 20 | -0.87% | ⚠️ flips / too few dates |
| Volatility (Month) | -0.0501 | -0.41 | 50% | 20 | +0.66% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0493 | -0.52 | 55% | 20 | -0.47% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0444 | -0.46 | 70% | 20 | -1.06% | ✅ consistent |
| d_Performance (Quarter) | -0.0412 | -0.33 | 55% | 20 | -0.92% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0405 | -0.38 | 70% | 20 | -0.21% | ✅ consistent |
| exit_price_3d | +0.0405 | +0.63 | 68% | 19 | n/a | ✅ consistent |
| d_Market Cap | -0.0396 | -0.56 | 70% | 20 | -0.90% | ✅ consistent |
| n_pos | -0.0388 | -0.49 | 62% | 21 | n/a | ⚠️ flips / too few dates |
| exit_price_2d | +0.0382 | +0.60 | 65% | 20 | n/a | ⚠️ flips / too few dates |
| d_Price | -0.0365 | -0.34 | 55% | 20 | -0.81% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0362 | +0.57 | 62% | 21 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0360 | -0.27 | 62% | 21 | -1.59% | ⚠️ flips / too few dates |
| Profit Margin | +0.0357 | +0.38 | 62% | 21 | -2.82% | ⚠️ flips / too few dates |
| Beta | -0.0352 | -0.20 | 55% | 20 | -1.37% | ⚠️ flips / too few dates |
| Forward P/E | -0.0343 | -0.36 | 67% | 21 | n/a | ✅ consistent |
| w_pos | -0.0281 | -0.34 | 62% | 21 | n/a | ⚠️ flips / too few dates |
| price_score | -0.0275 | -0.31 | 65% | 20 | -0.96% | ⚠️ flips / too few dates |
| Market Cap | +0.0268 | +0.49 | 67% | 21 | n/a | ✅ consistent |
| Average Volume | -0.0263 | -0.42 | 62% | 21 | n/a | ⚠️ flips / too few dates |
| 20-Day Simple Moving Average | -0.0261 | -0.22 | 62% | 21 | -1.63% | ⚠️ flips / too few dates |
| total_score | -0.0252 | -0.32 | 71% | 21 | -0.72% | ✅ consistent |
| Performance (Month) | -0.0245 | -0.24 | 62% | 21 | -1.68% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -18014398509481984.00 | 100% | 20 | -9.64% | ✅ consistent |
| short_fwd_3d | -0.7168 | -8.58 | 100% | 19 | -8.09% | ✅ consistent |
| short_fwd_1d | -0.6107 | -8.50 | 100% | 20 | -5.59% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0651 | -0.51 | 74% | 19 | -1.51% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0633 | -0.46 | 63% | 19 | -1.70% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0608 | -0.44 | 58% | 19 | -0.69% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0597 | -0.60 | 74% | 19 | -2.34% | ✅ consistent |
| Volatility (Month) | -0.0596 | -0.51 | 68% | 19 | +1.24% | ✅ consistent |
| Forward P/E | -0.0595 | -0.68 | 70% | 20 | n/a | ✅ consistent |
| true_ret | -0.0581 | -0.44 | 63% | 19 | -1.85% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0577 | -0.43 | 68% | 19 | -2.13% | ✅ consistent |
| d_Price | -0.0528 | -0.39 | 63% | 19 | -1.85% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0518 | -0.40 | 63% | 19 | -1.19% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0511 | -0.43 | 68% | 19 | -0.40% | ✅ consistent |
| exit_price_3d | +0.0500 | +0.89 | 79% | 19 | n/a | ✅ consistent |
| Profit Margin | +0.0498 | +0.69 | 75% | 20 | -5.37% | ✅ consistent |
| d_Market Cap | -0.0482 | -0.55 | 68% | 19 | -2.85% | ✅ consistent |
| exit_price_2d | +0.0473 | +0.82 | 80% | 20 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0453 | -0.40 | 47% | 19 | -1.63% | ⚠️ flips / too few dates |
| n_pos | -0.0435 | -0.48 | 70% | 20 | n/a | ✅ consistent |
| price_score | -0.0435 | -0.43 | 47% | 19 | -2.64% | ⚠️ flips / too few dates |
| Beta | -0.0413 | -0.23 | 68% | 19 | -2.81% | ✅ consistent |
| total_score | -0.0378 | -0.44 | 55% | 20 | -1.47% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0359 | +0.62 | 70% | 20 | n/a | ✅ consistent |
| w_pos | -0.0355 | -0.44 | 60% | 20 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0350 | -0.25 | 60% | 20 | -2.72% | ⚠️ flips / too few dates |
| Market Cap | +0.0343 | +0.65 | 70% | 20 | n/a | ✅ consistent |
| Gross Margin | +0.0328 | +0.44 | 65% | 20 | -1.73% | ⚠️ flips / too few dates |
| Average Volume | -0.0327 | -0.59 | 70% | 20 | n/a | ✅ consistent |
| Performance (YTD) | +0.0275 | +0.27 | 60% | 20 | -3.67% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -13881026303364274.00 | 100% | 19 | -11.78% | ✅ consistent |
| short_fwd_2d | -0.7168 | -8.58 | 100% | 19 | -8.58% | ✅ consistent |
| short_fwd_1d | -0.4804 | -4.25 | 100% | 19 | -4.66% | ✅ consistent |
| Forward P/E | -0.0758 | -0.86 | 68% | 19 | n/a | ✅ consistent |
| Volatility (Month) | -0.0746 | -0.62 | 67% | 18 | +2.17% | ✅ consistent |
| Profit Margin | +0.0626 | +0.90 | 84% | 19 | -6.88% | ✅ consistent |
| d_Performance (Week) | -0.0625 | -0.47 | 78% | 18 | -0.21% | ✅ consistent |
| d_Performance (Month) | -0.0587 | -0.49 | 78% | 18 | -1.44% | ✅ consistent |
| exit_price_3d | +0.0548 | +1.00 | 84% | 19 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0512 | -0.41 | 67% | 18 | -1.22% | ✅ consistent |
| Beta | -0.0498 | -0.28 | 50% | 18 | -4.40% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0474 | -0.36 | 61% | 18 | -1.43% | ⚠️ flips / too few dates |
| price_score | -0.0464 | -0.39 | 61% | 18 | -2.39% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0452 | +0.81 | 84% | 19 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0428 | -0.32 | 67% | 18 | -1.96% | ✅ consistent |
| Gross Margin | +0.0425 | +0.71 | 79% | 19 | -2.08% | ✅ consistent |
| true_ret | -0.0421 | -0.32 | 67% | 18 | -1.84% | ✅ consistent |
| d_Market Cap | -0.0399 | -0.49 | 72% | 18 | -2.91% | ✅ consistent |
| Market Cap | +0.0398 | +0.88 | 84% | 19 | n/a | ✅ consistent |
| Average Volume | -0.0394 | -0.75 | 68% | 19 | n/a | ✅ consistent |
| exit_price_1d | +0.0364 | +0.64 | 74% | 19 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0359 | -0.29 | 61% | 18 | -0.69% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0356 | -0.32 | 67% | 18 | -0.41% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0353 | -0.38 | 67% | 18 | -2.16% | ✅ consistent |
| n_pos | -0.0342 | -0.35 | 58% | 19 | n/a | ⚠️ flips / too few dates |
| w_pos | -0.0340 | -0.36 | 58% | 19 | n/a | ⚠️ flips / too few dates |
| d_Price | -0.0338 | -0.25 | 67% | 18 | -1.84% | ✅ consistent |
| total_score | -0.0329 | -0.30 | 58% | 19 | -1.49% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0307 | +0.28 | 63% | 19 | -4.85% | ⚠️ flips / too few dates |
| valuation_score | -0.0289 | -0.42 | 68% | 19 | +2.68% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

