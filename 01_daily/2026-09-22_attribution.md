# Factor attribution — signal 2026-09-22 → prediction day 2026-09-25

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-22** | Features/scores formed from this snapshot (and deltas vs **2026-09-21**). Only data on/before this date. |
| **Prediction day** | **2026-09-25** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-22 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-25 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11635** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0566**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -1.00% | 12.0% | 2342 |
| 2 | -1.10% | 6.4% | 2342 |
| 3 | -0.91% | 6.0% | 2445 |
| 4 | -1.11% | 6.6% | 2279 |
| 5 | -2.62% | 15.5% | 2227 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2759 | +0.2578 | -0.4316 | -2.38% | -1.13% | 4336/298 |
| d_Performance (Week) | -0.2267 | +0.1312 | -0.2787 | -1.64% | -0.57% | 8315/3093 |
| d_20-Day Simple Moving Average | -0.1665 | +0.0811 | -0.2052 | -1.69% | -0.80% | 7012/4452 |
| Short Float | -0.1626 | +0.1335 | -0.2184 | -1.60% | n/a | 5693/0 |
| Performance (Month) | +0.1565 | -0.1065 | +0.2529 | -0.93% | -1.56% | 4061/7409 |
| d_50-Day Simple Moving Average | -0.1473 | +0.0857 | -0.1819 | -1.72% | -0.80% | 6721/4748 |
| d_200-Day Simple Moving Average | -0.1415 | +0.0866 | -0.1669 | -1.69% | -1.07% | 6617/4819 |
| Relative Strength Index (14) | +0.1398 | -0.1491 | +0.1391 | -1.34% | n/a | 11551/0 |
| d_Beta | +0.1282 | -0.0171 | +0.1411 | -0.52% | -2.12% | 1658/3470 |
| true_ret | -0.1223 | +0.0603 | -0.1387 | -1.63% | -0.97% | 6462/4416 |
| d_Performance (YTD) | -0.1193 | +0.0544 | -0.1231 | -1.66% | -1.14% | 6581/4529 |
| d_Relative Strength Index (14) | -0.1098 | +0.0777 | -0.0819 | -1.65% | -0.92% | 6602/4545 |
| d_Price | -0.0892 | +0.0491 | -0.0686 | -1.63% | -0.97% | 6462/4416 |
| d_Performance (Quarter) | -0.0825 | +0.0846 | -0.0528 | -1.42% | -1.21% | 6706/4243 |
| d_Market Cap | -0.0732 | +0.1168 | -0.0893 | -2.07% | -1.04% | 3111/2563 |
| d_Volatility (Month) | +0.0715 | -0.0059 | +0.1255 | -1.03% | -1.79% | 4493/4924 |
| Institutional Transactions | -0.0703 | +0.0670 | -0.1082 | -1.46% | -2.11% | 3222/1809 |
| Relative Volume | -0.0698 | +0.0807 | -0.0782 | -1.36% | n/a | 11410/0 |
| Performance (Week) | -0.0647 | +0.1088 | -0.0478 | -1.51% | -1.05% | 7128/4312 |
| d_Forward P/E | -0.0488 | +0.1478 | -0.0800 | -1.55% | -1.26% | 1553/1389 |
| d_Target Price | +0.0443 | +0.0403 | +0.0226 | 0.02% | -3.08% | 126/157 |
| d_EPS Surprise | +0.0288 | +0.0401 | +0.0181 | 1.09% | -5.42% | 3/6 |
| d_Insider Transactions | +0.0226 | +0.0414 | +0.0153 | -0.76% | -2.38% | 97/251 |
| d_Sales Growth Quarter Over Quarter | +0.0217 | +0.0262 | -0.0010 | -4.24% | -6.94% | 4/5 |
| d_Average Volume | +0.0199 | -0.0849 | +0.0967 | -1.67% | -1.18% | 3816/7400 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 410 | -0.89% | 20.2% |
| true_ret>3% & UPTREND | 433 | -2.83% | 17.8% |
| true_ret>3% & MIXED | 305 | -3.88% | 19.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 281 | -1.51% | -3.63% |
| WASHED | 1090 | -0.90% | -0.57% |
