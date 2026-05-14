# Examples

各バージョンの coding-policy-prompt-generator 実行結果のサンプルです。入力 Excel と、ツールが生成した出力 Excel（`_with_prompts.xlsx`）を同梱しています。

## ディレクトリ構成

```
examples/
├── v0.2.0/         # v0.2.0 の入出力例
└── v0.2.1/         # v0.2.1 の入出力例
```

## ファイル

各バージョンディレクトリには次の 2 つのファイルが含まれます。

- `20260121AIオーディター形式サンプルコーディング規約.xlsx` — 入力 Excel（コーディング規約一覧）
- `20260121AIオーディター形式サンプルコーディング規約_with_prompts.xlsx` — そのバージョンの実装で生成した出力 Excel（プロンプト詳細シート展開済み）

## 再生成コマンド

### v0.2.1

```bash
uv run coding-policy-prompt-generator \
  docs/examples/v0.2.1/20260121AIオーディター形式サンプルコーディング規約.xlsx \
  --index-sheet "コーディング規約一覧" \
  --header-row 3 \
  --link-column "説明"
```

### v0.2.0

旧バージョンの再生成には `versions/v0.2.0/` 配下の実装を使用してください。

```bash
uv run --directory versions/v0.2.0 coding-policy-prompt-generator \
  ../../docs/examples/v0.2.0/20260121AIオーディター形式サンプルコーディング規約.xlsx \
  --index-sheet "コーディング規約一覧" \
  --header-row 3 \
  --link-column "説明"
```

## 注意事項

- 出力 Excel はテンプレート（Jinja2）と入力 Excel から決定的に生成されます（同じ入力に対して常に同じ結果）。
- 各バージョンの出力はそのバージョンの実装で生成されたものです。旧バージョンの再生成には [versions/](../../versions/) 配下の実装を使用してください。
