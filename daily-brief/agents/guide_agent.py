"""
وكيل الدليل — يستخدم LLM لتوليد دليل يومي طويل وشامل من السياق والعناصر المجموعة.
المشروع يعتمد أساساً على الـ LLM؛ هذا الوكيل هو القلب.
"""
from datetime import date

from core.base import BriefItem, Context
from llm_tools import LLMRunner


def _format_items_for_prompt(items_by_kind: dict[str, list[BriefItem]]) -> str:
    parts = []
    for kind, lst in items_by_kind.items():
        if not lst:
            continue
        label = {"reading": "قراءة اليوم", "update": "أحدث التحديثات (أوراق/مقالات)", "link": "روابط ومصادر"}.get(kind, kind)
        parts.append(f"### {label}")
        for it in lst[:15]:
            parts.append(f"- **{it.title}**")
            if it.url:
                parts.append(f"  الرابط: {it.url}")
            if it.description:
                parts.append(f"  {it.description[:300]}")
        parts.append("")
    return "\n".join(parts)


class GuideAgent:
    """يأخذ السياق والعناصر المجموعة ويطلب من LLM توليد دليل يومي كامل وشامل."""

    def __init__(self, llm_runner: LLMRunner):
        self.llm = llm_runner

    def run(
        self,
        context: Context,
        items_by_kind: dict[str, list[BriefItem]],
    ) -> str:
        """يولّد الدليل اليومي الكامل عبر LLM. يعتمد على وجود مفتاح API."""
        plan_summary = ""
        for rel_path, raw_text in (context.raw or {}).items():
            plan_summary += f"\n--- {rel_path} ---\n{raw_text}\n"

        items_text = _format_items_for_prompt(items_by_kind)

        system = """أنت مرشد تعلم يومي خبير. مهمتك كتابة دليل يومي **واحد** بالعربية: شامل، مفصّل، وعملي.
- الخطة الحالية للمتعلّم: **Phase A فقط** (تمثيل الكلمات — Word2Vec وما يليه). لا تذكر Phase B أو C.
- لديك نصوص من ملفاته: دليل ML/NLP (ml-nlp-guide.html)، خطة القراءة (Phase A)، الأهداف والموارد. استخدمها لاستخلاص تفاصيل دقيقة وربط التوصيات بها.
- مصادر يُفترض أن يتابعها: Hugging Face Trending Papers، Good AI List (Chip Huyen)، MLOps Community (gatewaze.mlops.community)، Papers With Code، ومدونات مثل Chip Huyen و Simon Willison. أدرج في الدليل ما يستحق من «أحدث التحديثات» مع شرح قصير لماذا يناسبه.
- اكتب بضمير المخاطب (أنت، لك). لا تكن عاماً: قدّم خطوات واضحة، أرقام أوراق، أسماء تقنيات (مثل CBOW، Skip-gram)، وتوصيات قابلة للتنفيذ في نفس اليوم."""

        user = f"""المعلومات المتوفرة عن المتعلّم ويومه:

## حالته الحالية (من New_ara)
- المرحلة: {context.phase or 'Phase A'}
- الورقة/المادة الحالية: {context.current_paper or 'غير محددة'}
- القسم: {context.current_section or '-'}

## نصوص من خطته وملفاته (استخلص منها التفاصيل — فيها ml-nlp-guide و Phase A وخططه)
{plan_summary[:14000]}

## عناصر اليوم (أوراق، تحديثات، روابط — من arXiv و Hugging Face و RSS والمراجع)
{items_text}

---

المطلوب: اكتب **دليلاً يومياً كاملاً وشاملاً ومفصّلاً** (لا تختصر). يجب أن يشمل:

1. **افتتاحية:** فقرة أو فقرتان تربط وضعه الحالي (Phase A، الورقة الحالية) بما في الدليل (ml-nlp-guide) وخطة القراءة. كن محدداً (مثلاً: «اليوم تركّز على Word2Vec والتمثيل التوزيعي»).

2. **ما الذي يجب أن يفعله اليوم — بالترتيب:** خطوات مرقّمة وواضحة: ماذا يقرأ بالضبط (اسم الورقة/القسم)، ماذا يفهم (المفاهيم من الدليل)، ماذا يجرّب (مثلاً Gensim، CBOW vs Skip-gram)، وكيف يراجع. اربط كل خطوة بـ Phase A والورقة الحالية.

3. **على ماذا يركز اليوم (تفصيل):** المفاهيم من الورقة والمرحلة (مثلاً CBOW، Skip-gram، negative sampling، الهدف الرياضي، تمثيل المتجهات). استخدم ما في النصوص أعلاه. اذكر أمثلة أو معادلات إن وردت في الدليل.

4. **أحدث التحديثات والروابط — ماذا يستحق النظر:** من قائمة «عناصر اليوم» اختر الأوراق/المقالات/الروابط الأكثر صلة بـ Phase A أو بتمثيل النص/اللغة. لكل عنصر: عنوان، الرابط، وشرح قصير (1–2 جملة) لماذا يناسبه ومتى يطّلع عليه. أدرج أيضاً تذكيراً بمصادر مثل Hugging Face Trending، Good AI List، MLOps Community، Papers With Code.

5. **توصيات عملية:** 1–2 توصية قابلة للتنفيذ اليوم (مشروع مصغّر، تمرين، سكربت، أو خطوة تالية في خطة Phase A). كن محدداً (مثلاً: «استخدم Gensim على نص X وقارن CBOW و Skip-gram»).

6. **تذكيرات من خطته:** إن وُجدت أهداف أو تذكيرات في النصوص، أدرجها بوضوح.

7. **مراجع سريعة:** لخص المراجع والروابط (PLAN_RESOURCES، Papers With Code، HF Trending، Good AI List، MLOps Community، المدونات) مع تذكير متى يفتح كل منها.

النتيجة يجب أن تكون **شاملة ومفصّلة** بحيث لو اتبع المتعلّم الدليل يكون لديه كل ما يحتاج لليوم دون أن يبحث بنفسه. تجنّب العموميات؛ قدّم تفاصيل من النصوص والمصادر أعلاه."""

        try:
            body = self.llm.complete(
                system=system,
                user=user,
                max_tokens=5000,
            )
            today_str = date.today().isoformat()
            return f"# دليلك اليوم — {today_str}\n\n{body}"
        except Exception as e:
            raise RuntimeError(f"فشل توليد الدليل عبر LLM: {e}") from e
