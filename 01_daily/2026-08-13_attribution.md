# Factor attribution — signal 2026-08-13 → prediction day 2026-08-18

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-13** | Features/scores formed from this snapshot (and deltas vs **2026-08-12**). Only data on/before this date. |
| **Prediction day** | **2026-08-18** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-13 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-18 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11542** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.1672**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.89% | 25.5% | 2360 |
| 2 | -0.82% | 9.3% | 2585 |
| 3 | 7.31% | 6.9% | 1990 |
| 4 | -1.21% | 9.4% | 2375 |
| 5 | -1.46% | 15.5% | 2232 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.2808 | -0.1384 | -0.2403 | 1.14% | 0.56% | 7767/3564 |
| d_50-Day Simple Moving Average | -0.2705 | -0.0697 | -0.2491 | 0.87% | 1.11% | 7694/3735 |
| d_200-Day Simple Moving Average | -0.2529 | -0.0821 | -0.2078 | 0.89% | 1.05% | 7674/3754 |
| true_ret | -0.2443 | -0.0994 | -0.2006 | -1.21% | 1.05% | 7504/3526 |
| d_Performance (YTD) | -0.2427 | -0.0963 | -0.1802 | 0.59% | 1.81% | 7591/3587 |
| d_Price | -0.2243 | -0.0891 | -0.0630 | -1.21% | 1.05% | 7504/3526 |
| d_20-Day Simple Moving Average | -0.2183 | -0.0838 | -0.1802 | 1.89% | -0.76% | 7356/4063 |
| Performance (Week) | -0.1879 | +0.0368 | -0.2585 | -0.55% | 5.26% | 8436/2940 |
| d_Performance (Month) | -0.1821 | -0.0611 | -0.1673 | 1.32% | 0.52% | 6418/4757 |
| d_Forward P/E | -0.1679 | -0.0590 | -0.1402 | -1.80% | -0.84% | 1840/1133 |
| Short Float | -0.1332 | +0.1872 | -0.2554 | 3.20% | n/a | 5689/0 |
| d_Relative Strength Index (14) | -0.1300 | -0.1070 | +0.1441 | 0.61% | 1.80% | 7553/3584 |
| d_Market Cap | -0.1284 | -0.0614 | -0.0021 | 3.26% | 3.01% | 3296/2407 |
| d_Performance (Quarter) | -0.1225 | -0.0489 | -0.0927 | 1.91% | -0.01% | 6573/4174 |
| Performance (Month) | -0.0842 | -0.0653 | -0.0634 | -1.03% | 4.36% | 7096/4209 |
| d_Short Ratio | -0.0420 | -0.0034 | -0.0281 | -1.27% | -0.04% | 4119/2744 |
| Institutional Transactions | +0.0400 | +0.0960 | -0.0293 | 1.91% | 5.11% | 2515/2514 |
| d_Average Volume | +0.0380 | +0.0023 | +0.0413 | 3.68% | -0.84% | 4523/6446 |
| d_EPS Surprise | -0.0361 | +0.0395 | -0.0517 | -2.16% | -0.24% | 118/101 |
| d_Target Price | +0.0354 | -0.0017 | +0.0387 | -0.61% | -2.06% | 323/207 |
| Relative Volume | -0.0353 | +0.0927 | -0.0879 | 0.97% | n/a | 11279/0 |
| d_Short Float | +0.0307 | +0.0288 | +0.0382 | -0.30% | -2.82% | 79/130 |
| Relative Strength Index (14) | -0.0299 | -0.1728 | +0.2041 | 0.96% | n/a | 11420/0 |
| d_Beta | -0.0152 | -0.0003 | -0.0071 | -0.68% | 9.89% | 1657/1546 |
| d_Sales Year Over Year TTM | +0.0133 | +0.0085 | +0.0247 | -1.37% | -3.11% | 76/83 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 398 | -2.43% | 19.6% |
| true_ret>3% & UPTREND | 468 | -3.41% | 16.9% |
| true_ret>3% & MIXED | 283 | 3.21% | 14.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 400 | -2.79% | -5.16% |
| WASHED | 505 | 43.51% | -4.05% |
