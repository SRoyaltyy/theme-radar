# Factor attribution — signal 2026-09-09 → prediction day 2026-09-11

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-09** | Features/scores formed from this snapshot (and deltas vs **2026-09-08**). Only data on/before this date. |
| **Prediction day** | **2026-09-11** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-09 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-11 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11598** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0188**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.20% | 16.0% | 2774 |
| 2 | -0.62% | 7.8% | 2122 |
| 3 | 2.99% | 8.4% | 2194 |
| 4 | -0.43% | 8.9% | 2321 |
| 5 | 1.49% | 19.9% | 2187 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.1808 | +0.2479 | -0.3897 | 1.47% | -0.19% | 4368/278 |
| d_Performance (Week) | -0.0888 | -0.0676 | -0.0479 | 0.11% | 1.29% | 6562/4840 |
| d_Relative Strength Index (14) | -0.0793 | +0.2009 | -0.1616 | 0.48% | 0.67% | 2301/8925 |
| d_Price | -0.0764 | -0.0090 | -0.0603 | 0.50% | 0.58% | 2252/8892 |
| Short Float | -0.0554 | +0.1491 | -0.2170 | 1.27% | n/a | 5681/0 |
| d_Market Cap | -0.0492 | +0.0348 | -0.0652 | 0.65% | 1.45% | 1503/4221 |
| d_EPS Surprise | +0.0481 | +0.0694 | +0.0407 | 0.98% | -4.91% | 27/19 |
| Institutional Transactions | -0.0462 | +0.0413 | -0.0972 | 1.85% | -0.17% | 3198/1831 |
| d_Performance (Quarter) | -0.0443 | -0.1183 | -0.0022 | -0.20% | 1.09% | 3418/7477 |
| Performance (Week) | -0.0442 | -0.0525 | -0.0240 | -0.28% | 1.56% | 5834/5547 |
| d_Short Ratio | -0.0332 | +0.0065 | -0.0352 | -0.34% | 1.25% | 3816/4191 |
| d_Institutional Ownership | -0.0321 | +0.0259 | -0.0416 | -0.08% | -0.09% | 473/710 |
| d_Total Debt/Equity | -0.0313 | -0.0603 | -0.0097 | -1.16% | 2.52% | 15/16 |
| d_Sales Year Over Year TTM | -0.0287 | -0.0320 | -0.0245 | -0.98% | 3.34% | 17/17 |
| Performance (Month) | -0.0287 | -0.1440 | +0.0501 | -0.29% | 1.11% | 4018/7371 |
| d_200-Day Simple Moving Average | -0.0282 | -0.1865 | +0.1078 | 0.40% | 0.67% | 2394/9080 |
| Relative Strength Index (14) | +0.0277 | -0.1298 | -0.0762 | 0.61% | n/a | 11521/0 |
| d_Volatility (Month) | +0.0247 | -0.0492 | +0.0583 | 1.44% | 0.30% | 4308/4863 |
| d_Sales Growth Quarter Over Quarter | -0.0234 | -0.0188 | -0.0158 | -0.04% | 2.18% | 17/19 |
| d_Performance (YTD) | -0.0227 | -0.1842 | +0.1119 | 0.48% | 0.68% | 2301/8952 |
| d_Beta | +0.0214 | -0.0474 | +0.0215 | -0.75% | -0.53% | 1280/1456 |
| d_Profit Margin | +0.0213 | +0.0570 | +0.0143 | 0.72% | 0.12% | 28/10 |
| d_50-Day Simple Moving Average | -0.0195 | -0.2016 | +0.1319 | 0.73% | 0.57% | 2484/9001 |
| Relative Volume | -0.0159 | +0.1320 | -0.0229 | 0.62% | n/a | 11336/0 |
| d_Relative Volume | +0.0138 | -0.0250 | +0.0505 | 1.23% | 0.15% | 4998/6200 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 149 | 4.91% | 31.5% |
| true_ret>3% & UPTREND | 154 | -2.26% | 18.2% |
| true_ret>3% & MIXED | 83 | -0.79% | 26.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 222 | -1.96% | -2.51% |
| WASHED | 954 | 1.06% | 7.92% |
