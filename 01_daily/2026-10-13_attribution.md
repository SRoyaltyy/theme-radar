# Factor attribution — signal 2026-10-13 → prediction day 2026-10-16

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-13** | Features/scores formed from this snapshot (and deltas vs **2026-10-12**). Only data on/before this date. |
| **Prediction day** | **2026-10-16** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-13 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-16 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11714** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0138**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -3.14% | 15.4% | 2347 |
| 2 | -1.49% | 14.4% | 2593 |
| 3 | -1.60% | 14.6% | 2255 |
| 4 | -1.72% | 15.8% | 2222 |
| 5 | -2.89% | 21.6% | 2297 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.4634 | +0.1198 | +0.5125 | -0.08% | -3.67% | 4766/6752 |
| upside_pct_lvl | -0.3297 | +0.1983 | -0.3524 | -1.83% | -2.14% | 4355/280 |
| d_20-Day Simple Moving Average | +0.2837 | +0.0576 | +0.2823 | -0.80% | -3.38% | 5416/6156 |
| d_50-Day Simple Moving Average | +0.2702 | +0.0482 | +0.2708 | -0.82% | -3.40% | 5438/6098 |
| true_ret | +0.2503 | +0.0023 | +0.2829 | -0.83% | -3.39% | 5046/5892 |
| d_200-Day Simple Moving Average | +0.2501 | +0.0201 | +0.2551 | -0.89% | -3.22% | 5203/6309 |
| d_Performance (YTD) | +0.2483 | -0.0048 | +0.2680 | -0.83% | -3.36% | 5190/6004 |
| d_Price | +0.2391 | -0.0086 | +0.2398 | -0.83% | -3.39% | 5046/5892 |
| d_Relative Strength Index (14) | +0.2318 | -0.1012 | +0.1754 | -0.85% | -3.37% | 5201/6013 |
| d_Beta | +0.1669 | -0.0183 | +0.1955 | -2.38% | -5.15% | 578/990 |
| d_Performance (Week) | +0.1613 | -0.0028 | +0.1741 | -1.55% | -2.57% | 4269/7230 |
| Institutional Transactions | -0.1339 | -0.0225 | -0.1295 | -2.85% | -0.50% | 3265/1778 |
| Short Float | -0.1169 | +0.1606 | -0.2607 | -2.03% | n/a | 5673/0 |
| d_Target Price | -0.1162 | -0.0453 | -0.0747 | -1.98% | 0.49% | 191/376 |
| d_Market Cap | +0.1140 | +0.0285 | +0.1178 | -0.90% | -2.81% | 2390/3314 |
| d_Performance (Month) | -0.1110 | -0.1932 | -0.0721 | -2.49% | -1.73% | 6781/4631 |
| d_Forward P/E | +0.1093 | +0.0612 | +0.1383 | -0.65% | -1.73% | 1463/1473 |
| d_Volatility (Month) | -0.0850 | -0.0353 | -0.0907 | -2.91% | -2.15% | 4056/5089 |
| Relative Strength Index (14) | +0.0788 | +0.0040 | +0.2583 | -2.16% | n/a | 11649/0 |
| Performance (Month) | -0.0559 | -0.2387 | +0.0821 | -3.28% | -1.54% | 4139/7389 |
| d_Relative Volume | +0.0531 | -0.0286 | +0.0192 | -2.00% | -2.44% | 6637/4625 |
| Relative Volume | +0.0511 | +0.0385 | -0.0815 | -2.20% | n/a | 11426/0 |
| d_Total Debt/Equity | -0.0317 | -0.0060 | -0.0382 | -18.34% | 6.42% | 4/2 |
| d_Performance (Quarter) | +0.0312 | -0.0429 | +0.0040 | -2.98% | -1.59% | 4442/6711 |
| d_Institutional Ownership | +0.0289 | +0.0260 | +0.0484 | 1.27% | -4.26% | 11/20 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 233 | 2.29% | 26.2% |
| true_ret>3% & UPTREND | 162 | -3.13% | 30.2% |
| true_ret>3% & MIXED | 96 | -3.14% | 29.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 157 | -3.23% | -8.05% |
| WASHED | 1275 | -3.10% | 0.75% |
