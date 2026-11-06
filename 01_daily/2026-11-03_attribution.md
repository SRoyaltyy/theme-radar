# Factor attribution — signal 2026-11-03 → prediction day 2026-11-06

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-03** | Features/scores formed from this snapshot (and deltas vs **2026-11-02**). Only data on/before this date. |
| **Prediction day** | **2026-11-06** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-03 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-06 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11736** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0579**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.46% | 22.1% | 2608 |
| 2 | -1.50% | 14.1% | 2316 |
| 3 | -0.89% | 13.5% | 2129 |
| 4 | -1.77% | 14.0% | 2396 |
| 5 | -3.85% | 24.6% | 2287 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_20-Day Simple Moving Average | -0.3233 | -0.0486 | -0.3807 | -2.46% | 0.99% | 6049/5547 |
| Performance (Month) | +0.3231 | -0.1410 | +0.4521 | -0.21% | -1.22% | 4873/6695 |
| d_Performance (Quarter) | -0.3009 | -0.0645 | -0.3565 | -3.44% | 2.46% | 5993/5189 |
| d_Price | -0.2838 | -0.0210 | -0.3042 | -3.56% | 0.81% | 5604/5512 |
| d_50-Day Simple Moving Average | -0.2767 | -0.0349 | -0.3415 | -2.93% | 1.68% | 6264/5332 |
| d_Relative Strength Index (14) | -0.2748 | +0.0682 | -0.2512 | -3.37% | 1.84% | 5715/5595 |
| true_ret | -0.2698 | -0.0957 | -0.2990 | -3.56% | 0.81% | 5604/5512 |
| d_Performance (YTD) | -0.2698 | -0.0661 | -0.3003 | -3.37% | 1.52% | 5701/5587 |
| Performance (Week) | +0.2692 | -0.0423 | +0.3500 | -0.21% | -1.18% | 4478/7097 |
| d_200-Day Simple Moving Average | -0.2667 | -0.0514 | -0.3166 | -3.24% | 1.44% | 5919/5646 |
| Relative Strength Index (14) | +0.2492 | -0.1818 | +0.2949 | -0.79% | n/a | 11660/0 |
| d_Volatility (Month) | -0.2070 | +0.2591 | -0.3266 | -0.92% | -0.56% | 7234/3017 |
| d_Forward P/E | -0.1945 | +0.0645 | -0.2478 | -3.43% | -0.58% | 1138/1799 |
| upside_pct_lvl | -0.1638 | +0.3291 | -0.3510 | -0.41% | -0.94% | 4331/303 |
| d_Market Cap | -0.1580 | +0.0664 | -0.2010 | -0.66% | 2.32% | 2646/3041 |
| d_Performance (Month) | -0.1361 | -0.0933 | -0.2037 | -1.69% | -0.22% | 4505/6959 |
| Short Float | -0.0493 | +0.3058 | -0.1835 | 0.23% | n/a | 5651/0 |
| d_Average Volume | +0.0491 | +0.0845 | -0.0472 | -0.79% | -0.69% | 6612/4473 |
| d_Short Ratio | -0.0448 | -0.0947 | +0.0148 | -1.11% | -1.47% | 2755/4390 |
| Institutional Transactions | -0.0446 | +0.0894 | -0.0906 | 1.96% | -1.95% | 3193/1831 |
| Relative Volume | +0.0437 | +0.0906 | -0.0303 | -0.80% | n/a | 11467/0 |
| d_Total Debt/Equity | +0.0328 | -0.0136 | +0.0362 | -1.30% | -4.07% | 84/97 |
| d_Target Price | +0.0277 | -0.0153 | +0.0471 | -0.75% | -2.91% | 283/233 |
| d_Short Float | +0.0270 | +0.0056 | +0.0187 | 8.30% | -3.75% | 2/5 |
| d_Performance (Week) | -0.0241 | -0.1670 | +0.0281 | -2.20% | -0.17% | 3614/7892 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 934 | -9.05% | 16.1% |
| true_ret>3% & UPTREND | 155 | 3.18% | 32.9% |
| true_ret>3% & MIXED | 201 | -4.24% | 25.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 200 | 3.72% | 17.36% |
| WASHED | 1678 | 0.03% | -11.43% |
