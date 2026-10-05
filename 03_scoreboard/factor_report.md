# Factor report — multi-date aggregate

_Generated 2026-10-05 16:54 EDT from 40 scan dates._

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
| 2026-09-15 | 2026-09-14 | 2026-09-16 | 2026-09-17 | 2026-09-18 | 11621 |
| 2026-09-16 | 2026-09-15 | 2026-09-17 | 2026-09-18 | 2026-09-21 | 11627 |
| 2026-09-17 | 2026-09-16 | 2026-09-18 | 2026-09-21 | 2026-09-22 | 11636 |
| 2026-09-18 | 2026-09-17 | 2026-09-21 | 2026-09-22 | 2026-09-23 | 11629 |
| 2026-09-21 | 2026-09-18 | 2026-09-22 | 2026-09-23 | 2026-09-24 | 11629 |
| 2026-09-22 | 2026-09-21 | 2026-09-23 | 2026-09-24 | 2026-09-25 | 11637 |
| 2026-09-23 | 2026-09-22 | 2026-09-24 | 2026-09-25 | 2026-09-28 | 11653 |
| 2026-09-24 | 2026-09-23 | 2026-09-25 | 2026-09-28 | 2026-09-29 | 11660 |
| 2026-09-25 | 2026-09-24 | 2026-09-28 | 2026-09-29 | 2026-09-30 | 11665 |
| 2026-09-28 | 2026-09-25 | 2026-09-29 | 2026-09-30 | 2026-10-01 | 11668 |
| 2026-09-29 | 2026-09-28 | 2026-09-30 | 2026-10-01 | 2026-10-02 | 11673 |
| 2026-09-30 | 2026-09-29 | 2026-10-01 | 2026-10-02 | 2026-10-05 | 11682 |
| 2026-10-01 | 2026-09-30 | 2026-10-02 | 2026-10-05 | — | 11693 |
| 2026-10-02 | 2026-10-01 | 2026-10-05 | — | — | 11685 |

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
| 2026-09-15 | -0.0616 | -0.1290 | -0.1450 |
| 2026-09-16 | -0.0722 | -0.0629 | -0.0266 |
| 2026-09-17 | +0.0987 | +0.2454 | +0.3070 |
| 2026-09-18 | +0.0668 | +0.0651 | +0.1188 |
| 2026-09-21 | +0.1709 | -0.0452 | -0.0110 |
| 2026-09-22 | -0.1323 | -0.1167 | -0.0566 |
| 2026-09-23 | +0.0928 | +0.0398 | +0.0444 |
| 2026-09-24 | -0.0345 | +0.0435 | +0.0182 |
| 2026-09-25 | -0.1114 | -0.0598 | -0.0952 |
| 2026-09-28 | -0.0477 | -0.0469 | -0.0752 |
| 2026-09-29 | -0.0367 | +0.0392 | +0.0858 |
| 2026-09-30 | +0.0026 | +0.0403 | +0.0472 |
| 2026-10-01 | +0.0950 | +0.1090 | — |
| 2026-10-02 | +0.0316 | — | — |
- **1d**: mean IC **-0.0182**, ICIR -0.23, sign consistency 68% over 40 dates
- **2d**: mean IC **-0.0220**, ICIR -0.24, sign consistency 54% over 39 dates
- **3d**: mean IC **-0.0235**, ICIR -0.20, sign consistency 61% over 38 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -18014398509481984.00 | 100% | 40 | -5.93% | ✅ consistent |
| short_fwd_2d | -0.6209 | -7.65 | 100% | 39 | -4.88% | ✅ consistent |
| short_fwd_3d | -0.4965 | -4.66 | 100% | 38 | -4.42% | ✅ consistent |
| Volatility (Month) | -0.0662 | -0.55 | 64% | 39 | +0.45% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0582 | +0.77 | 72% | 40 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0562 | -0.52 | 63% | 38 | -0.54% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0544 | +0.75 | 72% | 39 | n/a | ✅ consistent |
| exit_price_3d | +0.0509 | +0.72 | 71% | 38 | n/a | ✅ consistent |
| Profit Margin | +0.0498 | +0.52 | 70% | 40 | -2.42% | ✅ consistent |
| Performance (YTD) | +0.0453 | +0.48 | 68% | 40 | -1.47% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0431 | +0.51 | 65% | 40 | -1.40% | ⚠️ flips / too few dates |
| Price | +0.0426 | +0.56 | 65% | 40 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0426 | +0.56 | 65% | 40 | n/a | ⚠️ flips / too few dates |
| valuation_score | -0.0419 | -0.51 | 75% | 40 | +0.89% | ✅ consistent |
| Average Volume | -0.0419 | -0.73 | 75% | 40 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0417 | -0.41 | 55% | 38 | -0.48% | ⚠️ flips / too few dates |
| Market Cap | +0.0412 | +0.59 | 70% | 40 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0406 | -0.41 | 58% | 38 | -0.45% | ⚠️ flips / too few dates |
| upside_pct | -0.0406 | -0.32 | 62% | 40 | +0.85% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0406 | -0.32 | 62% | 40 | +0.84% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0395 | -0.41 | 58% | 38 | -0.32% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0359 | -0.36 | 55% | 38 | -0.59% | ⚠️ flips / too few dates |
| true_ret | -0.0357 | -0.36 | 53% | 38 | -0.62% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0338 | +0.48 | 75% | 40 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0337 | -0.40 | 63% | 38 | -0.68% | ⚠️ flips / too few dates |
| n_pos | -0.0337 | -0.40 | 62% | 40 | n/a | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0317 | -0.33 | 66% | 38 | -0.14% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0298 | -0.48 | 68% | 38 | -0.54% | ✅ consistent |
| d_Performance (Quarter) | -0.0297 | -0.24 | 58% | 38 | -0.61% | ⚠️ flips / too few dates |
| d_Price | -0.0276 | -0.27 | 53% | 38 | -0.62% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16237959380644838.00 | 100% | 39 | -9.16% | ✅ consistent |
| short_fwd_3d | -0.7369 | -10.60 | 100% | 38 | -8.20% | ✅ consistent |
| short_fwd_1d | -0.6209 | -7.65 | 100% | 39 | -5.39% | ✅ consistent |
| Volatility (Month) | -0.0890 | -0.73 | 76% | 38 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0767 | +1.02 | 85% | 39 | n/a | ✅ consistent |
| exit_price_3d | +0.0714 | +1.03 | 82% | 38 | n/a | ✅ consistent |
| exit_price_1d | +0.0657 | +0.86 | 77% | 39 | n/a | ✅ consistent |
| Profit Margin | +0.0649 | +0.72 | 77% | 39 | -4.48% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0608 | +0.65 | 74% | 39 | -2.62% | ✅ consistent |
| Performance (YTD) | +0.0596 | +0.61 | 74% | 39 | -2.74% | ✅ consistent |
| valuation_score | -0.0571 | -0.78 | 72% | 39 | +1.59% | ✅ consistent |
| upside_pct | -0.0567 | -0.43 | 59% | 39 | +1.50% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0567 | -0.43 | 59% | 39 | +1.49% | ⚠️ flips / too few dates |
| Average Volume | -0.0559 | -1.04 | 85% | 39 | n/a | ✅ consistent |
| Price | +0.0544 | +0.71 | 74% | 39 | n/a | ✅ consistent |
| entry_price | +0.0544 | +0.71 | 74% | 39 | n/a | ✅ consistent |
| Market Cap | +0.0493 | +0.68 | 74% | 39 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0417 | -0.31 | 59% | 37 | -0.57% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0412 | -0.34 | 65% | 37 | -0.97% | ⚠️ flips / too few dates |
| n_pos | -0.0405 | -0.42 | 67% | 39 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0398 | -0.31 | 59% | 37 | -1.05% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0391 | +0.50 | 67% | 39 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0381 | -0.31 | 57% | 37 | -0.80% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0374 | -0.37 | 62% | 37 | -1.42% | ⚠️ flips / too few dates |
| w_pos | -0.0367 | -0.39 | 64% | 39 | n/a | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0365 | +0.41 | 72% | 39 | -2.08% | ✅ consistent |
| Relative Strength Index (14) | +0.0356 | +0.38 | 69% | 39 | n/a | ✅ consistent |
| Beta | -0.0344 | -0.18 | 63% | 38 | -3.79% | ⚠️ flips / too few dates |
| Gross Margin | +0.0328 | +0.48 | 72% | 39 | -4.83% | ✅ consistent |
| d_Performance (YTD) | -0.0326 | -0.26 | 62% | 37 | -1.30% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -18508035071152368.00 | 100% | 38 | -11.68% | ✅ consistent |
| short_fwd_2d | -0.7369 | -10.60 | 100% | 38 | -8.30% | ✅ consistent |
| short_fwd_1d | -0.4965 | -4.66 | 100% | 38 | -4.80% | ✅ consistent |
| Volatility (Month) | -0.1086 | -0.91 | 76% | 37 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0861 | +1.17 | 89% | 38 | n/a | ✅ consistent |
| exit_price_2d | +0.0769 | +1.03 | 89% | 38 | n/a | ✅ consistent |
| Profit Margin | +0.0748 | +0.85 | 82% | 38 | -5.91% | ✅ consistent |
| valuation_score | -0.0693 | -0.97 | 84% | 38 | +2.09% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0682 | +0.69 | 71% | 38 | -3.55% | ✅ consistent |
| exit_price_1d | +0.0680 | +0.90 | 82% | 38 | n/a | ✅ consistent |
| upside_pct | -0.0670 | -0.51 | 71% | 38 | +1.97% | ✅ consistent |
| upside_pct_lvl | -0.0670 | -0.51 | 71% | 38 | +1.97% | ✅ consistent |
| Average Volume | -0.0669 | -1.30 | 84% | 38 | n/a | ✅ consistent |
| Performance (YTD) | +0.0652 | +0.65 | 79% | 38 | -3.68% | ✅ consistent |
| Price | +0.0585 | +0.76 | 74% | 38 | n/a | ✅ consistent |
| entry_price | +0.0585 | +0.76 | 74% | 38 | n/a | ✅ consistent |
| Market Cap | +0.0519 | +0.72 | 76% | 38 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0471 | -0.31 | 72% | 36 | -0.37% | ✅ consistent |
| Relative Strength Index (14) | +0.0467 | +0.53 | 63% | 38 | n/a | ⚠️ flips / too few dates |
| Beta | -0.0467 | -0.26 | 59% | 37 | -5.28% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0442 | +0.51 | 61% | 38 | -2.73% | ⚠️ flips / too few dates |
| w_pos | -0.0439 | -0.40 | 68% | 38 | n/a | ✅ consistent |
| n_pos | -0.0433 | -0.40 | 66% | 38 | n/a | ⚠️ flips / too few dates |
| Short Float | -0.0419 | -0.45 | 66% | 38 | n/a | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0411 | +0.53 | 66% | 38 | n/a | ⚠️ flips / too few dates |
| Gross Margin | +0.0372 | +0.59 | 74% | 38 | -6.28% | ✅ consistent |
| EPS Surprise | +0.0371 | +0.71 | 68% | 38 | -0.35% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0344 | -0.25 | 64% | 36 | -0.72% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0334 | -0.26 | 72% | 36 | -1.02% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0326 | -0.23 | 64% | 36 | -0.82% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

