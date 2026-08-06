"""Map scored themes → exact actionable tickers using the Finviz universe.

Rules:
- Prefer liquid names (avg volume + market cap floors)
- Match by Industry, Sector, description keywords, and PURE_PLAY_HINTS
- Rank by momentum + size quality + keyword hit strength
- Flag extended names (already parabolic)
"""
from __future__ import annotations

import re
from typing import Any

import pandas as pd
import numpy as np

from . import config

THEME_CONFIG: dict[str, dict[str, Any]] = {
    "optics": {
        "industries": [
            "Communication Equipment",
            "Scientific & Technical Instruments",
            "Electronic Components",
            "Semiconductor Equipment & Materials",
        ],
        "desc_keywords": [
            "optical", "transceiver", "photonic", "fiber optic", "laser",
            "optoelectronic", "wavelength", "pluggable", "coherent optics",
        ],
        "hint_boost": ["AAOI", "COHR", "LITE", "GLW", "CIEN", "VIAV", "OCC"],
    },
    "ai power": {
        "industries": [
            "Specialty Industrial Machinery",
            "Electrical Equipment & Parts",
            "Utilities - Independent Power Producers",
            "Utilities - Regulated Electric",
            "Utilities - Renewable",
            "Engineering & Construction",
        ],
        "desc_keywords": [
            "data center", "transformer", "turbine", "grid", "electrification",
            "power management", "ups", "switchgear", "generator",
        ],
        "hint_boost": ["GEV", "VRT", "ETN", "PWR", "HUBB", "EMR", "AYI"],
    },
    "nuclear": {
        "industries": [
            "Uranium",
            "Utilities - Independent Power Producers",
            "Utilities - Regulated Electric",
            "Specialty Industrial Machinery",
        ],
        "desc_keywords": [
            "nuclear", "uranium", "smr", "small modular", "reactor",
            "atomic", "enrichment",
        ],
        "hint_boost": ["CEG", "VST", "TLN", "NRG", "OKLO", "SMR", "CCJ", "UEC", "LEU"],
    },
    "copper": {
        "industries": [
            "Copper",
            "Other Industrial Metals & Mining",
            "Aluminum",
            "Steel",
        ],
        "desc_keywords": [
            "copper", "mining", "concentrate", "cathode", "smelter",
        ],
        "hint_boost": ["FCX", "SCCO", "TECK", "HBM", "ERO"],
    },
    "memory": {
        "industries": ["Semiconductors", "Semiconductor Equipment & Materials"],
        "desc_keywords": [
            "hbm", "high bandwidth memory", "dram", "nand", "memory",
        ],
        "hint_boost": ["MU", "SNDK", "WDC"],
    },
    "connectivity": {
        "industries": ["Semiconductors", "Communication Equipment", "Computer Hardware"],
        "desc_keywords": [
            "serdes", "pcie", "ethernet", "interconnect", "retimer",
            "optical module", "switch fabric",
        ],
        "hint_boost": ["ALAB", "CRDO", "AVGO", "MRVL", "ANET"],
    },
}


def _load_universe() -> pd.DataFrame:
    path = config.FINVIZ_CSV
    if not path.exists():
        alt = config.DATA / "finviz_with_descriptions.csv"
        path = alt if alt.exists() else path
    if not path.exists():
        raise FileNotFoundError(
            f"Finviz universe not found at {config.FINVIZ_CSV}. "
            "Place finviz_universe.csv in data/."
        )
    df = pd.read_csv(path, low_memory=False)
    for c in [
        "Market Cap", "Price", "Average Volume", "Short Float",
        "Performance (Week)", "Performance (Month)", "Performance (Quarter)",
        "Performance (Half Year)", "Performance (YTD)",
    ]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def _match_theme_key(theme_name: str) -> str | None:
    t = theme_name.lower()
    for key in THEME_CONFIG:
        if key in t:
            return key
    if "optic" in t or "transceiver" in t or "photonic" in t:
        return "optics"
    if "power" in t or "electrification" in t or "grid" in t or "turbine" in t:
        return "ai power"
    if "nuclear" in t or "smr" in t or "uranium" in t:
        return "nuclear"
    if "copper" in t or "metal" in t:
        return "copper"
    if "memory" in t or "hbm" in t or "dram" in t:
        return "memory"
    if "connect" in t or "interconnect" in t or "serdes" in t:
        return "connectivity"
    return None


def map_theme(
    theme_name: str,
    pure_play_hints: list[str] | None = None,
    top_n: int = 12,
    min_mcap: float = 80.0,
    min_adv: float = 150.0,
) -> pd.DataFrame:
    df = _load_universe()
    key = _match_theme_key(theme_name)
    cfg = THEME_CONFIG.get(key or "", {})

    industries = cfg.get("industries", [])
    keywords = cfg.get("desc_keywords", [])
    boost = set(cfg.get("hint_boost", []))
    if pure_play_hints:
        boost |= {h.strip().upper() for h in pure_play_hints if h.strip()}

    mask = (
        (df["Market Cap"].fillna(0) >= min_mcap)
        & (df["Average Volume"].fillna(0) >= min_adv)
    )
    ind_mask = df["Industry"].fillna("").isin(industries) if industries else False
    desc = df["Finviz_Description"].fillna("").str.lower()
    kw_mask = False
    for kw in keywords:
        kw_mask = kw_mask | desc.str.contains(re.escape(kw.lower()), na=False)
    hint_mask = df["Ticker"].str.upper().isin(boost)

    combined = mask & (ind_mask | kw_mask | hint_mask)
    sub = df[combined].copy()
    if sub.empty:
        return sub

    sub["kw_hits"] = 0
    for kw in keywords:
        sub["kw_hits"] += desc.loc[sub.index].str.contains(re.escape(kw.lower()), na=False).astype(int)

    sub["hint_boost"] = sub["Ticker"].str.upper().isin(boost).astype(int) * 3
    sub["ind_boost"] = sub["Industry"].fillna("").isin(industries).astype(int) * 2

    q = sub["Performance (Quarter)"].fillna(sub["Performance (YTD)"]).fillna(0)
    q_clipped = q.clip(-50, 250)
    sub["mom_score"] = (q_clipped + 50) / 50
    sub["size_score"] = np.log10(sub["Market Cap"].clip(lower=50))
    sub["rank_score"] = (
        sub["mom_score"] * 1.2
        + sub["size_score"] * 0.6
        + sub["kw_hits"] * 0.8
        + sub["hint_boost"]
        + sub["ind_boost"]
    )

    ytd = sub["Performance (YTD)"].fillna(0)
    half = sub["Performance (Half Year)"].fillna(ytd)
    sub["extended"] = (ytd > 150) | (half > 120)

    sub = sub.sort_values("rank_score", ascending=False).head(top_n)
    cols = [
        "Ticker", "Company", "Industry", "Market Cap", "Price",
        "Performance (Week)", "Performance (Month)", "Performance (Quarter)",
        "Performance (YTD)", "Average Volume", "Short Float",
        "rank_score", "extended", "kw_hits",
    ]
    return sub[[c for c in cols if c in sub.columns]]


def format_buy_list(theme_name: str, table: pd.DataFrame) -> str:
    if table is None or table.empty:
        return f"### {theme_name}\nNo liquid pure plays matched in Finviz universe.\n"

    lines = [f"### {theme_name} — exact candidates", ""]
    lines.append(
        "| Ticker | Company | Industry | Mkt Cap ($M) | Price | Q % | YTD % | Adv | Extended |"
    )
    lines.append("|--------|---------|----------|--------------|-------|-----|-------|-----|----------|")
    for _, r in table.iterrows():
        lines.append(
            f"| **{r['Ticker']}** | {str(r['Company'])[:32]} | {str(r.get('Industry',''))[:28]} | "
            f"{r['Market Cap']:.0f} | {r['Price']:.2f} | "
            f"{r.get('Performance (Quarter)', float('nan')):.1f} | "
            f"{r.get('Performance (YTD)', float('nan')):.1f} | "
            f"{r.get('Average Volume', float('nan')):.0f} | "
            f"{'YES' if r.get('extended') else ''} |"
        )
    lines.append("")
    core = table[~table["extended"].astype(bool)].head(5)["Ticker"].tolist()
    extended = table[table["extended"].astype(bool)]["Ticker"].tolist()
    if core:
        lines.append(f"**Core (less extended):** {', '.join(core)}")
    if extended:
        lines.append(f"**Extended (size carefully):** {', '.join(extended)}")
    lines.append("")
    return "\n".join(lines)


def parse_themes_from_predict(text: str) -> list[dict]:
    themes = []
    blocks = re.findall(
        r"THEME_SCORES_BEGIN(.*?)THEME_SCORES_END",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    for block in blocks:
        entry: dict[str, str] = {}
        for line in block.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                entry[k.strip().upper()] = v.strip()
        if not entry:
            for m in re.finditer(
                r"(THEME|NARRATIVE|TRIGGER|SCARCITY|INSTITUTIONAL|MOMENTUM|KILL_SWITCHES|OVERALL|CONFIDENCE|HORIZON|RATIONALE|PURE_PLAY_HINTS)\s*:\s*([^:]+?)(?=\s(?:THEME|NARRATIVE|TRIGGER|SCARCITY|INSTITUTIONAL|MOMENTUM|KILL_SWITCHES|OVERALL|CONFIDENCE|HORIZON|RATIONALE|PURE_PLAY_HINTS)\s*:|$)",
                block,
                re.I,
            ):
                entry[m.group(1).upper()] = m.group(2).strip()
        if entry.get("THEME"):
            hints = entry.get("PURE_PLAY_HINTS", "")
            entry["_hints"] = [h.strip() for h in re.split(r"[,/]", hints) if h.strip()]
            themes.append(entry)
    return themes


def map_all_from_predict(text: str, top_n: int = 10) -> str:
    themes = parse_themes_from_predict(text)
    if not themes:
        return "## Actionable map\nNo THEME_SCORES blocks parsed.\n"
    parts = ["## Actionable stock map (Finviz universe)", ""]
    for t in themes:
        name = t["THEME"]
        table = map_theme(name, pure_play_hints=t.get("_hints"), top_n=top_n)
        parts.append(format_buy_list(name, table))
    return "\n".join(parts)
