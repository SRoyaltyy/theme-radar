# Factor attribution — signal 2026-11-02 → prediction day 2026-11-04

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-02** | Features/scores formed from this snapshot (and deltas vs **2026-10-30**). Only data on/before this date. |
| **Prediction day** | **2026-11-04** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-02 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-04 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11734** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.1523**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.47% | 38.2% | 2477 |
| 2 | 1.01% | 36.1% | 2625 |
| 3 | 0.92% | 33.9% | 1941 |
| 4 | 1.97% | 37.6% | 2360 |
| 5 | 2.30% | 56.1% | 2331 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Forward P/E | +0.2580 | +0.0184 | +0.3273 | 2.42% | -0.14% | 1886/1076 |
| d_Performance (Week) | +0.2169 | +0.1281 | +0.2435 | 2.40% | 0.53% | 5028/6532 |
| d_Relative Strength Index (14) | +0.2070 | +0.1647 | +0.1637 | 1.88% | 0.73% | 5279/6092 |
| d_20-Day Simple Moving Average | +0.1955 | +0.1207 | +0.2377 | 2.13% | 0.60% | 5656/5952 |
| d_50-Day Simple Moving Average | +0.1897 | +0.0842 | +0.2465 | 2.04% | 0.66% | 5715/5903 |
| d_Price | +0.1825 | +0.0715 | +0.2024 | 1.91% | 0.73% | 5178/6018 |
| d_200-Day Simple Moving Average | +0.1816 | +0.0668 | +0.2372 | 2.05% | 0.71% | 5482/6114 |
| d_Performance (YTD) | +0.1784 | +0.0493 | +0.2306 | 1.89% | 0.74% | 5276/6092 |
| true_ret | +0.1775 | +0.0482 | +0.2767 | 1.91% | 0.73% | 5178/6018 |
| d_Performance (Month) | +0.1744 | +0.0493 | +0.2490 | 2.22% | 0.79% | 4541/6953 |
| Short Float | +0.1685 | +0.3323 | -0.1668 | 1.71% | n/a | 5640/0 |
| d_Market Cap | +0.1626 | -0.0652 | +0.2218 | 1.98% | 0.87% | 3047/2678 |
| d_Performance (Quarter) | +0.0740 | -0.0780 | +0.2142 | 2.25% | 1.05% | 3315/7888 |
| Performance (Week) | +0.0605 | -0.0627 | +0.1636 | 1.42% | 1.27% | 5349/6238 |
| d_Relative Volume | -0.0380 | -0.0552 | -0.0390 | 1.20% | 1.51% | 5639/5687 |
| d_Volatility (Month) | +0.0366 | +0.1788 | -0.1384 | 1.65% | 1.09% | 5612/4520 |
| d_Beta | +0.0351 | +0.1934 | -0.0811 | 1.97% | 1.18% | 3609/3660 |
| d_Short Ratio | -0.0348 | -0.0624 | +0.0031 | 1.24% | 1.55% | 2939/4104 |
| d_Average Volume | +0.0339 | +0.0529 | -0.0371 | 1.47% | 1.15% | 6435/4647 |
| Relative Volume | +0.0314 | +0.0617 | -0.0714 | 1.35% | n/a | 11495/0 |
| d_Sales Year Over Year TTM | -0.0283 | +0.0053 | +0.0109 | 0.16% | 1.84% | 62/46 |
| Performance (Month) | +0.0261 | -0.2042 | +0.2140 | 1.19% | 1.46% | 5043/6527 |
| Institutional Transactions | -0.0220 | +0.0726 | -0.0619 | 1.50% | 2.34% | 3193/1831 |
| d_Target Price | -0.0186 | -0.0361 | +0.0007 | 1.13% | 1.72% | 361/329 |
| d_Institutional Ownership | +0.0178 | +0.0012 | -0.0099 | 1.57% | 1.85% | 2134/1420 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 463 | 3.08% | 59.2% |
| true_ret>3% & UPTREND | 357 | 2.58% | 60.5% |
| true_ret>3% & MIXED | 317 | 1.77% | 59.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 270 | 0.41% | 0.27% |
| WASHED | 1780 | 1.41% | 4.09% |
