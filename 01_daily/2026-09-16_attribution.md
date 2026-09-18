# Factor attribution — signal 2026-09-16 → prediction day 2026-09-18

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-16** | Features/scores formed from this snapshot (and deltas vs **2026-09-15**). Only data on/before this date. |
| **Prediction day** | **2026-09-18** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-16 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-18 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11626** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0629**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.58% | 30.0% | 2932 |
| 2 | 0.88% | 18.5% | 2856 |
| 3 | 1.27% | 25.0% | 1218 |
| 4 | 1.84% | 24.4% | 2401 |
| 5 | 3.97% | 35.3% | 2219 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.2758 | -0.4528 | +0.0137 | 0.32% | 2.34% | 2443/9005 |
| d_Performance (Quarter) | +0.1904 | +0.2184 | -0.0017 | 3.46% | 0.49% | 4852/6043 |
| upside_pct_lvl | +0.1672 | +0.4392 | -0.3194 | 1.22% | 0.38% | 4378/262 |
| d_Performance (Month) | -0.1437 | -0.1223 | -0.1524 | 2.17% | 1.68% | 5493/5792 |
| d_Price | +0.1043 | +0.0976 | -0.0795 | 2.41% | 1.00% | 3605/7357 |
| d_Relative Strength Index (14) | +0.0931 | +0.1373 | -0.1167 | 3.75% | 1.01% | 3700/7451 |
| d_Performance (YTD) | +0.0880 | +0.0216 | +0.0078 | 3.83% | 1.00% | 3681/7452 |
| d_200-Day Simple Moving Average | +0.0836 | +0.0229 | +0.0042 | 3.65% | 1.00% | 3903/7579 |
| Performance (Month) | -0.0826 | -0.2344 | +0.1058 | 2.73% | 1.64% | 2682/8751 |
| d_Market Cap | +0.0770 | +0.1260 | -0.0378 | 4.77% | 0.84% | 2114/3546 |
| true_ret | +0.0756 | -0.0084 | +0.0613 | 2.41% | 1.00% | 3605/7357 |
| d_20-Day Simple Moving Average | +0.0725 | +0.0072 | +0.0345 | 3.20% | 1.03% | 4627/6873 |
| d_50-Day Simple Moving Average | +0.0702 | +0.0053 | +0.0156 | 3.41% | 1.04% | 4179/7317 |
| d_Forward P/E | +0.0659 | +0.1088 | -0.0063 | 0.44% | -0.10% | 1047/1883 |
| Institutional Transactions | +0.0568 | +0.1184 | -0.0237 | 2.44% | 2.75% | 3210/1829 |
| Relative Volume | -0.0542 | +0.0061 | -0.0207 | 1.92% | n/a | 11383/0 |
| d_Profit Margin | +0.0515 | +0.0381 | +0.0419 | 7.90% | -3.62% | 6/4 |
| d_Performance (Week) | +0.0508 | +0.1237 | -0.0713 | 1.67% | 2.32% | 7116/4251 |
| d_Beta | +0.0499 | +0.1475 | -0.0614 | 5.42% | 0.75% | 2346/1207 |
| d_Average Volume | -0.0483 | -0.1316 | +0.0425 | 2.28% | 1.26% | 4952/6088 |
| Relative Strength Index (14) | +0.0408 | +0.2233 | -0.1170 | 1.89% | n/a | 11539/0 |
| d_Short Ratio | +0.0400 | +0.0977 | -0.0505 | 1.24% | 1.29% | 4080/3272 |
| d_Relative Volume | +0.0343 | +0.0646 | -0.0233 | 2.60% | 1.13% | 5868/5340 |
| Short Float | -0.0298 | +0.1924 | -0.2220 | 1.80% | n/a | 5704/0 |
| d_Target Price | +0.0278 | -0.0154 | +0.0388 | 0.81% | 0.48% | 142/150 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 299 | 13.26% | 55.5% |
| true_ret>3% & UPTREND | 160 | 4.92% | 57.5% |
| true_ret>3% & MIXED | 126 | 1.48% | 47.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 121 | 6.11% | 11.06% |
| WASHED | 2001 | 4.10% | 8.87% |
