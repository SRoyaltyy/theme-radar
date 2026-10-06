# Factor attribution — signal 2026-10-05 → prediction day 2026-10-06

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-05** | Features/scores formed from this snapshot (and deltas vs **2026-10-02**). Only data on/before this date. |
| **Prediction day** | **2026-10-06** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-05 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-06 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11690** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.1002**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.54% | 18.1% | 2464 |
| 2 | 0.28% | 9.8% | 2318 |
| 3 | 0.97% | 10.6% | 2366 |
| 4 | 0.10% | 10.8% | 2211 |
| 5 | -0.45% | 17.8% | 2331 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | -0.1550 | -0.1726 | -0.0698 | 0.07% | 0.44% | 4135/7250 |
| Short Float | -0.1067 | +0.1000 | -0.1278 | 0.28% | n/a | 5687/0 |
| d_Forward P/E | -0.0916 | -0.0286 | -0.1452 | 0.13% | 0.38% | 1599/1332 |
| d_Target Price | -0.0849 | +0.0349 | -0.0958 | -0.56% | 0.41% | 248/468 |
| d_Market Cap | -0.0798 | -0.0455 | -0.0258 | 0.19% | 0.35% | 2755/2966 |
| true_ret | -0.0657 | -0.0585 | -0.0102 | 0.03% | 0.38% | 6922/4222 |
| d_Performance (YTD) | -0.0581 | -0.0711 | +0.0138 | 0.26% | 0.42% | 7002/4295 |
| d_200-Day Simple Moving Average | -0.0573 | -0.0479 | -0.0052 | 0.28% | 0.34% | 7142/4407 |
| d_50-Day Simple Moving Average | -0.0563 | -0.0281 | -0.0166 | 0.27% | 0.35% | 7355/4237 |
| Relative Strength Index (14) | -0.0563 | -0.0131 | +0.0216 | 0.30% | n/a | 11597/0 |
| d_20-Day Simple Moving Average | -0.0481 | +0.0129 | -0.0357 | 0.29% | 0.33% | 8012/3576 |
| d_Relative Strength Index (14) | -0.0461 | -0.1785 | +0.0959 | 0.26% | 0.40% | 6966/4309 |
| d_Total Debt/Equity | +0.0419 | +0.0252 | +0.0452 | 2.85% | -9.80% | 2/2 |
| Performance (Month) | -0.0408 | -0.2106 | +0.1207 | -0.06% | 0.46% | 3557/7937 |
| upside_pct_lvl | -0.0386 | +0.3139 | -0.3780 | 0.06% | -1.31% | 4351/282 |
| Institutional Transactions | -0.0370 | +0.0663 | -0.0906 | 0.19% | 0.32% | 3242/1803 |
| d_Performance (Week) | +0.0307 | +0.1614 | -0.0696 | 0.36% | 0.14% | 8846/2661 |
| d_Price | -0.0270 | -0.0943 | +0.0783 | 0.03% | 0.38% | 6922/4222 |
| d_Gross Margin | -0.0260 | -0.0268 | -0.0010 | -11.62% | -1.62% | 2/6 |
| d_Sales Growth Quarter Over Quarter | +0.0243 | +0.0364 | +0.0054 | -1.79% | -7.88% | 5/2 |
| d_EPS Surprise | +0.0243 | +0.0480 | +0.0072 | 2.01% | -1.90% | 3/3 |
| d_Sales Year Over Year TTM | +0.0217 | +0.0101 | +0.0326 | 2.95% | -2.22% | 2/2 |
| Performance (Week) | +0.0198 | +0.0154 | +0.0834 | 0.14% | 0.49% | 6269/5228 |
| d_Beta | -0.0190 | +0.0336 | +0.0094 | 1.21% | -0.41% | 1252/869 |
| d_Insider Transactions | -0.0189 | -0.0299 | +0.0084 | -0.14% | -0.11% | 267/203 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 381 | -0.60% | 22.8% |
| true_ret>3% & UPTREND | 356 | -1.59% | 14.9% |
| true_ret>3% & MIXED | 218 | -1.19% | 19.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 251 | -0.94% | -3.01% |
| WASHED | 1953 | 0.65% | -0.21% |
