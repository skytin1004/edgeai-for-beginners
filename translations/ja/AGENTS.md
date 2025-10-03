<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:26:44+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ja"
}
-->
# AGENTS.md

## プロジェクト概要

EdgeAI for Beginnersは、小型言語モデル（SLM）を使用したEdge AI開発を学ぶための包括的な教育リポジトリです。このコースでは、EdgeAIの基礎、モデルのデプロイ、最適化技術、Microsoft Foundry LocalやさまざまなAIフレームワークを使用した実践的な実装をカバーしています。

**主要技術:**
- Python 3.8+（AI/MLサンプルの主要言語）
- .NET C#（AI/MLサンプル）
- JavaScript/Node.jsとElectron（デスクトップアプリケーション用）
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AIフレームワーク: LangChain, Semantic Kernel, Chainlit
- モデル最適化: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**リポジトリタイプ:** 8つのモジュールと10の包括的なサンプルアプリケーションを含む教育コンテンツリポジトリ

**アーキテクチャ:** 実践的なサンプルを通じてEdge AIデプロイメントパターンを示すマルチモジュール学習パス

## リポジトリ構造

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## セットアップコマンド

### リポジトリセットアップ

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Pythonサンプルセットアップ（Module08およびPythonサンプル）

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Node.jsサンプルセットアップ（サンプル08 - Windowsチャットアプリ）

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Localセットアップ

Module08のサンプルを実行するにはFoundry Localが必要です:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## 開発ワークフロー

### コンテンツ開発

このリポジトリは主に**Markdown教育コンテンツ**を含んでいます。変更を加える際には以下を行ってください:

1. 適切なモジュールディレクトリ内の`.md`ファイルを編集
2. 既存のフォーマットパターンに従う
3. コード例が正確でテスト済みであることを確認
4. 必要に応じて対応する翻訳コンテンツを更新（または自動化に任せる）

### サンプルアプリケーション開発

Pythonサンプル（サンプル01-07, 09-10）:
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electronサンプル（サンプル08）:
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### サンプルアプリケーションのテスト

Pythonサンプルには自動テストがありませんが、実行して検証できます:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electronサンプルにはテストインフラがあります:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## テスト手順

### コンテンツ検証

リポジトリは自動翻訳ワークフローを使用しています。翻訳に対する手動テストは不要です。

**コンテンツ変更の手動検証:**
1. `.md`ファイルをプレビューしてMarkdownレンダリングを確認
2. すべてのリンクが有効なターゲットを指していることを確認
3. ドキュメントに含まれるコードスニペットをテスト
4. 画像が正しく読み込まれることを確認

### サンプルアプリケーションのテスト

**Module08/samples/08（Electronアプリ）は包括的なテストを含む:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Pythonサンプルは手動でテストする必要があります:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## コードスタイルガイドライン

### Markdownコンテンツ

- 一貫した見出し階層を使用（タイトルには#、メインセクションには##、サブセクションには###）
- 言語指定付きのコードブロックを含める: ```python, ```bash, ```javascript
- テーブル、リスト、強調の既存のフォーマットに従う
- 読みやすい行を維持（約80-100文字を目指すが厳密ではない）
- 内部参照には相対リンクを使用

### Pythonコードスタイル

- PEP 8規約に従う
- 適切な場所で型ヒントを使用
- 関数やクラスにドックストリングを含める
- 意味のある変数名を使用
- 関数を焦点を絞り簡潔に保つ

### JavaScript/Node.jsコードスタイル

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**主要な規約:**
- サンプル08に提供されるESLint構成
- Prettierを使用したコードフォーマット
- モダンなES6+構文を使用
- コードベースの既存のパターンに従う

## プルリクエストガイドライン

### タイトル形式
```
[ModuleXX] Brief description of change
```
または
```
[Module08/samples/XX] Description for sample changes
```

### 提出前

**コンテンツ変更の場合:**
- 変更されたすべてのMarkdownファイルをプレビュー
- リンクと画像が機能することを確認
- タイポや文法エラーをチェック

**サンプルコード変更の場合（Module08/samples/08）:**
```bash
npm run lint
npm test
```

**Pythonサンプル変更の場合:**
- サンプルが正常に実行されることをテスト
- エラーハンドリングが機能することを確認
- Foundry Localとの互換性をチェック

### レビュープロセス

- 教育コンテンツの変更は正確性と明確性を確認
- コードサンプルは機能性をテスト
- 翻訳の更新はGitHub Actionsによって自動的に処理

## 翻訳システム

**重要:** このリポジトリはGitHub Actionsを使用した自動翻訳を採用しています。

- 翻訳は`/translations/`ディレクトリにあります（50以上の言語）
- `co-op-translator.yml`ワークフローによって自動化
- **翻訳ファイルを手動で編集しないでください** - 上書きされます
- ルートおよびモジュールディレクトリ内の英語ソースファイルのみ編集
- 翻訳は`main`ブランチへのプッシュ時に自動生成

## Foundry Local統合

Module08のほとんどのサンプルはMicrosoft Foundry Localが実行されている必要があります:

### Foundry Localの起動
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Foundry Localの確認
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### サンプル用環境変数

ほとんどのサンプルは以下の環境変数を使用します:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## ビルドとデプロイ

### コンテンツデプロイ

このリポジトリは主にドキュメントで構成されているため、コンテンツに対するビルドプロセスは不要です。

### サンプルアプリケーションのビルド

**Electronアプリケーション（Module08/samples/08）:**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Pythonサンプル:**
ビルドプロセスは不要 - サンプルはPythonインタープリターで直接実行されます。

## よくある問題とトラブルシューティング

### Foundry Localが実行されていない
**問題:** サンプルが接続エラーで失敗する

**解決策:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python仮想環境の問題
**問題:** モジュールインポートエラー

**解決策:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electronビルドの問題
**問題:** npm installまたはビルドの失敗

**解決策:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### 翻訳ワークフローの競合
**問題:** 翻訳PRが変更と競合する

**解決策:**
- 英語のソースファイルのみ編集
- 自動翻訳ワークフローに翻訳を任せる
- 競合が発生した場合、翻訳がマージされた後に`main`をブランチにマージ

## 追加リソース

### 学習パス
- **初心者向けパス:** モジュール01-02（7-9時間）
- **中級者向けパス:** モジュール03-04（9-11時間）
- **上級者向けパス:** モジュール05-07（12-15時間）
- **エキスパート向けパス:** モジュール08（8-10時間）

### 主要モジュールコンテンツ
- **Module01:** EdgeAIの基礎と実世界のケーススタディ
- **Module02:** 小型言語モデル（SLM）のファミリーとアーキテクチャ
- **Module03:** ローカルおよびクラウドデプロイメント戦略
- **Module04:** 複数のフレームワークを使用したモデル最適化
- **Module05:** SLMOps - 本番運用
- **Module06:** AIエージェントと機能呼び出し
- **Module07:** プラットフォーム固有の実装
- **Module08:** Foundry Localツールキットと10の包括的なサンプル

### 外部依存関係
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - ローカルAIモデルランタイム
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - 最適化フレームワーク
- [Microsoft Olive](https://microsoft.github.io/Olive/) - モデル最適化ツールキット
- [OpenVINO](https://docs.openvino.ai/) - Intelの最適化ツールキット

## プロジェクト固有の注意事項

### Module08サンプルアプリケーション

リポジトリには10の包括的なサンプルアプリケーションが含まれています:

1. **01-REST Chat Quickstart** - 基本的なOpenAI SDK統合
2. **02-OpenAI SDK Integration** - 高度なSDK機能
3. **03-Model Discovery & Benchmarking** - モデル比較ツール
4. **04-Chainlit RAG Application** - 検索強化生成
5. **05-Multi-Agent Orchestration** - 基本的なエージェント調整
6. **06-Models-as-Tools Router** - インテリジェントモデルルーティング
7. **07-Direct API Client** - 低レベルAPI統合
8. **08-Windows 11 Chat App** - ネイティブElectronデスクトップアプリケーション
9. **09-Advanced Multi-Agent System** - 複雑なエージェント調整
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel統合

各サンプルはFoundry Localを使用したEdge AI開発の異なる側面を示しています。

### パフォーマンスに関する考慮事項

- SLMはエッジデプロイメント向けに最適化（2-16GB RAM）
- ローカル推論は50-500msの応答時間を提供
- 量子化技術により75%のサイズ削減と85%の性能維持を実現
- ローカルモデルによるリアルタイム会話機能

### セキュリティとプライバシー

- すべての処理はローカルで行われ、クラウドにデータは送信されない
- プライバシーに敏感なアプリケーション（医療、金融）に適している
- データ主権要件を満たす
- Foundry Localは完全にローカルハードウェア上で動作

---

**このリポジトリはEdge AI開発を教えることに焦点を当てた教育リポジトリです。主な貢献パターンは教育コンテンツの改善と、Edge AIの概念を示すサンプルアプリケーションの追加/強化です。**

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。