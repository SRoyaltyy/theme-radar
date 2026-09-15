# Factor attribution — signal 2026-09-14 → prediction day 2026-09-15

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-14** | Features/scores formed from this snapshot (and deltas vs **2026-09-11**). Only data on/before this date. |
| **Prediction day** | **2026-09-15** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-14 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-15 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11604** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0250**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.52% | 11.2% | 2518 |
| 2 | -0.68% | 4.5% | 2855 |
| 3 | -0.72% | 6.3% | 1662 |
| 4 | -0.61% | 5.4% | 2302 |
| 5 | -1.42% | 13.3% | 2267 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2933 | +0.2258 | -0.4286 | -1.25% | -0.19% | 4367/273 |
| Performance (Week) | +0.2160 | -0.0230 | +0.2880 | -0.70% | -0.81% | 2231/9235 |
| Performance (Month) | +0.1591 | -0.0372 | +0.2072 | -0.97% | -0.73% | 3033/8386 |
| Short Float | -0.1195 | +0.1356 | -0.1881 | -0.91% | n/a | 5706/0 |
| d_Forward P/E | -0.0981 | -0.0812 | -0.0766 | -0.94% | -0.56% | 1451/1497 |
| d_Relative Strength Index (14) | -0.0974 | -0.0012 | -0.1916 | -1.14% | -0.60% | 4021/7169 |
| Relative Strength Index (14) | +0.0936 | +0.0126 | -0.0705 | -0.79% | n/a | 11525/0 |
| d_20-Day Simple Moving Average | -0.0649 | -0.0733 | -0.0584 | -1.05% | -0.60% | 4798/6660 |
| d_50-Day Simple Moving Average | -0.0638 | -0.0827 | -0.0552 | -1.13% | -0.58% | 4337/7140 |
| d_Price | -0.0636 | -0.0271 | -0.1347 | -1.17% | -0.57% | 3935/7090 |
| d_200-Day Simple Moving Average | -0.0601 | -0.0726 | -0.0634 | -1.16% | -0.58% | 4135/7342 |
| d_Target Price | +0.0598 | +0.0899 | +0.0190 | -0.31% | -1.48% | 212/198 |
| d_Performance (YTD) | -0.0486 | -0.0707 | -0.0524 | -1.14% | -0.59% | 4000/7186 |
| d_Market Cap | -0.0435 | -0.0403 | -0.0290 | -1.00% | -0.84% | 2575/3108 |
| d_Short Float | +0.0414 | -0.0827 | +0.0551 | -1.30% | -0.95% | 104/256 |
| d_Performance (Week) | -0.0394 | -0.0279 | -0.0219 | -1.03% | -0.64% | 4357/7015 |
| true_ret | -0.0389 | -0.0928 | -0.0255 | -1.17% | -0.57% | 3935/7090 |
| d_Relative Volume | +0.0388 | +0.0053 | +0.0171 | -0.73% | -0.85% | 6641/4551 |
| d_Performance (Quarter) | -0.0353 | +0.0130 | -0.0624 | -1.13% | -0.62% | 3720/7170 |
| d_Performance (Month) | +0.0331 | -0.0315 | +0.0156 | -1.13% | -0.66% | 3327/7992 |
| d_Profit Margin | +0.0301 | +0.0306 | +0.0156 | 0.23% | -3.39% | 4/5 |
| d_Institutional Transactions | +0.0293 | -0.0040 | +0.0224 | -1.02% | -1.19% | 2142/1491 |
| d_Short Ratio | -0.0287 | -0.0207 | -0.0503 | -0.86% | -1.08% | 4521/2743 |
| Relative Volume | +0.0189 | +0.0615 | -0.0315 | -0.79% | n/a | 11409/0 |
| d_Analyst Recom | +0.0170 | -0.0084 | +0.0192 | -1.08% | -1.36% | 96/124 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 329 | -0.11% | 17.0% |
| true_ret>3% & UPTREND | 365 | -1.32% | 18.4% |
| true_ret>3% & MIXED | 223 | -4.28% | 13.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 158 | -3.23% | -5.97% |
| WASHED | 1684 | -0.94% | -1.30% |
