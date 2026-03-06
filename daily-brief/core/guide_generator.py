"""
مولّد الدليل اليومي — يقرأ السياق وكل العناصر ويبني ملخصاً طويلاً كأنه مرشد يحدد لك ماذا تسوي اليوم.
يدعم LLM (اختياري): لو OPENAI_API_KEY موجود يولد نص إرشادي؛ وإلا قالب تفصيلي بدون AI.
"""
from datetime import date
from pathlib import Path

from core.base import BriefItem, Context


def _format_items_for_prompt(items_by_kind: dict[str, list[BriefItem]]) -> str:
    parts = []
    for kind, lst in items_by_kind.items():
        if not lst:
            continue
        parts.append(f"[{kind}]")
        for it in lst[:10]:
            parts.append(f"  - {it.title}")
            if it.url:
                parts.append(f"    {it.url}")
            if it.description:
                parts.append(f"    {it.description[:200]}")
        parts.append("")
    return "\n".join(parts)


def build_guide_with_llm(
    context: Context,
    items_by_kind: dict[str, list[BriefItem]],
    plan_summary: str,
    api_key: str,
) -> str:
    """يستخدم LLM (OpenAI) لتوليد دليل يومي طويل بإسلوب مرشد."""
    try:
        from openai import OpenAI
    except ImportError:
        return build_guide_template(context, items_by_kind, plan_summary)

    client = OpenAI(api_key=api_key)
    items_text = _format_items_for_prompt(items_by_kind)

    prompt = f"""أنت مرشد يومي لشخص يتبع خطة تعلم (New_ara: ML/NLP من الأساسيات للـ embeddings).
لديك المعلومات التالية عن حالته اليوم:

## حالته الحالية
- المرحلة: {context.phase or 'غير محددة'}
- الورقة الحالية: {context.current_paper or 'غير محددة'}
- القسم: {context.current_section or '-'}

## ملخص من خطته
{plan_summary[:2500]}

## عناصر اليوم (قراءة، تحديثات، روابط)
{items_text}

المطلوب: اكتب دليل يومي طويل وواضح بالعربية، بصيغة مرشد يتابعه ويوجهه. شمّل:
1. افتتاحية: ماذا لديك اليوم بناءً على خطتك وحالتك.
2. ما الذي يجب أن تفعله اليوم بالترتيب (قراءة، فهم، تطبيق).
3. على ماذا تركز: ما المفاهيم التي يجب أن تفهمها من الورقة/المرحلة الحالية.
4. ماذا تبحث عنه أو تتابعه: من أحدث التحديثات والروابط، ما الذي يستحق النظر ولماذا.
5. توصيات: اقتراح واحد أو اثنين (مشروع مصغر، تمرين، أو خطوة تالية).
6. تذكيرات قصيرة من خطته إن لزم.

اجعل النص تفصيلياً ومفيداً كدليل حقيقي. استخدم عناوين وترقيم. اكتب بضمير المخاطب (أنت، لك، ...).
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "أنت مرشد تعلم يومي. تكتب بالعربية بشكل واضح ومنظم."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=2000,
        )
        text = response.choices[0].message.content or ""
        return f"# دليلك اليوم — {date.today().isoformat()}\n\n{text}"
    except Exception as e:
        return build_guide_template(context, items_by_kind, plan_summary) + f"\n\n*(توليد LLM لم يكتمل: {e})*"


def build_guide_template(
    context: Context,
    items_by_kind: dict[str, list[BriefItem]],
    plan_summary: str = "",
) -> str:
    """دليل تفصيلي من قالب بدون LLM — كل المعلومات منظمة كدليل."""
    lines = [
        "# دليلك اليوم — " + date.today().isoformat(),
        "",
        "## 1. أين أنت اليوم (من خطتك)",
        "",
    ]
    if context.phase:
        lines.append(f"- **المرحلة:** {context.phase}")
    if context.current_paper:
        lines.append(f"- **الورقة الحالية:** {context.current_paper}")
    if context.current_section:
        lines.append(f"- **القسم:** {context.current_section}")
    if not (context.phase or context.current_paper):
        lines.append("- حدّث `brief/current_reading.md` وحدد المرحلة والورقة.")
    lines.extend(["", "---", ""])

    lines.append("## 2. ماذا تفعل اليوم — بالترتيب")
    lines.append("")
    reading = items_by_kind.get("reading", [])
    if reading:
        r = reading[0]
        lines.append(f"1. **اقرأ:** {r.title}")
        if r.description:
            lines.append(f"   ({r.description})")
        lines.append("   افتح Paper Reading Guide وركّز على هذه الورقة.")
        lines.append("")
    lines.append("2. **راجع** قسم أحدث التحديثات أدناه واختر ورقة أو مقال واحد للمتابعة إن حاب.")
    lines.append("")
    lines.append("3. **تأكد** أنك فهمت الفكرة الرئيسية للورقة الحالية قبل الانتقال للتالية.")
    lines.extend(["", "---", ""])

    lines.append("## 3. على ماذا تركز اليوم")
    lines.append("")
    if context.phase == "Phase A":
        lines.append("- في Phase A التركيز على **تمثيل الكلمات (word embeddings)**.")
        lines.append("- افهم: CBOW، Skip-gram، الـ objective، ولماذا النتيجة متجهات.")
        lines.append("- لو الورقة الحالية Word2Vec: ركّز على المعادلة والـ negative sampling.")
    elif context.phase == "Phase B":
        lines.append("- في Phase B التركيز على **الانتقال من الكلمة للجملة والسياق**.")
        lines.append("- افهم: الـ Transformer، BERT، وتمثيل الجمل (sentence embeddings).")
    elif context.phase == "Phase C":
        lines.append("- في Phase C التركيز على **النماذج الحديثة والـ contrastive learning**.")
        lines.append("- افهم: SimCSE، Nomic Embed، وتقييم الـ embeddings.")
    else:
        lines.append("- ركّز على الورقة المحددة في current_reading.")
    lines.extend(["", "---", ""])

    lines.append("## 4. أحدث التحديثات — ماذا تستحق النظر")
    lines.append("")
    for it in items_by_kind.get("update", [])[:5]:
        lines.append(f"- **{it.title}**")
        lines.append(f"  {it.url}")
        if it.description:
            lines.append(f"  {it.description[:180]}...")
        lines.append("")
    if not items_by_kind.get("update"):
        lines.append("- (لا توجد عناصر هذا اليوم — ثبّت feedparser لجلب arXiv.)")
    lines.extend(["", "---", ""])

    lines.append("## 5. من المدونات والنشرات")
    lines.append("")
    for it in items_by_kind.get("link", []):
        if it.source_name in ("Chip Huyen", "Simon Willison") or "RSS" in (it.source_name or ""):
            lines.append(f"- [{it.title}]({it.url}) — *{it.source_name}*")
    lines.extend(["", "---", ""])

    lines.append("## 6. توصية اليوم")
    lines.append("")
    if context.phase == "Phase A":
        lines.append("- جرّب تكتب سكربت صغير يقرأ نصاً ويحسب متوسط متجهات الكلمات (لو عندك embeddings جاهزة) أو راجع كود Word2Vec من مصدر موثوق.")
    else:
        lines.append("- خصص 30 دقيقة لقراءة الورقة الحالية دون تشتيت، ثم سجّل ثلاث نقاط فهمت them.")
    lines.extend(["", "---", ""])

    lines.append("## 7. مراجع سريعة")
    lines.append("")
    for it in items_by_kind.get("link", []):
        if it.source_name == "static_links":
            lines.append(f"- **{it.title}** — {it.url}")
    lines.append("")

    return "\n".join(lines)


def build_guide(
    context: Context,
    items_by_kind: dict[str, list[BriefItem]],
    plan_summary: str = "",
    use_llm: bool = False,
    api_key: str = "",
) -> str:
    """يبني الدليل اليومي. لو use_llm=True و api_key موجود يستخدم LLM؛ وإلا قالب تفصيلي."""
    if use_llm and api_key:
        return build_guide_with_llm(context, items_by_kind, plan_summary, api_key)
    return build_guide_template(context, items_by_kind, plan_summary)
