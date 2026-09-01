# Factor attribution — signal 2026-08-26 → prediction day 2026-08-31

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-26** | Features/scores formed from this snapshot (and deltas vs **2026-08-25**). Only data on/before this date. |
| **Prediction day** | **2026-08-31** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-26 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-31 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11586** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0146**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.84% | 18.2% | 2438 |
| 2 | 0.91% | 12.6% | 2603 |
| 3 | -0.50% | 5.9% | 1948 |
| 4 | 0.85% | 8.3% | 2304 |
| 5 | 1.00% | 20.1% | 2293 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | -0.1858 | +0.2688 | -0.2407 | 2.18% | n/a | 5692/0 |
| upside_pct_lvl | -0.1481 | +0.1954 | -0.3508 | 1.85% | -0.44% | 4304/338 |
| Relative Strength Index (14) | +0.1266 | -0.2402 | +0.1884 | 1.10% | n/a | 11462/0 |
| Performance (Month) | +0.0841 | +0.1948 | -0.0286 | 0.46% | 2.44% | 7564/3754 |
| d_Performance (Quarter) | +0.0733 | +0.0426 | +0.0480 | 0.90% | 1.56% | 5130/5646 |
| d_Average Volume | +0.0653 | -0.1987 | +0.1736 | -0.11% | 1.37% | 2538/8702 |
| Relative Volume | -0.0546 | +0.1042 | -0.0731 | 1.11% | n/a | 11327/0 |
| Institutional Transactions | -0.0540 | +0.0420 | -0.1042 | 3.93% | 1.65% | 3173/1878 |
| d_Forward P/E | -0.0356 | -0.0358 | -0.0019 | -1.17% | -0.82% | 1390/1551 |
| d_Institutional Ownership | -0.0275 | -0.0225 | -0.0056 | -1.41% | -1.30% | 1242/913 |
| d_Analyst Recom | +0.0263 | +0.0182 | +0.0330 | -0.80% | -1.44% | 74/72 |
| d_Performance (YTD) | +0.0252 | -0.0976 | +0.0544 | 0.93% | 1.27% | 4775/6319 |
| d_Price | +0.0252 | -0.0757 | +0.0066 | 0.05% | 0.42% | 4641/6213 |
| d_200-Day Simple Moving Average | +0.0242 | -0.0735 | +0.0410 | 1.72% | 0.71% | 4512/6854 |
| true_ret | +0.0234 | -0.1059 | +0.0658 | 0.05% | 0.42% | 4641/6213 |
| d_EPS Surprise | +0.0229 | +0.0138 | +0.0091 | 1.39% | -1.53% | 38/27 |
| d_Gross Margin | +0.0198 | +0.0170 | +0.0106 | -1.38% | -3.09% | 20/15 |
| d_Sales Year Over Year TTM | -0.0189 | +0.0085 | -0.0002 | -2.29% | -1.89% | 23/16 |
| d_Beta | -0.0173 | +0.0458 | -0.0708 | 1.35% | 10.00% | 1789/1131 |
| Performance (Week) | +0.0154 | -0.1119 | +0.0808 | 1.11% | 1.13% | 5471/5880 |
| d_Performance (Week) | +0.0154 | -0.1246 | +0.0633 | 2.48% | 0.35% | 4076/7281 |
| d_Market Cap | -0.0145 | -0.0496 | +0.0217 | 3.06% | 2.25% | 2502/3186 |
| d_Performance (Month) | +0.0140 | +0.0099 | -0.0494 | 1.72% | 0.72% | 4541/6721 |
| d_Relative Volume | +0.0138 | -0.0176 | -0.0038 | 2.03% | 0.24% | 5013/6081 |
| d_Total Debt/Equity | +0.0125 | +0.0060 | -0.0156 | -2.88% | -2.52% | 12/16 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 231 | 2.87% | 25.1% |
| true_ret>3% & UPTREND | 163 | 12.93% | 20.9% |
| true_ret>3% & MIXED | 136 | -2.28% | 20.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 400 | 5.07% | 26.27% |
| WASHED | 423 | 15.83% | 13.70% |
