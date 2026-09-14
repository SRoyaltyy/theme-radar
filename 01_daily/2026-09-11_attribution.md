# Factor attribution — signal 2026-09-11 → prediction day 2026-09-14

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-11** | Features/scores formed from this snapshot (and deltas vs **2026-09-10**). Only data on/before this date. |
| **Prediction day** | **2026-09-14** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-11 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-14 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11598** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0419**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.03% | 14.0% | 2328 |
| 2 | -0.29% | 9.0% | 2312 |
| 3 | -0.38% | 10.6% | 2566 |
| 4 | 2.89% | 12.5% | 2110 |
| 5 | 0.25% | 25.4% | 2282 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.2134 | -0.3120 | -0.0468 | 0.52% | 0.97% | 2828/8609 |
| d_20-Day Simple Moving Average | -0.1858 | +0.0409 | -0.2571 | -0.45% | 2.72% | 8099/3416 |
| d_50-Day Simple Moving Average | -0.1856 | +0.0391 | -0.2477 | -0.44% | 2.43% | 7739/3752 |
| d_Performance (Quarter) | +0.1779 | -0.0149 | +0.3130 | 1.27% | 0.43% | 2945/7951 |
| d_Performance (YTD) | -0.1764 | +0.0131 | -0.1970 | -0.42% | 1.80% | 7496/3730 |
| true_ret | -0.1664 | +0.0292 | -0.2147 | -0.43% | 2.21% | 7417/3656 |
| d_Price | -0.1637 | -0.0305 | -0.1090 | -0.43% | 2.21% | 7417/3656 |
| d_200-Day Simple Moving Average | -0.1609 | +0.0511 | -0.2070 | -0.42% | 1.74% | 7653/3844 |
| d_Relative Strength Index (14) | -0.1476 | -0.1011 | +0.1277 | -0.42% | 2.38% | 7493/3742 |
| d_Forward P/E | -0.1406 | +0.0859 | -0.2808 | -0.48% | 0.30% | 1846/1081 |
| d_Performance (Week) | -0.1135 | -0.0861 | -0.0906 | -0.60% | 1.36% | 4974/6399 |
| Performance (Month) | +0.1090 | -0.0344 | +0.2144 | 1.02% | 0.81% | 3544/7867 |
| upside_pct_lvl | -0.1051 | +0.2775 | -0.3141 | 2.47% | -0.22% | 4378/269 |
| Short Float | +0.0779 | +0.1534 | -0.1706 | 2.41% | n/a | 5695/0 |
| d_Performance (Month) | +0.0588 | +0.1046 | +0.0461 | 0.48% | 0.58% | 6273/5003 |
| d_Average Volume | +0.0567 | -0.0122 | +0.1480 | 2.22% | -0.14% | 4885/6131 |
| Relative Volume | +0.0551 | +0.0345 | +0.0177 | 0.51% | n/a | 11316/0 |
| d_Market Cap | -0.0551 | +0.0289 | -0.0928 | 1.45% | 3.59% | 3202/2495 |
| Relative Strength Index (14) | -0.0496 | +0.0184 | -0.1262 | 0.86% | n/a | 11519/0 |
| d_Beta | -0.0449 | +0.0450 | -0.0723 | 2.25% | 5.30% | 2323/1243 |
| d_Short Ratio | -0.0376 | -0.0194 | -0.1051 | 0.28% | 3.67% | 4030/3171 |
| Institutional Transactions | -0.0361 | -0.0039 | -0.0485 | 3.19% | 2.04% | 3200/1831 |
| d_Analyst Recom | +0.0275 | +0.0376 | +0.0150 | 0.57% | -0.69% | 72/97 |
| d_Sales Growth Quarter Over Quarter | +0.0204 | +0.0011 | +0.0113 | 1.49% | -1.13% | 13/14 |
| d_Short Float | +0.0176 | -0.0684 | +0.0512 | 0.98% | 9.59% | 139/347 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 350 | 1.93% | 20.6% |
| true_ret>3% & UPTREND | 307 | -3.15% | 21.2% |
| true_ret>3% & MIXED | 206 | -1.47% | 29.1% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 165 | 0.51% | 4.86% |
| WASHED | 1475 | 6.66% | 13.72% |
