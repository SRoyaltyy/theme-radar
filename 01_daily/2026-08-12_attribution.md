# Factor attribution — signal 2026-08-12 → prediction day 2026-08-14

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-12** | Features/scores formed from this snapshot (and deltas vs **2026-08-11**). Only data on/before this date. |
| **Prediction day** | **2026-08-14** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-12 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-14 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11552** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0520**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.58% | 28.8% | 2331 |
| 2 | 0.32% | 12.5% | 3051 |
| 3 | 0.54% | 11.6% | 1646 |
| 4 | 0.70% | 14.5% | 2357 |
| 5 | 1.87% | 34.0% | 2167 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | +0.1544 | +0.1938 | -0.0006 | 1.27% | 1.64% | 7138/4148 |
| d_Beta | +0.0786 | +0.0690 | +0.0480 | 1.01% | 7.38% | 1992/1249 |
| Short Float | +0.0786 | +0.2399 | -0.1757 | 2.35% | n/a | 5702/0 |
| d_Price | +0.0641 | -0.0276 | +0.0370 | 0.84% | 2.43% | 7105/3868 |
| d_20-Day Simple Moving Average | +0.0520 | +0.0514 | -0.0091 | 1.37% | 1.44% | 6994/4431 |
| d_Performance (YTD) | +0.0500 | +0.0398 | -0.0073 | 0.84% | 2.45% | 7198/3939 |
| Relative Volume | +0.0486 | +0.1489 | -0.0879 | 1.41% | n/a | 11261/0 |
| true_ret | +0.0469 | +0.0456 | -0.0077 | 0.84% | 2.43% | 7105/3868 |
| d_200-Day Simple Moving Average | +0.0368 | +0.0528 | -0.0397 | 1.25% | 1.65% | 7330/4064 |
| d_Performance (Quarter) | +0.0362 | +0.0924 | -0.0655 | 1.47% | 1.33% | 7475/3310 |
| d_50-Day Simple Moving Average | +0.0350 | +0.0570 | -0.0480 | 1.46% | 1.28% | 7260/4158 |
| Performance (Month) | -0.0301 | -0.0388 | +0.0019 | 0.65% | 2.59% | 6922/4387 |
| d_Performance (Month) | +0.0286 | +0.0334 | -0.0143 | 1.31% | 1.46% | 5037/6161 |
| d_Sales Year Over Year TTM | +0.0249 | -0.0187 | -0.0091 | 1.75% | 0.47% | 109/93 |
| d_Short Float | -0.0233 | -0.0248 | -0.0203 | 2.23% | 2.66% | 2401/3101 |
| Relative Strength Index (14) | -0.0225 | -0.2364 | +0.1091 | 1.38% | n/a | 11439/0 |
| d_Profit Margin | +0.0196 | -0.0017 | -0.0097 | 1.40% | 0.40% | 133/106 |
| d_Gross Margin | +0.0194 | -0.0104 | +0.0258 | 0.85% | 1.07% | 126/100 |
| d_Relative Strength Index (14) | +0.0167 | -0.1427 | +0.0610 | 0.83% | 2.46% | 7160/3947 |
| Institutional Transactions | +0.0161 | +0.0577 | -0.0453 | 1.24% | 3.96% | 2520/2519 |
| d_Institutional Ownership | +0.0150 | -0.0384 | +0.0325 | 0.87% | 2.86% | 2139/1545 |
| upside_pct_lvl | +0.0143 | +0.4079 | -0.3739 | 1.97% | 0.06% | 4291/354 |
| d_Relative Volume | -0.0138 | +0.0137 | -0.0296 | 0.68% | 2.23% | 5744/5321 |
| d_EPS Surprise | +0.0126 | +0.0190 | +0.0014 | 1.14% | 0.52% | 92/93 |
| d_Average Volume | -0.0109 | -0.0890 | +0.0178 | 2.88% | 0.57% | 4095/6899 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 382 | 5.60% | 41.1% |
| true_ret>3% & UPTREND | 377 | 0.93% | 37.7% |
| true_ret>3% & MIXED | 296 | 3.37% | 45.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 326 | -0.39% | -2.58% |
| WASHED | 545 | 15.39% | 4.15% |
