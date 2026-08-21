# Factor report — multi-date aggregate

_Generated 2026-08-21 17:15 EDT from 11 scan dates._

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
| 2026-08-19 | 2026-08-18 | 2026-08-20 | 2026-08-21 | — | 11587 |
| 2026-08-20 | 2026-08-19 | 2026-08-21 | — | — | 11599 |

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
| 2026-08-19 | +0.0108 | +0.0519 | — |
| 2026-08-20 | -0.0007 | — | — |
- **1d**: mean IC **-0.0016**, ICIR -0.02, sign consistency 55% over 11 dates
- **2d**: mean IC **-0.0307**, ICIR -0.37, sign consistency 50% over 10 dates
- **3d**: mean IC **-0.0309**, ICIR -0.33, sign consistency 56% over 9 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -29873500339944656.00 | 100% | 11 | -6.13% | ✅ consistent |
| short_fwd_2d | -0.6083 | -8.76 | 100% | 10 | -4.69% | ✅ consistent |
| short_fwd_3d | -0.4835 | -3.94 | 100% | 9 | -4.29% | ✅ consistent |
| d_Performance (Quarter) | -0.0775 | -0.59 | 70% | 10 | -1.47% | ✅ consistent |
| d_Performance (Week) | -0.0608 | -0.59 | 60% | 10 | -0.97% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0569 | -0.56 | 60% | 10 | -1.20% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0559 | -0.55 | 60% | 10 | -1.29% | ⚠️ flips / too few dates |
| true_ret | -0.0550 | -0.57 | 60% | 10 | -1.18% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0520 | -0.52 | 60% | 10 | -1.04% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0506 | -0.53 | 60% | 10 | -0.88% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0453 | -0.36 | 70% | 10 | -0.24% | ✅ consistent |
| d_Market Cap | -0.0433 | -0.57 | 80% | 10 | -1.58% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0418 | -0.40 | 70% | 10 | -1.45% | ✅ consistent |
| d_Price | -0.0404 | -0.39 | 60% | 10 | -1.18% | ⚠️ flips / too few dates |
| Beta | -0.0355 | -0.21 | 50% | 10 | -1.27% | ⚠️ flips / too few dates |
| Gross Margin | +0.0304 | +0.41 | 55% | 11 | +0.36% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0304 | +0.59 | 67% | 9 | n/a | ✅ consistent |
| exit_price_1d | +0.0288 | +0.58 | 64% | 11 | n/a | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0281 | +0.77 | 78% | 9 | +0.51% | ✅ consistent |
| Volatility (Month) | -0.0280 | -0.26 | 40% | 10 | +0.66% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0270 | +0.53 | 60% | 10 | n/a | ⚠️ flips / too few dates |
| Market Cap | +0.0234 | +0.61 | 73% | 11 | n/a | ✅ consistent |
| Performance (Quarter) | -0.0224 | -0.29 | 55% | 11 | -2.19% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0223 | +0.44 | 64% | 11 | -1.69% | ⚠️ flips / too few dates |
| Profit Margin | +0.0202 | +0.24 | 64% | 11 | -4.18% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0200 | +0.49 | 64% | 11 | -0.38% | ⚠️ flips / too few dates |
| Forward P/E | -0.0195 | -0.28 | 55% | 11 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0167 | -0.14 | 64% | 11 | -2.29% | ⚠️ flips / too few dates |
| upside_pct_lvl | +0.0160 | +0.18 | 55% | 11 | +1.24% | ⚠️ flips / too few dates |
| upside_pct | +0.0160 | +0.18 | 55% | 11 | +1.24% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -20140709820486304.00 | 100% | 10 | -9.37% | ✅ consistent |
| short_fwd_3d | -0.7183 | -8.75 | 100% | 9 | -8.02% | ✅ consistent |
| short_fwd_1d | -0.6083 | -8.76 | 100% | 10 | -5.44% | ✅ consistent |
| Beta | -0.0587 | -0.38 | 67% | 9 | -2.89% | ✅ consistent |
| d_Forward P/E | -0.0560 | -0.42 | 67% | 9 | -0.42% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0483 | -0.37 | 67% | 9 | -2.48% | ✅ consistent |
| d_Relative Strength Index (14) | -0.0455 | -0.38 | 67% | 9 | -3.14% | ✅ consistent |
| d_Performance (Month) | -0.0443 | -0.47 | 44% | 9 | -2.04% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0434 | -0.31 | 67% | 9 | -2.74% | ✅ consistent |
| true_ret | -0.0427 | -0.32 | 67% | 9 | -2.38% | ✅ consistent |
| Volatility (Month) | -0.0412 | -0.38 | 67% | 9 | +1.24% | ✅ consistent |
| Gross Margin | +0.0409 | +0.53 | 60% | 10 | +0.36% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0397 | -0.30 | 67% | 9 | -2.66% | ✅ consistent |
| price_score | -0.0394 | -0.46 | 56% | 9 | -3.80% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0394 | -0.33 | 44% | 9 | -2.58% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0382 | -0.43 | 67% | 9 | -4.28% | ✅ consistent |
| exit_price_3d | +0.0379 | +0.61 | 78% | 9 | n/a | ✅ consistent |
| n_pos | -0.0366 | -0.38 | 70% | 10 | n/a | ✅ consistent |
| Performance (Month) | -0.0349 | -0.49 | 70% | 10 | -4.02% | ✅ consistent |
| exit_price_2d | +0.0346 | +0.56 | 70% | 10 | n/a | ✅ consistent |
| d_Price | -0.0336 | -0.25 | 56% | 9 | -2.38% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0334 | -0.25 | 44% | 9 | -2.08% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0330 | -0.22 | 56% | 9 | -1.05% | ⚠️ flips / too few dates |
| Profit Margin | +0.0323 | +0.46 | 70% | 10 | -7.83% | ✅ consistent |
| d_Volatility (Month) | +0.0316 | +0.59 | 62% | 8 | +1.05% | ⚠️ flips / too few dates |
| w_pos | -0.0314 | -0.35 | 50% | 10 | n/a | ⚠️ flips / too few dates |
| total_score | -0.0307 | -0.37 | 50% | 10 | -2.11% | ⚠️ flips / too few dates |
| Sales Year Over Year TTM | +0.0273 | +0.60 | 60% | 10 | -1.01% | ⚠️ flips / too few dates |
| Market Cap | +0.0268 | +0.66 | 70% | 10 | n/a | ✅ consistent |
| Forward P/E | -0.0265 | -0.43 | 60% | 10 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -15600926743107926.00 | 100% | 9 | -11.58% | ✅ consistent |
| short_fwd_2d | -0.7183 | -8.75 | 100% | 9 | -8.75% | ✅ consistent |
| short_fwd_1d | -0.4835 | -3.94 | 100% | 9 | -4.41% | ✅ consistent |
| d_Performance (Week) | -0.0767 | -0.56 | 75% | 8 | -0.72% | ✅ consistent |
| d_Performance (Month) | -0.0738 | -0.93 | 75% | 8 | -2.08% | ✅ consistent |
| Beta | -0.0686 | -0.39 | 50% | 8 | -4.30% | ⚠️ flips / too few dates |
| Gross Margin | +0.0524 | +0.82 | 78% | 9 | +1.33% | ✅ consistent |
| Volatility (Month) | -0.0505 | -0.45 | 50% | 8 | +2.17% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0490 | -0.45 | 75% | 8 | -0.42% | ✅ consistent |
| price_score | -0.0471 | -0.56 | 62% | 8 | -3.67% | ⚠️ flips / too few dates |
| Performance (Month) | -0.0456 | -0.81 | 78% | 9 | -5.16% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0453 | -0.35 | 62% | 8 | -2.27% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0439 | +0.65 | 67% | 9 | n/a | ✅ consistent |
| 20-Day Simple Moving Average | -0.0399 | -0.35 | 56% | 9 | -5.96% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0372 | -0.28 | 56% | 9 | -5.48% | ⚠️ flips / too few dates |
| true_ret | -0.0371 | -0.30 | 62% | 8 | -2.62% | ⚠️ flips / too few dates |
| Profit Margin | +0.0370 | +0.51 | 78% | 9 | -10.05% | ✅ consistent |
| Market Cap | +0.0363 | +0.89 | 78% | 9 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0360 | -0.29 | 50% | 8 | -2.32% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0338 | +0.49 | 67% | 9 | n/a | ✅ consistent |
| Sales Year Over Year TTM | +0.0333 | +0.63 | 67% | 9 | -1.64% | ✅ consistent |
| d_Market Cap | -0.0332 | -0.46 | 75% | 8 | -3.98% | ✅ consistent |
| d_Performance (YTD) | -0.0324 | -0.26 | 62% | 8 | -2.45% | ⚠️ flips / too few dates |
| Sales Growth Quarter Over Quarter | +0.0323 | +0.53 | 67% | 9 | -4.93% | ✅ consistent |
| w_pos | -0.0316 | -0.34 | 44% | 9 | n/a | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0316 | -0.34 | 62% | 8 | -2.96% | ⚠️ flips / too few dates |
| d_Volatility (Month) | +0.0315 | +0.56 | 57% | 7 | +2.01% | ⚠️ flips / too few dates |
| d_Performance (Quarter) | -0.0311 | -0.31 | 50% | 8 | -2.39% | ⚠️ flips / too few dates |
| n_pos | -0.0310 | -0.34 | 56% | 9 | n/a | ⚠️ flips / too few dates |
| total_score | -0.0309 | -0.33 | 56% | 9 | -2.74% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

