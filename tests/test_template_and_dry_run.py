from pathlib import Path

import pytest
from openpyxl import Workbook, load_workbook

from coding_policy_prompt_generator.excel_io import ColumnConfig, generate_prompts


def _make_input(path: Path) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "一覧"
    headers = ["項番", "分類", "カテゴリ", "概要", "説明"]
    for col, name in enumerate(headers, start=1):
        ws.cell(row=1, column=col, value=name)

    ws.cell(row=2, column=1, value="R-1")
    ws.cell(row=2, column=2, value="設計")
    ws.cell(row=2, column=3, value="命名")
    ws.cell(row=2, column=4, value="概要")
    ws.cell(row=2, column=5, value="補足")

    wb.save(path)


def test_template_file_is_applied(tmp_path: Path) -> None:
    pytest.importorskip("jinja2")
    input_path = tmp_path / "input.xlsx"
    output_path = tmp_path / "output.xlsx"
    template_path = tmp_path / "template.j2"

    _make_input(input_path)
    template_path.write_text(
        "RULE={{ rule_id }}\nCLASS={{ classification }}\nCAT={{ category }}\nSUMMARY={{ summary }}",
        encoding="utf-8",
    )

    generate_prompts(
        input_path=input_path,
        output_path=output_path,
        index_sheet="一覧",
        header_row=1,
        columns=ColumnConfig(
            id_column="項番",
            summary_column="概要",
            description_column="説明",
            link_column="説明",
        ),
        sheet_prefix="PROMPT_",
        dry_run=False,
        template_path=template_path,
    )

    wb = load_workbook(output_path)
    prompt = wb["PROMPT_R-1"]["A1"].value
    assert isinstance(prompt, str)
    assert "RULE=R-1" in prompt
    assert "CLASS=設計" in prompt
    assert "CAT=命名" in prompt


def test_dry_run_does_not_write_output(tmp_path: Path) -> None:
    input_path = tmp_path / "input.xlsx"
    output_path = tmp_path / "dry_run_output.xlsx"
    _make_input(input_path)

    plan = generate_prompts(
        input_path=input_path,
        output_path=output_path,
        index_sheet="一覧",
        header_row=1,
        columns=ColumnConfig(
            id_column="項番",
            summary_column="概要",
            description_column="説明",
            link_column="説明",
        ),
        sheet_prefix="PROMPT_",
        dry_run=True,
    )

    assert plan.processed_rules == 1
    assert output_path.exists() is False
    assert any(action.kind == "create" for action in plan.actions)
