# Factor report — multi-date aggregate

_Generated 2026-08-31 20:14 EDT from 16 scan dates._

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
| 2026-08-26 | 2026-08-25 | 2026-08-28 | 2026-08-31 | — | 11620 |
| 2026-08-28 | 2026-08-26 | 2026-08-31 | — | — | 11611 |

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
| 2026-08-26 | -0.0710 | -0.0146 | — |
| 2026-08-28 | -0.0442 | — | — |
- **1d**: mean IC **-0.0161**, ICIR -0.19, sign consistency 62% over 16 dates
- **2d**: mean IC **-0.0261**, ICIR -0.35, sign consistency 53% over 15 dates
- **3d**: mean IC **-0.0206**, ICIR -0.21, sign consistency 57% over 14 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -20801235657477236.00 | 100% | 16 | -6.05% | ✅ consistent |
| short_fwd_2d | -0.6098 | -7.70 | 100% | 15 | -4.44% | ✅ consistent |
| short_fwd_3d | -0.4767 | -4.22 | 100% | 14 | -3.85% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0664 | -0.63 | 67% | 15 | -1.00% | ✅ consistent |
| true_ret | -0.0639 | -0.62 | 60% | 15 | -1.04% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0638 | -0.55 | 60% | 15 | -1.10% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0637 | -0.59 | 60% | 15 | -1.02% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0612 | -0.63 | 60% | 15 | -0.72% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0608 | -0.63 | 67% | 15 | -0.90% | ✅ consistent |
| d_Performance (YTD) | -0.0598 | -0.57 | 60% | 15 | -0.94% | ⚠️ flips / too few dates |
| Volatility (Month) | -0.0533 | -0.45 | 53% | 15 | +0.66% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0521 | -0.52 | 73% | 15 | -1.19% | ✅ consistent |
| d_Forward P/E | -0.0507 | -0.45 | 73% | 15 | -0.24% | ✅ consistent |
| d_Price | -0.0465 | -0.43 | 60% | 15 | -1.04% | ⚠️ flips / too few dates |
| Beta | -0.0458 | -0.29 | 60% | 15 | -2.05% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0438 | -0.58 | 80% | 15 | -1.38% | ✅ consistent |
| n_pos | -0.0378 | -0.46 | 62% | 16 | n/a | ⚠️ flips / too few dates |
| Gross Margin | +0.0346 | +0.50 | 56% | 16 | -1.09% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0346 | +0.59 | 67% | 15 | n/a | ✅ consistent |
| exit_price_3d | +0.0324 | +0.54 | 64% | 14 | n/a | ⚠️ flips / too few dates |
| Profit Margin | +0.0320 | +0.32 | 62% | 16 | -3.68% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0309 | +0.51 | 62% | 16 | n/a | ⚠️ flips / too few dates |
| Forward P/E | -0.0308 | -0.38 | 62% | 16 | n/a | ⚠️ flips / too few dates |
| Average Volume | -0.0262 | -0.42 | 62% | 16 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0260 | -0.19 | 62% | 16 | -1.83% | ⚠️ flips / too few dates |
| w_pos | -0.0240 | -0.27 | 56% | 16 | n/a | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0238 | +0.59 | 71% | 14 | +0.91% | ✅ consistent |
| Market Cap | +0.0217 | +0.48 | 69% | 16 | n/a | ✅ consistent |
| valuation_score | -0.0206 | -0.24 | 62% | 16 | +1.31% | ⚠️ flips / too few dates |
| price_score | -0.0176 | -0.19 | 67% | 15 | -1.32% | ✅ consistent |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -20140709820486304.00 | 100% | 15 | -8.96% | ✅ consistent |
| short_fwd_3d | -0.7123 | -8.07 | 100% | 14 | -7.48% | ✅ consistent |
| short_fwd_1d | -0.6098 | -7.70 | 100% | 15 | -5.14% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0663 | -0.54 | 79% | 14 | -1.27% | ✅ consistent |
| Volatility (Month) | -0.0651 | -0.59 | 71% | 14 | +1.24% | ✅ consistent |
| d_Forward P/E | -0.0650 | -0.51 | 71% | 14 | -0.46% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0592 | -0.45 | 64% | 14 | -1.56% | ⚠️ flips / too few dates |
| true_ret | -0.0578 | -0.45 | 64% | 14 | -1.60% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0578 | -0.54 | 79% | 14 | -2.07% | ✅ consistent |
| d_Performance (YTD) | -0.0560 | -0.44 | 71% | 14 | -1.78% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0544 | -0.45 | 64% | 14 | -0.91% | ⚠️ flips / too few dates |
| Beta | -0.0528 | -0.38 | 71% | 14 | -3.25% | ✅ consistent |
| d_Price | -0.0513 | -0.40 | 64% | 14 | -1.60% | ⚠️ flips / too few dates |
| Gross Margin | +0.0502 | +0.73 | 67% | 15 | -0.85% | ✅ consistent |
| d_Market Cap | -0.0498 | -0.57 | 71% | 14 | -2.73% | ✅ consistent |
| Forward P/E | -0.0487 | -0.65 | 67% | 15 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0471 | -0.34 | 57% | 14 | -0.60% | ⚠️ flips / too few dates |
| n_pos | -0.0448 | -0.45 | 67% | 15 | n/a | ✅ consistent |
| Profit Margin | +0.0438 | +0.58 | 73% | 15 | -6.58% | ✅ consistent |
| exit_price_3d | +0.0420 | +0.73 | 71% | 14 | n/a | ✅ consistent |
| exit_price_2d | +0.0419 | +0.74 | 80% | 15 | n/a | ✅ consistent |
| d_Performance (Quarter) | -0.0388 | -0.36 | 50% | 14 | -1.23% | ⚠️ flips / too few dates |
| w_pos | -0.0331 | -0.37 | 53% | 15 | n/a | ⚠️ flips / too few dates |
| Average Volume | -0.0320 | -0.57 | 67% | 15 | n/a | ✅ consistent |
| exit_price_1d | +0.0305 | +0.53 | 67% | 15 | n/a | ✅ consistent |
| price_score | -0.0287 | -0.37 | 50% | 14 | -2.36% | ⚠️ flips / too few dates |
| Market Cap | +0.0283 | +0.71 | 73% | 15 | n/a | ✅ consistent |
| valuation_score | -0.0264 | -0.39 | 60% | 15 | +2.25% | ⚠️ flips / too few dates |
| total_score | -0.0261 | -0.35 | 53% | 15 | -1.28% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0240 | -0.28 | 43% | 14 | -1.14% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -13758724128133476.00 | 100% | 14 | -11.13% | ✅ consistent |
| short_fwd_2d | -0.7123 | -8.07 | 100% | 14 | -7.88% | ✅ consistent |
| short_fwd_1d | -0.4767 | -4.22 | 100% | 14 | -4.54% | ✅ consistent |
| Volatility (Month) | -0.0782 | -0.74 | 62% | 13 | +2.17% | ⚠️ flips / too few dates |
| Beta | -0.0651 | -0.43 | 54% | 13 | -4.69% | ⚠️ flips / too few dates |
| Gross Margin | +0.0581 | +1.11 | 86% | 14 | +0.11% | ✅ consistent |
| d_Performance (Week) | -0.0532 | -0.40 | 77% | 13 | -0.21% | ✅ consistent |
| Forward P/E | -0.0525 | -0.78 | 64% | 14 | n/a | ⚠️ flips / too few dates |
| Profit Margin | +0.0505 | +0.72 | 79% | 14 | -8.42% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0473 | -0.38 | 69% | 13 | -1.12% | ✅ consistent |
| exit_price_3d | +0.0465 | +0.83 | 79% | 14 | n/a | ✅ consistent |
| d_Forward P/E | -0.0395 | -0.34 | 69% | 13 | -0.42% | ✅ consistent |
| d_Performance (Month) | -0.0394 | -0.40 | 77% | 13 | -1.06% | ✅ consistent |
| true_ret | -0.0388 | -0.31 | 69% | 13 | -1.69% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0380 | -0.30 | 62% | 13 | -1.33% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0369 | +0.64 | 79% | 14 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0359 | -0.28 | 69% | 13 | -1.66% | ✅ consistent |
| Average Volume | -0.0357 | -0.74 | 64% | 14 | n/a | ⚠️ flips / too few dates |
| d_Market Cap | -0.0351 | -0.45 | 77% | 13 | -2.86% | ✅ consistent |
| d_Performance (Quarter) | -0.0334 | -0.35 | 62% | 13 | -1.26% | ⚠️ flips / too few dates |
| Market Cap | +0.0318 | +0.90 | 86% | 14 | n/a | ✅ consistent |
| n_pos | -0.0317 | -0.30 | 57% | 14 | n/a | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0315 | -0.27 | 62% | 13 | -0.56% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0312 | -0.30 | 69% | 13 | -1.94% | ✅ consistent |
| w_pos | -0.0301 | -0.31 | 50% | 14 | n/a | ⚠️ flips / too few dates |
| price_score | -0.0294 | -0.31 | 69% | 13 | -2.01% | ✅ consistent |
| exit_price_1d | +0.0277 | +0.47 | 64% | 14 | n/a | ⚠️ flips / too few dates |
| valuation_score | -0.0269 | -0.46 | 64% | 14 | +3.04% | ⚠️ flips / too few dates |
| d_Price | -0.0252 | -0.19 | 69% | 13 | -1.69% | ✅ consistent |
| Short Float | -0.0228 | -0.29 | 64% | 14 | n/a | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

