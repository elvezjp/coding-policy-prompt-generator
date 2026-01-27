# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project adheres to Semantic Versioning where practical.

## [Unreleased]

### Added

- Initial CLI implementation for Excel prompt generation
- Column resolution with NFC normalization and relaxed matching
- Idempotent sheet handling and collision safety improvements
- `--dry-run` planning output
- Jinja2-based `--template` support
- Test suite covering skip rules, NFC, collisions, and column resolution
