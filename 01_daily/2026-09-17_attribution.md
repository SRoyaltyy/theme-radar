# Factor attribution — signal 2026-09-17 → prediction day 2026-09-22

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-17** | Features/scores formed from this snapshot (and deltas vs **2026-09-16**). Only data on/before this date. |
| **Prediction day** | **2026-09-22** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-17 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-22 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11619** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.3070**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.45% | 18.2% | 2379 |
| 2 | 1.14% | 16.5% | 2272 |
| 3 | 1.32% | 23.3% | 2499 |
| 4 | 2.47% | 46.0% | 2475 |
| 5 | 5.57% | 58.6% | 1994 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | +0.3570 | +0.4824 | +0.0174 | 2.70% | 0.75% | 9165/2281 |
| d_Performance (Month) | +0.3564 | +0.4335 | +0.0130 | 2.40% | 2.05% | 8731/2588 |
| d_200-Day Simple Moving Average | +0.3079 | +0.3841 | +0.0144 | 2.23% | 2.40% | 8774/2756 |
| d_50-Day Simple Moving Average | +0.3053 | +0.4127 | -0.0039 | 2.45% | 1.82% | 8846/2699 |
| d_20-Day Simple Moving Average | +0.3007 | +0.4189 | -0.0302 | 2.60% | 1.14% | 9163/2387 |
| d_Performance (YTD) | +0.2960 | +0.3423 | +0.0246 | 2.15% | 2.79% | 8661/2646 |
| true_ret | +0.2918 | +0.3907 | -0.0053 | 2.26% | 1.43% | 8594/2600 |
| d_Price | +0.2844 | +0.1855 | +0.1350 | 2.26% | 1.43% | 8594/2600 |
| upside_pct_lvl | +0.1828 | +0.3276 | -0.1969 | 1.41% | -0.78% | 4354/285 |
| d_Relative Strength Index (14) | +0.1669 | -0.1229 | +0.3502 | 2.14% | 2.91% | 8640/2646 |
| d_Performance (Quarter) | +0.1641 | +0.2492 | -0.0568 | 1.77% | 4.13% | 8953/2020 |
| d_Forward P/E | +0.1511 | +0.2235 | -0.0263 | 0.82% | -0.38% | 1726/1214 |
| d_Beta | -0.1171 | -0.0671 | -0.1002 | 3.38% | 3.75% | 2114/1458 |
| Relative Strength Index (14) | +0.1071 | +0.0101 | -0.1626 | 2.29% | n/a | 11541/0 |
| Short Float | +0.1059 | +0.2363 | -0.1773 | 2.23% | n/a | 5690/0 |
| d_Market Cap | +0.0978 | +0.1163 | -0.0160 | 1.18% | 3.83% | 3632/2075 |
| Performance (Week) | +0.0749 | -0.0373 | +0.1448 | 1.85% | 2.79% | 5690/5716 |
| d_Average Volume | -0.0728 | -0.0464 | -0.0078 | 2.70% | 1.98% | 5581/5448 |
| Relative Volume | -0.0579 | +0.0629 | -0.0260 | 2.32% | n/a | 11415/0 |
| d_Short Ratio | +0.0547 | +0.0454 | -0.0187 | 1.80% | 2.19% | 3417/3674 |
| Institutional Transactions | +0.0384 | +0.1056 | -0.0098 | 2.49% | 2.03% | 3209/1825 |
| d_Relative Volume | +0.0313 | +0.0109 | +0.0033 | 1.93% | 2.58% | 4865/6376 |
| d_Profit Margin | -0.0204 | -0.0271 | -0.0273 | -1.35% | 3.94% | 4/7 |
| Performance (Month) | +0.0203 | -0.0595 | +0.1129 | 2.38% | 2.26% | 3688/7738 |
| d_Target Price | -0.0194 | +0.0531 | -0.0263 | 11.64% | 1.01% | 108/136 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 711 | 9.93% | 59.1% |
| true_ret>3% & UPTREND | 541 | 5.50% | 65.2% |
| true_ret>3% & MIXED | 380 | 8.19% | 65.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 159 | 3.77% | 10.65% |
| WASHED | 1112 | 9.31% | 8.88% |
