# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial CLI implementation (`coding-policy-prompt-generator`) for converting Excel-based coding policies to AI auditor prompts
- Column resolution with NFC normalization and relaxed matching for Japanese header variations
- Idempotent detail sheet handling with rule ID markers to prevent data loss on re-runs
- Sheet name collision safety with automatic suffix generation
- `--dry-run` option for previewing changes without modifying files
- Jinja2-based `--template` support for custom prompt templates
- Comprehensive test suite covering:
  - Skip rules for empty/incomplete rows
  - NFC normalization for Japanese text
  - Sheet name collisions
  - Column resolution edge cases

### Technical Details

- Uses `openpyxl` for Excel file manipulation
- Supports Python 3.9+
- Package management via `uv`

## Links

- Repository: https://github.com/elvez-inc/coding-policy-prompt-generator
- Issue Tracker: https://github.com/elvez-inc/coding-policy-prompt-generator/issues
