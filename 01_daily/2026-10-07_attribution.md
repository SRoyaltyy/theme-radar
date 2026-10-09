# Factor attribution — signal 2026-10-07 → prediction day 2026-10-09

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-07** | Features/scores formed from this snapshot (and deltas vs **2026-10-06**). Only data on/before this date. |
| **Prediction day** | **2026-10-09** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-07 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-09 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11703** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0495**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.50% | 24.7% | 2626 |
| 2 | 0.01% | 14.7% | 2330 |
| 3 | 0.20% | 15.0% | 2536 |
| 4 | 0.13% | 15.4% | 1880 |
| 5 | 0.47% | 34.4% | 2331 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2053 | +0.2086 | -0.4634 | -0.14% | 0.85% | 4384/252 |
| d_Performance (Month) | +0.1708 | +0.0126 | +0.2483 | 0.71% | -0.48% | 5091/6319 |
| d_Forward P/E | +0.1264 | +0.0524 | +0.1331 | 1.02% | 0.43% | 785/2160 |
| Relative Strength Index (14) | -0.1197 | -0.0590 | +0.1541 | 0.05% | n/a | 11612/0 |
| d_20-Day Simple Moving Average | +0.0932 | -0.1396 | +0.1985 | 0.34% | -0.06% | 3267/8335 |
| d_Performance (Quarter) | +0.0926 | -0.1720 | +0.1906 | 0.23% | 0.05% | 2271/8849 |
| d_50-Day Simple Moving Average | +0.0877 | -0.1736 | +0.2135 | 0.37% | -0.06% | 2943/8655 |
| true_ret | +0.0796 | -0.2004 | +0.2538 | 0.37% | -0.05% | 2496/8609 |
| d_Beta | +0.0734 | -0.0358 | +0.1271 | 0.20% | -0.23% | 985/1606 |
| d_Volatility (Month) | +0.0717 | +0.1274 | -0.0504 | 0.39% | -0.50% | 5304/3946 |
| Performance (Month) | -0.0681 | -0.2971 | +0.1942 | -0.25% | 0.19% | 3495/8024 |
| Relative Volume | +0.0615 | +0.0583 | -0.0440 | 0.05% | n/a | 11433/0 |
| Institutional Transactions | -0.0613 | +0.0412 | -0.0927 | 0.02% | 0.29% | 3243/1802 |
| d_200-Day Simple Moving Average | +0.0603 | -0.1772 | +0.1671 | 0.41% | -0.05% | 2749/8801 |
| d_Performance (YTD) | +0.0556 | -0.1780 | +0.1556 | 0.38% | -0.07% | 2583/8707 |
| d_Performance (Week) | +0.0536 | -0.1311 | +0.1694 | -0.01% | 0.02% | 4020/7443 |
| Performance (Week) | +0.0399 | -0.0732 | +0.1582 | 0.01% | 0.10% | 6200/5313 |
| d_Insider Transactions | -0.0377 | -0.0413 | -0.0253 | -1.14% | -0.55% | 126/166 |
| d_Market Cap | -0.0344 | +0.0744 | -0.0829 | 0.22% | 0.14% | 1666/4057 |
| d_Institutional Ownership | +0.0328 | +0.0093 | -0.0182 | 0.81% | 0.36% | 517/499 |
| d_Sales Growth Quarter Over Quarter | +0.0297 | +0.0026 | -0.0063 | 2.13% | -1.48% | 6/3 |
| d_Analyst Recom | -0.0274 | -0.0512 | +0.0059 | -0.91% | 0.64% | 69/62 |
| d_Sales Year Over Year TTM | +0.0233 | +0.0296 | +0.0331 | 2.20% | -1.08% | 5/3 |
| d_Relative Strength Index (14) | +0.0218 | +0.0453 | -0.0517 | 0.32% | -0.08% | 2615/8682 |
| Short Float | +0.0199 | +0.1995 | -0.1300 | 0.21% | n/a | 5691/0 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 223 | -1.04% | 35.9% |
| true_ret>3% & UPTREND | 110 | -1.54% | 31.8% |
| true_ret>3% & MIXED | 88 | 4.84% | 34.1% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 182 | -1.78% | -2.31% |
| WASHED | 1836 | -0.40% | -0.93% |
