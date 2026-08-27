# Factor attribution — signal 2026-08-25 → prediction day 2026-08-26

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-25** | Features/scores formed from this snapshot (and deltas vs **2026-08-24**). Only data on/before this date. |
| **Prediction day** | **2026-08-26** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-25 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-26 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11611** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0503**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.03% | 14.5% | 2336 |
| 2 | -0.25% | 6.1% | 2738 |
| 3 | -0.14% | 4.7% | 1953 |
| 4 | -0.19% | 4.6% | 2285 |
| 5 | -0.11% | 16.1% | 2299 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.3100 | -0.2165 | -0.2358 | -0.34% | 0.14% | 6640/4764 |
| Relative Strength Index (14) | -0.1932 | -0.3592 | +0.0415 | -0.15% | n/a | 11488/0 |
| d_200-Day Simple Moving Average | -0.1888 | -0.0097 | -0.1966 | -0.26% | 0.06% | 7599/3857 |
| Performance (Month) | -0.1884 | -0.1304 | -0.2035 | -0.27% | 0.12% | 7983/3381 |
| true_ret | -0.1844 | -0.0293 | -0.1949 | -0.25% | 0.07% | 7523/3557 |
| d_Performance (YTD) | -0.1741 | -0.0325 | -0.1588 | -0.25% | 0.08% | 7605/3622 |
| d_50-Day Simple Moving Average | -0.1653 | +0.0170 | -0.1945 | -0.23% | 0.01% | 7520/3964 |
| d_Price | -0.1505 | -0.0891 | +0.0041 | -0.25% | 0.07% | 7523/3557 |
| d_Relative Strength Index (14) | -0.1498 | -0.1515 | +0.1752 | -0.25% | 0.09% | 7557/3603 |
| d_Performance (Quarter) | -0.1393 | -0.0392 | -0.1173 | -0.25% | -0.08% | 4329/6490 |
| d_Market Cap | -0.1290 | +0.0304 | -0.0819 | -0.21% | 0.14% | 3277/2437 |
| d_Forward P/E | -0.1282 | +0.0282 | -0.1414 | -0.35% | 0.09% | 1471/1466 |
| d_20-Day Simple Moving Average | -0.1281 | +0.0255 | -0.1422 | -0.18% | -0.10% | 7245/4192 |
| d_Performance (Week) | -0.0909 | +0.0776 | -0.1904 | -0.14% | -0.15% | 8186/3211 |
| d_Beta | +0.0704 | -0.0257 | +0.1300 | -0.19% | -0.63% | 1001/1677 |
| Short Float | -0.0695 | +0.1390 | -0.1574 | -0.06% | n/a | 5692/0 |
| Relative Volume | -0.0679 | +0.0793 | -0.0700 | -0.16% | n/a | 11347/0 |
| upside_pct_lvl | -0.0593 | +0.3468 | -0.3205 | -0.06% | -0.65% | 4297/353 |
| d_Volatility (Month) | -0.0496 | -0.0200 | -0.0435 | -0.14% | -0.16% | 3578/5913 |
| Institutional Transactions | -0.0444 | +0.0393 | -0.0678 | -0.26% | 0.36% | 3177/1880 |
| d_Institutional Ownership | +0.0371 | -0.0074 | +0.0580 | 0.66% | -1.04% | 18/49 |
| d_Target Price | -0.0369 | -0.0054 | -0.0199 | -0.81% | -0.27% | 216/103 |
| d_Analyst Recom | -0.0327 | -0.0505 | +0.0484 | -0.32% | 0.25% | 89/74 |
| d_Short Float | -0.0275 | -0.0002 | +0.0106 | 0.22% | -0.34% | 63/78 |
| d_EPS Surprise | -0.0242 | -0.0201 | -0.0333 | -1.59% | 0.33% | 19/11 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 491 | -1.41% | 23.0% |
| true_ret>3% & UPTREND | 387 | -1.46% | 14.7% |
| true_ret>3% & MIXED | 346 | -1.15% | 17.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 504 | -1.86% | -3.54% |
| WASHED | 443 | 0.08% | -1.14% |
