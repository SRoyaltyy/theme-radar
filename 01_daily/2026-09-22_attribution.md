# Factor attribution — signal 2026-09-22 → prediction day 2026-09-23

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-22** | Features/scores formed from this snapshot (and deltas vs **2026-09-21**). Only data on/before this date. |
| **Prediction day** | **2026-09-23** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-22 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-23 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11637** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.1323**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.41% | 10.8% | 2343 |
| 2 | -1.17% | 3.9% | 2342 |
| 3 | -1.04% | 4.5% | 2445 |
| 4 | -1.24% | 4.3% | 2279 |
| 5 | -2.15% | 9.6% | 2228 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.3063 | -0.0456 | -0.3535 | -1.52% | -0.36% | 8315/3095 |
| Short Float | -0.2332 | +0.0572 | -0.2481 | -1.26% | n/a | 5695/0 |
| upside_pct_lvl | -0.2270 | +0.3225 | -0.4171 | -1.66% | -1.06% | 4338/298 |
| Performance (Week) | -0.2164 | -0.0938 | -0.1975 | -1.56% | -0.61% | 7128/4314 |
| d_20-Day Simple Moving Average | -0.1911 | -0.0120 | -0.2246 | -1.45% | -0.80% | 7012/4454 |
| d_50-Day Simple Moving Average | -0.1856 | -0.0189 | -0.2154 | -1.57% | -0.67% | 6721/4750 |
| d_200-Day Simple Moving Average | -0.1848 | -0.0231 | -0.2111 | -1.57% | -0.73% | 6618/4820 |
| d_Performance (Quarter) | -0.1841 | -0.0459 | -0.1792 | -1.51% | -0.68% | 6707/4244 |
| true_ret | -0.1779 | -0.0476 | -0.1951 | -1.54% | -0.76% | 6462/4418 |
| d_Performance (YTD) | -0.1747 | -0.0446 | -0.1829 | -1.55% | -0.76% | 6581/4531 |
| d_Price | -0.1518 | -0.0364 | -0.1458 | -1.54% | -0.76% | 6462/4418 |
| d_Relative Strength Index (14) | -0.1472 | -0.0003 | -0.1266 | -1.54% | -0.73% | 6602/4547 |
| Relative Volume | -0.0868 | -0.0095 | -0.0909 | -1.21% | n/a | 11412/0 |
| d_Market Cap | -0.0865 | -0.0299 | -0.0938 | -1.76% | -0.64% | 3111/2565 |
| d_Volatility (Month) | +0.0776 | +0.0292 | +0.1028 | -0.89% | -1.61% | 4495/4924 |
| Institutional Transactions | -0.0748 | +0.0727 | -0.1046 | -1.20% | -1.53% | 3222/1810 |
| Performance (Month) | +0.0727 | -0.1370 | +0.1501 | -1.01% | -1.30% | 4062/7410 |
| d_Beta | +0.0657 | -0.0470 | +0.0885 | -0.67% | -1.44% | 1660/3470 |
| d_Target Price | +0.0524 | +0.0243 | +0.0304 | 0.20% | -2.49% | 126/157 |
| d_Forward P/E | -0.0482 | -0.0100 | -0.0768 | -1.36% | -1.13% | 1553/1390 |
| d_Institutional Ownership | -0.0344 | +0.0520 | -0.0506 | -1.36% | -1.10% | 289/528 |
| d_Short Ratio | -0.0313 | -0.0122 | -0.0229 | -1.22% | -1.66% | 4560/2469 |
| d_Gross Margin | +0.0220 | +0.0175 | +0.0308 | -1.78% | -3.32% | 1/6 |
| d_Performance (Month) | +0.0195 | -0.0123 | +0.0333 | -1.36% | -1.11% | 4408/6943 |
| d_Average Volume | +0.0160 | -0.1126 | +0.0917 | -1.52% | -1.03% | 3816/7402 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 410 | -1.59% | 16.6% |
| true_ret>3% & UPTREND | 433 | -2.97% | 9.9% |
| true_ret>3% & MIXED | 305 | -3.28% | 13.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 281 | -2.75% | -3.17% |
| WASHED | 1090 | -0.92% | -0.89% |
