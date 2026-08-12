# Factor attribution — signal 2026-08-10 → prediction day 2026-08-12

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-10** | Features/scores formed from this snapshot (and deltas vs **2026-08-07**). Only data on/before this date. |
| **Prediction day** | **2026-08-12** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-10 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-12 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11533** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0596**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.73% | 42.3% | 2360 |
| 2 | 0.27% | 13.5% | 2843 |
| 3 | 0.26% | 13.1% | 2310 |
| 4 | 0.45% | 18.0% | 1801 |
| 5 | 0.57% | 29.9% | 2219 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_200-Day Simple Moving Average | -0.1722 | -0.2249 | -0.0589 | 0.21% | 0.94% | 4289/7067 |
| d_Performance (YTD) | -0.1654 | -0.2342 | -0.0252 | 0.23% | 0.95% | 4316/6793 |
| d_Price | -0.1647 | -0.1536 | -0.0567 | 0.25% | 0.97% | 4198/6681 |
| d_20-Day Simple Moving Average | -0.1556 | -0.2294 | -0.0565 | 0.21% | 0.90% | 3983/7418 |
| d_50-Day Simple Moving Average | -0.1555 | -0.2113 | -0.0692 | 0.20% | 0.94% | 4315/7071 |
| true_ret | -0.1542 | -0.2337 | -0.0234 | 0.25% | 0.97% | 4198/6681 |
| d_Performance (Week) | -0.1530 | -0.3778 | +0.0961 | 0.21% | 0.81% | 2936/8417 |
| d_Performance (Quarter) | -0.1521 | -0.1789 | -0.0745 | 0.34% | 0.63% | 3689/7111 |
| d_Relative Strength Index (14) | -0.1154 | +0.0180 | -0.0530 | 0.23% | 0.94% | 4316/6779 |
| d_Forward P/E | -0.1146 | -0.1371 | +0.0062 | -0.14% | 0.65% | 1097/1885 |
| Performance (Month) | -0.0949 | -0.1635 | +0.0926 | 0.19% | 1.21% | 6338/4971 |
| d_Market Cap | -0.0925 | -0.0443 | -0.0659 | 0.43% | 0.75% | 2379/3333 |
| d_Performance (Month) | -0.0787 | -0.1070 | -0.0789 | 0.30% | 0.84% | 4089/7117 |
| Relative Strength Index (14) | -0.0738 | -0.2121 | +0.2617 | 0.66% | n/a | 11434/0 |
| d_Institutional Ownership | +0.0678 | -0.0125 | +0.0475 | 0.90% | 0.31% | 3404/1512 |
| Institutional Transactions | +0.0626 | +0.0964 | -0.0287 | 0.73% | 0.67% | 2521/2519 |
| d_Volatility (Month) | +0.0402 | +0.1228 | -0.0759 | 0.97% | 0.48% | 4595/4618 |
| Performance (Week) | +0.0379 | +0.1123 | +0.0022 | 0.65% | 0.67% | 8013/3336 |
| Short Float | +0.0369 | +0.2334 | -0.1316 | 0.63% | n/a | 5686/0 |
| upside_pct_lvl | +0.0283 | +0.3447 | -0.2831 | 0.64% | -0.49% | 4274/369 |
| d_Average Volume | -0.0281 | -0.0650 | -0.0069 | 0.76% | 0.62% | 4318/6677 |
| d_Institutional Transactions | +0.0239 | +0.0078 | -0.0098 | 0.95% | 0.50% | 2213/2490 |
| d_Short Ratio | +0.0192 | +0.0475 | -0.0100 | 0.57% | 0.66% | 4292/2553 |
| Relative Volume | +0.0184 | +0.0927 | -0.0639 | 0.66% | n/a | 11305/0 |
| d_Insider Transactions | +0.0156 | +0.0367 | -0.0366 | 1.14% | 0.75% | 393/386 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 304 | 3.31% | 35.5% |
| true_ret>3% & UPTREND | 446 | 0.05% | 29.8% |
| true_ret>3% & MIXED | 216 | -1.50% | 30.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 349 | -0.70% | -1.21% |
| WASHED | 639 | 4.06% | 8.71% |
