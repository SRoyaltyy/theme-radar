# Factor attribution — signal 2026-10-02 → prediction day 2026-10-05

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-02** | Features/scores formed from this snapshot (and deltas vs **2026-10-01**). Only data on/before this date. |
| **Prediction day** | **2026-10-05** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-02 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-05 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11685** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0316**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.14% | 20.8% | 2538 |
| 2 | 0.71% | 8.8% | 2472 |
| 3 | 0.49% | 14.0% | 2086 |
| 4 | 0.42% | 16.9% | 2285 |
| 5 | 0.18% | 22.3% | 2304 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Forward P/E | -0.1643 | -0.0978 | -0.0659 | 0.36% | 0.82% | 1896/1056 |
| Relative Strength Index (14) | +0.1534 | +0.0706 | -0.1079 | 0.79% | n/a | 11576/0 |
| d_Performance (Quarter) | -0.1412 | -0.1574 | -0.0248 | 0.51% | 1.08% | 5108/5944 |
| upside_pct_lvl | -0.1124 | +0.2362 | -0.4514 | 1.41% | 0.80% | 4369/264 |
| Institutional Transactions | -0.0771 | +0.0168 | -0.1137 | 1.87% | 0.30% | 3232/1811 |
| Performance (Month) | +0.0761 | -0.1110 | +0.1834 | 0.51% | 0.92% | 3752/7742 |
| d_Price | +0.0647 | -0.0641 | +0.0527 | 0.58% | 1.34% | 7329/3868 |
| Short Float | +0.0588 | +0.1550 | -0.0843 | 1.12% | n/a | 5690/0 |
| d_Average Volume | -0.0549 | -0.0654 | +0.0397 | 1.28% | 0.29% | 5722/5380 |
| d_Volatility (Month) | -0.0480 | +0.0344 | -0.1101 | 1.06% | 0.53% | 6290/3607 |
| d_Beta | -0.0390 | +0.0571 | -0.0766 | 1.43% | 0.51% | 4378/2560 |
| d_Market Cap | -0.0343 | -0.0968 | +0.1528 | 0.61% | 1.44% | 3314/2388 |
| d_Relative Strength Index (14) | +0.0320 | -0.1685 | +0.0864 | 0.57% | 1.27% | 7357/3935 |
| Performance (Week) | +0.0314 | -0.1342 | +0.1414 | 0.35% | 1.02% | 3926/7593 |
| d_Short Ratio | +0.0305 | +0.0482 | -0.0405 | 0.35% | 0.72% | 3659/3817 |
| d_Performance (YTD) | +0.0297 | -0.0001 | +0.0101 | 0.48% | 1.07% | 7385/3935 |
| d_Performance (Month) | -0.0269 | -0.0812 | -0.0103 | 0.14% | 1.45% | 5640/5712 |
| d_Target Price | +0.0241 | +0.0215 | -0.0842 | 0.88% | 0.37% | 125/284 |
| d_Institutional Ownership | +0.0230 | +0.0502 | -0.0698 | 0.62% | 0.23% | 331/514 |
| d_EPS Surprise | -0.0197 | -0.0005 | -0.0095 | 0.29% | 2.97% | 2/3 |
| d_50-Day Simple Moving Average | -0.0173 | +0.0100 | -0.0553 | 0.60% | 1.19% | 7719/3899 |
| d_Performance (Week) | +0.0165 | +0.0896 | -0.0912 | 0.72% | 0.91% | 6831/4626 |
| d_Insider Transactions | +0.0144 | +0.0105 | -0.0168 | 0.34% | -0.03% | 135/175 |
| d_Profit Margin | +0.0141 | -0.0257 | -0.0010 | -0.94% | -3.14% | 2/6 |
| d_Relative Volume | +0.0140 | +0.1054 | -0.1064 | 0.71% | 0.84% | 4702/6665 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 381 | 2.72% | 24.7% |
| true_ret>3% & UPTREND | 378 | 0.60% | 28.3% |
| true_ret>3% & MIXED | 220 | 0.36% | 30.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 215 | 1.65% | 2.59% |
| WASHED | 2057 | 2.71% | -0.50% |
