# Factor report — multi-date aggregate

_Generated 2026-09-04 18:40 EDT from 20 scan dates._

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
| 2026-09-02 | 2026-09-01 | 2026-09-03 | 2026-09-04 | — | 11629 |
| 2026-09-03 | 2026-09-02 | 2026-09-04 | — | — | 11630 |

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
| 2026-09-02 | -0.0842 | -0.1304 | — |
| 2026-09-03 | -0.0656 | — | — |
- **1d**: mean IC **-0.0250**, ICIR -0.31, sign consistency 70% over 20 dates
- **2d**: mean IC **-0.0366**, ICIR -0.42, sign consistency 53% over 19 dates
- **3d**: mean IC **-0.0253**, ICIR -0.23, sign consistency 56% over 18 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -23256488473055812.00 | 100% | 20 | -6.17% | ✅ consistent |
| short_fwd_2d | -0.6115 | -8.31 | 100% | 19 | -4.89% | ✅ consistent |
| short_fwd_3d | -0.4821 | -4.16 | 100% | 18 | -4.23% | ✅ consistent |
| d_Performance (Week) | -0.0682 | -0.73 | 68% | 19 | -0.71% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0643 | -0.66 | 63% | 19 | -0.74% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0638 | -0.62 | 58% | 19 | -0.72% | ⚠️ flips / too few dates |
| true_ret | -0.0615 | -0.63 | 58% | 19 | -0.83% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0586 | -0.58 | 58% | 19 | -0.92% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0561 | -0.61 | 58% | 19 | -0.49% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0511 | -0.54 | 74% | 19 | -1.11% | ✅ consistent |
| d_Performance (Quarter) | -0.0482 | -0.39 | 58% | 19 | -0.94% | ⚠️ flips / too few dates |
| Volatility (Month) | -0.0479 | -0.38 | 47% | 19 | +0.66% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0465 | -0.44 | 74% | 19 | -0.24% | ✅ consistent |
| d_Price | -0.0442 | -0.43 | 58% | 19 | -0.83% | ⚠️ flips / too few dates |
| Forward P/E | -0.0442 | -0.52 | 70% | 20 | n/a | ✅ consistent |
| d_Market Cap | -0.0425 | -0.59 | 74% | 19 | -0.87% | ✅ consistent |
| Performance (Week) | -0.0415 | -0.30 | 65% | 20 | -1.63% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0409 | +0.64 | 68% | 19 | n/a | ✅ consistent |
| exit_price_1d | +0.0390 | +0.61 | 65% | 20 | n/a | ⚠️ flips / too few dates |
| Profit Margin | +0.0375 | +0.39 | 65% | 20 | -2.91% | ⚠️ flips / too few dates |
| n_pos | -0.0372 | -0.46 | 60% | 20 | n/a | ⚠️ flips / too few dates |
| exit_price_3d | +0.0332 | +0.58 | 67% | 18 | n/a | ✅ consistent |
| Beta | -0.0312 | -0.17 | 53% | 19 | -1.39% | ⚠️ flips / too few dates |
| price_score | -0.0306 | -0.34 | 68% | 19 | -1.04% | ✅ consistent |
| Market Cap | +0.0288 | +0.52 | 70% | 20 | n/a | ✅ consistent |
| Gross Margin | +0.0262 | +0.38 | 60% | 20 | -0.96% | ⚠️ flips / too few dates |
| w_pos | -0.0253 | -0.30 | 60% | 20 | n/a | ⚠️ flips / too few dates |
| 20-Day Simple Moving Average | -0.0253 | -0.21 | 60% | 20 | -1.63% | ⚠️ flips / too few dates |
| total_score | -0.0250 | -0.31 | 70% | 20 | -0.74% | ✅ consistent |
| Performance (Month) | -0.0242 | -0.23 | 60% | 20 | -1.67% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -17558263751735406.00 | 100% | 19 | -9.58% | ✅ consistent |
| short_fwd_3d | -0.7183 | -8.40 | 100% | 18 | -8.24% | ✅ consistent |
| short_fwd_1d | -0.6115 | -8.31 | 100% | 19 | -5.65% | ✅ consistent |
| Forward P/E | -0.0674 | -0.81 | 74% | 19 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0632 | -0.48 | 72% | 18 | -1.46% | ✅ consistent |
| Volatility (Month) | -0.0606 | -0.50 | 67% | 18 | +1.24% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0586 | -0.42 | 61% | 18 | -1.67% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0555 | -0.55 | 72% | 18 | -2.31% | ✅ consistent |
| d_Performance (YTD) | -0.0538 | -0.39 | 67% | 18 | -2.09% | ✅ consistent |
| true_ret | -0.0537 | -0.40 | 61% | 18 | -1.80% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0535 | -0.39 | 56% | 18 | -0.62% | ⚠️ flips / too few dates |
| Profit Margin | +0.0535 | +0.74 | 79% | 19 | -5.42% | ✅ consistent |
| exit_price_2d | +0.0509 | +0.90 | 84% | 19 | n/a | ✅ consistent |
| d_Forward P/E | -0.0498 | -0.41 | 67% | 18 | -0.40% | ✅ consistent |
| d_Price | -0.0487 | -0.35 | 61% | 18 | -1.80% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0484 | -0.37 | 61% | 18 | -1.13% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0476 | -0.42 | 44% | 18 | -1.59% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0463 | -0.51 | 67% | 18 | -2.87% | ✅ consistent |
| price_score | -0.0462 | -0.44 | 50% | 18 | -2.62% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0461 | +0.84 | 78% | 18 | n/a | ✅ consistent |
| Gross Margin | +0.0420 | +0.64 | 68% | 19 | -1.74% | ✅ consistent |
| Beta | -0.0412 | -0.22 | 67% | 18 | -2.94% | ✅ consistent |
| exit_price_1d | +0.0397 | +0.70 | 74% | 19 | n/a | ✅ consistent |
| Market Cap | +0.0388 | +0.77 | 74% | 19 | n/a | ✅ consistent |
| n_pos | -0.0378 | -0.42 | 68% | 19 | n/a | ✅ consistent |
| total_score | -0.0366 | -0.42 | 53% | 19 | -1.55% | ⚠️ flips / too few dates |
| w_pos | -0.0321 | -0.40 | 58% | 19 | n/a | ⚠️ flips / too few dates |
| Average Volume | -0.0314 | -0.56 | 68% | 19 | n/a | ✅ consistent |
| Performance (Week) | -0.0291 | -0.21 | 58% | 19 | -2.92% | ⚠️ flips / too few dates |
| Price | +0.0280 | +0.48 | 68% | 19 | n/a | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -13510798882111488.00 | 100% | 18 | -11.89% | ✅ consistent |
| short_fwd_2d | -0.7183 | -8.40 | 100% | 18 | -8.80% | ✅ consistent |
| short_fwd_1d | -0.4821 | -4.16 | 100% | 18 | -4.80% | ✅ consistent |
| Forward P/E | -0.0836 | -1.00 | 72% | 18 | n/a | ✅ consistent |
| Volatility (Month) | -0.0787 | -0.65 | 65% | 17 | +2.17% | ⚠️ flips / too few dates |
| Profit Margin | +0.0645 | +0.91 | 83% | 18 | -6.95% | ✅ consistent |
| d_Performance (Week) | -0.0629 | -0.46 | 76% | 17 | -0.09% | ✅ consistent |
| Beta | -0.0607 | -0.34 | 53% | 17 | -4.75% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0538 | +0.96 | 83% | 18 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0534 | -0.41 | 65% | 17 | -1.14% | ⚠️ flips / too few dates |
| Gross Margin | +0.0505 | +0.99 | 83% | 18 | -2.11% | ✅ consistent |
| d_Performance (Month) | -0.0496 | -0.42 | 76% | 17 | -1.41% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0469 | -0.34 | 59% | 17 | -1.33% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0444 | +0.78 | 83% | 18 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0427 | -0.31 | 65% | 17 | -1.87% | ⚠️ flips / too few dates |
| true_ret | -0.0417 | -0.31 | 65% | 17 | -1.74% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0404 | -0.48 | 71% | 17 | -2.82% | ✅ consistent |
| Market Cap | +0.0403 | +0.87 | 83% | 18 | n/a | ✅ consistent |
| price_score | -0.0384 | -0.33 | 59% | 17 | -2.24% | ⚠️ flips / too few dates |
| Average Volume | -0.0375 | -0.70 | 67% | 18 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0362 | -0.29 | 59% | 17 | -0.57% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0354 | +0.61 | 72% | 18 | n/a | ✅ consistent |
| d_Price | -0.0344 | -0.25 | 65% | 17 | -1.74% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0342 | -0.30 | 65% | 17 | -0.41% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0325 | -0.34 | 65% | 17 | -2.08% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0302 | +0.32 | 67% | 18 | -4.87% | ✅ consistent |
| n_pos | -0.0293 | -0.30 | 56% | 18 | n/a | ⚠️ flips / too few dates |
| w_pos | -0.0293 | -0.31 | 56% | 18 | n/a | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0289 | +0.35 | 44% | 18 | -4.20% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0286 | +0.33 | 56% | 18 | n/a | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

