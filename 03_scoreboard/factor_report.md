# Factor report — multi-date aggregate

_Generated 2026-09-17 19:19 EDT from 28 scan dates._

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
| 2026-09-11 | 2026-09-10 | 2026-09-14 | 2026-09-15 | 2026-09-16 | 11598 |
| 2026-09-14 | 2026-09-11 | 2026-09-15 | 2026-09-16 | 2026-09-17 | 11604 |
| 2026-09-15 | 2026-09-14 | 2026-09-16 | 2026-09-17 | — | 11621 |
| 2026-09-16 | 2026-09-15 | 2026-09-17 | — | — | 11627 |

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
| 2026-09-11 | -0.0419 | -0.0676 | -0.1072 |
| 2026-09-14 | -0.0250 | -0.1114 | -0.2010 |
| 2026-09-15 | -0.0616 | -0.1290 | — |
| 2026-09-16 | -0.0722 | — | — |
- **1d**: mean IC **-0.0330**, ICIR -0.47, sign consistency 79% over 28 dates
- **2d**: mean IC **-0.0410**, ICIR -0.48, sign consistency 59% over 27 dates
- **3d**: mean IC **-0.0425**, ICIR -0.38, sign consistency 65% over 26 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -19457774262956300.00 | 100% | 28 | -6.16% | ✅ consistent |
| short_fwd_2d | -0.6144 | -7.56 | 100% | 27 | -5.07% | ✅ consistent |
| short_fwd_3d | -0.4835 | -4.25 | 100% | 26 | -4.58% | ✅ consistent |
| d_Performance (Week) | -0.0671 | -0.68 | 69% | 26 | -0.73% | ✅ consistent |
| Volatility (Month) | -0.0641 | -0.49 | 59% | 27 | +0.54% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0535 | -0.51 | 54% | 26 | -0.60% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0531 | -0.52 | 58% | 26 | -0.61% | ⚠️ flips / too few dates |
| n_pos | -0.0502 | -0.69 | 71% | 28 | n/a | ✅ consistent |
| true_ret | -0.0500 | -0.49 | 54% | 26 | -0.73% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0498 | -0.48 | 58% | 26 | -0.74% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0463 | -0.47 | 54% | 26 | -0.47% | ⚠️ flips / too few dates |
| Beta | -0.0461 | -0.24 | 59% | 27 | -1.32% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0461 | +0.70 | 69% | 26 | n/a | ✅ consistent |
| Profit Margin | +0.0461 | +0.46 | 68% | 28 | -2.67% | ✅ consistent |
| exit_price_2d | +0.0459 | +0.71 | 70% | 27 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0442 | -0.49 | 69% | 26 | -0.90% | ✅ consistent |
| exit_price_1d | +0.0435 | +0.65 | 68% | 28 | n/a | ✅ consistent |
| Performance (Week) | -0.0429 | -0.30 | 61% | 28 | -1.36% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0418 | -0.42 | 69% | 26 | -0.24% | ✅ consistent |
| w_pos | -0.0410 | -0.53 | 71% | 28 | n/a | ✅ consistent |
| d_Price | -0.0401 | -0.37 | 58% | 26 | -0.73% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0357 | -0.54 | 69% | 26 | -0.74% | ✅ consistent |
| Average Volume | -0.0342 | -0.55 | 68% | 28 | n/a | ✅ consistent |
| valuation_score | -0.0335 | -0.37 | 68% | 28 | +1.08% | ✅ consistent |
| total_score | -0.0330 | -0.47 | 79% | 28 | -0.54% | ✅ consistent |
| Market Cap | +0.0311 | +0.51 | 68% | 28 | n/a | ✅ consistent |
| Performance (YTD) | +0.0286 | +0.30 | 61% | 28 | -1.78% | ⚠️ flips / too few dates |
| Price | +0.0274 | +0.40 | 61% | 28 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0274 | +0.40 | 61% | 28 | n/a | ⚠️ flips / too few dates |
| upside_pct | -0.0269 | -0.21 | 61% | 28 | +1.02% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16547281639269260.00 | 100% | 27 | -9.67% | ✅ consistent |
| short_fwd_3d | -0.7246 | -9.28 | 100% | 26 | -8.64% | ✅ consistent |
| short_fwd_1d | -0.6144 | -7.56 | 100% | 27 | -5.66% | ✅ consistent |
| Volatility (Month) | -0.0890 | -0.70 | 73% | 26 | +0.73% | ✅ consistent |
| Beta | -0.0679 | -0.37 | 69% | 26 | -2.66% | ✅ consistent |
| Profit Margin | +0.0651 | +0.77 | 78% | 27 | -5.06% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0616 | -0.49 | 72% | 25 | -1.30% | ✅ consistent |
| exit_price_3d | +0.0610 | +1.02 | 81% | 26 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0593 | -0.44 | 64% | 25 | -1.44% | ⚠️ flips / too few dates |
| n_pos | -0.0592 | -0.67 | 74% | 27 | n/a | ✅ consistent |
| exit_price_2d | +0.0592 | +0.97 | 81% | 27 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0579 | -0.44 | 60% | 25 | -0.68% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0552 | -0.55 | 72% | 25 | -1.94% | ✅ consistent |
| w_pos | -0.0543 | -0.66 | 70% | 27 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0536 | -0.41 | 68% | 25 | -1.75% | ✅ consistent |
| true_ret | -0.0530 | -0.41 | 60% | 25 | -1.60% | ⚠️ flips / too few dates |
| d_Price | -0.0525 | -0.41 | 64% | 25 | -1.60% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0499 | -0.40 | 60% | 25 | -1.08% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0479 | +0.78 | 74% | 27 | n/a | ✅ consistent |
| Average Volume | -0.0463 | -0.79 | 78% | 27 | n/a | ✅ consistent |
| valuation_score | -0.0452 | -0.56 | 63% | 27 | +1.98% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0446 | -0.38 | 68% | 25 | -0.35% | ✅ consistent |
| upside_pct | -0.0436 | -0.36 | 56% | 27 | +1.86% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0436 | -0.36 | 56% | 27 | +1.85% | ⚠️ flips / too few dates |
| Forward P/E | -0.0432 | -0.47 | 67% | 27 | n/a | ✅ consistent |
| d_Market Cap | -0.0416 | -0.52 | 72% | 25 | -2.49% | ✅ consistent |
| total_score | -0.0410 | -0.48 | 59% | 27 | -1.18% | ⚠️ flips / too few dates |
| Market Cap | +0.0404 | +0.69 | 70% | 27 | n/a | ✅ consistent |
| Short Float | -0.0377 | -0.36 | 59% | 27 | n/a | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0374 | +0.41 | 67% | 27 | -3.32% | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -16237959380644838.00 | 100% | 26 | -12.33% | ✅ consistent |
| short_fwd_2d | -0.7246 | -9.28 | 100% | 26 | -8.75% | ✅ consistent |
| short_fwd_1d | -0.4835 | -4.25 | 100% | 26 | -4.86% | ✅ consistent |
| Volatility (Month) | -0.1117 | -0.91 | 76% | 25 | +1.36% | ✅ consistent |
| Beta | -0.0878 | -0.51 | 64% | 25 | -4.02% | ⚠️ flips / too few dates |
| Profit Margin | +0.0807 | +1.12 | 88% | 26 | -6.67% | ✅ consistent |
| exit_price_3d | +0.0694 | +1.17 | 88% | 26 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0674 | -0.48 | 79% | 24 | -0.38% | ✅ consistent |
| w_pos | -0.0602 | -0.62 | 69% | 26 | n/a | ✅ consistent |
| exit_price_2d | +0.0601 | +1.00 | 88% | 26 | n/a | ✅ consistent |
| upside_pct | -0.0583 | -0.53 | 73% | 26 | +2.52% | ✅ consistent |
| upside_pct_lvl | -0.0583 | -0.53 | 73% | 26 | +2.52% | ✅ consistent |
| n_pos | -0.0580 | -0.57 | 65% | 26 | n/a | ⚠️ flips / too few dates |
| Forward P/E | -0.0564 | -0.64 | 62% | 26 | n/a | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0560 | -0.41 | 71% | 24 | -1.04% | ✅ consistent |
| Average Volume | -0.0558 | -0.99 | 77% | 26 | n/a | ✅ consistent |
| valuation_score | -0.0558 | -0.71 | 77% | 26 | +2.68% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0522 | -0.36 | 67% | 24 | -1.16% | ✅ consistent |
| exit_price_1d | +0.0511 | +0.84 | 81% | 26 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0494 | -0.40 | 79% | 24 | -1.16% | ✅ consistent |
| Short Float | -0.0490 | -0.49 | 65% | 26 | n/a | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0463 | -0.32 | 71% | 24 | -1.60% | ✅ consistent |
| Performance (YTD) | +0.0456 | +0.46 | 73% | 26 | -4.45% | ✅ consistent |
| true_ret | -0.0452 | -0.31 | 71% | 24 | -1.54% | ✅ consistent |
| Market Cap | +0.0451 | +0.84 | 81% | 26 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0448 | -0.42 | 71% | 24 | -1.78% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0446 | +0.49 | 69% | 26 | -4.41% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0446 | -0.32 | 67% | 24 | -0.66% | ✅ consistent |
| d_Price | -0.0439 | -0.32 | 71% | 24 | -1.54% | ✅ consistent |
| total_score | -0.0425 | -0.38 | 65% | 26 | -1.09% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

