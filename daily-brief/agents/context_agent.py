"""
وكيل السياق — يقرأ مجلد New_ara ويستخرج المرحلة والورقة الحالية وملخص الخطط.
"""
from pathlib import Path

from core.base import Context
from sources import NewAraContextSource


class ContextAgent:
    """يقرأ الملفات المحددة من New_ara ويُرجع Context (المرحلة، الورقة، النص الخام للخطط)."""

    def __init__(self, context_files: list[str], source_name: str = "new_ara_context"):
        self.context_files = context_files
        self._source = NewAraContextSource(
            source_name,
            {"context_files": context_files},
        )

    def run(self, new_ara_root: Path) -> Context:
        """يشغّل القراءة من new_ara_root ويُرجع Context."""
        root = new_ara_root.resolve()
        return self._source.get_context(root)
