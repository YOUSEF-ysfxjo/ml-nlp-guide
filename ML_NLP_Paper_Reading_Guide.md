# Paper Reading Guide — From Foundations to Embeddings

This guide maps **papers** to the topics in your `ML_NLP_Comprehensive_Summary.md`, in an order that fits “understanding from the beginning” with a research mindset.

---

## 1. Suggested reading order (from the beginning)

### Phase A — Where your summary ends (word-level embeddings)


| Order | Paper                                                                                                  | Why read it                                                                                                                          |
| ----- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **1** | **Efficient Estimation of Word Representations in Vector Space** (Mikolov et al., 2013)                | The Word2Vec paper. Defines CBOW vs Skip-gram, negative sampling, and the objective you’re already studying. Short and foundational. |
| **2** | **Distributed Representations of Words and Phrases and their Compositionality** (Mikolov et al., 2013) | Follow-up: phrases, negative sampling, subsampling. Completes the Word2Vec story.                                                    |
| **3** | **GloVe: Global Vectors for Word Representation** (Pennington et al., EMNLP 2014)                      | Count-based + prediction hybrid; different view of “context” (co-occurrence matrix). Good for contrasting with Word2Vec.             |
| **4** | **Enriching Word Vectors with Subword Information** (Bojanowski et al., FastText, ACL 2017)            | Subword units → handles OOV and rare words. Directly addresses limitations in your summary §14.                                      |


### Phase B — From words to sentences and context


| Order | Paper                                                                                                            | Why read it                                                                                                                                   |
| ----- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **5** | **A Simple but Tough-to-Beat Baseline for Sentence Embeddings** (Arora et al., ICLR 2017)                        | Sentence embeddings from word vectors (weighted average + PCA). Connects your §15 “averaging” to a principled baseline.                       |
| **6** | **Attention Is All You Need** (Vaswani et al., 2017)                                                             | Transformer architecture. Prerequisite for understanding BERT and modern embedders.                                                           |
| **7** | **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding** (Devlin et al., NAACL 2019) | Contextual representations (fixes “one vector per word” in your §14). Foundation for most modern text embedders.                              |
| **8** | **Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks** (Reimers & Gurevych, EMNLP 2019)              | How to get sentence embeddings from BERT with siamese nets and contrastive-style training. Bridge to “embedding models” as we use them today. |


### Phase C — Modern embedding models (including Nomic Embed)


| Order  | Paper                                                                                   | Why read it                                                                                                                           |
| ------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **9**  | **SimCSE: Simple Contrastive Learning of Sentence Embeddings** (Gao et al., EMNLP 2021) | Unsupervised + supervised contrastive sentence embeddings. Clear introduction to contrastive objectives used in embedders.            |
| **10** | **Nomic Embed: Training a Reproducible Long Context Text Embedder** (Nomic, 2024)       | Long-context, reproducible training of a text embedder. Good **after** you’re comfortable with BERT, SBERT, and contrastive learning. |


---

## 2. Nomic Embed — Is it good for understanding embeddings?

**Short answer:** Yes, but **not** as the first paper. It’s best after you have the foundations above.

**What Nomic Embed is good for:**

- **Modern embedding pipeline:** Data mix, training stages (continued pretraining → contrastive fine-tuning), and evaluation.
- **Long context:** How long-context embedders are built and evaluated (e.g. 8192 tokens).
- **Reproducibility:** Full training details, data, and code — useful for research and implementation.
- **Contrastive learning:** In-batch negatives, loss formulation, and why we train embedders this way instead of Word2Vec-style prediction.

**Why not “from the very beginning”:**

- Assumes **transformers** and **contrastive learning** (no derivation of word embeddings or Word2Vec).
- Doesn’t teach the **distributional hypothesis** or **Word2Vec mechanics**; those are in the Phase A papers.
- Fits naturally after: Word2Vec → (GloVe/FastText) → BERT → SBERT/SimCSE → then Nomic Embed.

**Recommendation:** Keep it on your list. Read it in **Phase C**, after SimCSE (or similar). You’ll get much more out of it once you know (1) how classic word embeddings work, (2) how BERT gives contextual representations, and (3) how contrastive learning is used for sentence/text embeddings.

---

## 3. Extra papers by topic (from your summary)

Aligned with the sections of your summary:


| Your summary topic                          | Papers                                                                                                                                                                                       |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Linear models / XOR / limitations**       | *Perceptrons* (Minsky & Papert, 1969) — historical; optional.                                                                                                                                |
| **Optimization, backprop, loss**            | “Learning representations by back-propagating errors” (Rumelhart et al., 1986) — backprop; “Adam: A Method for Stochastic Optimization” (Kingma & Ba, ICLR 2015) — Adam.                     |
| **Distributional hypothesis (§13)**         | “Efficient Estimation…” (Mikolov 2013); “A mathematical theory of communication” (Shannon, 1948) for information view; Firth’s writings for the linguistic origin.                           |
| **Dot product, similarity (§12)**           | Same Word2Vec papers; “Improving Distributional Similarity with Lessons Learned from Word Embeddings” (Levy & Goldberg, 2015) — theory of skip-gram and PMI.                                 |
| **Sentence representation (§15)**           | Arora et al. (2017) baseline; SBERT; SimCSE.                                                                                                                                                 |
| **Road ahead — RNN/LSTM/Transformer (§16)** | “Attention Is All You Need”; “Sequence to Sequence Learning with Neural Networks” (Sutskever et al., 2014); “Learning Phrase Representations using RNN Encoder–Decoder…” (Cho et al., 2014). |


---

## 4. Minimal “from the beginning” path for embeddings only

If you want a **short path focused on embeddings**:

1. **Mikolov et al. (2013)** — Word2Vec (both papers).
2. **Levy & Goldberg (2015)** — “Improving Distributional Similarity…” (optional but sharp on the theory).
3. **Sentence-BERT (Reimers & Gurevych, 2019)** — sentence embeddings from BERT.
4. **SimCSE (Gao et al., 2021)** — contrastive sentence embeddings.
5. **Nomic Embed (2024)** — long-context, reproducible embedder.

That sequence takes you from word-level distributional semantics to modern long-context text embedders in a coherent way.

---

## 5. Quick reference — BibTeX-style citations

```
Mikolov et al. (2013). Efficient Estimation of Word Representations in Vector Space. ICLR.
Mikolov et al. (2013). Distributed Representations of Words and Phrases and their Compositionality. NeurIPS.
Pennington et al. (2014). GloVe: Global Vectors for Word Representation. EMNLP.
Bojanowski et al. (2017). Enriching Word Vectors with Subword Information. ACL.
Arora et al. (2017). A Simple but Tough-to-Beat Baseline for Sentence Embeddings. ICLR.
Vaswani et al. (2017). Attention Is All You Need. NeurIPS.
Devlin et al. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. NAACL.
Reimers & Gurevych (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. EMNLP.
Gao et al. (2021). SimCSE: Simple Contrastive Learning of Sentence Embeddings. EMNLP.
Nomic (2024). Nomic Embed: Training a Reproducible Long Context Text Embedder. arXiv.
```

---

*Use this guide alongside `ML_NLP_Comprehensive_Summary.md`: the summary gives you the concepts; these papers give you the formal definitions, algorithms, and evolution of the ideas.*