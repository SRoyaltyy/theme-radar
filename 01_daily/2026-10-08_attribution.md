# Factor attribution — signal 2026-10-08 → prediction day 2026-10-13

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-08** | Features/scores formed from this snapshot (and deltas vs **2026-10-07**). Only data on/before this date. |
| **Prediction day** | **2026-10-13** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-08 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-13 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11689** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.1301**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.45% | 15.5% | 2541 |
| 2 | -0.33% | 11.0% | 2170 |
| 3 | -0.72% | 13.7% | 2306 |
| 4 | -0.39% | 15.7% | 2334 |
| 5 | -0.34% | 30.3% | 2338 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.4135 | +0.1275 | -0.5527 | -0.23% | 0.53% | 4376/256 |
| Performance (Week) | +0.3012 | +0.0907 | +0.3637 | 0.19% | 0.68% | 6315/5205 |
| true_ret | +0.2175 | +0.0616 | +0.2784 | 0.00% | 0.91% | 5249/5898 |
| d_Performance (YTD) | +0.2079 | +0.0683 | +0.2060 | -0.01% | 0.88% | 5327/5971 |
| Performance (Month) | +0.2014 | -0.1247 | +0.3635 | -0.07% | 0.64% | 3712/7792 |
| d_50-Day Simple Moving Average | +0.1954 | +0.0780 | +0.2236 | -0.15% | 0.93% | 5635/5958 |
| d_200-Day Simple Moving Average | +0.1951 | +0.0733 | +0.2003 | -0.12% | 0.91% | 5497/6068 |
| d_Price | +0.1908 | +0.0786 | +0.1505 | 0.00% | 0.91% | 5249/5898 |
| d_Market Cap | +0.1828 | -0.0390 | +0.2477 | -0.62% | 2.73% | 2986/2712 |
| Relative Strength Index (14) | +0.1744 | -0.0003 | +0.1929 | 0.40% | n/a | 11604/0 |
| d_20-Day Simple Moving Average | +0.1674 | +0.0825 | +0.1859 | -0.27% | 1.09% | 5905/5695 |
| d_Relative Strength Index (14) | +0.1654 | +0.0617 | +0.1309 | -0.04% | 0.85% | 5322/5960 |
| d_Forward P/E | +0.1438 | -0.0059 | +0.1922 | 0.36% | -0.52% | 1896/1069 |
| d_Performance (Month) | +0.1371 | +0.1758 | +0.0701 | -0.33% | 1.76% | 7313/4076 |
| Short Float | -0.1243 | +0.2217 | -0.2013 | 1.02% | n/a | 5678/0 |
| d_Performance (Week) | +0.1241 | +0.0783 | +0.1046 | -0.45% | 1.17% | 5426/6087 |
| Institutional Transactions | -0.1151 | +0.0206 | -0.1464 | 2.65% | -1.05% | 3240/1800 |
| d_Performance (Quarter) | +0.0464 | +0.0185 | +0.0672 | -0.65% | 1.47% | 5181/5935 |
| d_Target Price | +0.0429 | +0.0689 | -0.0303 | 0.57% | -0.84% | 219/310 |
| d_Volatility (Month) | +0.0426 | -0.0786 | +0.1056 | 1.37% | -0.40% | 4626/4885 |
| d_Beta | -0.0371 | -0.0321 | -0.0435 | 3.28% | -1.57% | 695/1194 |
| d_EPS Surprise | -0.0262 | -0.0522 | +0.0134 | -2.49% | 1.19% | 8/6 |
| d_Short Ratio | -0.0219 | +0.0405 | -0.0545 | -0.40% | 0.00% | 3683/3429 |
| d_Sales Growth Quarter Over Quarter | -0.0199 | -0.0490 | +0.0061 | -8.70% | -0.80% | 1/11 |
| Relative Volume | +0.0189 | +0.0909 | -0.0374 | 0.40% | n/a | 11443/0 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 340 | -1.92% | 28.5% |
| true_ret>3% & UPTREND | 187 | 1.02% | 51.9% |
| true_ret>3% & MIXED | 137 | 1.22% | 40.1% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 124 | 0.22% | 1.77% |
| WASHED | 1361 | 5.41% | -5.19% |
