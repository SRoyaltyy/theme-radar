# Predictive audit — horizon **3d**

Generated: 2026-08-12T05:19:35.266845-04:00
Signal dates pooled: **1** (`2026-08-06`)

## 1. Prediction accuracy (composite `total_score`, full universe)

Rule: score > +2 → expect UP; score < −2 → expect DOWN; else neutral.

| Metric | Value |
|--------|-------|
| Names graded | 11518 |
| Actionable (|score|>2) | 314 |
| **Accuracy (actionable)** | **57.6%** |
| Long accuracy | 62.1% |
| Short accuracy | 34.0% |
| Spearman IC(score, fwd) | +0.0815 |

### Per signal date

| Signal | n | Actionable | Accuracy | Long | Short | IC |
|--------|---|------------|----------|------|-------|----|
| 2026-08-06 | 11518 | 314 | 57.6% | 62.1% | 34.0% | +0.0815 |

## 2. Top correlating factors (pooled across dates)

IC = Spearman(factor, forward return). Ranked by |IC|. Spread = mean fwd when factor>0 minus mean fwd when factor<0.

| Rank | Factor | IC | n | Mean fwd if ↑ | Mean fwd if ↓ | Spread |
|------|--------|----|---|---------------|---------------|--------|
| 1 | Performance (Week) | +0.2028 | 11470 | +1.53% | +11.07% | -9.54% |
| 2 | upside_pct | +0.1338 | 4648 | +4.66% | +0.46% | +4.20% |
| 3 | upside_pct_lvl | +0.1337 | 4648 | +4.66% | +0.50% | +4.16% |
| 4 | 20-Day Simple Moving Average | +0.1224 | 11518 | +1.30% | +9.59% | -8.29% |
| 5 | Profit Margin | -0.1143 | 4675 | +0.49% | +21.85% | -21.36% |
| 6 | Analyst Recom | -0.1084 | 4588 | n/a | n/a | n/a |
| 7 | w_pos | +0.0836 | 11518 | n/a | n/a | n/a |
| 8 | total_score | +0.0815 | 11518 | +3.74% | +5.53% | -1.78% |
| 9 | technical_score | +0.0757 | 11518 | +1.07% | +13.78% | -12.71% |
| 10 | n_pos | +0.0743 | 11518 | n/a | n/a | n/a |
| 11 | Short Float | +0.0737 | 5741 | n/a | n/a | n/a |
| 12 | n_neg | -0.0658 | 11518 | n/a | n/a | n/a |
| 13 | Sales Growth Quarter Over Quarter | +0.0643 | 4746 | +2.45% | +4.49% | -2.04% |
| 14 | Relative Strength Index (14) | +0.0623 | 11422 | n/a | n/a | n/a |
| 15 | Sales Year Over Year TTM | +0.0607 | 4536 | +7.10% | +6.93% | +0.16% |
| 16 | cat_copper_metals | +0.0591 | 11518 | n/a | n/a | n/a |
| 17 | Performance (Quarter) | -0.0537 | 10887 | +0.62% | +8.76% | -8.14% |
| 18 | catalyst_score | +0.0531 | 11518 | +2.91% | +4.48% | -1.56% |
| 19 | n_catalysts | +0.0530 | 11518 | n/a | n/a | n/a |
| 20 | valuation_score | +0.0525 | 11518 | +5.05% | +0.50% | +4.54% |
| 21 | w_neg | -0.0486 | 11518 | n/a | n/a | n/a |
| 22 | Institutional Transactions | +0.0453 | 5059 | +14.44% | +3.67% | +10.78% |
| 23 | Forward P/E | +0.0449 | 3061 | n/a | n/a | n/a |
| 24 | Institutional Ownership | -0.0432 | 5844 | n/a | n/a | n/a |
| 25 | Target Price | -0.0376 | 4648 | n/a | n/a | n/a |

## 3. Factor combinations (sign quadrants)

Among stronger single factors: A↑B↑ / A↑B↓ / A↓B↑ / A↓B↓. **Score** = |mean_fwd| × √n (ranking aid only).

| Rank | Combination | n | Mean fwd | % up | % down | Score |
|------|-------------|---|----------|------|--------|-------|
| 1 | Performance (Week)↓ & Profit Margin↓ | 695 | +56.29% | 52.8% | 44.0% | 14.840 |
| 2 | 20-Day Simple Moving Average↓ & Profit Margin↓ | 947 | +42.53% | 56.6% | 38.8% | 13.087 |
| 3 | Profit Margin↓ & total_score↓ | 647 | +39.34% | 53.8% | 41.0% | 10.006 |
| 4 | Profit Margin↓ & w_pos↑ | 1794 | +18.81% | 58.0% | 38.7% | 7.966 |
| 5 | Performance (Week)↓ & 20-Day Simple Moving Average↓ | 2794 | +13.96% | 49.6% | 46.8% | 7.382 |
| 6 | Performance (Week)↓ & w_pos↑ | 2593 | +11.84% | 49.4% | 47.9% | 6.028 |
| 7 | 20-Day Simple Moving Average↓ & w_pos↑ | 3007 | +10.92% | 54.5% | 42.1% | 5.990 |
| 8 | Performance (Week)↓ & total_score↓ | 1927 | +12.97% | 50.5% | 45.0% | 5.694 |
| 9 | 20-Day Simple Moving Average↓ & total_score↓ | 2584 | +10.23% | 54.3% | 40.8% | 5.199 |
| 10 | Profit Margin↓ & total_score↑ | 1149 | +14.33% | 60.0% | 37.6% | 4.857 |
| 11 | upside_pct↑ & Profit Margin↓ | 1501 | +11.87% | 60.0% | 37.2% | 4.599 |
| 12 | upside_pct_lvl↑ & Profit Margin↓ | 1501 | +11.87% | 60.0% | 37.2% | 4.599 |
| 13 | Profit Margin↓ & Analyst Recom↑ | 1575 | +11.20% | 59.0% | 38.2% | 4.444 |
| 14 | 20-Day Simple Moving Average↓ & total_score↑ | 1532 | +9.95% | 54.7% | 42.7% | 3.894 |
| 15 | upside_pct↑ & total_score↓ | 747 | +13.84% | 52.2% | 44.6% | 3.782 |
| 16 | upside_pct_lvl↑ & total_score↓ | 748 | +13.82% | 52.3% | 44.5% | 3.780 |
| 17 | upside_pct↑ & 20-Day Simple Moving Average↓ | 1869 | +8.72% | 52.4% | 45.3% | 3.770 |
| 18 | upside_pct_lvl↑ & 20-Day Simple Moving Average↓ | 1870 | +8.72% | 52.5% | 45.2% | 3.770 |
| 19 | Performance (Week)↓ & total_score↑ | 1415 | +10.00% | 48.3% | 49.8% | 3.762 |
| 20 | Performance (Week)↓ & upside_pct↑ | 1554 | +9.45% | 47.5% | 50.8% | 3.724 |

## Notes

- With few signal dates, treat rankings as **exploratory**.
- `d_*` = day-over-day delta on the signal pair; bare names = levels.
- JSON: `03_scoreboard/predictive_audit_3d.json`
