# Factor attribution — signal 2026-11-09 → prediction day 2026-11-11

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-09** | Features/scores formed from this snapshot (and deltas vs **2026-11-06**). Only data on/before this date. |
| **Prediction day** | **2026-11-11** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-09 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-11 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11727** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0774**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.81% | 21.7% | 2396 |
| 2 | 0.14% | 20.0% | 2311 |
| 3 | 1.55% | 19.5% | 2546 |
| 4 | 0.86% | 24.4% | 2561 |
| 5 | -0.26% | 25.2% | 1913 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | +0.2535 | +0.4219 | -0.1256 | 1.05% | 0.42% | 8726/2866 |
| d_Price | +0.2322 | +0.0332 | +0.0455 | 0.52% | 1.16% | 9323/1975 |
| d_Performance (YTD) | +0.2066 | +0.2167 | -0.0868 | 0.88% | 1.09% | 9381/2025 |
| Relative Strength Index (14) | -0.2032 | -0.3865 | +0.2885 | 0.88% | n/a | 11674/0 |
| d_Relative Strength Index (14) | +0.2024 | -0.2509 | +0.0631 | 0.88% | 1.06% | 9368/2034 |
| Performance (Week) | -0.2006 | -0.2451 | -0.0807 | -0.27% | 2.54% | 6802/4771 |
| d_20-Day Simple Moving Average | +0.1853 | +0.3674 | -0.2244 | 0.92% | 0.76% | 9258/2369 |
| d_200-Day Simple Moving Average | +0.1765 | +0.2601 | -0.1505 | 0.83% | 1.17% | 9536/2066 |
| Performance (Month) | -0.1740 | -0.4316 | +0.2116 | -0.50% | 2.06% | 5293/6276 |
| true_ret | +0.1728 | +0.3290 | -0.1919 | 0.52% | 1.16% | 9323/1975 |
| d_50-Day Simple Moving Average | +0.1611 | +0.3221 | -0.2097 | 0.84% | 1.12% | 9631/1989 |
| d_Performance (Quarter) | +0.1580 | +0.2161 | -0.1026 | 1.06% | 0.31% | 8588/2607 |
| d_Performance (Month) | +0.1564 | +0.2810 | -0.1444 | 0.89% | 0.92% | 8642/2839 |
| d_Beta | -0.1162 | -0.2537 | +0.1228 | 0.32% | 0.62% | 2571/2742 |
| d_Market Cap | +0.0544 | -0.0506 | +0.1752 | 0.91% | 2.62% | 4486/1280 |
| upside_pct_lvl | -0.0494 | +0.4760 | -0.4671 | 1.61% | -0.63% | 4301/326 |
| d_Insider Transactions | +0.0487 | +0.0288 | +0.0157 | 0.70% | 0.05% | 471/334 |
| d_Relative Volume | -0.0425 | +0.0305 | -0.0911 | 1.66% | 0.14% | 5596/5751 |
| Relative Volume | +0.0423 | +0.1523 | -0.1301 | 0.90% | n/a | 11481/0 |
| d_Target Price | +0.0350 | -0.0710 | +0.0753 | 0.05% | -0.47% | 393/469 |
| d_Institutional Ownership | +0.0349 | +0.0493 | +0.0177 | 0.34% | -0.35% | 2836/2149 |
| d_Sales Year Over Year TTM | +0.0314 | +0.0024 | +0.0382 | 0.20% | -0.52% | 222/205 |
| d_Analyst Recom | -0.0307 | -0.0092 | -0.0244 | -0.74% | 0.18% | 148/179 |
| d_Average Volume | +0.0258 | +0.0840 | -0.0204 | 1.42% | 0.18% | 6536/4539 |
| d_Sales Growth Quarter Over Quarter | +0.0244 | +0.0500 | +0.0518 | 0.07% | -1.27% | 123/138 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 2139 | 1.81% | 47.1% |
| true_ret>3% & UPTREND | 837 | -0.63% | 23.2% |
| true_ret>3% & MIXED | 642 | 0.61% | 36.1% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 343 | -0.81% | -0.19% |
| WASHED | 1502 | 5.64% | 3.59% |
