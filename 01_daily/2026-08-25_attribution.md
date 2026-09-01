# Factor attribution — signal 2026-08-25 → prediction day 2026-08-31

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-25** | Features/scores formed from this snapshot (and deltas vs **2026-08-24**). Only data on/before this date. |
| **Prediction day** | **2026-08-31** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-25 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-31 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11576** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0661**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.51% | 21.4% | 2325 |
| 2 | -0.52% | 11.1% | 2721 |
| 3 | -0.74% | 9.0% | 1949 |
| 4 | -0.26% | 7.2% | 2285 |
| 5 | 4.40% | 20.8% | 2296 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Forward P/E | -0.1827 | -0.1270 | -0.1983 | -1.86% | -0.33% | 1471/1465 |
| Short Float | -0.1805 | +0.2684 | -0.2438 | 1.96% | n/a | 5682/0 |
| d_Market Cap | -0.1729 | -0.0630 | -0.1575 | 1.37% | 2.50% | 3274/2433 |
| d_Performance (Week) | -0.1687 | -0.0145 | -0.2340 | 0.65% | 1.55% | 8179/3203 |
| d_50-Day Simple Moving Average | -0.1678 | -0.0273 | -0.2063 | 1.10% | 0.49% | 7515/3960 |
| true_ret | -0.1672 | -0.0576 | -0.1960 | -0.14% | 0.55% | 7519/3553 |
| d_20-Day Simple Moving Average | -0.1671 | -0.0705 | -0.1738 | 0.78% | 1.10% | 7240/4188 |
| d_200-Day Simple Moving Average | -0.1644 | -0.0365 | -0.1963 | 1.09% | 0.52% | 7594/3853 |
| d_Performance (YTD) | -0.1639 | -0.0723 | -0.1754 | 0.57% | 1.68% | 7600/3618 |
| upside_pct_lvl | -0.1594 | +0.2428 | -0.3422 | 1.68% | -1.01% | 4291/353 |
| Performance (Week) | -0.1317 | -0.0734 | -0.1283 | 0.50% | 1.50% | 6634/4760 |
| d_Price | -0.1270 | -0.1490 | -0.0698 | -0.14% | 0.55% | 7519/3553 |
| d_Relative Strength Index (14) | -0.0853 | -0.2121 | +0.1143 | 0.59% | 1.69% | 7553/3599 |
| Relative Volume | -0.0839 | +0.1057 | -0.0594 | 0.90% | n/a | 11338/0 |
| Institutional Transactions | -0.0686 | +0.0599 | -0.1071 | 3.57% | 1.76% | 3173/1878 |
| d_Average Volume | -0.0389 | -0.0053 | -0.0203 | 1.53% | 0.41% | 5286/5756 |
| d_Institutional Ownership | +0.0289 | -0.0063 | +0.0591 | -3.37% | -6.15% | 18/49 |
| Relative Strength Index (14) | +0.0272 | -0.2468 | +0.1047 | 0.90% | n/a | 11453/0 |
| d_Volatility (Month) | +0.0242 | -0.0026 | +0.0191 | 1.78% | 0.87% | 3573/5911 |
| d_Short Ratio | +0.0204 | -0.0085 | +0.0086 | 0.10% | -0.30% | 3497/3210 |
| d_Insider Transactions | +0.0154 | +0.0449 | +0.0130 | -0.12% | -2.15% | 194/219 |
| d_EPS Surprise | -0.0127 | -0.0065 | -0.0200 | -3.22% | -3.77% | 19/11 |
| Performance (Month) | -0.0103 | +0.1296 | -0.1010 | 0.14% | 2.73% | 7960/3371 |
| d_Gross Margin | -0.0099 | -0.0325 | +0.0078 | -2.27% | -2.40% | 11/7 |
| d_Sales Year Over Year TTM | -0.0090 | -0.0467 | -0.0316 | -3.12% | 2.06% | 12/4 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 491 | 5.41% | 19.1% |
| true_ret>3% & UPTREND | 386 | -4.03% | 20.5% |
| true_ret>3% & MIXED | 346 | 5.03% | 21.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 503 | 3.60% | 24.46% |
| WASHED | 439 | 22.06% | 64.20% |
