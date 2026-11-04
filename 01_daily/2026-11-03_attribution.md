# Factor attribution — signal 2026-11-03 → prediction day 2026-11-04

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-03** | Features/scores formed from this snapshot (and deltas vs **2026-11-02**). Only data on/before this date. |
| **Prediction day** | **2026-11-04** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-03 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-04 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11737** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.1243**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.55% | 43.9% | 2608 |
| 2 | 1.35% | 43.6% | 2316 |
| 3 | 1.22% | 38.7% | 2129 |
| 4 | 0.92% | 39.4% | 2396 |
| 5 | -0.54% | 39.8% | 2288 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_20-Day Simple Moving Average | -0.2723 | -0.1529 | -0.2689 | 0.00% | 1.93% | 6050/5547 |
| d_Forward P/E | -0.2600 | -0.1286 | -0.1564 | 0.36% | 2.69% | 1138/1799 |
| d_Performance (Quarter) | -0.2585 | -0.1380 | -0.2487 | 0.06% | 2.03% | 5994/5189 |
| d_Price | -0.2572 | -0.1753 | -0.1330 | -0.00% | 1.80% | 5605/5512 |
| d_Performance (YTD) | -0.2552 | -0.1818 | -0.1649 | 0.02% | 1.79% | 5702/5587 |
| d_Performance (Month) | -0.2549 | -0.2277 | -0.1901 | -0.20% | 1.66% | 4506/6959 |
| true_ret | -0.2511 | -0.1852 | -0.2167 | -0.00% | 1.80% | 5605/5512 |
| d_200-Day Simple Moving Average | -0.2469 | -0.1636 | -0.1914 | 0.14% | 1.76% | 5920/5646 |
| d_Relative Strength Index (14) | -0.2439 | -0.1365 | -0.0763 | 0.02% | 1.85% | 5716/5595 |
| d_50-Day Simple Moving Average | -0.2393 | -0.1369 | -0.2282 | 0.17% | 1.79% | 6265/5332 |
| d_Market Cap | -0.2274 | -0.1060 | -0.1099 | 0.24% | 1.97% | 2647/3041 |
| Performance (Month) | +0.1942 | -0.0415 | +0.3219 | 1.69% | 0.36% | 4873/6696 |
| Short Float | +0.1621 | +0.3359 | -0.2455 | 1.28% | n/a | 5652/0 |
| Performance (Week) | +0.1580 | +0.0271 | +0.2214 | 1.61% | 0.48% | 4479/7097 |
| d_Beta | -0.1481 | -0.2559 | -0.0291 | -0.16% | 1.70% | 1694/4369 |
| upside_pct_lvl | -0.1448 | +0.1739 | -0.1411 | 1.46% | 2.26% | 4331/303 |
| d_Performance (Week) | -0.1213 | -0.1944 | +0.0300 | 0.48% | 1.13% | 3615/7892 |
| Relative Strength Index (14) | +0.1201 | -0.0316 | +0.1660 | 0.92% | n/a | 11661/0 |
| Relative Volume | +0.0890 | +0.1108 | -0.1003 | 0.93% | n/a | 11468/0 |
| d_Volatility (Month) | -0.0873 | +0.1754 | -0.2755 | 0.70% | 1.41% | 7235/3017 |
| Institutional Transactions | -0.0849 | -0.0005 | -0.0865 | 1.20% | 1.73% | 3193/1831 |
| d_Short Ratio | -0.0414 | -0.0793 | +0.0293 | 1.09% | 1.14% | 2755/4391 |
| d_Total Debt/Equity | +0.0298 | +0.0231 | +0.0410 | 1.84% | 0.01% | 84/97 |
| d_Short Float | +0.0268 | +0.0316 | -0.0317 | 5.63% | -0.43% | 2/5 |
| d_Relative Volume | +0.0248 | +0.0062 | +0.0003 | 0.88% | 0.93% | 4474/6867 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 935 | -3.09% | 30.1% |
| true_ret>3% & UPTREND | 155 | 0.77% | 50.3% |
| true_ret>3% & MIXED | 201 | 0.22% | 41.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 200 | 1.67% | 0.66% |
| WASHED | 1678 | -1.45% | -5.19% |
