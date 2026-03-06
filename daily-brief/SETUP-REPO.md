# ربط المشروع بمستودع daily-brief على GitHub

المستودع: **https://github.com/YOUSEF-ysfxjo/daily-brief**

يجب الرفع من مجلد **New_ara** (الأب الذي فيه مجلد `daily-brief`) حتى ترفع الكود + ملفات الخطط معاً، لأن السكربت يقرأ من هذه الملفات.

---

## الخطوات (مرة واحدة)

### 1. افتح PowerShell أو Terminal وانتقل لمجلد New_ara

```powershell
cd C:\Users\HP\Desktop\projects\New_ara
```

(المجلد اللي فيه `daily-brief` و `GOAL_AND_APPROACH.md` و `brief` وغيرها.)

### 2. تهيئة Git والربط بالمستودع

إذا المشروع ما فيه Git من قبل:

```powershell
git init
git add .
git status
```

تأكد أن ملف **`.env`** لا يظهر في القائمة (مهم: لا ترفع الأسرار). إذا ظهر، تأكد أن `.gitignore` يحتوي على `.env`.

ثم:

```powershell
git commit -m "Add daily brief project and GitHub Action"
git branch -M main
git remote add origin https://github.com/YOUSEF-ysfxjo/daily-brief.git
git push -u origin main
```

إذا كان عندك بالفعل `git` و `remote` مضبوط لمستودع ثاني، غيّر الـ remote أو اربط بالمستودع الجديد:

```powershell
git remote remove origin
git remote add origin https://github.com/YOUSEF-ysfxjo/daily-brief.git
git push -u origin main
```

### 3. إضافة الأسرار في GitHub

1. ادخل: **https://github.com/YOUSEF-ysfxjo/daily-brief**
2. **Settings** → **Secrets and variables** → **Actions**
3. **New repository secret** وأضف واحدة واحدة:

| الاسم (Name)       | القيمة (Value)              |
|--------------------|-----------------------------|
| `OPENAI_API_KEY`   | مفتاح OpenAI (sk-...)      |
| `EMAIL_SENDER`     | بريدك Gmail                |
| `EMAIL_PASSWORD`   | كلمة مرور التطبيق Gmail   |
| `EMAIL_RECIPIENT`  | البريد اللي يوصل عليه الدليل |

### 4. تجربة التشغيل يدوياً

- **Actions** → **Daily Brief 8am KSA** → **Run workflow** → **Run workflow**
- بعد دقائق تحقق من بريدك إن وصل الدليل.

بعد هذا، كل يوم الساعة **8 ص** بتوقيت السعودية يشغّل GitHub السكربت ويرسلك الإيميل تلقائياً.
