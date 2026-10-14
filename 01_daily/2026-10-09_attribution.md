# Factor attribution — signal 2026-10-09 → prediction day 2026-10-14

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-09** | Features/scores formed from this snapshot (and deltas vs **2026-10-08**). Only data on/before this date. |
| **Prediction day** | **2026-10-14** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-09 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-14 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11697** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.2697**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.01% | 16.3% | 2345 |
| 2 | -0.43% | 9.3% | 2389 |
| 3 | -0.55% | 9.9% | 2342 |
| 4 | -3.41% | 10.2% | 2286 |
| 5 | -4.21% | 7.9% | 2335 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.4780 | -0.1947 | -0.4199 | -2.32% | 0.19% | 8053/3102 |
| upside_pct_lvl | -0.4773 | +0.1179 | -0.5121 | -2.09% | -1.92% | 4353/278 |
| d_Performance (Month) | -0.3709 | -0.0965 | -0.3315 | -2.44% | 0.65% | 8718/2717 |
| Performance (Week) | +0.2789 | +0.1563 | +0.3010 | -0.97% | -2.60% | 6245/5267 |
| d_20-Day Simple Moving Average | -0.2302 | -0.0451 | -0.1686 | -2.02% | -0.97% | 8197/3392 |
| d_200-Day Simple Moving Average | -0.2109 | -0.0736 | -0.1129 | -2.15% | -0.81% | 7704/3860 |
| d_50-Day Simple Moving Average | -0.2019 | -0.0450 | -0.1313 | -2.12% | -0.82% | 7972/3617 |
| d_Performance (YTD) | -0.1948 | -0.0699 | -0.0829 | -2.04% | -0.95% | 7514/3804 |
| true_ret | -0.1944 | -0.0710 | -0.1070 | -2.02% | -1.76% | 7432/3713 |
| Short Float | -0.1829 | +0.1396 | -0.2617 | -1.06% | n/a | 5681/0 |
| Institutional Transactions | -0.1615 | -0.0188 | -0.1865 | -0.32% | -1.95% | 3240/1801 |
| d_Forward P/E | -0.1610 | +0.0116 | -0.1604 | -2.31% | -1.13% | 1556/1401 |
| d_Price | -0.1430 | -0.0867 | +0.0363 | -2.02% | -1.76% | 7432/3713 |
| d_Relative Strength Index (14) | -0.0988 | -0.1301 | +0.1637 | -2.05% | -1.02% | 7492/3812 |
| d_Beta | -0.0914 | +0.0185 | -0.1056 | -2.06% | 4.03% | 1553/733 |
| d_Volatility (Month) | -0.0825 | +0.0761 | -0.1211 | -1.14% | -2.99% | 6020/3625 |
| Performance (Month) | +0.0799 | -0.0969 | +0.1775 | -2.79% | -1.04% | 4341/7157 |
| d_Market Cap | -0.0721 | -0.0050 | -0.0162 | -1.83% | -0.32% | 3037/2669 |
| Relative Strength Index (14) | +0.0698 | +0.1617 | +0.1891 | -1.70% | n/a | 11610/0 |
| d_Relative Volume | +0.0416 | -0.0491 | +0.0650 | 1.02% | -2.92% | 3568/7764 |
| d_Short Float | +0.0343 | +0.0155 | +0.0387 | -7.13% | -3.12% | 28/57 |
| Relative Volume | +0.0318 | -0.0061 | -0.0220 | -1.73% | n/a | 11402/0 |
| d_Performance (Week) | -0.0263 | -0.0586 | -0.0046 | -1.34% | -2.07% | 5522/5954 |
| d_Total Debt/Equity | -0.0248 | -0.0219 | -0.0079 | -5.28% | -0.40% | 5/4 |
| d_Gross Margin | +0.0180 | +0.0053 | +0.0451 | -0.95% | -5.18% | 6/4 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 428 | 7.00% | 8.4% |
| true_ret>3% & UPTREND | 360 | -7.62% | 10.8% |
| true_ret>3% & MIXED | 187 | -6.19% | 10.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 172 | -4.56% | -13.90% |
| WASHED | 1068 | 5.41% | 1.02% |
