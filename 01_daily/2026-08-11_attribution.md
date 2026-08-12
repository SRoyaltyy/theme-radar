# Factor attribution — signal 2026-08-11 → prediction day 2026-08-12

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-11** | Features/scores formed from this snapshot (and deltas vs **2026-08-10**). Only data on/before this date. |
| **Prediction day** | **2026-08-12** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-11 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-12 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11543** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.1007**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.02% | 20.7% | 2347 |
| 2 | 0.22% | 6.7% | 3055 |
| 3 | 0.24% | 5.8% | 1944 |
| 4 | 0.84% | 22.1% | 2049 |
| 5 | 0.70% | 31.6% | 2148 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | +0.1451 | +0.3108 | -0.0963 | 0.54% | -0.06% | 7758/3463 |
| d_Performance (Quarter) | -0.1257 | -0.0605 | -0.1314 | 0.03% | 0.53% | 5736/5009 |
| d_Performance (Week) | -0.1166 | -0.2647 | +0.0762 | -0.04% | 0.50% | 2858/8494 |
| Performance (Week) | -0.0858 | -0.0942 | -0.0455 | 0.06% | 0.71% | 6032/5301 |
| d_Beta | -0.0811 | -0.1217 | -0.0346 | -0.15% | 0.56% | 1463/1965 |
| Institutional Transactions | +0.0510 | +0.0578 | -0.0319 | 0.27% | 0.06% | 2521/2519 |
| Performance (Month) | -0.0492 | -0.0683 | +0.0620 | 0.20% | 0.61% | 6985/4304 |
| d_Price | +0.0423 | +0.0822 | -0.0179 | 0.47% | 0.29% | 5857/4933 |
| Relative Strength Index (14) | -0.0402 | -0.2182 | +0.1890 | 0.37% | n/a | 11436/0 |
| d_20-Day Simple Moving Average | +0.0333 | +0.1062 | -0.0859 | 0.51% | 0.23% | 5731/5661 |
| d_Performance (YTD) | +0.0302 | +0.0899 | -0.0426 | 0.46% | 0.29% | 5978/5046 |
| d_Insider Transactions | +0.0281 | -0.0104 | +0.0019 | 0.58% | 0.03% | 164/220 |
| d_Average Volume | -0.0248 | -0.0512 | -0.0292 | 0.26% | 0.48% | 5279/5704 |
| d_Analyst Recom | -0.0239 | +0.0218 | -0.0228 | 0.08% | 0.88% | 68/75 |
| upside_pct_lvl | -0.0238 | +0.3541 | -0.3412 | 0.25% | -0.24% | 4278/370 |
| true_ret | +0.0226 | +0.0903 | -0.0548 | 0.47% | 0.29% | 5857/4933 |
| d_Relative Volume | -0.0211 | -0.0327 | -0.0119 | 0.36% | 0.39% | 4530/6599 |
| d_50-Day Simple Moving Average | +0.0193 | +0.1196 | -0.0971 | 0.46% | 0.27% | 6070/5310 |
| d_Sales Growth Quarter Over Quarter | -0.0185 | -0.0232 | -0.0236 | 0.02% | 0.74% | 89/103 |
| d_Forward P/E | -0.0172 | -0.0399 | -0.0374 | 0.20% | 0.35% | 1665/1316 |
| d_Sales Year Over Year TTM | -0.0154 | -0.0161 | -0.0276 | -0.04% | 0.25% | 92/95 |
| d_Gross Margin | -0.0148 | -0.0184 | +0.0049 | 0.31% | 0.21% | 90/103 |
| d_Short Float | -0.0142 | +0.0038 | -0.0106 | -0.73% | -0.14% | 48/36 |
| d_Market Cap | -0.0114 | -0.0268 | +0.0102 | 0.04% | 0.32% | 3183/2513 |
| d_Institutional Ownership | -0.0106 | -0.0483 | +0.0415 | 0.01% | 0.26% | 182/349 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 409 | 2.24% | 40.6% |
| true_ret>3% & UPTREND | 300 | -0.47% | 27.0% |
| true_ret>3% & MIXED | 257 | 0.02% | 35.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 313 | -0.72% | -0.59% |
| WASHED | 558 | 1.01% | 3.71% |
