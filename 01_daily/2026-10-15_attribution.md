# Factor attribution — signal 2026-10-15 → prediction day 2026-10-19

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-15** | Features/scores formed from this snapshot (and deltas vs **2026-10-14**). Only data on/before this date. |
| **Prediction day** | **2026-10-19** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-15 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-19 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11715** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0222**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.38% | 9.8% | 2678 |
| 2 | 1.32% | 4.7% | 2255 |
| 3 | -0.84% | 5.2% | 2266 |
| 4 | -2.16% | 8.7% | 2178 |
| 5 | -2.04% | 10.8% | 2338 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.3650 | -0.1298 | -0.3706 | -1.33% | 0.75% | 8725/2797 |
| Relative Strength Index (14) | +0.3349 | -0.1348 | +0.4116 | -0.81% | n/a | 11646/0 |
| upside_pct_lvl | -0.3126 | +0.3476 | -0.4776 | 0.12% | -1.45% | 4334/299 |
| Performance (Week) | +0.3091 | -0.0563 | +0.3939 | -0.79% | -0.82% | 5541/5995 |
| d_Beta | -0.2816 | +0.0048 | -0.3253 | -0.57% | -0.69% | 3038/1525 |
| Short Float | -0.2298 | +0.1518 | -0.2400 | -0.28% | n/a | 5662/0 |
| d_Performance (Quarter) | -0.2148 | -0.1065 | -0.1957 | -1.70% | 2.41% | 8751/2456 |
| Performance (Month) | +0.2044 | -0.1257 | +0.3148 | -1.14% | -0.60% | 4603/6920 |
| d_20-Day Simple Moving Average | -0.1936 | -0.0475 | -0.2138 | -1.70% | 1.84% | 8689/2930 |
| d_50-Day Simple Moving Average | -0.1646 | -0.0556 | -0.1705 | -1.67% | 1.60% | 8565/3045 |
| d_Volatility (Month) | -0.1573 | +0.0760 | -0.1904 | -0.61% | -1.31% | 6517/3354 |
| true_ret | -0.1458 | -0.0692 | -0.1424 | -1.58% | 1.46% | 8230/3026 |
| d_200-Day Simple Moving Average | -0.1367 | -0.0644 | -0.1221 | -1.66% | 1.41% | 8374/3211 |
| d_Performance (YTD) | -0.1119 | -0.0818 | -0.0760 | -1.59% | 1.42% | 8300/3065 |
| d_Forward P/E | -0.1023 | -0.1422 | -0.0505 | -1.44% | -0.93% | 2216/751 |
| d_Performance (Month) | -0.0783 | +0.1118 | -0.1203 | -0.91% | -0.53% | 8579/2868 |
| Institutional Transactions | -0.0766 | +0.0866 | -0.1182 | -1.01% | 1.54% | 3260/1776 |
| d_Short Ratio | +0.0566 | +0.0208 | +0.0684 | -1.57% | -0.75% | 2643/4396 |
| d_Average Volume | -0.0516 | -0.0065 | -0.0936 | -1.00% | -0.50% | 6692/4337 |
| d_Short Float | +0.0386 | -0.0189 | +0.0424 | -1.96% | -3.97% | 35/72 |
| d_Market Cap | +0.0366 | -0.1547 | +0.1643 | -1.96% | 3.28% | 3911/1813 |
| Relative Volume | -0.0345 | +0.0172 | -0.0845 | -0.81% | n/a | 11476/0 |
| d_Price | -0.0285 | -0.1464 | +0.1014 | -1.58% | 1.46% | 8230/3026 |
| d_Profit Margin | +0.0255 | -0.0344 | +0.0162 | -0.63% | -2.27% | 12/7 |
| d_EPS Surprise | -0.0212 | +0.0446 | -0.0327 | -2.41% | -0.51% | 9/15 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1093 | -4.40% | 9.7% |
| true_ret>3% & UPTREND | 393 | -2.28% | 11.5% |
| true_ret>3% & MIXED | 299 | -2.49% | 16.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 154 | -2.58% | -6.95% |
| WASHED | 1200 | -0.26% | -5.16% |
