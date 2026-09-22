# Factor report — multi-date aggregate

_Generated 2026-09-22 19:25 EDT from 31 scan dates._

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
| 2026-09-18 | 2026-09-17 | 2026-09-21 | 2026-09-22 | — | 11629 |
| 2026-09-21 | 2026-09-18 | 2026-09-22 | — | — | 11629 |

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
| 2026-09-18 | +0.0668 | +0.0651 | — |
| 2026-09-21 | +0.1709 | — | — |
- **1d**: mean IC **-0.0189**, ICIR -0.24, sign consistency 71% over 31 dates
- **2d**: mean IC **-0.0287**, ICIR -0.29, sign consistency 57% over 30 dates
- **3d**: mean IC **-0.0334**, ICIR -0.27, sign consistency 66% over 29 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -17730689463655972.00 | 100% | 31 | -6.00% | ✅ consistent |
| short_fwd_2d | -0.6210 | -7.53 | 100% | 30 | -4.91% | ✅ consistent |
| short_fwd_3d | -0.4903 | -4.36 | 100% | 29 | -4.40% | ✅ consistent |
| Volatility (Month) | -0.0543 | -0.42 | 57% | 30 | +0.45% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0541 | -0.50 | 66% | 29 | -0.62% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0432 | +0.67 | 70% | 30 | n/a | ✅ consistent |
| exit_price_3d | +0.0416 | +0.64 | 69% | 29 | n/a | ✅ consistent |
| exit_price_1d | +0.0413 | +0.63 | 68% | 31 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0387 | -0.35 | 48% | 29 | -0.50% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0382 | -0.36 | 52% | 29 | -0.51% | ⚠️ flips / too few dates |
| true_ret | -0.0362 | -0.34 | 48% | 29 | -0.62% | ⚠️ flips / too few dates |
| Profit Margin | +0.0362 | +0.36 | 65% | 31 | -2.55% | ⚠️ flips / too few dates |
| Average Volume | -0.0359 | -0.58 | 68% | 31 | n/a | ✅ consistent |
| n_pos | -0.0351 | -0.42 | 65% | 31 | n/a | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0351 | -0.32 | 52% | 29 | -0.62% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0329 | -0.36 | 62% | 29 | -0.79% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0328 | -0.32 | 48% | 29 | -0.35% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0325 | -0.31 | 66% | 29 | -0.18% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0322 | -0.22 | 58% | 31 | -1.24% | ⚠️ flips / too few dates |
| valuation_score | -0.0321 | -0.36 | 68% | 31 | +1.06% | ✅ consistent |
| d_Market Cap | -0.0313 | -0.46 | 69% | 29 | -0.66% | ✅ consistent |
| Market Cap | +0.0273 | +0.44 | 65% | 31 | n/a | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0271 | +0.30 | 61% | 31 | -1.70% | ⚠️ flips / too few dates |
| d_Price | -0.0265 | -0.24 | 52% | 29 | -0.62% | ⚠️ flips / too few dates |
| w_pos | -0.0252 | -0.28 | 65% | 31 | n/a | ⚠️ flips / too few dates |
| Price | +0.0252 | +0.38 | 58% | 31 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0252 | +0.38 | 58% | 31 | n/a | ⚠️ flips / too few dates |
| Beta | -0.0242 | -0.12 | 53% | 30 | -1.28% | ⚠️ flips / too few dates |
| Gross Margin | +0.0228 | +0.34 | 61% | 31 | -1.12% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0209 | +0.27 | 55% | 31 | -1.64% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16444820705884542.00 | 100% | 30 | -9.39% | ✅ consistent |
| short_fwd_3d | -0.7317 | -9.52 | 100% | 29 | -8.35% | ✅ consistent |
| short_fwd_1d | -0.6210 | -7.53 | 100% | 30 | -5.60% | ✅ consistent |
| Volatility (Month) | -0.0745 | -0.58 | 69% | 29 | +0.97% | ✅ consistent |
| exit_price_3d | +0.0563 | +0.94 | 76% | 29 | n/a | ✅ consistent |
| exit_price_2d | +0.0562 | +0.94 | 80% | 30 | n/a | ✅ consistent |
| Average Volume | -0.0493 | -0.85 | 80% | 30 | n/a | ✅ consistent |
| Profit Margin | +0.0492 | +0.53 | 70% | 30 | -4.85% | ✅ consistent |
| valuation_score | -0.0456 | -0.59 | 63% | 30 | +1.91% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0447 | +0.74 | 73% | 30 | n/a | ✅ consistent |
| n_pos | -0.0436 | -0.42 | 70% | 30 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0425 | -0.30 | 57% | 28 | -0.51% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0413 | -0.31 | 64% | 28 | -1.02% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0386 | -0.27 | 57% | 28 | -1.15% | ⚠️ flips / too few dates |
| w_pos | -0.0379 | -0.38 | 67% | 30 | n/a | ✅ consistent |
| Performance (Week) | -0.0363 | -0.26 | 53% | 30 | -2.10% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0361 | -0.33 | 64% | 28 | -1.61% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0351 | +0.40 | 67% | 30 | -3.19% | ✅ consistent |
| Beta | -0.0350 | -0.17 | 62% | 29 | -2.54% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0346 | -0.30 | 64% | 28 | -0.25% | ⚠️ flips / too few dates |
| Market Cap | +0.0343 | +0.56 | 70% | 30 | n/a | ✅ consistent |
| true_ret | -0.0341 | -0.25 | 54% | 28 | -1.34% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0334 | -0.24 | 61% | 28 | -1.43% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0331 | +0.41 | 67% | 30 | -3.10% | ✅ consistent |
| Price | +0.0330 | +0.53 | 70% | 30 | n/a | ✅ consistent |
| entry_price | +0.0330 | +0.53 | 70% | 30 | n/a | ✅ consistent |
| d_Market Cap | -0.0325 | -0.40 | 68% | 28 | -2.14% | ✅ consistent |
| Gross Margin | +0.0324 | +0.46 | 70% | 30 | -2.13% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0312 | -0.24 | 54% | 28 | -0.81% | ⚠️ flips / too few dates |
| d_Price | -0.0304 | -0.22 | 57% | 28 | -1.34% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -17149196460853472.00 | 100% | 29 | -11.97% | ✅ consistent |
| short_fwd_2d | -0.7317 | -9.52 | 100% | 29 | -8.55% | ✅ consistent |
| short_fwd_1d | -0.4903 | -4.36 | 100% | 29 | -4.93% | ✅ consistent |
| Volatility (Month) | -0.0946 | -0.75 | 68% | 28 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0638 | +1.08 | 86% | 29 | n/a | ✅ consistent |
| Profit Margin | +0.0615 | +0.69 | 79% | 29 | -6.45% | ✅ consistent |
| Average Volume | -0.0591 | -1.08 | 79% | 29 | n/a | ✅ consistent |
| valuation_score | -0.0563 | -0.75 | 79% | 29 | +2.60% | ✅ consistent |
| exit_price_2d | +0.0542 | +0.90 | 86% | 29 | n/a | ✅ consistent |
| Beta | -0.0531 | -0.28 | 57% | 28 | -3.73% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0518 | -0.32 | 74% | 27 | -0.37% | ✅ consistent |
| n_pos | -0.0494 | -0.42 | 66% | 29 | n/a | ⚠️ flips / too few dates |
| w_pos | -0.0487 | -0.42 | 69% | 29 | n/a | ✅ consistent |
| exit_price_1d | +0.0449 | +0.74 | 76% | 29 | n/a | ✅ consistent |
| Performance (Week) | -0.0418 | -0.31 | 52% | 29 | -2.57% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0412 | +0.43 | 72% | 29 | -4.28% | ✅ consistent |
| Short Float | -0.0409 | -0.41 | 62% | 29 | n/a | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0391 | -0.26 | 67% | 27 | -0.85% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0381 | +0.43 | 62% | 29 | -4.21% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0374 | -0.27 | 78% | 27 | -1.06% | ✅ consistent |
| Gross Margin | +0.0363 | +0.56 | 76% | 29 | -2.82% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0360 | -0.23 | 63% | 27 | -0.98% | ⚠️ flips / too few dates |
| Market Cap | +0.0355 | +0.61 | 72% | 29 | n/a | ✅ consistent |
| Price | +0.0352 | +0.57 | 66% | 29 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0352 | +0.57 | 66% | 29 | n/a | ⚠️ flips / too few dates |
| upside_pct | -0.0341 | -0.27 | 66% | 29 | +2.44% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0341 | -0.27 | 66% | 29 | +2.44% | ⚠️ flips / too few dates |
| total_score | -0.0334 | -0.27 | 66% | 29 | -0.88% | ⚠️ flips / too few dates |
| Forward P/E | -0.0331 | -0.31 | 55% | 29 | n/a | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0330 | -0.29 | 67% | 27 | -1.55% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

