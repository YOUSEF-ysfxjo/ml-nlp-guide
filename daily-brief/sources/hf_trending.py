"""
أوراق Hugging Face الشائعة — يجلب عناوين وروابط من صفحة Trending Papers.
"""
import re

from core.base import BaseSource, BriefItem, Context

HF_TRENDING_URL = "https://huggingface.co/papers/trending"


class HFTrendingSource(BaseSource):
    """يجلب أوراقاً من صفحة Hugging Face Trending Papers (تحليل HTML بسيط)."""

    def fetch(self, context: Context | None = None) -> list[BriefItem]:
        max_items = self.config.get("max_items", 5)
        try:
            import urllib.request
            req = urllib.request.Request(HF_TRENDING_URL, headers={"User-Agent": "DailyBrief/1.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode("utf-8", errors="replace")
        except Exception as e:
            return [
                BriefItem(
                    kind="update",
                    title="Hugging Face Trending — لم يتم الجلب",
                    url=HF_TRENDING_URL,
                    description=str(e)[:150],
                    source_name=self.source_name,
                )
            ]
        items = []
        # استخراج روابط أوراق: نمط روابط /papers/...
        pattern = r'href="(/papers/[^"]+)"[^>]*>([^<]+)</a>'
        seen = set()
        for m in re.finditer(pattern, html):
            slug = m.group(1)
            title = m.group(2).strip()
            if len(title) < 10 or slug in seen:
                continue
            seen.add(slug)
            url = "https://huggingface.co" + slug if slug.startswith("/") else slug
            items.append(
                BriefItem(
                    kind="update",
                    title=title[:200],
                    url=url,
                    description="Hugging Face — ورقة شائعة",
                    source_name="HF Trending",
                )
            )
            if len(items) >= max_items:
                break
        if not items:
            items.append(
                BriefItem(
                    kind="link",
                    title="Hugging Face Trending Papers",
                    url=HF_TRENDING_URL,
                    description="افتح الرابط لرؤية الأوراق الشائعة",
                    source_name=self.source_name,
                )
            )
        return items
