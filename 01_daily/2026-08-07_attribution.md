# Factor attribution — signal 2026-08-07 → prediction day 2026-08-12

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-07** | Features/scores formed from this snapshot (and deltas vs **2026-08-06**). Only data on/before this date. |
| **Prediction day** | **2026-08-12** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-07 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-12 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11525** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0009**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 12.82% | 31.8% | 2323 |
| 2 | 2.69% | 15.2% | 2579 |
| 3 | 0.25% | 12.2% | 2042 |
| 4 | 0.42% | 21.9% | 2463 |
| 5 | 0.15% | 35.1% | 2118 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.0608 | +0.2043 | -0.1069 | 0.31% | 14.00% | 8834/2556 |
| d_Performance (Quarter) | +0.0561 | +0.1758 | -0.0955 | 0.27% | 14.48% | 8332/2435 |
| d_Performance (Week) | -0.0502 | +0.1069 | -0.1681 | 1.10% | 8.02% | 7544/3771 |
| d_Forward P/E | -0.0477 | +0.0412 | -0.0607 | -0.28% | 0.13% | 1801/1182 |
| Institutional Transactions | +0.0453 | +0.0929 | +0.0174 | 11.53% | 2.64% | 2536/2487 |
| d_Performance (Month) | -0.0417 | +0.0327 | -0.0457 | 1.08% | 6.13% | 5945/5186 |
| d_Sales Growth Quarter Over Quarter | +0.0406 | +0.0592 | +0.0220 | 1.29% | -0.63% | 202/183 |
| d_Relative Strength Index (14) | -0.0389 | -0.1520 | +0.1889 | 0.10% | 13.78% | 8449/2738 |
| Relative Strength Index (14) | +0.0317 | -0.2916 | +0.2119 | 3.37% | n/a | 11429/0 |
| d_Gross Margin | +0.0311 | -0.0036 | -0.0128 | 0.85% | -0.10% | 220/194 |
| d_Market Cap | -0.0286 | -0.0048 | +0.0670 | 1.13% | 15.02% | 3601/2131 |
| upside_pct_lvl | +0.0277 | +0.3487 | -0.2455 | 2.55% | -0.81% | 4266/382 |
| Short Float | -0.0248 | +0.2511 | -0.1656 | 6.27% | n/a | 5697/0 |
| d_Average Volume | -0.0220 | -0.0728 | +0.0102 | 8.29% | 0.38% | 4352/6657 |
| d_Institutional Ownership | -0.0199 | -0.0035 | -0.0111 | -0.49% | 0.29% | 66/117 |
| d_200-Day Simple Moving Average | -0.0197 | +0.1038 | -0.1275 | 0.28% | 12.68% | 8578/2860 |
| d_50-Day Simple Moving Average | -0.0163 | +0.1303 | -0.1532 | 0.32% | 12.42% | 8563/2884 |
| true_ret | -0.0154 | +0.1072 | -0.1290 | 0.11% | 11.21% | 8421/2677 |
| d_Target Price | +0.0147 | -0.0178 | +0.0200 | 0.12% | 0.23% | 435/284 |
| Relative Volume | -0.0138 | +0.1085 | -0.1156 | 3.43% | n/a | 11237/0 |
| d_Analyst Recom | -0.0129 | -0.0291 | +0.0503 | -0.32% | -0.63% | 80/72 |
| d_Sales Year Over Year TTM | -0.0097 | -0.0036 | +0.0267 | 0.24% | 0.58% | 205/157 |
| d_Price | -0.0079 | -0.0514 | +0.0831 | 0.11% | 11.21% | 8421/2677 |
| Performance (Month) | -0.0077 | -0.0856 | +0.0809 | 0.18% | 7.86% | 6563/4716 |
| d_Insider Transactions | +0.0067 | +0.0108 | -0.0063 | 0.99% | -0.01% | 198/207 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 643 | 0.28% | 40.9% |
| true_ret>3% & UPTREND | 649 | 0.73% | 39.8% |
| true_ret>3% & MIXED | 466 | -0.42% | 34.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 368 | 1.15% | 2.53% |
| WASHED | 578 | 60.60% | -2.23% |
