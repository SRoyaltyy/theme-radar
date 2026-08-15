# Suggestion check — signal **2026-08-12** (full universe)

## What this measures

- **Signal as-of:** **2026-08-12** — `total_score` from data through this day only.
- **Expected UP** if score > +2; **Expected DOWN** if score < −2; else NEUTRAL (excluded from accuracy).
- **Hit** = expected UP and fwd>0, or expected DOWN and fwd<0.
- **fwd** = exit/entry − 1 on a **later** snapshot (not scan.md same-window Ret%).
- **Full universe CSV:** `data/attribution/2026-08-12_suggestion_check.csv`

## Prediction accuracy (full universe)

| Horizon | Pred day | n universe | n actionable | Accuracy | Long acc | Short acc | IC(score,fwd) | Mean fwd long | Mean fwd short |
|---------|----------|------------|--------------|----------|----------|-----------|---------------|---------------|----------------|
| 1d | 2026-08-13 | 11553 | 2681 | **42.3%** | 48.4% | 37.6% | -0.0472 | +2.09% | +2.02% |
| 2d | 2026-08-14 | 11552 | 2681 | **48.0%** | 54.8% | 42.8% | +0.0520 | +2.58% | +5.48% |

## Readable slice — horizon 1d (pred day **2026-08-13**)
_(every ticker is in the CSV)_

### Top 15 scores

| Ticker | Score | Entry | Exit | fwd | Hit? |
|---|---|---|---|---|---|
| SLNG | +6.5 | 5.5 | 5.61 | +2.00% | **YES** |
| IVDA | +6.5 | 0.37 | 0.53 | +43.24% | **YES** |
| LITE | +6.3 | 932.47 | 880.41 | -5.58% | **NO** |
| KITT | +6.2 | 1.22 | 1.03 | -15.57% | **NO** |
| FIP | +6.2 | 4.51 | 4.66 | +3.33% | **YES** |
| BRUN | +6.2 | 22.17 | 22.55 | +1.71% | **YES** |
| CIEN | +6.2 | 432.05 | 442.79 | +2.49% | **YES** |
| NRGV | +6.2 | 3.92 | 3.69 | -5.87% | **NO** |
| SBMT | +6.2 | 7.36 | 7.29 | -0.95% | **NO** |
| BKCH | +6.0 | 65.36 | 64.74 | -0.95% | **NO** |
| GMRS | +5.5 | 12.86 | 13.96 | +8.55% | **YES** |
| GPCR | +5.5 | 53.91 | 54.7 | +1.47% | **YES** |
| AKA | +5.5 | 10.99 | 10.73 | -2.37% | **NO** |
| CCEL | +5.5 | 3.88 | 3.89 | +0.26% | **YES** |
| CANG | +5.5 | 2.19 | 2.26 | +3.20% | **YES** |

### Bottom 10 scores

| Ticker | Score | Entry | Exit | fwd | Hit? |
|---|---|---|---|---|---|
| TANH | -5.5 | 0.4 | 0.37 | -7.50% | **YES** |
| PMA | -5.5 | 1.19 | 1.62 | +36.13% | **NO** |
| CSCS | -5.5 | 12.4 | 13.49 | +8.79% | **NO** |
| LITZ | -5.5 | 8.45 | 9.34 | +10.53% | **NO** |
| CBRZ | -5.5 | 6.74 | 8.3 | +23.15% | **NO** |
| TPLX | -5.5 | 20.46 | 20.9 | +2.15% | **NO** |
| BEZ | -5.5 | 8.85 | 8.99 | +1.58% | **NO** |
| MYPS | -5.7 | 0.56 | 0.55 | -1.79% | **YES** |
| GPRO | -6.5 | 0.58 | 0.63 | +8.62% | **NO** |
| TISI | -7.0 | 22.0 | 22.16 | +0.73% | **NO** |
