# Factor attribution — signal 2026-09-28 → prediction day 2026-09-30

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-28** | Features/scores formed from this snapshot (and deltas vs **2026-09-25**). Only data on/before this date. |
| **Prediction day** | **2026-09-30** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-28 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-30 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11667** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0469**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.32% | 20.3% | 2340 |
| 2 | -0.42% | 7.0% | 3371 |
| 3 | 1.32% | 7.3% | 1306 |
| 4 | -0.58% | 8.4% | 2704 |
| 5 | -0.47% | 17.8% | 1946 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.1229 | -0.2153 | +0.2659 | 0.30% | 0.00% | 2792/8712 |
| d_Performance (Quarter) | -0.1200 | -0.1859 | -0.0232 | 0.58% | -0.06% | 2566/8478 |
| d_Performance (Month) | -0.1148 | -0.1783 | -0.0199 | -0.79% | 0.40% | 3063/8322 |
| d_Forward P/E | -0.1015 | -0.1180 | +0.0135 | -0.89% | -0.74% | 843/2087 |
| d_Relative Strength Index (14) | -0.1001 | +0.1538 | -0.2980 | -0.41% | 0.22% | 2314/8986 |
| Relative Strength Index (14) | +0.0830 | -0.0834 | -0.0050 | 0.08% | n/a | 11564/0 |
| d_Performance (Week) | -0.0645 | -0.1646 | +0.0141 | 0.67% | -0.09% | 2551/8937 |
| Short Float | -0.0495 | +0.2130 | -0.0792 | 0.56% | n/a | 5691/0 |
| d_20-Day Simple Moving Average | -0.0416 | -0.1475 | +0.0562 | 0.59% | -0.09% | 2870/8718 |
| d_Beta | +0.0377 | -0.0817 | +0.0300 | 1.46% | -0.24% | 1134/2391 |
| d_50-Day Simple Moving Average | -0.0316 | -0.1659 | +0.0752 | 0.12% | 0.07% | 2500/9095 |
| d_200-Day Simple Moving Average | -0.0295 | -0.1511 | +0.0584 | 0.20% | -0.13% | 2367/9197 |
| d_Performance (YTD) | -0.0275 | -0.1448 | +0.0573 | -0.41% | 0.05% | 2299/9038 |
| d_Relative Volume | +0.0255 | +0.0166 | +0.0172 | -0.11% | 0.36% | 6159/5077 |
| d_Institutional Ownership | +0.0208 | -0.0040 | -0.0120 | -0.41% | -0.95% | 210/397 |
| d_Sales Growth Quarter Over Quarter | +0.0206 | -0.0489 | +0.0096 | 0.13% | 5.73% | 7/4 |
| d_Volatility (Month) | -0.0202 | +0.0311 | -0.0268 | 0.01% | 0.19% | 5594/3892 |
| upside_pct_lvl | +0.0199 | +0.3290 | -0.2672 | -0.40% | -0.57% | 4385/248 |
| d_Short Ratio | -0.0182 | +0.0264 | -0.0334 | -0.27% | 0.15% | 4359/3027 |
| Institutional Transactions | -0.0154 | +0.0631 | -0.0666 | 0.08% | 1.30% | 3234/1813 |
| d_Target Price | +0.0152 | -0.0288 | -0.0178 | -0.88% | -0.89% | 202/265 |
| true_ret | -0.0146 | -0.2089 | +0.1209 | -0.42% | -0.12% | 2257/8967 |
| d_Price | -0.0139 | +0.0170 | -0.1059 | -0.42% | -0.12% | 2257/8967 |
| d_Insider Transactions | +0.0135 | +0.0260 | +0.0376 | -0.99% | -1.13% | 261/151 |
| d_Gross Margin | -0.0125 | +0.0162 | -0.0293 | -1.98% | 0.38% | 5/12 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 192 | -1.36% | 29.7% |
| true_ret>3% & UPTREND | 134 | 5.33% | 33.6% |
| true_ret>3% & MIXED | 108 | -1.35% | 38.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 169 | -0.49% | 0.63% |
| WASHED | 2432 | 0.86% | -1.13% |
