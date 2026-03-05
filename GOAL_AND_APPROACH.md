# Goal, Idea & Approach — Research-Applied ML/NLP Journey

This document states **why** we are doing this, **how** we think about it, and **what** we will do and apply.

---

## 1. Goal

**Primary goal:** Build a clear, research-applied understanding of ML/NLP by following the **historical arc of problems and solutions** — from early ideas to where the field is today.

You are already specialized and understand the domain; here we **start from the beginning** so that understanding is grounded in:

- **Why** each step was taken (what problem it addressed).
- **What** was tried and what worked (the actual research and methods).
- **How** one solution led to new limitations and then to new solutions.

The outcome we want is not just “knowing the current tools,” but **seeing the chain**: problem → solution → new problem → new solution → … up to modern embeddings and beyond.

---

## 2. The Idea: Problem → Solution → New Problem → Solution

We care about the **narrative of the field**:

1. **A problem appears** (e.g., words as discrete symbols, no notion of similarity).
2. **Researchers propose a solution** (e.g., distributed word representations).
3. **New limitations show up** (e.g., one vector per word, no context sensitivity).
4. **A new solution is proposed** (e.g., contextual representations, subword units).
5. **This repeats** until we reach the current state (e.g., long-context text embedders, contrastive learning).

By following this arc we:

- Understand **motivation**, not just formulas.
- See **what each paper was reacting to** and what it enabled next.
- Connect **theory** (papers, algorithms) with **practice** (how we use embeddings and models today).

So the “idea” is: **learn by reconstructing the problem–solution chain**, from the beginning to the present.

---

## 3. What We Want to Do

Concretely, we will:

1. **Follow a structured path**  
   Use the reading order in `ML_NLP_Paper_Reading_Guide.md` (and any linked summaries) so that each topic builds on the previous one.

2. **Emphasize the chain**  
   For each major step (e.g., Word2Vec, GloVe, FastText, BERT, SBERT, SimCSE, Nomic Embed), we explicitly note:
   - **Problem:** What limitation or question did this address?
   - **Solution:** What was proposed (method, objective, architecture)?
   - **Outcome:** What new capabilities or new problems did it create?

3. **Connect to today**  
   We keep in view how each step leads toward **current practice**: e.g., pretraining + contrastive fine-tuning, long-context embedders, reproducibility.

4. **Stay research-applied**  
   We read papers and summaries not only for theory but to see **how research is translated into applied systems** (training pipelines, evaluation, real-world use).

---

## 4. What We Will Apply

To make this concrete and usable:

- **Summaries and guides**  
  We maintain and use documents (e.g. `ML_NLP_Comprehensive_Summary.md`, `ML_NLP_Paper_Reading_Guide.md`) that organize concepts and papers along this problem–solution storyline.

- **Paper reading**  
  We read (or revisit) key papers in the suggested order, with the above three questions (problem / solution / outcome) in mind for each.

- **Narrative write-ups**  
  Where useful, we write short “story” notes that spell out: “Before X we had problem P; X did Y; after X we had new capability C and new problem P′.”

- **Practical anchor**  
  We tie the narrative to a **concrete target** (e.g., understanding modern text embedders like Nomic Embed, or designing/improving an embedding pipeline) so that the journey has a clear applied endpoint.

---

## 5. One-Sentence Summary

**We are reconstructing the ML/NLP embedding story from the beginning, in problem–solution steps, so that our existing expertise is grounded in the research narrative and we can see how the field evolved to what we use today — and we support this with structured reading, summaries, and applied targets.**

---

*This document is the “north star” for the reading guide and any related summaries: whenever we add or reorder material, we keep this goal and approach in mind.*
