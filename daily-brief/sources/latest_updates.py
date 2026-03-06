"""
أحدث التحديثات — من arXiv (cs.CL) كأوراق حديثة. لاحقاً Papers with Code أو Hugging Face.
"""
from pathlib import Path

from core.base import BaseSource, BriefItem, Context

try:
    import feedparser
except ImportError:
    feedparser = None


ARXIV_RSS = "http://rss.arxiv.org/rss/cs.CL"


class LatestUpdatesSource(BaseSource):
    def fetch(self, context: Context | None = None) -> list[BriefItem]:
        if not feedparser:
            return [
                BriefItem(
                    kind="update",
                    title="ثبّت feedparser: pip install feedparser",
                    url="",
                    description="",
                    source_name=self.source_name,
                )
            ]
        max_items = self.config.get("max_items", 5)
        category = self.config.get("arxiv_category", "cs.CL")
        url = f"http://rss.arxiv.org/rss/{category}"
        try:
            feed = feedparser.parse(url)
            items = []
            for entry in feed.get("entries", [])[:max_items]:
                link = entry.get("link", "")
                title = entry.get("title", "").strip()
                summary = (entry.get("summary", "") or "")[:200].replace("\n", " ")
                items.append(
                    BriefItem(
                        kind="update",
                        title=title,
                        url=link,
                        description=summary,
                        source_name="arXiv " + category,
                    )
                )
            return items
        except Exception as e:
            return [
                BriefItem(
                    kind="update",
                    title="لم نتمكن من جلب أحدث الأوراق",
                    url=url,
                    description=str(e),
                    source_name=self.source_name,
                )
            ]
