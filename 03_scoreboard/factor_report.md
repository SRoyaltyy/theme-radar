# Factor report — multi-date aggregate

_Generated 2026-08-11 03:42 EDT from 2 scan dates._

How to read: **IC** = Spearman rank correlation between the factor and the forward return, computed per scan date then averaged (mean IC). **ICIR** = mean/std across dates — the consistency score; |ICIR| above ~0.5 with sign consistency ≥ 2/3 is what we call a real signal. **spread** = average forward return when the factor is positive minus when negative. Factors marked ⚠️ flips sign between dates — treat as noise.

## Coverage (exact date spans)

| Scan date (features) | Deltas vs | 1d label | 2d label | 3d label | Stocks |
|---|---|---|---|---|---|
| 2026-08-06 | — | 2026-08-07 | 2026-08-10 | — | 11543 |
| 2026-08-07 | 2026-08-06 | 2026-08-10 | — | — | 11525 |

## Composite score effectiveness (total_score IC)

| Scan date | 1d IC | 2d IC | 3d IC |
|---|---|---|---|
| 2026-08-06 | +0.0958 | +0.0636 | — |
| 2026-08-07 | -0.0339 | — | — |
- **1d**: mean IC **+0.0309**, ICIR +0.48, sign consistency 50% over 2 dates
- **2d**: mean IC **+0.0636**, ICIR +nan, sign consistency 100% over 1 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| Beta | -0.1566 | +nan | 100% | 1 | +2.89% | ⚠️ flips / too few dates |
| Volatility (Month) | -0.1242 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.1212 | +nan | 100% | 1 | -7.72% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.1028 | +nan | 100% | 1 | -12.05% | ⚠️ flips / too few dates |
| Total Debt/Equity | -0.0936 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| Performance (Week) | +0.0910 | +0.64 | 50% | 2 | -7.80% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0875 | +nan | 100% | 1 | -15.17% | ⚠️ flips / too few dates |
| 20-Day Simple Moving Average | +0.0841 | +1.57 | 100% | 2 | -5.69% | ✅ consistent |
| true_ret | -0.0831 | +nan | 100% | 1 | -10.74% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0829 | +nan | 100% | 1 | -11.97% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0815 | +nan | 100% | 1 | -12.30% | ⚠️ flips / too few dates |
| upside_pct | +0.0807 | +1.09 | 100% | 2 | +2.39% | ✅ consistent |
| upside_pct_lvl | +0.0807 | +1.09 | 100% | 2 | +2.37% | ✅ consistent |
| d_Performance (YTD) | -0.0806 | +nan | 100% | 1 | -9.69% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0748 | +1.36 | 100% | 2 | +nan% | ✅ consistent |
| d_Price | -0.0688 | +nan | 100% | 1 | -10.74% | ⚠️ flips / too few dates |
| Analyst Recom | -0.0616 | -7.30 | 100% | 2 | +nan% | ✅ consistent |
| d_Forward P/E | -0.0614 | +nan | 100% | 1 | -0.30% | ⚠️ flips / too few dates |
| cat_copper_metals | +0.0550 | +9.39 | 100% | 2 | +nan% | ✅ consistent |
| d_Market Cap | -0.0548 | +nan | 100% | 1 | -14.67% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0527 | +5.10 | 100% | 2 | -1.79% | ✅ consistent |
| Performance (Month) | +0.0501 | +0.90 | 50% | 2 | -4.53% | ⚠️ flips / too few dates |
| Profit Margin | -0.0500 | -0.69 | 50% | 2 | -11.31% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0492 | +12.55 | 100% | 2 | +0.45% | ✅ consistent |
| Performance (YTD) | -0.0455 | -3.17 | 100% | 2 | -5.02% | ✅ consistent |
| n_neg | -0.0451 | -3.11 | 100% | 2 | +nan% | ✅ consistent |
| w_neg | -0.0431 | -4.64 | 100% | 2 | +nan% | ✅ consistent |
| Gross Margin | +0.0393 | +8.40 | 100% | 2 | -4.39% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0388 | +nan | 100% | 1 | -13.70% | ⚠️ flips / too few dates |
| d_Gross Margin | +0.0378 | +nan | 100% | 1 | +0.91% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.1820 | +nan | 100% | 1 | -9.34% | ⚠️ flips / too few dates |
| 20-Day Simple Moving Average | +0.1492 | +nan | 100% | 1 | -7.86% | ⚠️ flips / too few dates |
| upside_pct_lvl | +0.1357 | +nan | 100% | 1 | +3.84% | ⚠️ flips / too few dates |
| upside_pct | +0.1357 | +nan | 100% | 1 | +3.88% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.1102 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| Profit Margin | -0.1013 | +nan | 100% | 1 | -20.12% | ⚠️ flips / too few dates |
| Analyst Recom | -0.0965 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| technical_score | +0.0857 | +nan | 100% | 1 | -12.16% | ⚠️ flips / too few dates |
| cat_copper_metals | +0.0684 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| total_score | +0.0636 | +nan | 100% | 1 | -1.74% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0621 | +nan | 100% | 1 | -0.41% | ⚠️ flips / too few dates |
| w_pos | +0.0618 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| n_neg | -0.0590 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0584 | +nan | 100% | 1 | -2.52% | ⚠️ flips / too few dates |
| Performance (Month) | +0.0570 | +nan | 100% | 1 | -7.90% | ⚠️ flips / too few dates |
| Short Float | +0.0551 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| Institutional Ownership | -0.0503 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| n_pos | +0.0459 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| Performance (YTD) | -0.0440 | +nan | 100% | 1 | -8.70% | ⚠️ flips / too few dates |
| Performance (Quarter) | -0.0440 | +nan | 100% | 1 | -7.63% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0421 | +nan | 100% | 1 | -7.53% | ⚠️ flips / too few dates |
| w_neg | -0.0389 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| Target Price | -0.0387 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| Gross Margin | +0.0340 | +nan | 100% | 1 | -8.66% | ⚠️ flips / too few dates |
| cat_data_center_power | -0.0303 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| cat_defense | +0.0298 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | -0.0296 | +nan | 100% | 1 | -8.22% | ⚠️ flips / too few dates |
| catalyst_score | +0.0282 | +nan | 100% | 1 | -2.17% | ⚠️ flips / too few dates |
| n_catalysts | +0.0281 | +nan | 100% | 1 | +nan% | ⚠️ flips / too few dates |
| Institutional Transactions | +0.0251 | +nan | 100% | 1 | +10.87% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

