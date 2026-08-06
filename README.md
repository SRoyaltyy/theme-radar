# Theme Radar

**Closed-loop Theme & Sector Rally Predictor**

Detects high-confidence market themes/concepts likely to rally over the coming weeks/months, maps them to pure-play stocks, and improves through predict → outcome → reflect → distill.

Architecture mirrors `SRoyaltyy/fullscan`.

## How research works

Every predict run forces the model through a staged process:

1. **Stage 1 – Broad Discovery**  
   Live web search across macro/policy, hyperscaler CapEx, commodities, analyst notes, and price-action clusters. Surfaces 8–15 candidate narratives.

2. **Stage 2 – Hard Trigger Filter**  
   Only candidates with a concrete, dated trigger in the last 14–21 days survive.

3. **Stage 3 – Five-Layer Scoring**  
   Narrative / Trigger / Scarcity / Institutional / Momentum + Kill Switches.

4. **Output**  
   Structured `THEME_SCORES` blocks that the pipeline can parse and later map to stocks via the Finviz universe.

## Secrets (same names as fullscan)

In GitHub → Settings → Secrets and variables → Actions, add:

- `DEEPSEEK_API_KEY` (required)
- `SEARXNG_URL` (optional but recommended)
- `FRED_API_KEY` (optional for later Channel 1)

You can copy the values from the fullscan repository secrets.

## Run

**Manual (GitHub Actions)**  
Actions → Theme Radar Predict → Run workflow

**Local**
```bash
export DEEPSEEK_API_KEY=...
export SEARXNG_URL=...   # optional
pip install -r requirements.txt
python -m src.run_predict
```

## Status

- Predict stage is operational (DeepSeek + web_search tool loop)
- Outcome / Reflect / Finviz pure-play mapper still to be built
- Channel 1 is currently a placeholder (model relies on live search)
