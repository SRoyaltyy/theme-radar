# Factor attribution — signal 2026-11-09 → prediction day 2026-11-12

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-09** | Features/scores formed from this snapshot (and deltas vs **2026-11-06**). Only data on/before this date. |
| **Prediction day** | **2026-11-12** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-09 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-12 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11726** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0053**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.45% | 19.8% | 2395 |
| 2 | -0.04% | 13.4% | 2311 |
| 3 | 0.52% | 13.5% | 2546 |
| 4 | -0.85% | 16.7% | 2561 |
| 5 | -2.40% | 17.9% | 1913 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.2412 | -0.2945 | -0.1017 | -1.75% | 1.60% | 6801/4771 |
| upside_pct_lvl | -0.1618 | +0.4650 | -0.4627 | 0.01% | -2.12% | 4301/326 |
| d_Relative Strength Index (14) | +0.1615 | -0.3307 | +0.2218 | -0.58% | 0.66% | 9367/2034 |
| d_Price | +0.1492 | -0.0448 | +0.1595 | -0.95% | 0.77% | 9322/1975 |
| Short Float | -0.1490 | +0.2011 | -0.2157 | -0.06% | n/a | 5596/0 |
| Relative Strength Index (14) | -0.1465 | -0.3636 | +0.2372 | -0.38% | n/a | 11673/0 |
| d_Performance (Week) | +0.1397 | +0.3542 | -0.0889 | -0.11% | -1.20% | 8725/2866 |
| Performance (Month) | -0.1016 | -0.3963 | +0.2097 | -1.56% | 0.63% | 5293/6275 |
| d_Performance (YTD) | +0.0860 | +0.1202 | +0.0031 | -0.57% | 0.73% | 9380/2025 |
| d_Forward P/E | -0.0796 | +0.0366 | -0.1581 | -1.25% | -0.59% | 2414/532 |
| d_Short Float | +0.0693 | -0.0575 | +0.0919 | -0.96% | -3.11% | 308/372 |
| d_Beta | -0.0687 | -0.1954 | +0.0934 | -1.09% | -0.74% | 2571/2741 |
| Institutional Transactions | -0.0561 | +0.0700 | -0.0764 | 0.28% | -0.54% | 3097/1917 |
| d_Performance (Quarter) | +0.0535 | +0.1344 | -0.0492 | -0.51% | -0.03% | 8587/2607 |
| d_Volatility (Month) | -0.0517 | +0.2340 | -0.2295 | -0.22% | -0.63% | 6062/3778 |
| d_Performance (Month) | +0.0501 | +0.2295 | -0.0694 | -0.34% | -0.49% | 8641/2839 |
| d_Sales Year Over Year TTM | +0.0460 | -0.0172 | +0.0393 | -1.64% | -3.13% | 222/205 |
| d_200-Day Simple Moving Average | +0.0454 | +0.1617 | -0.0742 | -0.41% | -0.25% | 9535/2066 |
| d_Analyst Recom | -0.0354 | +0.0062 | -0.0182 | -2.65% | -1.15% | 148/179 |
| d_Target Price | +0.0350 | -0.0288 | +0.0942 | -1.56% | -2.68% | 393/469 |
| d_Relative Volume | -0.0349 | +0.0399 | -0.0806 | 0.18% | -0.93% | 5596/5750 |
| d_20-Day Simple Moving Average | +0.0332 | +0.2516 | -0.1661 | -0.36% | -0.45% | 9257/2369 |
| d_Insider Transactions | +0.0299 | +0.0395 | +0.0239 | -1.06% | -1.69% | 471/334 |
| true_ret | +0.0292 | +0.2176 | -0.1318 | -0.95% | 0.77% | 9322/1975 |
| d_Sales Growth Quarter Over Quarter | +0.0275 | +0.0235 | +0.0228 | -1.46% | -3.27% | 123/138 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 2139 | -1.06% | 30.9% |
| true_ret>3% & UPTREND | 837 | -2.75% | 14.1% |
| true_ret>3% & MIXED | 642 | -1.55% | 22.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 343 | -2.84% | -5.22% |
| WASHED | 1501 | 3.76% | -0.24% |
