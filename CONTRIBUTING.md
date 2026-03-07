# Contributing to ML / NLP Guide

Thank you for your interest in contributing! Here are a few guidelines to help
keep the project consistent and welcoming.

## How to Contribute

1. **Fork** the repository and create a feature branch from `main`.
2. **Make your changes** — keep commits focused and descriptive.
3. **Test your changes** before opening a pull request:
   - Python code: `pytest` (if tests exist)
   - Notebooks: run cells manually and ensure there are no errors
4. **Open a pull request** using the provided template and describe what you
   changed and why.

## Project Structure

| Path | What goes here |
|------|---------------|
| `daily-brief/` | Automated brief logic and agents |
| `coffee-flavor-map/` | Word2Vec case study code |
| `*.ipynb` | Jupyter notebooks (experiments / tutorials) |
| `ml-nlp-guide.html` | The static HTML learning guide |

## Coding Style

- **Python**: Follow [PEP 8](https://peps.python.org/pep-0008/). Use
  descriptive variable names and add docstrings to public functions.
- **Notebooks**: Keep cells small and self-contained. Add Markdown cells to
  explain each section.
- **HTML/CSS/JS**: Follow the conventions already used in the repo.

## Commit Messages

Use the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>: <short description>

[optional body]
```

Common types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`.

## Reporting Issues

Use the GitHub issue templates (Bug Report or Feature Request) to report
problems or suggest improvements. Please include enough detail to reproduce any
bug you report.

## Code of Conduct

By participating, you agree to abide by the
[Code of Conduct](CODE_OF_CONDUCT.md).
