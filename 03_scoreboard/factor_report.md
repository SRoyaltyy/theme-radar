# Factor report — multi-date aggregate

_Generated 2026-08-25 17:20 EDT from 13 scan dates._

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
| 2026-08-21 | 2026-08-20 | 2026-08-24 | 2026-08-25 | — | 11602 |
| 2026-08-24 | 2026-08-21 | 2026-08-25 | — | — | 11605 |

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
| 2026-08-21 | -0.0802 | +0.0158 | — |
| 2026-08-24 | +0.0056 | — | — |
- **1d**: mean IC **-0.0071**, ICIR -0.08, sign consistency 54% over 13 dates
- **2d**: mean IC **-0.0199**, ICIR -0.25, sign consistency 42% over 12 dates
- **3d**: mean IC **-0.0057**, ICIR -0.05, sign consistency 45% over 11 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -22963942381371352.00 | 100% | 13 | -6.04% | ✅ consistent |
| short_fwd_2d | -0.6043 | -9.38 | 100% | 12 | -4.71% | ✅ consistent |
| short_fwd_3d | -0.4952 | -4.35 | 100% | 11 | -4.13% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0752 | -0.73 | 67% | 12 | -1.07% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0723 | -0.70 | 67% | 12 | -1.10% | ✅ consistent |
| true_ret | -0.0722 | -0.73 | 67% | 12 | -1.07% | ✅ consistent |
| d_Performance (Quarter) | -0.0722 | -0.59 | 67% | 12 | -1.19% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0696 | -0.70 | 67% | 12 | -0.75% | ✅ consistent |
| d_Performance (YTD) | -0.0691 | -0.68 | 67% | 12 | -1.01% | ✅ consistent |
| d_Performance (Week) | -0.0677 | -0.65 | 67% | 12 | -0.89% | ✅ consistent |
| d_Price | -0.0563 | -0.54 | 67% | 12 | -1.07% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0558 | -0.54 | 75% | 12 | -1.31% | ✅ consistent |
| d_Forward P/E | -0.0523 | -0.45 | 75% | 12 | -0.25% | ✅ consistent |
| d_Market Cap | -0.0475 | -0.65 | 83% | 12 | -1.39% | ✅ consistent |
| Gross Margin | +0.0370 | +0.49 | 62% | 13 | +0.44% | ⚠️ flips / too few dates |
| Beta | -0.0327 | -0.19 | 50% | 12 | -1.16% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0311 | +0.65 | 67% | 12 | n/a | ✅ consistent |
| Volatility (Month) | -0.0309 | -0.26 | 42% | 12 | +0.66% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0280 | +0.59 | 64% | 11 | n/a | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0273 | +0.80 | 82% | 11 | +0.59% | ✅ consistent |
| technical_score | -0.0263 | -0.38 | 69% | 13 | -3.20% | ✅ consistent |
| Forward P/E | -0.0257 | -0.36 | 62% | 13 | n/a | ⚠️ flips / too few dates |
| exit_price_1d | +0.0249 | +0.46 | 62% | 13 | n/a | ⚠️ flips / too few dates |
| Market Cap | +0.0222 | +0.51 | 69% | 13 | n/a | ✅ consistent |
| Profit Margin | +0.0217 | +0.21 | 62% | 13 | -3.77% | ⚠️ flips / too few dates |
| n_pos | -0.0202 | -0.26 | 54% | 13 | n/a | ⚠️ flips / too few dates |
| Performance (Quarter) | -0.0195 | -0.24 | 54% | 13 | -2.05% | ⚠️ flips / too few dates |
| upside_pct_lvl | +0.0175 | +0.15 | 54% | 13 | +1.23% | ⚠️ flips / too few dates |
| upside_pct | +0.0175 | +0.15 | 54% | 13 | +1.24% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0168 | +0.41 | 62% | 13 | -0.42% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -22063042185692344.00 | 100% | 12 | -9.23% | ✅ consistent |
| short_fwd_3d | -0.7185 | -9.63 | 100% | 11 | -8.02% | ✅ consistent |
| short_fwd_1d | -0.6043 | -9.38 | 100% | 12 | -5.53% | ✅ consistent |
| Beta | -0.0550 | -0.39 | 73% | 11 | -2.90% | ✅ consistent |
| Gross Margin | +0.0533 | +0.71 | 67% | 12 | +0.70% | ✅ consistent |
| Volatility (Month) | -0.0449 | -0.46 | 73% | 11 | +1.24% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0446 | -0.38 | 73% | 11 | -1.66% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0431 | -0.40 | 73% | 11 | -2.35% | ✅ consistent |
| Forward P/E | -0.0412 | -0.63 | 67% | 12 | n/a | ✅ consistent |
| d_Forward P/E | -0.0410 | -0.33 | 64% | 11 | -0.29% | ⚠️ flips / too few dates |
| Profit Margin | +0.0397 | +0.58 | 75% | 12 | -7.26% | ✅ consistent |
| exit_price_3d | +0.0377 | +0.65 | 73% | 11 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0363 | -0.29 | 64% | 11 | -1.94% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0352 | +0.60 | 75% | 12 | n/a | ✅ consistent |
| true_ret | -0.0351 | -0.29 | 64% | 11 | -1.82% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0346 | -0.32 | 45% | 11 | -1.37% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0331 | -0.27 | 73% | 11 | -1.99% | ✅ consistent |
| d_Performance (Month) | -0.0328 | -0.37 | 45% | 11 | -1.60% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0326 | -0.27 | 55% | 11 | -1.21% | ⚠️ flips / too few dates |
| Market Cap | +0.0317 | +0.76 | 75% | 12 | n/a | ✅ consistent |
| d_Market Cap | -0.0314 | -0.39 | 64% | 11 | -3.28% | ⚠️ flips / too few dates |
| d_Price | -0.0302 | -0.25 | 64% | 11 | -1.82% | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0297 | +0.61 | 70% | 10 | +1.02% | ✅ consistent |
| price_score | -0.0269 | -0.33 | 45% | 11 | -2.99% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0266 | +0.31 | 58% | 12 | -3.65% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0250 | -0.18 | 55% | 11 | -0.65% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0235 | +0.40 | 58% | 12 | n/a | ⚠️ flips / too few dates |
| Short Ratio | +0.0217 | +0.41 | 58% | 12 | n/a | ⚠️ flips / too few dates |
| n_pos | -0.0214 | -0.22 | 58% | 12 | n/a | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0211 | +0.25 | 58% | 12 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -14936750169972328.00 | 100% | 11 | -11.62% | ✅ consistent |
| short_fwd_2d | -0.7185 | -9.63 | 100% | 11 | -8.64% | ✅ consistent |
| short_fwd_1d | -0.4952 | -4.35 | 100% | 11 | -4.72% | ✅ consistent |
| Beta | -0.0627 | -0.37 | 50% | 10 | -4.66% | ⚠️ flips / too few dates |
| Gross Margin | +0.0564 | +0.96 | 82% | 11 | +1.68% | ✅ consistent |
| Volatility (Month) | -0.0528 | -0.50 | 50% | 10 | +2.17% | ⚠️ flips / too few dates |
| Forward P/E | -0.0450 | -0.63 | 55% | 11 | n/a | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0448 | -0.31 | 70% | 10 | -0.07% | ✅ consistent |
| Profit Margin | +0.0434 | +0.58 | 73% | 11 | -9.41% | ✅ consistent |
| exit_price_3d | +0.0398 | +0.65 | 73% | 11 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0392 | -0.35 | 70% | 10 | -1.60% | ✅ consistent |
| Market Cap | +0.0338 | +0.90 | 82% | 11 | n/a | ✅ consistent |
| exit_price_2d | +0.0299 | +0.48 | 73% | 11 | n/a | ✅ consistent |
| Short Ratio | +0.0247 | +0.65 | 73% | 11 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0237 | -0.18 | 60% | 10 | -1.33% | ⚠️ flips / too few dates |
| d_Beta | +0.0232 | +0.29 | 44% | 9 | -2.60% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0230 | +0.40 | 55% | 11 | -4.52% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0227 | -0.22 | 50% | 10 | -1.32% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0224 | +0.42 | 55% | 11 | -1.61% | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0221 | +0.41 | 56% | 9 | +1.31% | ⚠️ flips / too few dates |
| 50-Day Simple Moving Average | +0.0211 | +0.27 | 36% | 11 | -4.77% | ⚠️ flips / too few dates |
| Average Volume | -0.0209 | -0.56 | 55% | 11 | n/a | ⚠️ flips / too few dates |
| Insider Transactions | +0.0207 | +0.35 | 45% | 11 | +1.12% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0206 | +0.32 | 55% | 11 | n/a | ⚠️ flips / too few dates |
| Target Price | -0.0202 | -0.29 | 55% | 11 | n/a | ⚠️ flips / too few dates |
| Analyst Recom | -0.0193 | -0.37 | 64% | 11 | n/a | ⚠️ flips / too few dates |
| d_Market Cap | -0.0189 | -0.25 | 70% | 10 | -3.31% | ✅ consistent |
| d_Forward P/E | -0.0188 | -0.16 | 60% | 10 | -0.23% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0183 | +0.23 | 55% | 11 | n/a | ⚠️ flips / too few dates |
| price_score | -0.0175 | -0.16 | 60% | 10 | -2.89% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

