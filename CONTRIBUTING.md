# coding-policy-prompt-generator への貢献

coding-policy-prompt-generator への貢献に興味をお持ちいただきありがとうございます！このドキュメントでは、本プロジェクトへの貢献方法を説明します。

## 貢献の方法

### 1. バグの報告

バグを発見した場合は、以下の情報を含めて Issue を作成してください：

- **明確で説明的なタイトル**
- **問題を再現する手順**
- **期待される動作**
- **実際の動作**
- **サンプル Excel ファイル**（該当する場合、機密情報は削除してください）
- **バージョン情報**：
  - coding-policy-prompt-generator のバージョン
  - Python のバージョン
  - OS

### 2. 機能改善の提案

機能提案の場合は、以下の情報を含めて Issue を作成してください：

- **明確で説明的なタイトル**
- **提案する機能の詳細な説明**
- **ユースケースとメリット**
- **例やモックアップ**（該当する場合）

### 3. プルリクエスト

プルリクエストを歓迎します！以下の手順に従ってください。

## 開発環境のセットアップ

### 前提条件

- Python 3.10 以上
- `uv` パッケージマネージャ

### インストール手順

```bash
# リポジトリをクローン
git clone https://github.com/elvez-inc/coding-policy-prompt-generator.git
cd coding-policy-prompt-generator

# uv のインストール（未導入の場合）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 依存関係のインストール（開発用依存関係を含む）
uv sync --dev
```

### インストールの確認

```bash
# テストの実行
uv run pytest

# CLI の実行
uv run coding-policy-prompt-generator --help
```

## テストの実行

### 全テストの実行

```bash
uv run pytest
```

### 特定のテストファイルの実行

```bash
uv run pytest tests/test_m1_smoke.py
```

### カバレッジ付きテストの実行

```bash
uv run pytest --cov=src/coding_policy_prompt_generator --cov-report=html
```

## プルリクエストの手順

### 1. フォークとブランチの作成

```bash
# GitHub でリポジトリをフォークし、フォークをクローン
git clone https://github.com/YOUR_USERNAME/coding-policy-prompt-generator.git
cd coding-policy-prompt-generator

# フィーチャーブランチを作成
# ブランチ命名規則: {ユーザー名}/{YYYYMMDD}-{内容}
git checkout -b your-username/20260128-add-new-feature
```

### 2. コーディングスタイルへの準拠

本プロジェクトは [PEP 8](https://peps.python.org/pep-0008/) スタイルガイドに従っています。

- インデントには 4 スペースを使用
- 最大行長: 88 文字（Black のデフォルト）
- 適切な場所で型ヒントを使用

#### 命名規則

- 変数と関数: `snake_case`
- クラス: `PascalCase`
- 定数: `UPPER_SNAKE_CASE`
- プライベートメンバー: `_leading_underscore`

#### ドキュメント

- パブリック関数とクラスには docstring を追加
- Google スタイルの docstring を使用

```python
def process_rule(rule_id: str, summary: str) -> dict:
    """単一のルールを処理し、プロンプトデータを生成します。

    Args:
        rule_id: ルールの一意識別子。
        summary: ルールの概要テキスト。

    Returns:
        処理されたルールデータを含む辞書。

    Raises:
        ValueError: rule_id が空の場合。
    """
```

### 3. テストの作成

- 新機能にはテストを追加してください
- 既存のテストがパスすることを確認してください
- テストファイルは `tests/` ディレクトリに配置してください

```bash
# コミット前にテストを実行
uv run pytest
```

### 4. ドキュメントの更新

必要に応じて以下を更新してください：

- `README.md` / `README_ja.md` - 新機能や使い方の変更
- `CHANGELOG.md` - "Unreleased" セクションにエントリを追加
- docstring - コード変更に対応

### 5. コミットメッセージのルール

以下の形式に従ってください：

```
<type>: <subject>

<body>

<footer>
```

#### タイプ

- `feat`: 新機能
- `fix`: バグ修正
- `docs`: ドキュメントの変更
- `style`: フォーマット（コード変更なし）
- `refactor`: コードのリファクタリング
- `test`: テストの追加・更新
- `chore`: メンテナンスタスク

#### 例

良い例：
```
feat: カスタムテンプレート変数のサポートを追加

--extra-vars オプションを通じて Jinja2 テンプレートに
追加の変数を渡せるようになりました。

Closes #123
```

```
fix: 概要列の空セルの処理を修正

以前は空白のみのセルが有効なルールとして処理されていました。
現在は警告を出力して適切にスキップされます。
```

悪い例：
```
バグ修正
```

```
コード更新
```

### 6. プッシュとプルリクエストの作成

```bash
# ブランチをプッシュ
git push -u origin your-username/20260128-add-new-feature
```

GitHub でプルリクエストを作成し、以下を含めてください：

- 変更内容を説明する明確なタイトル
- 何が変更されたか、なぜ変更されたかの説明
- 関連する Issue への参照（例: "Closes #123"）

### 7. レビュープロセス

- メンテナーからのコードレビューをお待ちください
- フィードバックに対応し、追加のコミットをプッシュしてください
- 承認されたら、メンテナーが PR をマージします

## 送信前チェックリスト

プルリクエストを送信する前に、以下を確認してください：

- [ ] すべてのテストがパスする（`uv run pytest`）
- [ ] コードが PEP 8 スタイルガイドラインに従っている
- [ ] 新機能には対応するテストがある
- [ ] ドキュメントが更新されている
- [ ] コミットメッセージが規則に従っている
- [ ] ブランチが main と同期されている

## コードレビューのガイドライン

レビューでは以下に焦点を当てます：

- 正確性と機能性
- テストカバレッジ
- コードの可読性と保守性
- プロジェクトの規則への準拠
- ドキュメントの品質

## コミュニティガイドライン

- 敬意を持って建設的に
- [行動規範](./CODE_OF_CONDUCT.md) に従ってください
- 不明な点があれば質問してください
- 可能な範囲で他の人を助けてください

## 質問がありますか？

- `question` ラベルを付けて Issue を作成してください
- Email: info@elvez.co.jp

貢献いただきありがとうございます！
