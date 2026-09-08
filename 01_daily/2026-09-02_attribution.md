# Factor attribution — signal 2026-09-02 → prediction day 2026-09-08

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-02** | Features/scores formed from this snapshot (and deltas vs **2026-09-01**). Only data on/before this date. |
| **Prediction day** | **2026-09-08** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-02 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-08 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11586** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.1700**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 7.09% | 43.9% | 2333 |
| 2 | 1.32% | 18.2% | 2302 |
| 3 | 0.26% | 13.0% | 2564 |
| 4 | 0.04% | 14.7% | 2139 |
| 5 | 3.07% | 24.6% | 2248 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | -0.2124 | -0.3146 | -0.0193 | 1.01% | 3.07% | 3632/7640 |
| Performance (Week) | -0.1339 | -0.3055 | +0.0340 | 1.83% | 2.65% | 3434/7952 |
| d_Volatility (Month) | -0.1065 | -0.3189 | +0.1287 | 3.01% | 2.64% | 3774/5897 |
| Performance (Month) | -0.0960 | -0.1489 | -0.0495 | 0.95% | 3.40% | 4697/6665 |
| Relative Strength Index (14) | -0.0902 | -0.0857 | -0.1020 | 2.38% | n/a | 11479/0 |
| upside_pct_lvl | +0.0847 | +0.4346 | -0.2229 | 1.67% | -1.44% | 4318/325 |
| d_Relative Strength Index (14) | -0.0835 | -0.2229 | +0.1136 | 1.41% | 4.90% | 7843/3299 |
| d_Forward P/E | -0.0603 | -0.0632 | -0.0260 | -0.13% | 0.31% | 2008/943 |
| d_Institutional Ownership | +0.0589 | +0.0302 | +0.0493 | 0.20% | 0.26% | 1874/531 |
| Institutional Transactions | +0.0565 | +0.0998 | -0.0585 | 5.43% | 1.38% | 3182/1856 |
| d_200-Day Simple Moving Average | -0.0561 | +0.0764 | -0.1077 | 1.46% | 4.58% | 8037/3410 |
| d_Performance (Week) | -0.0552 | +0.1115 | -0.1639 | 1.78% | 3.92% | 8007/3357 |
| Relative Volume | -0.0500 | -0.0107 | +0.0421 | 2.40% | n/a | 11351/0 |
| true_ret | -0.0475 | +0.0723 | -0.1008 | 1.26% | 4.78% | 7766/3234 |
| d_Performance (YTD) | -0.0436 | +0.0565 | -0.0681 | 1.42% | 4.90% | 7874/3309 |
| Short Float | -0.0339 | +0.2367 | -0.2171 | 3.33% | n/a | 5689/0 |
| d_Market Cap | -0.0311 | -0.0514 | +0.0228 | 1.80% | 6.16% | 3606/2095 |
| d_20-Day Simple Moving Average | -0.0301 | +0.1247 | -0.1088 | 1.56% | 4.42% | 8200/3284 |
| d_Sales Year Over Year TTM | +0.0258 | +0.0151 | +0.0146 | 0.78% | -4.04% | 9/9 |
| d_Price | -0.0239 | -0.0197 | +0.0330 | 1.26% | 4.78% | 7766/3234 |
| d_Gross Margin | +0.0234 | -0.0215 | +0.0108 | 0.70% | -2.86% | 12/10 |
| d_Sales Growth Quarter Over Quarter | +0.0232 | +0.0025 | +0.0098 | 0.80% | -2.68% | 8/11 |
| d_Short Float | -0.0230 | -0.0349 | -0.0099 | -3.41% | 0.43% | 43/79 |
| d_Beta | +0.0219 | -0.0003 | +0.0580 | 1.23% | 4.64% | 3793/2914 |
| d_EPS Surprise | +0.0194 | +0.0164 | +0.0070 | 2.52% | -0.67% | 23/17 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 442 | 4.04% | 44.8% |
| true_ret>3% & UPTREND | 432 | -0.37% | 28.0% |
| true_ret>3% & MIXED | 304 | 19.51% | 29.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 198 | -0.03% | -0.55% |
| WASHED | 836 | 12.86% | 1.59% |
