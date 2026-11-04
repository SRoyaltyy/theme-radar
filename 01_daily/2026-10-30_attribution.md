# Factor attribution — signal 2026-10-30 → prediction day 2026-11-04

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-30** | Features/scores formed from this snapshot (and deltas vs **2026-10-29**). Only data on/before this date. |
| **Prediction day** | **2026-11-04** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-30 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-04 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11730** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0800**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.30% | 37.3% | 2635 |
| 2 | 1.71% | 40.0% | 2146 |
| 3 | 1.46% | 44.3% | 2263 |
| 4 | 0.96% | 37.5% | 2403 |
| 5 | 1.53% | 49.5% | 2283 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | +0.1896 | -0.0121 | +0.3404 | 2.17% | 0.65% | 3976/7563 |
| Performance (Month) | +0.1457 | -0.0547 | +0.2766 | 1.44% | 0.95% | 5345/6212 |
| upside_pct_lvl | -0.1210 | +0.1916 | -0.1672 | 1.74% | 1.05% | 4323/307 |
| d_Forward P/E | +0.1189 | -0.0277 | +0.0033 | 2.48% | 1.79% | 932/2029 |
| Short Float | +0.1006 | +0.3391 | -0.2216 | 2.08% | n/a | 5648/0 |
| d_Performance (Month) | +0.0886 | -0.0920 | +0.2551 | 1.62% | 1.00% | 3441/8035 |
| Institutional Transactions | -0.0733 | +0.0035 | -0.0877 | 1.91% | 2.40% | 3231/1813 |
| d_Beta | -0.0693 | +0.0856 | -0.1458 | 2.30% | 1.09% | 1819/1191 |
| Relative Volume | +0.0614 | +0.1403 | -0.0760 | 1.18% | n/a | 11470/0 |
| d_50-Day Simple Moving Average | +0.0590 | -0.1362 | +0.2488 | 1.06% | 1.21% | 3254/8380 |
| true_ret | +0.0573 | -0.1775 | +0.3010 | 0.98% | 1.22% | 2928/8403 |
| d_200-Day Simple Moving Average | +0.0444 | -0.1246 | +0.2203 | 1.12% | 1.20% | 3087/8533 |
| d_Performance (YTD) | +0.0426 | -0.1123 | +0.2001 | 1.05% | 0.87% | 2966/8452 |
| d_Target Price | -0.0412 | -0.0721 | +0.0160 | 1.45% | 3.63% | 336/295 |
| Relative Strength Index (14) | +0.0373 | -0.0918 | +0.2330 | 1.17% | n/a | 11649/0 |
| d_Performance (Quarter) | -0.0317 | -0.2569 | +0.2261 | 0.17% | 1.59% | 2601/8581 |
| d_Sales Growth Quarter Over Quarter | -0.0272 | -0.0319 | +0.0109 | 1.85% | 2.65% | 140/155 |
| d_Volatility (Month) | -0.0265 | +0.1195 | -0.1821 | 1.37% | 1.20% | 4616/5051 |
| d_20-Day Simple Moving Average | +0.0261 | -0.1849 | +0.2564 | 0.81% | 1.28% | 2823/8800 |
| d_Sales Year Over Year TTM | -0.0258 | +0.0008 | -0.0087 | 1.51% | 3.18% | 155/139 |
| d_Short Float | +0.0257 | -0.0219 | +0.0459 | 3.33% | 0.32% | 39/38 |
| Performance (Week) | -0.0250 | -0.0461 | +0.0086 | 0.52% | 1.85% | 5950/5619 |
| d_Relative Strength Index (14) | -0.0171 | +0.1613 | +0.0839 | 1.04% | 1.22% | 2969/8446 |
| d_Profit Margin | -0.0164 | +0.0077 | -0.0047 | 1.71% | 3.00% | 167/125 |
| d_Institutional Ownership | +0.0142 | -0.0026 | -0.0031 | 1.79% | 1.56% | 1382/1271 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 166 | 1.95% | 43.4% |
| true_ret>3% & UPTREND | 147 | -0.39% | 49.0% |
| true_ret>3% & MIXED | 146 | 1.27% | 46.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 219 | 0.77% | 4.44% |
| WASHED | 1669 | 1.23% | -0.12% |
