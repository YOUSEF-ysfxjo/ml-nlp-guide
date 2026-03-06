"""
قراءة اليوم من Paper Reading Guide و current_reading.
"""
from pathlib import Path

from core.base import BaseSource, BriefItem, Context


class ReadingPlanSource(BaseSource):
    def fetch(self, context: Context | None = None) -> list[BriefItem]:
        root = self.config.get("_root")
        if not root:
            return []
        path_guide = root / self.config.get("path_guide", "ML_NLP_Paper_Reading_Guide.md")
        path_current = root / self.config.get("path_current", "brief/current_reading.md")

        title = "قراءة اليوم"
        description = ""
        url = ""

        if path_current.exists():
            text = path_current.read_text(encoding="utf-8", errors="replace")
            for line in text.strip().splitlines():
                line = line.strip()
                if line.startswith("paper:") or line.startswith("current_paper:"):
                    title = line.split(":", 1)[-1].strip() or title
                elif line.startswith("phase:") or line.startswith("Phase:"):
                    description = f"المرحلة: {line.split(':', 1)[-1].strip()}"
            if context and context.current_paper:
                title = context.current_paper
            if context and context.phase:
                description = f"المرحلة: {context.phase}"

        if path_guide.exists():
            url = str(path_guide)

        return [
            BriefItem(
                kind="reading",
                title=title or "حدّث brief/current_reading.md",
                url=url,
                description=description or "افتح Paper Reading Guide واختر الورقة التالية.",
                source_name=self.source_name,
            )
        ]
