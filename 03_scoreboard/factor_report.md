# Factor report — multi-date aggregate

_Generated 2026-08-26 20:22 EDT from 14 scan dates._

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
| 2026-08-24 | 2026-08-21 | 2026-08-25 | 2026-08-26 | — | 11605 |
| 2026-08-25 | 2026-08-24 | 2026-08-26 | — | — | 11611 |

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
| 2026-08-24 | +0.0056 | -0.0285 | — |
| 2026-08-25 | -0.0503 | — | — |
- **1d**: mean IC **-0.0102**, ICIR -0.11, sign consistency 57% over 14 dates
- **2d**: mean IC **-0.0205**, ICIR -0.27, sign consistency 46% over 13 dates
- **3d**: mean IC **-0.0112**, ICIR -0.11, sign consistency 50% over 12 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -23830809237250984.00 | 100% | 14 | -5.84% | ✅ consistent |
| short_fwd_2d | -0.6070 | -9.70 | 100% | 13 | -4.56% | ✅ consistent |
| short_fwd_3d | -0.4963 | -4.55 | 100% | 12 | -4.21% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0821 | -0.81 | 69% | 13 | -1.00% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0813 | -0.79 | 69% | 13 | -1.04% | ✅ consistent |
| true_ret | -0.0808 | -0.81 | 69% | 13 | -1.02% | ✅ consistent |
| d_Performance (Quarter) | -0.0773 | -0.65 | 69% | 13 | -1.11% | ✅ consistent |
| d_Performance (YTD) | -0.0771 | -0.76 | 69% | 13 | -0.96% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0741 | -0.76 | 69% | 13 | -0.70% | ✅ consistent |
| d_Performance (Week) | -0.0695 | -0.70 | 69% | 13 | -0.82% | ✅ consistent |
| d_Price | -0.0635 | -0.61 | 69% | 13 | -1.02% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0631 | -0.62 | 77% | 13 | -1.24% | ✅ consistent |
| d_Forward P/E | -0.0582 | -0.51 | 77% | 13 | -0.27% | ✅ consistent |
| d_Market Cap | -0.0537 | -0.74 | 85% | 13 | -1.31% | ✅ consistent |
| Volatility (Month) | -0.0370 | -0.32 | 46% | 13 | +0.66% | ⚠️ flips / too few dates |
| Gross Margin | +0.0343 | +0.47 | 57% | 14 | +0.48% | ⚠️ flips / too few dates |
| Beta | -0.0340 | -0.20 | 54% | 13 | -1.08% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0338 | +0.56 | 64% | 14 | n/a | ⚠️ flips / too few dates |
| exit_price_3d | +0.0313 | +0.66 | 67% | 12 | n/a | ✅ consistent |
| n_pos | -0.0306 | -0.36 | 57% | 14 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0295 | -0.20 | 64% | 14 | -1.87% | ⚠️ flips / too few dates |
| technical_score | -0.0293 | -0.44 | 71% | 14 | -3.02% | ✅ consistent |
| 20-Day Simple Moving Average | -0.0279 | -0.26 | 57% | 14 | -1.88% | ⚠️ flips / too few dates |
| Market Cap | +0.0270 | +0.60 | 71% | 14 | n/a | ✅ consistent |
| Profit Margin | +0.0264 | +0.26 | 64% | 14 | -3.52% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0236 | +0.45 | 62% | 13 | n/a | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0209 | +0.54 | 75% | 12 | +0.54% | ✅ consistent |
| Forward P/E | -0.0191 | -0.27 | 57% | 14 | n/a | ⚠️ flips / too few dates |
| Institutional Ownership | +0.0187 | +0.33 | 79% | 14 | n/a | ✅ consistent |
| Performance (Quarter) | -0.0187 | -0.24 | 57% | 14 | -1.92% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -18749980439011012.00 | 100% | 13 | -8.88% | ✅ consistent |
| short_fwd_3d | -0.7195 | -10.06 | 100% | 12 | -7.92% | ✅ consistent |
| short_fwd_1d | -0.6070 | -9.70 | 100% | 13 | -5.37% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0591 | -0.48 | 75% | 12 | -1.56% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0562 | -0.50 | 75% | 12 | -2.20% | ✅ consistent |
| d_Forward P/E | -0.0543 | -0.42 | 67% | 12 | -0.38% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0531 | -0.40 | 67% | 12 | -1.82% | ✅ consistent |
| true_ret | -0.0515 | -0.40 | 67% | 12 | -1.72% | ✅ consistent |
| d_Performance (YTD) | -0.0503 | -0.39 | 75% | 12 | -1.87% | ✅ consistent |
| Gross Margin | +0.0486 | +0.65 | 62% | 13 | +0.71% | ⚠️ flips / too few dates |
| d_Price | -0.0481 | -0.37 | 67% | 12 | -1.72% | ✅ consistent |
| d_Performance (Quarter) | -0.0472 | -0.42 | 50% | 12 | -1.29% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0469 | -0.38 | 58% | 12 | -1.14% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0405 | -0.49 | 67% | 12 | -3.01% | ✅ consistent |
| d_Performance (Week) | -0.0389 | -0.28 | 58% | 12 | -0.68% | ⚠️ flips / too few dates |
| Beta | -0.0387 | -0.26 | 67% | 12 | -2.62% | ✅ consistent |
| Volatility (Month) | -0.0385 | -0.40 | 67% | 12 | +1.24% | ✅ consistent |
| exit_price_2d | +0.0366 | +0.65 | 77% | 13 | n/a | ✅ consistent |
| exit_price_3d | +0.0344 | +0.61 | 67% | 12 | n/a | ✅ consistent |
| Forward P/E | -0.0335 | -0.49 | 62% | 13 | n/a | ⚠️ flips / too few dates |
| Market Cap | +0.0311 | +0.77 | 77% | 13 | n/a | ✅ consistent |
| Profit Margin | +0.0308 | +0.43 | 69% | 13 | -6.85% | ✅ consistent |
| d_Volatility (Month) | +0.0292 | +0.63 | 73% | 11 | +0.92% | ✅ consistent |
| n_pos | -0.0284 | -0.30 | 62% | 13 | n/a | ⚠️ flips / too few dates |
| price_score | -0.0255 | -0.32 | 50% | 12 | -2.70% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0253 | +0.44 | 62% | 13 | n/a | ⚠️ flips / too few dates |
| technical_score | -0.0246 | -0.40 | 62% | 13 | -5.60% | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0241 | -0.27 | 42% | 12 | -1.41% | ⚠️ flips / too few dates |
| total_score | -0.0205 | -0.27 | 46% | 13 | -1.38% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0196 | +0.45 | 54% | 13 | -0.95% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -13953893083833488.00 | 100% | 12 | -11.32% | ✅ consistent |
| short_fwd_2d | -0.7195 | -10.06 | 100% | 12 | -8.49% | ✅ consistent |
| short_fwd_1d | -0.4963 | -4.55 | 100% | 12 | -4.86% | ✅ consistent |
| Beta | -0.0640 | -0.40 | 55% | 11 | -4.34% | ⚠️ flips / too few dates |
| Volatility (Month) | -0.0593 | -0.58 | 55% | 11 | +2.17% | ⚠️ flips / too few dates |
| Gross Margin | +0.0589 | +1.04 | 83% | 12 | +1.78% | ✅ consistent |
| Profit Margin | +0.0455 | +0.63 | 75% | 12 | -8.91% | ✅ consistent |
| Forward P/E | -0.0444 | -0.65 | 58% | 12 | n/a | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0431 | -0.31 | 73% | 11 | -0.16% | ✅ consistent |
| exit_price_3d | +0.0422 | +0.71 | 75% | 12 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0413 | -0.39 | 73% | 11 | -1.59% | ✅ consistent |
| Market Cap | +0.0359 | +0.98 | 83% | 12 | n/a | ✅ consistent |
| exit_price_2d | +0.0327 | +0.54 | 75% | 12 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0295 | -0.23 | 64% | 11 | -1.30% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0270 | -0.28 | 55% | 11 | -1.23% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0237 | +0.38 | 58% | 12 | n/a | ⚠️ flips / too few dates |
| d_Beta | +0.0228 | +0.30 | 50% | 10 | -2.38% | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0226 | +0.44 | 60% | 10 | +1.25% | ⚠️ flips / too few dates |
| Short Ratio | +0.0221 | +0.59 | 67% | 12 | n/a | ✅ consistent |
| Average Volume | -0.0218 | -0.61 | 58% | 12 | n/a | ⚠️ flips / too few dates |
| price_score | -0.0217 | -0.21 | 64% | 11 | -2.77% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0203 | -0.18 | 64% | 11 | -0.26% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0201 | +0.39 | 50% | 12 | -1.53% | ⚠️ flips / too few dates |
| Insider Transactions | +0.0201 | +0.35 | 50% | 12 | +1.40% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0200 | -0.27 | 73% | 11 | -3.17% | ✅ consistent |
| true_ret | -0.0199 | -0.16 | 64% | 11 | -1.89% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0197 | +0.35 | 50% | 12 | -4.08% | ⚠️ flips / too few dates |
| Performance (Month) | -0.0197 | -0.25 | 67% | 12 | -4.72% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0185 | -0.14 | 55% | 11 | -1.54% | ⚠️ flips / too few dates |
| 20-Day Simple Moving Average | -0.0175 | -0.15 | 50% | 12 | -5.05% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

