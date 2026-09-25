# Factor attribution — signal 2026-09-23 → prediction day 2026-09-25

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-23** | Features/scores formed from this snapshot (and deltas vs **2026-09-22**). Only data on/before this date. |
| **Prediction day** | **2026-09-25** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-23 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-25 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11653** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0398**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.16% | 17.8% | 2493 |
| 2 | -0.17% | 9.0% | 3301 |
| 3 | -0.38% | 18.3% | 1200 |
| 4 | 0.30% | 7.7% | 2544 |
| 5 | -0.51% | 21.0% | 2115 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.1960 | +0.2126 | -0.3664 | -0.65% | -0.21% | 4372/267 |
| d_Price | -0.1639 | -0.0738 | -0.1495 | -0.50% | 0.02% | 1880/9370 |
| Relative Strength Index (14) | +0.1611 | -0.0431 | -0.1524 | -0.08% | n/a | 11559/0 |
| Performance (Month) | +0.1496 | -0.0866 | +0.1586 | 0.13% | -0.18% | 3693/7778 |
| Performance (Week) | +0.1312 | +0.0851 | +0.0012 | 0.10% | -0.25% | 5743/5716 |
| d_Relative Strength Index (14) | -0.1129 | +0.1755 | -0.2451 | -0.50% | 0.00% | 1932/9385 |
| d_200-Day Simple Moving Average | -0.0944 | -0.2759 | +0.0733 | -0.52% | 0.02% | 2025/9533 |
| d_Performance (YTD) | -0.0890 | -0.2600 | +0.0675 | -0.50% | 0.01% | 1925/9420 |
| d_Forward P/E | -0.0848 | -0.0746 | -0.0460 | -0.69% | -0.00% | 699/2270 |
| d_Market Cap | -0.0816 | +0.0624 | -0.1024 | -0.48% | -0.15% | 1408/4333 |
| d_Performance (Quarter) | -0.0804 | -0.1505 | -0.0329 | -0.44% | 0.05% | 3098/7903 |
| d_20-Day Simple Moving Average | -0.0792 | -0.2870 | +0.1127 | -0.51% | 0.02% | 2218/9349 |
| d_50-Day Simple Moving Average | -0.0673 | -0.2871 | +0.1138 | -0.57% | 0.02% | 2077/9488 |
| d_Performance (Week) | -0.0658 | -0.2113 | +0.0562 | -0.43% | 0.06% | 3377/8089 |
| Relative Volume | -0.0474 | +0.0689 | -0.0227 | -0.09% | n/a | 11419/0 |
| true_ret | -0.0419 | -0.3098 | +0.1476 | -0.50% | 0.02% | 1880/9370 |
| d_Relative Volume | -0.0399 | -0.0681 | +0.0312 | -0.00% | -0.18% | 5268/5969 |
| Institutional Transactions | -0.0382 | +0.0698 | -0.0952 | -0.01% | -0.59% | 3222/1809 |
| d_Volatility (Month) | +0.0306 | +0.0492 | +0.0178 | -0.24% | 0.12% | 5313/3988 |
| d_Insider Transactions | -0.0256 | -0.0410 | -0.0255 | -2.06% | 0.68% | 92/177 |
| d_Short Ratio | -0.0251 | +0.0017 | -0.0246 | -0.27% | -0.15% | 3915/3307 |
| d_Sales Growth Quarter Over Quarter | +0.0244 | +0.0306 | -0.0012 | 4.36% | 1.40% | 6/8 |
| d_Short Float | +0.0212 | n/a | +0.0270 | n/a | -9.20% | 0/1 |
| d_Performance (Month) | +0.0212 | -0.0776 | +0.0282 | -0.18% | -0.04% | 3407/7989 |
| d_Institutional Ownership | +0.0175 | +0.0074 | +0.0134 | 4.87% | -0.78% | 12/40 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 205 | -0.08% | 30.2% |
| true_ret>3% & UPTREND | 115 | -1.79% | 23.5% |
| true_ret>3% & MIXED | 91 | -0.58% | 25.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 204 | 1.13% | -3.68% |
| WASHED | 1805 | 0.01% | -0.63% |
