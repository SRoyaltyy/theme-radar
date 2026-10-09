# Factor attribution — signal 2026-10-06 → prediction day 2026-10-09

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-06** | Features/scores formed from this snapshot (and deltas vs **2026-10-05**). Only data on/before this date. |
| **Prediction day** | **2026-10-09** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-06 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-09 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11694** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0286**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.44% | 20.2% | 2385 |
| 2 | -0.75% | 9.3% | 2512 |
| 3 | -0.89% | 11.3% | 2331 |
| 4 | -0.50% | 12.3% | 2237 |
| 5 | -1.75% | 24.6% | 2229 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.1819 | +0.2523 | -0.3703 | -1.28% | -0.27% | 4369/265 |
| d_Performance (Month) | +0.1424 | +0.0458 | +0.1399 | -0.58% | -1.28% | 6843/4561 |
| Relative Strength Index (14) | -0.0948 | +0.0119 | +0.0586 | -0.86% | n/a | 11603/0 |
| d_Relative Strength Index (14) | +0.0868 | -0.3185 | +0.2236 | -0.79% | -0.96% | 7123/4162 |
| d_Forward P/E | -0.0789 | -0.0687 | -0.0703 | -0.64% | -0.28% | 1599/1334 |
| Institutional Transactions | -0.0746 | +0.0439 | -0.1178 | -0.93% | -0.58% | 3243/1802 |
| d_Volatility (Month) | +0.0650 | +0.0120 | +0.0872 | -0.78% | -1.20% | 5072/4482 |
| Performance (Month) | -0.0528 | -0.2894 | +0.0899 | -1.63% | -0.50% | 3631/7877 |
| d_Average Volume | +0.0520 | -0.1293 | +0.1433 | -0.95% | -0.81% | 4277/7010 |
| d_Price | +0.0406 | -0.1353 | +0.1543 | -0.78% | -0.95% | 7068/4083 |
| d_Institutional Ownership | +0.0396 | +0.0217 | +0.0506 | 1.01% | -6.40% | 5/20 |
| d_Insider Transactions | -0.0330 | -0.0143 | +0.0087 | -1.51% | -0.79% | 47/148 |
| d_Gross Margin | +0.0307 | -0.0111 | +0.0101 | 1.47% | -8.04% | 1/4 |
| Performance (Week) | -0.0275 | -0.0023 | +0.0321 | -0.98% | -0.67% | 6974/4539 |
| d_Relative Volume | -0.0250 | -0.0535 | +0.0002 | -0.84% | -0.89% | 4990/6294 |
| d_Short Ratio | -0.0230 | +0.0187 | -0.0249 | -1.09% | -0.79% | 4086/2863 |
| d_Profit Margin | -0.0194 | +0.0099 | +0.0008 | -4.87% | 1.47% | 2/1 |
| d_50-Day Simple Moving Average | +0.0182 | -0.0337 | +0.0653 | -0.78% | -1.00% | 7362/4214 |
| d_Analyst Recom | -0.0171 | +0.0181 | +0.0102 | -0.73% | -0.15% | 74/84 |
| d_Performance (YTD) | +0.0165 | -0.0797 | +0.0970 | -0.78% | -0.93% | 7133/4168 |
| d_Market Cap | -0.0144 | -0.1196 | +0.0267 | -0.78% | -0.52% | 2945/2748 |
| Relative Volume | +0.0140 | +0.0102 | -0.0061 | -0.88% | n/a | 11429/0 |
| d_EPS Surprise | +0.0139 | -0.0122 | -0.0007 | -0.18% | -3.04% | 4/6 |
| true_ret | +0.0138 | -0.0635 | +0.0769 | -0.78% | -0.95% | 7068/4083 |
| d_200-Day Simple Moving Average | +0.0135 | -0.0532 | +0.0668 | -0.82% | -0.91% | 7268/4294 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 376 | -5.08% | 20.5% |
| true_ret>3% & UPTREND | 208 | -3.99% | 20.7% |
| true_ret>3% & MIXED | 138 | -2.49% | 32.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 237 | -3.91% | -5.42% |
| WASHED | 1505 | -0.85% | -1.75% |
