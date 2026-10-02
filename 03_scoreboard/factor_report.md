# Factor report — multi-date aggregate

_Generated 2026-10-02 16:49 EDT from 39 scan dates._

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
| 2026-09-30 | 2026-09-29 | 2026-10-01 | 2026-10-02 | — | 11682 |
| 2026-10-01 | 2026-09-30 | 2026-10-02 | — | — | 11693 |

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
| 2026-09-30 | +0.0026 | +0.0403 | — |
| 2026-10-01 | +0.0950 | — | — |
- **1d**: mean IC **-0.0195**, ICIR -0.24, sign consistency 69% over 39 dates
- **2d**: mean IC **-0.0254**, ICIR -0.28, sign consistency 55% over 38 dates
- **3d**: mean IC **-0.0254**, ICIR -0.22, sign consistency 62% over 37 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -17787793281263588.00 | 100% | 39 | -5.96% | ✅ consistent |
| short_fwd_2d | -0.6202 | -7.55 | 100% | 38 | -4.93% | ✅ consistent |
| short_fwd_3d | -0.4949 | -4.60 | 100% | 37 | -4.45% | ✅ consistent |
| Volatility (Month) | -0.0660 | -0.54 | 63% | 38 | +0.45% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0582 | -0.54 | 65% | 37 | -0.55% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0550 | +0.75 | 72% | 39 | n/a | ✅ consistent |
| exit_price_2d | +0.0511 | +0.72 | 71% | 38 | n/a | ✅ consistent |
| Profit Margin | +0.0483 | +0.50 | 69% | 39 | -2.45% | ✅ consistent |
| exit_price_3d | +0.0471 | +0.70 | 70% | 37 | n/a | ✅ consistent |
| Performance (YTD) | +0.0433 | +0.46 | 67% | 39 | -1.49% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0432 | -0.42 | 57% | 37 | -0.48% | ⚠️ flips / too few dates |
| Average Volume | -0.0413 | -0.72 | 74% | 39 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0412 | -0.41 | 57% | 37 | -0.45% | ⚠️ flips / too few dates |
| valuation_score | -0.0411 | -0.49 | 74% | 39 | +0.90% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0403 | -0.42 | 57% | 37 | -0.31% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0394 | +0.48 | 64% | 39 | -1.43% | ⚠️ flips / too few dates |
| Price | +0.0393 | +0.53 | 64% | 39 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0393 | +0.53 | 64% | 39 | n/a | ⚠️ flips / too few dates |
| upside_pct | -0.0388 | -0.30 | 62% | 39 | +0.85% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0388 | -0.30 | 62% | 39 | +0.85% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0376 | -0.37 | 57% | 37 | -0.59% | ⚠️ flips / too few dates |
| true_ret | -0.0370 | -0.37 | 54% | 37 | -0.62% | ⚠️ flips / too few dates |
| Market Cap | +0.0370 | +0.56 | 69% | 39 | n/a | ✅ consistent |
| n_pos | -0.0355 | -0.42 | 64% | 39 | n/a | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0355 | -0.41 | 65% | 37 | -0.68% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0310 | +0.45 | 74% | 39 | n/a | ✅ consistent |
| d_Price | -0.0301 | -0.30 | 54% | 37 | -0.62% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0297 | -0.47 | 68% | 37 | -0.53% | ✅ consistent |
| w_pos | -0.0283 | -0.31 | 67% | 39 | n/a | ✅ consistent |
| d_Forward P/E | -0.0281 | -0.30 | 65% | 37 | -0.13% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16028428545751282.00 | 100% | 38 | -9.24% | ✅ consistent |
| short_fwd_3d | -0.7361 | -10.48 | 100% | 37 | -8.27% | ✅ consistent |
| short_fwd_1d | -0.6202 | -7.55 | 100% | 38 | -5.45% | ✅ consistent |
| Volatility (Month) | -0.0906 | -0.74 | 76% | 37 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0720 | +1.02 | 84% | 38 | n/a | ✅ consistent |
| exit_price_3d | +0.0665 | +1.04 | 81% | 37 | n/a | ✅ consistent |
| Profit Margin | +0.0630 | +0.70 | 76% | 38 | -4.54% | ✅ consistent |
| exit_price_1d | +0.0609 | +0.86 | 76% | 38 | n/a | ✅ consistent |
| valuation_score | -0.0572 | -0.77 | 71% | 38 | +1.62% | ✅ consistent |
| Average Volume | -0.0558 | -1.03 | 84% | 38 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0557 | +0.63 | 74% | 38 | -2.68% | ✅ consistent |
| Performance (YTD) | +0.0541 | +0.58 | 74% | 38 | -2.80% | ✅ consistent |
| upside_pct | -0.0535 | -0.40 | 58% | 38 | +1.53% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0535 | -0.40 | 58% | 38 | +1.53% | ⚠️ flips / too few dates |
| Price | +0.0496 | +0.69 | 74% | 38 | n/a | ✅ consistent |
| entry_price | +0.0496 | +0.69 | 74% | 38 | n/a | ✅ consistent |
| Market Cap | +0.0442 | +0.67 | 74% | 38 | n/a | ✅ consistent |
| n_pos | -0.0440 | -0.46 | 68% | 38 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0431 | -0.35 | 67% | 36 | -0.95% | ✅ consistent |
| d_Performance (Week) | -0.0430 | -0.32 | 61% | 36 | -0.54% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0417 | -0.32 | 61% | 36 | -1.04% | ⚠️ flips / too few dates |
| Beta | -0.0407 | -0.22 | 65% | 37 | -3.91% | ⚠️ flips / too few dates |
| w_pos | -0.0404 | -0.43 | 66% | 38 | n/a | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0393 | -0.32 | 58% | 36 | -0.77% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0389 | -0.38 | 64% | 36 | -1.42% | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0352 | +0.47 | 66% | 38 | n/a | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0352 | -0.28 | 64% | 36 | -1.30% | ⚠️ flips / too few dates |
| Short Float | -0.0346 | -0.35 | 63% | 38 | n/a | ⚠️ flips / too few dates |
| d_Price | -0.0345 | -0.27 | 61% | 36 | -1.27% | ⚠️ flips / too few dates |
| true_ret | -0.0335 | -0.27 | 58% | 36 | -1.27% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -18262884709889520.00 | 100% | 37 | -11.77% | ✅ consistent |
| short_fwd_2d | -0.7361 | -10.48 | 100% | 37 | -8.37% | ✅ consistent |
| short_fwd_1d | -0.4949 | -4.60 | 100% | 37 | -4.83% | ✅ consistent |
| Volatility (Month) | -0.1105 | -0.92 | 75% | 36 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0803 | +1.23 | 89% | 37 | n/a | ✅ consistent |
| Profit Margin | +0.0716 | +0.82 | 81% | 37 | -5.99% | ✅ consistent |
| exit_price_2d | +0.0711 | +1.07 | 89% | 37 | n/a | ✅ consistent |
| valuation_score | -0.0697 | -0.96 | 84% | 37 | +2.18% | ✅ consistent |
| Average Volume | -0.0675 | -1.30 | 84% | 37 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0623 | +0.66 | 70% | 37 | -3.64% | ✅ consistent |
| exit_price_1d | +0.0622 | +0.92 | 81% | 37 | n/a | ✅ consistent |
| upside_pct | -0.0615 | -0.48 | 70% | 37 | +2.06% | ✅ consistent |
| upside_pct_lvl | -0.0615 | -0.48 | 70% | 37 | +2.05% | ✅ consistent |
| Performance (YTD) | +0.0593 | +0.62 | 78% | 37 | -3.77% | ✅ consistent |
| Beta | -0.0532 | -0.30 | 61% | 36 | -5.47% | ⚠️ flips / too few dates |
| Price | +0.0526 | +0.77 | 73% | 37 | n/a | ✅ consistent |
| entry_price | +0.0526 | +0.77 | 73% | 37 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0482 | -0.32 | 71% | 35 | -0.40% | ✅ consistent |
| w_pos | -0.0459 | -0.42 | 70% | 37 | n/a | ✅ consistent |
| Market Cap | +0.0456 | +0.74 | 76% | 37 | n/a | ✅ consistent |
| Short Float | -0.0451 | -0.49 | 68% | 37 | n/a | ✅ consistent |
| n_pos | -0.0450 | -0.41 | 68% | 37 | n/a | ✅ consistent |
| Relative Strength Index (14) | +0.0430 | +0.50 | 62% | 37 | n/a | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0402 | +0.48 | 59% | 37 | -2.80% | ⚠️ flips / too few dates |
| Gross Margin | +0.0380 | +0.60 | 73% | 37 | -6.40% | ✅ consistent |
| Institutional Ownership | +0.0353 | +0.50 | 65% | 37 | n/a | ⚠️ flips / too few dates |
| Short Ratio | -0.0340 | -0.45 | 65% | 37 | n/a | ⚠️ flips / too few dates |
| EPS Surprise | +0.0339 | +0.69 | 68% | 37 | -0.37% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0339 | -0.25 | 63% | 35 | -0.79% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0331 | -0.25 | 71% | 35 | -1.06% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

