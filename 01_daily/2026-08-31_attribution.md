# Factor attribution — signal 2026-08-31 → prediction day 2026-09-02

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-31** | Features/scores formed from this snapshot (and deltas vs **2026-08-28**). Only data on/before this date. |
| **Prediction day** | **2026-09-02** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-31 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-02 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11615** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0398**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -1.01% | 15.6% | 2467 |
| 2 | 9.16% | 10.9% | 2252 |
| 3 | -0.30% | 8.0% | 2286 |
| 4 | -0.36% | 10.7% | 2348 |
| 5 | 0.00% | 26.3% | 2262 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.1253 | -0.0034 | -0.1552 | 1.38% | 1.57% | 5451/5899 |
| d_Beta | +0.1143 | -0.0649 | +0.1855 | 20.39% | -0.63% | 1070/2129 |
| upside_pct_lvl | -0.0980 | +0.2661 | -0.2965 | 0.10% | 0.18% | 4329/321 |
| d_50-Day Simple Moving Average | -0.0789 | -0.0501 | -0.0638 | 2.14% | 1.08% | 4051/7395 |
| Relative Strength Index (14) | +0.0761 | -0.0749 | +0.1066 | 1.46% | n/a | 11491/0 |
| d_200-Day Simple Moving Average | -0.0737 | -0.0314 | -0.0697 | 2.31% | 1.03% | 3889/7536 |
| d_Performance (Quarter) | +0.0733 | +0.0505 | +0.0690 | 0.04% | 2.89% | 4855/5981 |
| d_Forward P/E | +0.0712 | +0.1208 | -0.0170 | -0.30% | -0.27% | 981/1967 |
| d_Volatility (Month) | +0.0701 | -0.0963 | +0.1888 | 4.07% | 0.98% | 2519/7141 |
| d_Relative Strength Index (14) | -0.0694 | +0.1394 | -0.2125 | -0.35% | 2.50% | 3829/7276 |
| d_Relative Volume | +0.0624 | -0.0001 | +0.0790 | -0.26% | 3.90% | 6437/4740 |
| d_Price | -0.0546 | +0.0808 | -0.1333 | -0.51% | -0.40% | 3757/7174 |
| d_Performance (YTD) | -0.0538 | -0.0337 | -0.0423 | -0.35% | 2.49% | 3847/7295 |
| d_Profit Margin | +0.0468 | -0.0190 | +0.0687 | 2.06% | -7.39% | 9/15 |
| true_ret | -0.0465 | -0.0527 | -0.0222 | -0.51% | -0.40% | 3757/7174 |
| d_Institutional Transactions | +0.0456 | +0.0115 | -0.0007 | 5.15% | -0.40% | 2012/2002 |
| d_Total Debt/Equity | +0.0430 | +0.0458 | +0.0329 | 1.62% | -8.04% | 15/7 |
| Performance (Month) | -0.0414 | +0.0658 | -0.0803 | -0.33% | 4.70% | 7256/4104 |
| d_20-Day Simple Moving Average | -0.0383 | -0.0627 | -0.0058 | 2.50% | 0.96% | 3664/7784 |
| Relative Volume | +0.0329 | +0.0721 | -0.0013 | 1.46% | n/a | 11388/0 |
| d_Market Cap | -0.0303 | +0.1224 | -0.0983 | 5.45% | 2.53% | 2098/3613 |
| d_Target Price | +0.0269 | +0.0433 | -0.0061 | 0.05% | -0.77% | 141/107 |
| d_Gross Margin | +0.0263 | +0.0090 | +0.0249 | -1.87% | -4.92% | 15/17 |
| d_Performance (Month) | +0.0166 | +0.0751 | -0.0255 | -0.24% | 2.84% | 4901/6368 |
| d_Insider Transactions | +0.0160 | +0.0316 | -0.0190 | 8.97% | 55.16% | 103/190 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 222 | -1.20% | 23.4% |
| true_ret>3% & UPTREND | 204 | -1.44% | 29.9% |
| true_ret>3% & MIXED | 182 | -2.86% | 20.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 292 | -2.33% | -2.51% |
| WASHED | 498 | 41.67% | 0.45% |
