# Factor attribution — signal 2026-08-25 → prediction day 2026-08-28

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-25** | Features/scores formed from this snapshot (and deltas vs **2026-08-24**). Only data on/before this date. |
| **Prediction day** | **2026-08-28** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-25 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-28 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11611** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0041**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.47% | 24.5% | 2336 |
| 2 | -0.10% | 12.3% | 2738 |
| 3 | 0.22% | 10.8% | 1953 |
| 4 | -0.09% | 10.7% | 2285 |
| 5 | 2.29% | 29.8% | 2299 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.2219 | -0.1490 | -0.1910 | 0.46% | 1.19% | 6640/4764 |
| d_Performance (Quarter) | -0.1144 | -0.0411 | -0.0927 | 0.15% | 1.15% | 4329/6490 |
| Relative Strength Index (14) | -0.1033 | -0.2547 | +0.0728 | 0.75% | n/a | 11488/0 |
| d_Forward P/E | -0.0830 | +0.0080 | -0.1056 | -0.26% | 0.34% | 1471/1466 |
| d_Performance (Week) | +0.0798 | +0.1925 | -0.1098 | 0.31% | 1.93% | 8186/3211 |
| d_Market Cap | -0.0723 | +0.0264 | -0.0609 | 0.09% | 2.55% | 3277/2437 |
| d_Beta | -0.0722 | -0.1504 | +0.0529 | 1.19% | 0.37% | 1001/1677 |
| Relative Volume | -0.0660 | +0.0517 | -0.0084 | 0.74% | n/a | 11347/0 |
| d_Performance (Month) | +0.0625 | +0.0691 | +0.0254 | 0.99% | 0.50% | 6065/5199 |
| d_Volatility (Month) | -0.0502 | -0.0709 | -0.0077 | 0.79% | 1.00% | 3578/5913 |
| d_Relative Strength Index (14) | -0.0488 | -0.0860 | +0.1902 | 0.26% | 1.87% | 7557/3603 |
| d_20-Day Simple Moving Average | -0.0477 | +0.0805 | -0.0994 | 0.26% | 1.61% | 7245/4192 |
| d_Average Volume | -0.0340 | +0.0008 | +0.0026 | 0.98% | 0.60% | 5291/5759 |
| d_Analyst Recom | -0.0313 | -0.0408 | +0.0206 | -0.51% | 0.42% | 89/74 |
| upside_pct_lvl | -0.0308 | +0.3256 | -0.2976 | 1.29% | -0.36% | 4297/353 |
| true_ret | -0.0304 | +0.1106 | -0.1184 | 0.24% | 0.90% | 7523/3557 |
| Institutional Transactions | +0.0301 | +0.0765 | +0.0029 | 1.81% | 0.59% | 3177/1880 |
| d_200-Day Simple Moving Average | -0.0284 | +0.1246 | -0.1224 | 0.71% | 0.84% | 7599/3857 |
| d_Relative Volume | -0.0247 | -0.0455 | +0.0058 | 1.15% | 0.47% | 4978/6197 |
| Performance (Month) | +0.0234 | +0.1300 | -0.1137 | 0.85% | 0.51% | 7983/3381 |
| d_50-Day Simple Moving Average | -0.0231 | +0.1300 | -0.1227 | 0.73% | 0.80% | 7520/3964 |
| d_Institutional Ownership | +0.0224 | -0.0129 | +0.0734 | -0.12% | -1.65% | 18/49 |
| d_Short Ratio | +0.0222 | -0.0188 | -0.0085 | 0.40% | 0.24% | 3498/3214 |
| d_Gross Margin | -0.0186 | +0.0026 | -0.0156 | -1.16% | 1.58% | 11/7 |
| d_Performance (YTD) | -0.0185 | +0.1017 | -0.0912 | 0.25% | 1.85% | 7605/3622 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 491 | 0.89% | 33.6% |
| true_ret>3% & UPTREND | 387 | -0.46% | 30.0% |
| true_ret>3% & MIXED | 346 | 0.68% | 33.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 504 | -0.40% | -3.24% |
| WASHED | 443 | 3.06% | -0.54% |
