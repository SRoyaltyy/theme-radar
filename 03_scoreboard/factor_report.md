# Factor report — multi-date aggregate

_Generated 2026-08-12 04:22 EDT from 3 scan dates._

How to read: **IC** = Spearman rank correlation between the factor and the forward return, computed per scan date then averaged (mean IC). **ICIR** = mean/std across dates — the consistency score; |ICIR| above ~0.5 with sign consistency ≥ 2/3 is what we call a real signal. **spread** = average forward return when the factor is positive minus when negative. Factors marked ⚠️ flips sign between dates — treat as noise.

## Coverage (exact date spans)

| Scan date (features) | Deltas vs | 1d label | 2d label | 3d label | Stocks |
|---|---|---|---|---|---|
| 2026-08-06 | — | 2026-08-07 | 2026-08-10 | 2026-08-11 | 11543 |
| 2026-08-07 | 2026-08-06 | 2026-08-10 | 2026-08-11 | — | 11525 |
| 2026-08-10 | 2026-08-07 | 2026-08-11 | — | — | 11533 |

## Composite score effectiveness (total_score IC)

| Scan date | 1d IC | 2d IC | 3d IC |
|---|---|---|---|
| 2026-08-06 | +0.0958 | +0.0636 | +0.0815 |
| 2026-08-07 | -0.0339 | -0.0242 | — |
| 2026-08-10 | -0.0491 | — | — |
- **1d**: mean IC **+0.0042**, ICIR +0.07, sign consistency 33% over 3 dates
- **2d**: mean IC **+0.0197**, ICIR +0.45, sign consistency 50% over 2 dates
- **3d**: mean IC **+0.0815**, ICIR +nan, sign consistency 100% over 1 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -15600926743107926.00 | 100% | 3 | -7.48% | ✅ consistent |
| short_fwd_2d | -0.6321 | -17.54 | 100% | 2 | -7.46% | ✅ consistent |
| short_fwd_3d | -0.5348 | +nan | 100% | 1 | -3.77% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.1012 | -5.06 | 100% | 2 | -3.60% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0955 | -13.16 | 100% | 2 | -5.89% | ✅ consistent |
| d_Performance (YTD) | -0.0926 | -7.68 | 100% | 2 | -4.75% | ✅ consistent |
| true_ret | -0.0916 | -10.81 | 100% | 2 | -5.25% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0889 | -11.97 | 100% | 2 | -6.03% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0856 | -31.36 | 100% | 2 | -5.86% | ✅ consistent |
| d_Price | -0.0853 | -5.17 | 100% | 2 | -5.25% | ✅ consistent |
| upside_pct | +0.0735 | +1.20 | 100% | 3 | +1.82% | ✅ consistent |
| upside_pct_lvl | +0.0735 | +1.20 | 100% | 3 | +1.81% | ✅ consistent |
| Performance (Week) | +0.0623 | +0.51 | 67% | 3 | -5.20% | ✅ consistent |
| Total Debt/Equity | -0.0590 | -1.71 | 100% | 2 | n/a | ✅ consistent |
| Analyst Recom | -0.0582 | -6.94 | 100% | 3 | n/a | ✅ consistent |
| d_Performance (Quarter) | -0.0559 | -1.77 | 100% | 2 | -7.33% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0553 | -3.35 | 100% | 2 | -6.75% | ✅ consistent |
| Beta | -0.0534 | -0.52 | 50% | 2 | +1.57% | ⚠️ flips / too few dates |
| Profit Margin | -0.0504 | -0.86 | 67% | 3 | -8.02% | ✅ consistent |
| d_Forward P/E | -0.0491 | -3.99 | 100% | 2 | -0.24% | ✅ consistent |
| 20-Day Simple Moving Average | +0.0457 | +0.66 | 67% | 3 | -3.95% | ✅ consistent |
| d_Market Cap | -0.0444 | -4.28 | 100% | 2 | -6.97% | ✅ consistent |
| d_Volatility (Month) | +0.0440 | +nan | 100% | 1 | +0.20% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0438 | +2.89 | 100% | 3 | -1.04% | ✅ consistent |
| Short Float | +0.0428 | +0.42 | 67% | 3 | n/a | ✅ consistent |
| Sales Year Over Year TTM | +0.0421 | +3.96 | 100% | 3 | +0.44% | ✅ consistent |
| price_score | -0.0403 | -1.69 | 100% | 2 | -6.20% | ✅ consistent |
| catalyst_score | +0.0386 | +1.02 | 67% | 3 | -0.75% | ✅ consistent |
| n_catalysts | +0.0385 | +1.02 | 67% | 3 | n/a | ✅ consistent |
| d_Institutional Ownership | +0.0339 | +1.52 | 100% | 2 | +0.45% | ✅ consistent |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | +nan | 100% | 2 | -12.48% | ✅ consistent |
| short_fwd_3d | -0.7888 | +nan | 100% | 1 | -10.37% | ⚠️ flips / too few dates |
| short_fwd_1d | -0.6321 | -17.54 | 100% | 2 | -5.04% | ✅ consistent |
| Beta | -0.0989 | +nan | 100% | 1 | +3.12% | ⚠️ flips / too few dates |
| Total Debt/Equity | -0.0901 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| upside_pct_lvl | +0.0885 | +1.87 | 100% | 2 | +3.52% | ✅ consistent |
| upside_pct | +0.0885 | +1.87 | 100% | 2 | +3.55% | ✅ consistent |
| d_Price | -0.0872 | +nan | 100% | 1 | -11.85% | ⚠️ flips / too few dates |
| Analyst Recom | -0.0827 | -5.99 | 100% | 2 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0814 | +nan | 100% | 1 | -7.20% | ⚠️ flips / too few dates |
| Performance (Week) | +0.0814 | +0.81 | 50% | 2 | -12.18% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0811 | +2.79 | 100% | 2 | n/a | ✅ consistent |
| 20-Day Simple Moving Average | +0.0787 | +1.11 | 100% | 2 | -9.15% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0772 | +nan | 100% | 1 | -12.55% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0758 | +nan | 100% | 1 | -13.15% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0733 | +nan | 100% | 1 | -12.98% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0713 | +nan | 100% | 1 | -10.32% | ⚠️ flips / too few dates |
| true_ret | -0.0711 | +nan | 100% | 1 | -11.85% | ⚠️ flips / too few dates |
| Profit Margin | -0.0641 | -1.72 | 100% | 2 | -19.90% | ✅ consistent |
| Sales Growth Quarter Over Quarter | +0.0571 | +42.78 | 100% | 2 | -2.45% | ✅ consistent |
| Sales Year Over Year TTM | +0.0529 | +5.82 | 100% | 2 | +0.82% | ✅ consistent |
| Performance (Month) | +0.0525 | +11.75 | 100% | 2 | -7.82% | ✅ consistent |
| Institutional Ownership | -0.0522 | -26.39 | 100% | 2 | n/a | ✅ consistent |
| cat_copper_metals | +0.0474 | +2.25 | 100% | 2 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0437 | +nan | 100% | 1 | -14.56% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0424 | +nan | 100% | 1 | -15.47% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0368 | +6.90 | 100% | 2 | -7.81% | ✅ consistent |
| n_neg | -0.0318 | -1.17 | 100% | 2 | n/a | ✅ consistent |
| d_Market Cap | -0.0317 | +nan | 100% | 1 | -14.90% | ⚠️ flips / too few dates |
| d_Gross Margin | +0.0309 | +nan | 100% | 1 | +0.85% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | +nan | 100% | 1 | -12.49% | ⚠️ flips / too few dates |
| short_fwd_2d | -0.7888 | +nan | 100% | 1 | -11.09% | ⚠️ flips / too few dates |
| short_fwd_1d | -0.5348 | +nan | 100% | 1 | +4.15% | ⚠️ flips / too few dates |
| Performance (Week) | +0.2028 | +nan | 100% | 1 | -9.54% | ⚠️ flips / too few dates |
| upside_pct | +0.1338 | +nan | 100% | 1 | +4.20% | ⚠️ flips / too few dates |
| upside_pct_lvl | +0.1337 | +nan | 100% | 1 | +4.16% | ⚠️ flips / too few dates |
| 20-Day Simple Moving Average | +0.1224 | +nan | 100% | 1 | -8.29% | ⚠️ flips / too few dates |
| Profit Margin | -0.1143 | +nan | 100% | 1 | -21.36% | ⚠️ flips / too few dates |
| Analyst Recom | -0.1084 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| w_pos | +0.0836 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| total_score | +0.0815 | +nan | 100% | 1 | -1.78% | ⚠️ flips / too few dates |
| technical_score | +0.0757 | +nan | 100% | 1 | -12.71% | ⚠️ flips / too few dates |
| n_pos | +0.0743 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| Short Float | +0.0737 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| n_neg | -0.0658 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0643 | +nan | 100% | 1 | -2.04% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0623 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0607 | +nan | 100% | 1 | +0.16% | ⚠️ flips / too few dates |
| cat_copper_metals | +0.0591 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| Performance (Quarter) | -0.0537 | +nan | 100% | 1 | -8.14% | ⚠️ flips / too few dates |
| catalyst_score | +0.0531 | +nan | 100% | 1 | -1.56% | ⚠️ flips / too few dates |
| n_catalysts | +0.0530 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| valuation_score | +0.0525 | +nan | 100% | 1 | +4.54% | ⚠️ flips / too few dates |
| w_neg | -0.0486 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| Institutional Transactions | +0.0453 | +nan | 100% | 1 | +10.78% | ⚠️ flips / too few dates |
| Forward P/E | +0.0449 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| Institutional Ownership | -0.0432 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| Target Price | -0.0376 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| Average Volume | +0.0372 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |
| cat_defense | +0.0372 | +nan | 100% | 1 | n/a | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

