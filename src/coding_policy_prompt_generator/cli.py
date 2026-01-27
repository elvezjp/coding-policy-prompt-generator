from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .excel_io import ColumnConfig, GenerationPlan, generate_prompts


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="coding-policy-prompt-generator",
        description="Generate AI auditor prompts from coding policy Excel files.",
    )

    parser.add_argument("input", help="Path to input .xlsx file")
    parser.add_argument("-o", "--output", help="Path to output .xlsx file")
    parser.add_argument("--dry-run", action="store_true", help="Show plan only; do not write output")

    parser.add_argument("--index-sheet", help="Index sheet name (default: first sheet)")
    parser.add_argument("--header-row", type=int, default=1, help="Header row number (1-based)")

    parser.add_argument("--id-column", default="項番", help="Rule ID column name")
    parser.add_argument("--summary-column", default="概要", help="Rule summary column name")
    parser.add_argument("--description-column", default="説明", help="Rule description column name")
    parser.add_argument("--link-column", help="Link column name (default: rightmost header column)")

    parser.add_argument("--sheet-prefix", default="PROMPT_", help="Detail sheet name prefix")
    parser.add_argument("--template", help="Template file path (Jinja2)")
    parser.add_argument(
        "--output-format",
        default="json",
        help="Output format hint (reserved for future use; default: json)",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1

    if input_path.suffix.lower() != ".xlsx":
        print("Input must be a .xlsx file", file=sys.stderr)
        return 1

    output_path = Path(args.output) if args.output else _default_output_path(input_path)
    if input_path.resolve() == output_path.resolve():
        print("Output path must differ from input path", file=sys.stderr)
        return 1

    columns = ColumnConfig(
        id_column=args.id_column,
        summary_column=args.summary_column,
        description_column=args.description_column,
        link_column=args.link_column,
    )

    if args.output_format and args.output_format != "json":
        print("Note: --output-format is reserved for future use in MVP.", file=sys.stderr)

    try:
        plan = generate_prompts(
            input_path=input_path,
            output_path=output_path,
            index_sheet=args.index_sheet,
            header_row=args.header_row,
            columns=columns,
            sheet_prefix=args.sheet_prefix,
            dry_run=args.dry_run,
            template_path=Path(args.template) if args.template else None,
        )
    except Exception as exc:  # pragma: no cover - exercised in error scenarios
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    _print_plan(plan=plan, output_path=output_path, dry_run=args.dry_run)
    return 0


def _default_output_path(input_path: Path) -> Path:
    return input_path.with_name(f"{input_path.stem}_with_prompts.xlsx")


def _print_plan(*, plan: GenerationPlan, output_path: Path, dry_run: bool) -> None:
    mode = "DRY-RUN" if dry_run else "APPLY"
    created_count = len(plan.created_sheets)
    updated_count = len(plan.updated_sheets)
    skipped_count = len(plan.skipped_rows)
    print(
        f"[{mode}] processed_rules={plan.processed_rules} "
        f"created={created_count} updated={updated_count} skipped={skipped_count}"
    )

    if plan.warnings:
        for message in plan.warnings:
            print(f"Warning: {message}", file=sys.stderr)

    if plan.created_sheets:
        print("created_sheets:")
        for name in plan.created_sheets:
            print(f"  - {name}")

    if plan.updated_sheets:
        print("updated_sheets:")
        for name in plan.updated_sheets:
            print(f"  - {name}")

    if plan.skipped_rows:
        print("skipped_rows:")
        for rec in plan.skipped_rows:
            print(f"  - row {rec.row}: {rec.reason}")

    if dry_run:
        print(f"dry_run_output_path={output_path}")
    else:
        print(f"output_path={output_path}")


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
