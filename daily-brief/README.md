# الدليل اليومي (Daily Brief) — نظام وكيل يعتمد على LLM

المشروع **وكيل كامل** (مثل Automated-Job-Application-Agent): agents يقرؤون New_ara ويجمعون المصادر، و**LLM** يولد دليلاً يومياً طويلاً وشاملاً. الاعتماد الأساسي على الـ LLM؛ بدون مفتاح API لا يُنتج الدليل.

## الهيكل (Agents)

| المكوّن | الوظيفة |
|--------|---------|
| **ContextAgent** | يقرأ مجلد New_ara والملفات المحددة (خطة، مرحلة، ورقة حالية) ويستخرج السياق. |
| **GatherAgent** | يشغّل المصادر المفعّلة: قراءة اليوم، arXiv، RSS، روابط ثابتة؛ يرجّع العناصر مجمّعة. |
| **GuideAgent** | يأخذ السياق والعناصر ويرسلها إلى **LLM**؛ يولد دليلاً يومياً كاملاً: ماذا تفعل، على ماذا تركز، أحدث التحديثات، توصيات، مراجع. |

## المتطلبات

- **OpenAI API key** مطلوب. ضعه في `.env` كـ `OPENAI_API_KEY` أو في التكوين `guide.openai_api_key`.
- بايثون 3.10+

## التشغيل

```bash
cd daily-brief
pip install -r requirements.txt
# ضع OPENAI_API_KEY في .env
python run_brief.py
```

## التكوين

- **config/sources.json** — `new_ara_root`, `context_files`, `sources` (قراءة، أحدث التحديثات، RSS، روابط)، `guide` (model، openai_api_key)، `email` (enabled).
- **brief/current_reading.md** (داخل New_ara) — حدّث فيه `phase:` و `paper:` و `section:`.

## المخرجات

- **brief/YYYY-MM-DD-guide.md** — الدليل اليومي الكامل (مولّد بالكامل من LLM): افتتاحية، ما الذي تفعله اليوم، على ماذا تركز، أحدث التحديثات وملاحظات عليها، توصيات، تذكيرات، مراجع.
- إن وُجد تكوين البريد يُرسل **نفس الدليل** إلى بريدك.

## البريد (مثل research_harvester)

انسخ `.env.example` إلى `.env` واملأ:

- `EMAIL_SENDER`, `EMAIL_PASSWORD`, `EMAIL_RECIPIENT`

أو فعّل `"email": { "enabled": true }` مع وجود المتغيرات في البيئة.

## المجلدات

- `agents/` — ContextAgent، GatherAgent، GuideAgent
- `llm_tools/` — LLMRunner (OpenAI)
- `sources/` — مصادرة البيانات (قراءة، arXiv، RSS، روابط)
- `core/` — base types، orchestrator، email_sender

## جدولة — 8 صباحاً بتوقيت السعودية

**طريقة 1 — سكربت الجدولة:** شغّل واتركه يعمل في الخلفية:
```bash
python run_scheduled.py
```
يفحص كل 10 دقائق؛ عند الساعة 8:00–8:14 ص (توقيت السعودية) يشغّل الدليل ويرسل الإيميل مرة واحدة يومياً.

**طريقة 2 — Windows Task Scheduler:** أنشئ مهمة يومية تشغّل:
- البرنامج: `C:\...\Python311\python.exe`
- الوسائط: `run_brief.py`
- بدء التشغيل في: مجلد `daily-brief`
- المُحرّك: يومياً الساعة 8:00 ص (اختر التوقيت المحلي إذا كنت في السعودية، أو 5:00 UTC إذا كان جهازك بـ UTC).

## السياق والمصادر

- **context_files** تتضمن `ml-nlp-guide.html` (يُقرأ كنص بعد إزالة الوسوم) وملفات الخطط. الدليل يقتصر على **Phase A** (تمثيل الكلمات).
- **مصادر إضافية:** Hugging Face Trending Papers، Good AI List، MLOps Community (Gatewaze)، إضافة إلى arXiv و RSS والمراجع الثابتة.
