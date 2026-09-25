# Factor attribution — signal 2026-09-24 → prediction day 2026-09-25

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-24** | Features/scores formed from this snapshot (and deltas vs **2026-09-23**). Only data on/before this date. |
| **Prediction day** | **2026-09-25** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-24 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-25 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11660** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0345**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.75% | 15.0% | 2788 |
| 2 | 0.17% | 8.7% | 2585 |
| 3 | 0.14% | 9.8% | 2396 |
| 4 | 0.06% | 10.2% | 1876 |
| 5 | -0.10% | 19.3% | 2015 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.1521 | -0.1070 | -0.1352 | -0.06% | 0.42% | 4108/6884 |
| upside_pct_lvl | -0.1146 | +0.2821 | -0.3496 | -0.04% | -0.32% | 4383/256 |
| d_Price | -0.1018 | -0.0624 | -0.1038 | 0.02% | 0.40% | 3916/7066 |
| d_Performance (Week) | -0.0951 | -0.2374 | +0.0960 | -0.14% | 0.36% | 2645/8843 |
| d_200-Day Simple Moving Average | -0.0814 | -0.1191 | -0.0410 | -0.04% | 0.40% | 3975/7531 |
| d_Performance (Month) | -0.0777 | -0.1804 | +0.0439 | -0.06% | 0.37% | 3256/8122 |
| d_Performance (YTD) | -0.0689 | -0.1196 | -0.0245 | -0.01% | 0.39% | 4013/7164 |
| d_Market Cap | -0.0641 | -0.0096 | -0.0439 | -0.03% | 0.47% | 2283/3405 |
| d_Forward P/E | -0.0588 | -0.0834 | +0.0168 | 0.17% | 0.24% | 1238/1690 |
| true_ret | -0.0560 | -0.1341 | +0.0034 | 0.02% | 0.40% | 3916/7066 |
| d_20-Day Simple Moving Average | -0.0556 | -0.0949 | -0.0254 | 0.01% | 0.41% | 4741/6740 |
| d_Institutional Ownership | -0.0555 | +0.0736 | -0.1219 | 0.26% | 0.23% | 435/1538 |
| d_Average Volume | -0.0546 | -0.0567 | -0.0537 | 0.29% | 0.19% | 5321/5763 |
| d_50-Day Simple Moving Average | -0.0533 | -0.1053 | -0.0175 | 0.01% | 0.37% | 4136/7379 |
| d_Relative Strength Index (14) | -0.0509 | +0.0243 | -0.1215 | 0.03% | 0.39% | 4046/7148 |
| Institutional Transactions | -0.0493 | +0.0053 | -0.0869 | 0.46% | 0.02% | 3222/1810 |
| Short Float | -0.0403 | +0.1318 | -0.1453 | 0.24% | n/a | 5693/0 |
| d_Sales Growth Quarter Over Quarter | +0.0341 | +0.0327 | +0.0646 | -0.38% | -5.68% | 3/7 |
| Performance (Week) | +0.0312 | -0.0314 | -0.0028 | 0.10% | 0.33% | 4473/7018 |
| d_Profit Margin | +0.0304 | -0.0005 | +0.0473 | 0.08% | -6.17% | 6/6 |
| d_EPS Surprise | +0.0284 | +0.0168 | +0.0036 | -0.55% | -3.11% | 3/6 |
| d_Target Price | -0.0254 | +0.0185 | -0.0561 | -0.20% | 0.55% | 101/193 |
| d_Short Float | -0.0211 | -0.0542 | -0.0017 | 0.49% | -0.08% | 3229/2283 |
| d_Total Debt/Equity | -0.0183 | +0.0065 | -0.0127 | -4.50% | -2.24% | 6/5 |
| d_Analyst Recom | -0.0172 | -0.0042 | +0.0046 | 0.41% | 0.32% | 60/103 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 199 | -1.34% | 23.1% |
| true_ret>3% & UPTREND | 264 | 0.31% | 31.1% |
| true_ret>3% & MIXED | 145 | 0.43% | 27.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 203 | -0.43% | 2.02% |
| WASHED | 2262 | 0.61% | -0.28% |
