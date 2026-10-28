# Factor attribution — signal 2026-10-27 → prediction day 2026-10-28

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-27** | Features/scores formed from this snapshot (and deltas vs **2026-10-26**). Only data on/before this date. |
| **Prediction day** | **2026-10-28** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-27 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-28 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11761** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.1504**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.00% | 17.6% | 2353 |
| 2 | 0.10% | 6.7% | 2371 |
| 3 | 0.57% | 13.3% | 2859 |
| 4 | 0.89% | 22.7% | 2254 |
| 5 | 1.61% | 40.5% | 1924 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_20-Day Simple Moving Average | +0.3180 | +0.4263 | -0.0129 | 0.97% | -0.15% | 7769/3844 |
| d_50-Day Simple Moving Average | +0.2942 | +0.3935 | -0.0061 | 0.91% | -0.17% | 8253/3332 |
| d_200-Day Simple Moving Average | +0.2922 | +0.3605 | +0.0107 | 0.91% | -0.10% | 8032/3527 |
| true_ret | +0.2899 | +0.3667 | +0.0263 | 0.91% | -0.11% | 7811/3370 |
| d_Performance (YTD) | +0.2844 | +0.3068 | +0.0342 | 0.91% | -0.10% | 7875/3429 |
| d_Performance (Quarter) | +0.2706 | +0.3572 | -0.0571 | 0.80% | -0.09% | 8414/2725 |
| d_Price | +0.2629 | +0.1451 | +0.0740 | 0.91% | -0.11% | 7811/3370 |
| Performance (Month) | -0.2604 | -0.4458 | +0.1428 | 0.01% | 1.12% | 5564/6009 |
| d_Relative Strength Index (14) | +0.2543 | +0.0784 | +0.0945 | 0.90% | -0.10% | 7854/3464 |
| d_Performance (Month) | +0.2384 | +0.3620 | -0.0535 | 0.76% | -0.04% | 8957/2483 |
| Relative Strength Index (14) | -0.2187 | -0.3987 | +0.3038 | 0.58% | n/a | 11674/0 |
| upside_pct_lvl | +0.2183 | +0.4467 | -0.2826 | 0.89% | 0.28% | 4309/326 |
| d_Beta | -0.2118 | -0.2994 | +0.0978 | -0.00% | 1.50% | 2233/2525 |
| d_Performance (Week) | +0.2081 | +0.1978 | +0.0784 | 1.05% | 0.14% | 5774/5710 |
| d_Forward P/E | +0.2056 | +0.2068 | +0.0778 | 0.72% | -0.13% | 1647/1295 |
| d_Market Cap | +0.1514 | +0.0886 | +0.0214 | 1.11% | 0.11% | 3602/2191 |
| Short Float | +0.0820 | +0.2353 | -0.1264 | 0.76% | n/a | 5659/0 |
| Institutional Transactions | +0.0614 | +0.1054 | -0.0617 | 0.92% | 0.63% | 3236/1814 |
| Performance (Week) | -0.0594 | -0.0690 | +0.0763 | 0.56% | 0.64% | 6746/4779 |
| d_Total Debt/Equity | -0.0388 | -0.0194 | -0.0345 | -2.96% | 4.35% | 3/1 |
| d_Relative Volume | +0.0386 | +0.0556 | -0.0218 | 0.72% | 0.50% | 5509/5734 |
| d_Gross Margin | +0.0234 | +0.0176 | +0.0042 | 0.89% | -2.61% | 3/2 |
| d_Average Volume | -0.0221 | +0.0297 | -0.0378 | 0.64% | 0.58% | 6041/4953 |
| d_Short Ratio | +0.0209 | +0.0435 | -0.0218 | 0.67% | 0.53% | 5492/5639 |
| d_Profit Margin | +0.0156 | -0.0201 | +0.0162 | n/a | -0.86% | 0/4 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1308 | 3.00% | 55.8% |
| true_ret>3% & UPTREND | 242 | 2.77% | 47.1% |
| true_ret>3% & MIXED | 287 | 1.43% | 47.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 157 | 0.39% | 1.32% |
| WASHED | 1294 | 2.08% | 3.94% |
