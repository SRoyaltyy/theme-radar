# Factor attribution — signal 2026-10-20 → prediction day 2026-10-21

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-20** | Features/scores formed from this snapshot (and deltas vs **2026-10-19**). Only data on/before this date. |
| **Prediction day** | **2026-10-21** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-20 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-21 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11744** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.2056**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.23% | 31.2% | 2422 |
| 2 | 0.55% | 21.5% | 2362 |
| 3 | 0.15% | 8.9% | 2718 |
| 4 | 0.41% | 12.5% | 1919 |
| 5 | -0.14% | 18.1% | 2323 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.2834 | -0.4713 | +0.1192 | -0.18% | 0.89% | 4814/6713 |
| d_Performance (Month) | -0.2586 | -0.2242 | -0.0758 | 0.04% | 0.81% | 5450/5962 |
| Performance (Month) | -0.1708 | -0.4587 | +0.2451 | -0.07% | 0.64% | 3363/8197 |
| Relative Strength Index (14) | -0.1535 | -0.3775 | +0.2338 | 0.44% | n/a | 11664/0 |
| d_Beta | -0.1507 | -0.3130 | +0.1462 | -0.31% | 1.13% | 1326/1854 |
| d_Relative Strength Index (14) | -0.0890 | -0.1490 | +0.1268 | 0.33% | 0.74% | 7974/3266 |
| d_Average Volume | -0.0717 | -0.0752 | -0.0273 | 0.25% | 0.61% | 5355/5676 |
| d_50-Day Simple Moving Average | -0.0712 | +0.0828 | -0.1166 | 0.39% | 0.58% | 8579/2972 |
| d_200-Day Simple Moving Average | -0.0682 | +0.0426 | -0.0591 | 0.39% | 0.56% | 8217/3329 |
| true_ret | -0.0655 | +0.0415 | -0.0799 | 0.34% | 0.62% | 7882/3144 |
| d_Volatility (Month) | -0.0641 | -0.0348 | -0.0843 | 0.41% | 0.56% | 4950/4392 |
| d_Performance (YTD) | -0.0598 | +0.0065 | -0.0032 | 0.33% | 0.76% | 7976/3237 |
| Institutional Transactions | +0.0506 | +0.1126 | -0.0383 | 0.31% | 0.22% | 3260/1788 |
| d_Short Ratio | +0.0456 | +0.0493 | +0.0252 | 0.45% | 0.26% | 3728/3248 |
| d_Price | -0.0400 | -0.0778 | +0.1125 | 0.34% | 0.62% | 7882/3144 |
| d_Forward P/E | -0.0353 | -0.0296 | +0.0505 | 0.10% | 0.39% | 2211/739 |
| d_Target Price | +0.0324 | +0.0110 | -0.0228 | 0.12% | -0.13% | 219/309 |
| d_Market Cap | -0.0310 | -0.1185 | +0.1743 | 0.28% | 0.28% | 3934/1835 |
| d_Total Debt/Equity | -0.0288 | +0.0061 | +0.0163 | -0.59% | 0.83% | 10/15 |
| Relative Volume | -0.0261 | -0.0040 | +0.0115 | 0.44% | n/a | 11411/0 |
| d_Insider Transactions | -0.0257 | +0.0048 | +0.0294 | 1.29% | 0.71% | 63/110 |
| d_Institutional Ownership | +0.0236 | +0.0259 | +0.0347 | n/a | -2.58% | 0/5 |
| d_Performance (Quarter) | -0.0192 | +0.1449 | -0.1046 | 0.44% | 0.39% | 8104/3015 |
| Short Float | -0.0146 | +0.1747 | -0.1549 | 0.24% | n/a | 5662/0 |
| d_Relative Volume | -0.0143 | -0.0203 | +0.0144 | 0.42% | 0.48% | 5673/5610 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 722 | 1.17% | 34.2% |
| true_ret>3% & UPTREND | 322 | 0.45% | 30.1% |
| true_ret>3% & MIXED | 222 | 0.22% | 35.1% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 160 | -1.61% | -3.02% |
| WASHED | 1551 | 1.44% | 0.09% |
