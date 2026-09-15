# Factor attribution — signal 2026-09-11 → prediction day 2026-09-15

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-11** | Features/scores formed from this snapshot (and deltas vs **2026-09-10**). Only data on/before this date. |
| **Prediction day** | **2026-09-15** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-11 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-15 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11598** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0676**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.12% | 13.1% | 2328 |
| 2 | -1.20% | 6.9% | 2312 |
| 3 | -0.91% | 8.9% | 2566 |
| 4 | 1.99% | 10.1% | 2110 |
| 5 | -1.21% | 19.0% | 2282 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | +0.2837 | +0.0545 | +0.3033 | 0.69% | -0.61% | 2945/7951 |
| upside_pct_lvl | -0.2829 | +0.2054 | -0.3947 | 0.95% | -0.32% | 4378/269 |
| d_50-Day Simple Moving Average | -0.2316 | -0.0208 | -0.2360 | -1.39% | 1.61% | 7739/3752 |
| d_20-Day Simple Moving Average | -0.2176 | -0.0027 | -0.2353 | -1.33% | 1.75% | 8099/3416 |
| d_200-Day Simple Moving Average | -0.1989 | -0.0066 | -0.1875 | -1.33% | 0.96% | 7653/3844 |
| true_ret | -0.1954 | -0.0278 | -0.1909 | -1.32% | 1.32% | 7417/3656 |
| d_Performance (YTD) | -0.1871 | -0.0292 | -0.1606 | -1.31% | 0.96% | 7496/3730 |
| d_Price | -0.1644 | -0.0661 | -0.0759 | -1.32% | 1.32% | 7417/3656 |
| Performance (Month) | +0.1582 | -0.0213 | +0.2211 | 0.01% | -0.11% | 3544/7867 |
| d_Forward P/E | -0.1473 | +0.0392 | -0.2072 | -1.24% | -0.41% | 1846/1081 |
| d_Relative Strength Index (14) | -0.1170 | -0.0777 | +0.1245 | -1.31% | 1.44% | 7493/3742 |
| d_Beta | -0.0821 | +0.0330 | -0.0583 | 0.92% | 3.85% | 2323/1243 |
| d_Average Volume | +0.0516 | +0.0004 | +0.1075 | 1.02% | -0.89% | 4885/6131 |
| Institutional Transactions | -0.0388 | +0.0298 | -0.0732 | 1.77% | 1.01% | 3200/1831 |
| d_Institutional Ownership | +0.0340 | -0.0334 | +0.0374 | -0.82% | -1.96% | 226/161 |
| d_Target Price | +0.0319 | +0.0634 | +0.0199 | 0.70% | -0.84% | 164/162 |
| Short Float | -0.0315 | +0.1863 | -0.1515 | 1.21% | n/a | 5695/0 |
| d_Market Cap | -0.0309 | +0.0089 | -0.0220 | 0.32% | 2.30% | 3202/2495 |
| d_Short Ratio | -0.0302 | -0.0443 | -0.0675 | -0.56% | 2.23% | 4030/3171 |
| d_Analyst Recom | +0.0282 | +0.0022 | +0.0022 | -0.29% | -1.55% | 72/97 |
| d_Short Float | +0.0259 | -0.0522 | +0.0816 | -0.62% | 5.17% | 139/347 |
| d_Total Debt/Equity | -0.0242 | -0.0166 | +0.0005 | -2.90% | 0.56% | 10/11 |
| Relative Strength Index (14) | +0.0241 | -0.0347 | -0.0986 | -0.08% | n/a | 11519/0 |
| Relative Volume | +0.0225 | +0.0565 | -0.0140 | -0.41% | n/a | 11316/0 |
| d_Performance (Month) | +0.0214 | +0.0661 | +0.0307 | -0.36% | -0.44% | 6273/5003 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 350 | 0.01% | 15.4% |
| true_ret>3% & UPTREND | 307 | -4.30% | 14.3% |
| true_ret>3% & MIXED | 206 | -4.85% | 13.1% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 165 | -2.45% | -2.09% |
| WASHED | 1475 | 5.32% | 11.31% |
