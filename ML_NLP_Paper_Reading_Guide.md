# Paper Reading Guide — Phase A (Word-Level Embeddings)

هذا الدليل يقتصر على **Phase A** فقط: تمثيل الكلمات (word-level embeddings). استخدمه مع `ml-nlp-guide.html` وملفات New_ara لفهم السياق الكامل.

---

## Phase A — تمثيل الكلمات (Word-Level Embeddings)

| الترتيب | الورقة | لماذا تقرأها |
|--------|--------|---------------|
| **1** | **Efficient Estimation of Word Representations in Vector Space** (Mikolov et al., 2013) | ورقة Word2Vec الأساسية: CBOW و Skip-gram، negative sampling، والهدف الذي تدرسه. قصيرة وأساسية. |
| **2** | **Distributed Representations of Words and Phrases and their Compositionality** (Mikolov et al., 2013) | تتمة: العبارات، negative sampling، subsampling. تكمل قصة Word2Vec. |
| **3** | **GloVe: Global Vectors for Word Representation** (Pennington et al., EMNLP 2014) | هجين count-based + prediction؛ نظرة مختلفة لـ "السياق" (مصفوفة التزامن). مفيد لمقارنتها مع Word2Vec. |
| **4** | **Enriching Word Vectors with Subword Information** (Bojanowski et al., FastText, ACL 2017) | وحدات فرعية للكلمات → يتعامل مع OOV والكلمات النادرة. يعالج مباشرة حدود التمثيل في الدليل. |

---

## مرجع سريع — استشهادات

```
Mikolov et al. (2013). Efficient Estimation of Word Representations in Vector Space. ICLR.
Mikolov et al. (2013). Distributed Representations of Words and Phrases and their Compositionality. NeurIPS.
Pennington et al. (2014). GloVe: Global Vectors for Word Representation. EMNLP.
Bojanowski et al. (2017). Enriching Word Vectors with Subword Information. ACL.
```

---

*استخدم هذا الدليل مع `ml-nlp-guide.html`: الدليل يعطيك المفاهيم؛ هذه الأوراق تعطيك التعريفات الرسمية والخوارزميات.*
