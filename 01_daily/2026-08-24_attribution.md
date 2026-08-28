# Factor attribution — signal 2026-08-24 → prediction day 2026-08-28

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-24** | Features/scores formed from this snapshot (and deltas vs **2026-08-21**). Only data on/before this date. |
| **Prediction day** | **2026-08-28** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-24 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-28 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11605** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0867**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.79% | 38.4% | 2376 |
| 2 | 1.14% | 24.8% | 2960 |
| 3 | 0.29% | 11.3% | 1781 |
| 4 | 0.47% | 15.0% | 2187 |
| 5 | 3.40% | 34.2% | 2301 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Price | -0.3354 | -0.3203 | -0.0484 | 0.31% | 1.66% | 4452/6543 |
| d_Performance (YTD) | -0.3261 | -0.3810 | -0.0694 | 0.26% | 2.29% | 4523/6632 |
| d_200-Day Simple Moving Average | -0.3210 | -0.3710 | -0.1019 | 0.36% | 2.19% | 4561/6899 |
| d_20-Day Simple Moving Average | -0.3136 | -0.4156 | -0.0589 | 0.32% | 2.11% | 4156/7305 |
| true_ret | -0.3105 | -0.3940 | -0.0715 | 0.31% | 1.66% | 4452/6543 |
| d_50-Day Simple Moving Average | -0.3086 | -0.3875 | -0.0956 | 0.33% | 2.18% | 4443/7007 |
| d_Relative Strength Index (14) | -0.3015 | -0.2227 | -0.0142 | 0.32% | 2.27% | 4532/6578 |
| d_Forward P/E | -0.2871 | -0.2457 | -0.0930 | -0.47% | 1.53% | 1398/1537 |
| d_Performance (Week) | -0.2719 | -0.2392 | -0.1436 | 0.81% | 2.27% | 6179/5151 |
| Performance (Week) | -0.2543 | -0.2655 | -0.1450 | 0.89% | 1.93% | 5048/6337 |
| d_Performance (Quarter) | -0.2522 | -0.3104 | -0.0599 | 0.41% | 2.05% | 4059/6757 |
| d_Market Cap | -0.2027 | -0.1401 | -0.0018 | 0.74% | 2.81% | 2451/3252 |
| Relative Strength Index (14) | -0.1352 | -0.2109 | +0.0806 | 1.46% | n/a | 11481/0 |
| upside_pct_lvl | +0.1296 | +0.3656 | -0.2613 | 2.19% | -0.15% | 4297/346 |
| Short Float | +0.0838 | +0.2869 | -0.0835 | 1.95% | n/a | 5681/0 |
| Institutional Transactions | +0.0765 | +0.1350 | +0.0141 | 2.95% | 1.07% | 3177/1880 |
| d_Performance (Month) | +0.0656 | +0.0902 | -0.0694 | 2.70% | 0.63% | 4677/6591 |
| d_Institutional Ownership | -0.0553 | -0.0512 | +0.0419 | -0.00% | 0.68% | 881/409 |
| d_Beta | +0.0402 | +0.1084 | -0.0665 | 2.34% | 2.05% | 2014/1223 |
| Performance (Month) | +0.0279 | +0.1385 | -0.0733 | 1.03% | 2.45% | 7796/3550 |
| Relative Volume | -0.0253 | +0.0658 | -0.0206 | 1.47% | n/a | 11329/0 |
| d_Analyst Recom | -0.0243 | +0.0346 | -0.0299 | 6.16% | 0.70% | 109/111 |
| d_Profit Margin | -0.0209 | -0.0531 | -0.0085 | -2.18% | 0.10% | 9/10 |
| d_Gross Margin | +0.0151 | +0.0237 | -0.0119 | 0.49% | -2.38% | 16/6 |
| d_Total Debt/Equity | +0.0115 | +0.0118 | +0.0137 | -2.40% | -1.70% | 7/12 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 206 | 3.94% | 30.1% |
| true_ret>3% & UPTREND | 226 | -0.18% | 28.8% |
| true_ret>3% & MIXED | 171 | 2.95% | 40.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 458 | 1.28% | 3.07% |
| WASHED | 491 | 3.85% | 2.78% |
