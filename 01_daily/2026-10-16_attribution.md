# Factor attribution — signal 2026-10-16 → prediction day 2026-10-20

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-16** | Features/scores formed from this snapshot (and deltas vs **2026-10-15**). Only data on/before this date. |
| **Prediction day** | **2026-10-20** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-16 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-20 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11733** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1901**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.19% | 34.9% | 2495 |
| 2 | 4.45% | 29.6% | 2247 |
| 3 | 0.61% | 24.5% | 2347 |
| 4 | 0.21% | 9.9% | 2655 |
| 5 | 0.00% | 20.2% | 1989 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Price | -0.3178 | -0.2885 | +0.1446 | -0.15% | 2.39% | 3295/7950 |
| d_Performance (YTD) | -0.3116 | -0.4257 | +0.1984 | -0.12% | 2.58% | 3351/8024 |
| d_200-Day Simple Moving Average | -0.3102 | -0.4349 | +0.1920 | -0.17% | 2.54% | 3508/8088 |
| d_20-Day Simple Moving Average | -0.3012 | -0.4426 | +0.1489 | 0.18% | 2.49% | 3859/7728 |
| d_Relative Strength Index (14) | -0.2984 | -0.0933 | +0.1458 | -0.15% | 2.56% | 3370/8002 |
| d_50-Day Simple Moving Average | -0.2890 | -0.4406 | +0.1861 | -0.15% | 2.63% | 3819/7796 |
| d_Performance (Week) | -0.2787 | -0.4165 | +0.1488 | 1.29% | 1.89% | 3154/8385 |
| true_ret | -0.2661 | -0.4705 | +0.2402 | -0.15% | 2.39% | 3295/7950 |
| d_Performance (Month) | -0.2231 | -0.3799 | +0.2349 | -0.05% | 2.25% | 2601/8873 |
| d_Market Cap | -0.2052 | -0.2794 | +0.0633 | -0.08% | 4.44% | 1871/3871 |
| d_Performance (Quarter) | -0.1987 | -0.2747 | +0.1170 | 1.09% | 2.26% | 4824/6369 |
| Short Float | +0.1974 | +0.3293 | -0.1337 | 2.99% | n/a | 5660/0 |
| d_Forward P/E | -0.1938 | -0.3497 | +0.1382 | 0.47% | 1.18% | 1160/1787 |
| Performance (Week) | -0.1134 | -0.3392 | +0.3389 | 0.34% | 2.56% | 4370/7205 |
| d_Volatility (Month) | +0.0637 | +0.2460 | -0.1485 | 2.98% | 0.83% | 5077/5012 |
| Relative Volume | +0.0633 | +0.0953 | +0.0234 | 1.73% | n/a | 11510/0 |
| d_Target Price | +0.0526 | +0.0747 | +0.0076 | 1.57% | 0.35% | 187/316 |
| Relative Strength Index (14) | -0.0425 | -0.2528 | +0.3203 | 1.71% | n/a | 11647/0 |
| upside_pct_lvl | -0.0371 | +0.3860 | -0.4996 | 4.10% | 0.85% | 4358/272 |
| Performance (Month) | +0.0280 | -0.2780 | +0.3865 | 0.66% | 2.16% | 3396/8143 |
| d_Profit Margin | +0.0241 | -0.0001 | +0.0266 | 0.58% | -1.77% | 14/16 |
| d_Insider Transactions | +0.0187 | -0.0017 | -0.0143 | 0.90% | 5.44% | 192/177 |
| Institutional Transactions | +0.0181 | +0.1246 | -0.1323 | 2.95% | 4.35% | 3260/1776 |
| d_Short Ratio | -0.0171 | -0.0666 | +0.0292 | 0.74% | 0.86% | 2672/4516 |
| d_Total Debt/Equity | +0.0169 | +0.0138 | +0.0346 | 0.80% | -1.74% | 10/14 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 166 | -3.18% | 22.9% |
| true_ret>3% & UPTREND | 111 | -0.38% | 17.1% |
| true_ret>3% & MIXED | 84 | -2.41% | 11.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 140 | -0.39% | 0.67% |
| WASHED | 1710 | 8.28% | -1.11% |
