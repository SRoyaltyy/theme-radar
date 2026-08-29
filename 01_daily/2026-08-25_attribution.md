# Factor attribution — signal 2026-08-25 → prediction day 2026-08-28

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-25** | Features/scores formed from this snapshot (and deltas vs **2026-08-24**). Only data on/before this date. |
| **Prediction day** | **2026-08-28** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-25 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-28 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11610** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1093**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.52% | 21.4% | 2336 |
| 2 | -0.64% | 9.9% | 2738 |
| 3 | -0.53% | 6.5% | 1952 |
| 4 | -0.78% | 6.7% | 2285 |
| 5 | -0.20% | 16.2% | 2299 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Forward P/E | -0.2236 | -0.0537 | -0.2168 | -1.36% | 0.13% | 1471/1466 |
| d_50-Day Simple Moving Average | -0.2180 | -0.0277 | -0.2541 | -0.66% | 0.29% | 7519/3964 |
| d_200-Day Simple Moving Average | -0.2152 | -0.0160 | -0.2498 | -0.66% | 0.31% | 7598/3857 |
| true_ret | -0.2152 | -0.0426 | -0.2464 | -1.06% | 0.31% | 7522/3557 |
| d_Performance (Week) | -0.2077 | -0.0224 | -0.2698 | -0.98% | 1.34% | 8185/3211 |
| d_Performance (YTD) | -0.2046 | -0.0426 | -0.2191 | -1.05% | 1.16% | 7604/3622 |
| d_Market Cap | -0.1972 | +0.0114 | -0.1295 | -1.18% | 1.67% | 3277/2437 |
| d_20-Day Simple Moving Average | -0.1952 | -0.0530 | -0.2041 | -1.06% | 0.92% | 7244/4192 |
| Performance (Week) | -0.1920 | -0.0754 | -0.1545 | -0.51% | -0.05% | 6639/4764 |
| upside_pct_lvl | -0.1910 | +0.2891 | -0.3905 | 0.08% | -0.78% | 4297/353 |
| d_Price | -0.1665 | -0.1009 | -0.1098 | -1.06% | 0.31% | 7522/3557 |
| Short Float | -0.1476 | +0.2158 | -0.2048 | 0.10% | n/a | 5692/0 |
| d_Relative Strength Index (14) | -0.1334 | -0.1661 | +0.0753 | -1.02% | 1.18% | 7556/3603 |
| Relative Volume | -0.0945 | +0.0708 | -0.0762 | -0.34% | n/a | 11346/0 |
| Institutional Transactions | -0.0790 | +0.0702 | -0.1154 | 0.40% | -0.20% | 3177/1880 |
| d_Performance (Month) | -0.0613 | -0.0431 | -0.0908 | -0.36% | -0.29% | 6064/5199 |
| Performance (Month) | -0.0560 | +0.1145 | -0.1478 | -0.18% | -0.67% | 7983/3380 |
| d_Average Volume | -0.0557 | -0.0031 | -0.0565 | -0.24% | -0.40% | 5291/5759 |
| d_Beta | +0.0534 | -0.0940 | +0.1346 | 0.52% | -1.86% | 1001/1677 |
| d_Performance (Quarter) | -0.0496 | +0.0299 | -0.0948 | -0.89% | 0.17% | 4329/6489 |
| Relative Strength Index (14) | -0.0419 | -0.2452 | +0.0575 | -0.32% | n/a | 11487/0 |
| d_Institutional Ownership | +0.0394 | +0.0146 | +0.0587 | -2.23% | -4.39% | 18/49 |
| d_Short Ratio | +0.0359 | -0.0103 | +0.0369 | -0.65% | -0.98% | 3498/3213 |
| d_Sales Year Over Year TTM | -0.0270 | -0.0177 | -0.0473 | -3.70% | 3.24% | 12/4 |
| d_Gross Margin | -0.0240 | +0.0118 | +0.0079 | -2.76% | -0.27% | 11/7 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 491 | -3.45% | 19.1% |
| true_ret>3% & UPTREND | 387 | -4.01% | 15.5% |
| true_ret>3% & MIXED | 346 | -3.63% | 17.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 504 | -2.52% | -3.26% |
| WASHED | 443 | 1.61% | -4.15% |
