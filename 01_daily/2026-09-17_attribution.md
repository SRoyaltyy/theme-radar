# Factor attribution — signal 2026-09-17 → prediction day 2026-09-21

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-17** | Features/scores formed from this snapshot (and deltas vs **2026-09-16**). Only data on/before this date. |
| **Prediction day** | **2026-09-21** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-17 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-21 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11622** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.2454**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.27% | 15.6% | 2379 |
| 2 | 0.20% | 12.5% | 2273 |
| 3 | 0.73% | 17.8% | 2500 |
| 4 | 1.48% | 38.9% | 2476 |
| 5 | 3.33% | 48.6% | 1994 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | +0.2912 | +0.4344 | -0.0372 | 1.42% | 1.16% | 8733/2589 |
| d_Performance (Week) | +0.2692 | +0.4657 | -0.0519 | 1.83% | -0.55% | 9167/2282 |
| d_Price | +0.2574 | +0.1997 | +0.1089 | 1.37% | 0.56% | 8597/2600 |
| d_200-Day Simple Moving Average | +0.2498 | +0.3980 | -0.0445 | 1.42% | 1.13% | 8777/2756 |
| d_Performance (YTD) | +0.2428 | +0.3541 | -0.0251 | 1.38% | 1.35% | 8664/2646 |
| d_50-Day Simple Moving Average | +0.2417 | +0.4214 | -0.0681 | 1.41% | 1.16% | 8849/2699 |
| true_ret | +0.2337 | +0.4000 | -0.0606 | 1.37% | 0.56% | 8597/2600 |
| d_20-Day Simple Moving Average | +0.2313 | +0.4168 | -0.0893 | 1.56% | 0.53% | 9166/2387 |
| d_Relative Strength Index (14) | +0.1659 | -0.0821 | +0.3185 | 1.38% | 1.32% | 8643/2646 |
| d_Beta | -0.1254 | -0.1119 | -0.0932 | 1.53% | 2.00% | 2115/1460 |
| d_Performance (Quarter) | +0.1177 | +0.2553 | -0.0953 | 1.03% | 2.23% | 8956/2020 |
| upside_pct_lvl | +0.1169 | +0.3972 | -0.2255 | 0.45% | -1.01% | 4354/285 |
| Relative Strength Index (14) | +0.1145 | +0.0417 | -0.1783 | 1.34% | n/a | 11544/0 |
| d_Forward P/E | +0.0990 | +0.2454 | -0.0454 | 0.24% | -0.44% | 1726/1214 |
| d_Average Volume | -0.0844 | -0.0534 | +0.0022 | 1.60% | 1.10% | 5582/5450 |
| Performance (Week) | +0.0708 | -0.0226 | +0.1204 | 0.98% | 1.75% | 5693/5716 |
| d_Short Ratio | +0.0692 | +0.0546 | -0.0167 | 1.12% | 0.73% | 3418/3675 |
| d_Market Cap | +0.0606 | +0.1258 | -0.0257 | 0.52% | 1.81% | 3634/2075 |
| Relative Volume | -0.0599 | +0.0389 | -0.0162 | 1.36% | n/a | 11418/0 |
| d_Relative Volume | +0.0397 | +0.0266 | +0.0057 | 1.26% | 1.40% | 4866/6378 |
| Performance (Month) | +0.0328 | -0.0223 | +0.0783 | 1.76% | 1.15% | 3691/7738 |
| Short Float | +0.0233 | +0.1771 | -0.1274 | 1.05% | n/a | 5692/0 |
| d_Profit Margin | -0.0228 | -0.0287 | -0.0013 | -3.21% | 3.27% | 4/7 |
| Institutional Transactions | +0.0225 | +0.0859 | -0.0317 | 0.99% | 1.33% | 3210/1826 |
| d_Institutional Ownership | +0.0209 | -0.0151 | +0.0363 | 0.82% | 9.47% | 587/238 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 711 | 3.54% | 48.0% |
| true_ret>3% & UPTREND | 543 | 4.01% | 53.2% |
| true_ret>3% & MIXED | 381 | 6.43% | 52.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 160 | 3.27% | 7.52% |
| WASHED | 1112 | 4.73% | 4.13% |
