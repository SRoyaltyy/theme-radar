# Factor report — multi-date aggregate

_Generated 2026-09-16 17:09 EDT from 27 scan dates._

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
| 2026-09-14 | 2026-09-11 | 2026-09-15 | 2026-09-16 | — | 11604 |
| 2026-09-15 | 2026-09-14 | 2026-09-16 | — | — | 11621 |

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
| 2026-09-14 | -0.0250 | -0.1114 | — |
| 2026-09-15 | -0.0616 | — | — |
- **1d**: mean IC **-0.0315**, ICIR -0.44, sign consistency 78% over 27 dates
- **2d**: mean IC **-0.0376**, ICIR -0.44, sign consistency 58% over 26 dates
- **3d**: mean IC **-0.0361**, ICIR -0.33, sign consistency 64% over 25 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -19107155017577316.00 | 100% | 27 | -6.21% | ✅ consistent |
| short_fwd_2d | -0.6159 | -7.47 | 100% | 26 | -5.15% | ✅ consistent |
| short_fwd_3d | -0.4860 | -4.22 | 100% | 25 | -4.68% | ✅ consistent |
| d_Performance (Week) | -0.0726 | -0.74 | 72% | 25 | -0.75% | ✅ consistent |
| Volatility (Month) | -0.0723 | -0.58 | 62% | 26 | +0.31% | ⚠️ flips / too few dates |
| Beta | -0.0580 | -0.31 | 62% | 26 | -1.35% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0562 | -0.53 | 56% | 25 | -0.69% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0557 | -0.54 | 60% | 25 | -0.70% | ⚠️ flips / too few dates |
| Profit Margin | +0.0530 | +0.56 | 70% | 27 | -2.70% | ✅ consistent |
| d_Performance (YTD) | -0.0526 | -0.50 | 60% | 25 | -0.84% | ⚠️ flips / too few dates |
| true_ret | -0.0523 | -0.51 | 56% | 25 | -0.80% | ⚠️ flips / too few dates |
| n_pos | -0.0504 | -0.68 | 70% | 27 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0491 | -0.50 | 56% | 25 | -0.55% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0483 | -0.54 | 72% | 25 | -1.01% | ✅ consistent |
| exit_price_1d | +0.0468 | +0.71 | 70% | 27 | n/a | ✅ consistent |
| exit_price_2d | +0.0466 | +0.70 | 69% | 26 | n/a | ✅ consistent |
| d_Forward P/E | -0.0456 | -0.46 | 72% | 25 | -0.25% | ✅ consistent |
| d_Price | -0.0434 | -0.40 | 60% | 25 | -0.80% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0425 | +0.65 | 68% | 25 | n/a | ✅ consistent |
| w_pos | -0.0414 | -0.53 | 70% | 27 | n/a | ✅ consistent |
| d_Market Cap | -0.0393 | -0.60 | 72% | 25 | -0.88% | ✅ consistent |
| Market Cap | +0.0351 | +0.60 | 70% | 27 | n/a | ✅ consistent |
| Average Volume | -0.0347 | -0.55 | 67% | 27 | n/a | ✅ consistent |
| upside_pct | -0.0338 | -0.27 | 63% | 27 | +1.05% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0338 | -0.27 | 63% | 27 | +1.05% | ⚠️ flips / too few dates |
| valuation_score | -0.0337 | -0.36 | 67% | 27 | +1.11% | ✅ consistent |
| Performance (Week) | -0.0329 | -0.24 | 59% | 27 | -1.39% | ⚠️ flips / too few dates |
| total_score | -0.0315 | -0.44 | 78% | 27 | -0.63% | ✅ consistent |
| Price | +0.0306 | +0.46 | 63% | 27 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0306 | +0.46 | 63% | 27 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16237959380644838.00 | 100% | 26 | -9.80% | ✅ consistent |
| short_fwd_3d | -0.7261 | -9.17 | 100% | 25 | -8.82% | ✅ consistent |
| short_fwd_1d | -0.6159 | -7.47 | 100% | 26 | -5.67% | ✅ consistent |
| Volatility (Month) | -0.0948 | -0.75 | 76% | 25 | +0.53% | ✅ consistent |
| Beta | -0.0775 | -0.42 | 72% | 25 | -2.74% | ✅ consistent |
| Profit Margin | +0.0716 | +0.91 | 81% | 26 | -5.13% | ✅ consistent |
| exit_price_2d | +0.0620 | +1.03 | 85% | 26 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0599 | -0.47 | 71% | 24 | -1.31% | ✅ consistent |
| exit_price_3d | +0.0582 | +0.98 | 80% | 25 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0566 | -0.42 | 62% | 24 | -1.45% | ⚠️ flips / too few dates |
| n_pos | -0.0561 | -0.63 | 73% | 26 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0543 | -0.53 | 71% | 24 | -1.97% | ✅ consistent |
| w_pos | -0.0523 | -0.63 | 69% | 26 | n/a | ✅ consistent |
| upside_pct | -0.0510 | -0.44 | 58% | 26 | +1.89% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0509 | -0.44 | 58% | 26 | +1.89% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0508 | +0.83 | 77% | 26 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0506 | -0.38 | 67% | 24 | -1.77% | ✅ consistent |
| d_Price | -0.0506 | -0.39 | 62% | 24 | -1.62% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0502 | -0.39 | 58% | 24 | -0.62% | ⚠️ flips / too few dates |
| true_ret | -0.0500 | -0.38 | 58% | 24 | -1.62% | ⚠️ flips / too few dates |
| Forward P/E | -0.0493 | -0.55 | 69% | 26 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0489 | -0.38 | 58% | 24 | -1.08% | ⚠️ flips / too few dates |
| Average Volume | -0.0461 | -0.77 | 77% | 26 | n/a | ✅ consistent |
| d_Forward P/E | -0.0457 | -0.38 | 67% | 24 | -0.36% | ✅ consistent |
| valuation_score | -0.0450 | -0.55 | 62% | 26 | +2.01% | ⚠️ flips / too few dates |
| Market Cap | +0.0439 | +0.77 | 73% | 26 | n/a | ✅ consistent |
| d_Market Cap | -0.0429 | -0.52 | 71% | 24 | -2.48% | ✅ consistent |
| Price | +0.0391 | +0.63 | 73% | 26 | n/a | ✅ consistent |
| entry_price | +0.0391 | +0.63 | 73% | 26 | n/a | ✅ consistent |
| Short Float | -0.0388 | -0.36 | 58% | 26 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -15922629181314432.00 | 100% | 25 | -12.54% | ✅ consistent |
| short_fwd_2d | -0.7261 | -9.17 | 100% | 25 | -8.85% | ✅ consistent |
| short_fwd_1d | -0.4860 | -4.22 | 100% | 25 | -4.93% | ✅ consistent |
| Volatility (Month) | -0.1120 | -0.89 | 75% | 24 | +1.54% | ✅ consistent |
| Beta | -0.0909 | -0.52 | 62% | 24 | -4.15% | ⚠️ flips / too few dates |
| Profit Margin | +0.0826 | +1.13 | 88% | 25 | -6.88% | ✅ consistent |
| exit_price_3d | +0.0687 | +1.14 | 88% | 25 | n/a | ✅ consistent |
| Forward P/E | -0.0627 | -0.75 | 64% | 25 | n/a | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0595 | -0.43 | 78% | 23 | -0.38% | ✅ consistent |
| exit_price_2d | +0.0594 | +0.97 | 88% | 25 | n/a | ✅ consistent |
| upside_pct | -0.0587 | -0.52 | 72% | 25 | +2.63% | ✅ consistent |
| upside_pct_lvl | -0.0587 | -0.52 | 72% | 25 | +2.62% | ✅ consistent |
| w_pos | -0.0560 | -0.58 | 68% | 25 | n/a | ✅ consistent |
| Average Volume | -0.0538 | -0.95 | 76% | 25 | n/a | ✅ consistent |
| valuation_score | -0.0522 | -0.67 | 76% | 25 | +2.79% | ✅ consistent |
| n_pos | -0.0522 | -0.53 | 64% | 25 | n/a | ⚠️ flips / too few dates |
| exit_price_1d | +0.0504 | +0.81 | 80% | 25 | n/a | ✅ consistent |
| Short Float | -0.0472 | -0.46 | 64% | 25 | n/a | ⚠️ flips / too few dates |
| Market Cap | +0.0463 | +0.85 | 80% | 25 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0462 | -0.35 | 70% | 23 | -1.06% | ✅ consistent |
| d_Performance (Month) | -0.0449 | -0.36 | 78% | 23 | -1.25% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0435 | +0.47 | 68% | 25 | -4.55% | ✅ consistent |
| Performance (YTD) | +0.0420 | +0.42 | 72% | 25 | -4.60% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0419 | -0.30 | 65% | 23 | -1.18% | ⚠️ flips / too few dates |
| Gross Margin | +0.0408 | +0.59 | 76% | 25 | -2.43% | ✅ consistent |
| Price | +0.0407 | +0.64 | 72% | 25 | n/a | ✅ consistent |
| entry_price | +0.0407 | +0.64 | 72% | 25 | n/a | ✅ consistent |
| total_score | -0.0361 | -0.33 | 64% | 25 | -1.13% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0358 | -0.26 | 70% | 23 | -1.64% | ✅ consistent |
| d_Market Cap | -0.0351 | -0.45 | 74% | 23 | -2.42% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

