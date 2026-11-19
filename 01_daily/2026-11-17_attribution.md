# Factor attribution — signal 2026-11-17 → prediction day 2026-11-18

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-17** | Features/scores formed from this snapshot (and deltas vs **2026-11-16**). Only data on/before this date. |
| **Prediction day** | **2026-11-18** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-17 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-18 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11736** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0020**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.56% | 14.7% | 2609 |
| 2 | 2.45% | 9.3% | 2160 |
| 3 | -0.40% | 9.0% | 2390 |
| 4 | -0.21% | 15.3% | 2239 |
| 5 | -0.39% | 19.4% | 2338 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.1488 | -0.1647 | +0.3730 | 0.08% | 0.16% | 3921/7663 |
| Relative Strength Index (14) | +0.1409 | -0.0134 | +0.2055 | 0.13% | n/a | 11675/0 |
| upside_pct_lvl | -0.1369 | +0.3416 | -0.5074 | 0.53% | 0.46% | 4398/226 |
| d_Beta | -0.1248 | +0.0282 | -0.2280 | 1.03% | -0.10% | 3350/3088 |
| Short Float | +0.0992 | +0.2153 | -0.1706 | 0.65% | n/a | 5614/0 |
| d_Performance (Quarter) | +0.0961 | -0.1323 | +0.1872 | -0.07% | 0.20% | 2532/8719 |
| Performance (Week) | +0.0809 | -0.3223 | +0.3267 | -0.23% | 0.19% | 1725/9862 |
| d_Forward P/E | -0.0688 | -0.0243 | -0.1182 | -0.36% | -0.04% | 602/2313 |
| true_ret | +0.0675 | -0.1892 | +0.1547 | -0.28% | 0.27% | 2322/8893 |
| d_Total Debt/Equity | -0.0585 | -0.0384 | -0.0341 | -2.63% | 2.56% | 70/51 |
| d_Target Price | +0.0481 | -0.0237 | +0.0453 | -0.16% | -1.22% | 197/273 |
| d_Institutional Ownership | +0.0395 | +0.0104 | +0.0561 | -0.26% | 1.93% | 2874/2472 |
| d_Performance (Month) | -0.0386 | -0.1514 | -0.0005 | 0.12% | 0.14% | 3441/8073 |
| d_200-Day Simple Moving Average | +0.0385 | -0.1301 | +0.0316 | -0.31% | 0.27% | 2632/8963 |
| d_Performance (YTD) | +0.0367 | -0.1198 | +0.0040 | -0.24% | 0.26% | 2381/8959 |
| d_Market Cap | -0.0275 | +0.1555 | -0.2229 | -0.40% | 0.96% | 1405/4311 |
| Institutional Transactions | -0.0259 | +0.0815 | -0.1065 | 0.90% | 0.60% | 2992/2019 |
| d_50-Day Simple Moving Average | +0.0239 | -0.1314 | +0.0331 | 0.26% | 0.09% | 2965/8649 |
| d_Relative Volume | +0.0207 | -0.0327 | +0.0411 | -0.34% | 0.66% | 5962/5362 |
| d_Relative Strength Index (14) | +0.0174 | +0.1329 | -0.2495 | -0.24% | 0.25% | 2423/8962 |
| d_Gross Margin | -0.0167 | -0.0407 | +0.0126 | -0.06% | -0.43% | 70/79 |
| d_20-Day Simple Moving Average | +0.0152 | -0.1240 | +0.0222 | 0.22% | 0.10% | 3097/8501 |
| d_Average Volume | -0.0138 | +0.0423 | -0.0462 | 0.45% | -0.37% | 7019/3986 |
| d_Short Float | +0.0129 | -0.0254 | +0.0602 | -1.02% | -0.44% | 24/81 |
| d_Insider Transactions | +0.0123 | +0.0213 | -0.0196 | 0.52% | -0.98% | 137/202 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 350 | -0.83% | 29.7% |
| true_ret>3% & UPTREND | 70 | 0.45% | 40.0% |
| true_ret>3% & MIXED | 88 | 0.19% | 43.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 167 | 1.40% | 2.92% |
| WASHED | 1834 | 1.85% | -1.37% |
