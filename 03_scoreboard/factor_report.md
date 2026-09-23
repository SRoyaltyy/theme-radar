# Factor report — multi-date aggregate

_Generated 2026-09-23 17:01 EDT from 32 scan dates._

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
| 2026-09-21 | 2026-09-18 | 2026-09-22 | 2026-09-23 | — | 11629 |
| 2026-09-22 | 2026-09-21 | 2026-09-23 | — | — | 11637 |

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
| 2026-09-21 | +0.1709 | -0.0452 | — |
| 2026-09-22 | -0.1323 | — | — |
- **1d**: mean IC **-0.0225**, ICIR -0.28, sign consistency 72% over 32 dates
- **2d**: mean IC **-0.0292**, ICIR -0.30, sign consistency 58% over 31 dates
- **3d**: mean IC **-0.0283**, ICIR -0.22, sign consistency 63% over 30 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -18014398509481984.00 | 100% | 32 | -5.99% | ✅ consistent |
| short_fwd_2d | -0.6166 | -7.27 | 100% | 31 | -4.91% | ✅ consistent |
| short_fwd_3d | -0.4945 | -4.38 | 100% | 30 | -4.37% | ✅ consistent |
| d_Performance (Week) | -0.0625 | -0.54 | 67% | 30 | -0.63% | ✅ consistent |
| Volatility (Month) | -0.0612 | -0.46 | 58% | 31 | +0.45% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0442 | +0.66 | 69% | 32 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0436 | -0.39 | 50% | 30 | -0.51% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0432 | -0.40 | 53% | 30 | -0.52% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0430 | +0.67 | 70% | 30 | n/a | ✅ consistent |
| true_ret | -0.0409 | -0.38 | 50% | 30 | -0.63% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0408 | +0.63 | 68% | 31 | n/a | ✅ consistent |
| n_pos | -0.0406 | -0.46 | 66% | 32 | n/a | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0398 | -0.36 | 53% | 30 | -0.63% | ⚠️ flips / too few dates |
| Profit Margin | +0.0396 | +0.39 | 66% | 32 | -2.45% | ⚠️ flips / too few dates |
| Average Volume | -0.0388 | -0.62 | 69% | 32 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0381 | -0.36 | 50% | 30 | -0.36% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0379 | -0.26 | 59% | 32 | -1.23% | ⚠️ flips / too few dates |
| valuation_score | -0.0367 | -0.40 | 69% | 32 | +1.00% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0367 | -0.39 | 63% | 30 | -0.79% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0332 | -0.49 | 70% | 30 | -0.68% | ✅ consistent |
| d_Forward P/E | -0.0330 | -0.33 | 67% | 30 | -0.18% | ✅ consistent |
| Beta | -0.0314 | -0.16 | 55% | 31 | -1.28% | ⚠️ flips / too few dates |
| w_pos | -0.0310 | -0.33 | 66% | 32 | n/a | ⚠️ flips / too few dates |
| d_Price | -0.0306 | -0.28 | 53% | 30 | -0.63% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0282 | +0.32 | 62% | 32 | -1.63% | ⚠️ flips / too few dates |
| Price | +0.0280 | +0.42 | 59% | 32 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0280 | +0.42 | 59% | 32 | n/a | ⚠️ flips / too few dates |
| Market Cap | +0.0276 | +0.45 | 66% | 32 | n/a | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0252 | -0.19 | 57% | 30 | -0.66% | ⚠️ flips / too few dates |
| Short Float | -0.0242 | -0.20 | 50% | 32 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -15858810771469616.00 | 100% | 31 | -9.35% | ✅ consistent |
| short_fwd_3d | -0.7318 | -9.68 | 100% | 30 | -8.29% | ✅ consistent |
| short_fwd_1d | -0.6166 | -7.27 | 100% | 31 | -5.53% | ✅ consistent |
| Volatility (Month) | -0.0762 | -0.60 | 70% | 30 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0564 | +0.95 | 81% | 31 | n/a | ✅ consistent |
| exit_price_3d | +0.0556 | +0.94 | 77% | 30 | n/a | ✅ consistent |
| Average Volume | -0.0503 | -0.88 | 81% | 31 | n/a | ✅ consistent |
| Profit Margin | +0.0485 | +0.53 | 71% | 31 | -4.67% | ✅ consistent |
| valuation_score | -0.0471 | -0.62 | 65% | 31 | +1.85% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0449 | +0.75 | 74% | 31 | n/a | ✅ consistent |
| n_pos | -0.0441 | -0.43 | 71% | 31 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0431 | -0.31 | 59% | 29 | -0.52% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0424 | -0.32 | 66% | 29 | -1.02% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0391 | -0.28 | 59% | 29 | -1.14% | ⚠️ flips / too few dates |
| w_pos | -0.0386 | -0.39 | 68% | 31 | n/a | ✅ consistent |
| Beta | -0.0365 | -0.18 | 63% | 30 | -2.45% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0357 | -0.33 | 66% | 29 | -1.59% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0354 | +0.41 | 68% | 31 | -3.12% | ✅ consistent |
| true_ret | -0.0351 | -0.26 | 55% | 29 | -1.33% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0339 | -0.25 | 62% | 29 | -1.39% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0334 | +0.42 | 68% | 31 | -3.03% | ✅ consistent |
| Performance (Week) | -0.0333 | -0.24 | 52% | 31 | -2.04% | ⚠️ flips / too few dates |
| Price | +0.0332 | +0.55 | 71% | 31 | n/a | ✅ consistent |
| entry_price | +0.0332 | +0.55 | 71% | 31 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0329 | -0.25 | 55% | 29 | -0.81% | ⚠️ flips / too few dates |
| Market Cap | +0.0325 | +0.53 | 68% | 31 | n/a | ✅ consistent |
| Short Float | -0.0303 | -0.28 | 58% | 31 | n/a | ⚠️ flips / too few dates |
| Gross Margin | +0.0302 | +0.43 | 68% | 31 | -2.18% | ✅ consistent |
| d_Price | -0.0302 | -0.22 | 59% | 29 | -1.33% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0300 | -0.37 | 66% | 29 | -2.09% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -16444820705884542.00 | 100% | 30 | -11.84% | ✅ consistent |
| short_fwd_2d | -0.7318 | -9.68 | 100% | 30 | -8.46% | ✅ consistent |
| short_fwd_1d | -0.4945 | -4.38 | 100% | 30 | -4.89% | ✅ consistent |
| Volatility (Month) | -0.0932 | -0.75 | 69% | 29 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0647 | +1.12 | 87% | 30 | n/a | ✅ consistent |
| Average Volume | -0.0607 | -1.11 | 80% | 30 | n/a | ✅ consistent |
| Profit Margin | +0.0580 | +0.65 | 77% | 30 | -6.26% | ✅ consistent |
| valuation_score | -0.0579 | -0.78 | 80% | 30 | +2.54% | ✅ consistent |
| exit_price_2d | +0.0553 | +0.93 | 87% | 30 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0503 | -0.31 | 75% | 28 | -0.36% | ✅ consistent |
| exit_price_1d | +0.0460 | +0.77 | 77% | 30 | n/a | ✅ consistent |
| Beta | -0.0453 | -0.23 | 55% | 29 | -3.66% | ⚠️ flips / too few dates |
| n_pos | -0.0445 | -0.38 | 63% | 30 | n/a | ⚠️ flips / too few dates |
| w_pos | -0.0436 | -0.37 | 67% | 30 | n/a | ✅ consistent |
| Performance (YTD) | +0.0408 | +0.44 | 73% | 30 | -4.19% | ✅ consistent |
| Short Float | -0.0396 | -0.40 | 63% | 30 | n/a | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0391 | +0.45 | 63% | 30 | -4.11% | ⚠️ flips / too few dates |
| Price | +0.0362 | +0.59 | 67% | 30 | n/a | ✅ consistent |
| entry_price | +0.0362 | +0.59 | 67% | 30 | n/a | ✅ consistent |
| Performance (Week) | -0.0356 | -0.26 | 50% | 30 | -2.46% | ⚠️ flips / too few dates |
| Market Cap | +0.0348 | +0.60 | 73% | 30 | n/a | ✅ consistent |
| Gross Margin | +0.0346 | +0.54 | 73% | 30 | -2.85% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0337 | -0.23 | 64% | 28 | -0.80% | ⚠️ flips / too few dates |
| upside_pct | -0.0329 | -0.27 | 63% | 30 | +2.39% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0329 | -0.26 | 63% | 30 | +2.38% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0323 | -0.23 | 75% | 28 | -0.99% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0304 | -0.20 | 61% | 28 | -0.91% | ⚠️ flips / too few dates |
| total_score | -0.0283 | -0.22 | 63% | 30 | -0.84% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0280 | -0.34 | 68% | 28 | -2.02% | ✅ consistent |
| Short Ratio | -0.0280 | -0.35 | 57% | 30 | n/a | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

