# Factor report — multi-date aggregate

_Generated 2026-09-24 16:51 EDT from 33 scan dates._

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
| 2026-09-22 | 2026-09-21 | 2026-09-23 | 2026-09-24 | — | 11637 |
| 2026-09-23 | 2026-09-22 | 2026-09-24 | — | — | 11653 |

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
| 2026-09-22 | -0.1323 | -0.1167 | — |
| 2026-09-23 | +0.0928 | — | — |
- **1d**: mean IC **-0.0190**, ICIR -0.23, sign consistency 70% over 33 dates
- **2d**: mean IC **-0.0319**, ICIR -0.33, sign consistency 59% over 32 dates
- **3d**: mean IC **-0.0278**, ICIR -0.22, sign consistency 65% over 31 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -18293708165931056.00 | 100% | 33 | -5.91% | ✅ consistent |
| short_fwd_2d | -0.6202 | -7.22 | 100% | 32 | -4.89% | ✅ consistent |
| short_fwd_3d | -0.4901 | -4.32 | 100% | 31 | -4.38% | ✅ consistent |
| Volatility (Month) | -0.0619 | -0.48 | 59% | 32 | +0.45% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0591 | -0.51 | 65% | 31 | -0.61% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0454 | +0.69 | 70% | 33 | n/a | ✅ consistent |
| exit_price_2d | +0.0437 | +0.66 | 69% | 32 | n/a | ✅ consistent |
| Profit Margin | +0.0411 | +0.41 | 67% | 33 | -2.36% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0408 | -0.37 | 48% | 31 | -0.49% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0406 | +0.63 | 68% | 31 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0401 | -0.37 | 52% | 31 | -0.51% | ⚠️ flips / too few dates |
| Average Volume | -0.0398 | -0.64 | 70% | 33 | n/a | ✅ consistent |
| valuation_score | -0.0386 | -0.43 | 70% | 33 | +0.95% | ✅ consistent |
| n_pos | -0.0371 | -0.42 | 64% | 33 | n/a | ⚠️ flips / too few dates |
| true_ret | -0.0371 | -0.35 | 48% | 31 | -0.60% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0369 | -0.34 | 52% | 31 | -0.60% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0354 | -0.34 | 48% | 31 | -0.35% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0351 | -0.38 | 61% | 31 | -0.76% | ⚠️ flips / too few dates |
| Performance (Week) | -0.0346 | -0.24 | 58% | 33 | -1.18% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0319 | +0.35 | 64% | 33 | -1.57% | ⚠️ flips / too few dates |
| Beta | -0.0316 | -0.16 | 56% | 32 | -1.23% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0314 | -0.31 | 65% | 31 | -0.17% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0314 | -0.47 | 68% | 31 | -0.65% | ✅ consistent |
| Price | +0.0293 | +0.44 | 61% | 33 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0293 | +0.44 | 61% | 33 | n/a | ⚠️ flips / too few dates |
| d_Price | -0.0288 | -0.26 | 52% | 31 | -0.60% | ⚠️ flips / too few dates |
| w_pos | -0.0282 | -0.30 | 64% | 33 | n/a | ⚠️ flips / too few dates |
| Market Cap | +0.0277 | +0.46 | 67% | 33 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0276 | +0.34 | 58% | 33 | -1.52% | ⚠️ flips / too few dates |
| upside_pct | -0.0258 | -0.20 | 58% | 33 | +0.89% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -16112567856389042.00 | 100% | 32 | -9.27% | ✅ consistent |
| short_fwd_3d | -0.7334 | -9.80 | 100% | 31 | -8.27% | ✅ consistent |
| short_fwd_1d | -0.6202 | -7.22 | 100% | 32 | -5.52% | ✅ consistent |
| Volatility (Month) | -0.0816 | -0.64 | 71% | 31 | +0.97% | ✅ consistent |
| exit_price_2d | +0.0591 | +0.98 | 81% | 32 | n/a | ✅ consistent |
| exit_price_3d | +0.0557 | +0.96 | 77% | 31 | n/a | ✅ consistent |
| Average Volume | -0.0529 | -0.91 | 81% | 32 | n/a | ✅ consistent |
| Profit Margin | +0.0518 | +0.56 | 72% | 32 | -4.49% | ✅ consistent |
| valuation_score | -0.0517 | -0.65 | 66% | 32 | +1.74% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0513 | -0.36 | 60% | 30 | -0.55% | ⚠️ flips / too few dates |
| n_pos | -0.0481 | -0.47 | 72% | 32 | n/a | ✅ consistent |
| exit_price_1d | +0.0477 | +0.78 | 75% | 32 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0476 | -0.36 | 67% | 30 | -1.02% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0441 | -0.32 | 60% | 30 | -1.13% | ⚠️ flips / too few dates |
| w_pos | -0.0430 | -0.43 | 69% | 32 | n/a | ✅ consistent |
| Beta | -0.0420 | -0.21 | 65% | 31 | -2.40% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0398 | -0.37 | 67% | 30 | -1.56% | ✅ consistent |
| true_ret | -0.0397 | -0.30 | 57% | 30 | -1.31% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0389 | -0.29 | 57% | 30 | -0.82% | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0387 | +0.45 | 69% | 32 | -2.99% | ✅ consistent |
| d_Performance (YTD) | -0.0385 | -0.28 | 63% | 30 | -1.38% | ⚠️ flips / too few dates |
| 200-Day Simple Moving Average | +0.0374 | +0.46 | 69% | 32 | -2.91% | ✅ consistent |
| Performance (Week) | -0.0363 | -0.26 | 53% | 32 | -2.00% | ⚠️ flips / too few dates |
| Price | +0.0360 | +0.58 | 72% | 32 | n/a | ✅ consistent |
| entry_price | +0.0360 | +0.58 | 72% | 32 | n/a | ✅ consistent |
| Short Float | -0.0348 | -0.32 | 59% | 32 | n/a | ⚠️ flips / too few dates |
| d_Price | -0.0343 | -0.25 | 60% | 30 | -1.31% | ⚠️ flips / too few dates |
| upside_pct | -0.0341 | -0.26 | 53% | 32 | +1.64% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0341 | -0.26 | 53% | 32 | +1.64% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0327 | -0.40 | 67% | 30 | -2.06% | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -16716654339818676.00 | 100% | 31 | -11.76% | ✅ consistent |
| short_fwd_2d | -0.7334 | -9.80 | 100% | 31 | -8.44% | ✅ consistent |
| short_fwd_1d | -0.4901 | -4.32 | 100% | 31 | -4.84% | ✅ consistent |
| Volatility (Month) | -0.0949 | -0.77 | 70% | 30 | +1.70% | ✅ consistent |
| exit_price_3d | +0.0657 | +1.15 | 87% | 31 | n/a | ✅ consistent |
| Average Volume | -0.0621 | -1.15 | 81% | 31 | n/a | ✅ consistent |
| valuation_score | -0.0602 | -0.81 | 81% | 31 | +2.42% | ✅ consistent |
| Profit Margin | +0.0580 | +0.66 | 77% | 31 | -6.03% | ✅ consistent |
| exit_price_2d | +0.0563 | +0.96 | 87% | 31 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0506 | -0.32 | 76% | 29 | -0.37% | ✅ consistent |
| exit_price_1d | +0.0470 | +0.79 | 77% | 31 | n/a | ✅ consistent |
| Beta | -0.0466 | -0.25 | 57% | 30 | -3.54% | ⚠️ flips / too few dates |
| n_pos | -0.0433 | -0.37 | 65% | 31 | n/a | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0432 | +0.46 | 74% | 31 | -4.07% | ✅ consistent |
| w_pos | -0.0428 | -0.37 | 68% | 31 | n/a | ✅ consistent |
| 200-Day Simple Moving Average | +0.0422 | +0.48 | 65% | 31 | -3.99% | ⚠️ flips / too few dates |
| Short Float | -0.0409 | -0.42 | 65% | 31 | n/a | ⚠️ flips / too few dates |
| Price | +0.0373 | +0.62 | 68% | 31 | n/a | ✅ consistent |
| entry_price | +0.0373 | +0.62 | 68% | 31 | n/a | ✅ consistent |
| upside_pct | -0.0367 | -0.30 | 65% | 31 | +2.27% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0367 | -0.30 | 65% | 31 | +2.27% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0338 | -0.23 | 66% | 29 | -0.78% | ⚠️ flips / too few dates |
| Gross Margin | +0.0335 | +0.53 | 71% | 31 | -2.83% | ✅ consistent |
| Market Cap | +0.0332 | +0.58 | 71% | 31 | n/a | ✅ consistent |
| d_Performance (Month) | -0.0322 | -0.23 | 76% | 29 | -0.97% | ✅ consistent |
| Performance (Week) | -0.0310 | -0.23 | 48% | 31 | -2.37% | ⚠️ flips / too few dates |
| Relative Strength Index (14) | +0.0307 | +0.35 | 55% | 31 | n/a | ⚠️ flips / too few dates |
| Short Ratio | -0.0303 | -0.38 | 58% | 31 | n/a | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0299 | -0.20 | 62% | 29 | -0.90% | ⚠️ flips / too few dates |
| total_score | -0.0278 | -0.22 | 65% | 31 | -0.82% | ⚠️ flips / too few dates |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

