# Factor attribution — signal 2026-09-09 → prediction day 2026-09-10

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-09** | Features/scores formed from this snapshot (and deltas vs **2026-09-08**). Only data on/before this date. |
| **Prediction day** | **2026-09-10** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-09 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-10 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11599** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0163**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.61% | 9.9% | 2774 |
| 2 | -0.91% | 4.7% | 2122 |
| 3 | -0.35% | 5.1% | 2194 |
| 4 | -0.90% | 4.8% | 2321 |
| 5 | -0.04% | 10.9% | 2188 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2003 | +0.2601 | -0.3452 | -0.89% | -0.68% | 4369/278 |
| d_Performance (Week) | -0.1736 | -0.1345 | -0.1515 | -0.72% | -0.36% | 6563/4840 |
| Performance (Week) | -0.1580 | -0.1115 | -0.1735 | -1.22% | 0.12% | 5835/5547 |
| Short Float | -0.1445 | +0.0709 | -0.2120 | -0.55% | n/a | 5682/0 |
| true_ret | +0.1302 | -0.0758 | +0.2247 | 0.13% | -0.86% | 2253/8892 |
| d_20-Day Simple Moving Average | +0.1293 | -0.0549 | +0.2100 | 0.03% | -0.73% | 2537/8959 |
| d_200-Day Simple Moving Average | +0.1212 | -0.0155 | +0.1830 | 0.14% | -0.74% | 2395/9080 |
| d_Performance (YTD) | +0.1210 | -0.0254 | +0.1804 | 0.12% | -0.74% | 2302/8952 |
| d_50-Day Simple Moving Average | +0.1137 | -0.0316 | +0.1822 | 0.40% | -0.83% | 2485/9001 |
| d_Price | +0.0942 | +0.0721 | +0.0261 | 0.13% | -0.86% | 2253/8892 |
| d_Beta | +0.0825 | -0.0565 | +0.1050 | -0.83% | -1.22% | 1280/1457 |
| Institutional Transactions | -0.0485 | +0.0848 | -0.1046 | -0.52% | -0.53% | 3199/1831 |
| d_Short Ratio | -0.0458 | +0.0019 | -0.0422 | -0.76% | -0.75% | 3816/4192 |
| d_Relative Volume | +0.0439 | -0.0156 | +0.0577 | -0.92% | -0.28% | 4999/6200 |
| d_Forward P/E | +0.0428 | -0.0468 | +0.0238 | -0.95% | -0.38% | 689/2266 |
| d_Performance (Quarter) | -0.0400 | -0.0088 | -0.0027 | -0.63% | -0.44% | 3419/7477 |
| d_Average Volume | +0.0373 | +0.0687 | +0.0051 | -0.36% | -0.81% | 5983/5285 |
| d_Total Debt/Equity | -0.0324 | -0.0540 | -0.0247 | -2.33% | 0.61% | 15/16 |
| d_EPS Surprise | +0.0318 | +0.0984 | -0.0004 | 0.07% | -5.72% | 27/19 |
| d_Market Cap | +0.0294 | +0.1218 | -0.0767 | 0.35% | -0.86% | 1504/4221 |
| d_Volatility (Month) | +0.0276 | +0.0098 | +0.0666 | -0.48% | -0.59% | 4309/4863 |
| Performance (Month) | +0.0246 | -0.0661 | +0.0604 | -0.67% | -0.50% | 4018/7372 |
| d_Sales Year Over Year TTM | -0.0162 | +0.0011 | -0.0182 | -1.11% | 0.13% | 17/17 |
| d_Performance (Month) | +0.0154 | -0.0569 | +0.0527 | -0.11% | -0.80% | 3968/7321 |
| Relative Volume | -0.0147 | +0.0266 | -0.0500 | -0.57% | n/a | 11337/0 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 150 | 5.46% | 30.7% |
| true_ret>3% & UPTREND | 154 | -3.11% | 14.9% |
| true_ret>3% & MIXED | 83 | -1.87% | 20.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 222 | -2.76% | -4.97% |
| WASHED | 954 | 0.82% | 7.78% |
