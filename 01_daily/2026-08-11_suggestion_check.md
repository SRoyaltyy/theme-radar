# Suggestion check — signal **2026-08-11** (full universe)

## What this measures

- **Signal as-of:** **2026-08-11** — `total_score` from data through this day only.
- **Expected UP** if score > +2; **Expected DOWN** if score < −2; else NEUTRAL (excluded from accuracy).
- **Hit** = expected UP and fwd>0, or expected DOWN and fwd<0.
- **fwd** = exit/entry − 1 on a **later** snapshot (not scan.md same-window Ret%).
- **Full universe CSV:** `data/attribution/2026-08-11_suggestion_check.csv`

## Prediction accuracy (full universe)

| Horizon | Pred day | n universe | n actionable | Accuracy | Long acc | Short acc | IC(score,fwd) | Mean fwd long | Mean fwd short |
|---------|----------|------------|--------------|----------|----------|-----------|---------------|---------------|----------------|
| 1d | 2026-08-12 | 11543 | 3818 | **51.0%** | 51.5% | 50.4% | +0.1007 | +0.70% | -0.13% |
| 2d | 2026-08-13 | 11543 | 3818 | **46.9%** | 51.8% | 40.7% | +0.0174 | +1.35% | +2.75% |
| 3d | 2026-08-14 | 11542 | 3817 | **49.4%** | 54.5% | 42.8% | +0.0639 | +2.71% | +4.30% |

## Readable slice — horizon 1d (pred day **2026-08-12**)
_(every ticker is in the CSV)_

### Top 15 scores

| Ticker | Score | Entry | Exit | fwd | Hit? |
|---|---|---|---|---|---|
| RIOT | +9.0 | 20.24 | 20.32 | +0.40% | **YES** |
| RUM | +9.0 | 6.92 | 7.55 | +9.10% | **YES** |
| ZENA | +8.5 | 1.82 | 1.9 | +4.40% | **YES** |
| ACHR | +8.5 | 6.79 | 6.29 | -7.36% | **NO** |
| KOPN | +8.5 | 5.2 | 5.02 | -3.46% | **NO** |
| BGDE | +8.2 | 6.0 | 6.4 | +6.67% | **YES** |
| TH | +8.2 | 16.62 | 16.14 | -2.89% | **NO** |
| FNUC | +8.2 | 1.86 | 1.85 | -0.54% | **NO** |
| SINT | +8.0 | 1.77 | 1.57 | -11.30% | **NO** |
| RPC | +8.0 | 8.85 | 8.82 | -0.34% | **NO** |
| HFFG | +8.0 | 1.78 | 1.84 | +3.37% | **YES** |
| CTNM | +8.0 | 14.82 | 14.98 | +1.08% | **YES** |
| LOCL | +8.0 | 1.26 | 1.06 | -15.87% | **NO** |
| DOMH | +8.0 | 3.14 | 2.92 | -7.01% | **NO** |
| IGC | +8.0 | 0.28 | 0.29 | +3.57% | **YES** |

### Bottom 10 scores

| Ticker | Score | Entry | Exit | fwd | Hit? |
|---|---|---|---|---|---|
| KLC | -7.8 | 4.78 | 4.64 | -2.93% | **YES** |
| GRNQ | -7.8 | 9.26 | 9.2 | -0.65% | **YES** |
| FEDU | -7.8 | 6.91 | 7.54 | +9.12% | **NO** |
| INNV | -7.8 | 10.23 | 10.43 | +1.96% | **NO** |
| WILC | -7.8 | 27.1 | 27.65 | +2.03% | **NO** |
| BXC | -8.2 | 89.88 | 89.22 | -0.73% | **YES** |
| GPRO | -8.5 | 0.62 | 0.58 | -6.45% | **YES** |
| ACFN | -8.5 | 17.97 | 18.37 | +2.23% | **NO** |
| HUBG | -8.5 | 38.0 | 40.21 | +5.82% | **NO** |
| EVC | -8.5 | 9.23 | 9.02 | -2.28% | **YES** |
