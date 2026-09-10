# Factor report — multi-date aggregate

_Generated 2026-09-10 18:53 EDT from 23 scan dates._

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
| 2026-09-08 | — | 2026-09-09 | 2026-09-10 | — | 11595 |
| 2026-09-09 | 2026-09-08 | 2026-09-10 | — | — | 11599 |

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
| 2026-09-08 | -0.0849 | -0.1276 | — |
| 2026-09-09 | -0.0163 | — | — |
- **1d**: mean IC **-0.0274**, ICIR -0.36, sign consistency 74% over 23 dates
- **2d**: mean IC **-0.0432**, ICIR -0.52, sign consistency 59% over 22 dates
- **3d**: mean IC **-0.0408**, ICIR -0.38, sign consistency 62% over 21 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -21598505061322840.00 | 100% | 23 | -6.36% | ✅ consistent |
| short_fwd_2d | -0.6199 | -8.22 | 100% | 22 | -5.23% | ✅ consistent |
| short_fwd_3d | -0.4842 | -4.42 | 100% | 21 | -4.49% | ✅ consistent |
| Volatility (Month) | -0.0677 | -0.52 | 55% | 22 | +0.66% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0635 | -0.63 | 67% | 21 | -0.67% | ✅ consistent |
| Beta | -0.0597 | -0.32 | 59% | 22 | -1.35% | ⚠️ flips / too few dates |
| Profit Margin | +0.0483 | +0.49 | 65% | 23 | -2.64% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0478 | -0.45 | 57% | 21 | -0.59% | ⚠️ flips / too few dates |
| d_200-Day Simple Moving Average | -0.0478 | -0.44 | 52% | 21 | -0.61% | ⚠️ flips / too few dates |
| true_ret | -0.0454 | -0.43 | 52% | 21 | -0.72% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0432 | -0.40 | 52% | 21 | -0.79% | ⚠️ flips / too few dates |
| n_pos | -0.0419 | -0.55 | 65% | 23 | n/a | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0418 | -0.44 | 67% | 21 | -0.97% | ✅ consistent |
| d_Performance (Quarter) | -0.0412 | -0.34 | 57% | 21 | -0.89% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0408 | -0.41 | 52% | 21 | -0.41% | ⚠️ flips / too few dates |
| Forward P/E | -0.0406 | -0.44 | 70% | 23 | n/a | ✅ consistent |
| exit_price_1d | +0.0389 | +0.63 | 65% | 23 | n/a | ⚠️ flips / too few dates |
| exit_price_2d | +0.0379 | +0.61 | 64% | 22 | n/a | ⚠️ flips / too few dates |
| Performance (Week) | -0.0366 | -0.27 | 61% | 23 | -1.55% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0366 | -0.35 | 67% | 21 | -0.22% | ✅ consistent |
| d_Market Cap | -0.0363 | -0.51 | 67% | 21 | -0.80% | ✅ consistent |
| exit_price_3d | +0.0349 | +0.55 | 62% | 21 | n/a | ⚠️ flips / too few dates |
| w_pos | -0.0336 | -0.41 | 65% | 23 | n/a | ⚠️ flips / too few dates |
| Average Volume | -0.0335 | -0.51 | 65% | 23 | n/a | ⚠️ flips / too few dates |
| Short Float | -0.0304 | -0.25 | 52% | 23 | n/a | ⚠️ flips / too few dates |
| d_Price | -0.0303 | -0.28 | 52% | 21 | -0.72% | ⚠️ flips / too few dates |
| valuation_score | -0.0290 | -0.31 | 65% | 23 | +1.10% | ⚠️ flips / too few dates |
| total_score | -0.0274 | -0.36 | 74% | 23 | -0.70% | ✅ consistent |
| Market Cap | +0.0248 | +0.47 | 65% | 23 | n/a | ⚠️ flips / too few dates |
| price_score | -0.0244 | -0.28 | 62% | 21 | -0.85% | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -15968057602249682.00 | 100% | 22 | -10.01% | ✅ consistent |
| short_fwd_3d | -0.7238 | -8.79 | 100% | 21 | -8.71% | ✅ consistent |
| short_fwd_1d | -0.6199 | -8.22 | 100% | 22 | -5.86% | ✅ consistent |
| Volatility (Month) | -0.0795 | -0.62 | 71% | 21 | +1.24% | ✅ consistent |
| Beta | -0.0669 | -0.35 | 71% | 21 | -2.79% | ✅ consistent |
| Profit Margin | +0.0612 | +0.77 | 77% | 22 | -5.08% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0595 | -0.47 | 70% | 20 | -1.47% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0579 | -0.42 | 60% | 20 | -1.66% | ⚠️ flips / too few dates |
| Forward P/E | -0.0568 | -0.63 | 68% | 22 | n/a | ✅ consistent |
| d_Performance (Week) | -0.0550 | -0.40 | 55% | 20 | -0.71% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0549 | -0.55 | 70% | 20 | -2.27% | ✅ consistent |
| true_ret | -0.0530 | -0.40 | 60% | 20 | -1.82% | ⚠️ flips / too few dates |
| d_Performance (YTD) | -0.0526 | -0.39 | 65% | 20 | -2.07% | ⚠️ flips / too few dates |
| n_pos | -0.0506 | -0.57 | 73% | 22 | n/a | ✅ consistent |
| exit_price_2d | +0.0491 | +0.88 | 82% | 22 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0484 | -0.38 | 60% | 20 | -1.15% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0476 | -0.41 | 65% | 20 | -0.37% | ⚠️ flips / too few dates |
| d_Price | -0.0470 | -0.35 | 60% | 20 | -1.82% | ⚠️ flips / too few dates |
| d_Market Cap | -0.0467 | -0.54 | 70% | 20 | -2.84% | ✅ consistent |
| exit_price_3d | +0.0457 | +0.82 | 76% | 21 | n/a | ✅ consistent |
| w_pos | -0.0451 | -0.55 | 64% | 22 | n/a | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0450 | -0.41 | 50% | 20 | -1.58% | ⚠️ flips / too few dates |
| total_score | -0.0432 | -0.52 | 59% | 22 | -1.48% | ⚠️ flips / too few dates |
| Average Volume | -0.0431 | -0.69 | 73% | 22 | n/a | ✅ consistent |
| price_score | -0.0416 | -0.42 | 50% | 20 | -2.72% | ⚠️ flips / too few dates |
| Short Float | -0.0399 | -0.36 | 55% | 22 | n/a | ⚠️ flips / too few dates |
| valuation_score | -0.0382 | -0.47 | 59% | 22 | +2.03% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0377 | +0.67 | 73% | 22 | n/a | ✅ consistent |
| Performance (YTD) | +0.0317 | +0.33 | 64% | 22 | -3.59% | ⚠️ flips / too few dates |
| Market Cap | +0.0310 | +0.60 | 68% | 22 | n/a | ✅ consistent |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -14593330697217224.00 | 100% | 21 | -12.39% | ✅ consistent |
| short_fwd_2d | -0.7238 | -8.79 | 100% | 21 | -8.77% | ✅ consistent |
| short_fwd_1d | -0.4842 | -4.42 | 100% | 21 | -4.71% | ✅ consistent |
| Volatility (Month) | -0.0898 | -0.72 | 70% | 20 | +2.17% | ✅ consistent |
| d_Performance (Week) | -0.0747 | -0.57 | 80% | 20 | -0.45% | ✅ consistent |
| Beta | -0.0701 | -0.39 | 55% | 20 | -4.23% | ⚠️ flips / too few dates |
| Profit Margin | +0.0686 | +0.98 | 86% | 21 | -6.70% | ✅ consistent |
| Forward P/E | -0.0661 | -0.74 | 62% | 21 | n/a | ⚠️ flips / too few dates |
| d_Performance (Month) | -0.0610 | -0.53 | 80% | 20 | -1.56% | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0539 | -0.45 | 70% | 20 | -1.30% | ✅ consistent |
| exit_price_3d | +0.0538 | +1.03 | 86% | 21 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0522 | -0.40 | 65% | 20 | -1.49% | ⚠️ flips / too few dates |
| w_pos | -0.0494 | -0.49 | 62% | 21 | n/a | ⚠️ flips / too few dates |
| n_pos | -0.0492 | -0.47 | 62% | 21 | n/a | ⚠️ flips / too few dates |
| Average Volume | -0.0491 | -0.84 | 71% | 21 | n/a | ✅ consistent |
| price_score | -0.0475 | -0.42 | 65% | 20 | -2.72% | ⚠️ flips / too few dates |
| true_ret | -0.0466 | -0.37 | 70% | 20 | -1.93% | ✅ consistent |
| d_Performance (YTD) | -0.0466 | -0.36 | 70% | 20 | -2.05% | ✅ consistent |
| exit_price_2d | +0.0443 | +0.84 | 86% | 21 | n/a | ✅ consistent |
| Short Float | -0.0433 | -0.41 | 67% | 21 | n/a | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0426 | -0.36 | 65% | 20 | -0.83% | ⚠️ flips / too few dates |
| valuation_score | -0.0422 | -0.54 | 71% | 21 | +2.76% | ✅ consistent |
| d_Market Cap | -0.0416 | -0.54 | 75% | 20 | -2.91% | ✅ consistent |
| total_score | -0.0408 | -0.38 | 62% | 21 | -1.48% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0389 | -0.43 | 70% | 20 | -2.23% | ✅ consistent |
| d_Forward P/E | -0.0382 | -0.36 | 70% | 20 | -0.39% | ✅ consistent |
| d_Price | -0.0375 | -0.29 | 70% | 20 | -1.93% | ✅ consistent |
| Performance (YTD) | +0.0359 | +0.34 | 67% | 21 | -4.79% | ✅ consistent |
| exit_price_1d | +0.0352 | +0.65 | 76% | 21 | n/a | ✅ consistent |
| Market Cap | +0.0333 | +0.70 | 76% | 21 | n/a | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

