# Factor report — multi-date aggregate

_Generated 2026-08-19 17:18 EDT from 9 scan dates._

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
| 2026-08-17 | 2026-08-14 | 2026-08-18 | 2026-08-19 | — | 11559 |
| 2026-08-18 | 2026-08-17 | 2026-08-19 | — | — | 11572 |

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
| 2026-08-17 | -0.2097 | -0.1365 | — |
| 2026-08-18 | +0.0486 | — | — |
- **1d**: mean IC **-0.0031**, ICIR -0.03, sign consistency 56% over 9 dates
- **2d**: mean IC **-0.0483**, ICIR -0.58, sign consistency 62% over 8 dates
- **3d**: mean IC **-0.0258**, ICIR -0.25, sign consistency 57% over 7 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -27021597764222976.00 | 100% | 9 | -6.35% | ✅ consistent |
| short_fwd_2d | -0.5899 | -9.82 | 100% | 8 | -4.81% | ✅ consistent |
| short_fwd_3d | -0.4386 | -4.51 | 100% | 7 | -3.71% | ✅ consistent |
| d_Performance (Week) | -0.0662 | -0.59 | 62% | 8 | -1.48% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0651 | -0.46 | 62% | 8 | -2.62% | ⚠️ flips / too few dates |
| true_ret | -0.0573 | -0.57 | 62% | 8 | -1.78% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0572 | -0.54 | 62% | 8 | -2.07% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0572 | -0.54 | 62% | 8 | -1.96% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0550 | -0.50 | 75% | 8 | -2.27% | ✅ consistent |
| d_Performance (YTD) | -0.0531 | -0.51 | 62% | 8 | -1.77% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0525 | -0.39 | 75% | 8 | -0.30% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0479 | -0.51 | 62% | 8 | -1.67% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0466 | +1.02 | 86% | 7 | n/a | ✅ consistent |
| d_Market Cap | -0.0439 | -0.53 | 75% | 8 | -2.59% | ✅ consistent |
| Beta | -0.0437 | -0.29 | 50% | 8 | -0.76% | ⚠️ flips / too few dates |
| d_Price | -0.0430 | -0.39 | 62% | 8 | -1.78% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0412 | +0.91 | 75% | 8 | n/a | ✅ consistent |
| Gross Margin | +0.0368 | +0.46 | 56% | 9 | +0.24% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0346 | -0.29 | 67% | 9 | -2.82% | ✅ consistent |
| exit_price_1d | +0.0316 | +0.59 | 67% | 9 | n/a | ✅ consistent |
| Volatility (Month) | -0.0299 | -0.30 | 38% | 8 | +0.66% | ⚠️ flips / too few dates |
| Performance (Month) | -0.0292 | -0.34 | 67% | 9 | -2.27% | ✅ consistent |
| upside_pct_lvl | +0.0287 | +0.36 | 56% | 9 | +1.48% | ⚠️ flips / too few dates |
| upside_pct | +0.0287 | +0.36 | 56% | 9 | +1.49% | ⚠️ flips / too few dates |
| d_Beta | -0.0281 | -0.46 | 57% | 7 | -0.74% | ⚠️ flips / too few dates |
| Market Cap | +0.0276 | +0.89 | 78% | 9 | n/a | ✅ consistent |
| Performance (Quarter) | -0.0271 | -0.40 | 56% | 9 | -2.25% | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0270 | +0.66 | 71% | 7 | +0.63% | ✅ consistent |
| 20-Day Simple Moving Average | -0.0263 | -0.26 | 56% | 9 | -2.66% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0256 | +0.47 | 67% | 9 | -1.70% | ✅ consistent |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -18014398509481984.00 | 100% | 8 | -9.67% | ✅ consistent |
| short_fwd_3d | -0.6883 | -10.22 | 100% | 7 | -7.41% | ✅ consistent |
| short_fwd_1d | -0.5899 | -9.82 | 100% | 8 | -5.12% | ✅ consistent |
| d_Forward P/E | -0.1110 | -1.19 | 86% | 7 | -0.77% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0987 | -0.98 | 86% | 7 | -3.59% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0965 | -0.87 | 86% | 7 | -3.69% | ✅ consistent |
| true_ret | -0.0920 | -0.86 | 86% | 7 | -3.37% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0905 | -0.96 | 86% | 7 | -4.15% | ✅ consistent |
| d_Performance (YTD) | -0.0903 | -0.85 | 86% | 7 | -3.55% | ✅ consistent |
| d_Price | -0.0846 | -0.80 | 71% | 7 | -3.37% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0780 | -0.67 | 57% | 7 | -2.93% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0745 | -0.51 | 71% | 7 | -1.90% | ✅ consistent |
| d_Performance (Quarter) | -0.0728 | -0.63 | 57% | 7 | -3.60% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0706 | -0.77 | 57% | 7 | -2.66% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0702 | -0.98 | 86% | 7 | -5.42% | ✅ consistent |
| price_score | -0.0694 | -0.94 | 71% | 7 | -5.17% | ✅ consistent |
| exit_price_3d | +0.0628 | +1.37 | 100% | 7 | n/a | ✅ consistent |
| Beta | -0.0563 | -0.32 | 57% | 7 | -2.30% | ⚠️ flips / too few dates |
| n_pos | -0.0555 | -0.57 | 75% | 8 | n/a | ✅ consistent |
| Performance (Month) | -0.0492 | -0.72 | 75% | 8 | -4.53% | ✅ consistent |
| exit_price_2d | +0.0492 | +0.83 | 88% | 8 | n/a | ✅ consistent |
| total_score | -0.0483 | -0.58 | 62% | 8 | -2.65% | ⚠️ flips / too few dates |
| Gross Margin | +0.0459 | +0.55 | 62% | 8 | +0.14% | ⚠️ flips / too few dates |
| w_pos | -0.0436 | -0.46 | 50% | 8 | n/a | ⚠️ flips / too few dates |
| 20-Day Simple Moving Average | -0.0411 | -0.38 | 62% | 8 | -5.30% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0398 | -0.33 | 75% | 8 | -5.39% | ✅ consistent |
| Sales Year Over Year TTM | +0.0391 | +0.92 | 75% | 8 | -0.69% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0387 | +0.79 | 88% | 8 | -3.56% | ✅ consistent |
| Volatility (Month) | -0.0381 | -0.32 | 57% | 7 | +1.35% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0369 | +0.60 | 75% | 8 | n/a | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -16850926812823186.00 | 100% | 7 | -11.04% | ✅ consistent |
| short_fwd_2d | -0.6883 | -10.22 | 100% | 7 | -8.14% | ✅ consistent |
| short_fwd_1d | -0.4386 | -4.51 | 100% | 7 | -2.86% | ✅ consistent |
| d_Performance (Week) | -0.0941 | -0.66 | 83% | 6 | -0.64% | ✅ consistent |
| d_Performance (Month) | -0.0779 | -0.94 | 83% | 6 | -2.00% | ✅ consistent |
| d_Forward P/E | -0.0709 | -0.82 | 83% | 6 | -0.51% | ✅ consistent |
| Performance (YTD) | +0.0703 | +0.62 | 71% | 7 | -4.56% | ✅ consistent |
| exit_price_3d | +0.0679 | +1.20 | 86% | 7 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0639 | -0.45 | 67% | 6 | -2.94% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0617 | -0.46 | 67% | 6 | -3.06% | ✅ consistent |
| exit_price_2d | +0.0577 | +0.98 | 86% | 7 | n/a | ✅ consistent |
| price_score | -0.0573 | -0.62 | 67% | 6 | -3.98% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0566 | +1.26 | 86% | 7 | -4.01% | ✅ consistent |
| true_ret | -0.0566 | -0.42 | 67% | 6 | -3.12% | ✅ consistent |
| Sales Year Over Year TTM | +0.0535 | +1.29 | 86% | 7 | -1.03% | ✅ consistent |
| d_Performance (YTD) | -0.0530 | -0.38 | 67% | 6 | -3.19% | ✅ consistent |
| Beta | -0.0515 | -0.28 | 50% | 6 | -4.45% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0489 | +0.81 | 71% | 7 | n/a | ✅ consistent |
| d_Market Cap | -0.0484 | -0.69 | 83% | 6 | -4.75% | ✅ consistent |
| Performance (Month) | -0.0482 | -1.19 | 86% | 7 | -5.03% | ✅ consistent |
| Market Cap | +0.0466 | +1.14 | 86% | 7 | n/a | ✅ consistent |
| d_Price | -0.0461 | -0.33 | 67% | 6 | -3.12% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0453 | +0.46 | 57% | 7 | -4.66% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0445 | -0.45 | 67% | 6 | -3.86% | ✅ consistent |
| Profit Margin | +0.0442 | +0.57 | 86% | 7 | -9.53% | ✅ consistent |
| Volatility (Month) | -0.0436 | -0.36 | 50% | 6 | +1.51% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0431 | -0.34 | 67% | 6 | -1.97% | ✅ consistent |
| Analyst Recom | -0.0419 | -1.00 | 86% | 7 | n/a | ✅ consistent |
| Price | +0.0400 | +0.67 | 71% | 7 | n/a | ✅ consistent |
| entry_price | +0.0400 | +0.67 | 71% | 7 | n/a | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

