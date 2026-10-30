# Factor attribution — signal 2026-10-27 → prediction day 2026-10-30

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-27** | Features/scores formed from this snapshot (and deltas vs **2026-10-26**). Only data on/before this date. |
| **Prediction day** | **2026-10-30** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-27 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-30 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11760** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.1468**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 7.14% | 25.8% | 2353 |
| 2 | -0.63% | 11.5% | 2371 |
| 3 | -1.24% | 13.3% | 2858 |
| 4 | -2.15% | 21.0% | 2254 |
| 5 | -1.67% | 24.2% | 1924 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_20-Day Simple Moving Average | -0.3501 | +0.0208 | -0.4336 | -1.60% | 3.12% | 7768/3844 |
| Performance (Month) | +0.3441 | -0.0439 | +0.4671 | 0.03% | 0.62% | 5564/6008 |
| d_Performance (Month) | -0.3265 | +0.0458 | -0.4271 | -1.58% | 5.62% | 8956/2483 |
| d_200-Day Simple Moving Average | -0.3229 | +0.0231 | -0.3763 | -1.69% | 3.40% | 8031/3527 |
| d_Performance (Quarter) | -0.3181 | +0.0716 | -0.3828 | -1.33% | 4.30% | 8414/2724 |
| d_Performance (YTD) | -0.3178 | +0.0015 | -0.3284 | -1.68% | 3.31% | 7874/3429 |
| true_ret | -0.3122 | +0.0107 | -0.3762 | -1.74% | 3.51% | 7810/3370 |
| d_50-Day Simple Moving Average | -0.3093 | +0.0490 | -0.3865 | -1.48% | 3.52% | 8252/3332 |
| d_Price | -0.3065 | -0.0330 | -0.2013 | -1.74% | 3.51% | 7810/3370 |
| d_Performance (Week) | -0.3009 | -0.1408 | -0.2942 | -1.81% | 1.77% | 5774/5709 |
| d_Relative Strength Index (14) | -0.2981 | -0.0266 | -0.0886 | -1.68% | 3.75% | 7853/3464 |
| Relative Strength Index (14) | +0.2909 | -0.2567 | +0.4191 | 0.32% | n/a | 11673/0 |
| d_Beta | +0.2744 | -0.0549 | +0.3286 | 2.25% | 1.86% | 2232/2525 |
| upside_pct_lvl | -0.1927 | +0.2661 | -0.3813 | 0.80% | -0.66% | 4308/326 |
| d_Forward P/E | -0.1792 | +0.0553 | -0.2460 | -0.63% | 0.43% | 1647/1295 |
| d_Market Cap | -0.0925 | +0.0298 | -0.1071 | 0.04% | 4.60% | 3601/2191 |
| Performance (Week) | +0.0899 | -0.0442 | +0.1208 | -0.98% | 1.34% | 6746/4778 |
| Institutional Transactions | -0.0626 | +0.0332 | -0.0437 | -0.78% | 8.73% | 3236/1813 |
| Relative Volume | +0.0487 | +0.1245 | -0.0461 | -0.03% | n/a | 11406/0 |
| d_Average Volume | +0.0375 | +0.0266 | -0.0320 | 0.24% | -0.21% | 6041/4952 |
| d_Analyst Recom | +0.0234 | -0.0102 | +0.0180 | 0.37% | -1.56% | 79/61 |
| d_Short Float | +0.0219 | +0.0430 | +0.0125 | 4.52% | 0.65% | 2782/2708 |
| d_Profit Margin | +0.0196 | n/a | -0.0102 | n/a | -4.93% | 0/4 |
| d_Gross Margin | -0.0193 | n/a | -0.0355 | -9.16% | -1.95% | 3/2 |
| d_Relative Volume | +0.0192 | +0.0507 | -0.0040 | 0.25% | -0.32% | 5509/5733 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1308 | -3.70% | 19.6% |
| true_ret>3% & UPTREND | 242 | -2.26% | 26.4% |
| true_ret>3% & MIXED | 287 | -4.30% | 20.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 157 | -0.92% | -3.34% |
| WASHED | 1294 | 9.16% | -6.17% |
