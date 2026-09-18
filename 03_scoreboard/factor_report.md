# Factor report — multi-date aggregate

_Generated 2026-09-18 18:57 EDT from 29 scan dates._

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
| 2026-09-16 | 2026-09-15 | 2026-09-17 | 2026-09-18 | — | 11627 |
| 2026-09-17 | 2026-09-16 | 2026-09-18 | — | — | 11636 |

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
| 2026-09-16 | -0.0722 | -0.0629 | — |
| 2026-09-17 | +0.0987 | — | — |
- **1d**: mean IC **-0.0284**, ICIR -0.39, sign consistency 76% over 29 dates
- **2d**: mean IC **-0.0418**, ICIR -0.49, sign consistency 61% over 28 dates
- **3d**: mean IC **-0.0463**, ICIR -0.41, sign consistency 67% over 27 dates

## Factor ranking — 1d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_1d | -1.0000 | -19802186386119060.00 | 100% | 29 | -6.11% | ✅ consistent |
| short_fwd_2d | -0.6171 | -7.61 | 100% | 28 | -5.02% | ✅ consistent |
| short_fwd_3d | -0.4844 | -4.34 | 100% | 27 | -4.49% | ✅ consistent |
| Volatility (Month) | -0.0630 | -0.49 | 61% | 28 | +0.45% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0614 | -0.60 | 67% | 27 | -0.66% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0491 | -0.46 | 52% | 27 | -0.58% | ⚠️ flips / too few dates |
| d_50-Day Simple Moving Average | -0.0491 | -0.48 | 56% | 27 | -0.60% | ⚠️ flips / too few dates |
| true_ret | -0.0462 | -0.46 | 52% | 27 | -0.69% | ⚠️ flips / too few dates |
| n_pos | -0.0460 | -0.62 | 69% | 29 | n/a | ✅ consistent |
| d_Performance (YTD) | -0.0456 | -0.44 | 56% | 27 | -0.72% | ⚠️ flips / too few dates |
| exit_price_3d | +0.0455 | +0.70 | 70% | 27 | n/a | ✅ consistent |
| Profit Margin | +0.0450 | +0.46 | 69% | 29 | -2.64% | ✅ consistent |
| Beta | -0.0439 | -0.23 | 57% | 28 | -1.25% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0431 | -0.44 | 52% | 27 | -0.43% | ⚠️ flips / too few dates |
| exit_price_2d | +0.0428 | +0.65 | 68% | 28 | n/a | ✅ consistent |
| Performance (Week) | -0.0425 | -0.30 | 62% | 29 | -1.34% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0422 | +0.64 | 69% | 29 | n/a | ✅ consistent |
| d_Relative Strength Index (14) | -0.0412 | -0.46 | 67% | 27 | -0.88% | ✅ consistent |
| d_Forward P/E | -0.0397 | -0.40 | 67% | 27 | -0.22% | ✅ consistent |
| d_Price | -0.0367 | -0.34 | 56% | 27 | -0.69% | ⚠️ flips / too few dates |
| w_pos | -0.0366 | -0.46 | 69% | 29 | n/a | ✅ consistent |
| Average Volume | -0.0366 | -0.59 | 69% | 29 | n/a | ✅ consistent |
| d_Market Cap | -0.0351 | -0.54 | 70% | 27 | -0.75% | ✅ consistent |
| valuation_score | -0.0345 | -0.39 | 69% | 29 | +1.08% | ✅ consistent |
| Performance (YTD) | +0.0291 | +0.31 | 62% | 29 | -1.74% | ⚠️ flips / too few dates |
| total_score | -0.0284 | -0.39 | 76% | 29 | -0.51% | ✅ consistent |
| Market Cap | +0.0280 | +0.45 | 66% | 29 | n/a | ⚠️ flips / too few dates |
| Short Float | -0.0272 | -0.24 | 52% | 29 | n/a | ⚠️ flips / too few dates |
| Price | +0.0261 | +0.39 | 59% | 29 | n/a | ⚠️ flips / too few dates |
| entry_price | +0.0261 | +0.39 | 59% | 29 | n/a | ⚠️ flips / too few dates |

## Factor ranking — 2d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_2d | -1.0000 | -15887206158167322.00 | 100% | 28 | -9.57% | ✅ consistent |
| short_fwd_3d | -0.7268 | -9.39 | 100% | 27 | -8.54% | ✅ consistent |
| short_fwd_1d | -0.6171 | -7.61 | 100% | 28 | -5.65% | ✅ consistent |
| Volatility (Month) | -0.0830 | -0.65 | 70% | 27 | +0.87% | ✅ consistent |
| Profit Margin | +0.0594 | +0.67 | 75% | 28 | -4.99% | ✅ consistent |
| n_pos | -0.0592 | -0.68 | 75% | 28 | n/a | ✅ consistent |
| Beta | -0.0587 | -0.31 | 67% | 27 | -2.55% | ✅ consistent |
| exit_price_3d | +0.0584 | +0.97 | 78% | 27 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0566 | -0.45 | 69% | 26 | -1.16% | ✅ consistent |
| exit_price_2d | +0.0561 | +0.91 | 79% | 28 | n/a | ✅ consistent |
| w_pos | -0.0541 | -0.67 | 71% | 28 | n/a | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0538 | -0.40 | 62% | 26 | -1.29% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0538 | -0.41 | 58% | 26 | -0.68% | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0495 | -0.48 | 69% | 26 | -1.76% | ✅ consistent |
| d_Performance (YTD) | -0.0482 | -0.37 | 65% | 26 | -1.58% | ⚠️ flips / too few dates |
| true_ret | -0.0481 | -0.37 | 58% | 26 | -1.49% | ⚠️ flips / too few dates |
| Average Volume | -0.0478 | -0.82 | 79% | 28 | n/a | ✅ consistent |
| d_Price | -0.0465 | -0.36 | 62% | 26 | -1.49% | ⚠️ flips / too few dates |
| valuation_score | -0.0461 | -0.58 | 64% | 28 | +1.94% | ⚠️ flips / too few dates |
| d_20-Day Simple Moving Average | -0.0452 | -0.36 | 58% | 26 | -0.95% | ⚠️ flips / too few dates |
| exit_price_1d | +0.0447 | +0.71 | 71% | 28 | n/a | ✅ consistent |
| Performance (Week) | -0.0439 | -0.31 | 57% | 28 | -2.25% | ⚠️ flips / too few dates |
| total_score | -0.0418 | -0.49 | 61% | 28 | -1.07% | ⚠️ flips / too few dates |
| d_Forward P/E | -0.0403 | -0.35 | 65% | 26 | -0.31% | ⚠️ flips / too few dates |
| Short Float | -0.0374 | -0.36 | 61% | 28 | n/a | ⚠️ flips / too few dates |
| Performance (YTD) | +0.0374 | +0.42 | 68% | 28 | -3.28% | ✅ consistent |
| Forward P/E | -0.0372 | -0.39 | 64% | 28 | n/a | ⚠️ flips / too few dates |
| d_Market Cap | -0.0370 | -0.45 | 69% | 26 | -2.24% | ✅ consistent |
| upside_pct | -0.0361 | -0.29 | 54% | 28 | +1.82% | ⚠️ flips / too few dates |
| upside_pct_lvl | -0.0361 | -0.29 | 54% | 28 | +1.82% | ⚠️ flips / too few dates |

## Factor ranking — 3d forward returns

| Factor | Mean IC | ICIR | Sign cons. | Dates | Spread | Verdict |
|---|---|---|---|---|---|---|
| short_fwd_3d | -1.0000 | -16547281639269260.00 | 100% | 27 | -12.19% | ✅ consistent |
| short_fwd_2d | -0.7268 | -9.39 | 100% | 27 | -8.68% | ✅ consistent |
| short_fwd_1d | -0.4844 | -4.34 | 100% | 27 | -4.88% | ✅ consistent |
| Volatility (Month) | -0.1069 | -0.87 | 73% | 26 | +1.38% | ✅ consistent |
| Beta | -0.0793 | -0.46 | 62% | 26 | -3.86% | ⚠️ flips / too few dates |
| d_Performance (Week) | -0.0752 | -0.52 | 80% | 25 | -0.50% | ✅ consistent |
| Profit Margin | +0.0750 | +0.98 | 85% | 27 | -6.58% | ✅ consistent |
| exit_price_3d | +0.0666 | +1.11 | 85% | 27 | n/a | ✅ consistent |
| w_pos | -0.0622 | -0.65 | 70% | 27 | n/a | ✅ consistent |
| n_pos | -0.0613 | -0.61 | 67% | 27 | n/a | ✅ consistent |
| d_50-Day Simple Moving Average | -0.0580 | -0.43 | 72% | 25 | -1.07% | ✅ consistent |
| Average Volume | -0.0574 | -1.02 | 78% | 27 | n/a | ✅ consistent |
| exit_price_2d | +0.0572 | +0.94 | 85% | 27 | n/a | ✅ consistent |
| valuation_score | -0.0569 | -0.74 | 78% | 27 | +2.65% | ✅ consistent |
| d_200-Day Simple Moving Average | -0.0551 | -0.39 | 68% | 25 | -1.19% | ✅ consistent |
| d_Performance (Month) | -0.0522 | -0.43 | 80% | 25 | -1.20% | ✅ consistent |
| upside_pct | -0.0502 | -0.44 | 70% | 27 | +2.49% | ✅ consistent |
| upside_pct_lvl | -0.0502 | -0.44 | 70% | 27 | +2.48% | ✅ consistent |
| d_Performance (YTD) | -0.0495 | -0.34 | 72% | 25 | -1.62% | ✅ consistent |
| Short Float | -0.0492 | -0.50 | 67% | 27 | n/a | ✅ consistent |
| true_ret | -0.0483 | -0.34 | 72% | 25 | -1.55% | ✅ consistent |
| exit_price_1d | +0.0482 | +0.78 | 78% | 27 | n/a | ✅ consistent |
| Forward P/E | -0.0480 | -0.50 | 59% | 27 | n/a | ⚠️ flips / too few dates |
| d_Relative Strength Index (14) | -0.0472 | -0.45 | 72% | 25 | -1.79% | ✅ consistent |
| total_score | -0.0463 | -0.41 | 67% | 27 | -1.13% | ✅ consistent |
| d_Price | -0.0461 | -0.34 | 72% | 25 | -1.55% | ✅ consistent |
| d_20-Day Simple Moving Average | -0.0459 | -0.34 | 68% | 25 | -0.70% | ✅ consistent |
| Performance (YTD) | +0.0443 | +0.45 | 74% | 27 | -4.37% | ✅ consistent |
| price_score | -0.0427 | -0.35 | 68% | 25 | -2.15% | ✅ consistent |
| 200-Day Simple Moving Average | +0.0418 | +0.46 | 67% | 27 | -4.34% | ✅ consistent |

## What to do with this

- ✅ consistent factors with positive IC → candidates to ADD or UP-WEIGHT in the rubric (weight_learner handles rubric fields automatically).
- ✅ consistent with negative IC → candidates to DOWN-WEIGHT or invert.
- ⚠️ flips → leave alone; single-date heroes are usually noise.
- `d_*` columns are day-over-day deltas; bare names are levels; `cat_*` are catalyst keyword flags (0/1).

