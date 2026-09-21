# Factor report — multi-date aggregate

_Generated 2026-09-21 16:55 EDT from 30 scan dates._

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
| 2026-09-17 | 2026-09-16 | 2026-09-18 | 2026-09-21 | — | 11636 |
| 2026-09-18 | 2026-09-17 | 2026-09-21 | — | — | 11629 |

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
| 2026-09-17 | +0.0987 | +0.2454 | — |
| 2026-09-18 | +0.0668 | — | — |
- **1d**: mean IC **-0.0253**, ICIR -0.34, sign consistency 73% over 30 dates
- **2d**: mean IC **-0.0319**, ICIR -0.32, sign consistency 59% over 29 dates
- **3d**: mean IC **-0.0456**, ICIR -0.42, sign consistency 68% over 28 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -18646673975492636.00 | 100% | 30 | -6.06% | ✅ consistent |
| short_fwd_2d | -0.6163 | -7.72 | 100% | 29 | -4.95% | ✅ consistent |
| short_fwd_3d | -0.4906 | -4.29 | 100% | 28 | -4.46% | ✅ consistent |
| d_Performance (Week) | -0.0626 | -0.62 | 68% | 28 | -0.64% | ✅ consistent |
| Volatility (Month) | -0.0603 | -0.48 | 59% | 29 | +0.45% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0455 | -0.43 | 50% | 28 | -0.53% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0452 | -0.44 | 54% | 28 | -0.54% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0437 | +0.67 | 70% | 30 | n/a | ✅ consistent |
| true_ret | -0.0429 | -0.42 | 50% | 28 | -0.64% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0427 | +0.65 | 68% | 28 | n/a | ✅ consistent |
| n_pos | -0.0421 | -0.55 | 67% | 30 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0419 | -0.40 | 54% | 28 | -0.66% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0417 | +0.64 | 69% | 29 | n/a | ✅ consistent |
| Profit Margin | +0.0409 | +0.41 | 67% | 30 | -2.60% | ✅ consistent |
| d_Forward P/E | -0.0401 | -0.41 | 68% | 28 | -0.21% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0399 | -0.41 | 50% | 28 | -0.38% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0394 | -0.28 | 60% | 30 | -1.28% | ⚠️ flips / too few dates |
| Average Volume | -0.0378 | -0.61 | 70% | 30 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0369 | -0.40 | 64% | 28 | -0.81% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0358 | -0.56 | 71% | 28 | -0.70% | ✅ consistent |
| valuation_score | -0.0354 | -0.40 | 70% | 30 | +1.07% | ✅ consistent |
| d_Price | -0.0325 | -0.30 | 54% | 28 | -0.64% | ⚠️ flips / too few dates |
| w_pos | -0.0324 | -0.40 | 67% | 30 | n/a | ✅ consistent |
| Beta | -0.0316 | -0.16 | 55% | 29 | -1.28% | ⚠️ flips / too few dates |
| Market Cap | +0.0297 | +0.48 | 67% | 30 | n/a | ✅ consistent |
| Performance (YTD) | +0.0281 | +0.31 | 63% | 30 | -1.71% | ⚠️ flips / too few dates |
| Price | +0.0274 | +0.41 | 60% | 30 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0274 | +0.41 | 60% | 30 | n/a | ⚠️ flips / too few dates |
| total_score | -0.0253 | -0.34 | 73% | 30 | -0.48% | ✅ consistent |
| d_Performance (Quarter) | -0.0249 | -0.20 | 57% | 28 | -0.68% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16168417479159774.00 | 100% | 29 | -9.47% | ✅ consistent |
| short_fwd_3d | -0.7289 | -9.49 | 100% | 28 | -8.44% | ✅ consistent |
| short_fwd_1d | -0.6163 | -7.72 | 100% | 29 | -5.63% | ✅ consistent |
| Volatility (Month) | -0.0810 | -0.64 | 71% | 28 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0568 | +0.93 | 79% | 29 | n/a | ✅ consistent |
| exit_price_3d | +0.0555 | +0.91 | 75% | 28 | n/a | ✅ consistent |
| Profit Margin | +0.0554 | +0.62 | 72% | 29 | -4.93% | ✅ consistent |
| Average Volume | -0.0504 | -0.86 | 79% | 29 | n/a | ✅ consistent |
| n_pos | -0.0493 | -0.49 | 72% | 29 | n/a | ✅ consistent |
| Beta | -0.0484 | -0.25 | 64% | 28 | -2.51% | ⚠️ flips / too few dates |
| valuation_score | -0.0476 | -0.61 | 66% | 29 | +1.92% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0455 | -0.34 | 67% | 27 | -1.11% | ✅ consistent |
| exit_price_1d | +0.0453 | +0.74 | 72% | 29 | n/a | ✅ consistent |
| w_pos | -0.0439 | -0.46 | 69% | 29 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0426 | -0.30 | 59% | 27 | -1.23% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0418 | -0.29 | 56% | 27 | -0.57% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0415 | -0.38 | 67% | 27 | -1.70% | ✅ consistent |
| Performance (Week) | -0.0399 | -0.28 | 55% | 29 | -2.20% | ⚠️ flips / too few dates |
| true_ret | -0.0376 | -0.27 | 56% | 27 | -1.40% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0374 | -0.27 | 63% | 27 | -1.52% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0368 | +0.42 | 69% | 29 | -3.22% | ✅ consistent |
| Short Float | -0.0353 | -0.34 | 59% | 29 | n/a | ⚠️ flips / too few dates |
| d_Price | -0.0352 | -0.26 | 59% | 27 | -1.40% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0352 | -0.30 | 63% | 27 | -0.28% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0350 | -0.26 | 56% | 27 | -0.88% | ⚠️ flips / too few dates |
| Market Cap | +0.0346 | +0.56 | 69% | 29 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0341 | +0.42 | 66% | 29 | -3.14% | ⚠️ flips / too few dates |
| Price | +0.0337 | +0.54 | 69% | 29 | n/a | ✅ consistent |
| entry_price | +0.0337 | +0.54 | 69% | 29 | n/a | ✅ consistent |
| d_Market Cap | -0.0334 | -0.40 | 67% | 27 | -2.20% | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -16850926812823186.00 | 100% | 28 | -12.08% | ✅ consistent |
| short_fwd_2d | -0.7289 | -9.49 | 100% | 28 | -8.62% | ✅ consistent |
| short_fwd_1d | -0.4906 | -4.29 | 100% | 28 | -4.91% | ✅ consistent |
| Volatility (Month) | -0.1006 | -0.81 | 70% | 27 | +1.69% | ✅ consistent |
| Profit Margin | +0.0679 | +0.81 | 82% | 28 | -6.51% | ✅ consistent |
| d_Performance (Week) | -0.0676 | -0.46 | 77% | 26 | -0.46% | ✅ consistent |
| Beta | -0.0656 | -0.36 | 59% | 27 | -3.77% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0649 | +1.09 | 86% | 28 | n/a | ✅ consistent |
| w_pos | -0.0618 | -0.65 | 71% | 28 | n/a | ✅ consistent |
| n_pos | -0.0617 | -0.62 | 68% | 28 | n/a | ✅ consistent |
| Average Volume | -0.0588 | -1.06 | 79% | 28 | n/a | ✅ consistent |
| valuation_score | -0.0576 | -0.76 | 79% | 28 | +2.61% | ✅ consistent |
| exit_price_2d | +0.0553 | +0.91 | 86% | 28 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0526 | -0.44 | 81% | 26 | -1.12% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0523 | -0.39 | 69% | 26 | -0.91% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0492 | -0.34 | 65% | 26 | -1.01% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0462 | +0.75 | 75% | 28 | n/a | ✅ consistent |
| Short Float | -0.0462 | -0.47 | 64% | 28 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0459 | -0.34 | 54% | 28 | -2.63% | ⚠️ flips / too few dates |
| total_score | -0.0456 | -0.42 | 68% | 28 | -0.99% | ✅ consistent |
| d_Performance (YTD) | -0.0436 | -0.30 | 69% | 26 | -1.41% | ✅ consistent |
| true_ret | -0.0429 | -0.30 | 69% | 26 | -1.40% | ✅ consistent |
| Performance (YTD) | +0.0428 | +0.44 | 75% | 28 | -4.32% | ✅ consistent |
| upside_pct | -0.0419 | -0.35 | 68% | 28 | +2.45% | ✅ consistent |
| upside_pct_lvl | -0.0419 | -0.35 | 68% | 28 | +2.45% | ✅ consistent |
| price_score | -0.0414 | -0.35 | 69% | 26 | -1.92% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0407 | -0.38 | 69% | 26 | -1.58% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0404 | -0.30 | 65% | 26 | -0.56% | ⚠️ flips / too few dates |
| Forward P/E | -0.0403 | -0.39 | 57% | 28 | n/a | ⚠️ flips / too few dates |
| d_Price | -0.0403 | -0.29 | 69% | 26 | -1.40% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

