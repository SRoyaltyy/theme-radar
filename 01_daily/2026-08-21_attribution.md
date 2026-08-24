# Factor attribution — signal 2026-08-21 → prediction day 2026-08-24

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-21** | Features/scores formed from this snapshot (and deltas vs **2026-08-20**). Only data on/before this date. |
| **Prediction day** | **2026-08-24** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-21 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-24 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11602** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0802**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.34% | 13.9% | 2352 |
| 2 | -0.27% | 6.4% | 2308 |
| 3 | 0.02% | 10.0% | 2351 |
| 4 | 0.97% | 8.7% | 2775 |
| 5 | 2.59% | 17.1% | 1816 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.2081 | +0.0650 | +0.2240 | 0.91% | 0.88% | 4210/7175 |
| upside_pct_lvl | -0.1860 | +0.3030 | -0.3954 | 1.39% | -0.10% | 4290/356 |
| d_50-Day Simple Moving Average | -0.1245 | +0.1250 | -0.1859 | 0.82% | 0.98% | 7788/3672 |
| d_20-Day Simple Moving Average | -0.1014 | +0.1154 | -0.1494 | 1.01% | 0.60% | 7560/3886 |
| true_ret | -0.1011 | +0.1176 | -0.1344 | 0.61% | 0.97% | 7670/3362 |
| d_200-Day Simple Moving Average | -0.0971 | +0.1331 | -0.1317 | 0.98% | 0.64% | 7869/3586 |
| d_Performance (YTD) | -0.0960 | +0.1046 | -0.0940 | 0.62% | 1.56% | 7737/3445 |
| Relative Strength Index (14) | +0.0927 | -0.0042 | +0.2850 | 0.89% | n/a | 11460/0 |
| Short Float | -0.0872 | +0.1049 | -0.2117 | 1.28% | n/a | 5690/0 |
| Institutional Transactions | -0.0847 | -0.0036 | -0.0879 | 1.89% | 0.93% | 2690/2352 |
| d_Price | -0.0765 | +0.0599 | +0.0600 | 0.61% | 0.97% | 7670/3362 |
| d_Relative Strength Index (14) | -0.0733 | +0.0549 | +0.1569 | 0.63% | 1.19% | 7675/3435 |
| Relative Volume | +0.0715 | +0.1420 | -0.0311 | 0.88% | n/a | 11334/0 |
| d_Performance (Month) | -0.0634 | +0.1905 | -0.1305 | 0.84% | 1.15% | 8786/2495 |
| d_Forward P/E | -0.0532 | +0.0488 | -0.0452 | 0.15% | -0.28% | 1952/973 |
| Performance (Month) | +0.0290 | +0.1028 | +0.0443 | 0.65% | 1.47% | 7841/3514 |
| d_Average Volume | +0.0227 | +0.0497 | -0.0109 | 2.56% | -0.31% | 4754/6280 |
| d_Analyst Recom | +0.0210 | -0.0114 | +0.0307 | -0.25% | -0.74% | 76/103 |
| d_Market Cap | -0.0203 | -0.0262 | +0.0289 | 0.87% | 1.09% | 3583/2122 |
| d_Short Ratio | -0.0189 | -0.0262 | +0.0144 | -0.57% | 2.89% | 3937/2836 |
| d_Relative Volume | +0.0185 | +0.0543 | +0.0050 | 0.46% | 1.33% | 5320/5847 |
| d_EPS Surprise | -0.0169 | +0.0159 | -0.0344 | 1.14% | 2.08% | 11/13 |
| d_Target Price | +0.0150 | -0.0206 | +0.0258 | -0.14% | -0.34% | 235/135 |
| d_Institutional Ownership | -0.0143 | +0.0179 | -0.0154 | -0.83% | -0.00% | 394/1182 |
| d_Total Debt/Equity | -0.0114 | +0.0059 | -0.0020 | 0.24% | -0.37% | 21/21 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 404 | 8.32% | 19.8% |
| true_ret>3% & UPTREND | 517 | -0.82% | 26.7% |
| true_ret>3% & MIXED | 434 | 5.90% | 28.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 471 | 6.18% | 21.06% |
| WASHED | 521 | 11.43% | 18.65% |
