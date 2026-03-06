"""
وكيل الجمع — يشغّل كل المصادر المفعّلة (قراءة، arXiv، RSS، روابط ثابتة) ويُرجع العناصر مجمّعة.
"""
from pathlib import Path

from core.base import BriefItem, Context
from sources import (
    HFTrendingSource,
    LatestUpdatesSource,
    ReadingPlanSource,
    RSSSource,
    StaticLinksSource,
)


class GatherAgent:
    """يشغّل المصادر حسب التكوين ويُرجع العناصر مجمّعة حسب النوع (reading, update, link)."""

    def __init__(self, sources_config: dict, new_ara_root: Path):
        self.sources_config = sources_config
        self.root = new_ara_root.resolve()
        for key in ("reading_plan", "static_links"):
            if key in sources_config and isinstance(sources_config[key], dict):
                sources_config[key]["_root"] = self.root

    def run(self, context: Context) -> dict[str, list[BriefItem]]:
        """يشغّل المصادر ويُرجع by_kind: { "reading": [...], "update": [...], "link": [...] }."""
        items: list[BriefItem] = []

        rp = self.sources_config.get("reading_plan", {})
        if rp.get("enabled"):
            src = ReadingPlanSource("reading_plan", rp)
            items.extend(src.fetch(context))

        lu = self.sources_config.get("latest_updates", {})
        if lu.get("enabled"):
            src = LatestUpdatesSource("latest_updates", lu)
            items.extend(src.fetch(context))

        rss = self.sources_config.get("rss", {})
        if rss.get("enabled"):
            src = RSSSource("rss", rss)
            items.extend(src.fetch(context))

        hf = self.sources_config.get("hf_trending", {})
        if hf.get("enabled"):
            src = HFTrendingSource("hf_trending", hf)
            items.extend(src.fetch(context))

        sl = self.sources_config.get("static_links", {})
        if sl.get("enabled"):
            src = StaticLinksSource("static_links", sl)
            items.extend(src.fetch(context))

        by_kind: dict[str, list[BriefItem]] = {}
        for it in items:
            by_kind.setdefault(it.kind, []).append(it)
        return by_kind
