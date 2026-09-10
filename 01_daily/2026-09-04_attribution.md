# Factor attribution — signal 2026-09-04 → prediction day 2026-09-10

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-04** | Features/scores formed from this snapshot (and deltas vs **2026-09-03**). Only data on/before this date. |
| **Prediction day** | **2026-09-10** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-04 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-10 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11589** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.1272**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.30% | 15.1% | 2337 |
| 2 | -0.54% | 6.1% | 2860 |
| 3 | -0.81% | 5.3% | 1765 |
| 4 | -2.14% | 7.0% | 2311 |
| 5 | -1.35% | 12.0% | 2316 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | -0.2564 | +0.1845 | -0.2709 | 0.12% | n/a | 5673/0 |
| d_Performance (Quarter) | -0.1962 | +0.1481 | -0.2631 | -0.88% | 2.22% | 8555/2362 |
| d_Performance (Week) | -0.1471 | +0.0583 | -0.1810 | -1.05% | 1.18% | 7413/3987 |
| upside_pct_lvl | -0.1432 | +0.3569 | -0.3197 | 0.09% | -2.72% | 4307/335 |
| d_Performance (Month) | -0.1024 | -0.0358 | -0.0775 | -0.98% | 0.69% | 6378/4872 |
| Performance (Week) | +0.0705 | +0.0576 | +0.0560 | -1.12% | 0.61% | 5732/5639 |
| d_20-Day Simple Moving Average | -0.0576 | +0.0362 | -0.0495 | -0.49% | -0.05% | 5849/5593 |
| Relative Volume | -0.0538 | +0.0675 | -0.0647 | -0.28% | n/a | 11307/0 |
| d_Market Cap | -0.0485 | +0.0200 | -0.0379 | -1.24% | 0.62% | 2960/2707 |
| d_EPS Surprise | +0.0423 | +0.0304 | +0.0399 | 0.44% | -3.78% | 19/16 |
| d_Forward P/E | -0.0411 | +0.0085 | -0.0425 | -2.26% | -2.68% | 1533/1400 |
| Relative Strength Index (14) | +0.0389 | -0.1739 | +0.0405 | -0.27% | n/a | 11490/0 |
| d_Short Ratio | -0.0386 | -0.0128 | -0.0359 | -1.62% | 0.83% | 4291/2675 |
| d_Average Volume | +0.0380 | +0.0111 | +0.0485 | 1.42% | -1.36% | 4505/6534 |
| d_Relative Strength Index (14) | -0.0367 | +0.0302 | -0.0526 | -0.96% | 0.47% | 5346/5761 |
| d_200-Day Simple Moving Average | -0.0310 | +0.0526 | -0.0291 | -0.62% | 0.06% | 5415/6021 |
| d_Short Float | -0.0290 | -0.0387 | -0.0281 | -6.23% | -3.96% | 19/28 |
| d_50-Day Simple Moving Average | -0.0278 | +0.0563 | -0.0236 | -0.55% | -0.02% | 5551/5897 |
| d_Performance (YTD) | -0.0261 | +0.0282 | -0.0157 | -0.96% | 0.47% | 5340/5755 |
| true_ret | -0.0260 | +0.0241 | -0.0137 | -1.27% | 0.20% | 5234/5644 |
| d_Target Price | +0.0181 | -0.0333 | +0.0112 | -2.36% | -2.32% | 161/87 |
| d_Price | -0.0159 | +0.0502 | -0.0196 | -1.27% | 0.20% | 5234/5644 |
| d_Profit Margin | +0.0156 | +0.0485 | -0.0029 | -2.51% | -5.69% | 30/10 |
| d_Analyst Recom | +0.0147 | -0.0137 | +0.0070 | -2.00% | -2.61% | 68/50 |
| d_Volatility (Month) | -0.0145 | -0.0120 | +0.0098 | 1.33% | -1.21% | 4251/5003 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 366 | 6.45% | 22.4% |
| true_ret>3% & UPTREND | 279 | -0.48% | 17.9% |
| true_ret>3% & MIXED | 235 | -2.12% | 21.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 242 | -4.10% | -6.60% |
| WASHED | 679 | 11.78% | 13.08% |
