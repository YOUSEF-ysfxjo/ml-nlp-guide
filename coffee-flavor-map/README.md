# The Coffee Flavor Map

مشروع تطبيقي لبناء **فضاء دلالي رقمي** لنكهات القهوة، ومقارنة تمثيلين:

- **Phase 1 — إحصائي عالمي:** متجهات ثابتة من تزامن الكلمات (Word2Vec / GloVe).
- **Phase 2 — سياقي:** تمثيل يعتمد على معنى الجملة/الفقرة (sentence embeddings).
- **Phase 3 — معيار ومقارنة:** قياس الدقة والتجميع مقابل Coffee Taster's Flavor Wheel.

---

## الربط مع مسار التعلّم (New_ara)

| مرحلة المشروع | يقابل في الدليل |
|---------------|------------------|
| Phase 1 | **Phase A** — Word2Vec، GloVe، FastText، Distributional Hypothesis |
| Phase 2 | **Phase B** — تمثيلات سياقية (LSTM، Attention، Transformer، sentence encoders) |
| Phase 3 | تقييم ومقارنة بين النهجين |

المراجع الرئيسية داخل المستودع:

- [`../ML_NLP_Paper_Reading_Guide.md`](../ML_NLP_Paper_Reading_Guide.md) — ترتيب الأوراق والمفاهيم.
- [`../ml-nlp-guide.html`](../ml-nlp-guide.html) — الشرح المفصّل + أمثلة Word2Vec/GloVe/FastText.
- [`../GOAL_AND_APPROACH.md`](../GOAL_AND_APPROACH.md) — هدف الرحلة البحثية–التطبيقية.

---

## هيكل المشروع

```
coffee-flavor-map/
├── README.md              ← أنت هنا
├── WORK_PLAN.md           ← خطة العمل خطوة بخطوة
├── data/
│   ├── raw/               ← نصوص خام (مراجعات، توصيفات)
│   └── processed/         ← كوربوس منظم للتدريب
├── phase1_global/         ← Word2Vec، GloVe، تقييم، تصور
├── phase2_contextual/    ← sentence embeddings، Flavor Fingerprint
├── phase3_benchmark/      ← تجميع، مقارنة، تقرير
└── docs/                  ← تقارير، Flavor Wheel، مراجع
```

---

## كيف تبدأ

1. اقرأ **WORK_PLAN.md** واتبع الخطوات بالترتيب.
2. ضع بياناتك الأولى في `data/raw/` ثم انقل الناتج المنظف إلى `data/processed/`.
3. نفّذ Phase 1 (Word2Vec ثم التقييم والتصور) حبة حبة.
4. بعد الاستقرار على Phase 1، انتقل لـ Phase 2 ثم Phase 3.

هدف المشروع: **تعلّم بالتطبيق** + **مشروع ابتكاري** — نطبّق ما نقرأه ونبني شيئاً مفيداً ومميزاً.
