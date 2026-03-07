# ML & NLP Guide

A comprehensive learning resource and interactive guide covering Machine Learning and Natural Language Processing concepts, with hands-on Jupyter notebooks, a coffee flavor map case study built with Word2Vec, and a daily AI brief generator.

## 📚 Contents

| Resource | Description |
|----------|-------------|
| [`ml-nlp-guide.html`](ml-nlp-guide.html) | Interactive HTML guide covering ML/NLP fundamentals |
| [`word2vec_from_scratch.ipynb`](word2vec_from_scratch.ipynb) | Jupyter notebook implementing Word2Vec from scratch |
| [`coffee-flavor-map/`](coffee-flavor-map/) | Case study: Word2Vec applied to coffee flavor profiling |
| [`daily-brief/`](daily-brief/) | Automated daily AI news brief generator |
| [`ML_NLP_Comprehensive_Summary.md`](ML_NLP_Comprehensive_Summary.md) | Comprehensive summary of ML/NLP concepts |
| [`PLAN_RESOURCES_AND_ROADMAP.md`](PLAN_RESOURCES_AND_ROADMAP.md) | Learning roadmap and resources |

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUSEF-ysfxjo/ml-nlp-guide.git
cd ml-nlp-guide

# Install dependencies for the daily brief
pip install -r daily-brief/requirements.txt
```

### Running the Jupyter Notebook

```bash
jupyter notebook word2vec_from_scratch.ipynb
```

### Running the Daily Brief

```bash
cd daily-brief
python run_brief.py
```

> **Note:** The daily brief requires environment variables (`OPENAI_API_KEY`, `EMAIL_SENDER`, `EMAIL_PASSWORD`, `EMAIL_RECIPIENT`). Copy `.env.example` to `.env` and fill in your values.

## 🗺️ Coffee Flavor Map

A real-world application of Word2Vec that maps relationships between coffee flavor descriptors. See [`COFFEE_FLAVOR_MAP.md`](COFFEE_FLAVOR_MAP.md) for details.

## 🤖 Daily Brief

An automated GitHub Actions workflow that generates and emails an AI-curated ML/NLP news brief every day at 8:25 AM KSA time. See [`daily-brief/README.md`](daily-brief/README.md) for setup instructions.

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
