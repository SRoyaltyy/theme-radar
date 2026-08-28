# Factor report — multi-date aggregate

_Generated 2026-08-28 01:03 EDT from 15 scan dates._

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
| 2026-08-25 | 2026-08-24 | 2026-08-26 | 2026-08-28 | — | 11611 |
| 2026-08-26 | 2026-08-25 | 2026-08-28 | — | — | 11621 |

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
| 2026-08-24 | +0.0056 | -0.0285 | -0.0867 |
| 2026-08-25 | -0.0503 | +0.0041 | — |
| 2026-08-26 | +0.0468 | — | — |
- **1d**: mean IC **-0.0064**, ICIR -0.07, sign consistency 53% over 15 dates
- **2d**: mean IC **-0.0188**, ICIR -0.25, sign consistency 43% over 14 dates
- **3d**: mean IC **-0.0170**, ICIR -0.17, sign consistency 54% over 13 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -24667231058826812.00 | 100% | 15 | -5.76% | ✅ consistent |
| short_fwd_2d | -0.6009 | -9.37 | 100% | 14 | -4.38% | ✅ consistent |
| short_fwd_3d | -0.4988 | -4.74 | 100% | 13 | -4.06% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0824 | -0.83 | 71% | 14 | -0.91% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0823 | -0.84 | 71% | 14 | -0.87% | ✅ consistent |
| true_ret | -0.0821 | -0.86 | 71% | 14 | -0.95% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0814 | -0.84 | 71% | 14 | -0.60% | ✅ consistent |
| d_Performance (YTD) | -0.0781 | -0.80 | 71% | 14 | -0.84% | ✅ consistent |
| d_Performance (Quarter) | -0.0699 | -0.59 | 64% | 14 | -0.95% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0666 | -0.69 | 71% | 14 | -0.70% | ✅ consistent |
| d_Price | -0.0638 | -0.64 | 71% | 14 | -0.95% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0629 | -0.64 | 79% | 14 | -1.10% | ✅ consistent |
| d_Forward P/E | -0.0563 | -0.52 | 79% | 14 | -0.26% | ✅ consistent |
| d_Market Cap | -0.0552 | -0.78 | 86% | 14 | -1.10% | ✅ consistent |
| Gross Margin | +0.0343 | +0.49 | 60% | 15 | +0.16% | ⚠️ flips / too few dates |
| Volatility (Month) | -0.0328 | -0.29 | 43% | 14 | +0.66% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0325 | +0.54 | 64% | 14 | n/a | ⚠️ flips / too few dates |
| exit_price_1d | +0.0318 | +0.54 | 67% | 15 | n/a | ✅ consistent |
| n_pos | -0.0315 | -0.39 | 60% | 15 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0302 | -0.21 | 67% | 15 | -1.73% | ✅ consistent |
| technical_score | -0.0282 | -0.43 | 73% | 15 | -2.94% | ✅ consistent |
| 20-Day Simple Moving Average | -0.0261 | -0.25 | 60% | 15 | -1.86% | ⚠️ flips / too few dates |
| Market Cap | +0.0245 | +0.54 | 67% | 15 | n/a | ✅ consistent |
| exit_price_3d | +0.0239 | +0.46 | 62% | 13 | n/a | ⚠️ flips / too few dates |
| Profit Margin | +0.0234 | +0.24 | 60% | 15 | -3.48% | ⚠️ flips / too few dates |
| Beta | -0.0226 | -0.13 | 50% | 14 | -1.02% | ⚠️ flips / too few dates |
| Performance (Quarter) | -0.0222 | -0.28 | 60% | 15 | -1.89% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0220 | +0.47 | 60% | 15 | -0.56% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0216 | +0.43 | 60% | 15 | -1.41% | ⚠️ flips / too few dates |
| Forward P/E | -0.0195 | -0.28 | 60% | 15 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -19457774262956300.00 | 100% | 14 | -8.66% | ✅ consistent |
| short_fwd_3d | -0.7175 | -10.40 | 100% | 13 | -7.60% | ✅ consistent |
| short_fwd_1d | -0.6009 | -9.37 | 100% | 14 | -5.21% | ✅ consistent |
| d_Forward P/E | -0.0565 | -0.46 | 69% | 13 | -0.40% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0563 | -0.48 | 77% | 13 | -1.45% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0556 | -0.52 | 77% | 13 | -2.16% | ✅ consistent |
| d_Performance (Quarter) | -0.0524 | -0.48 | 54% | 13 | -1.27% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0512 | -0.40 | 69% | 13 | -1.69% | ✅ consistent |
| true_ret | -0.0499 | -0.41 | 69% | 13 | -1.64% | ✅ consistent |
| d_Performance (YTD) | -0.0479 | -0.38 | 77% | 13 | -1.85% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0469 | -0.39 | 62% | 13 | -1.15% | ⚠️ flips / too few dates |
| Gross Margin | +0.0464 | +0.64 | 64% | 14 | +0.43% | ⚠️ flips / too few dates |
| d_Price | -0.0434 | -0.34 | 62% | 13 | -1.64% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0429 | -0.53 | 69% | 13 | -2.97% | ✅ consistent |
| exit_price_2d | +0.0412 | +0.73 | 79% | 14 | n/a | ✅ consistent |
| Volatility (Month) | -0.0380 | -0.41 | 69% | 13 | +1.24% | ✅ consistent |
| exit_price_3d | +0.0358 | +0.65 | 69% | 13 | n/a | ✅ consistent |
| Market Cap | +0.0323 | +0.83 | 79% | 14 | n/a | ✅ consistent |
| n_pos | -0.0314 | -0.34 | 64% | 14 | n/a | ⚠️ flips / too few dates |
| Profit Margin | +0.0304 | +0.44 | 71% | 14 | -6.57% | ✅ consistent |
| exit_price_1d | +0.0299 | +0.52 | 64% | 14 | n/a | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0297 | -0.21 | 54% | 13 | -0.76% | ⚠️ flips / too few dates |
| Forward P/E | -0.0291 | -0.43 | 57% | 14 | n/a | ⚠️ flips / too few dates |
| Beta | -0.0289 | -0.20 | 62% | 13 | -2.44% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0247 | +0.54 | 57% | 14 | -1.10% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0247 | -0.17 | 57% | 14 | -3.12% | ⚠️ flips / too few dates |
| technical_score | -0.0244 | -0.41 | 64% | 14 | -5.39% | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0226 | +0.46 | 67% | 12 | +0.82% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0223 | +0.44 | 71% | 14 | -2.68% | ✅ consistent |
| 20-Day Simple Moving Average | -0.0221 | -0.20 | 57% | 14 | -3.64% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -14523672396400896.00 | 100% | 13 | -10.98% | ✅ consistent |
| short_fwd_2d | -0.7175 | -10.40 | 100% | 13 | -8.16% | ✅ consistent |
| short_fwd_1d | -0.4988 | -4.74 | 100% | 13 | -4.73% | ✅ consistent |
| d_Performance (Week) | -0.0622 | -0.42 | 75% | 12 | -0.26% | ✅ consistent |
| Gross Margin | +0.0557 | +1.00 | 85% | 13 | +1.40% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0528 | -0.36 | 67% | 12 | -1.34% | ✅ consistent |
| Volatility (Month) | -0.0495 | -0.48 | 50% | 12 | +2.17% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0458 | -0.41 | 58% | 12 | -1.26% | ⚠️ flips / too few dates |
| true_ret | -0.0441 | -0.31 | 67% | 12 | -1.85% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0437 | -0.30 | 58% | 12 | -1.57% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0425 | -0.32 | 67% | 12 | -0.41% | ✅ consistent |
| exit_price_3d | +0.0419 | +0.73 | 77% | 13 | n/a | ✅ consistent |
| Beta | -0.0419 | -0.25 | 50% | 12 | -3.93% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0416 | -0.28 | 67% | 12 | -1.80% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0386 | -0.31 | 67% | 12 | -2.10% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0373 | -0.27 | 58% | 12 | -0.66% | ⚠️ flips / too few dates |
| Forward P/E | -0.0372 | -0.53 | 54% | 13 | n/a | ⚠️ flips / too few dates |
| Profit Margin | +0.0355 | +0.46 | 69% | 13 | -8.57% | ✅ consistent |
| d_Market Cap | -0.0352 | -0.41 | 75% | 12 | -3.08% | ✅ consistent |
| Market Cap | +0.0343 | +0.96 | 85% | 13 | n/a | ✅ consistent |
| d_Price | -0.0326 | -0.21 | 67% | 12 | -1.85% | ✅ consistent |
| d_Performance (Month) | -0.0324 | -0.30 | 67% | 12 | -1.29% | ✅ consistent |
| exit_price_2d | +0.0322 | +0.55 | 77% | 13 | n/a | ✅ consistent |
| Sales Year Over Year TTM | +0.0264 | +0.49 | 54% | 13 | -1.62% | ⚠️ flips / too few dates |
| d_Beta | +0.0244 | +0.34 | 55% | 11 | -2.14% | ⚠️ flips / too few dates |
| price_score | -0.0243 | -0.25 | 67% | 12 | -2.34% | ✅ consistent |
| 20-Day Simple Moving Average | -0.0241 | -0.22 | 54% | 13 | -4.74% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0237 | +0.42 | 54% | 13 | -3.98% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0236 | +0.39 | 62% | 13 | n/a | ⚠️ flips / too few dates |
| Analyst Recom | -0.0227 | -0.42 | 62% | 13 | n/a | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

