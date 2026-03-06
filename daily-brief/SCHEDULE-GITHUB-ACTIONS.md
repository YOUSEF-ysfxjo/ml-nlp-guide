# تشغيل الدليل تلقائياً كل يوم 8 ص (بدون إبقاء اللابتوب مفتوحاً)

استخدم **GitHub Actions** — يشغّل السكربت على سيرفرات GitHub يومياً الساعة 8 صباحاً بتوقيت السعودية ويرسل الإيميل. جهازك يبقى مغلقاً ولا يستهلك موارد.

---

## الخطوات (مرة واحدة)

### 1. رفع المشروع إلى GitHub

- إذا عندك بالفعل ريبو لـ **New_ara** (فيه مجلد `daily-brief` ومجلد `New_ara` نفسه فيه الملفات مثل `GOAL_AND_APPROACH.md` و `brief/current_reading.md`): ارفع التحديثات (بما فيها مجلد `.github/workflows`).
- إذا ما عندك ريبو:
  - أنشئ ريبو جديد على GitHub (مثلاً اسمه `New_ara`).
  - اجعل المجلد `New_ara` على جهازك هو جذر الريبو (كل المحتويات: `daily-brief`، `GOAL_AND_APPROACH.md`، `brief`، إلخ).
  - اربط المشروع وادفع:  
  `git remote add origin https://github.com/YOUR_USERNAME/New_ara.git`  
  `git add .`  
  `git commit -m "Add daily brief and GitHub Action"`  
  `git push -u origin main`

### 2. إضافة الأسرار (Secrets) في GitHub

- ادخل على ريبوك: **Settings** → **Secrets and variables** → **Actions**.
- اضغط **New repository secret** وأضف واحدة واحدة:


| الاسم (Name)      | القيمة (Value)                |
| ----------------- | ----------------------------- |
| `OPENAI_API_KEY`  | مفتاح OpenAI (يبدأ بـ sk-...) |
| `EMAIL_SENDER`    | بريدك Gmail (الإرسال)         |
| `EMAIL_PASSWORD`  | كلمة مرور التطبيق من Gmail    |
| `EMAIL_RECIPIENT` | البريد اللي يوصل عليه الدليل  |


**مهم:** لا ترفع ملف `.env` إلى GitHub. الأسرار تُضاف فقط من صفحة Secrets.

### 3. التأكد من المسارات

- في الريبو، المسار يكون تقريباً:
  - جذر الريبو = مجلد `New_ara` (فيه `daily-brief` و `GOAL_AND_APPROACH.md` و `brief` و `ml-nlp-guide.html` إلخ).
- في `daily-brief/config/sources.json` يكون `new_ara_root: ".."` (يعني المجلد الأب = جذر الريبو). لا تغيّره إذا كان هيك بالفعل.

---

## بعد الإعداد

- **كل يوم الساعة 8 ص (توقيت السعودية)** يشغّل GitHub الدليل ويرسل الإيميل تلقائياً.
- ما تحتاج تفتح اللابتوب ولا تشغّل أي برنامج.
- للتشغيل يدوياً مرة واحدة: ادخل **Actions** → **Daily Brief 8am KSA** → **Run workflow**.

---

## ملاحظات

- الخدمة مجانية ضمن حدود استخدام GitHub (تشغيل يومي واحد يكفي ولا يستهلك تقريباً شيء).
- إذا غيّرت مرحلة القراءة أو الورقة، حدّث الملفات في مجلد `New_ara` (مثل `brief/current_reading.md`) وادفع التعديلات إلى GitHub حتى يكون الدليل الجديد مبنيّاً على آخر تحديث.

