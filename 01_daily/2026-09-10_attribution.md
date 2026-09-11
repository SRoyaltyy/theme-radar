# Factor attribution — signal 2026-09-10 → prediction day 2026-09-11

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-10** | Features/scores formed from this snapshot (and deltas vs **2026-09-09**). Only data on/before this date. |
| **Prediction day** | **2026-09-11** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-10 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-11 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11616** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0932**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 4.84% | 28.3% | 2357 |
| 2 | 0.48% | 8.8% | 3832 |
| 3 | 0.27% | 19.1% | 935 |
| 4 | 0.43% | 12.1% | 2430 |
| 5 | 0.16% | 21.9% | 2062 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Price | -0.2200 | -0.1284 | -0.1204 | 0.09% | 1.65% | 2286/8860 |
| d_200-Day Simple Moving Average | -0.1812 | -0.2362 | +0.0349 | 0.10% | 1.61% | 2438/9068 |
| d_Performance (Quarter) | +0.1788 | +0.1693 | +0.0393 | 0.64% | 1.94% | 5364/5564 |
| d_Performance (YTD) | -0.1780 | -0.2339 | +0.0421 | 0.09% | 1.62% | 2354/8929 |
| d_Performance (Week) | -0.1651 | -0.2617 | +0.0927 | 0.09% | 1.57% | 2145/9297 |
| d_50-Day Simple Moving Average | -0.1641 | -0.2392 | +0.0533 | 0.07% | 1.62% | 2506/9010 |
| true_ret | -0.1522 | -0.2623 | +0.0941 | 0.09% | 1.65% | 2286/8860 |
| d_20-Day Simple Moving Average | -0.1441 | -0.2230 | +0.0530 | 0.13% | 1.65% | 2747/8782 |
| d_Performance (Month) | -0.1061 | -0.2109 | +0.0843 | 0.18% | 1.66% | 2761/8572 |
| d_Market Cap | -0.0784 | -0.0503 | -0.0240 | 0.19% | 2.84% | 1851/3865 |
| Short Float | +0.0748 | +0.1944 | -0.1337 | 1.99% | n/a | 5709/0 |
| upside_pct_lvl | -0.0719 | +0.3296 | -0.4595 | 2.62% | 0.45% | 4390/258 |
| d_Relative Strength Index (14) | -0.0718 | +0.1546 | -0.2697 | 0.09% | 1.63% | 2366/8894 |
| d_Forward P/E | -0.0602 | -0.1607 | +0.1297 | 0.56% | 0.66% | 990/1941 |
| Performance (Month) | -0.0536 | -0.1605 | +0.1337 | 0.35% | 1.69% | 3368/8052 |
| d_Short Float | +0.0446 | +0.0348 | +0.0348 | 0.37% | 4.43% | 3174/2306 |
| d_Average Volume | -0.0359 | -0.0768 | +0.0534 | 2.76% | 0.43% | 4227/6787 |
| d_EPS Surprise | -0.0352 | -0.0546 | +0.0119 | -0.95% | 2.37% | 6/13 |
| Performance (Week) | +0.0276 | -0.0348 | +0.1406 | 0.64% | 1.54% | 3055/8372 |
| d_Total Debt/Equity | -0.0266 | -0.0453 | +0.0050 | 1.30% | 1.72% | 10/17 |
| d_Analyst Recom | -0.0259 | +0.0195 | -0.0488 | -0.01% | 0.85% | 59/100 |
| Relative Strength Index (14) | +0.0247 | +0.0569 | -0.1932 | 1.29% | n/a | 11535/0 |
| d_Beta | -0.0218 | -0.0108 | -0.0530 | 5.90% | 0.56% | 1747/1163 |
| Institutional Transactions | -0.0203 | +0.0525 | -0.0827 | 2.63% | 0.37% | 3199/1831 |
| d_Sales Year Over Year TTM | +0.0138 | +0.0109 | -0.0125 | 1.70% | 1.21% | 9/13 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 217 | -0.52% | 28.1% |
| true_ret>3% & UPTREND | 141 | -0.15% | 31.2% |
| true_ret>3% & MIXED | 73 | -0.55% | 27.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 204 | 0.15% | -0.25% |
| WASHED | 1567 | 0.27% | -0.14% |
