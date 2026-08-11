# Regime questionnaire — Step B of label → regime → join

**Status: design contract. Not yet implemented as code.**
Step A (deep labeling, `src/segments.py` + `segments.json`) is live and answers
*"what is this stock?"*. This document defines the machine-fillable daily
template that answers the second question:

> **Given what we know about the market today, is the environment good for
> tags of type T?**

Only when both machines run do we join them: names whose labels land in
today's *favorable* set, minus *hostile* gates, are the actionable Venn.

---

## 1. Daily template (the regime engine must fill this, every day)

One object per label that actually exists in today's membership file:

```json
{
  "date": "YYYY-MM-DD",
  "regimes": {
    "beta:high": {
      "stance": "favorable | neutral | hostile | unknown",
      "confidence": "low | medium | high",
      "why": "one line, plain words",
      "sources": ["channel1", "general_predict", "sector_predict", "news", "index_tape"]
    }
  }
}
```

- **stance** — is TODAY good for this label? `unknown` is a legitimate,
  honest answer; never force a call.
- **confidence** — how much evidence agrees.
- **why** — one sentence max, must name the evidence.
- **sources** — which inputs voted (see §2).

Proposed output location once built: `01_daily/regime/<date>_regime.json`
+ a human `<date>_regime.md`.

## 2. Inputs the regime engine reads (all exist today)

| Input | Role | Where it lives |
|---|---|---|
| Channel 1 | rates, USD, VIX, futures, oil, breadth, overnight | fullscan `01_daily/_channel1/` |
| General market predict | risk-on / risk-off / mixed for the index world | fullscan `01_daily/general/` |
| Sector predicts (11) | Lead/Lag per sector | fullscan `01_daily/sectors/` |
| Event scan | scheduled/ongoing macro & policy events | fullscan `01_daily/events/` |
| News edges | catalyst direction per theme/bucket | fullscan `01_daily/news/` |
| Index tape | Dow vs NDX vs RUT leadership → size/style read | yfinance (already a dep) |
| Segment stats | the universe's own cross-section that day | theme-radar `data/universe/` |
| Supabase tables | stored filings/news/macro history | Supabase (existing) |

## 3. Question → stance logic sketches (hypotheses to encode, NOT backtested)

| Question | Favorable when | Hostile when |
|---|---|---|
| `sector:X` / `industry:Y` | sector predict = Lead + industry breadth up / aligned theme | predict = Lag + negative news edge |
| `size:small/micro` | risk-on, soft USD, easy conditions, RUT ≥ NDX/SPX | tight liquidity, strong USD, mega-only leadership |
| `size:large/mega` | mega index leadership, quality/defensive bid | broad small-cap risk-on (relative lag) |
| `beta:low` | risk-off, rising vol, flight to safety | strong risk-on, high-beta leadership |
| `beta:high` | risk-on, vol falling, breadth expanding | vol spike, gap-down macro, liquidity stress |
| `short:high/extreme` | risk-on + rising tape → squeeze fuel | gap-down + stress → dilution paths; never "bullish" by default |
| `liq:low` | quiet regime | macro stress → max pain, gaps |
| `rvol:hot` | participation confirms the move is real | high RVol + down day = distribution |
| `profit:yes` | tightening / higher rates / quality regime | speculative melt-up (lags, mild) |
| `profit:no` | easy money, speculative bid | QT / credit stress / risk-off |
| `lev:high` | easing, falling yields, risk-on | rising yields, credit stress — amplifies downside |
| `style:growth` | falling real yields, dovish path | rising real yields, hawkish reprice |
| `style:value` | rising yields, reflation, cyclical recovery | pure duration rally into growth |
| `mom:uptrend` / `ext:*` | trend/continuation regime | mean-revert day, post-parabolic VIX crush |
| `range:top` | breakout + volume regime | exhaustion + risk-off |
| `range:deep_low` | washout + risk-on turn | falling knife in risk-off |

**Special rule:** `short:high` and `lev:high` are regime *multipliers*, not
bullish tags. Their stance should often read "favorable for a squeeze" /
"hostile under stress" / "neutral — ignore as alpha".

## 4. Hard gates (applied at the JOIN, not here)

- `ext:extreme` + risk-off → cap long scores.
- `liq:low` → exclude or down-rank for size.
- `earn:today|this_week` → flag; not a pure segment bet (activates when the
  export includes Earnings Date).
- `short:extreme` + already parabolic week → squeeze-risk flag, not a
  "quality long".

## 5. Composite formula (Step C, after A and B stabilize)

```
S_name = Σ_k  w_k · M_ik · E_k
  M_ik = membership of name i in segment k   (Step A, done)
  E_k  = stance of segment k today mapped to favorable=+1, neutral=0, hostile=−1
  w_k  = weight — equal within family at first, learned later
```

Stance numeric mapping and family weights are the LAST thing to tune — only
after the label side is trusted and the regime table has accumulated enough
days to backtest against.

## 6. Build order reminder

1. ✅ Step A — registry + membership + segment stats (this repo, live)
2. ⬜ Step B — regime engine that fills §1 daily from §2 inputs
3. ⬜ Step C — join + composite + ranked universe table
4. ⬜ Backtest — only after A trusted and B stable (their own words:
   "Backtest is reserved for AFTER we manage to label all stocks correctly")
