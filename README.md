# coding-policy-prompt-generator

[English](./README.md) | [日本語](./README_ja.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-recommended-5C2D91.svg)](https://docs.astral.sh/uv/)

A CLI tool that reads an Excel-based coding policy (1 row = 1 rule), automatically generates **rule-level prompts (System Prompts) for an AI auditor**, and expands them into “detail sheets” inside the same workbook. This README also serves as a design-and-usage document.

- Input: a coding policy workbook (for example, the first sheet is the rule index, and the rightmost column is a “detail link” column)
- Output: one detail sheet per rule (prompt body) + hyperlinks from the rule index to each detail sheet

> Goal: **preserve Excel-native workflows while converting policies into executable definitions for AI auditing.**

---

## Current Status

- This repository is implemented through **M4 (template / dry-run)**
- As of **January 27, 2026**, both `src/` and `pyproject.toml` are present
- Some CLI options are still future-facing / MVP-external (for example, `--output-format`)

---

## Features

- Generate **1 prompt per rule** from an Excel policy where **1 row = 1 rule**
- Automatically create rule detail sheets (for example, `PROMPT_XXXX`)
- Automatically set **Excel-internal links (HYPERLINK)** from the index sheet’s link column (default: the rightmost header column)
- Use templates for prompt generation and standardize the **JSON output shape** (OK / NG / reason)
- Extend existing policy workbooks by **appending** auditing definitions without breaking the index sheet

---

## Intended Use Cases

- Feed coding policies into AI and run **automated review / automated auditing**
- Manage rules as **data**, not just prose, and include AI execution definitions
- Build a full pipeline: policy (Excel) → prompt (System) → audit result (JSON)
- Use this as a preprocessor for `coding-policy-ai-auditor`

---

## Documents

- `CHANGELOG.md` - Version history
- `CONTRIBUTING.md` - Contribution guide
- `SECURITY.md` - Security policy
- `CODE_OF_CONDUCT.md` - Code of conduct
- `.github/` - Issue / Pull Request templates

---

## Setup

### Requirements

- Python 3.9+
- `uv` package manager (recommended)

### Install Dependencies

```bash
# Install uv (if needed)
# See: https://docs.astral.sh/uv/getting-started/installation/
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync dependencies
uv sync --dev
```

> Note: run `uv sync` from the directory that contains `pyproject.toml`.

---

## Usage (CLI)

Basic form:

```bash
uv run coding-policy-prompt-generator input.xlsx
```

This reads `input.xlsx` and generates a prompt-expanded workbook in the same directory.

- Default output name: `<stem>_with_prompts.xlsx`
- Example: `input.xlsx` → `input_with_prompts.xlsx`

> You can change the output path via `-o/--output`.

---

## Examples

### 1) Generate prompts with the built-in template

```bash
uv run coding-policy-prompt-generator rules.xlsx
```

### 2) Specify the output filename

```bash
uv run coding-policy-prompt-generator rules.xlsx -o rules_prompts.xlsx
```

### 3) Swap in a prompt template (Jinja2)

```bash
uv run coding-policy-prompt-generator rules.xlsx --template ./templates/system_prompt.j2
```

### 4) Specify the index sheet name / link column name

```bash
uv run coding-policy-prompt-generator rules.xlsx \
  --index-sheet "Policy Index" \
  --link-column "Detail Link"
```

---

## Input Excel Assumptions (Recommended Format)

- **First sheet**: rule index (1 row = 1 rule)
- Link column: the column used for detail links (default: the rightmost header column, for example `Detail Link`)
- It is recommended that the rule index contains at least the following columns:

| Column name (example) | Purpose |
|---|---|
| Item / RuleID | Rule ID (used in prompt sheet names and JSON output) |
| Classification | High-level grouping (optional) |
| Category | Target scope (for example: general / class / method) |
| Summary | The rule statement (core input for prompt generation) |
| Description | Background, exceptions, examples (optional) |
| Detail Link | The link column overwritten by the tool (required; writes into an existing column) |

> The tool is designed to allow column-name mapping via CLI options so it can fit existing workbooks.
> Header comparisons use NFC normalization, and the implementation tolerates some whitespace / separator variation.
> If required column resolution becomes ambiguous, the tool fails fast for safety.

### Sample Excel (in this repository)

We use the following sample workbook as the baseline for implementation and verification:

- `docs/ai-auditor-format/20260121AIオーディター形式サンプルコーディング規約.xlsx`

Key characteristics of the sample (implementation notes):

- Index sheet name: `コーディング規約一覧`
- Header row: row 3 (rows 1–2 are explanatory text)
- Headers are roughly: `項番 / 分類 / カテゴリ / 概要 / 説明`
- The first data cell in the `説明` column contains `リンク`, effectively making it the link column
- In that case, the `説明` column is treated as the link column and description text is not used

For safety, the implementation should support at least one of the following:

- Specify the header row number
- Explicitly specify the link column name (for example, treat `説明` as the link column)
- Skip pre-header explanatory rows

---

## Generated Detail Sheets (Example)

The tool creates one sheet per rule and writes the prompt body starting at cell A1.

- Example sheet names: `PROMPT_N-001`, `PROMPT_001` (derived from rule ID and naming rules)

Generation image:

```text
[SYSTEM PROMPT]

You are an AI auditor that reviews software code.
Evaluate the code using only the following rule.

[Rule ID]
N-001

[Classification]
(from the Excel “Classification” column, if present)

[Category]
(from the Excel “Category” column, if present)

[Rule Summary]
(from the Excel “Summary” column)

[Notes]
(from the Excel “Description” column, etc.)

[Output Format]
{
  "rule_id": "N-001",
  "result": "OK | NG",
  "reason": "Brief, clear Japanese explanation"
}
```

---

## Main Options (Design + Current Behavior)

> Keep this section aligned with the implementation. It reflects both the current behavior and the intended CLI shape.

### I/O

| Option | Default | Description |
|---|---:|---|
| `-o`, `--output` | Same directory as input | Output Excel path |
| `--dry-run` | false | Show the change plan only; do not write the file |

### Sheet / Column Mapping

| Option | Default | Description |
|---|---:|---|
| `--index-sheet` | First sheet | Index sheet name |
| `--header-row` | `1` | Header row number (the sample uses `3`) |
| `--id-column` | `項番` | Rule ID column |
| `--summary-column` | `概要` | Rule summary column |
| `--description-column` | `説明` | Description / notes column |
| `--link-column` | Rightmost header column | Detail link column (if omitted, the rightmost header column is used) |

> The link column is always an existing column. If the specified column (or the rightmost header column) cannot be resolved, the tool fails with an error (per `Spec.md`).
> Existing detail sheets are only updated when A1 contains the rule ID marker. If it does not match, the tool creates a new sheet.
> Marker format: `【ルールID】\n<rule_id>` (example: `【ルールID】\nN-001`)

### Generation

| Option | Default | Description |
|---|---:|---|
| `--sheet-prefix` | `PROMPT_` | Prefix for detail sheet names |
| `--template` | Built-in | Prompt template file (Jinja2) |
| `--output-format` | `json` | Audit output format hint (planned; MVP-external) |

> Note: `--output-format` is outside the current MVP scope. `--template` is implemented (requires Jinja2).

---

## Repository Structure (Current)

```text
coding-policy-prompt-generator/
├── .github/
├── docs/
├── src/
├── tests/
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── README_ja.md
├── SECURITY.md
└── pyproject.toml
```

---

## Security

- Only process Excel files you trust
- Macros (VBA) are not executed
- Generated prompts and links are stored as plain text in the workbook (be careful with sensitive data)

---

## Contributing

Issues and Pull Requests are welcome.

- Bug reports: GitHub Issues
- Improvement proposals: Issues or Discussions
- PRs: small, focused changes are preferred (tests are strongly recommended)

---

## Background

This tool originated as one of a set of verification utilities created during the development of the IXV AI assistant. Its role is the pre-processing step of turning **Excel-based coding policies into AI-executable definitions**.

---

## License

MIT License. See `LICENSE` for details.

---

## Contact

- Email: info@elvez.co.jp
- Company: Elvez, Inc.
