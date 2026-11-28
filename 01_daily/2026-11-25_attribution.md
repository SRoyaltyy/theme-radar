# Factor attribution — signal 2026-11-25 → prediction day 2026-11-27

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-25** | Features/scores formed from this snapshot (and deltas vs **2026-11-24**). Only data on/before this date. |
| **Prediction day** | **2026-11-27** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-25 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-27 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11771** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.1635**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 4.12% | 56.2% | 2473 |
| 2 | 1.61% | 41.7% | 2583 |
| 3 | 1.41% | 25.9% | 2092 |
| 4 | 2.06% | 29.0% | 2301 |
| 5 | 2.62% | 44.0% | 2322 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | -0.4115 | -0.5407 | +0.1744 | 0.99% | 2.96% | 3245/8360 |
| Performance (Week) | -0.3957 | -0.4735 | +0.0618 | 0.88% | 3.27% | 4174/7421 |
| Relative Strength Index (14) | -0.3746 | -0.3977 | +0.3384 | 2.39% | n/a | 11680/0 |
| d_Volatility (Month) | +0.3664 | +0.5090 | -0.4598 | 2.52% | 3.20% | 8799/1631 |
| d_Performance (Month) | -0.2506 | -0.2694 | -0.0597 | 2.10% | 2.73% | 5473/6040 |
| upside_pct_lvl | +0.2301 | +0.5523 | -0.5924 | 2.78% | 0.65% | 4391/240 |
| d_Beta | +0.2147 | +0.3088 | -0.0195 | 5.10% | 1.35% | 2870/3488 |
| Short Float | +0.1861 | +0.1367 | -0.0497 | 3.26% | n/a | 5589/0 |
| d_20-Day Simple Moving Average | +0.1781 | +0.2434 | -0.1460 | 2.36% | 2.59% | 8952/2708 |
| d_Relative Strength Index (14) | -0.1334 | -0.0991 | +0.3003 | 2.24% | 2.82% | 7431/3944 |
| d_Performance (Quarter) | -0.1317 | -0.1343 | -0.0503 | 2.11% | 2.91% | 6497/4781 |
| Relative Volume | +0.1307 | +0.0978 | -0.1240 | 2.43% | n/a | 11529/0 |
| d_50-Day Simple Moving Average | +0.0625 | +0.1032 | -0.1323 | 2.43% | 2.38% | 8119/3521 |
| d_Forward P/E | +0.0530 | +0.0622 | +0.0344 | 1.93% | 1.83% | 1998/868 |
| d_Price | -0.0447 | -0.0773 | +0.1655 | 2.08% | 2.57% | 7336/3855 |
| d_Relative Volume | +0.0437 | +0.0420 | -0.0690 | 2.32% | 2.55% | 6133/5244 |
| d_Target Price | -0.0435 | -0.0494 | +0.0563 | 1.43% | 3.31% | 111/164 |
| d_Insider Transactions | +0.0428 | +0.0757 | -0.0512 | 18.76% | 1.46% | 152/162 |
| d_Market Cap | +0.0414 | -0.0604 | +0.2116 | 2.80% | 3.35% | 3701/1992 |
| d_Performance (Week) | +0.0329 | +0.0490 | -0.0905 | 2.60% | 2.11% | 7537/4019 |
| Institutional Transactions | +0.0243 | +0.0306 | -0.0501 | 4.82% | 2.30% | 2579/2423 |
| d_Analyst Recom | -0.0223 | -0.0162 | +0.0309 | 2.50% | 2.66% | 67/70 |
| d_Short Ratio | -0.0208 | -0.0113 | -0.0019 | 2.51% | 1.93% | 2644/4287 |
| d_Average Volume | +0.0197 | +0.0318 | -0.0034 | 2.56% | 2.32% | 6697/4470 |
| d_Performance (YTD) | -0.0174 | -0.0250 | -0.0008 | 1.94% | 2.39% | 7431/3941 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 927 | 7.33% | 67.2% |
| true_ret>3% & UPTREND | 169 | 0.35% | 44.4% |
| true_ret>3% & MIXED | 212 | 1.28% | 51.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 165 | -0.28% | -0.82% |
| WASHED | 2031 | 5.73% | 9.03% |
