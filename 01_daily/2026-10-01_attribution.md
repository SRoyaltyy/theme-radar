# Factor attribution — signal 2026-10-01 → prediction day 2026-10-05

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-01** | Features/scores formed from this snapshot (and deltas vs **2026-09-30**). Only data on/before this date. |
| **Prediction day** | **2026-10-05** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-01 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-05 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11680** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.1090**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.89% | 27.4% | 2367 |
| 2 | 0.40% | 14.5% | 2372 |
| 3 | 0.81% | 29.4% | 2380 |
| 4 | 0.72% | 31.9% | 2321 |
| 5 | 1.05% | 42.3% | 2240 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Relative Strength Index (14) | +0.1891 | +0.1709 | -0.1905 | 1.38% | n/a | 11574/0 |
| Performance (Month) | +0.1831 | +0.0384 | +0.2567 | 1.46% | 1.35% | 3717/7770 |
| upside_pct_lvl | -0.1762 | +0.2325 | -0.4317 | 1.79% | 1.60% | 4386/247 |
| d_Performance (Month) | +0.0962 | +0.1479 | -0.0412 | 0.71% | 3.11% | 8153/3239 |
| Short Float | +0.0750 | +0.1359 | -0.1376 | 1.81% | n/a | 5689/0 |
| d_Beta | -0.0726 | -0.0507 | -0.0894 | 1.70% | 1.40% | 2075/1021 |
| d_Price | +0.0687 | +0.0296 | +0.0830 | 0.80% | 2.20% | 6031/5091 |
| d_Performance (Quarter) | +0.0675 | +0.1291 | -0.0394 | 0.78% | 2.02% | 5525/5543 |
| d_Performance (YTD) | +0.0606 | +0.0280 | +0.0814 | 0.77% | 2.20% | 6113/5171 |
| true_ret | +0.0576 | +0.0218 | +0.0908 | 0.80% | 2.20% | 6031/5091 |
| d_Average Volume | -0.0540 | -0.0514 | +0.0476 | 2.00% | 0.84% | 5266/5820 |
| Performance (Week) | +0.0457 | -0.0688 | +0.1916 | 0.93% | 1.58% | 3313/8189 |
| d_Short Ratio | +0.0443 | +0.0515 | -0.0626 | 0.82% | 1.19% | 3895/3493 |
| d_Market Cap | +0.0430 | -0.0767 | +0.0951 | 0.56% | 3.04% | 2860/2831 |
| d_Target Price | +0.0422 | +0.0806 | -0.0505 | 1.29% | 0.21% | 127/259 |
| d_Sales Year Over Year TTM | -0.0397 | -0.0285 | -0.0241 | -2.98% | 71.43% | 9/10 |
| d_200-Day Simple Moving Average | +0.0296 | +0.0211 | +0.0485 | 0.70% | 2.18% | 6187/5354 |
| Institutional Transactions | -0.0281 | +0.0389 | -0.0772 | 2.12% | 1.89% | 3232/1811 |
| d_Volatility (Month) | -0.0280 | -0.0199 | +0.0240 | -0.33% | 0.92% | 34/4 |
| d_50-Day Simple Moving Average | +0.0260 | +0.0228 | +0.0436 | 0.69% | 2.22% | 6347/5202 |
| d_Profit Margin | +0.0190 | +0.0185 | -0.0054 | 1.58% | 74.64% | 10/9 |
| d_Relative Strength Index (14) | +0.0170 | -0.0150 | +0.1459 | 0.79% | 2.15% | 6119/5186 |
| d_EPS Surprise | -0.0158 | +0.0038 | -0.0219 | -1.22% | 1.21% | 6/5 |
| d_Gross Margin | -0.0154 | -0.0363 | -0.0142 | -2.31% | 63.30% | 10/11 |
| d_Institutional Ownership | +0.0148 | -0.0309 | +0.0622 | 0.08% | -3.10% | 15/33 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 306 | -0.20% | 33.7% |
| true_ret>3% & UPTREND | 318 | 1.11% | 44.7% |
| true_ret>3% & MIXED | 190 | 0.43% | 38.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 186 | 1.62% | 3.72% |
| WASHED | 2312 | 3.19% | -0.71% |
