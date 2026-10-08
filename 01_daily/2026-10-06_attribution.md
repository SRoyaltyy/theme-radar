# Factor attribution — signal 2026-10-06 → prediction day 2026-10-08

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-06** | Features/scores formed from this snapshot (and deltas vs **2026-10-05**). Only data on/before this date. |
| **Prediction day** | **2026-10-08** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-06 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-08 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11695** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0822**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.76% | 16.6% | 2386 |
| 2 | -0.98% | 6.5% | 2512 |
| 3 | -1.19% | 9.4% | 2331 |
| 4 | -0.93% | 9.5% | 2237 |
| 5 | -2.40% | 18.2% | 2229 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2120 | +0.2738 | -0.3809 | -1.46% | -1.12% | 4369/265 |
| Relative Strength Index (14) | -0.1695 | +0.0944 | -0.0072 | -1.24% | n/a | 11604/0 |
| Institutional Transactions | -0.1068 | +0.0223 | -0.1280 | -1.16% | -0.94% | 3243/1803 |
| d_Forward P/E | -0.1037 | -0.1265 | -0.0768 | -0.93% | -0.45% | 1599/1334 |
| Performance (Month) | -0.0969 | -0.3017 | +0.0237 | -2.30% | -0.75% | 3631/7878 |
| Performance (Week) | -0.0853 | -0.0256 | -0.0306 | -1.48% | -0.89% | 6974/4540 |
| d_Performance (Month) | +0.0787 | +0.0136 | +0.1025 | -1.00% | -1.62% | 6843/4562 |
| d_Relative Strength Index (14) | +0.0748 | -0.2906 | +0.2482 | -1.19% | -1.34% | 7123/4163 |
| d_Volatility (Month) | +0.0719 | -0.0055 | +0.1134 | -1.22% | -1.53% | 5073/4482 |
| d_Average Volume | +0.0535 | -0.1452 | +0.1515 | -1.30% | -1.20% | 4277/7011 |
| d_Relative Volume | -0.0521 | -0.0311 | -0.0314 | -1.34% | -1.21% | 4990/6295 |
| d_Institutional Ownership | +0.0488 | -0.0058 | +0.0380 | 0.78% | -5.93% | 5/20 |
| d_Performance (Quarter) | -0.0465 | -0.0282 | -0.0149 | -1.15% | -1.36% | 7948/3159 |
| true_ret | -0.0362 | -0.0937 | +0.0407 | -1.20% | -1.33% | 7068/4084 |
| d_Performance (YTD) | -0.0326 | -0.1000 | +0.0579 | -1.20% | -1.32% | 7133/4168 |
| d_200-Day Simple Moving Average | -0.0317 | -0.0731 | +0.0356 | -1.20% | -1.30% | 7268/4294 |
| d_Short Ratio | -0.0314 | +0.0451 | -0.0365 | -1.45% | -1.17% | 4086/2863 |
| d_Market Cap | -0.0240 | -0.1074 | +0.0368 | -1.01% | -0.82% | 2945/2749 |
| d_Analyst Recom | -0.0195 | +0.0095 | +0.0039 | -0.92% | -0.48% | 74/84 |
| d_20-Day Simple Moving Average | -0.0195 | -0.0329 | +0.0173 | -1.16% | -1.42% | 7770/3819 |
| d_Gross Margin | +0.0186 | +0.0201 | +0.0438 | 1.92% | -5.85% | 1/4 |
| Relative Volume | -0.0174 | -0.0451 | -0.0115 | -1.27% | n/a | 11430/0 |
| d_Profit Margin | -0.0150 | -0.0091 | -0.0277 | -4.29% | 1.92% | 2/1 |
| Short Float | -0.0149 | +0.2333 | -0.1845 | -0.94% | n/a | 5690/0 |
| d_Target Price | -0.0145 | +0.0249 | -0.0450 | -0.56% | -0.67% | 211/350 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 376 | -4.58% | 18.1% |
| true_ret>3% & UPTREND | 208 | -6.01% | 13.5% |
| true_ret>3% & MIXED | 138 | -3.69% | 23.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 237 | -5.36% | -8.09% |
| WASHED | 1505 | -0.69% | -1.20% |
