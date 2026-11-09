# Factor attribution — signal 2026-11-06 → prediction day 2026-11-09

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-06** | Features/scores formed from this snapshot (and deltas vs **2026-11-05**). Only data on/before this date. |
| **Prediction day** | **2026-11-09** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-06 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-09 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11724** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.2104**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.62% | 49.4% | 2367 |
| 2 | 1.81% | 59.0% | 2417 |
| 3 | 2.55% | 48.7% | 2633 |
| 4 | 4.07% | 50.5% | 2138 |
| 5 | 4.84% | 72.9% | 2169 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | +0.3798 | +0.5158 | -0.1299 | 3.92% | 2.01% | 8087/3490 |
| d_Volatility (Month) | +0.3582 | +0.5542 | -0.4512 | 3.21% | 6.03% | 9328/1255 |
| d_20-Day Simple Moving Average | +0.2990 | +0.4142 | -0.0908 | 4.16% | 2.11% | 6986/4620 |
| d_50-Day Simple Moving Average | +0.2846 | +0.3823 | -0.0398 | 3.80% | 2.62% | 7124/4474 |
| d_Price | +0.2791 | +0.3265 | +0.0074 | 3.49% | 2.64% | 6539/4682 |
| d_Performance (Month) | +0.2782 | +0.4013 | -0.1114 | 3.99% | 2.53% | 6509/4964 |
| Relative Strength Index (14) | -0.2735 | -0.3456 | +0.2659 | 3.32% | n/a | 11672/0 |
| Performance (Month) | -0.2698 | -0.4284 | +0.2330 | 1.45% | 4.59% | 4635/6933 |
| d_Forward P/E | +0.2670 | +0.3189 | -0.1818 | 3.41% | 1.88% | 1404/1531 |
| d_200-Day Simple Moving Average | +0.2660 | +0.3538 | -0.0264 | 3.89% | 2.60% | 6795/4785 |
| d_Performance (YTD) | +0.2652 | +0.3391 | -0.0033 | 3.91% | 2.62% | 6617/4733 |
| true_ret | +0.2642 | +0.3456 | +0.0029 | 3.49% | 2.64% | 6539/4682 |
| Performance (Week) | -0.2500 | -0.3480 | +0.0872 | 1.91% | 4.18% | 4251/7320 |
| d_Performance (Quarter) | +0.2459 | +0.3041 | +0.0151 | 3.42% | 3.27% | 7116/4088 |
| Short Float | +0.2387 | +0.2907 | -0.1706 | 4.39% | n/a | 5624/0 |
| d_Relative Strength Index (14) | +0.2249 | +0.2928 | +0.0003 | 3.94% | 2.61% | 6636/4740 |
| d_Market Cap | +0.2140 | +0.2664 | -0.0919 | 4.65% | 4.12% | 3273/2451 |
| upside_pct_lvl | +0.1597 | +0.4252 | -0.4662 | 4.40% | 1.65% | 4354/276 |
| d_Beta | +0.1427 | +0.1644 | +0.0651 | 4.33% | 2.47% | 3067/5010 |
| Relative Volume | +0.1340 | +0.1155 | -0.0304 | 3.38% | n/a | 11439/0 |
| d_Short Ratio | -0.1009 | -0.1240 | +0.0289 | 4.10% | 3.61% | 1977/5711 |
| d_Relative Volume | -0.0865 | -0.0948 | +0.0151 | 2.44% | 3.72% | 3060/8353 |
| d_Average Volume | +0.0708 | +0.1185 | -0.0815 | 3.41% | 3.36% | 7962/3190 |
| Institutional Transactions | +0.0688 | +0.1027 | -0.0443 | 4.20% | 6.06% | 3189/1829 |
| d_Target Price | -0.0464 | -0.0829 | +0.0944 | 2.41% | 3.43% | 365/395 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1482 | 7.91% | 78.9% |
| true_ret>3% & UPTREND | 237 | 3.33% | 68.8% |
| true_ret>3% & MIXED | 255 | 3.90% | 65.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 260 | -0.31% | 1.64% |
| WASHED | 1957 | 10.19% | 9.55% |
