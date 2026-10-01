# Factor attribution — signal 2026-09-25 → prediction day 2026-09-30

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-25** | Features/scores formed from this snapshot (and deltas vs **2026-09-24**). Only data on/before this date. |
| **Prediction day** | **2026-09-30** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-25 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-30 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11664** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0952**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 4.43% | 14.0% | 2372 |
| 2 | 0.04% | 7.0% | 2562 |
| 3 | -1.23% | 6.2% | 2131 |
| 4 | 3.18% | 7.8% | 2266 |
| 5 | -2.04% | 13.7% | 2333 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | -0.1568 | -0.0505 | -0.1373 | 0.19% | 2.29% | 7274/4079 |
| d_20-Day Simple Moving Average | -0.1564 | -0.0512 | -0.1236 | 0.17% | 2.45% | 7864/3714 |
| Performance (Month) | +0.1358 | -0.1680 | +0.2471 | -0.83% | 1.73% | 3597/7880 |
| d_50-Day Simple Moving Average | -0.1211 | -0.0847 | -0.0647 | 0.12% | 2.28% | 7351/4210 |
| d_Performance (Week) | -0.1184 | -0.0914 | -0.0885 | -0.31% | 3.21% | 7464/3996 |
| d_200-Day Simple Moving Average | -0.1162 | -0.0867 | -0.0444 | -1.12% | 2.24% | 7195/4339 |
| true_ret | -0.1034 | -0.1147 | -0.0275 | -1.39% | 2.25% | 6905/4151 |
| d_Performance (YTD) | -0.1010 | -0.1038 | -0.0108 | -1.14% | 2.23% | 7001/4224 |
| upside_pct_lvl | -0.0966 | +0.3438 | -0.3212 | 1.38% | -1.13% | 4374/260 |
| d_Price | -0.0879 | -0.0856 | +0.0448 | -1.39% | 2.25% | 6905/4151 |
| Short Float | -0.0732 | +0.2632 | -0.1497 | 3.11% | n/a | 5697/0 |
| d_Forward P/E | -0.0700 | -0.0529 | -0.0138 | -1.85% | -1.53% | 1734/1192 |
| Relative Strength Index (14) | +0.0690 | -0.1508 | +0.0372 | 0.91% | n/a | 11562/0 |
| d_Market Cap | -0.0662 | -0.0830 | +0.0532 | 2.31% | 4.17% | 2961/2698 |
| d_Short Ratio | -0.0595 | -0.0557 | -0.0721 | -1.29% | 2.02% | 4239/3175 |
| d_Relative Strength Index (14) | -0.0501 | -0.1149 | +0.1426 | 0.14% | 2.21% | 6983/4221 |
| d_Average Volume | +0.0498 | +0.0669 | +0.0707 | 3.53% | -1.10% | 5026/6098 |
| d_Total Debt/Equity | -0.0302 | -0.0329 | -0.0087 | -14.29% | -0.87% | 3/9 |
| d_Analyst Recom | +0.0284 | +0.0024 | +0.0330 | 0.04% | -1.80% | 39/67 |
| Performance (Week) | +0.0281 | -0.1017 | +0.1083 | -1.37% | 2.75% | 5080/6397 |
| Relative Volume | -0.0268 | +0.1076 | -0.0238 | 0.92% | n/a | 11410/0 |
| d_Beta | -0.0195 | +0.0449 | -0.0287 | -0.00% | 0.98% | 1024/598 |
| d_Insider Transactions | -0.0189 | +0.0023 | -0.0114 | 61.04% | -1.33% | 141/128 |
| Institutional Transactions | -0.0186 | +0.0520 | -0.0951 | 4.71% | 2.20% | 3220/1809 |
| d_Institutional Ownership | +0.0171 | +0.0007 | +0.0034 | 0.93% | 67.06% | 13/23 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 277 | -2.74% | 21.7% |
| true_ret>3% & UPTREND | 218 | -3.18% | 17.0% |
| true_ret>3% & MIXED | 139 | 0.20% | 23.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 215 | -2.93% | -2.10% |
| WASHED | 1885 | 9.85% | 24.87% |
