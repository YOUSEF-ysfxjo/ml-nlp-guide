# Contributing to ML & NLP Guide

Thank you for your interest in contributing! This document outlines the process for contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue using the **Bug Report** template and include:
- A clear description of the problem
- Steps to reproduce the issue
- Expected vs. actual behavior
- Your environment (OS, Python version, etc.)

### Suggesting Features

Have an idea for a new feature or improvement? Open an issue using the **Feature Request** template.

### Submitting Pull Requests

1. **Fork** the repository and create your branch from `main`:
   ```bash
   git checkout -b feature/my-feature
   ```

2. **Make your changes** and ensure they follow the existing code style.

3. **Test your changes** (run any existing notebooks or scripts to verify they still work).

4. **Commit** with a clear message:
   ```bash
   git commit -m "feat: add short description of change"
   ```

5. **Push** to your fork and **open a Pull Request** using the PR template.

## Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

| Type | Use for |
|------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `chore` | Maintenance / housekeeping |
| `refactor` | Code refactoring |
| `test` | Adding or updating tests |

## Code Style

- **Python**: Follow [PEP 8](https://pep8.org/). Use `black` for auto-formatting if available.
- **Notebooks**: Keep cells clean and well-documented with markdown explanations.
- **Markdown**: Use standard GitHub Flavored Markdown.

## Setting Up the Development Environment

```bash
git clone https://github.com/YOUSEF-ysfxjo/ml-nlp-guide.git
cd ml-nlp-guide
pip install -r daily-brief/requirements.txt
```

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).
