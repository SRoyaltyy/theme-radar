# Factor report — multi-date aggregate

_Generated 2026-08-20 17:20 EDT from 10 scan dates._

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
| 2026-08-18 | 2026-08-17 | 2026-08-19 | 2026-08-20 | — | 11572 |
| 2026-08-19 | 2026-08-18 | 2026-08-20 | — | — | 11587 |

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
| 2026-08-18 | +0.0486 | +0.0270 | — |
| 2026-08-19 | +0.0108 | — | — |
- **1d**: mean IC **-0.0017**, ICIR -0.02, sign consistency 50% over 10 dates
- **2d**: mean IC **-0.0399**, ICIR -0.48, sign consistency 56% over 9 dates
- **3d**: mean IC **-0.0355**, ICIR -0.36, sign consistency 62% over 8 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -28483264983952712.00 | 100% | 10 | -6.20% | ✅ consistent |
| short_fwd_2d | -0.6061 | -8.32 | 100% | 9 | -4.87% | ✅ consistent |
| short_fwd_3d | -0.4569 | -4.44 | 100% | 8 | -4.22% | ✅ consistent |
| d_Performance (Quarter) | -0.0668 | -0.50 | 67% | 9 | -2.29% | ✅ consistent |
| Beta | -0.0640 | -0.41 | 56% | 9 | -1.06% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0568 | -0.52 | 56% | 9 | -1.25% | ⚠️ flips / too few dates |
| true_ret | -0.0481 | -0.49 | 56% | 9 | -1.50% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0478 | -0.46 | 56% | 9 | -1.67% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0476 | -0.46 | 56% | 9 | -1.77% | ⚠️ flips / too few dates |
| Volatility (Month) | -0.0451 | -0.44 | 44% | 9 | +0.66% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0440 | -0.43 | 56% | 9 | -1.50% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0419 | -0.32 | 67% | 9 | -0.24% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0413 | -0.37 | 67% | 9 | -1.94% | ✅ consistent |
| exit_price_3d | +0.0404 | +0.88 | 75% | 8 | n/a | ✅ consistent |
| d_Market Cap | -0.0390 | -0.50 | 78% | 9 | -2.25% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0383 | -0.42 | 56% | 9 | -1.41% | ⚠️ flips / too few dates |
| Performance (Quarter) | -0.0349 | -0.51 | 60% | 10 | -2.11% | ⚠️ flips / too few dates |
| d_Price | -0.0335 | -0.31 | 56% | 9 | -1.50% | ⚠️ flips / too few dates |
| Gross Margin | +0.0315 | +0.41 | 50% | 10 | +0.26% | ⚠️ flips / too few dates |
| Performance (Month) | -0.0309 | -0.37 | 70% | 10 | -2.03% | ✅ consistent |
| exit_price_2d | +0.0306 | +0.59 | 67% | 9 | n/a | ✅ consistent |
| exit_price_1d | +0.0279 | +0.54 | 60% | 10 | n/a | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0269 | +0.70 | 75% | 8 | +0.50% | ✅ consistent |
| Profit Margin | +0.0263 | +0.31 | 70% | 10 | -4.12% | ✅ consistent |
| n_pos | -0.0227 | -0.29 | 50% | 10 | n/a | ⚠️ flips / too few dates |
| 20-Day Simple Moving Average | -0.0227 | -0.23 | 50% | 10 | -2.35% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0219 | +0.41 | 60% | 10 | -1.54% | ⚠️ flips / too few dates |
| d_Beta | -0.0219 | -0.37 | 50% | 8 | -0.71% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0208 | +0.49 | 60% | 10 | -0.42% | ⚠️ flips / too few dates |
| Market Cap | +0.0195 | +0.51 | 70% | 10 | n/a | ✅ consistent |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -19107155017577316.00 | 100% | 9 | -9.49% | ✅ consistent |
| short_fwd_3d | -0.7073 | -8.78 | 100% | 8 | -8.16% | ✅ consistent |
| short_fwd_1d | -0.6061 | -8.32 | 100% | 9 | -5.29% | ✅ consistent |
| d_Forward P/E | -0.0736 | -0.56 | 75% | 8 | -0.55% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0685 | -0.55 | 75% | 8 | -2.82% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0634 | -0.47 | 75% | 8 | -2.90% | ✅ consistent |
| true_ret | -0.0624 | -0.49 | 75% | 8 | -2.62% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0618 | -0.53 | 75% | 8 | -3.32% | ✅ consistent |
| Beta | -0.0618 | -0.37 | 62% | 8 | -2.38% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0594 | -0.46 | 75% | 8 | -2.78% | ✅ consistent |
| d_Performance (Quarter) | -0.0541 | -0.46 | 50% | 8 | -2.81% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0534 | -0.55 | 50% | 8 | -2.20% | ⚠️ flips / too few dates |
| d_Price | -0.0517 | -0.39 | 62% | 8 | -2.62% | ⚠️ flips / too few dates |
| price_score | -0.0515 | -0.61 | 62% | 8 | -4.14% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0507 | -0.39 | 50% | 8 | -2.23% | ⚠️ flips / too few dates |
| n_pos | -0.0500 | -0.54 | 78% | 9 | n/a | ✅ consistent |
| d_Market Cap | -0.0482 | -0.54 | 75% | 8 | -4.36% | ✅ consistent |
| exit_price_3d | +0.0481 | +0.83 | 88% | 8 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0480 | -0.31 | 62% | 8 | -1.36% | ⚠️ flips / too few dates |
| Performance (Month) | -0.0473 | -0.73 | 78% | 9 | -4.20% | ✅ consistent |
| Gross Margin | +0.0471 | +0.60 | 67% | 9 | +0.18% | ✅ consistent |
| Volatility (Month) | -0.0429 | -0.38 | 62% | 8 | +1.24% | ⚠️ flips / too few dates |
| w_pos | -0.0411 | -0.45 | 56% | 9 | n/a | ⚠️ flips / too few dates |
| total_score | -0.0399 | -0.48 | 56% | 9 | -2.33% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0386 | +0.61 | 78% | 9 | n/a | ✅ consistent |
| 20-Day Simple Moving Average | -0.0367 | -0.36 | 67% | 9 | -4.81% | ✅ consistent |
| d_Volatility (Month) | +0.0349 | +0.62 | 57% | 7 | +1.38% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0329 | -0.28 | 67% | 9 | -4.80% | ✅ consistent |
| Market Cap | +0.0315 | +0.78 | 78% | 9 | n/a | ✅ consistent |
| Sales Year Over Year TTM | +0.0312 | +0.68 | 67% | 9 | -1.14% | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -18014398509481984.00 | 100% | 8 | -11.64% | ✅ consistent |
| short_fwd_2d | -0.7073 | -8.78 | 100% | 8 | -8.77% | ✅ consistent |
| short_fwd_1d | -0.4569 | -4.44 | 100% | 8 | -4.23% | ✅ consistent |
| d_Performance (Week) | -0.0985 | -0.75 | 86% | 7 | -1.36% | ✅ consistent |
| d_Performance (Month) | -0.0852 | -1.08 | 86% | 7 | -2.56% | ✅ consistent |
| Beta | -0.0789 | -0.42 | 57% | 7 | -4.07% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0780 | -0.95 | 86% | 7 | -0.59% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0589 | -0.45 | 71% | 7 | -3.12% | ✅ consistent |
| Performance (Month) | -0.0581 | -1.26 | 88% | 8 | -5.40% | ✅ consistent |
| Volatility (Month) | -0.0577 | -0.49 | 57% | 7 | +1.75% | ⚠️ flips / too few dates |
| price_score | -0.0564 | -0.66 | 71% | 7 | -4.84% | ✅ consistent |
| exit_price_3d | +0.0539 | +0.83 | 75% | 8 | n/a | ✅ consistent |
| Gross Margin | +0.0525 | +0.78 | 75% | 8 | +1.24% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0525 | -0.42 | 57% | 7 | -3.20% | ⚠️ flips / too few dates |
| 20-Day Simple Moving Average | -0.0508 | -0.43 | 62% | 8 | -6.40% | ⚠️ flips / too few dates |
| true_ret | -0.0506 | -0.40 | 71% | 7 | -3.28% | ✅ consistent |
| d_Market Cap | -0.0479 | -0.73 | 86% | 7 | -5.33% | ✅ consistent |
| d_Performance (YTD) | -0.0471 | -0.36 | 71% | 7 | -3.34% | ✅ consistent |
| Profit Margin | +0.0456 | +0.63 | 88% | 8 | -10.23% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0445 | -0.48 | 71% | 7 | -3.91% | ✅ consistent |
| exit_price_2d | +0.0439 | +0.66 | 75% | 8 | n/a | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0415 | +0.72 | 75% | 8 | -4.99% | ✅ consistent |
| Sales Year Over Year TTM | +0.0413 | +0.82 | 75% | 8 | -1.26% | ✅ consistent |
| d_Price | -0.0400 | -0.31 | 71% | 7 | -3.28% | ✅ consistent |
| Market Cap | +0.0399 | +0.95 | 75% | 8 | n/a | ✅ consistent |
| d_Performance (Quarter) | -0.0395 | -0.38 | 57% | 7 | -3.09% | ⚠️ flips / too few dates |
| w_pos | -0.0378 | -0.39 | 50% | 8 | n/a | ⚠️ flips / too few dates |
| n_pos | -0.0373 | -0.40 | 62% | 8 | n/a | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0368 | +0.27 | 62% | 8 | -5.05% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0365 | -0.26 | 50% | 8 | -6.02% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

