# شرح المشروع حبى حبى — Daily Brief

شرح كل ملف وسطر مهم عشان تفهم الـ workflow من أول تشغيل لحد ما يطلع الملف.

---

## 1. run_brief.py — نقطة الدخول

```python
ROOT = Path(__file__).resolve().parent
```
- **إيش يصير:** `__file__` = مسار ملف run_brief.py نفسه. `.resolve().parent` = المجلد اللي فيه الملف، يعني مجلد `daily-brief`. نسميه `ROOT`.

```python
sys.path.insert(0, str(ROOT))
```
- **إيش يصير:** نضيف مجلد `daily-brief` لأول مكان في قائمة المسارات اللي بايثون يبحث فيها عن الموديولات. عشان لما نكتب `from core.orchestrator import ...` يلاقي مجلد `core` داخل daily-brief.

```python
CONFIG_PATH = ROOT / "config" / "sources.yaml"
CONFIG_JSON = ROOT / "config" / "sources.json"
OUTPUT_DIR = ROOT / "brief"
```
- **إيش يصير:** نحدد مسارات ثابتة: ملف التكوين (YAML أو JSON) ومجلد المخرجات (اللي راح يطلع فيه ملف الموجز).

```python
path = CONFIG_JSON if CONFIG_JSON.exists() else CONFIG_PATH
```
- **إيش يصير:** نفضّل JSON لو موجود (عشان نستغني عن مكتبة YAML). لو ما فيه JSON نستخدم YAML.

```python
config = load_config(path)
new_ara_root = ROOT / config.get("new_ara_root", "..")
out_path = run(path, OUTPUT_DIR, new_ara_root)
```
- **إيش يصير:** نقرأ التكوين من الملف. نستخرج `new_ara_root` (مثلاً `".."`) ونحوّله لمسار مطلق: مجلد New_ara. بعدين نستدعي الدالة `run` وندخل لها مسار التكوين، مجلد المخرجات، ومسار New_ara. الناتج = مسار الملف اللي اتولد.

**بجملة:** run_brief يجهّز المسارات، يقرأ التكوين، ويشغّل الدالة اللي تجمع كل شي وتكتب الموجز.

---

## 2. core/base.py — الأشكال المشتركة

### BriefItem
```python
@dataclass
class BriefItem:
    kind: str   # reading | link | update | ...
    title: str
    url: str = ""
    description: str = ""
    source_name: str = ""
    metadata: dict = ...
```
- **إيش هو:** "عنصر واحد" يمكن يظهر في الموجز. كل مصدر (RSS، arXiv، قراءة اليوم، مراجع) يرجّع قائمة من هالكلاس.
- **kind:** يحدد وين يروى في الموجز: `reading` → قسم قراءة اليوم، `update` → أحدث التحديثات، `link` → إما RSS أو مراجع حسب source_name.
- **title, url, description:** اللي يظهر للمستخدم. **source_name:** اسم المصدر (عشان الـ orchestrator يفرّق بين روابط المدونات وروابط المراجع).

### Context
```python
@dataclass
class Context:
    phase: str = ""
    current_paper: str = ""
    current_section: str = ""
    reminders: list[str] = ...
    raw: dict[str, Any] = ...
```
- **إيش هو:** نتيجة قراءة مجلد New_ara. يملأه مصدر واحد فقط (NewAraContextSource). باقي المصادر تقدر تستخدمه (مثلاً reading_plan ياخذ منه الورقة والمرحلة لو حاب).

### BaseSource
```python
class BaseSource(ABC):
    def __init__(self, source_name: str, config: dict): ...
    @abstractmethod
    def fetch(self, context: Optional[Context] = None) -> list[BriefItem]: ...
```
- **إيش هو:** واجهة (عقد). أي مصدر "عادي" يورث منها ويطبّق `fetch`. يعطي للمصدر اسم وتكوين، ويطلب منه يرجع قائمة `BriefItem`. الـ orchestrator يستدعي `fetch(context)` لكل مصدر.

### BaseContextSource
```python
class BaseContextSource(ABC):
    def get_context(self, root: Path) -> Context: ...
```
- **إيش هو:** واجهة لمصدر "سياق" فقط. يختلف عن BaseSource: ما يرجع عناصر للموجز، يرجع كائن Context واحد (المرحلة، الورقة، إلخ). الوحيد اللي يطبّقها حالياً = NewAraContextSource.

**بجملة:** base.py يعرّف شكل البيانات (عنصر موجز، سياق) والواجهات (مصدر عادي يرجع عناصر، مصدر سياق يرجع Context).

---

## 3. core/orchestrator.py — القلب

### load_config
```python
def load_config(config_path: Path) -> dict:
    text = config_path.read_text(encoding="utf-8")
    if config_path.suffix.lower() in (".json",):
        import json
        return json.loads(text)
    try:
        import yaml
        return yaml.safe_load(text) or {}
    except ModuleNotFoundError:
        alt = config_path.parent / "sources.json"
        if alt.exists():
            return json.loads(alt.read_text(...))
        raise SystemExit("ثبّت PyYAML أو استخدم config/sources.json")
```
- **إيش يصير:** نقرأ الملف. لو امتداده `.json` نستخدم json ونرجع قاموس. لو `.yaml` نجرب نستورد yaml ونفك الملف؛ لو ما فيه موديول yaml نبحث عن `sources.json` في نفس المجلد ونفكّه. لو ما فيه أي شي نطلع رسالة خطأ.

### build_brief_md
- **الدخل:** `context` (المرحلة والورقة)، و `items_by_kind` (قاموس: نوع → قائمة BriefItem).
- **الشغل:**
  1. نبدأ بعنوان وتاريخ اليوم.
  2. لو عندنا مرحلة أو ورقة في الـ context نكتب قسم "حالتك (من New_ara)".
  3. قسم "قراءة اليوم": نأخذ أول عنصر من `items_by_kind["reading"]` ونكتب عنوانه ووصفه ورابط الملف. لو ما فيه نكتب تذكير حدّث current_reading.
  4. قسم "أحدث التحديثات": نمر على عناصر `update` (حد أقصى 5) ونكتب عنوان ورابط وملخص قصير.
  5. قسم "من المصادر (RSS)": نمر على عناصر `link` اللي مصدرها Chip Huyen أو Simon Willison (أو أي اسم فيه "RSS") ونكتب عنوان ورابط واسم المصدر.
  6. قسم "مراجع سريعة": نمر على عناصر `link` اللي مصدرها `static_links` ونكتب عنوان ورابط.
- **الخرج:** نص واحد (string) بصيغة Markdown.

**بجملة:** الدالة تاخذ السياق والعناصر المصنّفة وترتبهم في قالب ثابت وتُرجع نص الموجز.

### run
```python
config = load_config(config_path)
root = new_ara_root.resolve()
context = Context()
```
- نقرأ التكوين. نثبت مسار مجلد New_ara. نجهز context فاضي.

```python
ctx_cfg = config.get("sources", {}).get("new_ara_context", {})
if ctx_cfg.get("enabled", True):
    ctx_src = NewAraContextSource("new_ara_context", {"context_files": config.get("context_files", [])})
    context = ctx_src.get_context(root)
```
- نقرأ تكوين مصدر `new_ara_context`. لو مفعّل، ننشئ NewAraContextSource ونديله قائمة الملفات اللي يقرأها. نستدعي `get_context(root)` فيقرأ من مجلد New_ara الملفات ويستخرج المرحلة والورقة والقسم ويملأ `context`.

```python
for key in ("reading_plan", "static_links"):
    if key in sources_config and isinstance(sources_config[key], dict):
        sources_config[key]["_root"] = root
```
- نمرّر مسار مجلد New_ara للمصادر اللي تحتاج تقرأ ملفات من هناك (reading_plan يقرأ current_reading والـ guide، static_links يقدر يربط روابط محلية بالمسار).

```python
rp = sources_config.get("reading_plan", {})
if rp.get("enabled"):
    src = ReadingPlanSource("reading_plan", rp)
    items.extend(src.fetch(context))
```
- نفس الفكرة لباقي المصادر: نقرأ التكوين، لو المصدر مفعّل ننشئ الكلاس ونديله التكوين، نستدعي `fetch(context)` ونضيف الناتج لقائمة `items`. يكرر لـ latest_updates، rss، static_links.

```python
by_kind: dict[str, list[BriefItem]] = {}
for it in items:
    by_kind.setdefault(it.kind, []).append(it)
```
- نصنّف كل العناصر حسب الحقل `kind`. الناتج: قاموس كل مفتاح فيه نوع (reading, update, link) والقيمة قائمة العناصر من هالنوع.

```python
md = build_brief_md(context, by_kind)
output_dir.mkdir(parents=True, exist_ok=True)
out_file = output_dir / f"{date.today().isoformat()}.md"
out_file.write_text(md, encoding="utf-8")
return str(out_file)
```
- نبني نص الموجز. ننشئ مجلد المخرجات لو ما موجود. نكتب النص في ملف اسمه تاريخ اليوم. نرجع مسار الملف.

**بجملة:** run يقرأ التكوين، يستخرج السياق من New_ara، يشغّل كل المصادر المفعّلة، يصنّف العناصر، يبني الـ Markdown ويكتب الملف.

---

## 4. sources/new_ara_context.py — استخراج السياق

```python
def get_context(self, root: Path) -> Context:
    context_files = self.config.get("context_files", [])
```
- ناخذ قائمة الملفات من التكوين (مثلاً GOAL_AND_APPROACH.md، Paper_Reading_Guide، brief/current_reading.md، PLAN_RESOURCES).

```python
for rel_path in context_files:
    path = root / rel_path
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    raw[rel_path] = text[:2000]

    if "current_reading" in rel_path:
        phase, current_paper, current_section = self._parse_current_reading(text)
    if "Paper_Reading_Guide" in rel_path and not phase:
        phase = self._infer_phase_from_guide(text)
```
- نمر على كل ملف. نقرأه. نخزّن أول 2000 حرف في `raw` (لو حاب تستخدمهم لاحقاً). لو اسم الملف فيه "current_reading" نستدعي _parse_current_reading ونستخرج phase و paper و section. لو فيه "Paper_Reading_Guide" وما عندنا phase بعد نستنتج المرحلة من نص الـ guide.

### _parse_current_reading
- نمر على الأسطر. أي سطر يبدأ بـ `phase:` أو `Phase:` ناخذ الجزء بعد النقطتين ونخزنه في phase. نفس الفكرة لـ `paper:` و `section:`. نرجع ثلاثة قيم (phase, paper, section).

### _infer_phase_from_guide
- نبحث في النص عن "### Phase A" أو "Phase B" أو "Phase C" ونرجع النص المناسب. لو ما لقينا نرجع "Phase A" كافتراضي.

**بجملة:** هذا الملف يقرأ من New_ara الملفات المحددة ويستخرج "أين أنت" (المرحلة والورقة) ويحطها في كائن Context.

---

## 5. sources/reading_plan.py — قراءة اليوم

```python
root = self.config.get("_root")
path_guide = root / self.config.get("path_guide", ...)
path_current = root / self.config.get("path_current", ...)
```
- المسار الجذر = مجلد New_ara (اللي الـ orchestrator حطه في التكوين تحت المفتاح _root). مسار الـ guide و current_reading من التكوين.

```python
if path_current.exists():
    text = path_current.read_text(...)
    for line in text.strip().splitlines():
        if line.startswith("paper:") or ...: title = ...
        elif line.startswith("phase:") or ...: description = ...
    if context and context.current_paper: title = context.current_paper
    if context and context.phase: description = f"المرحلة: {context.phase}"
```
- نقرأ current_reading.md. نستخرج من الأسطر paper و phase ونحطهم في title و description. لو الـ context جاهز (من NewAraContextSource) نستخدم قيم الـ context كأولوية عشان العنوان والوصف.

```python
return [ BriefItem(kind="reading", title=title or "حدّث ...", url=str(path_guide), description=..., source_name=self.source_name) ]
```
- نرجع عنصر واحد من نوع "reading". العنوان = ورقة اليوم (أو تذكير حدّث الملف). الرابط = مسار ملف الـ guide. الوصف = المرحلة.

**بجملة:** يحدد "قراءة اليوم" من ملف current_reading (والسياق) ويرجع عنصر واحد للموجز.

---

## 6. sources/latest_updates.py — أحدث التحديثات

```python
if not feedparser:
    return [ BriefItem(kind="update", title="ثبّت feedparser ...", ...) ]
```
- لو مكتبة feedparser مو مثبتة نرجع عنصر واحد يطلب من المستخدم يثبتها.

```python
max_items = self.config.get("max_items", 5)
category = self.config.get("arxiv_category", "cs.CL")
url = f"http://rss.arxiv.org/rss/{category}"
feed = feedparser.parse(url)
```
- نقرأ من التكوين عدد العناصر والتصنيف (مثلاً cs.CL). نطلب من arXiv الـ RSS لهالتصنيف. feedparser يرجع قاموس فيه قائمة "entries" (كل entry = ورقة: عنوان، رابط، ملخص).

```python
for entry in feed.get("entries", [])[:max_items]:
    link = entry.get("link", "")
    title = entry.get("title", "").strip()
    summary = (entry.get("summary", "") or "")[:200]...
    items.append(BriefItem(kind="update", title=title, url=link, description=summary, source_name="arXiv " + category))
```
- نمر على أول max_items ورقة. لكل ورقة نأخذ الرابط والعنوان وقطعة من الملخص ونصنع BriefItem من نوع "update". الناتج يروح لقسم "أحدث التحديثات" في الموجز.

**بجملة:** يجلب آخر أوراق من arXiv ويحوّلها لعناصر نوع "update".

---

## 7. sources/rss.py — مدونات ونشرات

```python
feeds = self.config.get("feeds", [])
```
- قائمة الـ feeds من التكوين (كل واحد فيه name, url, max_items).

```python
for feed_config in feeds:
    name = feed_config.get("name", "RSS")
    url = feed_config.get("url", "")
    max_items = feed_config.get("max_items", 1)
    feed = feedparser.parse(url)
    for entry in feed.get("entries", [])[:max_items]:
        items.append(BriefItem(kind="link", title=..., link=..., description=name, source_name=name))
```
- لكل feed نطلب الرابط بـ feedparser. نأخذ آخر max_items مقال. كل مقال = BriefItem من نوع "link" و source_name = اسم المصدر (Chip Huyen، Simon Willison). الـ orchestrator يستخدم source_name عشان يضعهم في قسم "من المصادر (RSS)" ويترك عناصر static_links لقسم "مراجع سريعة".

**بجملة:** يجلب آخر مقال من كل مدونة في التكوين ويرجعهم كعناصر "link" مع اسم المصدر.

---

## 8. sources/static_links.py — مراجع سريعة

```python
links = self.config.get("links", [])
for link in links:
    title = link.get("title", "")
    url = link.get("url", "")
    if url and not url.startswith("http") and root:
        path = root / url
        url = str(path) if path.exists() else url
    items.append(BriefItem(kind="link", title=title, url=url, description=label, source_name=self.source_name))
```
- نقرأ قائمة الروابط من التكوين. لو الرابط مو http (يعني مسار محلي) نربطه بمسار مجلد New_ara. كل رابط = BriefItem من نوع "link" و source_name = "static_links" عشان الـ build_brief_md يضعهم في قسم "مراجع سريعة".

**بجملة:** يقرأ قائمة مراجع ثابتة من التكوين ويرجعها كعناصر "link" مع source_name = static_links.

---

## تسلسل التنفيذ (مرة وحدة)

1. **run_brief.py:** يحدد المسارات، يقرأ التكوين، يستدعي `run(path, OUTPUT_DIR, new_ara_root)`.
2. **orchestrator.run:** يحمّل التكوين، يحسب root = New_ara.
3. **NewAraContextSource.get_context(root):** يقرأ الملفات من New_ara ويملأ Context (phase, current_paper, ...).
4. **orchestrator:** يضيف _root لتكوين reading_plan و static_links.
5. **ReadingPlanSource.fetch(context):** يقرأ current_reading والـ guide، يرجع عنصر "reading".
6. **LatestUpdatesSource.fetch(context):** يطلب arXiv، يرجع قائمة "update".
7. **RSSSource.fetch(context):** يطلب كل feed، يرجع قائمة "link" (مدونات).
8. **StaticLinksSource.fetch(context):** يقرأ links من التكوين، يرجع قائمة "link" (مراجع).
9. **orchestrator:** يجمع كل العناصر في items، يصنّفهم في by_kind حسب kind.
10. **build_brief_md(context, by_kind):** يبني نص Markdown من القالب والعناصر.
11. **orchestrator:** يكتب النص في brief/YYYY-MM-DD.md ويرجع المسار.
12. **run_brief.py:** يطبع "تم إنشاء الموجز: ...".

لو تتبع هذا التسلسل مع الملفات راح تفهم كل خطوة من أول تشغيل البرنامج لحد ما يطلع الملف.
