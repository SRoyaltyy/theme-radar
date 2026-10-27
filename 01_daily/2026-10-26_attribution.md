# Factor attribution — signal 2026-10-26 → prediction day 2026-10-27

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-26** | Features/scores formed from this snapshot (and deltas vs **2026-10-23**). Only data on/before this date. |
| **Prediction day** | **2026-10-27** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-26 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-27 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11757** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0571**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.53% | 34.0% | 2424 |
| 2 | 1.70% | 27.1% | 2291 |
| 3 | 0.95% | 14.8% | 2426 |
| 4 | 1.14% | 14.2% | 2297 |
| 5 | 2.13% | 39.4% | 2319 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | -0.4490 | -0.6122 | +0.0261 | -0.12% | 2.54% | 4514/7049 |
| Relative Strength Index (14) | -0.4210 | -0.5225 | +0.2056 | 1.49% | n/a | 11665/0 |
| upside_pct_lvl | +0.3244 | +0.4906 | -0.1996 | 2.37% | -0.30% | 4291/340 |
| d_Performance (Quarter) | +0.3199 | +0.3097 | +0.1000 | 2.53% | 0.37% | 5885/5294 |
| d_Beta | +0.3034 | +0.3908 | -0.0562 | 4.73% | -0.11% | 2310/1837 |
| Performance (Week) | -0.2647 | -0.3100 | +0.0286 | 0.42% | 2.75% | 6142/5375 |
| d_20-Day Simple Moving Average | +0.2571 | +0.2367 | +0.1369 | 1.70% | 1.17% | 7295/4292 |
| d_50-Day Simple Moving Average | +0.1842 | +0.1505 | +0.1292 | 1.47% | 1.57% | 7634/3951 |
| d_Forward P/E | +0.1718 | +0.1293 | +0.1121 | 0.95% | 0.28% | 1607/1316 |
| Short Float | +0.1715 | +0.3139 | -0.0645 | 2.04% | n/a | 5651/0 |
| d_200-Day Simple Moving Average | +0.1470 | +0.0881 | +0.1276 | 1.45% | 1.63% | 7226/4316 |
| true_ret | +0.1387 | +0.0798 | +0.1509 | 1.28% | 1.68% | 6976/4197 |
| d_Performance (YTD) | +0.1368 | +0.0620 | +0.1372 | 1.46% | 1.65% | 7055/4264 |
| d_Price | +0.1338 | -0.0132 | +0.1626 | 1.28% | 1.68% | 6976/4197 |
| d_Relative Strength Index (14) | +0.1220 | -0.1291 | +0.1869 | 1.46% | 1.63% | 7032/4267 |
| Institutional Transactions | +0.1108 | +0.1690 | +0.0333 | 3.07% | 0.68% | 3236/1814 |
| d_Volatility (Month) | +0.0722 | +0.1910 | -0.1405 | 1.64% | 1.70% | 5282/4881 |
| d_Market Cap | +0.0645 | -0.0431 | +0.1030 | 2.15% | 1.87% | 2842/2941 |
| d_Target Price | -0.0389 | -0.0080 | -0.0567 | 0.71% | 1.43% | 327/319 |
| d_Performance (Week) | -0.0329 | -0.0420 | +0.0535 | 1.09% | 2.26% | 7261/4228 |
| d_Analyst Recom | -0.0286 | -0.0187 | -0.0103 | 0.67% | 1.36% | 89/118 |
| d_Insider Transactions | +0.0270 | +0.0298 | -0.0178 | 1.17% | 0.66% | 232/270 |
| d_Short Float | -0.0261 | -0.0321 | -0.0144 | 0.87% | 2.27% | 74/58 |
| d_Performance (Month) | +0.0222 | +0.0313 | +0.0148 | 1.71% | 1.31% | 5888/5566 |
| d_EPS Surprise | +0.0178 | -0.0066 | +0.0350 | 2.66% | -0.16% | 29/37 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 503 | 6.94% | 68.2% |
| true_ret>3% & UPTREND | 153 | 1.67% | 45.8% |
| true_ret>3% & MIXED | 157 | 2.49% | 67.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 186 | -0.61% | 1.48% |
| WASHED | 1690 | 6.74% | 8.79% |
