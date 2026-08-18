# Factor report — multi-date aggregate

_Generated 2026-08-18 17:16 EDT from 8 scan dates._

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
| 2026-08-14 | 2026-08-13 | 2026-08-17 | 2026-08-18 | — | 11551 |
| 2026-08-17 | 2026-08-14 | 2026-08-18 | — | — | 11559 |

## Composite score effectiveness (total_score IC)

| Scan date | 1d IC | 2d IC | 3d IC |
|---|---|---|---|
| 2026-08-06 | +0.0958 | +0.0636 | +0.0815 |
| 2026-08-07 | -0.0339 | -0.0242 | -0.0009 |
| 2026-08-10 | -0.0491 | -0.0596 | -0.1054 |
| 2026-08-11 | +0.1007 | +0.0174 | +0.0639 |
| 2026-08-12 | -0.0472 | +0.0520 | +0.0878 |
| 2026-08-13 | -0.0908 | -0.1428 | -0.1672 |
| 2026-08-14 | +0.1577 | -0.1560 | — |
| 2026-08-17 | -0.2097 | — | — |
- **1d**: mean IC **-0.0096**, ICIR -0.09, sign consistency 62% over 8 dates
- **2d**: mean IC **-0.0357**, ICIR -0.44, sign consistency 57% over 7 dates
- **3d**: mean IC **-0.0067**, ICIR -0.07, sign consistency 50% over 6 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -25476206690103088.00 | 100% | 8 | -6.40% | ✅ consistent |
| short_fwd_2d | -0.5854 | -9.30 | 100% | 7 | -4.48% | ✅ consistent |
| short_fwd_3d | -0.4597 | -5.16 | 100% | 6 | -3.98% | ✅ consistent |
| d_Performance (Week) | -0.0898 | -0.91 | 71% | 7 | -1.92% | ✅ consistent |
| d_Performance (Quarter) | -0.0849 | -0.60 | 71% | 7 | -3.25% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0815 | -0.90 | 71% | 7 | -2.60% | ✅ consistent |
| d_Forward P/E | -0.0811 | -0.68 | 86% | 7 | -0.45% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0788 | -0.81 | 86% | 7 | -2.82% | ✅ consistent |
| true_ret | -0.0776 | -0.85 | 71% | 7 | -2.26% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0769 | -0.78 | 71% | 7 | -2.46% | ✅ consistent |
| d_Performance (YTD) | -0.0752 | -0.81 | 71% | 7 | -2.25% | ✅ consistent |
| d_Price | -0.0671 | -0.69 | 71% | 7 | -2.26% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0666 | -0.79 | 71% | 7 | -2.15% | ✅ consistent |
| d_Market Cap | -0.0598 | -0.79 | 86% | 7 | -3.24% | ✅ consistent |
| Beta | -0.0583 | -0.37 | 57% | 7 | -1.05% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0477 | +1.06 | 86% | 7 | n/a | ✅ consistent |
| exit_price_3d | +0.0445 | +0.90 | 83% | 6 | n/a | ✅ consistent |
| exit_price_1d | +0.0427 | +0.92 | 75% | 8 | n/a | ✅ consistent |
| Volatility (Month) | -0.0391 | -0.38 | 43% | 7 | +0.34% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0366 | +0.77 | 75% | 8 | -1.85% | ✅ consistent |
| Performance (YTD) | +0.0349 | +0.32 | 50% | 8 | -2.18% | ⚠️ flips / too few dates |
| Performance (Month) | -0.0330 | -0.36 | 75% | 8 | -2.36% | ✅ consistent |
| n_pos | -0.0319 | -0.37 | 50% | 8 | n/a | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0315 | +0.76 | 75% | 8 | +0.09% | ✅ consistent |
| 20-Day Simple Moving Average | -0.0301 | -0.28 | 62% | 8 | -2.84% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | -0.0297 | -0.52 | 88% | 8 | -2.41% | ✅ consistent |
| Profit Margin | +0.0285 | +0.37 | 75% | 8 | -4.67% | ✅ consistent |
| Market Cap | +0.0278 | +0.84 | 75% | 8 | n/a | ✅ consistent |
| Gross Margin | +0.0277 | +0.34 | 50% | 8 | +0.24% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0274 | -0.22 | 62% | 8 | -3.04% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16850926812823186.00 | 100% | 7 | -9.24% | ✅ consistent |
| short_fwd_3d | -0.6872 | -9.46 | 100% | 6 | -7.16% | ✅ consistent |
| short_fwd_1d | -0.5854 | -9.30 | 100% | 7 | -3.97% | ✅ consistent |
| d_Forward P/E | -0.0994 | -1.04 | 83% | 6 | -0.67% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0970 | -0.81 | 83% | 6 | -3.50% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0939 | -0.87 | 83% | 6 | -3.35% | ✅ consistent |
| true_ret | -0.0885 | -0.77 | 83% | 6 | -3.09% | ✅ consistent |
| d_Performance (YTD) | -0.0872 | -0.76 | 83% | 6 | -3.31% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0851 | -0.84 | 83% | 6 | -4.02% | ✅ consistent |
| d_Price | -0.0820 | -0.72 | 67% | 6 | -3.09% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0791 | -0.63 | 50% | 6 | -2.70% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0707 | +0.84 | 57% | 7 | -3.57% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0686 | +1.45 | 100% | 6 | n/a | ✅ consistent |
| d_Market Cap | -0.0667 | -0.87 | 83% | 6 | -4.88% | ✅ consistent |
| exit_price_2d | +0.0644 | +1.38 | 100% | 7 | n/a | ✅ consistent |
| price_score | -0.0618 | -0.80 | 67% | 6 | -3.93% | ✅ consistent |
| d_Performance (Quarter) | -0.0593 | -0.50 | 50% | 6 | -2.42% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0574 | -0.38 | 67% | 6 | -1.23% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0537 | +1.76 | 100% | 7 | -2.42% | ✅ consistent |
| exit_price_1d | +0.0529 | +1.11 | 86% | 7 | n/a | ✅ consistent |
| n_pos | -0.0527 | -0.51 | 71% | 7 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0522 | -0.60 | 50% | 6 | -1.92% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0507 | +1.60 | 86% | 7 | -0.29% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0492 | +0.76 | 57% | 7 | -3.64% | ⚠️ flips / too few dates |
| Price | +0.0418 | +0.87 | 71% | 7 | n/a | ✅ consistent |
| entry_price | +0.0418 | +0.87 | 71% | 7 | n/a | ✅ consistent |
| Beta | -0.0400 | -0.22 | 50% | 6 | -3.15% | ⚠️ flips / too few dates |
| Analyst Recom | -0.0396 | -0.67 | 71% | 7 | n/a | ✅ consistent |
| Profit Margin | +0.0387 | +0.48 | 71% | 7 | -7.70% | ✅ consistent |
| Performance (Month) | -0.0378 | -0.58 | 71% | 7 | -3.96% | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -15600926743107926.00 | 100% | 6 | -10.59% | ✅ consistent |
| short_fwd_2d | -0.6872 | -9.46 | 100% | 6 | -7.17% | ✅ consistent |
| short_fwd_1d | -0.4597 | -5.16 | 100% | 6 | -3.19% | ✅ consistent |
| Performance (YTD) | +0.1069 | +1.41 | 83% | 6 | -4.28% | ✅ consistent |
| d_Performance (Week) | -0.1044 | -0.68 | 80% | 5 | -1.39% | ✅ consistent |
| exit_price_3d | +0.0825 | +1.74 | 100% | 6 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0756 | +1.11 | 67% | 6 | -4.39% | ✅ consistent |
| exit_price_2d | +0.0733 | +1.52 | 100% | 6 | n/a | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0713 | +2.48 | 100% | 6 | -2.81% | ✅ consistent |
| Sales Year Over Year TTM | +0.0681 | +3.00 | 100% | 6 | -0.68% | ✅ consistent |
| exit_price_1d | +0.0652 | +1.35 | 83% | 6 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0636 | -0.76 | 80% | 5 | -1.26% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0596 | -0.41 | 60% | 5 | -2.79% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0568 | -0.37 | 60% | 5 | -2.60% | ⚠️ flips / too few dates |
| Price | +0.0557 | +1.14 | 83% | 6 | n/a | ✅ consistent |
| entry_price | +0.0557 | +1.14 | 83% | 6 | n/a | ✅ consistent |
| d_Forward P/E | -0.0525 | -0.63 | 80% | 5 | -0.39% | ✅ consistent |
| Market Cap | +0.0486 | +1.11 | 83% | 6 | n/a | ✅ consistent |
| true_ret | -0.0484 | -0.33 | 60% | 5 | -3.24% | ⚠️ flips / too few dates |
| Analyst Recom | -0.0469 | -1.09 | 83% | 6 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0449 | -0.30 | 60% | 5 | -2.85% | ⚠️ flips / too few dates |
| price_score | -0.0439 | -0.46 | 60% | 5 | -3.99% | ⚠️ flips / too few dates |
| Profit Margin | +0.0431 | +0.52 | 83% | 6 | -9.07% | ✅ consistent |
| Performance (Month) | -0.0428 | -1.03 | 83% | 6 | -4.68% | ✅ consistent |
| Institutional Transactions | +0.0415 | +5.24 | 100% | 6 | +2.05% | ✅ consistent |
| d_Market Cap | -0.0407 | -0.54 | 80% | 5 | -3.71% | ✅ consistent |
| d_Performance (Quarter) | -0.0394 | -0.38 | 60% | 5 | -2.74% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0390 | -0.28 | 60% | 5 | -1.80% | ⚠️ flips / too few dates |
| d_Price | -0.0362 | -0.24 | 60% | 5 | -3.24% | ⚠️ flips / too few dates |
| Target Price | +0.0338 | +0.94 | 83% | 6 | n/a | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

