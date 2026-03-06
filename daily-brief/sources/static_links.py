"""
روابط ثابتة من التكوين (مراجع سريعة).
"""
from pathlib import Path

from core.base import BaseSource, BriefItem, Context


class StaticLinksSource(BaseSource):
    def fetch(self, context: Context | None = None) -> list[BriefItem]:
        root = self.config.get("_root")
        label = self.config.get("label", "مراجع")
        links = self.config.get("links", [])
        items = []
        for link in links:
            title = link.get("title", "")
            url = link.get("url", "")
            if not title and not url:
                continue
            if url and not url.startswith("http") and root:
                path = root / url
                url = str(path) if path.exists() else url
            items.append(
                BriefItem(
                    kind="link",
                    title=title,
                    url=url,
                    description=label,
                    source_name=self.source_name,
                )
            )
        return items
