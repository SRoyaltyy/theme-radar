# Factor report — multi-date aggregate

_Generated 2026-08-17 17:18 EDT from 7 scan dates._

How to read: **IC** = Spearman rank correlation between the factor and the forward return, computed per scan date then averaged (mean IC). **ICIR** = mean/std across dates — the consistency score; |ICIR| above ~0.5 with sign consistency ≥ 2/3 is what we call a real signal. **spread** = average forward return when the factor is positive minus when negative. Factors marked ⚠️ flips sign between dates — treat as noise.

## Coverage (exact date spans)

| Scan date (features) | Deltas vs | 1d label | 2d label | 3d label | Stocks |
|---|---|---|---|---|---|
| 2026-08-06 | — | 2026-08-07 | 2026-08-10 | 2026-08-11 | 11543 |
| 2026-08-07 | 2026-08-06 | 2026-08-10 | 2026-08-11 | 2026-08-12 | 11525 |
| 2026-08-10 | 2026-08-07 | 2026-08-11 | 2026-08-12 | 2026-08-13 | 11533 |
| 2026-08-11 | 2026-08-10 | 2026-08-12 | 2026-08-13 | 2026-08-14 | 11543 |
| 2026-08-12 | 2026-08-11 | 2026-08-13 | 2026-08-14 | 2026-08-17 | 11553 |
| 2026-08-13 | 2026-08-12 | 2026-08-14 | 2026-08-17 | — | 11566 |
| 2026-08-14 | 2026-08-13 | 2026-08-17 | — | — | 11551 |

## Composite score effectiveness (total_score IC)

| Scan date | 1d IC | 2d IC | 3d IC |
|---|---|---|---|
| 2026-08-06 | +0.0958 | +0.0636 | +0.0815 |
| 2026-08-07 | -0.0339 | -0.0242 | -0.0009 |
| 2026-08-10 | -0.0491 | -0.0596 | -0.1054 |
| 2026-08-11 | +0.1007 | +0.0174 | +0.0639 |
| 2026-08-12 | -0.0472 | +0.0520 | +0.0878 |
| 2026-08-13 | -0.0908 | -0.1428 | — |
| 2026-08-14 | +0.1577 | — | — |
- **1d**: mean IC **+0.0190**, ICIR +0.21, sign consistency 43% over 7 dates
- **2d**: mean IC **-0.0156**, ICIR -0.22, sign consistency 50% over 6 dates
- **3d**: mean IC **+0.0254**, ICIR +0.35, sign consistency 60% over 5 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -23830809237250984.00 | 100% | 7 | -5.77% | ✅ consistent |
| short_fwd_2d | -0.6090 | -22.40 | 100% | 6 | -4.65% | ✅ consistent |
| short_fwd_3d | -0.4695 | -4.97 | 100% | 5 | -3.93% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0689 | -0.75 | 67% | 6 | -2.35% | ✅ consistent |
| d_Performance (Week) | -0.0688 | -0.75 | 67% | 6 | -1.45% | ✅ consistent |
| true_ret | -0.0642 | -0.70 | 67% | 6 | -1.94% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0620 | -0.68 | 67% | 6 | -1.90% | ✅ consistent |
| d_Performance (YTD) | -0.0605 | -0.66 | 67% | 6 | -1.93% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0589 | -0.62 | 67% | 6 | -2.18% | ✅ consistent |
| d_Forward P/E | -0.0580 | -0.51 | 83% | 6 | -0.28% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0574 | -0.65 | 83% | 6 | -2.61% | ✅ consistent |
| Performance (YTD) | +0.0572 | +0.59 | 57% | 7 | -1.78% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0500 | +1.49 | 86% | 7 | -0.62% | ✅ consistent |
| exit_price_1d | +0.0496 | +1.10 | 86% | 7 | n/a | ✅ consistent |
| d_Price | -0.0489 | -0.53 | 67% | 6 | -1.94% | ✅ consistent |
| exit_price_2d | +0.0459 | +0.95 | 83% | 6 | n/a | ✅ consistent |
| d_Market Cap | -0.0458 | -0.63 | 83% | 6 | -2.75% | ✅ consistent |
| Sales Year Over Year TTM | +0.0448 | +1.96 | 86% | 7 | -0.13% | ✅ consistent |
| exit_price_3d | +0.0445 | +0.83 | 80% | 5 | n/a | ✅ consistent |
| d_Performance (Month) | +0.0401 | +0.35 | 50% | 6 | -0.74% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0397 | -0.41 | 67% | 6 | -2.44% | ✅ consistent |
| Analyst Recom | -0.0385 | -0.64 | 86% | 7 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0343 | +0.51 | 57% | 7 | -1.83% | ⚠️ flips / too few dates |
| Market Cap | +0.0339 | +1.10 | 86% | 7 | n/a | ✅ consistent |
| Price | +0.0334 | +0.73 | 71% | 7 | n/a | ✅ consistent |
| entry_price | +0.0334 | +0.73 | 71% | 7 | n/a | ✅ consistent |
| upside_pct_lvl | +0.0325 | +0.46 | 57% | 7 | +1.15% | ⚠️ flips / too few dates |
| upside_pct | +0.0325 | +0.46 | 57% | 7 | +1.15% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | -0.0285 | -0.46 | 86% | 7 | -2.03% | ✅ consistent |
| Performance (Quarter) | -0.0283 | -0.38 | 57% | 7 | -1.91% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -15600926743107926.00 | 100% | 6 | -8.42% | ✅ consistent |
| short_fwd_3d | -0.7074 | -11.33 | 100% | 5 | -7.18% | ✅ consistent |
| short_fwd_1d | -0.6090 | -22.40 | 100% | 6 | -4.31% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.1101 | -0.87 | 80% | 5 | -3.49% | ✅ consistent |
| d_Forward P/E | -0.1031 | -0.99 | 80% | 5 | -0.73% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.1006 | -0.86 | 80% | 5 | -3.28% | ✅ consistent |
| true_ret | -0.0983 | -0.80 | 80% | 5 | -3.43% | ✅ consistent |
| d_Performance (YTD) | -0.0976 | -0.79 | 80% | 5 | -3.23% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0970 | -0.74 | 60% | 5 | -2.76% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0967 | -0.71 | 80% | 5 | -1.93% | ✅ consistent |
| d_Price | -0.0915 | -0.74 | 60% | 5 | -3.43% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0906 | -0.83 | 80% | 5 | -4.08% | ✅ consistent |
| Performance (YTD) | +0.0860 | +1.06 | 67% | 6 | -3.48% | ✅ consistent |
| d_Performance (Quarter) | -0.0852 | -0.75 | 60% | 5 | -3.33% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0754 | -0.93 | 80% | 5 | -4.40% | ✅ consistent |
| exit_price_2d | +0.0709 | +1.49 | 100% | 6 | n/a | ✅ consistent |
| exit_price_3d | +0.0689 | +1.33 | 100% | 5 | n/a | ✅ consistent |
| Sales Year Over Year TTM | +0.0621 | +3.79 | 100% | 6 | -0.57% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0619 | +1.00 | 67% | 6 | -3.54% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0614 | +2.37 | 100% | 6 | -1.22% | ✅ consistent |
| exit_price_1d | +0.0602 | +1.27 | 83% | 6 | n/a | ✅ consistent |
| Price | +0.0483 | +0.99 | 67% | 6 | n/a | ✅ consistent |
| entry_price | +0.0483 | +0.99 | 67% | 6 | n/a | ✅ consistent |
| Analyst Recom | -0.0456 | -0.74 | 67% | 6 | n/a | ✅ consistent |
| price_score | -0.0449 | -0.61 | 60% | 5 | -4.02% | ⚠️ flips / too few dates |
| Market Cap | +0.0427 | +0.96 | 83% | 6 | n/a | ✅ consistent |
| Institutional Transactions | +0.0362 | +1.20 | 83% | 6 | +2.74% | ✅ consistent |
| upside_pct_lvl | +0.0349 | +0.57 | 83% | 6 | +2.09% | ✅ consistent |
| upside_pct | +0.0349 | +0.57 | 83% | 6 | +2.09% | ✅ consistent |
| Beta | +0.0316 | +0.31 | 60% | 5 | -3.09% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -14241632491976356.00 | 100% | 5 | -9.55% | ✅ consistent |
| short_fwd_2d | -0.7074 | -11.33 | 100% | 5 | -7.61% | ✅ consistent |
| short_fwd_1d | -0.4695 | -4.97 | 100% | 5 | -3.13% | ✅ consistent |
| Performance (YTD) | +0.1221 | +1.64 | 80% | 5 | -4.14% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0929 | +1.51 | 80% | 5 | -4.25% | ✅ consistent |
| exit_price_3d | +0.0926 | +2.03 | 100% | 5 | n/a | ✅ consistent |
| exit_price_2d | +0.0843 | +1.86 | 100% | 5 | n/a | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0772 | +2.76 | 100% | 5 | -1.36% | ✅ consistent |
| Sales Year Over Year TTM | +0.0762 | +5.12 | 100% | 5 | -0.40% | ✅ consistent |
| exit_price_1d | +0.0758 | +1.63 | 80% | 5 | n/a | ✅ consistent |
| Beta | +0.0708 | +0.97 | 75% | 4 | -4.37% | ✅ consistent |
| Price | +0.0657 | +1.38 | 80% | 5 | n/a | ✅ consistent |
| entry_price | +0.0657 | +1.38 | 80% | 5 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0603 | -0.43 | 75% | 4 | -1.88% | ✅ consistent |
| Market Cap | +0.0541 | +1.18 | 80% | 5 | n/a | ✅ consistent |
| Performance (Week) | +0.0458 | +0.40 | 80% | 5 | -5.53% | ✅ consistent |
| Analyst Recom | -0.0433 | -0.94 | 80% | 5 | n/a | ✅ consistent |
| Institutional Transactions | +0.0417 | +4.83 | 100% | 5 | +3.10% | ✅ consistent |
| Volatility (Month) | +0.0364 | +0.77 | 75% | 4 | n/a | ✅ consistent |
| technical_score | +0.0361 | +0.65 | 80% | 5 | -8.36% | ✅ consistent |
| Insider Transactions | -0.0357 | -1.48 | 100% | 5 | -1.02% | ✅ consistent |
| catalyst_score | +0.0357 | +2.31 | 100% | 5 | -0.04% | ✅ consistent |
| n_catalysts | +0.0357 | +2.30 | 100% | 5 | n/a | ✅ consistent |
| Short Float | +0.0346 | +0.77 | 60% | 5 | n/a | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0346 | +0.65 | 60% | 5 | n/a | ⚠️ flips / too few dates |
| Performance (Month) | -0.0345 | -0.85 | 80% | 5 | -4.53% | ✅ consistent |
| d_Performance (Month) | -0.0340 | -0.52 | 75% | 4 | -1.78% | ✅ consistent |
| 50-Day Simple Moving Average | -0.0336 | -0.96 | 100% | 5 | -4.79% | ✅ consistent |
| Target Price | +0.0319 | +0.82 | 80% | 5 | n/a | ✅ consistent |
| 20-Day Simple Moving Average | +0.0316 | +0.57 | 60% | 5 | -4.92% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

