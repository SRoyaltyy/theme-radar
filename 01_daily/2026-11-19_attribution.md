# Factor attribution — signal 2026-11-19 → prediction day 2026-11-24

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-19** | Features/scores formed from this snapshot (and deltas vs **2026-11-18**). Only data on/before this date. |
| **Prediction day** | **2026-11-24** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-19 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-24 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11721** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0898**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.50% | 12.7% | 3059 |
| 2 | 7.55% | 22.6% | 1662 |
| 3 | 4.47% | 26.4% | 2346 |
| 4 | -0.06% | 17.3% | 2365 |
| 5 | 2.07% | 29.0% | 2289 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.3214 | -0.1107 | +0.4924 | 0.53% | 3.90% | 2897/8680 |
| Performance (Week) | +0.2323 | -0.2966 | +0.4700 | 3.45% | 2.95% | 1738/9854 |
| upside_pct_lvl | -0.2138 | +0.4553 | -0.5234 | 5.14% | 0.33% | 4439/189 |
| d_Volatility (Month) | -0.1978 | +0.1948 | -0.3843 | 2.91% | 3.35% | 8393/1942 |
| Relative Strength Index (14) | +0.1974 | +0.0476 | +0.0777 | 3.03% | n/a | 11662/0 |
| d_Relative Strength Index (14) | -0.1972 | +0.0687 | -0.2835 | 1.41% | 3.01% | 1913/9447 |
| d_Performance (Month) | +0.1370 | -0.1474 | +0.2658 | 5.49% | 2.51% | 2235/9240 |
| d_Market Cap | -0.1176 | +0.1211 | -0.1852 | 10.43% | 5.83% | 1049/4677 |
| d_Price | -0.0886 | -0.0493 | -0.1567 | 0.30% | 2.84% | 1828/9409 |
| true_ret | +0.0665 | -0.2760 | +0.2782 | 0.30% | 2.84% | 1828/9409 |
| Short Float | +0.0663 | +0.3386 | -0.2141 | 7.61% | n/a | 5600/0 |
| d_Beta | -0.0649 | +0.0430 | -0.0620 | 12.26% | 0.60% | 2742/2393 |
| d_Target Price | +0.0619 | +0.0240 | -0.0043 | 1.23% | 9.01% | 175/222 |
| d_Forward P/E | -0.0603 | -0.1920 | +0.0874 | -0.61% | 0.10% | 316/2599 |
| d_Short Ratio | -0.0590 | -0.1036 | -0.0149 | -0.75% | 0.62% | 2715/4100 |
| d_Average Volume | +0.0556 | +0.0961 | -0.0011 | 5.07% | -0.29% | 6475/4563 |
| d_Institutional Ownership | +0.0530 | -0.0563 | +0.0499 | -0.09% | 25.42% | 1015/500 |
| d_Analyst Recom | +0.0437 | -0.0128 | +0.0536 | 1.14% | 0.32% | 401/188 |
| d_50-Day Simple Moving Average | -0.0422 | -0.2355 | +0.1053 | 1.85% | 2.89% | 2304/9301 |
| d_200-Day Simple Moving Average | -0.0395 | -0.2097 | +0.0621 | 1.46% | 2.97% | 2128/9460 |
| Institutional Transactions | -0.0395 | +0.0936 | -0.1385 | 6.00% | 6.74% | 2990/2014 |
| d_Relative Volume | -0.0339 | -0.1083 | -0.0051 | 1.72% | 4.15% | 6580/4776 |
| d_Performance (YTD) | -0.0327 | -0.1811 | +0.0266 | 1.50% | 2.98% | 1892/9453 |
| d_Performance (Week) | -0.0287 | +0.0043 | -0.0918 | 3.76% | 2.04% | 4386/7189 |
| d_Total Debt/Equity | +0.0266 | -0.0029 | +0.0207 | -0.08% | -3.95% | 23/21 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 267 | 4.80% | 28.1% |
| true_ret>3% & UPTREND | 103 | -3.35% | 25.2% |
| true_ret>3% & MIXED | 86 | -0.21% | 33.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 153 | -1.92% | -5.57% |
| WASHED | 2708 | 11.57% | 7.02% |
