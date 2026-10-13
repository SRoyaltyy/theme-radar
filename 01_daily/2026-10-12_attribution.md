# Factor attribution — signal 2026-10-12 → prediction day 2026-10-13

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-12** | Features/scores formed from this snapshot (and deltas vs **2026-10-09**). Only data on/before this date. |
| **Prediction day** | **2026-10-13** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-12 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-13 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11712** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.1197**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.42% | 13.8% | 2351 |
| 2 | -0.29% | 5.0% | 2831 |
| 3 | -0.31% | 5.6% | 2588 |
| 4 | -0.17% | 8.6% | 1867 |
| 5 | -0.35% | 15.9% | 2075 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.3404 | +0.2203 | -0.5967 | -1.02% | 0.34% | 4353/279 |
| d_50-Day Simple Moving Average | +0.2353 | +0.0333 | +0.2980 | -0.05% | -0.21% | 5038/6499 |
| true_ret | +0.2333 | -0.0014 | +0.3355 | -0.06% | -0.18% | 4674/6334 |
| d_Performance (YTD) | +0.2279 | +0.0072 | +0.2842 | -0.05% | -0.19% | 4758/6429 |
| d_200-Day Simple Moving Average | +0.2250 | +0.0231 | +0.2784 | -0.09% | -0.17% | 4877/6623 |
| d_20-Day Simple Moving Average | +0.2212 | +0.0721 | +0.2525 | -0.12% | -0.17% | 5335/6203 |
| Performance (Week) | +0.2198 | -0.0685 | +0.3420 | -0.08% | -0.20% | 5500/6037 |
| d_Price | +0.2017 | +0.0254 | +0.1700 | -0.06% | -0.18% | 4674/6334 |
| d_Relative Strength Index (14) | +0.1920 | +0.0021 | +0.1798 | -0.06% | -0.19% | 4777/6433 |
| d_Market Cap | +0.1646 | -0.0242 | +0.1958 | -0.18% | -0.06% | 2480/3241 |
| d_Performance (Quarter) | +0.1580 | -0.0035 | +0.1929 | -0.22% | -0.06% | 3893/7251 |
| d_Performance (Week) | +0.1480 | -0.0103 | +0.1898 | -0.32% | -0.04% | 4107/7376 |
| Relative Strength Index (14) | +0.1319 | -0.0864 | +0.3607 | -0.14% | n/a | 11628/0 |
| d_Performance (Month) | +0.1291 | -0.0283 | +0.1714 | -0.39% | -0.01% | 3845/7591 |
| Institutional Transactions | -0.1282 | +0.0267 | -0.1505 | 0.12% | -0.29% | 3263/1778 |
| d_Beta | +0.1232 | -0.0428 | +0.2101 | -0.25% | 0.67% | 1012/1911 |
| Performance (Month) | +0.1194 | -0.2301 | +0.3807 | -0.21% | -0.11% | 3891/7639 |
| d_Forward P/E | +0.1052 | -0.0301 | +0.2034 | 0.20% | -0.18% | 1583/1345 |
| Short Float | -0.1014 | +0.1398 | -0.1870 | -0.11% | n/a | 5667/0 |
| d_Institutional Ownership | +0.0917 | -0.0831 | +0.1690 | -0.46% | -0.71% | 2401/640 |
| d_Short Float | -0.0591 | -0.0320 | -0.0361 | -0.99% | 0.86% | 2897/2619 |
| d_Short Ratio | -0.0265 | +0.0083 | -0.0589 | -0.63% | 0.37% | 5674/5463 |
| d_Sales Year Over Year TTM | -0.0224 | +0.0178 | +0.0012 | -2.06% | 0.57% | 3/1 |
| d_Sales Growth Quarter Over Quarter | -0.0219 | +0.0072 | -0.0164 | -1.45% | 0.45% | 4/5 |
| d_Institutional Transactions | +0.0210 | -0.0769 | +0.0323 | -0.81% | 2.11% | 3102/1308 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 155 | -1.08% | 25.8% |
| true_ret>3% & UPTREND | 126 | -0.59% | 37.3% |
| true_ret>3% & MIXED | 97 | -1.06% | 29.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 173 | 0.17% | -1.06% |
| WASHED | 1192 | 0.99% | -1.82% |
