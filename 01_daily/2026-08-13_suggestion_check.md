# Suggestion check — signal **2026-08-13** (full universe)

## What this measures

- **Signal as-of:** **2026-08-13** — `total_score` from data through this day only.
- **Expected UP** if score > +2; **Expected DOWN** if score < −2; else NEUTRAL (excluded from accuracy).
- **Hit** = expected UP and fwd>0, or expected DOWN and fwd<0.
- **fwd** = exit/entry − 1 on a **later** snapshot (not scan.md same-window Ret%).
- **Full universe CSV:** `data/attribution/2026-08-13_suggestion_check.csv`

## Prediction accuracy (full universe)

| Horizon | Pred day | n universe | n actionable | Accuracy | Long acc | Short acc | IC(score,fwd) | Mean fwd long | Mean fwd short |
|---------|----------|------------|--------------|----------|----------|-----------|---------------|---------------|----------------|
| 1d | 2026-08-14 | 11566 | 2961 | **41.3%** | 43.6% | 39.3% | -0.0908 | -0.27% | +0.80% |

## Readable slice — horizon 1d (pred day **2026-08-14**)
_(every ticker is in the CSV)_

### Top 15 scores

| Ticker | Score | Entry | Exit | fwd | Hit? |
|---|---|---|---|---|---|
| OXBR | +7.0 | 1.3 | 1.53 | +17.69% | **YES** |
| SNDK | +6.3 | 1528.11 | 1641.11 | +7.39% | **YES** |
| HYLN | +6.3 | 4.11 | 4.06 | -1.22% | **NO** |
| XE | +6.3 | 22.73 | 20.98 | -7.70% | **NO** |
| PXLW | +5.8 | 7.18 | 6.98 | -2.79% | **NO** |
| ACHR | +5.8 | 6.97 | 6.62 | -5.02% | **NO** |
| GMTL | +5.5 | 13.59 | 12.91 | -5.00% | **NO** |
| LAC | +5.5 | 3.43 | 3.38 | -1.46% | **NO** |
| SHEN | +5.5 | 13.43 | 13.27 | -1.19% | **NO** |
| OKLO | +5.5 | 46.45 | 44.38 | -4.46% | **NO** |
| MP | +5.5 | 55.66 | 58.74 | +5.53% | **YES** |
| FNUC | +5.5 | 1.92 | 1.82 | -5.21% | **NO** |
| CIEN | +5.5 | 442.79 | 428.77 | -3.17% | **NO** |
| NNE | +5.5 | 20.52 | 19.66 | -4.19% | **NO** |
| FIP | +5.5 | 4.66 | 4.51 | -3.22% | **NO** |

### Bottom 10 scores

| Ticker | Score | Entry | Exit | fwd | Hit? |
|---|---|---|---|---|---|
| KJD | -5.5 | 17.79 | 17.58 | -1.18% | **YES** |
| SPRU | -5.5 | 1.83 | 1.84 | +0.55% | **NO** |
| VBIO | -5.5 | 0.17 | 0.19 | +11.76% | **NO** |
| VALG | -5.5 | 15.36 | 15.16 | -1.30% | **YES** |
| BAOS | -5.5 | 0.6 | 0.5 | -16.67% | **YES** |
| SNDQ | -5.5 | 17.43 | 14.84 | -14.86% | **YES** |
| ZNB | -5.5 | 2.34 | 2.08 | -11.11% | **YES** |
| PMTS | -5.7 | 29.0 | 28.5 | -1.72% | **YES** |
| HRB | -6.3 | 53.34 | 53.92 | +1.09% | **NO** |
| SCOR | -6.5 | 6.07 | 6.2 | +2.14% | **NO** |
