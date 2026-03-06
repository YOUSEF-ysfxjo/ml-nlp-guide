# ML & NLP Guide — Site Summary

## What the site is

The site is a **static, single-page guide** that walks through the foundations of Machine Learning and Natural Language Processing: from linear models and the text problem to word embeddings (Word2Vec, CBOW, Skip-gram, negative sampling) and how they connect to modern NLP.

- **URL (when deployed):** The guide is served as the main page (e.g. `yoursite.netlify.app` or `yoursite.vercel.app`). The root `/` shows `ml-nlp-guide.html`.
- **Tech:** Plain HTML, CSS, and JavaScript. No framework, no backend. It uses a table-of-contents sidebar, read-progress bar, dark/light theme toggle, and copy buttons on code blocks.
- **Content:** Sections mirror the narrative in `ML_NLP_Comprehensive_Summary.md`: linear model → limitations (XOR) → neural networks → text problem → one-hot → word embeddings → Word2Vec (objectives, architectures, similarity) → distributional hypothesis → limitations of Word2Vec → representing sentences → and a short bridge to the paper-reading path (RNNs, Transformers, BERT, etc.).

So in short: **it’s the same ML/NLP “from the beginning” story, in a readable, navigable web format.**

---

## What it’s for

- **Learning path:** For someone (including you) who already knows the field but wants to (re)build understanding from the ground up in a **research-applied** way: problem → solution → new problem → solution, up to where we are today.
- **Reference:** One place to revisit concepts (linear model, embeddings, Word2Vec, distributional hypothesis) without opening papers or long markdown files.
- **Bridge to papers:** The guide ties into the **Paper Reading Guide** (`ML_NLP_Paper_Reading_Guide.md`): it sets the conceptual base; the papers give the formal definitions and the actual research arc (Word2Vec → GloVe/FastText → BERT → SBERT/SimCSE → Nomic Embed, etc.).

So the site’s **purpose** is: **concepts + narrative in one place, on the web, aligned with your goal of understanding how the field evolved and what we do with it in practice.**

---

## What we’ll do next (future)

- **Keep the site in sync with the narrative:** As you refine `ML_NLP_Comprehensive_Summary.md` or the Paper Reading Guide, we’ll update `ml-nlp-guide.html` (and CSS/JS if needed) so the live site stays the same story.
- **Extend the content:** Add more sections as you go deeper (e.g. Phase 0 “problem and idea”, or more paper summaries) so the site grows with your reading path.
- **Deploy and auto-update:** With the repo on GitHub and connected to Netlify (or Vercel), every push updates the deployed page; we’ll keep using that workflow so the live site always reflects the latest version.
- **Optional later:** Add a simple way to jump from each section to the corresponding papers or to the markdown sources, or to host multiple “chapters” (e.g. embeddings vs. transformers) if the guide grows.

---

**In one sentence:** The site is the web version of your ML/NLP “from the beginning” guide—what it is, what it’s for, and we’ll keep updating and extending it as you progress through the paper-reading path and future topics.
