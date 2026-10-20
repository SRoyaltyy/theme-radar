# Factor attribution — signal 2026-10-15 → prediction day 2026-10-20

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-15** | Features/scores formed from this snapshot (and deltas vs **2026-10-14**). Only data on/before this date. |
| **Prediction day** | **2026-10-20** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-15 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-20 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11715** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.1677**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.16% | 12.4% | 2678 |
| 2 | 1.31% | 8.1% | 2255 |
| 3 | -0.25% | 11.2% | 2266 |
| 4 | -0.89% | 20.9% | 2178 |
| 5 | -0.42% | 30.1% | 2338 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.3754 | +0.0022 | +0.4570 | 0.05% | -0.05% | 5541/5995 |
| Relative Strength Index (14) | +0.3234 | -0.1012 | +0.4310 | -0.01% | n/a | 11646/0 |
| upside_pct_lvl | -0.2608 | +0.3027 | -0.4567 | 1.64% | -0.23% | 4334/299 |
| d_Beta | -0.2410 | +0.0604 | -0.3508 | 0.70% | 0.50% | 3038/1525 |
| d_Performance (Week) | -0.2138 | +0.0345 | -0.3174 | -0.57% | 1.71% | 8725/2797 |
| d_Price | +0.1854 | -0.0071 | +0.1521 | -0.57% | 1.76% | 8230/3026 |
| d_Market Cap | +0.1656 | -0.0181 | +0.1451 | -0.50% | 3.97% | 3911/1813 |
| d_Volatility (Month) | -0.1622 | +0.0511 | -0.2240 | -0.05% | 0.15% | 6517/3354 |
| Performance (Month) | +0.1619 | -0.1413 | +0.3587 | -0.42% | 0.26% | 4603/6920 |
| d_Relative Strength Index (14) | +0.1547 | -0.1546 | +0.2565 | -0.61% | 1.71% | 8309/3071 |
| d_Performance (Month) | +0.1286 | +0.2375 | -0.0538 | -0.03% | 0.06% | 8579/2868 |
| d_Performance (YTD) | +0.1238 | +0.1232 | -0.0036 | -0.58% | 1.74% | 8300/3065 |
| d_200-Day Simple Moving Average | +0.0970 | +0.1446 | -0.0466 | -0.65% | 1.72% | 8374/3211 |
| true_ret | +0.0782 | +0.1557 | -0.0576 | -0.57% | 1.76% | 8230/3026 |
| d_50-Day Simple Moving Average | +0.0682 | +0.1744 | -0.0984 | -0.68% | 1.88% | 8565/3045 |
| d_Forward P/E | +0.0623 | +0.0652 | +0.0583 | -0.04% | -0.60% | 2216/751 |
| Institutional Transactions | -0.0423 | +0.0913 | -0.1290 | 0.53% | 2.56% | 3260/1776 |
| d_20-Day Simple Moving Average | +0.0409 | +0.1836 | -0.1435 | -0.74% | 2.16% | 8689/2930 |
| d_Average Volume | -0.0365 | +0.0380 | -0.1042 | -0.14% | 0.25% | 6692/4337 |
| Short Float | -0.0357 | +0.2312 | -0.2225 | 0.92% | n/a | 5662/0 |
| d_Relative Volume | +0.0338 | +0.0191 | +0.0005 | 0.29% | -0.22% | 5822/5500 |
| d_Short Ratio | +0.0310 | -0.0307 | +0.0711 | -0.63% | -0.01% | 2643/4396 |
| d_Performance (Quarter) | -0.0246 | +0.0972 | -0.1348 | -0.81% | 2.98% | 8751/2456 |
| d_Sales Year Over Year TTM | -0.0241 | -0.0211 | +0.0327 | -0.92% | 1.26% | 12/8 |
| d_Sales Growth Quarter Over Quarter | -0.0210 | -0.0101 | +0.0245 | -0.77% | 0.93% | 11/10 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1093 | -2.65% | 21.5% |
| true_ret>3% & UPTREND | 393 | -0.03% | 39.4% |
| true_ret>3% & MIXED | 299 | -0.17% | 38.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 154 | -1.81% | -3.53% |
| WASHED | 1200 | 1.44% | -3.93% |
