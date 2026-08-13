# Factor attribution — signal 2026-08-10 → prediction day 2026-08-13

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-10** | Features/scores formed from this snapshot (and deltas vs **2026-08-07**). Only data on/before this date. |
| **Prediction day** | **2026-08-13** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-10 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-13 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11533** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.1054**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.51% | 49.3% | 2360 |
| 2 | 1.06% | 19.1% | 2843 |
| 3 | 0.67% | 19.5% | 2310 |
| 4 | 0.92% | 27.5% | 1801 |
| 5 | 1.17% | 34.5% | 2219 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.2241 | -0.3980 | +0.0492 | 1.25% | 1.58% | 2936/8417 |
| d_200-Day Simple Moving Average | -0.1930 | -0.2141 | -0.0387 | 1.04% | 1.78% | 4289/7067 |
| d_Performance (YTD) | -0.1883 | -0.2231 | -0.0139 | 0.81% | 1.83% | 4316/6793 |
| d_50-Day Simple Moving Average | -0.1879 | -0.2089 | -0.0588 | 0.98% | 1.81% | 4315/7071 |
| d_Price | -0.1875 | -0.1542 | -0.0332 | 0.85% | 1.86% | 4198/6681 |
| true_ret | -0.1779 | -0.2233 | -0.0186 | 0.85% | 1.86% | 4198/6681 |
| d_20-Day Simple Moving Average | -0.1766 | -0.2222 | -0.0452 | 1.05% | 1.73% | 3983/7418 |
| d_Performance (Quarter) | -0.1726 | -0.1903 | -0.0562 | 0.98% | 1.59% | 3689/7111 |
| d_Relative Strength Index (14) | -0.1438 | -0.0066 | -0.0109 | 1.03% | 1.82% | 4316/6779 |
| d_Performance (Month) | -0.1329 | -0.1347 | -0.0716 | 0.85% | 1.81% | 4089/7117 |
| d_Market Cap | -0.1108 | -0.0244 | -0.0633 | 1.58% | 2.14% | 2379/3333 |
| d_Forward P/E | -0.0881 | -0.0878 | -0.0169 | 0.79% | 1.37% | 1097/1885 |
| Performance (Month) | -0.0877 | -0.1335 | +0.0703 | 0.70% | 2.43% | 6338/4971 |
| Short Float | +0.0801 | +0.2716 | -0.1395 | 1.92% | n/a | 5686/0 |
| Relative Strength Index (14) | -0.0766 | -0.2128 | +0.1918 | 1.48% | n/a | 11434/0 |
| d_Institutional Ownership | +0.0753 | +0.0014 | +0.0667 | 1.44% | 1.44% | 3404/1512 |
| d_Short Float | +0.0277 | -0.0253 | +0.0320 | 1.47% | 0.88% | 406/610 |
| d_Sales Growth Quarter Over Quarter | -0.0262 | -0.0226 | +0.0276 | 0.48% | 1.24% | 208/186 |
| upside_pct_lvl | -0.0257 | +0.2971 | -0.2870 | 1.59% | 0.49% | 4274/369 |
| Institutional Transactions | +0.0250 | +0.0493 | -0.0628 | 1.93% | 2.18% | 2521/2519 |
| d_Average Volume | -0.0207 | -0.0631 | -0.0158 | 1.78% | 1.35% | 4318/6677 |
| d_Target Price | -0.0171 | -0.0479 | +0.0461 | 0.72% | 1.33% | 544/279 |
| Relative Volume | +0.0169 | +0.0936 | -0.0240 | 1.51% | n/a | 11305/0 |
| d_Analyst Recom | -0.0162 | -0.0558 | -0.0288 | 1.42% | 1.97% | 123/129 |
| d_Insider Transactions | -0.0156 | +0.0066 | -0.0206 | 1.50% | 1.66% | 393/386 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 304 | 6.35% | 38.5% |
| true_ret>3% & UPTREND | 446 | 0.23% | 35.0% |
| true_ret>3% & MIXED | 216 | -0.75% | 33.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 349 | -0.10% | -0.56% |
| WASHED | 639 | 8.00% | 17.03% |
