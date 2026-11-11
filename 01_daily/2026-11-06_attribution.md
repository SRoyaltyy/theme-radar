# Factor attribution — signal 2026-11-06 → prediction day 2026-11-11

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-06** | Features/scores formed from this snapshot (and deltas vs **2026-11-05**). Only data on/before this date. |
| **Prediction day** | **2026-11-11** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-06 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-11 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11722** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.1068**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.52% | 54.6% | 2367 |
| 2 | 2.39% | 61.9% | 2417 |
| 3 | 4.27% | 45.0% | 2633 |
| 4 | 5.17% | 44.5% | 2138 |
| 5 | 5.37% | 63.7% | 2167 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.3502 | -0.4397 | +0.0644 | 0.93% | 5.74% | 4250/7319 |
| Relative Strength Index (14) | -0.3354 | -0.3678 | +0.3477 | 4.10% | n/a | 11670/0 |
| d_Volatility (Month) | +0.2877 | +0.5119 | -0.4792 | 4.37% | 4.80% | 9326/1255 |
| Performance (Month) | -0.2769 | -0.4726 | +0.2506 | 0.84% | 6.32% | 4635/6931 |
| d_Performance (Week) | +0.2762 | +0.4871 | -0.2244 | 5.02% | 2.11% | 8085/3490 |
| d_Beta | +0.2568 | +0.2544 | +0.0820 | 5.62% | 2.49% | 3067/5009 |
| d_Price | +0.2513 | +0.3468 | -0.0274 | 4.36% | 2.24% | 6537/4682 |
| d_20-Day Simple Moving Average | +0.2452 | +0.4296 | -0.1378 | 5.81% | 1.61% | 6984/4620 |
| d_Performance (Month) | +0.2203 | +0.3948 | -0.1393 | 5.78% | 2.03% | 6507/4964 |
| d_50-Day Simple Moving Average | +0.2185 | +0.3949 | -0.1048 | 5.37% | 2.18% | 7122/4474 |
| d_Performance (YTD) | +0.2177 | +0.3528 | -0.0509 | 4.78% | 3.36% | 6615/4733 |
| true_ret | +0.2107 | +0.3599 | -0.0571 | 4.36% | 2.24% | 6537/4682 |
| d_200-Day Simple Moving Average | +0.2051 | +0.3648 | -0.0817 | 4.88% | 3.13% | 6793/4785 |
| d_Forward P/E | +0.1965 | +0.2859 | -0.1947 | 3.82% | 1.90% | 1404/1531 |
| d_Relative Strength Index (14) | +0.1923 | +0.2973 | -0.0498 | 4.80% | 3.35% | 6634/4740 |
| d_Performance (Quarter) | +0.1651 | +0.3054 | -0.0621 | 4.75% | 3.10% | 7114/4088 |
| Short Float | +0.1483 | +0.2467 | -0.1937 | 5.48% | n/a | 5622/0 |
| d_Market Cap | +0.1323 | +0.2548 | -0.0839 | 5.21% | 5.23% | 3271/2451 |
| Relative Volume | +0.1308 | +0.1293 | -0.0519 | 4.18% | n/a | 11437/0 |
| d_Short Ratio | -0.0930 | -0.1250 | +0.0980 | 3.91% | 4.69% | 1976/5710 |
| d_Relative Volume | -0.0906 | -0.0777 | +0.0669 | 3.06% | 4.58% | 3060/8351 |
| d_Average Volume | +0.0647 | +0.1471 | -0.0917 | 4.48% | 3.55% | 7961/3189 |
| upside_pct_lvl | +0.0559 | +0.4668 | -0.4395 | 5.65% | 0.89% | 4352/276 |
| Institutional Transactions | +0.0493 | +0.1112 | -0.0572 | 6.42% | 5.54% | 3187/1829 |
| d_Institutional Ownership | +0.0447 | -0.0149 | +0.0707 | 4.40% | 5.11% | 2248/1835 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1482 | 11.50% | 69.2% |
| true_ret>3% & UPTREND | 237 | 1.85% | 60.3% |
| true_ret>3% & MIXED | 254 | 3.66% | 62.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 260 | -2.17% | 1.65% |
| WASHED | 1957 | 16.11% | 13.77% |
