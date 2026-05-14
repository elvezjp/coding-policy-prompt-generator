# Plan: セル結合対応と v0.2.1 リリース

関連 Issue: [#4](https://github.com/elvezjp/coding-policy-prompt-generator/issues/4)
ブランチ: `tominaga/20260514-fix-merged-cells-v0.2.1`

## 1. 背景

`src/coding_policy_prompt_generator/excel_io.py` の `_process_rows()` が `worksheet.cell(...).value` で直接セル値を取得しているため、分類・カテゴリ列がセル結合されている場合、結合範囲の 2 行目以降が `None` となりプロンプトに「（未指定）」が出力される（[Issue #4](https://github.com/elvezjp/coding-policy-prompt-generator/issues/4)）。

v0.2.0 でも未修正のため、v0.2.1（パッチリリース）で対応する。

## 2. 方針

- バグ修正のみのパッチリリースとして **v0.2.0 → v0.2.1**。
- 公開後も過去バージョンの実装・仕様を参照できるよう、リリース単位のスナップショットを `versions/` 配下に残す運用を導入する。
- 影響範囲は分類列・カテゴリ列・説明列の 3 列（Issue 対応案どおり）。

## 3. 全体の流れ

1. **過去バージョンの保全**
   現在の `src/`、`spec.md`、`pyproject.toml`、`uv.lock` を `versions/v0.2.0/` 配下にコピーしてコミットする。以降、リリースごとに同様のスナップショットを残す運用とする。
2. **結合セル対応の実装**
   `excel_io.py` に `_get_merged_cell_value(worksheet, row, col)` ヘルパーを追加し、`_process_rows()` 内の分類・カテゴリ・説明列の値取得を差し替える。
3. **テスト追加**
   結合セルを含むサンプル Excel を用意し、2 行目以降でも結合元の値が取得されることを検証するテストを追加する。
4. **仕様書の更新**
   `spec.md` に結合セルの取り扱いに関する記述を追加する。
5. **バージョン・ドキュメント更新**
   `pyproject.toml` を `0.2.1` に、`CHANGELOG.md` / `CHANGELOG_ja.md` / `SECURITY.md` / `SECURITY_ja.md` のサポートバージョン表を更新する。
6. **検証**
   `uv sync --dev` / `uv run pytest` / 実行サンプルで動作確認。
7. **PR 作成と Issue クローズ**

## 4. 試験項目

### 4.1 自動テスト（pytest）

- [ ] 結合セルなしの既存サンプルで、従来どおり全行の分類・カテゴリ・説明が取得できる（リグレッション）
- [ ] 分類列のみが結合されたサンプルで、結合範囲内の全行で分類値が取得できる
- [ ] カテゴリ列のみが結合されたサンプルで、結合範囲内の全行でカテゴリ値が取得できる
- [ ] 説明列が結合されたサンプルで、結合範囲内の全行で説明値が取得できる
- [ ] 分類・カテゴリ・説明が同時に結合されたサンプルで、3 列とも結合元の値が取得できる
- [ ] 結合範囲の左上セル自身でも従来どおり値が取得できる
- [ ] 結合セル外で空セルの場合は従来どおり「（未指定）」として扱われる（誤って結合元を引かない）

### 4.2 手動検証

- [ ] `uv run pytest` が全件パス
- [ ] `uv run coding-policy-prompt-generator --help` がエラーなく動作
- [ ] 結合セルを含むサンプル Excel で実際に生成されたプロンプトを目視確認

## 5. 完了チェック

- [ ] `versions/v0.2.0/` に v0.2.0 時点の `src/`、`spec.md`、`pyproject.toml`、`uv.lock` が保存されている
- [ ] `_get_merged_cell_value` ヘルパーが追加され、`_process_rows()` の分類・カテゴリ・説明列で使用されている
- [ ] 「4.1 自動テスト」のテストケースがすべて追加・パスしている
- [ ] `spec.md` に結合セルの取り扱いが追記されている
- [ ] `pyproject.toml` の `version` が `0.2.1`
- [ ] `CHANGELOG.md` / `CHANGELOG_ja.md` に `## [0.2.1] - 2026-05-14` セクションが追加されている
- [ ] `SECURITY.md` / `SECURITY_ja.md` のサポートバージョン表が `0.2.x: ✅` を維持しつつ最新版表記が `0.2.1` に揃っている
- [ ] Issue [#4](https://github.com/elvezjp/coding-policy-prompt-generator/issues/4) がクローズできる状態になる
