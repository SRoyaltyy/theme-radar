# Factor report — multi-date aggregate

_Generated 2026-08-14 17:17 EDT from 6 scan dates._

How to read: **IC** = Spearman rank correlation between the factor and the forward return, computed per scan date then averaged (mean IC). **ICIR** = mean/std across dates — the consistency score; |ICIR| above ~0.5 with sign consistency ≥ 2/3 is what we call a real signal. **spread** = average forward return when the factor is positive minus when negative. Factors marked ⚠️ flips sign between dates — treat as noise.

## Coverage (exact date spans)

| Scan date (features) | Deltas vs | 1d label | 2d label | 3d label | Stocks |
|---|---|---|---|---|---|
| 2026-08-06 | — | 2026-08-07 | 2026-08-10 | 2026-08-11 | 11543 |
| 2026-08-07 | 2026-08-06 | 2026-08-10 | 2026-08-11 | 2026-08-12 | 11525 |
| 2026-08-10 | 2026-08-07 | 2026-08-11 | 2026-08-12 | 2026-08-13 | 11533 |
| 2026-08-11 | 2026-08-10 | 2026-08-12 | 2026-08-13 | 2026-08-14 | 11543 |
| 2026-08-12 | 2026-08-11 | 2026-08-13 | 2026-08-14 | — | 11553 |
| 2026-08-13 | 2026-08-12 | 2026-08-14 | — | — | 11566 |

## Composite score effectiveness (total_score IC)

| Scan date | 1d IC | 2d IC | 3d IC |
|---|---|---|---|
| 2026-08-06 | +0.0958 | +0.0636 | +0.0815 |
| 2026-08-07 | -0.0339 | -0.0242 | -0.0009 |
| 2026-08-10 | -0.0491 | -0.0596 | -0.1054 |
| 2026-08-11 | +0.1007 | +0.0174 | +0.0639 |
| 2026-08-12 | -0.0472 | +0.0520 | — |
| 2026-08-13 | -0.0908 | — | — |
- **1d**: mean IC **-0.0041**, ICIR -0.05, sign consistency 67% over 6 dates
- **2d**: mean IC **+0.0098**, ICIR +0.21, sign consistency 60% over 5 dates
- **3d**: mean IC **+0.0098**, ICIR +0.13, sign consistency 50% over 4 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -22063042185692344.00 | 100% | 6 | -5.96% | ✅ consistent |
| short_fwd_2d | -0.6106 | -20.69 | 100% | 5 | -4.78% | ✅ consistent |
| short_fwd_3d | -0.5105 | -9.71 | 100% | 4 | -4.36% | ✅ consistent |
| d_Forward P/E | -0.0936 | -1.05 | 100% | 5 | -0.41% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0908 | -1.06 | 80% | 5 | -2.77% | ✅ consistent |
| d_Performance (Week) | -0.0878 | -0.99 | 80% | 5 | -1.67% | ✅ consistent |
| true_ret | -0.0864 | -1.01 | 80% | 5 | -2.36% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0848 | -1.02 | 80% | 5 | -2.57% | ✅ consistent |
| d_Performance (YTD) | -0.0831 | -0.99 | 80% | 5 | -2.28% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0803 | -0.91 | 80% | 5 | -2.36% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0775 | -0.94 | 100% | 5 | -3.08% | ✅ consistent |
| d_Price | -0.0711 | -0.83 | 80% | 5 | -2.36% | ✅ consistent |
| d_Market Cap | -0.0686 | -1.21 | 100% | 5 | -3.19% | ✅ consistent |
| d_Performance (Quarter) | -0.0664 | -0.81 | 80% | 5 | -3.04% | ✅ consistent |
| exit_price_1d | +0.0472 | +0.97 | 83% | 6 | n/a | ✅ consistent |
| Performance (YTD) | +0.0466 | +0.46 | 50% | 6 | -2.08% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0457 | +0.87 | 80% | 5 | n/a | ✅ consistent |
| Sales Year Over Year TTM | +0.0434 | +1.78 | 83% | 6 | -0.28% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0428 | +1.39 | 83% | 6 | -0.86% | ✅ consistent |
| upside_pct_lvl | +0.0413 | +0.57 | 67% | 6 | +1.31% | ✅ consistent |
| upside_pct | +0.0413 | +0.57 | 67% | 6 | +1.31% | ✅ consistent |
| exit_price_3d | +0.0412 | +0.69 | 75% | 4 | n/a | ✅ consistent |
| Analyst Recom | -0.0341 | -0.54 | 83% | 6 | n/a | ✅ consistent |
| Short Float | +0.0316 | +0.43 | 83% | 6 | n/a | ✅ consistent |
| Price | +0.0308 | +0.63 | 67% | 6 | n/a | ✅ consistent |
| entry_price | +0.0308 | +0.63 | 67% | 6 | n/a | ✅ consistent |
| Market Cap | +0.0303 | +0.95 | 83% | 6 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0300 | +0.42 | 50% | 6 | -2.11% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | -0.0294 | -0.44 | 83% | 6 | -2.27% | ✅ consistent |
| price_score | -0.0270 | -0.35 | 80% | 5 | -2.52% | ✅ consistent |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -14241632491976356.00 | 100% | 5 | -8.64% | ✅ consistent |
| short_fwd_3d | -0.7335 | -19.13 | 100% | 4 | -7.73% | ✅ consistent |
| short_fwd_1d | -0.6106 | -20.69 | 100% | 5 | -4.23% | ✅ consistent |
| Performance (YTD) | +0.0711 | +0.87 | 60% | 5 | -3.97% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0705 | +1.36 | 100% | 5 | n/a | ✅ consistent |
| exit_price_3d | +0.0622 | +1.11 | 100% | 4 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0605 | +0.90 | 60% | 5 | -3.98% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0600 | +1.15 | 80% | 5 | n/a | ✅ consistent |
| Beta | +0.0598 | +0.63 | 75% | 4 | -1.97% | ✅ consistent |
| d_Performance (Week) | -0.0592 | -0.47 | 75% | 4 | -2.22% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0570 | -0.74 | 75% | 4 | -3.69% | ✅ consistent |
| Sales Year Over Year TTM | +0.0559 | +5.93 | 100% | 5 | +0.01% | ✅ consistent |
| d_Forward P/E | -0.0550 | -1.20 | 75% | 4 | -0.43% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0515 | -0.72 | 75% | 4 | -3.47% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0507 | +4.51 | 100% | 5 | -1.35% | ✅ consistent |
| Price | +0.0478 | +0.89 | 60% | 5 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0478 | +0.89 | 60% | 5 | n/a | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0477 | -0.59 | 75% | 4 | -3.33% | ✅ consistent |
| true_ret | -0.0465 | -0.62 | 75% | 4 | -3.67% | ✅ consistent |
| d_Price | -0.0442 | -0.50 | 50% | 4 | -3.67% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0423 | -0.53 | 50% | 4 | -3.36% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0402 | -0.83 | 75% | 4 | -4.40% | ✅ consistent |
| Volatility (Month) | +0.0386 | +0.88 | 75% | 4 | n/a | ✅ consistent |
| d_Performance (Quarter) | -0.0382 | -0.54 | 50% | 4 | -3.92% | ⚠️ flips / too few dates |
| Short Float | +0.0382 | +0.99 | 80% | 5 | n/a | ✅ consistent |
| d_Market Cap | -0.0381 | -1.05 | 75% | 4 | -4.71% | ✅ consistent |
| Market Cap | +0.0377 | +0.80 | 80% | 5 | n/a | ✅ consistent |
| Analyst Recom | -0.0310 | -0.54 | 60% | 5 | n/a | ⚠️ flips / too few dates |
| upside_pct_lvl | +0.0298 | +0.45 | 80% | 5 | +2.13% | ✅ consistent |
| upside_pct | +0.0298 | +0.45 | 80% | 5 | +2.14% | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -12738103345051544.00 | 100% | 4 | -10.09% | ✅ consistent |
| short_fwd_2d | -0.7335 | -19.13 | 100% | 4 | -8.25% | ✅ consistent |
| short_fwd_1d | -0.5105 | -9.71 | 100% | 4 | -3.37% | ✅ consistent |
| d_Performance (Week) | -0.1329 | -1.86 | 100% | 3 | -2.52% | ✅ consistent |
| Performance (YTD) | +0.1093 | +1.40 | 75% | 4 | -4.72% | ✅ consistent |
| exit_price_3d | +0.0868 | +1.76 | 100% | 4 | n/a | ✅ consistent |
| Beta | +0.0841 | +1.05 | 67% | 3 | -2.27% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0829 | +1.28 | 75% | 4 | -4.79% | ✅ consistent |
| exit_price_2d | +0.0785 | +1.60 | 100% | 4 | n/a | ✅ consistent |
| Sales Year Over Year TTM | +0.0713 | +5.72 | 100% | 4 | +0.11% | ✅ consistent |
| exit_price_1d | +0.0697 | +1.39 | 75% | 4 | n/a | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0677 | +2.95 | 100% | 4 | -1.44% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0657 | -0.72 | 67% | 3 | -4.54% | ✅ consistent |
| d_Forward P/E | -0.0614 | -3.26 | 100% | 3 | -0.53% | ✅ consistent |
| Volatility (Month) | +0.0588 | +1.85 | 100% | 3 | n/a | ✅ consistent |
| Price | +0.0588 | +1.15 | 75% | 4 | n/a | ✅ consistent |
| entry_price | +0.0588 | +1.15 | 75% | 4 | n/a | ✅ consistent |
| d_Performance (Quarter) | -0.0576 | -0.62 | 67% | 3 | -5.21% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0569 | -0.60 | 67% | 3 | -4.41% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0567 | -0.87 | 67% | 3 | -5.04% | ✅ consistent |
| true_ret | -0.0528 | -0.58 | 67% | 3 | -4.20% | ✅ consistent |
| d_Market Cap | -0.0520 | -1.24 | 100% | 3 | -5.47% | ✅ consistent |
| d_Performance (YTD) | -0.0495 | -0.50 | 67% | 3 | -3.91% | ✅ consistent |
| d_Price | -0.0469 | -0.46 | 67% | 3 | -4.20% | ✅ consistent |
| Short Float | +0.0468 | +1.11 | 75% | 4 | n/a | ✅ consistent |
| Analyst Recom | -0.0444 | -0.86 | 75% | 4 | n/a | ✅ consistent |
| Market Cap | +0.0432 | +0.96 | 75% | 4 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0426 | -0.44 | 67% | 3 | -4.17% | ✅ consistent |
| d_Performance (Month) | -0.0418 | -0.56 | 67% | 3 | -2.23% | ✅ consistent |
| catalyst_score | +0.0408 | +3.15 | 100% | 4 | +0.04% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

