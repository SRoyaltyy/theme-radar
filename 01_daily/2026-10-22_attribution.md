# Factor attribution — signal 2026-10-22 → prediction day 2026-10-26

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-22** | Features/scores formed from this snapshot (and deltas vs **2026-10-21**). Only data on/before this date. |
| **Prediction day** | **2026-10-26** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-22 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-26 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11737** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1951**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 11.11% | 31.4% | 2495 |
| 2 | 0.54% | 16.7% | 2326 |
| 3 | -0.49% | 10.7% | 2513 |
| 4 | -0.82% | 10.9% | 2079 |
| 5 | 0.33% | 13.0% | 2324 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | -0.2724 | -0.2649 | -0.0617 | -0.33% | 5.91% | 6561/4908 |
| d_Price | -0.2250 | -0.1652 | +0.0530 | 0.11% | 3.84% | 4818/6444 |
| d_Relative Strength Index (14) | -0.2183 | +0.0171 | +0.0973 | 0.08% | 4.10% | 4869/6491 |
| d_Forward P/E | -0.2175 | -0.2867 | +0.0444 | -0.33% | 0.26% | 1793/1174 |
| d_200-Day Simple Moving Average | -0.2071 | -0.2648 | +0.0486 | 0.16% | 3.98% | 5001/6581 |
| d_Performance (YTD) | -0.2066 | -0.2603 | +0.0640 | 0.09% | 3.05% | 4867/6505 |
| d_20-Day Simple Moving Average | -0.2051 | -0.2591 | +0.0083 | 0.15% | 4.07% | 5177/6427 |
| d_50-Day Simple Moving Average | -0.2005 | -0.2721 | +0.0380 | 0.12% | 4.08% | 5160/6442 |
| true_ret | -0.1751 | -0.2930 | +0.0801 | 0.11% | 3.84% | 4818/6444 |
| d_Performance (Quarter) | -0.1668 | -0.1216 | -0.0783 | 1.62% | 2.99% | 4902/6275 |
| upside_pct_lvl | -0.1476 | +0.2919 | -0.3994 | 1.01% | -0.32% | 4293/340 |
| d_Market Cap | -0.1247 | -0.2061 | +0.1323 | 0.69% | 7.53% | 2831/2891 |
| Short Float | -0.0935 | +0.2060 | -0.1999 | 4.22% | n/a | 5646/0 |
| Relative Strength Index (14) | -0.0561 | -0.2398 | +0.2580 | 2.30% | n/a | 11655/0 |
| Performance (Week) | -0.0530 | -0.2352 | +0.1923 | 0.21% | 3.93% | 4965/6583 |
| d_Performance (Week) | -0.0508 | -0.2461 | +0.1683 | 0.47% | 3.18% | 3568/7951 |
| d_Total Debt/Equity | -0.0484 | +0.0003 | -0.0259 | -0.64% | 1.01% | 36/60 |
| Relative Volume | +0.0477 | +0.1245 | +0.0307 | 2.36% | n/a | 11445/0 |
| d_Relative Volume | +0.0443 | +0.0531 | +0.0204 | 3.09% | 1.40% | 6651/4669 |
| d_Gross Margin | +0.0427 | +0.0128 | +0.0204 | 1.63% | -0.84% | 42/37 |
| d_Profit Margin | +0.0412 | -0.0374 | +0.0320 | 0.72% | -0.62% | 66/46 |
| d_Institutional Ownership | +0.0375 | -0.0113 | +0.0356 | -0.38% | 3.10% | 1077/1057 |
| d_Target Price | +0.0312 | -0.0348 | -0.0270 | 0.06% | 3.33% | 212/236 |
| d_Analyst Recom | -0.0228 | -0.0423 | +0.0039 | -1.52% | 0.43% | 70/84 |
| d_Sales Growth Quarter Over Quarter | -0.0206 | +0.0252 | -0.0077 | -0.20% | 0.75% | 58/57 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 472 | -1.71% | 19.7% |
| true_ret>3% & UPTREND | 448 | -1.43% | 13.4% |
| true_ret>3% & MIXED | 286 | 10.06% | 18.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 237 | 0.23% | -2.83% |
| WASHED | 1744 | 14.67% | -2.36% |
