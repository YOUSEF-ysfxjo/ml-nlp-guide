# ML / NLP Guide

A comprehensive, hands-on reference for machine-learning and natural-language-processing concepts, papers, and experiments — including interactive notebooks, a daily-brief automation, and an HTML learning guide.

## Contents

| Path | Description |
|------|-------------|
| `ml-nlp-guide.html` | Interactive HTML learning guide |
| `word2vec_from_scratch.ipynb` | Word2Vec implemented from scratch (Jupyter notebook) |
| `daily-brief/` | Automated daily ML/NLP digest sent by email |
| `coffee-flavor-map/` | Word2Vec case study — coffee flavor embeddings |
| `assets/`, `css/`, `js/` | Static assets for the HTML guide |
| `brief/` | Brief content and templates |

## Getting Started

### Prerequisites

- Python 3.11+
- `pip`

### Install dependencies

```bash
pip install -r daily-brief/requirements.txt
```

### Run the daily brief locally

```bash
cd daily-brief
python run_brief.py
```

> **Note:** Set the required environment variables before running:
> `OPENAI_API_KEY`, `EMAIL_SENDER`, `EMAIL_PASSWORD`, `EMAIL_RECIPIENT`

### Open the HTML guide

Open `ml-nlp-guide.html` directly in your browser — no server needed.

### Explore notebooks

Launch JupyterLab or Jupyter Notebook and open any `.ipynb` file:

```bash
jupyter lab
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

## License

See [LICENSE](LICENSE) if present, otherwise all rights reserved.
