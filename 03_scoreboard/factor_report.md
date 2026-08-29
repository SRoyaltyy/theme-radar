# Factor report — multi-date aggregate

_Generated 2026-08-28 22:58 EDT from 15 scan dates._

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
| 2026-08-26 | 2026-08-25 | 2026-08-28 | — | — | 11620 |

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
| 2026-08-25 | -0.0503 | -0.1093 | — |
| 2026-08-26 | -0.0710 | — | — |
- **1d**: mean IC **-0.0143**, ICIR -0.16, sign consistency 60% over 15 dates
- **2d**: mean IC **-0.0269**, ICIR -0.35, sign consistency 50% over 14 dates
- **3d**: mean IC **-0.0171**, ICIR -0.17, sign consistency 54% over 13 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -20140709820486304.00 | 100% | 15 | -5.86% | ✅ consistent |
| short_fwd_2d | -0.5981 | -8.76 | 100% | 14 | -4.37% | ✅ consistent |
| short_fwd_3d | -0.4824 | -4.18 | 100% | 13 | -4.01% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0774 | -0.78 | 71% | 14 | -0.88% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0753 | -0.74 | 64% | 14 | -0.91% | ⚠️ flips / too few dates |
| true_ret | -0.0745 | -0.76 | 64% | 14 | -0.93% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0709 | -0.61 | 64% | 14 | -0.97% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0709 | -0.71 | 64% | 14 | -0.82% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0683 | -0.71 | 64% | 14 | -0.59% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0627 | -0.63 | 64% | 14 | -0.74% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0605 | -0.55 | 79% | 14 | -0.28% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0587 | -0.59 | 79% | 14 | -1.09% | ✅ consistent |
| d_Price | -0.0582 | -0.57 | 64% | 14 | -0.93% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0527 | -0.75 | 86% | 14 | -1.12% | ✅ consistent |
| Volatility (Month) | -0.0509 | -0.41 | 50% | 14 | +0.66% | ⚠️ flips / too few dates |
| Beta | -0.0403 | -0.25 | 57% | 14 | -1.06% | ⚠️ flips / too few dates |
| n_pos | -0.0376 | -0.44 | 60% | 15 | n/a | ⚠️ flips / too few dates |
| Gross Margin | +0.0371 | +0.52 | 60% | 15 | +0.26% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0356 | +0.60 | 67% | 15 | n/a | ✅ consistent |
| Profit Margin | +0.0346 | +0.34 | 67% | 15 | -3.41% | ✅ consistent |
| exit_price_2d | +0.0326 | +0.54 | 64% | 14 | n/a | ⚠️ flips / too few dates |
| Forward P/E | -0.0311 | -0.38 | 60% | 15 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0303 | -0.21 | 67% | 15 | -1.74% | ✅ consistent |
| 20-Day Simple Moving Average | -0.0268 | -0.26 | 60% | 15 | -1.83% | ⚠️ flips / too few dates |
| Market Cap | +0.0253 | +0.57 | 73% | 15 | n/a | ✅ consistent |
| exit_price_3d | +0.0234 | +0.44 | 62% | 13 | n/a | ⚠️ flips / too few dates |
| Average Volume | -0.0229 | -0.36 | 60% | 15 | n/a | ⚠️ flips / too few dates |
| w_pos | -0.0213 | -0.23 | 53% | 15 | n/a | ⚠️ flips / too few dates |
| technical_score | -0.0207 | -0.29 | 67% | 15 | -2.88% | ✅ consistent |
| d_Volatility (Month) | +0.0192 | +0.51 | 69% | 13 | +0.49% | ✅ consistent |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -19457774262956300.00 | 100% | 14 | -8.75% | ✅ consistent |
| short_fwd_3d | -0.7043 | -8.14 | 100% | 13 | -7.55% | ✅ consistent |
| short_fwd_1d | -0.5981 | -8.76 | 100% | 14 | -5.22% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0713 | -0.57 | 77% | 13 | -1.51% | ✅ consistent |
| d_Forward P/E | -0.0673 | -0.51 | 69% | 13 | -0.47% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0656 | -0.48 | 69% | 13 | -1.75% | ✅ consistent |
| true_ret | -0.0641 | -0.49 | 69% | 13 | -1.69% | ✅ consistent |
| d_Performance (YTD) | -0.0622 | -0.47 | 77% | 13 | -1.89% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0621 | -0.57 | 77% | 13 | -2.20% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0583 | -0.46 | 62% | 13 | -1.20% | ⚠️ flips / too few dates |
| d_Price | -0.0572 | -0.44 | 69% | 13 | -1.69% | ✅ consistent |
| Volatility (Month) | -0.0527 | -0.51 | 69% | 13 | +1.24% | ✅ consistent |
| d_Market Cap | -0.0525 | -0.58 | 69% | 13 | -3.00% | ✅ consistent |
| d_Performance (Week) | -0.0519 | -0.36 | 62% | 13 | -0.81% | ⚠️ flips / too few dates |
| Gross Margin | +0.0497 | +0.69 | 64% | 14 | +0.54% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0474 | -0.44 | 54% | 13 | -1.27% | ⚠️ flips / too few dates |
| Beta | -0.0452 | -0.32 | 69% | 13 | -2.49% | ✅ consistent |
| exit_price_2d | +0.0428 | +0.73 | 79% | 14 | n/a | ✅ consistent |
| Forward P/E | -0.0400 | -0.57 | 64% | 14 | n/a | ⚠️ flips / too few dates |
| Profit Margin | +0.0395 | +0.52 | 71% | 14 | -6.49% | ✅ consistent |
| n_pos | -0.0393 | -0.39 | 64% | 14 | n/a | ⚠️ flips / too few dates |
| exit_price_3d | +0.0355 | +0.65 | 69% | 13 | n/a | ✅ consistent |
| Market Cap | +0.0320 | +0.83 | 79% | 14 | n/a | ✅ consistent |
| price_score | -0.0318 | -0.40 | 54% | 13 | -2.54% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0312 | +0.53 | 64% | 14 | n/a | ⚠️ flips / too few dates |
| w_pos | -0.0286 | -0.32 | 50% | 14 | n/a | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0269 | -0.31 | 46% | 13 | -1.31% | ⚠️ flips / too few dates |
| total_score | -0.0269 | -0.35 | 50% | 14 | -1.29% | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0249 | +0.54 | 67% | 12 | +0.80% | ✅ consistent |
| Average Volume | -0.0239 | -0.49 | 64% | 14 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -13258238315539808.00 | 100% | 13 | -11.00% | ✅ consistent |
| short_fwd_2d | -0.7043 | -8.14 | 100% | 13 | -8.12% | ✅ consistent |
| short_fwd_1d | -0.4824 | -4.18 | 100% | 13 | -4.67% | ✅ consistent |
| Volatility (Month) | -0.0657 | -0.65 | 58% | 12 | +2.17% | ⚠️ flips / too few dates |
| Gross Margin | +0.0590 | +1.08 | 85% | 13 | +1.52% | ✅ consistent |
| Beta | -0.0582 | -0.38 | 50% | 12 | -3.98% | ⚠️ flips / too few dates |
| Forward P/E | -0.0474 | -0.71 | 62% | 13 | n/a | ⚠️ flips / too few dates |
| Profit Margin | +0.0449 | +0.64 | 77% | 13 | -8.49% | ✅ consistent |
| exit_price_3d | +0.0437 | +0.76 | 77% | 13 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0436 | -0.33 | 75% | 12 | -0.15% | ✅ consistent |
| d_Performance (Month) | -0.0422 | -0.41 | 75% | 12 | -1.37% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0372 | -0.30 | 67% | 12 | -1.27% | ✅ consistent |
| d_Performance (Quarter) | -0.0361 | -0.37 | 58% | 12 | -1.24% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0339 | +0.58 | 77% | 13 | n/a | ✅ consistent |
| Market Cap | +0.0333 | +0.92 | 85% | 13 | n/a | ✅ consistent |
| true_ret | -0.0281 | -0.23 | 67% | 12 | -1.77% | ✅ consistent |
| Average Volume | -0.0281 | -0.69 | 62% | 13 | n/a | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0276 | -0.25 | 67% | 12 | -0.32% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0275 | -0.22 | 58% | 12 | -1.49% | ⚠️ flips / too few dates |
| price_score | -0.0274 | -0.27 | 67% | 12 | -2.41% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0267 | -0.25 | 67% | 12 | -2.01% | ✅ consistent |
| d_Performance (YTD) | -0.0253 | -0.20 | 67% | 12 | -1.71% | ✅ consistent |
| exit_price_1d | +0.0252 | +0.42 | 62% | 13 | n/a | ⚠️ flips / too few dates |
| d_Market Cap | -0.0236 | -0.33 | 75% | 12 | -3.00% | ✅ consistent |
| n_pos | -0.0226 | -0.22 | 54% | 13 | n/a | ⚠️ flips / too few dates |
| w_pos | -0.0224 | -0.23 | 46% | 13 | n/a | ⚠️ flips / too few dates |
| 20-Day Simple Moving Average | -0.0212 | -0.19 | 54% | 13 | -4.71% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0202 | -0.17 | 58% | 12 | -0.58% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0201 | +0.41 | 54% | 13 | -1.62% | ⚠️ flips / too few dates |
| Performance (Month) | -0.0196 | -0.25 | 69% | 13 | -4.43% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

