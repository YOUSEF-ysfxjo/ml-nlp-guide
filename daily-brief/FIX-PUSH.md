# إصلاح الرفع بعد رفض GitHub (أسرار + ملف كبير)

نفّذ الأوامر التالية من مجلد **New_ara**:

```powershell
cd C:\Users\HP\Desktop\projects\New_ara
```

## 1. إخراج الملف الكبير من Git (يبقى على جهازك فقط)
```powershell
git rm --cached MLOps-Community-GPU-Guide.pdf
```
(إذا ظهر خطأ أن الملف غير متتبع، تخطّ هذا السطر.)

## 2. إضافة التعديلات (بدون أسرار في .env.example)
```powershell
git add daily-brief/.env.example .gitignore
```

## 3. تعديل آخر commit ليشمل الإصلاح
```powershell
git commit --amend -m "Add daily brief and 8am schedule"
```

## 4. الدفع (يستبدل الـ commit السابق)
```powershell
git push --force-with-lease origin main
```

إذا كان الـ remote لا يزال يشير إلى **ml-nlp-guide** وتريد **daily-brief**:
```powershell
git remote set-url origin https://github.com/YOUSEF-ysfxjo/daily-brief.git
git push --force-with-lease origin main
```

بعدها أضف الأسرار في GitHub من **Settings → Secrets → Actions** (لأن .env.example الآن بدون قيم حقيقية).

---

## إزالة خطأ word2vec submodule (اختياري)

إذا ظهر في الـ Actions: `fatal: No url found for submodule path 'word2vec'`، نفّذ مرة واحدة من مجلد New_ara:

```powershell
git rm --cached word2vec
git add .gitignore
git commit -m "Remove word2vec submodule reference"
git push origin main
```
