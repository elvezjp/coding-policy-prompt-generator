# Contributing to coding-policy-prompt-generator

Thank you for your interest in contributing to coding-policy-prompt-generator! This document explains how to contribute to this project.

## Ways to Contribute

### 1. Bug Reports

If you find a bug, please create an Issue with the following information:

- **Clear and descriptive title**
- **Steps to reproduce the issue**
- **Expected behavior**
- **Actual behavior**
- **Sample Excel file** (if applicable, with sensitive data removed)
- **Version information**:
  - coding-policy-prompt-generator version
  - Python version
  - Operating system

### 2. Feature Requests

For feature suggestions, please create an Issue with:

- **Clear and descriptive title**
- **Detailed description of the proposed feature**
- **Use cases and benefits**
- **Examples or mockups** (if applicable)

### 3. Pull Requests

We welcome Pull Requests! Please follow the process below.

## Development Setup

### Prerequisites

- Python 3.9 or higher
- `uv` package manager

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/elvez-inc/coding-policy-prompt-generator.git
cd coding-policy-prompt-generator

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies (including dev dependencies)
uv sync --dev
```

### Verify Installation

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

### Run Specific Test File

```bash
uv run pytest tests/test_m1_smoke.py
```

### Run Tests with Coverage

```bash
uv run pytest --cov=src/coding_policy_prompt_generator --cov-report=html
```

## Pull Request Process

### 1. Fork and Create Branch

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/coding-policy-prompt-generator.git
cd coding-policy-prompt-generator

# Create a feature branch
# Branch naming convention: {username}/{YYYYMMDD}-{description}
git checkout -b your-username/20260128-add-new-feature
```

### 2. Follow Coding Style

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
    """Process a single rule and generate prompt data.

    Args:
        rule_id: The unique identifier for the rule.
        summary: The rule summary text.

    Returns:
        A dictionary containing the processed rule data.

    Raises:
        ValueError: If rule_id is empty.
    """
```

### 3. Write Tests

- Add tests for new features
- Ensure existing tests pass
- Place test files in the `tests/` directory

```bash
# Run tests before committing
uv run pytest
```

### 4. Update Documentation

Update the following as needed:

- `README.md` / `README_ja.md` - For new features or usage changes
- `CHANGELOG.md` - Add entry under "Unreleased" section
- Docstrings - For code changes

### 5. Commit Messages

Follow this format for commit messages:

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
feat: add support for custom template variables

Allow users to pass additional variables to Jinja2 templates
via the --extra-vars option.

Closes #123
```

```
fix: handle empty cells in summary column

Previously, cells with whitespace-only content were processed
as valid rules. Now they are properly skipped with a warning.
```

Bad:
```
Fixed bug
```

```
Update code
```

### 6. Push and Create Pull Request

```bash
# Push your branch
git push -u origin your-username/20260128-add-new-feature
```

Then create a Pull Request on GitHub with:

- Clear title describing the change
- Description of what changed and why
- Reference to related Issues (e.g., "Closes #123")

### 7. Review Process

- Wait for code review from maintainers
- Address feedback and push additional commits
- Once approved, a maintainer will merge your PR

## Pre-Submit Checklist

Before submitting a Pull Request, verify:

- [ ] All tests pass (`uv run pytest`)
- [ ] Code follows PEP 8 style guidelines
- [ ] New features have corresponding tests
- [ ] Documentation is updated
- [ ] Commit messages follow the convention
- [ ] Branch is up to date with main

## Code Review Guidelines

Reviews focus on:

- Correctness and functionality
- Test coverage
- Code readability and maintainability
- Adherence to project conventions
- Documentation quality

## Community Guidelines

- Be respectful and constructive
- Follow our [Code of Conduct](./CODE_OF_CONDUCT.md)
- Ask questions if something is unclear
- Help others when you can

## Questions?

- Create an Issue with the `question` label
- Email: info@elvez.co.jp

Thank you for contributing!
