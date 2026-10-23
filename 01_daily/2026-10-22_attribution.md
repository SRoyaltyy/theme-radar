# Factor attribution — signal 2026-10-22 → prediction day 2026-10-23

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-22** | Features/scores formed from this snapshot (and deltas vs **2026-10-21**). Only data on/before this date. |
| **Prediction day** | **2026-10-23** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-22 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-23 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11759** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.1349**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.57% | 18.0% | 2497 |
| 2 | 0.64% | 12.9% | 2331 |
| 3 | -0.35% | 8.9% | 2525 |
| 4 | -0.58% | 10.0% | 2080 |
| 5 | 0.77% | 8.5% | 2326 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | -0.1933 | -0.1717 | -0.1286 | 0.03% | 0.48% | 6569/4921 |
| d_Forward P/E | -0.1396 | -0.2564 | +0.0425 | -0.26% | 0.10% | 1793/1174 |
| d_50-Day Simple Moving Average | -0.1201 | -0.1840 | -0.0384 | 0.22% | 0.25% | 5162/6443 |
| d_200-Day Simple Moving Average | -0.1161 | -0.1812 | -0.0342 | 0.28% | 0.20% | 5003/6582 |
| d_Performance (YTD) | -0.1124 | -0.1823 | -0.0268 | 0.32% | 0.20% | 4869/6506 |
| d_20-Day Simple Moving Average | -0.1114 | -0.1662 | -0.0459 | 0.24% | 0.23% | 5179/6428 |
| d_Price | -0.1061 | -0.1426 | -0.0664 | 0.32% | 0.20% | 4820/6445 |
| upside_pct_lvl | -0.1046 | +0.2814 | -0.3787 | -0.20% | -0.05% | 4297/340 |
| d_Market Cap | -0.1025 | -0.2140 | +0.0933 | 0.71% | 0.58% | 2833/2892 |
| true_ret | -0.0977 | -0.2104 | +0.0094 | 0.32% | 0.20% | 4820/6445 |
| Short Float | -0.0916 | +0.1242 | -0.1898 | 0.68% | n/a | 5653/0 |
| d_Relative Strength Index (14) | -0.0904 | -0.1023 | -0.0935 | 0.31% | 0.16% | 4871/6492 |
| d_Performance (Week) | +0.0643 | -0.1279 | +0.1680 | 0.69% | 0.03% | 3570/7952 |
| d_Performance (Quarter) | -0.0551 | -0.0364 | -0.0826 | 0.13% | 0.30% | 4918/6279 |
| d_Gross Margin | +0.0443 | +0.0021 | +0.0443 | 0.59% | -1.08% | 42/37 |
| d_Total Debt/Equity | -0.0361 | +0.0382 | -0.0324 | -0.74% | 0.20% | 36/60 |
| d_Profit Margin | +0.0315 | -0.0451 | +0.0684 | -0.02% | -0.76% | 66/46 |
| d_Sales Growth Quarter Over Quarter | -0.0266 | +0.0009 | -0.0397 | -0.66% | 0.14% | 58/57 |
| Performance (Week) | -0.0211 | -0.1617 | +0.1062 | 0.32% | 0.16% | 4968/6583 |
| d_Target Price | +0.0202 | -0.0111 | -0.0067 | -0.09% | 3.32% | 212/236 |
| d_Relative Volume | +0.0187 | +0.0007 | +0.0040 | 0.49% | -0.09% | 6654/4669 |
| d_Average Volume | -0.0177 | -0.0257 | -0.0113 | 0.77% | -0.29% | 5676/5290 |
| d_Institutional Ownership | +0.0164 | +0.0329 | +0.0356 | -0.34% | 1.27% | 1078/1058 |
| d_Short Ratio | +0.0160 | +0.0049 | +0.0086 | -0.33% | 0.70% | 3354/3497 |
| Relative Strength Index (14) | -0.0140 | -0.1913 | +0.1612 | 0.22% | n/a | 11677/0 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 473 | -1.27% | 14.4% |
| true_ret>3% & UPTREND | 449 | -0.73% | 13.6% |
| true_ret>3% & MIXED | 286 | 11.93% | 15.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 238 | -0.81% | -0.93% |
| WASHED | 1746 | 1.28% | -1.06% |
