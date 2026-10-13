# Factor attribution — signal 2026-10-09 → prediction day 2026-10-13

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-09** | Features/scores formed from this snapshot (and deltas vs **2026-10-08**). Only data on/before this date. |
| **Prediction day** | **2026-10-13** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-09 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-13 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11697** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.2058**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.63% | 17.7% | 2345 |
| 2 | 1.46% | 10.0% | 2389 |
| 3 | 0.75% | 11.1% | 2342 |
| 4 | -1.39% | 12.4% | 2286 |
| 5 | -1.53% | 11.0% | 2335 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.4317 | +0.1545 | -0.5422 | -0.47% | -0.36% | 4353/278 |
| d_Performance (Quarter) | -0.3919 | -0.1527 | -0.3073 | -0.35% | 1.16% | 8053/3102 |
| d_Performance (Month) | -0.2852 | -0.0313 | -0.2487 | -0.35% | 1.17% | 8718/2717 |
| Performance (Week) | +0.2393 | +0.0625 | +0.3356 | -0.01% | 0.01% | 6245/5267 |
| d_20-Day Simple Moving Average | -0.1869 | -0.0308 | -0.1243 | -0.16% | 0.39% | 8197/3392 |
| d_200-Day Simple Moving Average | -0.1696 | -0.0695 | -0.0422 | -0.43% | 0.89% | 7704/3860 |
| d_50-Day Simple Moving Average | -0.1688 | -0.0534 | -0.0766 | -0.48% | 1.06% | 7972/3617 |
| d_Forward P/E | -0.1687 | +0.0026 | -0.1310 | -0.59% | 0.27% | 1556/1401 |
| d_Performance (YTD) | -0.1558 | -0.0777 | -0.0036 | -0.36% | 0.82% | 7514/3804 |
| true_ret | -0.1514 | -0.0641 | -0.0411 | -0.34% | -0.34% | 7432/3713 |
| Institutional Transactions | -0.1261 | +0.0388 | -0.1757 | 2.25% | -1.19% | 3240/1801 |
| Short Float | -0.1139 | +0.2112 | -0.2320 | 0.77% | n/a | 5681/0 |
| d_Price | -0.1099 | -0.1194 | +0.1459 | -0.34% | -0.34% | 7432/3713 |
| d_Relative Strength Index (14) | -0.0966 | -0.1934 | +0.2220 | -0.37% | 0.78% | 7492/3812 |
| Relative Strength Index (14) | +0.0926 | +0.0459 | +0.2795 | 0.00% | n/a | 11610/0 |
| d_Market Cap | -0.0866 | +0.0032 | +0.0330 | -0.05% | 1.58% | 3037/2669 |
| d_Beta | -0.0808 | +0.0214 | -0.1317 | 1.35% | 6.14% | 1553/733 |
| Performance (Month) | +0.0803 | -0.1475 | +0.2733 | -0.92% | 0.57% | 4341/7157 |
| d_Volatility (Month) | -0.0714 | +0.0308 | -0.0976 | 0.97% | -1.49% | 6020/3625 |
| d_Performance (Week) | -0.0668 | -0.0811 | -0.0288 | 0.42% | -0.38% | 5522/5954 |
| d_Short Float | +0.0420 | -0.0002 | +0.0390 | -3.46% | -1.75% | 28/57 |
| Relative Volume | +0.0340 | +0.0334 | -0.0289 | 0.00% | n/a | 11402/0 |
| d_Gross Margin | +0.0281 | +0.0106 | -0.0054 | 1.08% | -2.14% | 6/4 |
| d_Institutional Ownership | -0.0157 | -0.0157 | -0.0071 | -1.82% | -0.88% | 278/292 |
| d_Profit Margin | +0.0135 | +0.0305 | -0.0181 | 0.06% | -0.92% | 6/5 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 428 | 8.74% | 14.3% |
| true_ret>3% & UPTREND | 360 | -3.64% | 15.0% |
| true_ret>3% & MIXED | 187 | -2.67% | 19.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 172 | -1.73% | -8.67% |
| WASHED | 1068 | 7.41% | 1.80% |
