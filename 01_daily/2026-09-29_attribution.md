# Factor attribution — signal 2026-09-29 → prediction day 2026-10-01

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-29** | Features/scores formed from this snapshot (and deltas vs **2026-09-28**). Only data on/before this date. |
| **Prediction day** | **2026-10-01** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-29 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-01 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11672** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0392**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.39% | 14.9% | 2364 |
| 2 | -0.45% | 7.5% | 2529 |
| 3 | -0.05% | 9.6% | 2177 |
| 4 | -0.40% | 14.6% | 2297 |
| 5 | 0.23% | 27.4% | 2305 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.1488 | -0.1135 | +0.2401 | -0.08% | 0.23% | 3091/8390 |
| upside_pct_lvl | -0.1359 | +0.2531 | -0.3410 | -0.26% | -0.66% | 4388/247 |
| Performance (Week) | +0.0988 | -0.2274 | +0.2595 | -0.43% | 0.26% | 1894/9628 |
| d_Performance (Week) | +0.0944 | -0.0313 | +0.1832 | 0.77% | -0.19% | 4041/7371 |
| Relative Strength Index (14) | +0.0838 | +0.0159 | -0.0608 | 0.14% | n/a | 11567/0 |
| d_Performance (Quarter) | -0.0780 | -0.0555 | -0.0132 | 0.59% | -0.12% | 4227/6822 |
| d_Volatility (Month) | -0.0721 | +0.0340 | -0.1122 | 0.40% | -0.05% | 5836/3580 |
| d_Beta | -0.0662 | +0.0984 | -0.0844 | -0.12% | -0.69% | 3551/1244 |
| true_ret | +0.0562 | +0.0177 | +0.1074 | 0.72% | -0.43% | 4229/6815 |
| Institutional Transactions | -0.0556 | +0.0298 | -0.1138 | -0.02% | 1.12% | 3234/1812 |
| d_Price | +0.0518 | +0.0814 | -0.0015 | 0.72% | -0.43% | 4229/6815 |
| d_Performance (YTD) | +0.0509 | +0.0363 | +0.0794 | 0.72% | -0.31% | 4316/6938 |
| d_200-Day Simple Moving Average | +0.0403 | +0.0485 | +0.0605 | 0.82% | -0.27% | 4470/7064 |
| d_Relative Strength Index (14) | +0.0340 | +0.1164 | +0.0164 | 0.71% | -0.32% | 4307/6920 |
| d_50-Day Simple Moving Average | +0.0331 | +0.0265 | +0.0726 | 0.99% | -0.40% | 4559/6978 |
| Short Float | -0.0294 | +0.2092 | -0.1476 | 0.50% | n/a | 5693/0 |
| d_Forward P/E | +0.0230 | +0.1076 | -0.0060 | -0.10% | -0.22% | 1188/1742 |
| d_Performance (Month) | +0.0203 | +0.1170 | -0.0703 | -0.06% | 0.26% | 6639/4751 |
| d_Gross Margin | -0.0202 | +0.0021 | -0.0404 | -2.42% | 0.49% | 14/15 |
| d_Market Cap | +0.0183 | +0.0835 | -0.0347 | 1.08% | -0.28% | 2438/3260 |
| d_Institutional Ownership | -0.0166 | -0.0220 | -0.0054 | -3.64% | 3.61% | 5/26 |
| d_20-Day Simple Moving Average | +0.0146 | +0.0677 | +0.0369 | 0.78% | -0.41% | 5415/6111 |
| d_Average Volume | -0.0140 | -0.1806 | +0.1335 | 0.62% | -0.12% | 4140/6937 |
| d_Relative Volume | -0.0135 | -0.0359 | -0.0095 | 0.36% | -0.02% | 5496/5725 |
| d_Short Float | -0.0117 | -0.0186 | -0.0005 | -1.44% | 0.75% | 43/40 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 269 | 14.10% | 32.3% |
| true_ret>3% & UPTREND | 194 | 0.95% | 45.9% |
| true_ret>3% & MIXED | 127 | -1.06% | 31.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 160 | -1.58% | -4.27% |
| WASHED | 2419 | 0.19% | 1.00% |
