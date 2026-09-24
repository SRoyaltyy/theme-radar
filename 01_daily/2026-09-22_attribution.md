# Factor attribution — signal 2026-09-22 → prediction day 2026-09-24

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-22** | Features/scores formed from this snapshot (and deltas vs **2026-09-21**). Only data on/before this date. |
| **Prediction day** | **2026-09-24** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-22 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-24 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11635** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1167**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.83% | 13.7% | 2342 |
| 2 | -1.44% | 5.5% | 2342 |
| 3 | -1.24% | 5.6% | 2445 |
| 4 | -1.45% | 6.1% | 2279 |
| 5 | -2.80% | 12.3% | 2227 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.2876 | +0.0251 | -0.3194 | -1.91% | -0.61% | 8315/3093 |
| upside_pct_lvl | -0.2646 | +0.2487 | -0.4063 | -2.35% | -0.78% | 4336/298 |
| d_20-Day Simple Moving Average | -0.2123 | +0.0221 | -0.2518 | -1.93% | -0.94% | 7012/4452 |
| d_50-Day Simple Moving Average | -0.1982 | +0.0277 | -0.2344 | -1.98% | -0.94% | 6721/4748 |
| d_200-Day Simple Moving Average | -0.1888 | +0.0280 | -0.2170 | -1.95% | -1.01% | 6617/4819 |
| true_ret | -0.1732 | +0.0105 | -0.1942 | -1.92% | -1.07% | 6462/4416 |
| Short Float | -0.1730 | +0.1046 | -0.2213 | -1.80% | n/a | 5693/0 |
| d_Performance (YTD) | -0.1724 | +0.0102 | -0.1848 | -1.92% | -1.06% | 6581/4529 |
| d_Performance (Quarter) | -0.1721 | +0.0648 | -0.1515 | -1.84% | -1.07% | 6706/4243 |
| d_Relative Strength Index (14) | -0.1586 | +0.0448 | -0.1368 | -1.91% | -1.05% | 6602/4545 |
| d_Price | -0.1535 | +0.0175 | -0.1429 | -1.92% | -1.07% | 6462/4416 |
| Performance (Month) | +0.1511 | -0.0858 | +0.2356 | -1.04% | -1.82% | 4061/7409 |
| d_Beta | +0.1312 | -0.0134 | +0.1475 | -0.58% | -2.17% | 1658/3470 |
| Performance (Week) | -0.1296 | +0.0220 | -0.1085 | -1.78% | -1.16% | 7128/4312 |
| Relative Strength Index (14) | +0.1143 | -0.0956 | +0.1166 | -1.54% | n/a | 11551/0 |
| d_Market Cap | -0.1096 | +0.0585 | -0.1097 | -2.28% | -1.17% | 3111/2563 |
| d_Forward P/E | -0.1026 | +0.0562 | -0.1102 | -1.93% | -1.25% | 1553/1389 |
| d_Volatility (Month) | +0.0789 | +0.0256 | +0.1105 | -1.23% | -2.02% | 4493/4924 |
| Relative Volume | -0.0785 | +0.0325 | -0.1035 | -1.56% | n/a | 11410/0 |
| d_Target Price | +0.0602 | +0.0123 | +0.0116 | -0.50% | -3.37% | 126/157 |
| Institutional Transactions | -0.0507 | +0.0808 | -0.0824 | -1.75% | -2.14% | 3222/1809 |
| d_Performance (Month) | -0.0315 | -0.0078 | -0.0202 | -1.88% | -1.35% | 4407/6942 |
| d_Average Volume | +0.0220 | -0.0621 | +0.0907 | -1.74% | -1.46% | 3816/7400 |
| d_Short Ratio | -0.0211 | -0.0750 | -0.0138 | -1.61% | -1.87% | 4558/2469 |
| d_EPS Surprise | +0.0208 | +0.0196 | +0.0072 | -0.48% | -4.68% | 3/6 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 410 | -1.91% | 17.6% |
| true_ret>3% & UPTREND | 433 | -3.11% | 16.2% |
| true_ret>3% & MIXED | 305 | -3.78% | 17.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 281 | -1.51% | -4.72% |
| WASHED | 1090 | -1.88% | -1.86% |
