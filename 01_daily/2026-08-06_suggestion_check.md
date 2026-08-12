# Suggestion check — signal **2026-08-06** (full universe)

## What this measures

- **Signal as-of:** **2026-08-06** — `total_score` from data through this day only.
- **Expected UP** if score > +2; **Expected DOWN** if score < −2; else NEUTRAL (excluded from accuracy).
- **Hit** = expected UP and fwd>0, or expected DOWN and fwd<0.
- **fwd** = exit/entry − 1 on a **later** snapshot (not scan.md same-window Ret%).
- **Full universe CSV:** `data/attribution/2026-08-06_suggestion_check.csv`

## Prediction accuracy (full universe)

| Horizon | Pred day | n universe | n actionable | Accuracy | Long acc | Short acc | IC(score,fwd) | Mean fwd long | Mean fwd short |
|---------|----------|------------|--------------|----------|----------|-----------|---------------|---------------|----------------|
| 1d | 2026-08-07 | 11543 | 314 | **58.0%** | 63.3% | 30.0% | +0.0958 | +2.20% | -0.34% |
| 2d | 2026-08-10 | 11518 | 314 | **54.8%** | 60.2% | 26.0% | +0.0636 | +2.49% | +0.43% |
| 3d | 2026-08-11 | 11518 | 314 | **57.6%** | 62.1% | 34.0% | +0.0815 | +3.60% | -0.33% |

## Readable slice — horizon 1d (pred day **2026-08-07**)
_(every ticker is in the CSV)_

### Top 15 scores

| Ticker | Score | Entry | Exit | fwd | Hit? |
|---|---|---|---|---|---|
| FIP | +4.0 | 4.05 | 4.27 | +5.43% | **YES** |
| CBAT | +4.0 | 0.6 | 0.65 | +8.33% | **YES** |
| LIDR | +4.0 | 1.22 | 1.32 | +8.20% | **YES** |
| USGO | +4.0 | 8.47 | 8.64 | +2.01% | **YES** |
| AEVA | +3.3 | 25.26 | 26.62 | +5.38% | **YES** |
| MDU | +3.3 | 20.76 | 20.55 | -1.01% | **NO** |
| AMRC | +3.2 | 25.55 | 25.65 | +0.39% | **YES** |
| ALB | +3.2 | 125.42 | 131.11 | +4.54% | **YES** |
| XE | +3.2 | 20.82 | 22.65 | +8.79% | **YES** |
| AIRJ | +3.2 | 5.59 | 5.92 | +5.90% | **YES** |
| NBIS | +3.2 | 189.88 | 187.97 | -1.01% | **NO** |
| MTSI | +3.2 | 301.64 | 310.82 | +3.04% | **YES** |
| CCLD | +3.0 | 2.32 | 2.63 | +13.36% | **YES** |
| GTIM | +3.0 | 1.42 | 1.47 | +3.52% | **YES** |
| ZTS | +3.0 | 77.27 | 72.66 | -5.97% | **NO** |

### Bottom 10 scores

| Ticker | Score | Entry | Exit | fwd | Hit? |
|---|---|---|---|---|---|
| CAR | -2.8 | 138.35 | 142.18 | +2.77% | **NO** |
| BZFD | -2.8 | 1.13 | 1.16 | +2.65% | **NO** |
| HTT | -2.8 | 2.48 | 2.52 | +1.61% | **NO** |
| HIW | -2.8 | 31.48 | 31.45 | -0.10% | **YES** |
| KG | -2.8 | 8.91 | 8.82 | -1.01% | **YES** |
| HERZ | -2.8 | 15.77 | 15.78 | +0.06% | **NO** |
| TIL | -2.8 | 7.28 | 7.41 | +1.79% | **NO** |
| SGLY | -3.2 | 6.68 | 6.87 | +2.84% | **NO** |
| APGE | -3.2 | 134.49 | 134.84 | +0.26% | **NO** |
| EA | -3.2 | 209.7 | 209.7 | +0.00% | **NO** |
