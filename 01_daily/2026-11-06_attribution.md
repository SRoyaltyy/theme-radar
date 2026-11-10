# Factor attribution — signal 2026-11-06 → prediction day 2026-11-10

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-06** | Features/scores formed from this snapshot (and deltas vs **2026-11-05**). Only data on/before this date. |
| **Prediction day** | **2026-11-10** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-06 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-10 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11722** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.1151**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.94% | 40.4% | 2367 |
| 2 | 1.19% | 50.8% | 2417 |
| 3 | 3.12% | 40.6% | 2633 |
| 4 | 2.99% | 40.9% | 2138 |
| 5 | 3.21% | 59.9% | 2167 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Volatility (Month) | +0.2517 | +0.4857 | -0.4698 | 2.70% | 4.25% | 9326/1255 |
| Performance (Week) | -0.2254 | -0.3164 | +0.1566 | 1.17% | 3.62% | 4250/7319 |
| d_Performance (Week) | +0.2142 | +0.3979 | -0.2497 | 3.29% | 1.37% | 8085/3490 |
| Relative Strength Index (14) | -0.2008 | -0.2036 | +0.3863 | 2.68% | n/a | 11670/0 |
| d_Price | +0.1999 | +0.2544 | -0.0070 | 2.52% | 1.75% | 6537/4682 |
| d_Beta | +0.1798 | +0.1611 | +0.0542 | 3.74% | 1.45% | 3067/5009 |
| d_20-Day Simple Moving Average | +0.1776 | +0.3311 | -0.1523 | 3.59% | 1.37% | 6984/4620 |
| d_Performance (YTD) | +0.1760 | +0.2772 | -0.0355 | 2.89% | 2.52% | 6615/4733 |
| true_ret | +0.1713 | +0.2852 | -0.0456 | 2.52% | 1.75% | 6537/4682 |
| d_Performance (Month) | +0.1711 | +0.3186 | -0.1467 | 3.50% | 1.69% | 6507/4964 |
| d_50-Day Simple Moving Average | +0.1710 | +0.3150 | -0.1020 | 3.28% | 1.79% | 7122/4474 |
| d_200-Day Simple Moving Average | +0.1651 | +0.2922 | -0.0695 | 2.84% | 2.55% | 6793/4785 |
| d_Forward P/E | +0.1618 | +0.2467 | -0.1599 | 2.39% | 1.47% | 1404/1531 |
| d_Performance (Quarter) | +0.1543 | +0.2670 | -0.0817 | 2.85% | 2.51% | 7114/4088 |
| d_Relative Strength Index (14) | +0.1433 | +0.2133 | -0.0417 | 2.92% | 2.48% | 6634/4740 |
| Short Float | +0.1375 | +0.2532 | -0.1919 | 3.95% | n/a | 5622/0 |
| Performance (Month) | -0.1371 | -0.3228 | +0.3206 | 1.00% | 3.83% | 4635/6931 |
| Relative Volume | +0.1317 | +0.1267 | -0.0138 | 2.73% | n/a | 11437/0 |
| d_Market Cap | +0.1156 | +0.2145 | -0.0568 | 3.61% | 4.33% | 3271/2451 |
| d_Short Ratio | -0.0873 | -0.1105 | +0.0987 | 3.09% | 3.00% | 1976/5710 |
| d_Relative Volume | -0.0736 | -0.0440 | +0.0562 | 1.53% | 3.18% | 3060/8351 |
| d_Institutional Ownership | +0.0557 | -0.0141 | +0.0921 | 3.58% | 3.37% | 2248/1835 |
| d_Average Volume | +0.0506 | +0.1299 | -0.0858 | 2.76% | 2.76% | 7961/3189 |
| d_Sales Growth Quarter Over Quarter | +0.0461 | +0.0517 | -0.0254 | 3.02% | 1.86% | 283/295 |
| d_Profit Margin | +0.0426 | +0.0268 | -0.0332 | 2.84% | 1.70% | 229/184 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1482 | 6.26% | 64.3% |
| true_ret>3% & UPTREND | 237 | 2.07% | 60.3% |
| true_ret>3% & MIXED | 254 | 2.59% | 57.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 260 | -0.39% | -0.08% |
| WASHED | 1957 | 9.86% | 7.55% |
