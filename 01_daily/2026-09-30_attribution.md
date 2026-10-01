# Factor attribution — signal 2026-09-30 → prediction day 2026-10-01

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-30** | Features/scores formed from this snapshot (and deltas vs **2026-09-29**). Only data on/before this date. |
| **Prediction day** | **2026-10-01** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-30 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-01 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11682** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0026**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.32% | 16.5% | 2449 |
| 2 | -0.10% | 8.5% | 2616 |
| 3 | 1.41% | 12.2% | 2501 |
| 4 | 0.40% | 13.0% | 1937 |
| 5 | -0.32% | 23.6% | 2179 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2347 | +0.1748 | -0.4061 | 0.22% | -0.19% | 4405/233 |
| Performance (Month) | +0.1162 | -0.1241 | +0.2640 | 0.33% | 0.37% | 3052/8453 |
| d_Forward P/E | +0.0995 | +0.1013 | +0.0498 | 0.75% | 0.23% | 896/2050 |
| d_Performance (Week) | -0.0966 | +0.0533 | -0.1696 | 0.39% | 0.29% | 8425/3079 |
| Institutional Transactions | -0.0860 | +0.0171 | -0.1381 | 0.45% | 1.12% | 3235/1812 |
| d_Beta | -0.0710 | +0.0059 | -0.0899 | -0.07% | 0.03% | 1571/855 |
| Relative Strength Index (14) | +0.0670 | +0.0887 | -0.0656 | 0.35% | n/a | 11584/0 |
| d_20-Day Simple Moving Average | -0.0626 | -0.1137 | +0.0052 | 0.66% | 0.16% | 4508/7029 |
| d_Institutional Ownership | +0.0566 | -0.0440 | +0.0651 | 0.27% | -0.74% | 621/281 |
| d_Average Volume | -0.0560 | -0.1549 | +0.0606 | 0.42% | 0.33% | 4798/6260 |
| d_Market Cap | -0.0458 | +0.1231 | -0.1159 | 1.45% | 0.09% | 2147/3563 |
| d_200-Day Simple Moving Average | -0.0370 | -0.0913 | +0.0117 | 0.78% | 0.15% | 3969/7565 |
| d_Price | -0.0367 | -0.0122 | -0.0595 | 0.11% | 0.11% | 3737/7340 |
| d_Performance (Month) | -0.0354 | -0.0823 | +0.0100 | 0.60% | 0.13% | 5601/5743 |
| d_50-Day Simple Moving Average | -0.0351 | -0.1010 | +0.0249 | 0.80% | 0.11% | 4141/7403 |
| d_Short Ratio | +0.0307 | +0.1220 | -0.0698 | 0.29% | -0.15% | 4348/3040 |
| d_Target Price | -0.0307 | +0.0591 | -0.0445 | -0.30% | 0.18% | 141/264 |
| d_Short Float | +0.0287 | -0.0028 | +0.0393 | -0.51% | -1.16% | 27/63 |
| d_Sales Year Over Year TTM | +0.0275 | +0.0068 | +0.0401 | 1.81% | -1.65% | 10/11 |
| d_Performance (YTD) | -0.0233 | -0.0934 | +0.0275 | 0.91% | 0.11% | 3834/7424 |
| d_Volatility (Month) | -0.0218 | -0.0258 | -0.0316 | 0.24% | 0.60% | 5454/4739 |
| Performance (Week) | +0.0201 | -0.1918 | +0.1684 | 0.26% | 0.40% | 2675/8822 |
| d_Relative Strength Index (14) | -0.0197 | +0.0156 | -0.0371 | 0.89% | 0.10% | 3862/7413 |
| d_Profit Margin | -0.0192 | -0.0049 | -0.0104 | -0.32% | 0.17% | 13/12 |
| Relative Volume | +0.0135 | +0.0084 | -0.0131 | 0.36% | n/a | 11451/0 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 285 | -1.62% | 22.8% |
| true_ret>3% & UPTREND | 150 | 0.00% | 28.0% |
| true_ret>3% & MIXED | 120 | -0.11% | 27.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 172 | -0.41% | 0.56% |
| WASHED | 2596 | 0.05% | -0.61% |
