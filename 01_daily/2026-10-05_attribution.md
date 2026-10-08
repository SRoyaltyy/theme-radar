# Factor attribution — signal 2026-10-05 → prediction day 2026-10-08

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-05** | Features/scores formed from this snapshot (and deltas vs **2026-10-02**). Only data on/before this date. |
| **Prediction day** | **2026-10-08** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-05 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-08 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11690** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0885**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.25% | 15.5% | 2464 |
| 2 | -0.57% | 10.9% | 2318 |
| 3 | -0.42% | 11.7% | 2366 |
| 4 | -1.49% | 11.4% | 2211 |
| 5 | -2.19% | 22.4% | 2331 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.3773 | -0.1011 | -0.3427 | -1.43% | 0.36% | 7852/3246 |
| upside_pct_lvl | -0.2128 | +0.2703 | -0.3757 | -1.41% | -2.28% | 4351/282 |
| Relative Strength Index (14) | -0.1906 | -0.0102 | -0.0266 | -0.96% | n/a | 11597/0 |
| d_Performance (Week) | -0.1851 | +0.0955 | -0.2090 | -1.20% | -0.22% | 8846/2661 |
| Performance (Month) | -0.1277 | -0.3773 | +0.0030 | -2.53% | -0.26% | 3557/7937 |
| Institutional Transactions | -0.1205 | +0.0068 | -0.1328 | -1.00% | -0.63% | 3242/1803 |
| true_ret | -0.0799 | -0.0033 | -0.0465 | -1.35% | -0.73% | 6922/4222 |
| d_Performance (YTD) | -0.0791 | -0.0155 | -0.0249 | -1.14% | -0.67% | 7002/4295 |
| d_Performance (Month) | +0.0745 | -0.0076 | +0.0629 | -1.07% | -0.90% | 4135/7250 |
| Short Float | -0.0744 | +0.2376 | -0.1711 | -0.67% | n/a | 5687/0 |
| d_200-Day Simple Moving Average | -0.0720 | +0.0135 | -0.0409 | -1.10% | -0.75% | 7142/4407 |
| Performance (Week) | -0.0706 | -0.0466 | -0.0139 | -1.46% | -0.44% | 6269/5228 |
| d_Average Volume | +0.0652 | -0.0489 | +0.0644 | -0.93% | -1.02% | 5381/5686 |
| d_50-Day Simple Moving Average | -0.0637 | +0.0312 | -0.0454 | -1.06% | -0.80% | 7355/4237 |
| d_Target Price | -0.0591 | +0.0492 | -0.1414 | -1.29% | -0.22% | 248/468 |
| d_20-Day Simple Moving Average | -0.0530 | +0.0933 | -0.0555 | -0.96% | -0.99% | 8012/3576 |
| d_Price | -0.0525 | -0.0374 | +0.0438 | -1.35% | -0.73% | 6922/4222 |
| d_Short Ratio | -0.0473 | +0.0426 | -0.0441 | -1.54% | -1.02% | 3831/3432 |
| d_Institutional Ownership | -0.0379 | -0.0134 | -0.0630 | -0.53% | -0.95% | 1171/1735 |
| d_Total Debt/Equity | +0.0370 | -0.0037 | +0.0394 | 2.32% | -17.54% | 2/2 |
| d_Volatility (Month) | -0.0366 | +0.0065 | -0.0869 | -1.07% | -1.22% | 5346/4293 |
| d_Market Cap | +0.0339 | +0.0600 | -0.0488 | -0.93% | -0.42% | 2755/2966 |
| d_Relative Volume | +0.0299 | +0.0039 | -0.0001 | -1.14% | -0.79% | 5597/5753 |
| d_Forward P/E | +0.0299 | +0.0301 | -0.0380 | -0.44% | -0.57% | 1599/1332 |
| d_Sales Year Over Year TTM | +0.0286 | +0.0375 | +0.0330 | 3.27% | -12.25% | 2/2 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 381 | -2.70% | 26.0% |
| true_ret>3% & UPTREND | 356 | -5.61% | 14.0% |
| true_ret>3% & MIXED | 218 | -4.50% | 23.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 251 | -6.20% | -9.80% |
| WASHED | 1953 | -0.05% | -2.14% |
