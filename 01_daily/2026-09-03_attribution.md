# Factor attribution — signal 2026-09-03 → prediction day 2026-09-09

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-03** | Features/scores formed from this snapshot (and deltas vs **2026-09-02**). Only data on/before this date. |
| **Prediction day** | **2026-09-09** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-03 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-09 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11586** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.1049**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 4.55% | 17.9% | 2330 |
| 2 | -0.73% | 6.8% | 3244 |
| 3 | 0.00% | 9.7% | 2161 |
| 4 | 0.91% | 20.7% | 1556 |
| 5 | 1.01% | 18.6% | 2295 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.2228 | -0.1021 | -0.1853 | 0.02% | 3.08% | 7462/3906 |
| Short Float | -0.1772 | +0.2302 | -0.2432 | 2.09% | n/a | 5681/0 |
| d_200-Day Simple Moving Average | -0.1595 | +0.0062 | -0.1368 | 0.06% | 3.45% | 8119/3362 |
| true_ret | -0.1492 | -0.0015 | -0.1352 | -0.28% | 3.63% | 7928/3160 |
| d_20-Day Simple Moving Average | -0.1485 | +0.0436 | -0.1539 | 0.03% | 3.59% | 8224/3273 |
| d_Performance (YTD) | -0.1360 | -0.0011 | -0.1053 | -0.10% | 4.21% | 7998/3200 |
| d_50-Day Simple Moving Average | -0.1275 | +0.0609 | -0.1338 | 0.06% | 3.47% | 8184/3324 |
| d_Price | -0.1262 | -0.0461 | -0.0209 | -0.28% | 3.63% | 7928/3160 |
| d_Relative Strength Index (14) | -0.1066 | -0.0776 | +0.1682 | -0.11% | 4.19% | 7970/3195 |
| Relative Strength Index (14) | -0.0879 | -0.1906 | -0.0510 | 1.06% | n/a | 11487/0 |
| d_Forward P/E | -0.0816 | -0.0354 | -0.0595 | -1.98% | -1.30% | 1925/1016 |
| d_Market Cap | -0.0671 | +0.0117 | +0.0207 | 0.52% | 4.50% | 3293/2376 |
| d_Performance (Quarter) | +0.0647 | +0.0694 | +0.0664 | 0.91% | 1.17% | 5636/5174 |
| d_Performance (Month) | -0.0616 | +0.1724 | -0.1477 | 0.02% | 3.53% | 7939/3341 |
| Performance (Month) | -0.0614 | -0.1183 | -0.0485 | -1.03% | 3.02% | 5536/5826 |
| Performance (Week) | -0.0604 | -0.2172 | +0.0368 | 1.21% | 0.95% | 4607/6844 |
| Relative Volume | -0.0532 | +0.0929 | -0.0376 | 1.07% | n/a | 11302/0 |
| d_Short Ratio | -0.0382 | +0.0846 | -0.0918 | 1.20% | 1.79% | 4226/2808 |
| d_Average Volume | +0.0336 | -0.0928 | +0.1215 | 1.26% | 1.08% | 4555/6448 |
| d_Total Debt/Equity | +0.0292 | -0.0275 | +0.0382 | 2.88% | -0.96% | 13/18 |
| Institutional Transactions | +0.0287 | +0.0782 | -0.0074 | 2.15% | 3.27% | 3181/1856 |
| d_Profit Margin | +0.0228 | -0.0184 | +0.0177 | 0.11% | 0.54% | 25/11 |
| d_EPS Surprise | -0.0186 | -0.0077 | -0.0215 | -3.17% | 0.09% | 24/30 |
| d_Target Price | -0.0158 | -0.0184 | -0.0380 | -2.32% | -1.66% | 156/118 |
| d_Short Float | +0.0148 | +0.0164 | +0.0252 | -2.33% | -4.02% | 15/29 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 330 | 17.63% | 34.8% |
| true_ret>3% & UPTREND | 508 | -3.43% | 13.0% |
| true_ret>3% & MIXED | 343 | 0.58% | 24.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 250 | -3.60% | -9.34% |
| WASHED | 732 | 11.43% | 3.54% |
