# Factor report — multi-date aggregate

_Generated 2026-09-01 18:56 EDT from 17 scan dates._

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
| 2026-08-28 | 2026-08-26 | 2026-08-31 | 2026-09-01 | — | 11611 |
| 2026-08-31 | 2026-08-28 | 2026-09-01 | — | — | 11617 |

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
| 2026-08-28 | -0.0442 | +0.0258 | — |
| 2026-08-31 | -0.0065 | — | — |
- **1d**: mean IC **-0.0156**, ICIR -0.19, sign consistency 65% over 17 dates
- **2d**: mean IC **-0.0228**, ICIR -0.31, sign consistency 50% over 16 dates
- **3d**: mean IC **-0.0194**, ICIR -0.21, sign consistency 60% over 15 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -21441422939785764.00 | 100% | 17 | -6.55% | ✅ consistent |
| short_fwd_2d | -0.6062 | -7.77 | 100% | 16 | -4.93% | ✅ consistent |
| short_fwd_3d | -0.4901 | -4.08 | 100% | 15 | -4.03% | ✅ consistent |
| Beta | -0.0672 | -0.38 | 62% | 16 | -1.83% | ⚠️ flips / too few dates |
| Volatility (Month) | -0.0672 | -0.53 | 56% | 16 | +0.66% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0653 | -0.69 | 69% | 16 | -0.86% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0622 | -0.61 | 62% | 16 | -0.85% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0583 | -0.55 | 56% | 16 | -0.85% | ⚠️ flips / too few dates |
| true_ret | -0.0574 | -0.56 | 56% | 16 | -0.98% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0546 | -0.56 | 56% | 16 | -0.56% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0540 | -0.45 | 56% | 16 | -1.23% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0537 | -0.51 | 56% | 16 | -1.06% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0501 | -0.52 | 75% | 16 | -1.29% | ✅ consistent |
| d_Price | -0.0419 | -0.40 | 56% | 16 | -0.98% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0417 | -0.37 | 69% | 16 | -0.22% | ✅ consistent |
| n_pos | -0.0400 | -0.49 | 65% | 17 | n/a | ⚠️ flips / too few dates |
| d_Market Cap | -0.0393 | -0.52 | 75% | 16 | -1.09% | ✅ consistent |
| Profit Margin | +0.0392 | +0.39 | 65% | 17 | -3.22% | ⚠️ flips / too few dates |
| Gross Margin | +0.0346 | +0.51 | 59% | 17 | -1.02% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0345 | +0.59 | 67% | 15 | n/a | ✅ consistent |
| Forward P/E | -0.0343 | -0.43 | 65% | 17 | n/a | ⚠️ flips / too few dates |
| exit_price_1d | +0.0329 | +0.56 | 65% | 17 | n/a | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0327 | +0.64 | 73% | 15 | +1.05% | ✅ consistent |
| Average Volume | -0.0304 | -0.48 | 65% | 17 | n/a | ⚠️ flips / too few dates |
| exit_price_2d | +0.0299 | +0.50 | 62% | 16 | n/a | ⚠️ flips / too few dates |
| w_pos | -0.0287 | -0.32 | 59% | 17 | n/a | ⚠️ flips / too few dates |
| Short Float | -0.0263 | -0.23 | 53% | 17 | n/a | ⚠️ flips / too few dates |
| valuation_score | -0.0253 | -0.30 | 65% | 17 | +1.22% | ⚠️ flips / too few dates |
| Market Cap | +0.0224 | +0.51 | 71% | 17 | n/a | ✅ consistent |
| d_Beta | +0.0218 | +0.26 | 60% | 15 | +0.23% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -18014398509481984.00 | 100% | 16 | -9.97% | ✅ consistent |
| short_fwd_3d | -0.7184 | -8.14 | 100% | 15 | -8.02% | ✅ consistent |
| short_fwd_1d | -0.6062 | -7.77 | 100% | 16 | -5.35% | ✅ consistent |
| Volatility (Month) | -0.0781 | -0.67 | 73% | 15 | +1.24% | ✅ consistent |
| Beta | -0.0736 | -0.47 | 73% | 15 | -3.96% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0549 | -0.44 | 73% | 15 | -1.55% | ✅ consistent |
| d_Forward P/E | -0.0542 | -0.42 | 67% | 15 | -0.39% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0526 | -0.50 | 73% | 15 | -2.29% | ✅ consistent |
| Forward P/E | -0.0507 | -0.69 | 69% | 16 | n/a | ✅ consistent |
| Gross Margin | +0.0483 | +0.72 | 69% | 16 | -2.01% | ✅ consistent |
| Profit Margin | +0.0474 | +0.64 | 75% | 16 | -6.37% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0473 | -0.35 | 60% | 15 | -1.80% | ⚠️ flips / too few dates |
| n_pos | -0.0454 | -0.47 | 69% | 16 | n/a | ✅ consistent |
| true_ret | -0.0452 | -0.34 | 60% | 15 | -1.85% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0439 | -0.33 | 67% | 15 | -2.02% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0425 | -0.34 | 60% | 15 | -1.18% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0420 | -0.47 | 67% | 15 | -3.27% | ✅ consistent |
| exit_price_3d | +0.0412 | +0.74 | 73% | 15 | n/a | ✅ consistent |
| exit_price_2d | +0.0407 | +0.74 | 81% | 16 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0406 | -0.30 | 53% | 15 | -0.45% | ⚠️ flips / too few dates |
| d_Price | -0.0398 | -0.31 | 60% | 15 | -1.85% | ⚠️ flips / too few dates |
| Average Volume | -0.0376 | -0.65 | 69% | 16 | n/a | ✅ consistent |
| w_pos | -0.0365 | -0.42 | 56% | 16 | n/a | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0343 | +0.60 | 71% | 14 | +1.70% | ✅ consistent |
| valuation_score | -0.0335 | -0.47 | 62% | 16 | +2.26% | ⚠️ flips / too few dates |
| Short Float | -0.0326 | -0.35 | 50% | 16 | n/a | ⚠️ flips / too few dates |
| exit_price_1d | +0.0292 | +0.53 | 69% | 16 | n/a | ✅ consistent |
| Market Cap | +0.0256 | +0.64 | 69% | 16 | n/a | ✅ consistent |
| d_Performance (Quarter) | -0.0242 | -0.21 | 47% | 15 | -1.20% | ⚠️ flips / too few dates |
| price_score | -0.0230 | -0.30 | 47% | 15 | -2.83% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -13185189614645562.00 | 100% | 15 | -12.00% | ✅ consistent |
| short_fwd_2d | -0.7184 | -8.14 | 100% | 15 | -7.95% | ✅ consistent |
| short_fwd_1d | -0.4901 | -4.08 | 100% | 15 | -4.36% | ✅ consistent |
| Volatility (Month) | -0.0939 | -0.80 | 64% | 14 | +2.17% | ⚠️ flips / too few dates |
| Beta | -0.0823 | -0.52 | 57% | 14 | -5.20% | ⚠️ flips / too few dates |
| Forward P/E | -0.0600 | -0.85 | 67% | 15 | n/a | ✅ consistent |
| Gross Margin | +0.0587 | +1.16 | 87% | 15 | -1.19% | ✅ consistent |
| Profit Margin | +0.0572 | +0.79 | 80% | 15 | -8.16% | ✅ consistent |
| exit_price_3d | +0.0466 | +0.86 | 80% | 15 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0457 | -0.35 | 71% | 14 | -0.03% | ✅ consistent |
| Average Volume | -0.0434 | -0.79 | 67% | 15 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0407 | -0.33 | 64% | 14 | -0.90% | ⚠️ flips / too few dates |
| valuation_score | -0.0377 | -0.54 | 67% | 15 | +2.97% | ✅ consistent |
| d_Forward P/E | -0.0374 | -0.34 | 71% | 14 | -0.40% | ✅ consistent |
| n_pos | -0.0374 | -0.36 | 60% | 15 | n/a | ⚠️ flips / too few dates |
| exit_price_2d | +0.0369 | +0.67 | 80% | 15 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0369 | -0.39 | 79% | 14 | -0.91% | ✅ consistent |
| w_pos | -0.0365 | -0.37 | 53% | 15 | n/a | ⚠️ flips / too few dates |
| Short Float | -0.0365 | -0.40 | 67% | 15 | n/a | ✅ consistent |
| d_Market Cap | -0.0310 | -0.40 | 71% | 14 | -2.60% | ✅ consistent |
| true_ret | -0.0310 | -0.25 | 64% | 14 | -1.55% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0306 | -0.25 | 57% | 14 | -1.13% | ⚠️ flips / too few dates |
| Market Cap | +0.0288 | +0.80 | 80% | 15 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0285 | -0.23 | 64% | 14 | -1.54% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0280 | +0.49 | 67% | 15 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0270 | -0.27 | 64% | 14 | -1.81% | ⚠️ flips / too few dates |
| price_score | -0.0264 | -0.28 | 64% | 14 | -1.84% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0247 | -0.26 | 57% | 14 | -1.23% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0229 | -0.19 | 57% | 14 | -0.25% | ⚠️ flips / too few dates |
| n_catalysts | -0.0218 | -0.44 | 67% | 15 | n/a | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

