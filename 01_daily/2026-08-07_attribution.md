# Factor attribution — 2026-08-07

**What this report measures, exactly:** features computed from the **2026-08-07** Finviz snapshot (deltas vs the **2026-08-06** snapshot), graded against `fwd_2d` = the return from **2026-08-07** to **2026-08-11** (n=11525 stocks with valid labels).
Provisional until multiple scan dates agree.

_Column guide: **IC** = Spearman rank correlation between the feature and the forward return (whole universe); **IC↑** = IC computed only among stocks that went UP; **IC↓** = IC only among stocks that went DOWN. A high IC↑ means the feature ranks winners among winners._

## Score calibration
- Spearman IC(total_score, fwd_2d) = **-0.0242**

| Quintile | Mean fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 13.39% | 26.8% | 2323 |
| 2 | 2.61% | 10.6% | 2579 |
| 3 | -0.01% | 7.6% | 2042 |
| 4 | -0.15% | 15.8% | 2463 |
| 5 | -0.07% | 30.6% | 2118 |

## Top |IC| features (full universe)

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Price | -0.0872 | -0.0976 | +0.0227 | -0.23% | 11.62% | 8421/2677 |
| d_Performance (Week) | -0.0814 | +0.0687 | -0.2099 | 0.90% | 8.10% | 7544/3771 |
| d_20-Day Simple Moving Average | -0.0772 | +0.0841 | -0.2050 | 0.10% | 12.65% | 8572/2881 |
| d_200-Day Simple Moving Average | -0.0758 | +0.0581 | -0.1750 | -0.02% | 13.12% | 8578/2860 |
| d_50-Day Simple Moving Average | -0.0733 | +0.0842 | -0.1975 | -0.01% | 12.97% | 8563/2884 |
| d_Performance (YTD) | -0.0713 | +0.0308 | -0.1384 | -0.22% | 10.09% | 8488/2733 |
| true_ret | -0.0711 | +0.0571 | -0.1743 | -0.23% | 11.62% | 8421/2677 |
| Relative Strength Index (14) | +0.0520 | -0.2360 | +0.2739 | 3.27% | n/a | 11429/0 |
| Performance (Month) | +0.0481 | -0.0435 | +0.0969 | 0.07% | 7.81% | 6563/4716 |
| d_Relative Strength Index (14) | -0.0437 | -0.1121 | +0.1806 | -0.22% | 14.33% | 8449/2738 |
| d_Performance (Quarter) | -0.0424 | +0.0875 | -0.1424 | -0.00% | 15.46% | 8332/2435 |
| upside_pct_lvl | +0.0413 | +0.3665 | -0.2385 | 2.47% | -0.74% | 4266/382 |
| Short Float | -0.0346 | +0.2468 | -0.1785 | 6.62% | n/a | 5697/0 |
| d_Market Cap | -0.0317 | -0.0228 | +0.0318 | 1.09% | 16.00% | 3601/2131 |
| d_Gross Margin | +0.0309 | +0.0207 | -0.0124 | 0.46% | -0.40% | 220/194 |
| d_Forward P/E | -0.0299 | +0.0514 | -0.0575 | -0.46% | -0.26% | 1801/1182 |
| Institutional Transactions | +0.0286 | +0.0700 | -0.0470 | 12.09% | 2.91% | 2536/2487 |
| d_Sales Growth Quarter Over Quarter | +0.0273 | +0.0398 | +0.0196 | 0.70% | -0.84% | 202/183 |
| Performance (Week) | -0.0192 | +0.1263 | -0.1575 | -0.09% | 14.92% | 8834/2556 |
| Relative Volume | -0.0186 | +0.0773 | -0.1387 | 3.32% | n/a | 11237/0 |
| d_Sales Year Over Year TTM | -0.0107 | -0.0051 | -0.0015 | -0.24% | 0.34% | 205/157 |
| d_Performance (Month) | +0.0107 | +0.0699 | -0.0335 | 1.11% | 5.93% | 5945/5186 |
| d_Institutional Ownership | -0.0107 | -0.0401 | +0.0130 | -0.25% | -0.04% | 66/117 |
| d_Analyst Recom | -0.0096 | -0.0456 | -0.0047 | -0.34% | -0.22% | 80/72 |
| d_Average Volume | -0.0091 | -0.0506 | +0.0451 | 8.59% | 0.01% | 4352/6657 |

## Combinations

| Pattern | n | Mean fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 643 | -0.67% | 33.4% |
| true_ret>3% & UPTREND | 649 | 0.04% | 34.1% |
| true_ret>3% & MIXED | 466 | -0.58% | 33.0% |
| MonthΔ+ & Month<0 | 938 | 1.03% | 33.0% |
| MonthΔ+ & Month>0 | 1402 | -0.07% | 31.3% |

## Risk dominance probes

| State | n | Mean fwd | Mean fwd if score top quintile |
|---|---|---|---|
| Week>40% | 173 | -2.17% | -1.76% |
| Week>25% | 434 | -0.29% | -0.17% |
| Week>100% | 18 | -15.72% | n/a |
| RSI>75 | 217 | -0.48% | n/a |
