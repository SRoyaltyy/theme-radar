# Factor attribution — signal 2026-08-17 → prediction day 2026-08-18

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-17** | Features/scores formed from this snapshot (and deltas vs **2026-08-14**). Only data on/before this date. |
| **Prediction day** | **2026-08-18** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-17 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-18 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11559** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.2097**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 8.54% | 20.0% | 2389 |
| 2 | -0.44% | 6.8% | 2569 |
| 3 | -0.67% | 5.0% | 2742 |
| 4 | -1.41% | 7.7% | 1710 |
| 5 | -2.19% | 10.8% | 2149 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.3566 | -0.1134 | -0.3935 | -1.16% | 6.99% | 7737/3073 |
| d_Performance (Month) | -0.2647 | -0.1429 | -0.2496 | -1.43% | 3.91% | 6255/5001 |
| Performance (Week) | -0.2356 | -0.1193 | -0.2650 | -1.36% | 4.41% | 6854/4493 |
| Performance (Month) | -0.2202 | -0.0235 | -0.2445 | -1.30% | 4.91% | 7258/4072 |
| d_Forward P/E | -0.2196 | -0.1376 | -0.1641 | -1.86% | -0.43% | 946/2035 |
| d_Performance (Week) | -0.2156 | -0.1947 | -0.2286 | -1.55% | 3.19% | 5397/5921 |
| d_Relative Strength Index (14) | -0.2073 | +0.0865 | -0.3240 | -1.73% | 2.37% | 3809/7306 |
| d_50-Day Simple Moving Average | -0.1846 | -0.1749 | -0.1833 | -1.84% | 2.33% | 3907/7509 |
| d_Price | -0.1760 | -0.0263 | -0.2293 | -1.78% | 2.41% | 3758/7234 |
| d_Performance (YTD) | -0.1636 | -0.1481 | -0.1524 | -1.79% | 2.36% | 3839/7327 |
| true_ret | -0.1582 | -0.1911 | -0.1339 | -1.78% | 2.41% | 3758/7234 |
| d_200-Day Simple Moving Average | -0.1572 | -0.1445 | -0.1575 | -1.79% | 2.30% | 3873/7541 |
| d_Market Cap | -0.1437 | +0.0857 | -0.1832 | -0.90% | 5.29% | 2055/3681 |
| d_Volatility (Month) | +0.1001 | -0.0750 | +0.1633 | 0.63% | 1.46% | 2961/6551 |
| Relative Strength Index (14) | -0.0984 | -0.0770 | +0.1577 | 0.92% | n/a | 11438/0 |
| d_20-Day Simple Moving Average | -0.0943 | -0.1680 | -0.0692 | -1.61% | 2.02% | 3512/7914 |
| upside_pct_lvl | -0.0896 | +0.3151 | -0.3320 | 4.10% | -0.67% | 4310/337 |
| Short Float | -0.0843 | +0.1542 | -0.2127 | 3.09% | n/a | 5685/0 |
| d_Beta | -0.0676 | +0.0104 | -0.0728 | 7.27% | 2.50% | 1931/1503 |
| Institutional Transactions | -0.0348 | -0.0224 | -0.0423 | 1.02% | 6.32% | 2689/2352 |
| d_Relative Volume | +0.0284 | -0.0004 | +0.0278 | 1.65% | -0.06% | 6608/4526 |
| d_Profit Margin | +0.0276 | -0.0141 | +0.0309 | -1.19% | 43.57% | 84/104 |
| d_Analyst Recom | +0.0199 | -0.0031 | +0.0302 | -0.83% | -0.99% | 170/167 |
| d_Average Volume | +0.0198 | -0.0267 | +0.0607 | 4.02% | -0.92% | 4199/6780 |
| d_Short Float | +0.0174 | -0.0634 | +0.0574 | -0.21% | -0.59% | 178/359 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 216 | -0.43% | 22.2% |
| true_ret>3% & UPTREND | 338 | -5.06% | 16.0% |
| true_ret>3% & MIXED | 194 | -3.27% | 12.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 309 | -4.20% | -9.90% |
| WASHED | 492 | 44.19% | 4.30% |
