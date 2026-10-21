# Factor attribution — signal 2026-10-19 → prediction day 2026-10-21

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-19** | Features/scores formed from this snapshot (and deltas vs **2026-10-16**). Only data on/before this date. |
| **Prediction day** | **2026-10-21** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-19 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-21 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11741** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0326**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.63% | 33.6% | 2687 |
| 2 | 0.87% | 25.7% | 2181 |
| 3 | 0.81% | 24.8% | 2309 |
| 4 | 0.87% | 24.3% | 2374 |
| 5 | 1.67% | 48.2% | 2190 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | +0.1703 | +0.2830 | -0.1280 | 1.79% | n/a | 5659/0 |
| Performance (Week) | -0.1646 | -0.3421 | +0.2612 | 0.61% | 1.83% | 3875/7700 |
| d_Volatility (Month) | +0.1501 | +0.2899 | -0.1858 | 1.80% | 0.87% | 7512/2514 |
| d_Performance (Quarter) | -0.1391 | -0.2255 | +0.0513 | 0.83% | 1.70% | 3181/7963 |
| d_20-Day Simple Moving Average | +0.1186 | +0.1276 | +0.0149 | 1.40% | 1.46% | 6012/5590 |
| d_Performance (Week) | +0.1112 | +0.1622 | -0.0717 | 1.89% | 0.95% | 5978/5535 |
| d_Forward P/E | +0.0956 | +0.1816 | -0.0430 | 1.75% | 1.04% | 1138/1795 |
| d_Beta | +0.0876 | +0.2463 | -0.2348 | 2.89% | 0.76% | 3071/2068 |
| Relative Strength Index (14) | -0.0873 | -0.2438 | +0.2601 | 1.41% | n/a | 11655/0 |
| Performance (Month) | -0.0867 | -0.3121 | +0.3171 | 0.88% | 1.67% | 3589/7963 |
| d_50-Day Simple Moving Average | +0.0831 | +0.0608 | +0.0299 | 1.27% | 1.59% | 5759/5816 |
| true_ret | +0.0825 | +0.0214 | +0.1154 | 1.40% | 1.54% | 5068/6062 |
| d_Relative Strength Index (14) | +0.0824 | +0.0611 | -0.0151 | 1.37% | 1.52% | 5150/6142 |
| d_Performance (YTD) | +0.0813 | +0.0347 | +0.0668 | 1.39% | 1.54% | 5145/6131 |
| d_200-Day Simple Moving Average | +0.0771 | +0.0445 | +0.0488 | 1.34% | 1.52% | 5316/6235 |
| d_Price | +0.0736 | +0.0511 | +0.0045 | 1.40% | 1.54% | 5068/6062 |
| d_Market Cap | +0.0534 | +0.1437 | -0.0354 | 1.57% | 2.06% | 2322/3438 |
| d_Performance (Month) | +0.0423 | +0.0155 | +0.0682 | 1.12% | 1.89% | 6656/4775 |
| Institutional Transactions | +0.0406 | +0.1024 | -0.0761 | 2.20% | 1.80% | 3260/1788 |
| Relative Volume | +0.0370 | +0.0409 | +0.0252 | 1.43% | n/a | 11488/0 |
| d_Average Volume | -0.0340 | -0.0150 | -0.0116 | 1.62% | 1.25% | 5987/5040 |
| d_Short Ratio | +0.0189 | +0.0046 | -0.0140 | 1.24% | 1.24% | 3215/3851 |
| d_Relative Volume | -0.0179 | -0.0437 | -0.0187 | 1.18% | 1.64% | 4485/6843 |
| upside_pct_lvl | -0.0165 | +0.3184 | -0.4221 | 2.17% | 1.59% | 4360/270 |
| d_Institutional Ownership | -0.0155 | -0.0144 | +0.0383 | 1.40% | 1.46% | 1692/1734 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 493 | 2.06% | 53.8% |
| true_ret>3% & UPTREND | 162 | 2.36% | 55.6% |
| true_ret>3% & MIXED | 159 | 2.81% | 54.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 116 | -0.27% | -3.38% |
| WASHED | 1661 | 3.96% | 1.85% |
