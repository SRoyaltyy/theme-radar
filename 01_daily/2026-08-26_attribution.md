# Factor attribution — signal 2026-08-26 → prediction day 2026-09-01

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-26** | Features/scores formed from this snapshot (and deltas vs **2026-08-25**). Only data on/before this date. |
| **Prediction day** | **2026-09-01** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-26 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-01 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11585** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0019**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 4.87% | 14.5% | 2438 |
| 2 | -0.22% | 10.1% | 2602 |
| 3 | -1.18% | 5.0% | 1948 |
| 4 | -0.30% | 6.8% | 2304 |
| 5 | 3.32% | 18.3% | 2293 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | -0.2276 | +0.2689 | -0.2690 | 3.93% | n/a | 5692/0 |
| upside_pct_lvl | -0.1807 | +0.2356 | -0.3373 | 0.83% | -1.04% | 4304/338 |
| Relative Strength Index (14) | +0.1475 | -0.1937 | +0.2328 | 1.41% | n/a | 11461/0 |
| d_Performance (Quarter) | +0.0890 | +0.0831 | +0.0619 | 1.27% | 2.05% | 5130/5645 |
| d_20-Day Simple Moving Average | +0.0884 | -0.0512 | +0.1253 | 3.92% | 0.13% | 3847/7588 |
| d_Average Volume | +0.0749 | -0.1324 | +0.1852 | 5.09% | 0.29% | 2538/8701 |
| true_ret | +0.0710 | -0.0484 | +0.1051 | 0.69% | 0.50% | 4641/6212 |
| d_Performance (YTD) | +0.0681 | -0.0416 | +0.0941 | 1.45% | 1.47% | 4775/6318 |
| d_200-Day Simple Moving Average | +0.0667 | -0.0214 | +0.0825 | 2.27% | 0.85% | 4512/6853 |
| d_Volatility (Month) | +0.0664 | -0.1159 | +0.1419 | 4.66% | 0.35% | 3066/6474 |
| d_Price | +0.0614 | -0.0322 | +0.0551 | 0.69% | 0.50% | 4641/6212 |
| d_Performance (Week) | +0.0525 | -0.1120 | +0.0887 | 2.93% | 0.57% | 4076/7280 |
| d_Beta | -0.0506 | -0.0038 | -0.0706 | 0.10% | 22.25% | 1789/1131 |
| d_Institutional Ownership | -0.0499 | -0.0301 | -0.0301 | -2.83% | 7.76% | 1242/913 |
| Institutional Transactions | -0.0473 | +0.0924 | -0.0791 | 7.99% | 0.24% | 3173/1878 |
| d_50-Day Simple Moving Average | +0.0442 | -0.0392 | +0.0667 | 2.60% | 0.57% | 4712/6671 |
| Relative Volume | -0.0395 | +0.1047 | -0.0674 | 1.41% | n/a | 11326/0 |
| d_Relative Volume | +0.0321 | +0.0075 | +0.0234 | 4.37% | -1.07% | 5013/6080 |
| d_Analyst Recom | +0.0309 | -0.0620 | -0.0009 | -1.60% | -2.75% | 74/72 |
| d_Target Price | +0.0305 | +0.0413 | +0.0068 | -1.52% | -2.96% | 155/70 |
| d_Relative Strength Index (14) | +0.0284 | -0.0208 | -0.0066 | 1.46% | 1.51% | 4770/6313 |
| Performance (Week) | +0.0263 | -0.1158 | +0.0766 | -0.00% | 2.77% | 5470/5880 |
| d_EPS Surprise | +0.0219 | +0.0456 | +0.0102 | 0.11% | -3.05% | 38/27 |
| d_Market Cap | +0.0215 | -0.0412 | +0.0340 | 4.78% | 3.95% | 2502/3186 |
| d_Short Ratio | -0.0165 | +0.0323 | -0.0152 | 1.65% | 0.16% | 5424/5560 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 231 | 34.29% | 24.2% |
| true_ret>3% & UPTREND | 163 | 10.31% | 23.3% |
| true_ret>3% & MIXED | 136 | -4.21% | 17.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 400 | 2.45% | 20.01% |
| WASHED | 423 | 51.64% | 92.68% |
