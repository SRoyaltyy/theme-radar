# Factor attribution — signal 2026-09-21 → prediction day 2026-09-22

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-21** | Features/scores formed from this snapshot (and deltas vs **2026-09-18**). Only data on/before this date. |
| **Prediction day** | **2026-09-22** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-21 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-22 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11629** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.1709**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.63% | 18.0% | 2369 |
| 2 | 0.22% | 11.3% | 2286 |
| 3 | 0.76% | 12.7% | 2520 |
| 4 | 0.78% | 21.0% | 2234 |
| 5 | 2.35% | 32.0% | 2220 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | +0.1852 | +0.1424 | +0.1108 | 0.97% | 0.86% | 7867/3575 |
| Performance (Week) | +0.1840 | +0.0669 | +0.2067 | 0.97% | 0.92% | 6055/5377 |
| d_Forward P/E | +0.1806 | +0.0915 | +0.0699 | 0.65% | -0.06% | 1652/1285 |
| d_Performance (Month) | +0.1670 | +0.1596 | +0.0438 | 1.11% | 0.55% | 8184/3185 |
| d_20-Day Simple Moving Average | +0.1658 | +0.1432 | +0.0698 | 1.06% | 0.61% | 8363/3186 |
| d_50-Day Simple Moving Average | +0.1578 | +0.1095 | +0.0957 | 1.07% | 0.65% | 8012/3528 |
| d_Performance (YTD) | +0.1546 | +0.0505 | +0.1376 | 0.95% | 0.44% | 7721/3573 |
| d_200-Day Simple Moving Average | +0.1521 | +0.0719 | +0.1192 | 0.94% | 0.61% | 7854/3677 |
| true_ret | +0.1495 | +0.0856 | +0.1161 | 0.93% | 0.98% | 7648/3532 |
| d_Price | +0.1424 | -0.0600 | +0.1767 | 0.93% | 0.98% | 7648/3532 |
| upside_pct_lvl | +0.1333 | +0.2972 | -0.2304 | 1.01% | 0.26% | 4354/282 |
| Short Float | +0.1325 | +0.2226 | -0.1291 | 1.21% | n/a | 5702/0 |
| d_Performance (Quarter) | +0.1251 | +0.0993 | +0.0643 | 1.02% | 0.81% | 7366/3587 |
| d_Market Cap | +0.0949 | -0.0235 | +0.0427 | 1.36% | 1.00% | 3170/2553 |
| d_Relative Strength Index (14) | +0.0814 | -0.2762 | +0.2825 | 0.94% | 0.97% | 7701/3580 |
| d_Volatility (Month) | -0.0642 | -0.2247 | +0.1461 | 1.82% | 0.72% | 3423/6003 |
| Relative Strength Index (14) | +0.0637 | -0.0742 | +0.0225 | 0.94% | n/a | 11546/0 |
| d_Institutional Ownership | +0.0338 | +0.0161 | +0.0190 | 0.60% | 0.10% | 163/177 |
| d_Beta | -0.0278 | -0.0571 | +0.0039 | 1.17% | 1.18% | 1478/1058 |
| d_Sales Growth Quarter Over Quarter | +0.0258 | +0.0081 | +0.0237 | 4.30% | 3.24% | 6/3 |
| Performance (Month) | -0.0210 | -0.1683 | +0.1584 | 0.59% | 1.16% | 4296/7151 |
| d_EPS Surprise | -0.0197 | -0.0144 | -0.0110 | -1.80% | 0.27% | 4/4 |
| d_Average Volume | -0.0185 | +0.0126 | -0.0218 | 1.44% | 0.51% | 5454/5635 |
| d_Target Price | +0.0172 | +0.0406 | -0.0446 | 0.73% | 0.46% | 162/223 |
| d_Analyst Recom | +0.0172 | +0.0322 | -0.0756 | 0.75% | -0.16% | 73/108 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 538 | 6.13% | 43.5% |
| true_ret>3% & UPTREND | 725 | 0.91% | 33.4% |
| true_ret>3% & MIXED | 296 | 3.81% | 42.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 236 | 2.64% | 10.16% |
| WASHED | 1114 | 4.17% | 10.88% |
