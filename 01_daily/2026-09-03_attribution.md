# Factor attribution — signal 2026-09-03 → prediction day 2026-09-04

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-03** | Features/scores formed from this snapshot (and deltas vs **2026-09-02**). Only data on/before this date. |
| **Prediction day** | **2026-09-04** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-03 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-04 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11630** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0656**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.19% | 20.1% | 2358 |
| 2 | 0.08% | 8.2% | 3258 |
| 3 | 0.12% | 9.9% | 2161 |
| 4 | 1.06% | 23.1% | 1557 |
| 5 | 2.31% | 19.6% | 2296 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | -0.2357 | -0.1836 | -0.1945 | -0.07% | 1.41% | 5551/5851 |
| Relative Strength Index (14) | -0.2343 | -0.1251 | -0.0631 | 0.69% | n/a | 11528/0 |
| Performance (Week) | -0.1731 | -0.2273 | -0.0152 | 1.26% | 0.32% | 4612/6849 |
| d_Relative Strength Index (14) | -0.1653 | -0.2503 | +0.1629 | 0.68% | 0.79% | 7973/3198 |
| d_200-Day Simple Moving Average | -0.1508 | -0.0279 | -0.1919 | 0.76% | 0.51% | 8123/3367 |
| d_Performance (Week) | -0.1460 | -0.0732 | -0.1483 | 0.83% | 0.46% | 7466/3910 |
| true_ret | -0.1452 | -0.0251 | -0.1962 | 0.67% | 0.50% | 7931/3164 |
| d_Performance (YTD) | -0.1336 | -0.0376 | -0.1582 | 0.68% | 0.80% | 8001/3204 |
| d_Price | -0.1217 | -0.1136 | -0.0439 | 0.67% | 0.50% | 7931/3164 |
| upside_pct_lvl | +0.1086 | +0.3477 | -0.2172 | 0.49% | -0.12% | 4306/345 |
| d_50-Day Simple Moving Average | -0.1070 | +0.0332 | -0.1933 | 0.72% | 0.61% | 8188/3329 |
| d_20-Day Simple Moving Average | -0.1060 | +0.0261 | -0.1911 | 0.71% | 0.63% | 8228/3278 |
| d_Forward P/E | -0.0859 | +0.0149 | -0.0983 | 0.12% | 0.35% | 1925/1016 |
| d_Market Cap | -0.0839 | -0.0533 | -0.0198 | 1.75% | 0.72% | 3300/2383 |
| d_Performance (Quarter) | -0.0822 | -0.0290 | -0.0875 | 1.14% | 0.17% | 5655/5181 |
| d_Target Price | -0.0683 | -0.0663 | -0.0252 | -0.58% | 0.61% | 156/118 |
| d_Volatility (Month) | -0.0561 | -0.1584 | +0.0523 | 2.08% | 0.22% | 3130/6541 |
| Short Float | +0.0498 | +0.1418 | -0.1592 | 1.33% | n/a | 5696/0 |
| d_Analyst Recom | -0.0372 | -0.0140 | +0.0045 | -0.46% | 0.25% | 92/71 |
| Relative Volume | -0.0344 | +0.0263 | -0.0722 | 0.70% | n/a | 11308/0 |
| d_Relative Volume | -0.0342 | +0.0697 | -0.0760 | 1.19% | 0.28% | 5342/5836 |
| d_Beta | -0.0336 | -0.0063 | -0.0556 | 5.16% | 0.28% | 1216/1246 |
| Institutional Transactions | +0.0240 | +0.0554 | -0.0393 | 2.31% | 0.09% | 3183/1858 |
| d_Total Debt/Equity | +0.0208 | -0.0002 | +0.0362 | 1.90% | 0.34% | 13/18 |
| d_Short Ratio | -0.0204 | +0.0679 | -0.0751 | 0.12% | 2.22% | 4229/2809 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 331 | 18.25% | 41.1% |
| true_ret>3% & UPTREND | 509 | -1.57% | 13.8% |
| true_ret>3% & MIXED | 343 | -1.37% | 19.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 252 | -1.40% | -3.65% |
| WASHED | 737 | 0.66% | 0.49% |
