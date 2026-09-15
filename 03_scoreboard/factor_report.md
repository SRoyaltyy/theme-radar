# Factor report — multi-date aggregate

_Generated 2026-09-15 19:21 EDT from 26 scan dates._

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
| 2026-09-09 | 2026-09-08 | 2026-09-10 | 2026-09-11 | 2026-09-14 | 11599 |
| 2026-09-10 | 2026-09-09 | 2026-09-11 | 2026-09-14 | 2026-09-15 | 11616 |
| 2026-09-11 | 2026-09-10 | 2026-09-14 | 2026-09-15 | — | 11598 |
| 2026-09-14 | 2026-09-11 | 2026-09-15 | — | — | 11604 |

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
| 2026-09-09 | -0.0163 | +0.0188 | -0.0591 |
| 2026-09-10 | -0.0932 | +0.1308 | +0.1827 |
| 2026-09-11 | -0.0419 | -0.0676 | — |
| 2026-09-14 | -0.0250 | — | — |
- **1d**: mean IC **-0.0304**, ICIR -0.42, sign consistency 77% over 26 dates
- **2d**: mean IC **-0.0347**, ICIR -0.40, sign consistency 56% over 25 dates
- **3d**: mean IC **-0.0332**, ICIR -0.30, sign consistency 62% over 24 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -18749980439011012.00 | 100% | 26 | -6.29% | ✅ consistent |
| short_fwd_2d | -0.6144 | -7.34 | 100% | 25 | -5.23% | ✅ consistent |
| short_fwd_3d | -0.4826 | -4.15 | 100% | 24 | -4.46% | ✅ consistent |
| Volatility (Month) | -0.0716 | -0.56 | 60% | 25 | +0.41% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0688 | -0.70 | 71% | 24 | -0.75% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0591 | -0.56 | 62% | 24 | -0.73% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0585 | -0.54 | 58% | 24 | -0.71% | ⚠️ flips / too few dates |
| Beta | -0.0581 | -0.30 | 60% | 25 | -1.38% | ⚠️ flips / too few dates |
| true_ret | -0.0546 | -0.52 | 58% | 24 | -0.83% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0546 | -0.51 | 58% | 24 | -0.87% | ⚠️ flips / too few dates |
| Profit Margin | +0.0545 | +0.56 | 69% | 26 | -2.76% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0522 | -0.52 | 58% | 24 | -0.57% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0498 | -0.54 | 71% | 24 | -1.05% | ✅ consistent |
| exit_price_1d | +0.0475 | +0.71 | 69% | 26 | n/a | ✅ consistent |
| n_pos | -0.0474 | -0.64 | 69% | 26 | n/a | ✅ consistent |
| d_Price | -0.0451 | -0.41 | 58% | 24 | -0.83% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0444 | -0.44 | 71% | 24 | -0.25% | ✅ consistent |
| exit_price_3d | +0.0437 | +0.66 | 67% | 24 | n/a | ✅ consistent |
| exit_price_2d | +0.0429 | +0.66 | 68% | 25 | n/a | ✅ consistent |
| d_Market Cap | -0.0392 | -0.59 | 71% | 24 | -0.90% | ✅ consistent |
| w_pos | -0.0384 | -0.49 | 69% | 26 | n/a | ✅ consistent |
| upside_pct | -0.0360 | -0.29 | 65% | 26 | +1.06% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0360 | -0.29 | 65% | 26 | +1.05% | ⚠️ flips / too few dates |
| Market Cap | +0.0355 | +0.60 | 69% | 26 | n/a | ✅ consistent |
| Forward P/E | -0.0353 | -0.39 | 69% | 26 | n/a | ✅ consistent |
| Average Volume | -0.0338 | -0.53 | 65% | 26 | n/a | ⚠️ flips / too few dates |
| valuation_score | -0.0323 | -0.34 | 65% | 26 | +1.12% | ⚠️ flips / too few dates |
| Price | +0.0313 | +0.46 | 62% | 26 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0313 | +0.46 | 62% | 26 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0312 | -0.22 | 58% | 26 | -1.42% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -15922629181314432.00 | 100% | 25 | -9.91% | ✅ consistent |
| short_fwd_3d | -0.7229 | -9.13 | 100% | 24 | -8.69% | ✅ consistent |
| short_fwd_1d | -0.6144 | -7.34 | 100% | 25 | -5.74% | ✅ consistent |
| Volatility (Month) | -0.0882 | -0.71 | 75% | 24 | +0.91% | ✅ consistent |
| Beta | -0.0713 | -0.39 | 71% | 24 | -2.80% | ✅ consistent |
| Profit Margin | +0.0684 | +0.87 | 80% | 25 | -5.32% | ✅ consistent |
| exit_price_2d | +0.0591 | +0.99 | 84% | 25 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0577 | -0.44 | 70% | 23 | -1.31% | ✅ consistent |
| exit_price_3d | +0.0561 | +0.94 | 79% | 24 | n/a | ✅ consistent |
| Forward P/E | -0.0552 | -0.65 | 72% | 25 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0540 | -0.39 | 61% | 23 | -1.46% | ⚠️ flips / too few dates |
| n_pos | -0.0510 | -0.59 | 72% | 25 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0499 | -0.49 | 70% | 23 | -2.00% | ✅ consistent |
| d_Performance (YTD) | -0.0480 | -0.36 | 65% | 23 | -1.80% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0478 | +0.79 | 76% | 25 | n/a | ✅ consistent |
| true_ret | -0.0477 | -0.36 | 57% | 23 | -1.63% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0472 | -0.36 | 57% | 23 | -0.61% | ⚠️ flips / too few dates |
| w_pos | -0.0471 | -0.59 | 68% | 25 | n/a | ✅ consistent |
| d_Price | -0.0470 | -0.36 | 61% | 23 | -1.63% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0457 | -0.35 | 57% | 23 | -1.08% | ⚠️ flips / too few dates |
| upside_pct | -0.0448 | -0.39 | 56% | 25 | +1.98% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0448 | -0.39 | 56% | 25 | +1.98% | ⚠️ flips / too few dates |
| Average Volume | -0.0431 | -0.73 | 76% | 25 | n/a | ✅ consistent |
| Market Cap | +0.0422 | +0.74 | 72% | 25 | n/a | ✅ consistent |
| d_Market Cap | -0.0414 | -0.50 | 70% | 23 | -2.56% | ✅ consistent |
| d_Forward P/E | -0.0411 | -0.34 | 65% | 23 | -0.34% | ⚠️ flips / too few dates |
| valuation_score | -0.0393 | -0.50 | 60% | 25 | +2.10% | ⚠️ flips / too few dates |
| Gross Margin | +0.0365 | +0.48 | 68% | 25 | -2.04% | ✅ consistent |
| Price | +0.0361 | +0.59 | 72% | 25 | n/a | ✅ consistent |
| entry_price | +0.0361 | +0.59 | 72% | 25 | n/a | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -15600926743107926.00 | 100% | 24 | -12.47% | ✅ consistent |
| short_fwd_2d | -0.7229 | -9.13 | 100% | 24 | -8.80% | ✅ consistent |
| short_fwd_1d | -0.4826 | -4.15 | 100% | 24 | -4.86% | ✅ consistent |
| Volatility (Month) | -0.1051 | -0.85 | 74% | 23 | +2.17% | ✅ consistent |
| Beta | -0.0820 | -0.47 | 61% | 23 | -4.20% | ⚠️ flips / too few dates |
| Profit Margin | +0.0804 | +1.09 | 88% | 24 | -6.91% | ✅ consistent |
| exit_price_3d | +0.0670 | +1.10 | 88% | 24 | n/a | ✅ consistent |
| Forward P/E | -0.0658 | -0.78 | 67% | 24 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0621 | -0.44 | 77% | 22 | -0.34% | ✅ consistent |
| exit_price_2d | +0.0575 | +0.93 | 88% | 24 | n/a | ✅ consistent |
| Average Volume | -0.0527 | -0.91 | 75% | 24 | n/a | ✅ consistent |
| upside_pct | -0.0514 | -0.47 | 71% | 24 | +2.66% | ✅ consistent |
| upside_pct_lvl | -0.0514 | -0.47 | 71% | 24 | +2.66% | ✅ consistent |
| w_pos | -0.0503 | -0.53 | 67% | 24 | n/a | ✅ consistent |
| valuation_score | -0.0491 | -0.63 | 75% | 24 | +2.83% | ✅ consistent |
| exit_price_1d | +0.0485 | +0.77 | 79% | 24 | n/a | ✅ consistent |
| n_pos | -0.0470 | -0.48 | 62% | 24 | n/a | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0464 | -0.36 | 77% | 22 | -1.31% | ✅ consistent |
| Short Float | -0.0460 | -0.44 | 62% | 24 | n/a | ⚠️ flips / too few dates |
| Market Cap | +0.0445 | +0.81 | 79% | 24 | n/a | ✅ consistent |
| Performance (YTD) | +0.0426 | +0.42 | 71% | 24 | -4.69% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0411 | +0.44 | 67% | 24 | -4.65% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0400 | -0.30 | 68% | 22 | -1.00% | ✅ consistent |
| Price | +0.0389 | +0.61 | 71% | 24 | n/a | ✅ consistent |
| entry_price | +0.0389 | +0.61 | 71% | 24 | n/a | ✅ consistent |
| Gross Margin | +0.0376 | +0.55 | 75% | 24 | -2.15% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0364 | -0.26 | 64% | 22 | -1.16% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0362 | -0.45 | 73% | 22 | -2.48% | ✅ consistent |
| price_score | -0.0332 | -0.27 | 64% | 22 | -2.27% | ⚠️ flips / too few dates |
| total_score | -0.0332 | -0.30 | 62% | 24 | -1.21% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

