# Contributing to coding-policy-prompt-generator

[English](./CONTRIBUTING.md) | [日本語](./CONTRIBUTING_ja.md)

Thank you for your interest in contributing to coding-policy-prompt-generator! This document describes how to contribute to the project.

## How to Contribute

### 1. Reporting Bugs

When you find a bug, please open an issue with the following information:

- **Clear, descriptive title**
- **Steps to reproduce the problem**
- **Expected behavior**
- **Actual behavior**
- **Sample Excel file** (if applicable; please remove any sensitive information)
- **Version information**:
  - coding-policy-prompt-generator version
  - Python version
  - OS

### 2. Proposing Enhancements

For feature proposals, please open an issue with the following information:

- **Clear, descriptive title**
- **Detailed description of the proposed feature**
- **Use cases and benefits**
- **Examples or mockups** (if applicable)

### 3. Pull Requests

Pull requests are welcome! Please follow the steps below.

## Setting Up the Development Environment

### Prerequisites

- Python 3.10 or higher
- The `uv` package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/elvezjp/coding-policy-prompt-generator.git
cd coding-policy-prompt-generator

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies (including dev dependencies)
uv sync --dev
```

### Verifying the Installation

```bash
# Run tests
uv run pytest

# Run the CLI
uv run coding-policy-prompt-generator --help
```

## Running Tests

### Run All Tests

```bash
uv run pytest
```

### Run a Specific Test File

```bash
uv run pytest tests/test_basic_functionality.py
```

### Run Tests with Coverage

```bash
uv run pytest --cov=src/coding_policy_prompt_generator --cov-report=html
```

## Pull Request Workflow

### 1. Fork and Create a Branch

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/coding-policy-prompt-generator.git
cd coding-policy-prompt-generator

# Create a feature branch
# Branch naming convention: {username}/{YYYYMMDD}-{description}
git checkout -b your-username/20260128-add-new-feature
```

### 2. Coding Style

This project follows the [PEP 8](https://peps.python.org/pep-0008/) style guide.

- Use 4 spaces for indentation
- Maximum line length: 88 characters (Black default)
- Use type hints where appropriate

#### Naming Conventions

- Variables and functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private members: `_leading_underscore`

#### Documentation

- Add docstrings to public functions and classes
- Use Google-style docstrings

```python
def process_rule(rule_id: str, summary: str) -> dict:
    """Process a single rule and produce prompt data.

    Args:
        rule_id: Unique identifier of the rule.
        summary: Summary text of the rule.

    Returns:
        A dict containing the processed rule data.

    Raises:
        ValueError: If rule_id is empty.
    """
```

### 3. Writing Tests

- Add tests for new features
- Make sure existing tests still pass
- Place test files under the `tests/` directory

```bash
# Run tests before committing
uv run pytest
```

### 4. Updating Documentation

Update the following as needed:

- `README.md` / `README_ja.md` — new features or usage changes
- `CHANGELOG.md` / `CHANGELOG_ja.md` — add an entry to the "Unreleased" section
- Docstrings — keep them in sync with code changes

### 5. Commit Message Convention

Follow this format:

```
<type>: <subject>

<body>

<footer>
```

#### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting (no code change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

#### Examples

Good:
```
feat: support custom template variables

Allow passing extra variables to Jinja2 templates
via the --extra-vars option.

Closes #123
```

```
fix: handle empty cells in the summary column

Previously, whitespace-only cells were processed as
valid rules. They are now skipped with a warning.
```

Bad:
```
bug fix
```

```
update code
```

### 6. Push and Open a Pull Request

```bash
# Push your branch
git push -u origin your-username/20260128-add-new-feature
```

When opening a pull request on GitHub, please include:

- A clear title describing the change
- An explanation of what changed and why
- References to related issues (e.g., "Closes #123")

### 7. Review Process

- Wait for code review from a maintainer
- Address feedback and push additional commits
- Once approved, a maintainer will merge the PR

## Pre-submission Checklist

Before submitting a pull request, please confirm:

- [ ] All tests pass (`uv run pytest`)
- [ ] Code follows the PEP 8 style guidelines
- [ ] New features have corresponding tests
- [ ] Documentation has been updated
- [ ] Commit messages follow the convention
- [ ] The branch is up to date with main

## Code Review Guidelines

Reviews focus on:

- Correctness and functionality
- Test coverage
- Readability and maintainability
- Adherence to project conventions
- Documentation quality

## Community Guidelines

- Be respectful and constructive
- Ask questions when something is unclear
- Help others when you can

## Questions?

- Open an issue with the `question` label
- Email: info@elvez.co.jp

Thank you for contributing!
