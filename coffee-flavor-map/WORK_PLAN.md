# Work Plan — The Coffee Flavor Map

An actionable plan to implement the project step by step, with each phase tied to concepts from the guide’s Phase A/B.

---

## Overall Goal

Build a **semantic digital space** for coffee flavors and compare **global statistics** (Phase 1) with **contextual meaning** (Phase 2), then measure performance (Phase 3).

---

## Phase 1 — Global Statistical Foundation

**Concepts from the guide:** Word2Vec, GloVe, Distributional Hypothesis, one fixed vector per word.

| # | Step | Outputs | Tools / References |
|---|------|--------|---------------------|
| 1.1 | Collect or prepare a **text corpus** about coffee flavors (reviews, descriptions, articles) | `data/raw` folder + text or CSV file | Scraping, public datasets, or hand-curated text |
| 1.2 | Clean text: normalize encoding, remove noise, split into sentences/short segments | `data/processed/corpus.txt` or `.csv` | Python: regex, pandas, nltk/spacy (optional) |
| 1.3 | Train **Word2Vec** on the corpus (Gensim) | Saved model + flavor term vectors | `gensim.models.Word2Vec` — see ml-nlp-guide.html |
| 1.4 | (Optional) Train **GloVe** on the same corpus for comparison | Co-occurrence matrix + GloVe vectors | Stanford GloVe or glove-python |
| 1.5 | Extract vectors for **flavor terms** (e.g. from Flavor Wheel), compute similarity and analogies | Evaluation script + tables/numbers | cosine similarity, `most_similar`, analogy equations |
| 1.6 | Simple **clustering** and dimensionality reduction (PCA/t-SNE/UMAP) for visualization | Distance matrix, 2D neighborhood plot | sklearn, umap-learn |

**Phase 1 success criteria:** Semantically related flavors (e.g. Lemon, Citrus) sit close in the space; analogies like `Ethiopia - Lemon + Chocolate ≈ ...` are sensible.

---

## Phase 2 — Deep Contextual Representation

**Concepts from the guide:** Phase B — RNN, LSTM, Attention, Transformer; representation that depends on the full sentence.

| # | Step | Outputs | Tools / References |
|---|------|--------|---------------------|
| 2.1 | Choose a **sentence/paragraph-level** embedding model (e.g. sentence-transformers) | Loaded or fine-tuned model | SBERT, MiniLM, or other open models |
| 2.2 | Map **full flavor descriptions** (paragraphs) to a single vector “Flavor Fingerprint” | Function: text → 384/768-dim vector | encode(paragraph) |
| 2.3 | Compare flavors by **meaning of the description**, not just word overlap | Contextual similarity matrix | cosine similarity on sentence vectors |
| 2.4 | (Optional) Document differences between Phase 1 and Phase 2 on the same data | Short report or comparison table | — |

**Phase 2 success criteria:** Ability to distinguish “fruity acidity” from “harsh acidity” from longer descriptive text.

---

## Phase 3 — Benchmarking and Comparison

**Goal:** Compare both approaches and see which fits which scenario best.

| # | Step | Outputs | Tools / References |
|---|------|--------|---------------------|
| 3.1 | Define an **evaluation benchmark**: clustering that aligns with the Coffee Taster’s Flavor Wheel (known groups) | Reference group list + metrics (e.g. purity, NMI) | Flavor Wheel as ground truth |
| 3.2 | Run **clustering** on Phase 1 and Phase 2 vectors and compare to the benchmark | Metrics: clustering accuracy, runtime, behavior on rare flavors | sklearn.metrics, timing |
| 3.3 | Write an **analytical report**: when is the statistical approach better? (speed, rarity, interpretability). When is the contextual one better? (accuracy, fine-grained nuance) | File `docs/phase3_report.md` or PDF | — |

---

## Repository Layout

```
New_ara/
├── coffee-flavor-map/
│   ├── README.md           ← Overview and link to the guide
│   ├── WORK_PLAN.md        ← This file
│   ├── data/
│   │   ├── raw/            ← Raw text
│   │   └── processed/      ← Clean corpus
│   ├── phase1_global/      ← Word2Vec, GloVe, evaluation, visualization
│   ├── phase2_contextual/ ← Sentence embeddings, Flavor Fingerprint
│   ├── phase3_benchmark/   ← Clustering, comparison, report
│   └── docs/               ← Reports, references, Flavor Wheel
├── ML_NLP_Paper_Reading_Guide.md
├── ml-nlp-guide.html
└── ...
```

---

## Execution Order (Step by Step)

1. **Now:** Create folders and prepare a first small corpus (even 100–500 sentences) in `data/`.
2. **Next:** Run step 1.3 (Word2Vec) on the corpus; run `most_similar` and at least one analogy.
3. **Then:** Steps 1.5 and 1.6 (evaluation + visualization).
4. **Later:** Add GloVe if desired, then move to Phase 2 and 3.

Each step builds on the previous one — implement, verify, then move on.
