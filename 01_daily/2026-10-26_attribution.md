# Factor attribution — signal 2026-10-26 → prediction day 2026-10-28

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-26** | Features/scores formed from this snapshot (and deltas vs **2026-10-23**). Only data on/before this date. |
| **Prediction day** | **2026-10-28** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-26 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-28 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11756** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0612**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.32% | 46.3% | 2424 |
| 2 | 2.40% | 37.9% | 2291 |
| 3 | 1.18% | 18.5% | 2425 |
| 4 | 1.44% | 18.1% | 2297 |
| 5 | 3.14% | 45.1% | 2319 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | -0.4555 | -0.6079 | +0.0420 | -0.19% | 3.57% | 4514/7048 |
| Relative Strength Index (14) | -0.4240 | -0.4983 | +0.2219 | 2.08% | n/a | 11664/0 |
| upside_pct_lvl | +0.3508 | +0.4730 | -0.2107 | 3.26% | -0.02% | 4291/340 |
| d_Performance (Quarter) | +0.3202 | +0.2743 | +0.1473 | 3.38% | 0.67% | 5884/5294 |
| d_Beta | +0.3181 | +0.3994 | -0.0585 | 6.20% | -0.12% | 2309/1837 |
| Performance (Week) | -0.2839 | -0.3065 | +0.0160 | 0.67% | 3.77% | 6141/5375 |
| d_20-Day Simple Moving Average | +0.2572 | +0.2230 | +0.1340 | 2.44% | 1.56% | 7294/4292 |
| d_50-Day Simple Moving Average | +0.1760 | +0.1369 | +0.1205 | 2.12% | 2.12% | 7633/3951 |
| d_Forward P/E | +0.1714 | +0.1381 | +0.0832 | 1.40% | 0.56% | 1607/1316 |
| Short Float | +0.1529 | +0.3525 | -0.0923 | 2.78% | n/a | 5650/0 |
| d_200-Day Simple Moving Average | +0.1428 | +0.0781 | +0.1266 | 2.06% | 2.25% | 7225/4316 |
| true_ret | +0.1342 | +0.0686 | +0.1530 | 1.92% | 2.31% | 6975/4197 |
| d_Performance (YTD) | +0.1319 | +0.0506 | +0.1403 | 2.07% | 2.30% | 7054/4264 |
| d_Price | +0.1261 | -0.0139 | +0.1664 | 1.92% | 2.31% | 6975/4197 |
| Institutional Transactions | +0.1157 | +0.1661 | +0.0190 | 3.93% | 1.36% | 3235/1814 |
| d_Relative Strength Index (14) | +0.1151 | -0.1351 | +0.2070 | 2.06% | 2.23% | 7031/4267 |
| d_Market Cap | +0.0683 | -0.0364 | +0.0948 | 2.87% | 2.56% | 2841/2941 |
| d_Performance (Week) | -0.0642 | -0.0629 | +0.0241 | 1.49% | 3.24% | 7260/4228 |
| d_Volatility (Month) | +0.0608 | +0.1804 | -0.1738 | 2.47% | 2.15% | 5282/4880 |
| d_Target Price | -0.0424 | -0.0438 | -0.0200 | 0.88% | 2.03% | 327/319 |
| d_Performance (Month) | +0.0375 | +0.0298 | +0.0610 | 2.40% | 1.81% | 5888/5565 |
| d_Insider Transactions | +0.0301 | +0.0095 | +0.0218 | 2.37% | 1.53% | 232/270 |
| d_Analyst Recom | -0.0242 | -0.0143 | +0.0040 | 1.30% | 2.28% | 89/118 |
| d_Short Float | -0.0200 | -0.0347 | -0.0191 | 1.51% | 2.91% | 74/58 |
| d_Relative Volume | +0.0195 | +0.0207 | -0.0216 | 2.21% | 2.08% | 5625/5565 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 503 | 10.48% | 70.6% |
| true_ret>3% & UPTREND | 153 | 2.50% | 50.3% |
| true_ret>3% & MIXED | 156 | 3.76% | 66.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 185 | -1.56% | 1.86% |
| WASHED | 1690 | 8.86% | 12.90% |
