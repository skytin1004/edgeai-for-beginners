<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-08T19:08:07+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "ja"
}
-->
# ワークショップ クイックスタートガイド

## 前提条件

### 1. Foundry Local のインストール

公式のインストールガイドに従ってください:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Python 依存関係のインストール

ワークショップディレクトリから以下を実行してください:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## ワークショップサンプルの実行

### セッション 01: 基本的なチャット

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**環境変数:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### セッション 02: RAG パイプライン

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**環境変数:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### セッション 02: RAG 評価 (Ragas)

```bash
python rag_eval_ragas.py
```

**注意**: 追加の依存関係が `requirements.txt` を通じてインストールされる必要があります

### セッション 03: ベンチマーク

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**環境変数:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**出力**: レイテンシ、スループット、最初のトークンのメトリクスを含む JSON

### セッション 04: モデル比較

```bash
cd Workshop/samples/session04
python model_compare.py
```

**環境変数:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### セッション 05: マルチエージェントオーケストレーション

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**環境変数:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### セッション 06: モデルルーター

```bash
cd Workshop/samples/session06
python models_router.py
```

**テスト内容**: 複数のインテント (コード、要約、分類) に基づくルーティングロジック

### セッション 06: パイプライン

```bash
python models_pipeline.py
```

**内容**: 計画、実行、改良を含む複雑なマルチステップパイプライン

## スクリプト

### ベンチマークレポートのエクスポート

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**出力**: Markdown テーブル + JSON メトリクス

### Markdown CLI パターンのリント

```bash
python lint_markdown_cli.py --verbose
```

**目的**: ドキュメント内の非推奨 CLI パターンを検出

## テスト

### スモークテスト

```bash
cd Workshop
python -m tests.smoke
```

**テスト内容**: 主要なサンプルの基本機能

## トラブルシューティング

### サービスが起動していない

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### モジュールのインポートエラー

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### 接続エラー

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### モデルが見つからない

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## 環境変数リファレンス

### コア設定
| 変数 | デフォルト | 説明 |
|------|-----------|------|
| `FOUNDRY_LOCAL_ALIAS` | 可変 | 使用するモデルのエイリアス |
| `FOUNDRY_LOCAL_ENDPOINT` | 自動 | サービスエンドポイントのオーバーライド |
| `SHOW_USAGE` | `0` | トークン使用状況の統計を表示 |
| `RETRY_ON_FAIL` | `1` | リトライロジックを有効化 |
| `RETRY_BACKOFF` | `1.0` | リトライの初期遅延 (秒) |

### セッション固有
| 変数 | デフォルト | 説明 |
|------|-----------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | 埋め込みモデル |
| `RAG_QUESTION` | サンプル参照 | RAG テストの質問 |
| `BENCH_MODELS` | 可変 | カンマ区切りのモデル |
| `BENCH_ROUNDS` | `3` | ベンチマークの反復回数 |
| `BENCH_PROMPT` | サンプル参照 | ベンチマークプロンプト |
| `BENCH_STREAM` | `0` | 最初のトークンのレイテンシを測定 |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | プライマリエージェントモデル |
| `AGENT_MODEL_EDITOR` | プライマリ | エディタエージェントモデル |
| `SLM_ALIAS` | `phi-4-mini` | 小型言語モデル |
| `LLM_ALIAS` | `qwen2.5-7b` | 大型言語モデル |
| `COMPARE_PROMPT` | サンプル参照 | 比較プロンプト |

## 推奨モデル

### 開発 & テスト
- **phi-4-mini** - 品質と速度のバランスが良い
- **qwen2.5-0.5b** - 分類に非常に高速
- **gemma-2-2b** - 良好な品質と中程度の速度

### 本番環境
- **phi-4-mini** - 汎用
- **deepseek-coder-1.3b** - コード生成
- **qwen2.5-7b** - 高品質な応答

## SDK ドキュメント

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## サポートを受けるには

1. サービスの状態を確認: `foundry service status`
2. ログを確認: Foundry Local サービスログを確認
3. SDK ドキュメントを確認: https://github.com/microsoft/Foundry-Local
4. サンプルコードを確認: すべてのサンプルに詳細なドックストリングがあります

## 次のステップ

1. ワークショップセッションを順番に完了する
2. 異なるモデルを試す
3. サンプルを自分のユースケースに合わせて変更する
4. `SDK_MIGRATION_NOTES.md` を確認して高度なパターンを学ぶ

---

**最終更新日**: 2025-01-08  
**ワークショップバージョン**: 最新版  
**SDK**: Foundry Local Python SDK

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。