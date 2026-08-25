# Factor attribution — signal 2026-08-24 → prediction day 2026-08-25

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-24** | Features/scores formed from this snapshot (and deltas vs **2026-08-21**). Only data on/before this date. |
| **Prediction day** | **2026-08-25** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-24 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-25 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11605** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0056**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.20% | 26.6% | 2376 |
| 2 | 0.60% | 16.7% | 2960 |
| 3 | 0.38% | 9.7% | 1781 |
| 4 | 0.51% | 9.2% | 2187 |
| 5 | 1.09% | 34.8% | 2301 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | +0.2369 | +0.4286 | -0.2685 | 1.02% | 0.11% | 4297/346 |
| d_20-Day Simple Moving Average | -0.2286 | -0.3343 | +0.0635 | 0.32% | 0.99% | 4156/7305 |
| true_ret | -0.2145 | -0.3022 | +0.0569 | 0.31% | 1.04% | 4452/6543 |
| d_Performance (YTD) | -0.2131 | -0.2874 | +0.0587 | 0.30% | 1.04% | 4523/6632 |
| d_200-Day Simple Moving Average | -0.2110 | -0.2774 | +0.0328 | 0.36% | 1.00% | 4561/6899 |
| d_50-Day Simple Moving Average | -0.2090 | -0.2980 | +0.0349 | 0.35% | 1.00% | 4443/7007 |
| d_Performance (Week) | -0.1986 | -0.2054 | -0.0197 | 0.31% | 1.28% | 6179/5151 |
| d_Price | -0.1945 | -0.2152 | +0.0631 | 0.31% | 1.04% | 4452/6543 |
| d_Relative Strength Index (14) | -0.1788 | -0.1626 | +0.0728 | 0.31% | 1.03% | 4532/6578 |
| Performance (Week) | -0.1284 | -0.1337 | -0.0565 | 0.47% | 0.98% | 5048/6337 |
| d_Forward P/E | -0.1211 | -0.1421 | +0.0583 | 0.04% | 1.11% | 1398/1537 |
| Relative Strength Index (14) | -0.1198 | -0.1870 | +0.1178 | 0.77% | n/a | 11481/0 |
| d_Market Cap | -0.1165 | -0.1191 | +0.0792 | 0.43% | 1.11% | 2451/3252 |
| Short Float | +0.1036 | +0.2757 | -0.0664 | 0.82% | n/a | 5681/0 |
| d_Performance (Month) | +0.1029 | +0.1312 | -0.0431 | 1.12% | 0.54% | 4677/6591 |
| d_Performance (Quarter) | -0.0962 | -0.1596 | +0.0463 | 0.55% | 0.86% | 4059/6757 |
| d_Institutional Ownership | -0.0697 | -0.1026 | +0.0807 | 0.03% | 0.58% | 881/409 |
| d_Beta | +0.0612 | +0.1249 | -0.0699 | 1.67% | 1.12% | 2014/1223 |
| Institutional Transactions | +0.0602 | +0.1320 | -0.0410 | 1.34% | 0.47% | 3177/1880 |
| d_Volatility (Month) | +0.0431 | -0.0172 | +0.0679 | 1.06% | 0.72% | 3466/5985 |
| d_Analyst Recom | -0.0397 | +0.0046 | -0.0305 | -0.20% | 1.08% | 109/111 |
| Performance (Month) | +0.0370 | +0.1037 | -0.0510 | 0.75% | 0.83% | 7796/3550 |
| d_Profit Margin | -0.0216 | -0.0501 | -0.0102 | -0.80% | 0.70% | 9/10 |
| d_Short Ratio | -0.0176 | -0.0163 | -0.0042 | 0.63% | 1.24% | 3704/3062 |
| d_Sales Year Over Year TTM | -0.0173 | -0.0426 | +0.0005 | -0.64% | -0.52% | 9/8 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 206 | 0.69% | 31.1% |
| true_ret>3% & UPTREND | 226 | -0.04% | 25.2% |
| true_ret>3% & MIXED | 171 | 1.74% | 38.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 458 | 1.05% | 1.85% |
| WASHED | 491 | 2.04% | 1.56% |
