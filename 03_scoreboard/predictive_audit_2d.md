# Predictive audit — horizon **2d**

Generated: 2026-08-12T05:19:34.299637-04:00
Signal dates pooled: **2** (`2026-08-06, 2026-08-07`)

## 1. Prediction accuracy (composite `total_score`, full universe)

Rule: score > +2 → expect UP; score < −2 → expect DOWN; else neutral.

| Metric | Value |
|--------|-------|
| Names graded | 23043 |
| Actionable (|score|>2) | 4663 |
| **Accuracy (actionable)** | **47.7%** |
| Long accuracy | 47.2% |
| Short accuracy | 48.9% |
| Spearman IC(score, fwd) | -0.0071 |

### Per signal date

| Signal | n | Actionable | Accuracy | Long | Short | IC |
|--------|---|------------|----------|------|-------|----|
| 2026-08-06 | 11518 | 314 | 54.8% | 60.2% | 26.0% | +0.0636 |
| 2026-08-07 | 11525 | 4349 | 47.2% | 46.0% | 49.7% | -0.0242 |

## 2. Top correlating factors (pooled across dates)

IC = Spearman(factor, forward return). Ranked by |IC|. Spread = mean fwd when factor>0 minus mean fwd when factor<0.

| Rank | Factor | IC | n | Mean fwd if ↑ | Mean fwd if ↓ | Spread |
|------|--------|----|---|---------------|---------------|--------|
| 1 | Beta | -0.0989 | 9755 | +4.06% | +0.94% | +3.12% |
| 2 | Total Debt/Equity | -0.0901 | 5043 | n/a | n/a | n/a |
| 3 | upside_pct_lvl | +0.0899 | 9298 | +3.47% | -0.06% | +3.53% |
| 4 | upside_pct | +0.0899 | 9298 | +3.47% | -0.09% | +3.56% |
| 5 | d_Price | -0.0872 | 11518 | -0.23% | +11.62% | -11.85% |
| 6 | Analyst Recom | -0.0830 | 9178 | n/a | n/a | n/a |
| 7 | d_Performance (Week) | -0.0814 | 11470 | +0.90% | +8.10% | -7.20% |
| 8 | d_20-Day Simple Moving Average | -0.0772 | 11518 | +0.10% | +12.65% | -12.55% |
| 9 | d_200-Day Simple Moving Average | -0.0758 | 11518 | -0.02% | +13.12% | -13.15% |
| 10 | d_50-Day Simple Moving Average | -0.0733 | 11518 | -0.01% | +12.97% | -12.98% |
| 11 | d_Performance (YTD) | -0.0713 | 11509 | -0.22% | +10.09% | -10.32% |
| 12 | true_ret | -0.0711 | 11518 | -0.23% | +11.62% | -11.85% |
| 13 | Profit Margin | -0.0646 | 9354 | +0.05% | +19.95% | -19.90% |
| 14 | Performance (Week) | +0.0642 | 22949 | +0.55% | +12.43% | -11.88% |
| 15 | n_pos | -0.0637 | 23043 | n/a | n/a | n/a |
| 16 | 20-Day Simple Moving Average | +0.0615 | 23043 | +0.52% | +9.64% | -9.11% |
| 17 | Relative Strength Index (14) | +0.0596 | 22851 | n/a | n/a | n/a |
| 18 | Sales Growth Quarter Over Quarter | +0.0558 | 9492 | +1.77% | +4.22% | -2.45% |
| 19 | Institutional Ownership | -0.0530 | 11690 | n/a | n/a | n/a |
| 20 | Sales Year Over Year TTM | +0.0519 | 9076 | +6.94% | +6.12% | +0.82% |
| 21 | Performance (Month) | +0.0495 | 22694 | +0.46% | +8.29% | -7.83% |
| 22 | cat_copper_metals | +0.0454 | 23043 | n/a | n/a | n/a |
| 23 | d_Relative Strength Index (14) | -0.0437 | 11422 | -0.22% | +14.33% | -14.56% |
| 24 | n_neg | -0.0437 | 23043 | n/a | n/a | n/a |
| 25 | d_Performance (Quarter) | -0.0424 | 10887 | -0.00% | +15.46% | -15.47% |

## 3. Factor combinations (sign quadrants)

Among stronger single factors: A↑B↑ / A↑B↓ / A↓B↑ / A↓B↓. **Score** = |mean_fwd| × √n (ranking aid only).

| Rank | Combination | n | Mean fwd | % up | % down | Score |
|------|-------------|---|----------|------|--------|-------|
| 1 | d_200-Day Simple Moving Average↓ & d_50-Day Simple Moving Average↓ | 2688 | +13.92% | 51.5% | 44.7% | 7.218 |
| 2 | d_20-Day Simple Moving Average↓ & d_200-Day Simple Moving Average↓ | 2604 | +13.98% | 51.8% | 44.7% | 7.133 |
| 3 | d_20-Day Simple Moving Average↓ & d_50-Day Simple Moving Average↓ | 2661 | +13.70% | 51.6% | 44.7% | 7.067 |
| 4 | d_Performance (Week)↓ & d_20-Day Simple Moving Average↓ | 2042 | +15.00% | 54.2% | 42.9% | 6.780 |
| 5 | d_Performance (Week)↓ & d_200-Day Simple Moving Average↓ | 2042 | +15.00% | 53.5% | 43.3% | 6.778 |
| 6 | d_Performance (Week)↓ & d_50-Day Simple Moving Average↓ | 2045 | +14.98% | 53.7% | 43.1% | 6.773 |
| 7 | d_Price↓ & true_ret↓ | 2677 | +11.62% | 51.0% | 46.2% | 6.011 |
| 8 | d_Price↓ & d_50-Day Simple Moving Average↓ | 2531 | +11.64% | 51.3% | 45.8% | 5.855 |
| 9 | d_50-Day Simple Moving Average↓ & true_ret↓ | 2531 | +11.64% | 51.3% | 45.8% | 5.855 |
| 10 | d_Price↓ & d_200-Day Simple Moving Average↓ | 2582 | +11.40% | 51.2% | 46.0% | 5.793 |
| 11 | d_200-Day Simple Moving Average↓ & true_ret↓ | 2582 | +11.40% | 51.2% | 46.0% | 5.793 |
| 12 | d_Price↓ & d_20-Day Simple Moving Average↓ | 2455 | +11.58% | 51.4% | 45.8% | 5.740 |
| 13 | d_20-Day Simple Moving Average↓ & true_ret↓ | 2455 | +11.58% | 51.4% | 45.8% | 5.740 |
| 14 | d_Performance (Week)↓ & d_Performance (YTD)↓ | 1997 | +11.88% | 53.5% | 43.5% | 5.308 |
| 15 | d_Price↓ & d_Performance (Week)↓ | 1959 | +11.59% | 53.7% | 43.6% | 5.130 |
| 16 | d_Performance (Week)↓ & true_ret↓ | 1959 | +11.59% | 53.7% | 43.6% | 5.130 |
| 17 | d_Price↓ & d_Performance (YTD)↓ | 2668 | +9.89% | 51.0% | 46.2% | 5.107 |
| 18 | d_Performance (YTD)↓ & true_ret↓ | 2668 | +9.89% | 51.0% | 46.2% | 5.107 |
| 19 | d_50-Day Simple Moving Average↓ & d_Performance (YTD)↓ | 2563 | +10.03% | 51.2% | 45.7% | 5.080 |
| 20 | d_200-Day Simple Moving Average↓ & d_Performance (YTD)↓ | 2619 | +9.88% | 51.1% | 45.9% | 5.058 |

## Notes

- With few signal dates, treat rankings as **exploratory**.
- `d_*` = day-over-day delta on the signal pair; bare names = levels.
- JSON: `03_scoreboard/predictive_audit_2d.json`
