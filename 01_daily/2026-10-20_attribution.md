# Factor attribution — signal 2026-10-20 → prediction day 2026-10-23

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-20** | Features/scores formed from this snapshot (and deltas vs **2026-10-19**). Only data on/before this date. |
| **Prediction day** | **2026-10-23** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-20 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-23 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11744** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.2546**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -2.62% | 12.1% | 2422 |
| 2 | 2.31% | 14.3% | 2362 |
| 3 | -0.16% | 11.6% | 2718 |
| 4 | -0.36% | 18.4% | 1919 |
| 5 | 0.57% | 36.8% | 2323 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.3646 | +0.0618 | +0.4245 | 0.40% | -0.39% | 4814/6713 |
| Performance (Month) | +0.3337 | -0.0964 | +0.5042 | 0.32% | -0.22% | 3363/8197 |
| Relative Strength Index (14) | +0.3260 | -0.0572 | +0.4183 | -0.06% | n/a | 11664/0 |
| upside_pct_lvl | -0.3005 | +0.1596 | -0.4010 | -0.57% | 0.80% | 4324/311 |
| d_Performance (Month) | +0.2834 | +0.1860 | +0.1524 | 0.15% | -0.26% | 5450/5962 |
| d_Beta | +0.2353 | -0.0695 | +0.2877 | 0.30% | 2.86% | 1326/1854 |
| d_Forward P/E | +0.2037 | +0.0787 | +0.2150 | 0.63% | -0.69% | 2211/739 |
| d_Price | +0.1928 | +0.1057 | +0.2320 | -0.29% | -0.65% | 7882/3144 |
| d_Market Cap | +0.1890 | +0.0104 | +0.1821 | 0.09% | 3.11% | 3934/1835 |
| d_Relative Strength Index (14) | +0.1757 | +0.0181 | +0.2564 | -0.33% | 0.72% | 7974/3266 |
| d_Performance (YTD) | +0.1581 | +0.1779 | +0.1356 | -0.29% | 0.76% | 7976/3237 |
| d_200-Day Simple Moving Average | +0.1377 | +0.2031 | +0.0801 | -0.35% | 0.70% | 8217/3329 |
| true_ret | +0.1343 | +0.2156 | +0.0860 | -0.29% | -0.65% | 7882/3144 |
| d_50-Day Simple Moving Average | +0.1076 | +0.2341 | +0.0194 | -0.43% | 1.04% | 8579/2972 |
| d_Performance (Quarter) | +0.0519 | +0.1762 | -0.0322 | -0.07% | 0.11% | 8104/3015 |
| Relative Volume | +0.0481 | +0.0573 | -0.0277 | -0.06% | n/a | 11411/0 |
| d_Performance (Week) | -0.0322 | +0.1838 | -0.1254 | -0.16% | 0.24% | 8068/3385 |
| d_Short Float | +0.0283 | +0.0289 | +0.0458 | 110.50% | -4.45% | 38/54 |
| d_Relative Volume | +0.0219 | +0.0019 | -0.0114 | 0.09% | -0.13% | 5673/5610 |
| d_Gross Margin | -0.0213 | +0.0094 | +0.0026 | -4.67% | 0.84% | 2/7 |
| d_Total Debt/Equity | -0.0208 | -0.0167 | -0.0210 | 0.70% | 2.43% | 10/15 |
| d_Average Volume | +0.0187 | -0.0520 | +0.0101 | 0.88% | -0.88% | 5355/5676 |
| Institutional Transactions | -0.0182 | +0.0812 | -0.0952 | 2.02% | -0.41% | 3260/1788 |
| d_Sales Growth Quarter Over Quarter | -0.0179 | -0.0074 | +0.0054 | 0.80% | 260.15% | 16/15 |
| d_Short Ratio | -0.0177 | +0.0636 | -0.0316 | -0.84% | -0.64% | 3728/3248 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 724 | 0.29% | 27.8% |
| true_ret>3% & UPTREND | 322 | 0.76% | 45.0% |
| true_ret>3% & MIXED | 222 | -1.71% | 30.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 160 | -1.72% | -3.08% |
| WASHED | 1551 | 0.52% | 0.14% |
