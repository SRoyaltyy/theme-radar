# Theme Radar

**Closed-loop Theme & Sector Rally Predictor**

Detects high-confidence market themes/concepts that are likely to rally over the coming weeks/months, maps them to pure-play stocks using a Finviz universe, and improves over time through a predict → outcome → reflect → distill lessons loop.

Inspired by (and largely compatible with) the architecture of `SRoyaltyy/fullscan`.

## Core Loop

1. **Predict** – LLM (DeepSeek) + live search analyzes macro, policy, earnings language, flows, and price action to surface 3–7 high-conviction themes.
2. **Map** – Each theme is turned into an actionable watchlist of pure-play / high-exposure stocks from the Finviz universe.
3. **Outcome** – After a defined horizon (e.g. 4–8 weeks), measure how the pure-play baskets actually performed.
4. **Reflect** – The system diagnoses what it got right/wrong, updates assumptions, and proposes prompt/architecture changes.
5. **Distill** – Lessons are promoted into standing memory so future runs get smarter.

## Folder Structure

```
00_grounding/          # Core prompts & rubric (the "brain")
01_daily/              # Daily/periodic prediction outputs
02_lessons/            # Standing lessons learned
03_scoreboard/         # Accuracy tracking
04_archive/            # Long-term memory
src/                   # Pipeline code
data/                  # Finviz universe & derived indexes
```

## Key Design Principles (inherited from fullscan)

- Strict separation of **Channel 1** (deterministic / pre-fetched data) vs **Channel 2** (LLM must actively search).
- Forced memory confirmation as the first output line.
- Machine-readable `THEME_SCORES` blocks that the pipeline parses.
- Deterministic scoring / ranking after the LLM (do not trust the model to do arithmetic).
- Closed feedback loop so the system can rewrite its own assumptions and prompts over time.

## Status

Initial scaffolding. The `master_rubric.md` and core runners are the next priority.
