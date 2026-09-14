# Factor report — multi-date aggregate

_Generated 2026-09-14 19:37 EDT from 25 scan dates._

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
| 2026-09-10 | 2026-09-09 | 2026-09-11 | 2026-09-14 | — | 11616 |
| 2026-09-11 | 2026-09-10 | 2026-09-14 | — | — | 11598 |

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
| 2026-09-10 | -0.0932 | +0.1308 | — |
| 2026-09-11 | -0.0419 | — | — |
- **1d**: mean IC **-0.0306**, ICIR -0.42, sign consistency 76% over 25 dates
- **2d**: mean IC **-0.0333**, ICIR -0.38, sign consistency 54% over 24 dates
- **3d**: mean IC **-0.0425**, ICIR -0.41, sign consistency 65% over 23 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -20140709820486304.00 | 100% | 25 | -6.37% | ✅ consistent |
| short_fwd_2d | -0.6120 | -7.24 | 100% | 24 | -5.07% | ✅ consistent |
| short_fwd_3d | -0.4926 | -4.55 | 100% | 23 | -4.49% | ✅ consistent |
| d_Performance (Week) | -0.0701 | -0.70 | 70% | 23 | -0.76% | ✅ consistent |
| Volatility (Month) | -0.0647 | -0.51 | 58% | 24 | +0.72% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0588 | -0.55 | 61% | 23 | -0.73% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0585 | -0.53 | 57% | 23 | -0.72% | ⚠️ flips / too few dates |
| true_ret | -0.0553 | -0.52 | 57% | 23 | -0.84% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0548 | -0.50 | 57% | 23 | -0.88% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0516 | -0.51 | 57% | 23 | -0.58% | ⚠️ flips / too few dates |
| Beta | -0.0492 | -0.26 | 58% | 24 | -1.43% | ⚠️ flips / too few dates |
| Profit Margin | +0.0490 | +0.52 | 68% | 25 | -2.90% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0477 | -0.51 | 70% | 23 | -1.07% | ✅ consistent |
| n_pos | -0.0453 | -0.61 | 68% | 25 | n/a | ✅ consistent |
| d_Price | -0.0443 | -0.39 | 57% | 23 | -0.84% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0440 | +0.67 | 67% | 24 | n/a | ✅ consistent |
| exit_price_1d | +0.0438 | +0.67 | 68% | 25 | n/a | ✅ consistent |
| d_Forward P/E | -0.0421 | -0.41 | 70% | 23 | -0.24% | ✅ consistent |
| Performance (Week) | -0.0411 | -0.31 | 60% | 25 | -1.48% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0390 | -0.57 | 70% | 23 | -0.93% | ✅ consistent |
| exit_price_3d | +0.0380 | +0.62 | 65% | 23 | n/a | ⚠️ flips / too few dates |
| Forward P/E | -0.0365 | -0.40 | 68% | 25 | n/a | ✅ consistent |
| w_pos | -0.0355 | -0.45 | 68% | 25 | n/a | ✅ consistent |
| Market Cap | +0.0329 | +0.56 | 68% | 25 | n/a | ✅ consistent |
| Average Volume | -0.0315 | -0.49 | 64% | 25 | n/a | ⚠️ flips / too few dates |
| total_score | -0.0306 | -0.42 | 76% | 25 | -0.65% | ✅ consistent |
| Price | +0.0275 | +0.41 | 60% | 25 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0275 | +0.41 | 60% | 25 | n/a | ⚠️ flips / too few dates |
| valuation_score | -0.0268 | -0.29 | 64% | 25 | +1.21% | ⚠️ flips / too few dates |
| Gross Margin | +0.0261 | +0.35 | 64% | 25 | -1.17% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -15600926743107926.00 | 100% | 24 | -9.86% | ✅ consistent |
| short_fwd_3d | -0.7237 | -8.96 | 100% | 23 | -8.64% | ✅ consistent |
| short_fwd_1d | -0.6120 | -7.24 | 100% | 24 | -5.67% | ✅ consistent |
| Volatility (Month) | -0.0823 | -0.67 | 74% | 23 | +1.24% | ✅ consistent |
| Profit Margin | +0.0646 | +0.82 | 79% | 24 | -5.32% | ✅ consistent |
| Beta | -0.0615 | -0.34 | 70% | 23 | -2.83% | ✅ consistent |
| exit_price_2d | +0.0570 | +0.95 | 83% | 24 | n/a | ✅ consistent |
| Forward P/E | -0.0554 | -0.63 | 71% | 24 | n/a | ✅ consistent |
| exit_price_3d | +0.0531 | +0.90 | 78% | 23 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0498 | -0.39 | 68% | 22 | -1.24% | ✅ consistent |
| d_Performance (Week) | -0.0488 | -0.36 | 55% | 22 | -0.57% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0474 | -0.35 | 59% | 22 | -1.42% | ⚠️ flips / too few dates |
| n_pos | -0.0471 | -0.54 | 71% | 24 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0468 | -0.45 | 68% | 22 | -1.97% | ✅ consistent |
| exit_price_1d | +0.0456 | +0.75 | 75% | 24 | n/a | ✅ consistent |
| Average Volume | -0.0432 | -0.72 | 75% | 24 | n/a | ✅ consistent |
| w_pos | -0.0430 | -0.54 | 67% | 24 | n/a | ✅ consistent |
| d_Market Cap | -0.0419 | -0.49 | 68% | 22 | -2.58% | ✅ consistent |
| d_Price | -0.0417 | -0.32 | 59% | 22 | -1.58% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0417 | -0.31 | 64% | 22 | -1.77% | ⚠️ flips / too few dates |
| true_ret | -0.0410 | -0.31 | 55% | 22 | -1.58% | ⚠️ flips / too few dates |
| Market Cap | +0.0393 | +0.70 | 71% | 24 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0378 | -0.30 | 55% | 22 | -0.99% | ⚠️ flips / too few dates |
| valuation_score | -0.0373 | -0.47 | 58% | 24 | +2.14% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0362 | -0.30 | 64% | 22 | -0.32% | ⚠️ flips / too few dates |
| upside_pct | -0.0349 | -0.33 | 54% | 24 | +2.01% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0349 | -0.33 | 54% | 24 | +2.00% | ⚠️ flips / too few dates |
| Short Float | -0.0348 | -0.32 | 54% | 24 | n/a | ⚠️ flips / too few dates |
| Price | +0.0341 | +0.55 | 71% | 24 | n/a | ✅ consistent |
| entry_price | +0.0341 | +0.55 | 71% | 24 | n/a | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -15272449392353350.00 | 100% | 23 | -12.50% | ✅ consistent |
| short_fwd_2d | -0.7237 | -8.96 | 100% | 23 | -8.82% | ✅ consistent |
| short_fwd_1d | -0.4926 | -4.55 | 100% | 23 | -4.98% | ✅ consistent |
| Volatility (Month) | -0.1003 | -0.81 | 73% | 22 | +2.17% | ✅ consistent |
| Beta | -0.0787 | -0.45 | 59% | 22 | -4.21% | ⚠️ flips / too few dates |
| Profit Margin | +0.0773 | +1.05 | 87% | 23 | -6.80% | ✅ consistent |
| d_Performance (Week) | -0.0761 | -0.59 | 81% | 21 | -0.47% | ✅ consistent |
| Forward P/E | -0.0675 | -0.79 | 65% | 23 | n/a | ⚠️ flips / too few dates |
| exit_price_3d | +0.0616 | +1.09 | 87% | 23 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0608 | -0.54 | 81% | 21 | -1.43% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0537 | -0.45 | 71% | 21 | -1.15% | ✅ consistent |
| Average Volume | -0.0524 | -0.89 | 74% | 23 | n/a | ✅ consistent |
| exit_price_2d | +0.0521 | +0.91 | 87% | 23 | n/a | ✅ consistent |
| w_pos | -0.0514 | -0.53 | 65% | 23 | n/a | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0507 | -0.40 | 67% | 21 | -1.33% | ✅ consistent |
| n_pos | -0.0494 | -0.50 | 65% | 23 | n/a | ⚠️ flips / too few dates |
| Short Float | -0.0481 | -0.46 | 65% | 23 | n/a | ⚠️ flips / too few dates |
| valuation_score | -0.0472 | -0.60 | 74% | 23 | +2.81% | ✅ consistent |
| price_score | -0.0468 | -0.43 | 67% | 21 | -2.50% | ✅ consistent |
| d_Performance (YTD) | -0.0451 | -0.36 | 71% | 21 | -1.85% | ✅ consistent |
| true_ret | -0.0445 | -0.36 | 71% | 21 | -1.73% | ✅ consistent |
| exit_price_1d | +0.0432 | +0.74 | 78% | 23 | n/a | ✅ consistent |
| d_Market Cap | -0.0431 | -0.57 | 76% | 21 | -2.65% | ✅ consistent |
| total_score | -0.0425 | -0.41 | 65% | 23 | -1.32% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0416 | -0.36 | 67% | 21 | -0.71% | ✅ consistent |
| upside_pct | -0.0411 | -0.42 | 70% | 23 | +2.63% | ✅ consistent |
| upside_pct_lvl | -0.0410 | -0.42 | 70% | 23 | +2.63% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0401 | -0.46 | 71% | 21 | -2.03% | ✅ consistent |
| Market Cap | +0.0392 | +0.79 | 78% | 23 | n/a | ✅ consistent |
| Performance (YTD) | +0.0391 | +0.38 | 70% | 23 | -4.74% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

