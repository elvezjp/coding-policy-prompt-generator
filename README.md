# coding-policy-prompt-generator

[English](./README.md) | [日本語](./README_ja.md)

[![Elvez](https://img.shields.io/badge/Elvez-Product-3F61A7?style=flat-square)](https://elvez.co.jp/)
[![IXV Ecosystem](https://img.shields.io/badge/IXV-Ecosystem-3F61A7?style=flat-square)](https://elvez.co.jp/ixv/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-recommended-5C2D91?style=flat-square)](https://docs.astral.sh/uv/)

A CLI tool that reads an Excel-based coding policy (1 row = 1 rule), automatically generates **rule-level prompts (System Prompts) for an AI auditor**, and expands them into "detail sheets" inside the same workbook.

---

## Use Cases

- **Automated Code Review**: Feed coding policies into AI for automated review and auditing
- **Rules as Data**: Manage rules as structured data (not just prose) with AI execution definitions
- **End-to-End Pipeline**: Automate the conversion from policy (Excel) to prompt (System) to audit result (JSON)
- **AI Auditor Integration**: Use as a preprocessor for `coding-policy-ai-auditor`

---

## Background

This tool is a small utility born during the development of **IXV**, an AI assistant for Japanese development documents and specifications.

IXV addresses challenges in understanding, structuring, and utilizing Japanese documents in software development. This repository provides a standalone component from that ecosystem.

---

## Features

- Generate **1 prompt per rule** from an Excel policy where **1 row = 1 rule**
- Automatically create **detail sheets** (e.g., `PROMPT_XXXX`) for each rule
- Automatically set **Excel-internal links (HYPERLINK)** from the index sheet's link column
- Standardize prompt generation with templates and **JSON output format** (OK/NG/reason)
- Extend existing policy workbooks by **appending** without breaking the index sheet
- Ensure **idempotency** - re-runs do not destroy existing data

---

## Documents

- [CHANGELOG.md](CHANGELOG.md) - Version history
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guide
- [SECURITY.md](SECURITY.md) - Security policy
- [spec.md](spec.md) - Technical specification

---

## Setup

### Requirements

- Python 3.9 or higher
- `uv` package manager (recommended)

### Install Dependencies

```bash
# Install uv (if not already installed)
# See: https://docs.astral.sh/uv/getting-started/installation/
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync dependencies
uv sync --dev
```

> Note: Run `uv sync` from the directory containing `pyproject.toml`.

---

## Usage

### Basic Usage

```bash
uv run coding-policy-prompt-generator input.xlsx
```

This reads `input.xlsx` and generates a **prompt-expanded workbook** in the same directory.

- Default output name: `<stem>_with_prompts.xlsx`
- Example: `input.xlsx` → `input_with_prompts.xlsx`

### Examples

#### 1) Generate prompts with the built-in template

```bash
uv run coding-policy-prompt-generator rules.xlsx
```

#### 2) Specify the output filename

```bash
uv run coding-policy-prompt-generator rules.xlsx -o rules_prompts.xlsx
```

#### 3) Use a custom prompt template (Jinja2)

```bash
uv run coding-policy-prompt-generator rules.xlsx --template ./templates/system_prompt.j2
```

#### 4) Specify the index sheet name / link column name

```bash
uv run coding-policy-prompt-generator rules.xlsx \
  --index-sheet "Policy Index" \
  --link-column "Detail Link"
```

#### 5) Preview changes (dry-run)

```bash
uv run coding-policy-prompt-generator rules.xlsx --dry-run
```

---

## Main Options

### I/O

| Option | Default | Description |
|---|---|---|
| `-o`, `--output` | Same directory as input | Output Excel path |
| `--dry-run` | false | Show change summary only; do not write the file |

### Sheet / Column Mapping

| Option | Default | Description |
|---|---|---|
| `--index-sheet` | First sheet | Index sheet name |
| `--header-row` | `1` | Header row number (sample uses `3`) |
| `--id-column` | `項番` | Rule ID column |
| `--summary-column` | `概要` | Rule summary column |
| `--description-column` | `説明` | Description / notes column |
| `--link-column` | Rightmost header column | Detail link column |

### Generation

| Option | Default | Description |
|---|---|---|
| `--sheet-prefix` | `PROMPT_` | Prefix for detail sheet names |
| `--template` | Built-in | Prompt template file (Jinja2) |

---

## Output Example

### Generated Detail Sheets

The tool creates one sheet per rule and writes the prompt body starting at cell A1.

- Example sheet names: `PROMPT_N-001` / `PROMPT_001`

```text
[SYSTEM PROMPT]

You are an AI auditor that reviews software code.
Evaluate the code using only the following rule.

[Rule ID]
N-001

[Rule Summary]
(Content from the "Summary" column in Excel)

[Notes]
(Content from the "Description" column in Excel)

[Output Format]
{
  "rule_id": "N-001",
  "result": "OK | NG",
  "reason": "Brief explanation"
}
```

---

## Input Excel Assumptions

### Recommended Format

- **First sheet**: Rule index (1 row = 1 rule)
- Link column: Column for detail links (default: rightmost header column)

| Column name (example) | Purpose |
|---|---|
| Item / RuleID | Rule ID (used in prompt sheet names and JSON output) |
| Classification | High-level grouping (optional) |
| Category | Target scope (e.g., general / class / method) |
| Summary | The rule statement (core input for prompt generation) |
| Description | Background, exceptions, examples (optional) |
| Detail Link | Link column overwritten by the tool (required) |

### Sample Excel

The following sample workbook is used for implementation and verification:

- `docs/ai-auditor-format/20260121AIオーディター形式サンプルコーディング規約.xlsx`

---

## Directory Structure

```text
coding-policy-prompt-generator/
├── docs/                   # Documentation and samples
├── src/                    # Source code
├── tests/                  # Test code
├── CHANGELOG.md            # Version history
├── CONTRIBUTING.md         # Contribution guide
├── LICENSE                 # License
├── README.md               # README (English)
├── README_ja.md            # README (Japanese)
├── SECURITY.md             # Security policy
├── pyproject.toml          # Project configuration
└── spec.md                 # Technical specification
```

---

## Security

For details, see [SECURITY.md](SECURITY.md).

- Only process Excel files from trusted sources
- Macros (VBA) are not executed
- Generated prompts and links are stored as plain text in the workbook (be careful with sensitive data)

---

## Contributing

Issues and Pull Requests are welcome. For details, see [CONTRIBUTING.md](CONTRIBUTING.md).

- **Bug reports**: GitHub Issues
- **Improvement proposals**: Issues or Discussions
- **PRs**: Small, focused changes preferred (tests recommended)

---

## Changelog

For details, see [CHANGELOG.md](CHANGELOG.md).

---

## License

MIT License - See [LICENSE](LICENSE) for details.

---

## Contact

- **Email**: info@elvez.co.jp
- **Company**: Elvez, Inc.
