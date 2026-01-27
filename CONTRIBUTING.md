# Contributing

Thanks for your interest in contributing to `coding-policy-prompt-generator`.

## Principles

- Do not break the index sheet.
- Prefer explicit, readable code over clever tricks.
- Keep changes small and testable.
- Treat `Spec.md` as the source of truth.

## Development Setup

Prerequisites:

- Python 3.9+
- `uv` (recommended)

Setup:

```bash
uv sync --dev
```

Run tests:

```bash
uv run pytest -q
```

## Workflow

1. Open an Issue for non-trivial changes.
2. Create a branch with a descriptive name.
3. Add or update tests with the change.
4. Ensure `uv run pytest -q` passes.
5. Open a Pull Request with a clear summary.

## Pull Request Checklist

- The change aligns with `Spec.md`.
- Tests were added or updated.
- No unrelated refactors are bundled in.
- User-facing behavior is documented in `README_ja.md` when relevant.

## Scope Guidance

Good early contributions:

- Column resolution edge cases
- Sheet name constraints and idempotency
- Clearer error messages
- Template behavior improvements

Please avoid:

- Large-scale rewrites without prior discussion
- Changing the file format contract without updating `Spec.md`
