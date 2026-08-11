# Factor attribution — 2026-08-07

**What this report measures, exactly:** features computed from the **2026-08-07** Finviz snapshot (deltas vs the **2026-08-06** snapshot), graded against `fwd_1d` = the return from **2026-08-07** to **2026-08-10** (n=11525 stocks with valid labels).
Provisional until multiple scan dates agree.

_Column guide: **IC** = Spearman rank correlation between the feature and the forward return (whole universe); **IC↑** = IC computed only among stocks that went UP; **IC↓** = IC only among stocks that went DOWN. A high IC↑ means the feature ranks winners among winners._

## Score calibration
- Spearman IC(total_score, fwd_1d) = **-0.0339**

| Quintile | Mean fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 12.08% | 20.8% | 2323 |
| 2 | 2.58% | 7.5% | 2579 |
| 3 | 0.05% | 5.8% | 2042 |
| 4 | -0.25% | 14.9% | 2463 |
| 5 | -0.55% | 23.8% | 2118 |

## Top |IC| features (full universe)

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Relative Strength Index (14) | +0.1298 | -0.2622 | +0.2924 | 2.89% | n/a | 11429/0 |
| d_Performance (Week) | -0.1212 | +0.0687 | -0.2705 | 0.35% | 8.06% | 7544/3771 |
| Performance (Month) | +0.1057 | -0.0068 | +0.1494 | -0.05% | 7.08% | 6563/4716 |
| d_20-Day Simple Moving Average | -0.1028 | +0.0806 | -0.2452 | -0.15% | 11.90% | 8572/2881 |
| Short Float | -0.0878 | +0.2117 | -0.1969 | 5.95% | n/a | 5697/0 |
| d_Performance (Quarter) | -0.0875 | +0.0795 | -0.1886 | -0.30% | 14.87% | 8332/2435 |
| true_ret | -0.0831 | +0.0649 | -0.2079 | -0.41% | 10.33% | 8421/2677 |
| d_50-Day Simple Moving Average | -0.0829 | +0.0933 | -0.2274 | -0.13% | 11.84% | 8563/2884 |
| d_200-Day Simple Moving Average | -0.0815 | +0.0677 | -0.2058 | -0.19% | 12.11% | 8578/2860 |
| d_Performance (YTD) | -0.0806 | +0.0424 | -0.1750 | -0.40% | 9.30% | 8488/2733 |
| d_Price | -0.0688 | -0.0733 | -0.0027 | -0.41% | 10.33% | 8421/2677 |
| d_Forward P/E | -0.0614 | +0.0743 | -0.1646 | -0.63% | -0.33% | 1801/1182 |
| d_Market Cap | -0.0548 | -0.0373 | -0.0514 | 0.51% | 15.18% | 3601/2131 |
| Performance (Week) | -0.0505 | +0.0920 | -0.1980 | -0.33% | 14.04% | 8834/2556 |
| d_Relative Strength Index (14) | -0.0388 | -0.0926 | +0.1323 | -0.40% | 13.30% | 8449/2738 |
| d_Gross Margin | +0.0378 | +0.0363 | +0.0323 | 0.18% | -0.73% | 220/194 |
| d_Relative Volume | +0.0282 | +0.0283 | -0.0207 | 2.43% | 3.47% | 5190/5900 |
| Relative Volume | -0.0279 | +0.0940 | -0.1316 | 2.94% | n/a | 11237/0 |
| d_Target Price | +0.0272 | -0.0242 | +0.0452 | -0.16% | -0.47% | 435/284 |
| d_Sales Growth Quarter Over Quarter | +0.0243 | +0.0384 | +0.0183 | 0.22% | -0.86% | 202/183 |
| d_Analyst Recom | -0.0223 | +0.0032 | +0.0006 | -0.90% | -0.31% | 80/72 |
| d_Performance (Month) | +0.0216 | +0.1054 | -0.0569 | 0.47% | 5.85% | 5945/5186 |
| d_Short Ratio | +0.0175 | +0.0413 | -0.0253 | -0.24% | 3.74% | 4345/2655 |
| d_Institutional Ownership | +0.0116 | -0.0079 | +0.0125 | -0.01% | -0.44% | 66/117 |
| d_EPS Surprise | +0.0113 | +0.0173 | -0.0131 | 0.30% | -0.68% | 111/82 |

## Combinations

| Pattern | n | Mean fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 643 | -1.63% | 26.0% |
| true_ret>3% & UPTREND | 649 | -0.39% | 29.9% |
| true_ret>3% & MIXED | 466 | -1.07% | 26.2% |
| MonthΔ+ & Month<0 | 938 | -0.22% | 25.8% |
| MonthΔ+ & Month>0 | 1402 | -0.34% | 27.4% |

## Risk dominance probes

| State | n | Mean fwd | Mean fwd if score top quintile |
|---|---|---|---|
| Week>40% | 173 | -2.56% | -4.28% |
| Week>25% | 434 | -1.25% | -1.76% |
| Week>100% | 18 | -12.34% | n/a |
| RSI>75 | 217 | -0.38% | n/a |
