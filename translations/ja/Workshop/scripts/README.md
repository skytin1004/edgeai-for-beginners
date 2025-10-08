<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-08T19:30:32+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "ja"
}
-->
# ワークショップスクリプト

このディレクトリには、ワークショップ資料の品質と一貫性を維持するための自動化およびサポートスクリプトが含まれています。

## 内容

| ファイル | 目的 |
|------|---------|
| `lint_markdown_cli.py` | Markdownのコードブロック内で非推奨のFoundry Local CLIコマンドパターンをブロックするためのリントツール。 |
| `export_benchmark_markdown.py` | 複数モデルのレイテンシベンチマークを実行し、MarkdownとJSONレポートを生成します。 |

## 1. Markdown CLIパターンリントツール

`lint_markdown_cli.py`は、翻訳されていないすべての`.md`ファイルをスキャンし、**コードブロック内**（``` ... ```）で許可されていないFoundry Local CLIパターンを検出します。情報提供のための文章では、歴史的な文脈で非推奨コマンドを言及することが可能です。

### 非推奨パターン（コードブロック内でブロック）

リントツールは非推奨のCLIパターンをブロックします。代わりに最新の代替案を使用してください。

### 必須の置き換え
| 非推奨 | 使用すべき代替 |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | ベンチマークスクリプト + システムツール（`タスクマネージャー`、`nvidia-smi`） |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### 終了コード
| コード | 意味 |
|------|---------|
| 0 | 違反なし |
| 1 | 1つ以上の非推奨パターンが検出された |

### ローカルでの実行
リポジトリのルートから（推奨）:

Windows（PowerShell）:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### プリコミットフック（オプション）
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
これにより、非推奨パターンを導入するコミットがブロックされます。

### CI統合
GitHub Actionワークフロー（`.github/workflows/markdown-cli-lint.yml`）が、`main`および`Reactor`ブランチへのプッシュやプルリクエストごとにリントツールを実行します。失敗したジョブはマージ前に修正する必要があります。

### 新しい非推奨パターンの追加
1. `lint_markdown_cli.py`を開きます。
2. タプル`(regex, suggestion)`を`DEPRECATED`リストに追加します。生文字列を使用し、適切な場合は`\b`単語境界を含めます。
3. ローカルでリントツールを実行し、検出を確認します。
4. コミットしてプッシュします。CIが新しいルールを強制します。

追加例:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### 説明的な言及を許可
コードブロックのみが強制されるため、非推奨コマンドを説明文で安全に記述できます。対比のためにコードブロック内で表示する必要がある場合は、**三重バックティックを使用しない**ブロック（例: インデントや引用）を追加するか、擬似形式に書き換えてください。

### 特定ファイルのスキップ（高度な設定）
必要に応じて、レガシー例をリポジトリ外の別ファイルにラップするか、ドラフト中に別の拡張子で名前を変更します。翻訳されたコピーに対する意図的なスキップは自動的に行われます（`translations`を含むパス）。

### トラブルシューティング
| 問題 | 原因 | 解決策 |
|-------|-------|-----------|
| リントツールが更新した行をフラグする | 正規表現が広すぎる | 追加の単語境界（`\b`）やアンカーでパターンを狭める |
| CIが失敗するがローカルでは成功する | 異なるPythonバージョンまたは未コミットの変更 | ローカルで再実行し、作業ツリーがクリーンであることを確認し、ワークフローのPythonバージョン（3.11）を確認 |
| 一時的にバイパスする必要がある | 緊急のホットフィックス | 修正を直ちに適用し、可能であれば一時的なブランチとフォローアップPRを使用（バイパススイッチの追加は避ける） |

### 理由
ドキュメントを*現在の*安定したCLIインターフェースに合わせることで、ワークショップの混乱を防ぎ、学習者の混乱を回避し、Pythonスクリプトを通じてパフォーマンス測定を集中化します。

---
ワークショップ品質ツールチェーンの一部として維持されています。改善（例: 自動修正提案やHTMLレポート生成）については、Issueを作成するかPRを提出してください。

## 2. サンプル検証スクリプト

`validate_samples.py`は、すべてのPythonサンプルファイルを構文、インポート、およびベストプラクティスの遵守について検証します。

### 使用方法
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### 検証内容
- ✅ Python構文の有効性
- ✅ 必須インポートの存在
- ✅ エラーハンドリングの実装（詳細モード）
- ✅ 型ヒントの使用（詳細モード）
- ✅ 関数のドキュメンテーション（詳細モード）
- ✅ SDK参照リンク（詳細モード）

### 環境変数
- `SKIP_IMPORT_CHECK=1` - インポート検証をスキップ
- `SKIP_SYNTAX_CHECK=1` - 構文検証をスキップ

### 終了コード
- `0` - すべてのサンプルが検証に合格
- `1` - 1つ以上のサンプルが失敗

## 3. サンプルテストランナー

`test_samples.py`は、すべてのサンプルがエラーなく実行できることを確認するためのスモークテストを実行します。

### 使用方法
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### 前提条件
- Foundry Localサービスが実行中: `foundry service start`
- モデルがロード済み: `foundry model run phi-4-mini`
- 依存関係がインストール済み: `pip install -r requirements.txt`

### テスト内容
- ✅ サンプルがランタイムエラーなしで実行可能
- ✅ 必要な出力が生成される
- ✅ 失敗時の適切なエラーハンドリング
- ✅ パフォーマンス（実行時間）

### 環境変数
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - テストに使用するモデル
- `TEST_TIMEOUT=30` - サンプルごとのタイムアウト（秒）

### 予想される失敗
一部のテストは、オプションの依存関係がインストールされていない場合に失敗する可能性があります（例: `ragas`、`sentence-transformers`）。以下でインストールしてください:
```bash
pip install sentence-transformers ragas datasets
```

### 終了コード
- `0` - すべてのテストが合格
- `1` - 1つ以上のテストが失敗

## 4. ベンチマークMarkdownエクスポーター

スクリプト: `export_benchmark_markdown.py`

モデルセットの再現可能なパフォーマンステーブルを生成します。

### 使用方法
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### 出力
| ファイル | 説明 |
|------|-------------|
| `benchmark_report.md` | Markdownテーブル（平均、p95、トークン/秒、オプションの最初のトークン） |
| `benchmark_report.json` | 差分および履歴用の生メトリクス配列 |

### オプション
| フラグ | 説明 | デフォルト |
|------|-------------|---------|
| `--models` | カンマ区切りのモデルエイリアス | （必須） |
| `--prompt` | 各ラウンドで使用されるプロンプト | （必須） |
| `--rounds` | モデルごとのラウンド数 | 3 |
| `--output` | Markdown出力ファイル | `benchmark_report.md` |
| `--json` | JSON出力ファイル | `benchmark_report.json` |
| `--fail-on-empty` | すべてのベンチマークが失敗した場合に非ゼロ終了 | オフ |

環境変数`BENCH_STREAM=1`を設定すると、最初のトークンのレイテンシ測定が追加されます。

### 注意事項
- 一貫したモデルのブートストラップとキャッシングのために`workshop_utils`を再利用します。
- 別の作業ディレクトリから実行する場合、スクリプトは`workshop_utils`を見つけるためにパスフォールバックを試みます。
- GPU比較の場合: 一度実行し、CLI設定でアクセラレーションを有効にして再実行し、JSONを比較してください。

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。