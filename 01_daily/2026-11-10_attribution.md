# Factor attribution — signal 2026-11-10 → prediction day 2026-11-12

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-10** | Features/scores formed from this snapshot (and deltas vs **2026-11-09**). Only data on/before this date. |
| **Prediction day** | **2026-11-12** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-10 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-12 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11733** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0286**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.33% | 26.1% | 2614 |
| 2 | 0.14% | 21.5% | 2154 |
| 3 | 0.36% | 8.8% | 2393 |
| 4 | -0.25% | 10.2% | 2462 |
| 5 | -0.79% | 24.0% | 2110 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Beta | -0.3267 | -0.2370 | -0.1770 | 0.39% | 1.35% | 4134/2681 |
| Performance (Week) | -0.2831 | -0.4714 | -0.0225 | -1.32% | 2.07% | 5580/5967 |
| d_20-Day Simple Moving Average | +0.2745 | +0.0325 | +0.2803 | 0.45% | 0.42% | 3409/8209 |
| Performance (Month) | -0.2245 | -0.5443 | +0.1834 | -1.16% | 1.66% | 5070/6507 |
| Relative Strength Index (14) | -0.2086 | -0.4561 | +0.2191 | 0.42% | n/a | 11684/0 |
| d_Relative Strength Index (14) | +0.1898 | +0.0604 | -0.0846 | -0.24% | 0.69% | 3139/8272 |
| d_Performance (Month) | +0.1589 | +0.1152 | +0.0833 | 0.61% | 0.33% | 4067/7404 |
| d_50-Day Simple Moving Average | +0.1564 | -0.1296 | +0.2444 | -0.11% | 0.65% | 3424/8185 |
| Short Float | -0.1333 | +0.2237 | -0.1906 | 0.64% | n/a | 5625/0 |
| true_ret | +0.1286 | -0.2244 | +0.2894 | -0.21% | 0.71% | 3066/8223 |
| d_200-Day Simple Moving Average | +0.1260 | -0.1666 | +0.2247 | -0.23% | 0.67% | 3161/8440 |
| d_Performance (YTD) | +0.1169 | -0.1800 | +0.2184 | -0.21% | 0.70% | 3124/8266 |
| d_Forward P/E | +0.1052 | -0.1613 | +0.2110 | -0.27% | -0.71% | 1192/1725 |
| d_Market Cap | +0.0996 | -0.0698 | +0.0651 | -0.60% | 1.48% | 2049/3697 |
| upside_pct_lvl | -0.0775 | +0.4933 | -0.4636 | 1.14% | -1.18% | 4322/312 |
| d_Price | +0.0704 | -0.0796 | +0.0549 | -0.21% | 0.71% | 3066/8223 |
| d_Institutional Ownership | +0.0580 | -0.0356 | +0.0881 | -0.36% | -1.86% | 383/561 |
| Institutional Transactions | -0.0427 | +0.0689 | -0.1032 | 0.23% | 1.38% | 3099/1917 |
| d_Sales Growth Quarter Over Quarter | +0.0326 | +0.0543 | -0.0103 | -0.41% | -2.14% | 110/131 |
| d_EPS Surprise | -0.0305 | -0.0089 | -0.0351 | -2.00% | -0.78% | 107/112 |
| d_Short Float | +0.0272 | n/a | +0.0430 | -1.75% | -9.63% | 2/4 |
| d_Performance (Quarter) | +0.0234 | -0.2233 | +0.1670 | 0.02% | 0.57% | 3042/8204 |
| d_Analyst Recom | -0.0226 | -0.0412 | +0.0349 | -1.05% | 0.50% | 118/87 |
| d_Volatility (Month) | +0.0206 | +0.3659 | -0.2913 | 0.28% | 1.41% | 7779/2244 |
| d_Sales Year Over Year TTM | +0.0199 | +0.0413 | -0.0067 | -0.77% | -1.61% | 116/123 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 275 | -1.30% | 33.1% |
| true_ret>3% & UPTREND | 169 | -2.89% | 24.9% |
| true_ret>3% & MIXED | 140 | -1.85% | 30.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 276 | -3.08% | -4.48% |
| WASHED | 1536 | 7.47% | 2.15% |
