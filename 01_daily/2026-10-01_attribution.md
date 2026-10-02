# Factor attribution — signal 2026-10-01 → prediction day 2026-10-02

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-01** | Features/scores formed from this snapshot (and deltas vs **2026-09-30**). Only data on/before this date. |
| **Prediction day** | **2026-10-02** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-01 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-02 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11693** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0950**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.94% | 18.9% | 2371 |
| 2 | 0.32% | 7.8% | 2372 |
| 3 | 0.38% | 18.0% | 2383 |
| 4 | 0.50% | 18.7% | 2327 |
| 5 | 0.72% | 32.2% | 2240 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.1622 | +0.0389 | +0.2374 | 0.90% | 0.42% | 3718/7782 |
| upside_pct_lvl | -0.1429 | +0.2176 | -0.4010 | 0.45% | 0.62% | 4392/247 |
| d_Performance (Quarter) | +0.1425 | +0.1988 | -0.0220 | 0.63% | 0.50% | 5528/5544 |
| Relative Strength Index (14) | +0.1149 | +0.1370 | -0.2014 | 0.58% | n/a | 11587/0 |
| d_Performance (Month) | +0.0903 | +0.2157 | -0.0706 | 0.50% | 0.81% | 8157/3239 |
| d_Beta | -0.0620 | -0.0410 | -0.0898 | 0.87% | 0.69% | 2082/1021 |
| d_Average Volume | -0.0596 | -0.0691 | +0.0312 | 0.61% | 0.56% | 5268/5822 |
| d_Short Ratio | +0.0467 | +0.0598 | -0.0367 | 0.54% | 0.40% | 3896/3494 |
| d_Market Cap | +0.0415 | +0.0192 | +0.0745 | 0.51% | 0.83% | 2861/2832 |
| d_Price | +0.0385 | +0.0522 | +0.0680 | 0.53% | 0.69% | 6033/5092 |
| Institutional Transactions | +0.0353 | +0.0796 | -0.0660 | 0.34% | 1.34% | 3235/1813 |
| Performance (Week) | +0.0331 | -0.0809 | +0.1815 | 0.59% | 0.58% | 3313/8195 |
| d_Performance (YTD) | +0.0330 | +0.0500 | +0.0480 | 0.50% | 0.70% | 6116/5172 |
| d_Gross Margin | -0.0274 | -0.0215 | -0.0083 | -1.12% | 0.95% | 10/12 |
| true_ret | +0.0272 | +0.0429 | +0.0543 | 0.53% | 0.69% | 6033/5092 |
| d_Forward P/E | +0.0257 | +0.0994 | -0.0428 | 0.67% | 0.55% | 1789/1143 |
| d_Analyst Recom | +0.0226 | +0.0412 | -0.0482 | 0.25% | 0.39% | 40/56 |
| d_Sales Year Over Year TTM | -0.0209 | -0.0115 | -0.0106 | -0.90% | 1.21% | 10/10 |
| d_Profit Margin | +0.0203 | +0.0384 | -0.0027 | 1.49% | -1.48% | 11/9 |
| d_Short Float | +0.0201 | +0.0161 | +0.0305 | n/a | -3.86% | 0/3 |
| Short Float | +0.0170 | +0.1456 | -0.0979 | 0.67% | n/a | 5695/0 |
| d_50-Day Simple Moving Average | +0.0163 | +0.0584 | +0.0134 | 0.48% | 0.70% | 6350/5203 |
| d_20-Day Simple Moving Average | -0.0124 | +0.0301 | -0.0049 | 0.41% | 0.81% | 6804/4768 |
| d_Volatility (Month) | -0.0119 | -0.0120 | +0.0085 | 0.25% | 1.39% | 34/4 |
| d_Institutional Ownership | +0.0091 | -0.0183 | +0.0649 | -0.07% | 1.41% | 15/33 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 306 | -0.43% | 29.4% |
| true_ret>3% & UPTREND | 318 | 0.82% | 39.9% |
| true_ret>3% & MIXED | 190 | 1.00% | 36.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 186 | 0.26% | 1.74% |
| WASHED | 2315 | 0.71% | -0.38% |
