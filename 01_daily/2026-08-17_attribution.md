# Factor attribution — signal 2026-08-17 → prediction day 2026-08-19

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-17** | Features/scores formed from this snapshot (and deltas vs **2026-08-14**). Only data on/before this date. |
| **Prediction day** | **2026-08-19** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-17 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-19 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11559** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1365**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 12.72% | 34.0% | 2389 |
| 2 | 0.53% | 15.5% | 2569 |
| 3 | -0.13% | 14.6% | 2742 |
| 4 | -1.02% | 17.7% | 1710 |
| 5 | -1.02% | 30.4% | 2149 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.2502 | -0.0832 | -0.3129 | -0.94% | 7.59% | 6854/4493 |
| d_Forward P/E | -0.1808 | -0.0767 | -0.1996 | -1.34% | 0.08% | 946/2035 |
| d_Performance (Month) | -0.1807 | -0.0037 | -0.2034 | -0.68% | 6.40% | 6255/5001 |
| d_Performance (Week) | -0.1774 | -0.0992 | -0.2266 | -0.68% | 5.30% | 5397/5921 |
| d_Performance (Quarter) | -0.1533 | +0.0936 | -0.2790 | -0.27% | 10.39% | 7737/3073 |
| Performance (Month) | -0.1291 | +0.0586 | -0.2042 | -0.63% | 7.93% | 7258/4072 |
| d_50-Day Simple Moving Average | -0.1280 | -0.0851 | -0.1461 | -0.88% | 4.12% | 3907/7509 |
| d_Relative Strength Index (14) | -0.1231 | +0.1634 | -0.2655 | -0.74% | 4.19% | 3809/7306 |
| true_ret | -0.1135 | -0.0985 | -0.1016 | -0.77% | 4.24% | 3758/7234 |
| d_Performance (YTD) | -0.1091 | -0.0688 | -0.1161 | -0.80% | 4.17% | 3839/7327 |
| Relative Strength Index (14) | -0.1008 | -0.0718 | +0.2605 | 2.43% | n/a | 11438/0 |
| d_Price | -0.1001 | +0.0273 | -0.1912 | -0.77% | 4.24% | 3758/7234 |
| d_200-Day Simple Moving Average | -0.0939 | -0.0569 | -0.1158 | -0.76% | 4.04% | 3873/7541 |
| d_Market Cap | -0.0917 | +0.0465 | -0.1684 | -0.11% | 8.56% | 2055/3681 |
| Short Float | +0.0867 | +0.2875 | -0.2255 | 5.50% | n/a | 5685/0 |
| d_Beta | -0.0818 | -0.0254 | -0.0894 | 8.70% | 4.16% | 1931/1503 |
| d_20-Day Simple Moving Average | -0.0710 | -0.0943 | -0.0499 | -0.58% | 3.74% | 3512/7914 |
| upside_pct_lvl | +0.0572 | +0.2832 | -0.1894 | 6.04% | 0.30% | 4310/337 |
| d_Volatility (Month) | +0.0427 | -0.1402 | +0.1593 | 1.41% | 3.60% | 2961/6551 |
| Institutional Transactions | -0.0421 | -0.0083 | -0.0799 | 3.60% | 9.06% | 2689/2352 |
| d_Short Ratio | +0.0407 | +0.0875 | +0.0027 | 0.27% | 1.64% | 4297/2460 |
| Relative Volume | +0.0301 | +0.0876 | -0.0894 | 2.43% | n/a | 11311/0 |
| d_Average Volume | -0.0256 | -0.0837 | +0.0316 | 6.61% | -0.03% | 4199/6780 |
| d_Analyst Recom | +0.0248 | +0.0177 | +0.0286 | -0.00% | -0.50% | 170/167 |
| d_Total Debt/Equity | -0.0217 | -0.0179 | -0.0427 | -0.70% | 63.13% | 115/79 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 216 | -1.55% | 31.5% |
| true_ret>3% & UPTREND | 338 | -4.04% | 30.8% |
| true_ret>3% & MIXED | 194 | -2.55% | 35.1% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 309 | -4.84% | -13.47% |
| WASHED | 492 | 61.69% | 1.36% |
