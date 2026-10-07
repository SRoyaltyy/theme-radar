# Factor attribution — signal 2026-10-06 → prediction day 2026-10-07

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-06** | Features/scores formed from this snapshot (and deltas vs **2026-10-05**). Only data on/before this date. |
| **Prediction day** | **2026-10-07** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-06 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-07 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11695** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0979**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.54% | 12.3% | 2386 |
| 2 | -0.73% | 3.9% | 2512 |
| 3 | -0.85% | 4.2% | 2331 |
| 4 | -0.77% | 4.1% | 2237 |
| 5 | -1.62% | 10.1% | 2229 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.1550 | -0.0476 | -0.1350 | -0.97% | -0.70% | 7948/3159 |
| d_20-Day Simple Moving Average | -0.0849 | -0.0718 | -0.0203 | -0.90% | -0.91% | 7770/3819 |
| Performance (Week) | -0.0805 | -0.1522 | +0.0316 | -1.01% | -0.73% | 6974/4540 |
| Short Float | -0.0715 | +0.1193 | -0.1405 | -0.89% | n/a | 5690/0 |
| d_Performance (Week) | -0.0667 | -0.0277 | -0.0168 | -0.89% | -0.94% | 7663/3822 |
| d_Forward P/E | -0.0650 | -0.0840 | -0.0480 | -1.17% | -0.98% | 1599/1334 |
| Relative Volume | -0.0640 | -0.0837 | -0.0447 | -0.91% | n/a | 11430/0 |
| Institutional Transactions | -0.0638 | +0.0485 | -0.0904 | -0.91% | -0.78% | 3243/1803 |
| true_ret | -0.0583 | -0.1402 | +0.0471 | -0.91% | -0.93% | 7068/4084 |
| Performance (Month) | +0.0568 | -0.2812 | +0.1861 | -1.07% | -0.81% | 3631/7878 |
| d_Target Price | +0.0525 | +0.0335 | -0.0011 | -0.72% | -1.40% | 211/350 |
| upside_pct_lvl | -0.0519 | +0.3764 | -0.2928 | -1.14% | -0.98% | 4369/265 |
| d_200-Day Simple Moving Average | -0.0509 | -0.1017 | +0.0455 | -0.89% | -0.91% | 7268/4294 |
| d_Performance (YTD) | -0.0504 | -0.1389 | +0.0722 | -0.89% | -0.95% | 7133/4168 |
| d_50-Day Simple Moving Average | -0.0504 | -0.0819 | +0.0336 | -0.87% | -0.95% | 7362/4215 |
| d_Relative Strength Index (14) | +0.0483 | -0.2412 | +0.2644 | -0.89% | -0.93% | 7123/4163 |
| d_Market Cap | -0.0435 | -0.0871 | +0.0169 | -0.99% | -0.80% | 2945/2749 |
| d_Price | -0.0274 | -0.1717 | +0.1372 | -0.91% | -0.93% | 7068/4084 |
| d_Analyst Recom | -0.0219 | +0.0560 | -0.0308 | -1.47% | -1.12% | 74/84 |
| d_Gross Margin | +0.0177 | +0.0542 | +0.0013 | 2.77% | -1.99% | 1/4 |
| Relative Strength Index (14) | -0.0174 | -0.0462 | +0.0695 | -0.89% | n/a | 11604/0 |
| d_Institutional Ownership | +0.0157 | -0.0200 | +0.0325 | 0.20% | -2.03% | 5/20 |
| d_Short Float | +0.0133 | +0.0055 | +0.0021 | -0.54% | -1.21% | 16/19 |
| d_Profit Margin | -0.0130 | -0.0528 | -0.0068 | -1.13% | 2.77% | 2/1 |
| d_Sales Growth Quarter Over Quarter | +0.0108 | +0.0543 | +0.0132 | 0.24% | -2.70% | 2/2 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 376 | -2.70% | 16.0% |
| true_ret>3% & UPTREND | 208 | -2.23% | 11.1% |
| true_ret>3% & MIXED | 138 | -1.46% | 21.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 237 | -1.77% | -1.71% |
| WASHED | 1505 | -0.34% | -0.36% |
