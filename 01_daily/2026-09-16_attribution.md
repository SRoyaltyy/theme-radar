# Factor attribution — signal 2026-09-16 → prediction day 2026-09-21

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-16** | Features/scores formed from this snapshot (and deltas vs **2026-09-15**). Only data on/before this date. |
| **Prediction day** | **2026-09-21** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-16 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-21 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11612** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0266**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.41% | 43.4% | 2930 |
| 2 | 1.66% | 34.0% | 2853 |
| 3 | 2.12% | 29.5% | 1215 |
| 4 | 2.82% | 36.8% | 2396 |
| 5 | 6.30% | 43.1% | 2218 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.2701 | -0.4243 | +0.0065 | 0.69% | 3.70% | 2441/8999 |
| d_Performance (Quarter) | +0.2203 | +0.2633 | +0.0096 | 5.37% | 0.91% | 4849/6040 |
| upside_pct_lvl | +0.1839 | +0.4138 | -0.2847 | 1.90% | 0.39% | 4372/262 |
| Performance (Month) | -0.1387 | -0.2481 | +0.0348 | 3.62% | 2.87% | 2676/8746 |
| d_Performance (Week) | +0.1225 | +0.1496 | +0.0058 | 3.26% | 2.74% | 7115/4248 |
| d_Relative Strength Index (14) | +0.1218 | +0.1509 | -0.0541 | 5.57% | 1.84% | 3699/7450 |
| d_Price | +0.1059 | +0.0967 | -0.0414 | 4.31% | 1.85% | 3604/7354 |
| d_Performance (YTD) | +0.1044 | +0.0386 | +0.0330 | 5.65% | 1.84% | 3680/7449 |
| d_Forward P/E | +0.1031 | +0.0929 | +0.0444 | 1.18% | 0.20% | 1047/1883 |
| d_200-Day Simple Moving Average | +0.0982 | +0.0385 | +0.0289 | 5.37% | 1.85% | 3902/7576 |
| d_20-Day Simple Moving Average | +0.0957 | +0.0271 | +0.0662 | 4.82% | 1.84% | 4626/6869 |
| true_ret | +0.0937 | +0.0136 | +0.0884 | 4.31% | 1.85% | 3604/7354 |
| d_50-Day Simple Moving Average | +0.0892 | +0.0247 | +0.0450 | 5.03% | 1.90% | 4178/7314 |
| d_Beta | +0.0857 | +0.1183 | +0.0012 | 7.34% | 1.39% | 2343/1204 |
| d_Market Cap | +0.0812 | +0.1078 | -0.0337 | 6.06% | 1.32% | 2112/3544 |
| Relative Volume | -0.0752 | -0.0144 | +0.0008 | 3.07% | n/a | 11379/0 |
| d_Average Volume | -0.0706 | -0.1497 | +0.0432 | 3.41% | 2.43% | 4949/6084 |
| d_Performance (Month) | -0.0607 | -0.0758 | -0.0429 | 3.58% | 2.57% | 5487/5788 |
| d_Short Ratio | +0.0598 | +0.1143 | -0.0666 | 2.44% | 2.10% | 4080/3271 |
| d_Volatility (Month) | -0.0447 | -0.0222 | -0.0108 | 3.55% | 3.42% | 5061/4077 |
| Institutional Transactions | +0.0362 | +0.1071 | -0.0257 | 3.53% | 3.18% | 3209/1826 |
| Short Float | +0.0349 | +0.2349 | -0.1944 | 2.66% | n/a | 5695/0 |
| d_EPS Surprise | -0.0331 | -0.0277 | -0.0288 | -1.97% | 8.16% | 5/3 |
| d_Profit Margin | +0.0315 | +0.0478 | +0.0144 | 7.76% | -2.78% | 6/4 |
| d_Analyst Recom | -0.0253 | +0.0220 | -0.0205 | 0.02% | 1.55% | 63/77 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 299 | 22.23% | 61.5% |
| true_ret>3% & UPTREND | 160 | 6.19% | 53.1% |
| true_ret>3% & MIXED | 126 | 3.96% | 47.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 119 | 6.72% | 13.05% |
| WASHED | 1998 | 6.25% | 15.66% |
