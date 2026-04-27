# Changelog

[English](./CHANGELOG.md) | [日本語](./CHANGELOG_ja.md)

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-04-27

### Changed (Breaking)

- Raised the minimum supported Python version to **3.10** (Python 3.9 support dropped)
- Updated the CI matrix Python versions to `["3.10", "3.13"]`

### Fixed

- Bumped `pytest` to `9.0.3` or later (resolves CVE-2025-71176 / GHSA-6w46-j5rx-g56g, Dependabot #2)
- Resolved `Pygments` to `2.20.0` or later transitively via the `pytest` upgrade (CVE-2026-4539 / GHSA-5239-wwwm-4pmq, Dependabot #1). `Pygments` is not a direct dependency.

## [0.1.0] - 2026-01-29

### Added

- Initial CLI implementation (`coding-policy-prompt-generator`) that converts Excel-based coding policies into prompts for AI auditors
- Column resolution with NFC normalization and flexible matching to handle Japanese header variations
- Idempotent detail-sheet processing using rule-ID markers (prevents data loss on re-runs)
- Sheet-name collision protection via automatic suffix generation
- `--dry-run` option to preview changes without modifying the file
- Jinja2-based `--template` support for custom prompt templates
- `--strictness` option to control judgement strictness (`strict` / `lenient`)
- `--project-context` option to specify project preconditions
- Two-cell detail-sheet output (A1: system prompt, A2: user prompt)
- Externalized default templates (`templates/system_prompt.j2`, `templates/user_prompt.j2`)
- New user-prompt sections: severity, scope/exceptions, gray-zone examples
- Comprehensive test suite covering:
  - Skip rules for empty/incomplete rows
  - NFC normalization of Japanese text
  - Sheet-name collisions
  - Column-resolution edge cases

### Technical Notes

- Uses `openpyxl` for Excel manipulation
- Uses `jinja2` for the template engine
- Supports Python 3.9+ (raised to 3.10+ in v0.2.0)
- Package management via `uv`

## Links

- Repository: https://github.com/elvezjp/coding-policy-prompt-generator
- Issue tracker: https://github.com/elvezjp/coding-policy-prompt-generator/issues
