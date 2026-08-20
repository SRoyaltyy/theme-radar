# Factor attribution — signal 2026-08-17 → prediction day 2026-08-20

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-17** | Features/scores formed from this snapshot (and deltas vs **2026-08-14**). Only data on/before this date. |
| **Prediction day** | **2026-08-20** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-17 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-20 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11558** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.1034**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 11.43% | 30.3% | 2389 |
| 2 | -0.01% | 13.9% | 2569 |
| 3 | 0.22% | 12.3% | 2742 |
| 4 | -1.31% | 17.8% | 1710 |
| 5 | -1.08% | 29.3% | 2148 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.1934 | -0.0377 | -0.2582 | -0.96% | 6.70% | 6854/4492 |
| d_Performance (Quarter) | -0.1495 | +0.1184 | -0.2661 | -0.39% | 9.40% | 7737/3072 |
| d_Performance (Month) | -0.1295 | +0.0626 | -0.1543 | -0.52% | 5.37% | 6254/5001 |
| Performance (Month) | -0.1274 | +0.0764 | -0.1950 | -0.80% | 7.21% | 7257/4072 |
| d_Performance (Week) | -0.1251 | -0.0579 | -0.1606 | -0.90% | 4.81% | 5397/5920 |
| d_Forward P/E | -0.1208 | -0.0140 | -0.1360 | -1.81% | -0.78% | 946/2035 |
| d_Volatility (Month) | +0.0812 | -0.1051 | +0.1692 | 0.80% | 3.29% | 2961/6551 |
| Relative Strength Index (14) | -0.0669 | -0.0310 | +0.1876 | 2.07% | n/a | 11437/0 |
| Institutional Transactions | -0.0654 | -0.0231 | -0.0723 | 2.43% | 9.21% | 2689/2351 |
| d_Beta | -0.0606 | -0.0072 | -0.0853 | 8.17% | 4.60% | 1930/1503 |
| d_Market Cap | -0.0449 | +0.0645 | -0.1309 | -0.72% | 8.06% | 2054/3681 |
| d_Relative Strength Index (14) | -0.0446 | +0.2060 | -0.2452 | -0.63% | 3.58% | 3808/7306 |
| d_Analyst Recom | +0.0327 | +0.0075 | +0.0203 | -0.84% | -1.31% | 170/167 |
| d_50-Day Simple Moving Average | -0.0286 | +0.0193 | -0.0629 | -0.73% | 3.50% | 3906/7509 |
| d_20-Day Simple Moving Average | +0.0285 | +0.0042 | +0.0328 | -0.36% | 3.12% | 3511/7914 |
| Short Float | -0.0284 | +0.2011 | -0.2451 | 4.93% | n/a | 5684/0 |
| d_Institutional Transactions | -0.0257 | -0.0450 | +0.0260 | 7.28% | 3.66% | 2830/2065 |
| d_Institutional Ownership | -0.0236 | -0.0454 | -0.0604 | 2.76% | 0.03% | 3510/2223 |
| d_Target Price | -0.0213 | -0.0346 | -0.0158 | -0.74% | 0.62% | 383/222 |
| d_Short Float | +0.0206 | -0.0720 | +0.0635 | -0.40% | 3.52% | 178/359 |
| d_Total Debt/Equity | -0.0202 | +0.0045 | -0.0062 | 19.21% | 53.28% | 115/79 |
| d_Short Ratio | +0.0194 | +0.0872 | -0.0177 | -0.25% | 0.78% | 4296/2460 |
| d_EPS Surprise | -0.0182 | +0.0035 | -0.0048 | -1.81% | 0.81% | 53/45 |
| d_Relative Volume | +0.0147 | +0.0100 | +0.0133 | 3.43% | 0.19% | 6607/4526 |
| true_ret | -0.0146 | +0.0051 | -0.0237 | -0.66% | 3.62% | 3757/7234 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 216 | -0.97% | 32.9% |
| true_ret>3% & UPTREND | 337 | -4.27% | 34.1% |
| true_ret>3% & MIXED | 194 | -1.42% | 36.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 309 | -5.54% | -13.77% |
| WASHED | 492 | 58.18% | -1.03% |
