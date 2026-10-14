# Factor attribution — signal 2026-10-12 → prediction day 2026-10-14

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-12** | Features/scores formed from this snapshot (and deltas vs **2026-10-09**). Only data on/before this date. |
| **Prediction day** | **2026-10-14** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-12 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-14 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11712** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.2312**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -2.68% | 8.8% | 2351 |
| 2 | -1.81% | 4.1% | 2831 |
| 3 | -1.70% | 4.6% | 2588 |
| 4 | -1.29% | 9.3% | 1867 |
| 5 | -1.48% | 17.3% | 2075 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.4534 | +0.1743 | -0.5269 | -2.78% | -1.10% | 4353/279 |
| d_50-Day Simple Moving Average | +0.4267 | +0.1557 | +0.4650 | -0.82% | -2.63% | 5038/6499 |
| true_ret | +0.4184 | +0.1216 | +0.4751 | -0.82% | -2.63% | 4674/6334 |
| d_Performance (Quarter) | +0.4148 | +0.1629 | +0.4068 | -1.14% | -2.12% | 3893/7251 |
| d_Performance (YTD) | +0.4098 | +0.0994 | +0.4467 | -0.82% | -2.60% | 4758/6429 |
| d_200-Day Simple Moving Average | +0.4064 | +0.1227 | +0.4379 | -0.90% | -2.51% | 4877/6623 |
| d_Price | +0.3963 | +0.0956 | +0.3762 | -0.82% | -2.63% | 4674/6334 |
| d_20-Day Simple Moving Average | +0.3957 | +0.1605 | +0.4229 | -1.01% | -2.56% | 5335/6203 |
| Performance (Week) | +0.3930 | +0.0671 | +0.4327 | -0.91% | -2.67% | 5500/6037 |
| d_Relative Strength Index (14) | +0.3864 | +0.0296 | +0.3779 | -0.83% | -2.60% | 4777/6433 |
| d_Performance (Month) | +0.3578 | +0.0540 | +0.3685 | -1.39% | -2.06% | 3845/7591 |
| d_Performance (Week) | +0.3390 | +0.0903 | +0.3573 | -0.96% | -2.33% | 4107/7376 |
| d_Forward P/E | +0.3024 | +0.0274 | +0.3495 | -0.63% | -2.72% | 1583/1345 |
| d_Market Cap | +0.2853 | -0.0156 | +0.2716 | -1.48% | -2.10% | 2480/3241 |
| Short Float | -0.2008 | +0.0969 | -0.2549 | -1.83% | n/a | 5667/0 |
| d_Beta | +0.1838 | -0.0369 | +0.2124 | -2.34% | -1.49% | 1012/1911 |
| Performance (Month) | +0.1755 | -0.1026 | +0.2719 | -1.83% | -1.82% | 3891/7639 |
| Institutional Transactions | -0.1686 | -0.0378 | -0.1692 | -2.24% | -0.96% | 3263/1778 |
| Relative Strength Index (14) | +0.1562 | +0.1165 | +0.2824 | -1.82% | n/a | 11628/0 |
| d_Institutional Ownership | +0.1278 | -0.0376 | +0.1480 | -2.11% | -3.00% | 2401/640 |
| d_Relative Volume | -0.0499 | +0.0804 | -0.0372 | -1.29% | -2.30% | 5174/6071 |
| d_Short Float | -0.0450 | +0.0129 | -0.0317 | -2.50% | -1.15% | 2897/2619 |
| Relative Volume | -0.0373 | +0.0677 | -0.0796 | -1.87% | n/a | 11438/0 |
| d_Short Ratio | -0.0271 | -0.0435 | -0.0542 | -2.27% | -1.36% | 5674/5463 |
| d_Average Volume | +0.0266 | -0.0782 | +0.0128 | -1.72% | -1.99% | 5328/5627 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 155 | -1.90% | 29.0% |
| true_ret>3% & UPTREND | 126 | -3.60% | 23.8% |
| true_ret>3% & MIXED | 97 | -2.02% | 32.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 173 | -1.63% | -2.99% |
| WASHED | 1192 | -1.03% | -4.71% |
