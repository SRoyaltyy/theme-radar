# Factor attribution — signal 2026-09-11 → prediction day 2026-09-16

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-11** | Features/scores formed from this snapshot (and deltas vs **2026-09-10**). Only data on/before this date. |
| **Prediction day** | **2026-09-16** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-11 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-16 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11598** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.1072**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.71% | 13.3% | 2328 |
| 2 | -1.35% | 6.3% | 2312 |
| 3 | -1.15% | 8.1% | 2566 |
| 4 | 1.26% | 8.3% | 2110 |
| 5 | -1.20% | 16.3% | 2282 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | +0.2380 | +0.0084 | +0.2716 | 0.82% | -1.10% | 2945/7951 |
| upside_pct_lvl | -0.2358 | +0.2608 | -0.3996 | 0.55% | -1.23% | 4378/269 |
| d_50-Day Simple Moving Average | -0.1840 | -0.0137 | -0.1744 | -1.46% | 0.86% | 7739/3752 |
| d_20-Day Simple Moving Average | -0.1795 | +0.0215 | -0.1810 | -1.42% | 0.99% | 8099/3416 |
| true_ret | -0.1658 | -0.0372 | -0.1466 | -1.41% | 0.65% | 7417/3656 |
| d_200-Day Simple Moving Average | -0.1631 | -0.0048 | -0.1411 | -1.41% | 0.28% | 7653/3844 |
| d_Performance (YTD) | -0.1560 | -0.0255 | -0.1164 | -1.40% | 0.30% | 7496/3730 |
| d_Price | -0.1410 | -0.0419 | -0.0449 | -1.41% | 0.65% | 7417/3656 |
| Performance (Month) | +0.1176 | -0.1308 | +0.1823 | -0.57% | -0.27% | 3544/7867 |
| d_Forward P/E | -0.0936 | +0.0262 | -0.1380 | -1.72% | -1.09% | 1846/1081 |
| Short Float | -0.0757 | +0.1462 | -0.1870 | 0.88% | n/a | 5695/0 |
| d_Relative Strength Index (14) | -0.0751 | -0.0550 | +0.1342 | -1.41% | 0.76% | 7493/3742 |
| d_Average Volume | +0.0549 | -0.0421 | +0.0936 | 0.65% | -1.12% | 4885/6131 |
| d_Beta | -0.0490 | +0.0578 | -0.0485 | 0.23% | 3.71% | 2323/1243 |
| Performance (Week) | +0.0407 | -0.1981 | +0.1195 | 0.23% | -0.58% | 2828/8609 |
| d_Short Float | +0.0405 | -0.0558 | +0.0720 | -1.66% | 3.44% | 139/347 |
| d_Short Ratio | -0.0385 | +0.0005 | -0.0600 | -0.68% | 1.66% | 4030/3171 |
| Institutional Transactions | -0.0328 | +0.0863 | -0.0462 | 1.68% | 0.20% | 3200/1831 |
| d_Total Debt/Equity | -0.0284 | -0.0182 | -0.0155 | -3.81% | 2.02% | 10/11 |
| d_Institutional Ownership | +0.0258 | -0.0445 | +0.0404 | -1.69% | -2.57% | 226/161 |
| Relative Strength Index (14) | -0.0245 | -0.0854 | -0.0932 | -0.38% | n/a | 11519/0 |
| d_Target Price | +0.0211 | +0.0123 | +0.0057 | -0.37% | -1.73% | 164/162 |
| d_Volatility (Month) | -0.0161 | -0.0582 | +0.0165 | 0.17% | -0.61% | 4834/4512 |
| d_Performance (Month) | -0.0119 | +0.0303 | -0.0085 | -0.69% | -0.69% | 6273/5003 |
| Relative Volume | +0.0112 | +0.0142 | -0.0248 | -0.71% | n/a | 11316/0 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 350 | 3.96% | 17.1% |
| true_ret>3% & UPTREND | 307 | -3.48% | 16.0% |
| true_ret>3% & MIXED | 206 | -5.36% | 11.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 165 | -2.77% | -0.72% |
| WASHED | 1475 | 4.96% | 11.41% |
