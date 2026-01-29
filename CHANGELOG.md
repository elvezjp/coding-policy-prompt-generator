# 変更履歴

このプロジェクトにおける注目すべき変更はすべてこのファイルに記録されます。

このファイルの形式は [Keep a Changelog](https://keepachangelog.com/ja/1.0.0/) に基づいており、
このプロジェクトは [セマンティックバージョニング](https://semver.org/lang/ja/) に準拠しています。

## [0.1.0] - 2026-01-29

### 追加

- Excelベースのコーディング規約をAIオーディター向けプロンプトに変換する初期CLI実装（`coding-policy-prompt-generator`）
- 日本語ヘッダーの揺れに対応したNFC正規化と柔軟なマッチングによる列解決機能
- ルールIDマーカーによる冪等な詳細シート処理（再実行時のデータ損失を防止）
- 自動サフィックス生成によるシート名衝突の安全対策
- ファイルを変更せずに変更内容をプレビューする `--dry-run` オプション
- カスタムプロンプトテンプレート用のJinja2ベース `--template` サポート
- 判定の厳格度を指定する `--strictness` オプション（`strict` / `lenient`）
- プロジェクト前提情報を指定する `--project-context` オプション
- 詳細シートの2セル分割出力（A1: システムプロンプト、A2: ユーザープロンプト）
- デフォルトテンプレートの外部ファイル化（`templates/system_prompt.j2`, `user_prompt.j2`）
- ユーザープロンプトの新セクション（重大度、適用範囲・例外、グレーゾーンの具体例）
- 以下をカバーする包括的なテストスイート：
  - 空行・不完全な行のスキップルール
  - 日本語テキストのNFC正規化
  - シート名の衝突
  - 列解決のエッジケース

### 技術詳細

- Excelファイル操作に `openpyxl` を使用
- テンプレートエンジンに `jinja2` を使用
- Python 3.9+ をサポート
- `uv` によるパッケージ管理

## リンク

- リポジトリ: https://github.com/elvezjp/coding-policy-prompt-generator
- Issue トラッカー: https://github.com/elvezjp/coding-policy-prompt-generator/issues
