# Factor attribution — signal 2026-11-18 → prediction day 2026-11-23

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-18** | Features/scores formed from this snapshot (and deltas vs **2026-11-17**). Only data on/before this date. |
| **Prediction day** | **2026-11-23** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-18 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-23 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11718** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0696**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.18% | 12.0% | 2482 |
| 2 | -1.20% | 6.9% | 2213 |
| 3 | 2.08% | 4.8% | 2337 |
| 4 | 2.39% | 10.1% | 2639 |
| 5 | -2.56% | 14.0% | 2047 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.2781 | -0.3941 | +0.3669 | 3.59% | 0.30% | 1495/10114 |
| Performance (Month) | +0.2253 | -0.2906 | +0.3145 | -0.77% | 1.41% | 3437/8124 |
| upside_pct_lvl | -0.2119 | +0.4950 | -0.4942 | 0.42% | -2.31% | 4385/239 |
| d_Performance (Week) | +0.1621 | -0.0767 | +0.1432 | -1.30% | 0.94% | 3558/7991 |
| Relative Strength Index (14) | +0.1573 | -0.2500 | +0.1055 | 0.74% | n/a | 11658/0 |
| Short Float | -0.1091 | +0.2818 | -0.1814 | 3.07% | n/a | 5603/0 |
| d_Volatility (Month) | -0.0858 | +0.1286 | -0.1558 | 0.21% | 0.73% | 5191/4308 |
| true_ret | +0.0777 | -0.0572 | +0.0737 | -1.65% | 0.70% | 4955/6115 |
| d_Relative Strength Index (14) | +0.0759 | -0.0652 | -0.0162 | -1.35% | 1.64% | 5104/6236 |
| d_Price | +0.0674 | -0.0502 | -0.0175 | -1.65% | 0.70% | 4955/6115 |
| d_Performance (Month) | +0.0635 | -0.1782 | +0.0659 | -0.38% | 0.76% | 3690/7750 |
| d_Performance (YTD) | +0.0629 | -0.0471 | +0.0261 | -1.47% | 1.03% | 5089/6198 |
| d_200-Day Simple Moving Average | +0.0541 | -0.0249 | +0.0146 | -1.37% | 1.71% | 5310/6232 |
| d_Beta | -0.0533 | +0.1777 | -0.0976 | 6.06% | -1.25% | 3243/2063 |
| d_Average Volume | +0.0442 | +0.0694 | +0.0072 | 1.71% | -1.70% | 6634/4422 |
| Relative Volume | -0.0366 | +0.1412 | -0.0544 | 0.27% | n/a | 11493/0 |
| d_Sales Growth Quarter Over Quarter | +0.0348 | +0.0258 | +0.0270 | 108.11% | -6.80% | 46/46 |
| d_Short Float | +0.0334 | -0.0238 | +0.0773 | -4.43% | 10.78% | 17/94 |
| d_50-Day Simple Moving Average | +0.0311 | +0.0024 | -0.0042 | -1.43% | 1.95% | 5796/5780 |
| d_Short Ratio | -0.0286 | -0.0862 | -0.0054 | -2.02% | 0.44% | 2593/4172 |
| d_Forward P/E | +0.0282 | -0.0630 | -0.0193 | -2.01% | -2.15% | 1389/1506 |
| d_Profit Margin | +0.0267 | +0.0249 | +0.0111 | 154.54% | 8.16% | 52/49 |
| Institutional Transactions | -0.0266 | +0.1314 | -0.1031 | 1.33% | 2.03% | 2990/2015 |
| d_Relative Volume | -0.0233 | +0.0051 | -0.0352 | -1.02% | 1.34% | 5255/6066 |
| d_EPS Surprise | +0.0192 | +0.0596 | +0.0183 | -0.73% | -5.46% | 15/23 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 462 | -1.69% | 18.8% |
| true_ret>3% & UPTREND | 224 | -4.12% | 21.9% |
| true_ret>3% & MIXED | 207 | -4.63% | 20.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 169 | -4.04% | -11.45% |
| WASHED | 2062 | 10.53% | -1.57% |
