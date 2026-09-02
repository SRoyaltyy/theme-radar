# Factor attribution — signal 2026-09-01 → prediction day 2026-09-02

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-01** | Features/scores formed from this snapshot (and deltas vs **2026-08-31**). Only data on/before this date. |
| **Prediction day** | **2026-09-02** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-01 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-02 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11620** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0847**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.68% | 25.6% | 2560 |
| 2 | 0.83% | 31.6% | 2135 |
| 3 | 0.44% | 10.2% | 2369 |
| 4 | 0.49% | 13.6% | 2639 |
| 5 | 0.51% | 25.9% | 1917 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.1764 | -0.3391 | +0.1270 | 0.34% | 0.66% | 2465/8981 |
| Short Float | +0.1749 | +0.2188 | -0.1071 | 0.79% | n/a | 5697/0 |
| d_Performance (Month) | -0.1537 | -0.3250 | +0.1977 | 0.39% | 0.65% | 2182/9097 |
| d_Performance (Quarter) | -0.1437 | -0.1334 | -0.0419 | 0.54% | 0.61% | 3097/7731 |
| d_200-Day Simple Moving Average | -0.1415 | -0.2295 | +0.1027 | 0.54% | 0.61% | 2453/9025 |
| d_Performance (Week) | -0.1376 | -0.2570 | +0.1470 | 0.36% | 0.66% | 2375/9054 |
| d_Performance (YTD) | -0.1363 | -0.2220 | +0.1103 | 0.57% | 0.61% | 2369/8911 |
| d_50-Day Simple Moving Average | -0.1221 | -0.2397 | +0.1352 | 0.55% | 0.60% | 2471/9042 |
| d_Price | -0.1204 | -0.0325 | -0.0074 | 0.56% | 0.61% | 2315/8850 |
| true_ret | -0.1148 | -0.2572 | +0.1801 | 0.56% | 0.61% | 2315/8850 |
| d_20-Day Simple Moving Average | -0.1032 | -0.2182 | +0.1478 | 0.55% | 0.60% | 2592/8909 |
| d_Market Cap | -0.0945 | +0.0136 | -0.0252 | 0.77% | 0.77% | 1693/4041 |
| d_Institutional Ownership | +0.0374 | +0.0212 | +0.0155 | 1.16% | 0.68% | 404/413 |
| Institutional Transactions | +0.0339 | +0.0650 | -0.0591 | 0.95% | 0.81% | 3181/1858 |
| d_Volatility (Month) | -0.0329 | -0.0091 | +0.0081 | -0.31% | -0.89% | 40/17 |
| Relative Volume | +0.0316 | +0.0376 | +0.0789 | 0.59% | n/a | 11366/0 |
| d_Analyst Recom | -0.0312 | +0.0083 | -0.0157 | -0.08% | 1.31% | 60/78 |
| d_Gross Margin | -0.0303 | -0.0151 | -0.0316 | -2.17% | 2.05% | 6/6 |
| d_Average Volume | -0.0285 | -0.0965 | +0.0239 | 0.58% | 0.61% | 4258/6777 |
| d_Short Ratio | +0.0267 | +0.0805 | -0.0085 | 0.72% | 0.72% | 4607/2486 |
| d_Relative Strength Index (14) | -0.0180 | +0.3067 | -0.1225 | 0.56% | 0.62% | 2367/8853 |
| d_Insider Transactions | +0.0177 | +0.0433 | -0.0035 | 1.22% | 0.76% | 121/268 |
| d_Sales Growth Quarter Over Quarter | +0.0166 | +0.0246 | -0.0152 | 0.06% | 0.24% | 4/4 |
| d_EPS Surprise | +0.0146 | +0.0083 | +0.0269 | 1.42% | 0.72% | 46/29 |
| d_Beta | -0.0144 | -0.0353 | +0.0034 | 0.57% | 0.97% | 1382/1558 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 158 | -0.89% | 30.4% |
| true_ret>3% & UPTREND | 188 | 2.20% | 41.5% |
| true_ret>3% & MIXED | 126 | -0.43% | 28.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 199 | -0.40% | -0.01% |
| WASHED | 852 | 0.54% | 0.45% |
