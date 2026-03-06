"""
مصادر RSS — مدونات، نشرات.
"""
from pathlib import Path

from core.base import BaseSource, BriefItem, Context

try:
    import feedparser
except ImportError:
    feedparser = None


class RSSSource(BaseSource):
    def fetch(self, context: Context | None = None) -> list[BriefItem]:
        if not feedparser:
            return [
                BriefItem(
                    kind="link",
                    title="ثبّت feedparser: pip install feedparser",
                    url="",
                    description="",
                    source_name=self.source_name,
                )
            ]
        feeds = self.config.get("feeds", [])
        items = []
        for feed_config in feeds:
            name = feed_config.get("name", "RSS")
            url = feed_config.get("url", "")
            max_items = feed_config.get("max_items", 1)
            if not url:
                continue
            try:
                feed = feedparser.parse(url)
                for entry in feed.get("entries", [])[:max_items]:
                    link = entry.get("link", "")
                    title = entry.get("title", "").strip()
                    items.append(
                        BriefItem(
                            kind="link",
                            title=title,
                            url=link,
                            description=name,
                            source_name=name,
                        )
                    )
            except Exception:
                items.append(
                    BriefItem(
                        kind="link",
                        title=f"{name} (فشل الجلب)",
                        url=url,
                        description="",
                        source_name=name,
                    )
                )
        return items
