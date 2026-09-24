# Factor attribution — signal 2026-09-23 → prediction day 2026-09-24

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-23** | Features/scores formed from this snapshot (and deltas vs **2026-09-22**). Only data on/before this date. |
| **Prediction day** | **2026-09-24** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-23 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-24 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11653** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0928**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.51% | 13.0% | 2493 |
| 2 | -0.32% | 6.2% | 3301 |
| 3 | -0.27% | 12.9% | 1200 |
| 4 | -0.10% | 5.4% | 2544 |
| 5 | -0.37% | 17.0% | 2115 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Relative Strength Index (14) | +0.2015 | -0.0885 | -0.0024 | -0.32% | n/a | 11559/0 |
| upside_pct_lvl | -0.1738 | +0.2309 | -0.3719 | -0.63% | 0.20% | 4372/267 |
| Performance (Month) | +0.1733 | -0.0999 | +0.2703 | 0.01% | -0.47% | 3693/7778 |
| d_Performance (Month) | +0.0794 | -0.0311 | +0.0842 | -0.23% | -0.36% | 3407/7989 |
| true_ret | +0.0790 | -0.2310 | +0.2281 | -0.28% | -0.32% | 1880/9370 |
| Performance (Week) | +0.0720 | +0.0147 | +0.0586 | -0.15% | -0.48% | 5743/5716 |
| d_Target Price | +0.0526 | +0.0067 | -0.0217 | 0.05% | -0.62% | 104/138 |
| d_50-Day Simple Moving Average | +0.0509 | -0.2141 | +0.1823 | -0.34% | -0.31% | 2077/9488 |
| d_Performance (Quarter) | +0.0503 | -0.0724 | +0.0730 | -0.30% | -0.33% | 3098/7903 |
| d_Performance (YTD) | +0.0493 | -0.1785 | +0.1396 | -0.28% | -0.32% | 1925/9420 |
| Relative Volume | -0.0446 | +0.0722 | -0.0400 | -0.32% | n/a | 11419/0 |
| d_Performance (Week) | +0.0427 | -0.1462 | +0.1316 | -0.35% | -0.31% | 3377/8089 |
| d_20-Day Simple Moving Average | +0.0426 | -0.2000 | +0.1723 | -0.38% | -0.30% | 2218/9349 |
| d_200-Day Simple Moving Average | +0.0420 | -0.1911 | +0.1479 | -0.32% | -0.31% | 2025/9533 |
| d_Short Ratio | -0.0304 | -0.0342 | -0.0555 | -0.47% | -0.25% | 3915/3307 |
| d_Relative Volume | -0.0296 | -0.0325 | +0.0346 | -0.35% | -0.30% | 5268/5969 |
| d_Sales Growth Quarter Over Quarter | +0.0281 | +0.0256 | +0.0094 | 3.19% | 0.11% | 6/8 |
| d_Price | +0.0273 | +0.0258 | -0.1020 | -0.28% | -0.32% | 1880/9370 |
| d_Sales Year Over Year TTM | +0.0238 | +0.0496 | -0.0069 | 3.14% | -0.28% | 7/7 |
| d_Insider Transactions | -0.0227 | -0.0040 | -0.0244 | -0.79% | 0.26% | 92/177 |
| d_Market Cap | +0.0219 | +0.1124 | -0.0753 | -0.40% | -0.48% | 1408/4333 |
| d_Short Float | +0.0214 | n/a | +0.0271 | n/a | -7.36% | 0/1 |
| d_Average Volume | +0.0201 | +0.0399 | +0.0426 | -0.28% | -0.37% | 5089/5977 |
| d_Analyst Recom | -0.0190 | -0.0295 | +0.0210 | -0.11% | -0.09% | 68/90 |
| d_Profit Margin | +0.0190 | +0.0565 | +0.0090 | 2.21% | -0.29% | 9/6 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 205 | -0.40% | 27.8% |
| true_ret>3% & UPTREND | 115 | -0.46% | 24.3% |
| true_ret>3% & MIXED | 91 | -0.19% | 28.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 204 | 1.20% | -3.11% |
| WASHED | 1805 | -0.66% | -0.53% |
