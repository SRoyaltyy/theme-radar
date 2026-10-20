# Factor attribution — signal 2026-10-19 → prediction day 2026-10-20

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-19** | Features/scores formed from this snapshot (and deltas vs **2026-10-16**). Only data on/before this date. |
| **Prediction day** | **2026-10-20** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-19 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-20 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11741** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0458**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.82% | 26.9% | 2687 |
| 2 | 0.48% | 16.6% | 2181 |
| 3 | 0.47% | 17.4% | 2309 |
| 4 | 0.65% | 20.2% | 2374 |
| 5 | 1.27% | 42.4% | 2190 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | +0.2368 | +0.2982 | -0.1104 | 1.55% | n/a | 5659/0 |
| d_Price | -0.1338 | -0.0750 | +0.0436 | 0.66% | 1.30% | 5068/6062 |
| d_Relative Strength Index (14) | -0.1242 | -0.0376 | +0.0713 | 0.66% | 1.28% | 5150/6142 |
| d_Performance (YTD) | -0.1147 | -0.0961 | +0.0334 | 0.67% | 1.30% | 5145/6131 |
| d_200-Day Simple Moving Average | -0.1145 | -0.0857 | +0.0022 | 0.65% | 1.27% | 5316/6235 |
| d_Performance (Week) | -0.1084 | +0.0061 | -0.1567 | 1.08% | 0.88% | 5978/5535 |
| true_ret | -0.1078 | -0.1106 | +0.0181 | 0.66% | 1.30% | 5068/6062 |
| d_50-Day Simple Moving Average | -0.1046 | -0.0640 | -0.0439 | 0.64% | 1.32% | 5759/5816 |
| d_20-Day Simple Moving Average | -0.0987 | -0.0240 | -0.0837 | 0.66% | 1.33% | 6012/5590 |
| d_Beta | -0.0741 | +0.1546 | -0.2626 | 1.79% | 1.05% | 3071/2068 |
| Performance (Week) | +0.0721 | -0.1697 | +0.3128 | 0.81% | 1.06% | 3875/7700 |
| d_Volatility (Month) | +0.0680 | +0.2047 | -0.1664 | 1.22% | 0.61% | 7512/2514 |
| Relative Volume | +0.0520 | +0.0565 | +0.0194 | 0.98% | n/a | 11488/0 |
| d_Forward P/E | -0.0485 | +0.0572 | -0.1092 | 1.09% | 1.17% | 1138/1795 |
| Relative Strength Index (14) | +0.0370 | -0.1706 | +0.2381 | 0.97% | n/a | 11655/0 |
| d_Market Cap | -0.0206 | +0.1225 | -0.0394 | 1.15% | 1.83% | 2322/3438 |
| d_Performance (Month) | +0.0202 | +0.0152 | +0.0270 | 0.72% | 1.36% | 6656/4775 |
| upside_pct_lvl | -0.0196 | +0.3219 | -0.4334 | 2.00% | 1.13% | 4360/270 |
| d_Institutional Transactions | -0.0191 | +0.0061 | +0.0042 | 1.16% | 1.57% | 1907/2190 |
| d_Sales Growth Quarter Over Quarter | -0.0180 | -0.0200 | +0.0513 | 2.05% | 2.27% | 8/10 |
| d_Short Float | -0.0173 | -0.0495 | +0.0837 | 0.89% | 1.21% | 143/238 |
| d_Insider Transactions | -0.0170 | -0.0069 | -0.0063 | 0.96% | 0.97% | 338/317 |
| d_Relative Volume | -0.0166 | -0.0303 | +0.0038 | 0.70% | 1.20% | 4485/6843 |
| Institutional Transactions | +0.0156 | +0.1000 | -0.1190 | 1.88% | 1.56% | 3260/1788 |
| d_Total Debt/Equity | +0.0131 | -0.0008 | +0.0289 | 1.78% | 0.97% | 7/8 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 493 | 0.82% | 41.0% |
| true_ret>3% & UPTREND | 162 | 1.45% | 43.8% |
| true_ret>3% & MIXED | 159 | 1.42% | 48.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 116 | 1.11% | -0.50% |
| WASHED | 1661 | 2.51% | 1.02% |
