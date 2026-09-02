# Factor report — multi-date aggregate

_Generated 2026-09-02 18:56 EDT from 18 scan dates._

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
| 2026-08-31 | 2026-08-28 | 2026-09-01 | 2026-09-02 | — | 11617 |
| 2026-09-01 | 2026-08-31 | 2026-09-02 | — | — | 11620 |

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
| 2026-08-31 | -0.0065 | +0.0398 | — |
| 2026-09-01 | -0.0847 | — | — |
- **1d**: mean IC **-0.0194**, ICIR -0.24, sign consistency 67% over 18 dates
- **2d**: mean IC **-0.0191**, ICIR -0.26, sign consistency 47% over 17 dates
- **3d**: mean IC **-0.0175**, ICIR -0.19, sign consistency 56% over 16 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -22063042185692344.00 | 100% | 18 | -6.37% | ✅ consistent |
| short_fwd_2d | -0.6103 | -7.88 | 100% | 17 | -5.14% | ✅ consistent |
| short_fwd_3d | -0.4866 | -4.15 | 100% | 16 | -4.28% | ✅ consistent |
| d_Performance (Week) | -0.0695 | -0.74 | 71% | 17 | -0.83% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0658 | -0.65 | 65% | 17 | -0.80% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0631 | -0.60 | 59% | 17 | -0.81% | ⚠️ flips / too few dates |
| true_ret | -0.0608 | -0.60 | 59% | 17 | -0.92% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0592 | -0.51 | 59% | 17 | -1.16% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0585 | -0.57 | 59% | 17 | -1.00% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0574 | -0.61 | 59% | 17 | -0.53% | ⚠️ flips / too few dates |
| Volatility (Month) | -0.0567 | -0.43 | 53% | 17 | +0.66% | ⚠️ flips / too few dates |
| Beta | -0.0536 | -0.30 | 59% | 17 | -1.70% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0482 | -0.51 | 76% | 17 | -1.22% | ✅ consistent |
| d_Price | -0.0465 | -0.45 | 59% | 17 | -0.92% | ⚠️ flips / too few dates |
| Forward P/E | -0.0456 | -0.51 | 67% | 18 | n/a | ✅ consistent |
| d_Market Cap | -0.0425 | -0.57 | 76% | 17 | -1.02% | ✅ consistent |
| d_Forward P/E | -0.0400 | -0.36 | 71% | 17 | -0.22% | ✅ consistent |
| Profit Margin | +0.0392 | +0.40 | 67% | 18 | -3.04% | ✅ consistent |
| n_pos | -0.0346 | -0.42 | 61% | 18 | n/a | ⚠️ flips / too few dates |
| exit_price_1d | +0.0345 | +0.60 | 67% | 18 | n/a | ✅ consistent |
| Gross Margin | +0.0330 | +0.50 | 61% | 18 | -0.96% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0319 | +0.55 | 65% | 17 | n/a | ⚠️ flips / too few dates |
| exit_price_3d | +0.0298 | +0.50 | 62% | 16 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0296 | -0.21 | 61% | 18 | -1.82% | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0286 | +0.55 | 69% | 16 | +1.02% | ✅ consistent |
| Market Cap | +0.0264 | +0.58 | 72% | 18 | n/a | ✅ consistent |
| Average Volume | -0.0245 | -0.37 | 61% | 18 | n/a | ⚠️ flips / too few dates |
| price_score | -0.0241 | -0.26 | 65% | 17 | -1.18% | ⚠️ flips / too few dates |
| w_pos | -0.0240 | -0.27 | 56% | 18 | n/a | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0197 | +0.36 | 78% | 18 | n/a | ✅ consistent |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16608454792955988.00 | 100% | 17 | -10.00% | ✅ consistent |
| short_fwd_3d | -0.7210 | -8.38 | 100% | 16 | -8.55% | ✅ consistent |
| short_fwd_1d | -0.6103 | -7.88 | 100% | 17 | -5.86% | ✅ consistent |
| Beta | -0.0812 | -0.53 | 75% | 16 | -3.61% | ✅ consistent |
| Volatility (Month) | -0.0799 | -0.71 | 75% | 16 | +1.24% | ✅ consistent |
| Forward P/E | -0.0611 | -0.74 | 71% | 17 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0564 | -0.47 | 75% | 16 | -1.38% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0536 | -0.53 | 75% | 16 | -2.32% | ✅ consistent |
| Profit Margin | +0.0531 | +0.70 | 76% | 17 | -5.75% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0490 | -0.37 | 62% | 16 | -1.61% | ⚠️ flips / too few dates |
| Gross Margin | +0.0475 | +0.72 | 71% | 17 | -1.88% | ✅ consistent |
| d_Forward P/E | -0.0463 | -0.36 | 62% | 16 | -0.37% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0459 | -0.34 | 56% | 16 | -0.43% | ⚠️ flips / too few dates |
| true_ret | -0.0453 | -0.36 | 62% | 16 | -1.75% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0445 | -0.35 | 69% | 16 | -2.07% | ✅ consistent |
| exit_price_2d | +0.0425 | +0.79 | 82% | 17 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0422 | -0.35 | 62% | 16 | -1.01% | ⚠️ flips / too few dates |
| n_pos | -0.0416 | -0.44 | 65% | 17 | n/a | ⚠️ flips / too few dates |
| d_Market Cap | -0.0413 | -0.48 | 69% | 16 | -2.88% | ✅ consistent |
| d_Price | -0.0408 | -0.32 | 62% | 16 | -1.75% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0399 | +0.74 | 75% | 16 | n/a | ✅ consistent |
| d_Volatility (Month) | +0.0367 | +0.66 | 73% | 15 | +1.79% | ✅ consistent |
| Average Volume | -0.0355 | -0.62 | 71% | 17 | n/a | ✅ consistent |
| w_pos | -0.0345 | -0.40 | 59% | 17 | n/a | ⚠️ flips / too few dates |
| exit_price_1d | +0.0312 | +0.57 | 71% | 17 | n/a | ✅ consistent |
| Short Float | -0.0307 | -0.34 | 53% | 17 | n/a | ⚠️ flips / too few dates |
| valuation_score | -0.0297 | -0.42 | 59% | 17 | +2.12% | ⚠️ flips / too few dates |
| Market Cap | +0.0294 | +0.70 | 71% | 17 | n/a | ✅ consistent |
| 50-Day Simple Moving Average | +0.0239 | +0.26 | 59% | 17 | -3.50% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0223 | +0.25 | 59% | 17 | -3.93% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -13617605278429132.00 | 100% | 16 | -12.38% | ✅ consistent |
| short_fwd_2d | -0.7210 | -8.38 | 100% | 16 | -8.99% | ✅ consistent |
| short_fwd_1d | -0.4866 | -4.15 | 100% | 16 | -4.61% | ✅ consistent |
| Volatility (Month) | -0.0963 | -0.85 | 67% | 15 | +2.17% | ✅ consistent |
| Beta | -0.0922 | -0.59 | 60% | 15 | -5.76% | ⚠️ flips / too few dates |
| Forward P/E | -0.0693 | -0.90 | 69% | 16 | n/a | ✅ consistent |
| Profit Margin | +0.0601 | +0.85 | 81% | 16 | -7.84% | ✅ consistent |
| Gross Margin | +0.0558 | +1.11 | 88% | 16 | -2.28% | ✅ consistent |
| exit_price_3d | +0.0453 | +0.86 | 81% | 16 | n/a | ✅ consistent |
| Average Volume | -0.0433 | -0.82 | 69% | 16 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0430 | -0.34 | 73% | 15 | +0.06% | ✅ consistent |
| Short Float | -0.0379 | -0.43 | 69% | 16 | n/a | ✅ consistent |
| valuation_score | -0.0371 | -0.55 | 69% | 16 | +2.92% | ✅ consistent |
| exit_price_2d | +0.0358 | +0.67 | 81% | 16 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0357 | -0.30 | 60% | 15 | -1.20% | ⚠️ flips / too few dates |
| w_pos | -0.0356 | -0.38 | 56% | 16 | n/a | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0355 | -0.38 | 80% | 15 | -1.26% | ✅ consistent |
| n_pos | -0.0348 | -0.35 | 56% | 16 | n/a | ⚠️ flips / too few dates |
| Market Cap | +0.0291 | +0.84 | 81% | 16 | n/a | ✅ consistent |
| d_Forward P/E | -0.0289 | -0.26 | 67% | 15 | -0.34% | ✅ consistent |
| d_Volatility (Month) | +0.0274 | +0.52 | 64% | 14 | +2.34% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0273 | -0.36 | 67% | 15 | -3.12% | ✅ consistent |
| exit_price_1d | +0.0268 | +0.49 | 69% | 16 | n/a | ✅ consistent |
| Relative Strength Index (14) | +0.0259 | +0.32 | 56% | 16 | n/a | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0257 | -0.21 | 53% | 15 | -1.41% | ⚠️ flips / too few dates |
| price_score | -0.0245 | -0.27 | 60% | 15 | -2.34% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0244 | +0.34 | 44% | 16 | -4.48% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0241 | -0.25 | 60% | 15 | -2.04% | ⚠️ flips / too few dates |
| true_ret | -0.0241 | -0.20 | 60% | 15 | -1.82% | ⚠️ flips / too few dates |
| n_catalysts | -0.0238 | -0.49 | 69% | 16 | n/a | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

