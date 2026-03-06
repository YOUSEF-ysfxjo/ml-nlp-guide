"""
يقرأ من مجلد New_ara الملفات المحددة في التكوين ويُرجع السياق (المرحلة، الورقة الحالية).
يدعم HTML: لملفات .html يُستخرج النص فقط (بدون وسوم) لاستخدامه في الدليل.
"""
import re
from pathlib import Path

from core.base import BaseContextSource, Context


def _strip_html(html: str) -> str:
    """إزالة الوسوم واستخراج النص من HTML."""
    text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


class NewAraContextSource(BaseContextSource):
    # حد أقصى أحرف لكل ملف في raw (ملفات الدليل الكبير تأخذ أكثر)
    _LIMITS = {
        "ml-nlp-guide.html": 12000,
        "ML_NLP_Paper_Reading_Guide.md": 4000,
        "GOAL_AND_APPROACH.md": 4000,
        "PLAN_RESOURCES_AND_ROADMAP.md": 4000,
    }
    _DEFAULT_LIMIT = 3000

    def get_context(self, root: Path) -> Context:
        context_files = self.config.get("context_files", [])
        if not context_files:
            return Context()

        phase = ""
        current_paper = ""
        current_section = ""
        reminders = []
        raw = {}

        for rel_path in context_files:
            path = root / rel_path
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            limit = self._LIMITS.get(rel_path, self._DEFAULT_LIMIT)
            if rel_path.lower().endswith(".html"):
                raw[rel_path] = _strip_html(text)[:limit]
            else:
                raw[rel_path] = text[:limit]

            if "current_reading" in rel_path:
                phase, current_paper, current_section = self._parse_current_reading(text)
            if "Paper_Reading_Guide" in rel_path and not phase:
                phase = self._infer_phase_from_guide(text)

        return Context(
            phase=phase,
            current_paper=current_paper,
            current_section=current_section,
            reminders=reminders,
            raw=raw,
        )

    def _parse_current_reading(self, text: str) -> tuple[str, str, str]:
        phase, paper, section = "", "", ""
        for line in text.strip().splitlines():
            line = line.strip()
            if line.startswith("phase:") or line.startswith("Phase:"):
                phase = line.split(":", 1)[-1].strip()
            elif line.startswith("paper:") or line.startswith("current_paper:"):
                paper = line.split(":", 1)[-1].strip()
            elif line.startswith("section:") or line.startswith("current_section:"):
                section = line.split(":", 1)[-1].strip()
        return phase, paper, section

    def _infer_phase_from_guide(self, text: str) -> str:
        if "Phase A" in text and "Phase B" not in text[:text.find("Phase A") + 200]:
            return "Phase A"
        if "### Phase A" in text:
            return "Phase A"
        if "### Phase B" in text:
            return "Phase B"
        if "### Phase C" in text:
            return "Phase C"
        return "Phase A"
