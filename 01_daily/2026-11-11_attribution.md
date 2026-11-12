# Factor attribution — signal 2026-11-11 → prediction day 2026-11-12

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-11** | Features/scores formed from this snapshot (and deltas vs **2026-11-10**). Only data on/before this date. |
| **Prediction day** | **2026-11-12** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-11 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-12 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11739** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.1496**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -1.34% | 11.8% | 2356 |
| 2 | -0.74% | 3.0% | 2837 |
| 3 | -1.49% | 4.8% | 1955 |
| 4 | -1.37% | 4.4% | 2250 |
| 5 | -0.83% | 10.1% | 2341 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2776 | +0.5254 | -0.5263 | -1.23% | -1.43% | 4327/308 |
| Short Float | -0.2723 | +0.1098 | -0.2606 | -1.16% | n/a | 5646/0 |
| d_Performance (Month) | -0.2000 | +0.1276 | -0.2393 | -1.14% | -1.14% | 7545/3926 |
| d_Volatility (Month) | -0.1501 | +0.2672 | -0.2804 | -1.10% | -1.53% | 7541/2371 |
| d_50-Day Simple Moving Average | -0.1219 | +0.1513 | -0.1427 | -1.00% | -1.44% | 8062/3524 |
| Relative Strength Index (14) | +0.1089 | -0.3242 | +0.2688 | -1.12% | n/a | 11689/0 |
| Institutional Transactions | -0.1071 | +0.0630 | -0.1606 | -2.21% | 0.18% | 3099/1917 |
| d_Performance (Week) | +0.1051 | +0.1922 | +0.0490 | -0.64% | -1.42% | 4211/7361 |
| true_ret | -0.0994 | +0.1098 | -0.1022 | -0.97% | -1.57% | 7707/3453 |
| d_200-Day Simple Moving Average | -0.0956 | +0.1161 | -0.0913 | -1.00% | -1.44% | 7987/3569 |
| Performance (Month) | +0.0899 | -0.3113 | +0.2227 | -1.14% | -1.13% | 5375/6199 |
| Relative Volume | -0.0878 | +0.0833 | -0.1249 | -1.14% | n/a | 11459/0 |
| d_20-Day Simple Moving Average | -0.0839 | +0.1707 | -0.1124 | -0.98% | -1.42% | 7389/4197 |
| d_Performance (Quarter) | -0.0763 | +0.0667 | -0.1007 | -1.02% | -1.31% | 6409/4811 |
| d_Beta | -0.0592 | +0.1700 | -0.1285 | -0.30% | -1.96% | 1995/1542 |
| d_Performance (YTD) | -0.0563 | +0.0816 | -0.0302 | -0.97% | -1.53% | 7783/3522 |
| Performance (Week) | +0.0535 | -0.0729 | +0.0825 | -1.64% | -0.85% | 4126/7445 |
| d_Institutional Ownership | +0.0463 | -0.0690 | +0.0128 | -1.77% | -1.75% | 2071/2025 |
| d_EPS Surprise | -0.0438 | -0.0534 | -0.0476 | -4.26% | -1.95% | 77/66 |
| d_Short Ratio | -0.0406 | +0.0505 | -0.0828 | -0.91% | -1.34% | 4804/6301 |
| d_Short Float | -0.0331 | +0.0002 | -0.0552 | -0.61% | -1.60% | 2332/3124 |
| d_Average Volume | -0.0294 | +0.0607 | -0.0347 | -0.95% | -1.35% | 5855/5176 |
| d_Market Cap | +0.0290 | +0.0231 | -0.0001 | -0.71% | -1.84% | 3320/2382 |
| d_Relative Strength Index (14) | +0.0228 | +0.0525 | +0.1289 | -0.98% | -1.51% | 7798/3554 |
| d_Insider Transactions | -0.0228 | -0.0045 | -0.0389 | -2.96% | -1.94% | 103/159 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1260 | -0.44% | 12.3% |
| true_ret>3% & UPTREND | 201 | -1.82% | 17.4% |
| true_ret>3% & MIXED | 294 | -1.18% | 23.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 257 | -2.47% | -4.27% |
| WASHED | 1248 | -0.23% | 8.84% |
