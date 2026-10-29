# Factor attribution — signal 2026-10-26 → prediction day 2026-10-29

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-26** | Features/scores formed from this snapshot (and deltas vs **2026-10-23**). Only data on/before this date. |
| **Prediction day** | **2026-10-29** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-26 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-29 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11755** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0379**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.90% | 38.5% | 2423 |
| 2 | 3.71% | 36.1% | 2291 |
| 3 | 2.00% | 23.9% | 2425 |
| 4 | 4.91% | 27.6% | 2297 |
| 5 | 3.29% | 52.3% | 2319 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | -0.2518 | -0.4263 | +0.2100 | 0.51% | 5.23% | 4514/7047 |
| Relative Strength Index (14) | -0.2367 | -0.3908 | +0.2747 | 3.36% | n/a | 11663/0 |
| upside_pct_lvl | +0.2136 | +0.4188 | -0.3274 | 5.34% | 0.48% | 4290/340 |
| Short Float | +0.2101 | +0.3362 | -0.0780 | 5.69% | n/a | 5649/0 |
| d_Beta | +0.1946 | +0.2886 | -0.1503 | 11.69% | 0.49% | 2309/1837 |
| d_20-Day Simple Moving Average | +0.1830 | +0.1683 | +0.0886 | 3.53% | 3.15% | 7294/4291 |
| d_Performance (Quarter) | +0.1560 | +0.1251 | +0.0734 | 4.30% | 2.52% | 5884/5293 |
| d_50-Day Simple Moving Average | +0.1517 | +0.1224 | +0.1015 | 3.24% | 3.67% | 7633/3950 |
| d_Forward P/E | +0.1295 | +0.1000 | +0.0999 | 2.30% | 1.65% | 1607/1316 |
| d_200-Day Simple Moving Average | +0.1129 | +0.0586 | +0.1177 | 2.08% | 3.94% | 7225/4315 |
| d_Price | +0.1120 | -0.0146 | +0.1618 | 1.96% | 4.02% | 6975/4196 |
| true_ret | +0.1088 | +0.0484 | +0.1512 | 1.96% | 4.02% | 6975/4196 |
| d_Performance (YTD) | +0.1084 | +0.0358 | +0.1360 | 2.10% | 5.67% | 7054/4263 |
| Institutional Transactions | +0.0837 | +0.1308 | -0.0194 | 4.49% | 9.24% | 3235/1813 |
| Performance (Week) | -0.0742 | -0.1343 | +0.1296 | 1.26% | 5.86% | 6140/5375 |
| d_Target Price | -0.0705 | -0.0722 | -0.0020 | 0.94% | 2.99% | 327/319 |
| d_Relative Strength Index (14) | +0.0684 | -0.1391 | +0.1692 | 2.11% | 5.63% | 7031/4266 |
| d_Performance (Week) | +0.0658 | +0.0503 | +0.0680 | 2.00% | 5.86% | 7260/4227 |
| Relative Volume | +0.0537 | +0.0911 | -0.0076 | 3.43% | n/a | 11433/0 |
| d_Market Cap | +0.0420 | -0.0206 | +0.0930 | 3.19% | 7.78% | 2841/2940 |
| d_Volatility (Month) | +0.0336 | +0.1496 | -0.1577 | 2.96% | 4.63% | 5282/4879 |
| d_Total Debt/Equity | +0.0256 | -0.0103 | -0.0018 | 1.60% | -2.26% | 25/15 |
| d_EPS Surprise | +0.0215 | +0.0217 | +0.0465 | 6.00% | 1.02% | 29/37 |
| d_Sales Growth Quarter Over Quarter | +0.0126 | -0.0361 | -0.0122 | 1.76% | 1.28% | 24/18 |
| d_Profit Margin | -0.0125 | +0.0108 | +0.0292 | 0.06% | 1.27% | 24/22 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 503 | 8.87% | 68.4% |
| true_ret>3% & UPTREND | 153 | 2.61% | 54.2% |
| true_ret>3% & MIXED | 156 | 3.34% | 59.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 185 | -1.19% | 1.47% |
| WASHED | 1690 | 15.45% | 11.10% |
