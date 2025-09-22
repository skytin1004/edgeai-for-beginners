<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T12:20:59+00:00",
  "source_file": "Module08/README.md",
  "language_code": "ja"
}
-->
# モジュール 08: Microsoft Foundry Local を使った実践 - 完全な開発者ツールキット

## 概要

Microsoft Foundry Local は、エッジAI開発の次世代を担うプラットフォームであり、開発者がローカル環境でAIアプリケーションを構築、展開、スケールできる強力なツールを提供します。同時に、Azure AI Foundry とのシームレスな統合も可能です。このモジュールでは、Foundry Local のインストールから高度なエージェント開発までを包括的にカバーします。

**主要技術:**
- Microsoft Foundry Local CLI と SDK
- Azure AI Foundry との統合
- デバイス上でのモデル推論
- ローカルモデルのキャッシングと最適化
- エージェントベースのアーキテクチャ

## モジュール学習目標

このモジュールを完了することで、以下を習得できます:

- **Foundry Local のセットアップをマスター**: Windows 11 開発環境でのインストール、設定、最適化
- **多様なモデルの展開**: phi、qwen、deepseek、GPT-OSS-20B モデルを CLI コマンドでローカル実行
- **実用的なソリューションの構築**: 高度なプロンプトエンジニアリングとデータ統合を活用したAIアプリケーションの作成
- **オープンソースエコシステムの活用**: Hugging Face モデルやコミュニティ主導の追加機能の統合
- **AIアーキテクチャの比較**: LLM と SLM のトレードオフと展開戦略の理解
- **AIエージェントの開発**: Foundry Local のアーキテクチャとグラウンディング機能を活用したインテリジェントエージェントの構築
- **ツールとしてのモデルの実装**: エンタープライズアプリケーション向けのモジュール型でカスタマイズ可能なAIソリューションの作成

## セッション構成

### [1: Foundry Local の始め方](./01.FoundryLocalSetup.md)
**フォーカス**: インストール、CLI セットアップ、モデルキャッシング、ハードウェアアクセラレーション

**学べる内容:**
- Windows 11 での Foundry Local の完全インストール
- CLI の設定とコマンド構造
- 最適なパフォーマンスのためのモデルキャッシング戦略
- ハードウェアアクセラレーションの設定と最適化
- phi、qwen、deepseek、GPT-OSS-20B モデルの実践的な展開

**所要時間**: 2～3時間  
**前提条件**: Windows 11、基本的なコマンドライン知識

---

### [2: Azure AI Foundry を使ったAIソリューションの構築](./02.AzureAIFoundryIntegration.md)
**フォーカス**: 高度なプロンプトエンジニアリング、データ統合、実行可能なタスク

**学べる内容:**
- 高度なプロンプトエンジニアリング技術
- データ統合パターンとベストプラクティス
- Foundry Local を使った実行可能なAIタスクの構築
- シームレスな Azure AI Foundry 統合ワークフロー
- パフォーマンスの最適化とモニタリング

**所要時間**: 2～3時間  
**前提条件**: セッション1の完了、Azureアカウント（任意）

---

### [3: Foundry Local とオープンソースモデル](./03.OpenSourceModels.md)
**フォーカス**: Hugging Face の統合、モデル選択戦略、コミュニティ主導の追加機能

**学べる内容:**
- Foundry Local での Hugging Face モデル統合
- 独自モデル（BYOM）の戦略と実装
- Model Mondays シリーズの洞察とコミュニティ貢献
- カスタムモデルの展開と最適化
- コミュニティモデルの評価と選択基準

**所要時間**: 2～3時間  
**前提条件**: セッション1～2の完了、Hugging Face アカウント

---

### [4: 最先端モデルの探求 - LLM、SLM、オンデバイス推論](./04.CuttingEdgeModels.md)
**フォーカス**: モデル比較、Phi と ONNX Runtime を使った EdgeAI、高度なデモ

**学べる内容:**
- LLM と SLM の包括的な比較とユースケース
- ローカル推論とクラウド推論のトレードオフと意思決定フレームワーク
- Phi と ONNX Runtime を使った EdgeAI の実装
- Chainlit RAG チャットアプリの開発と展開
- WebGPU 推論の最適化技術
- AI PC SDK の統合と機能

**所要時間**: 3～4時間  
**前提条件**: セッション1～3の完了、推論概念の理解

---

### [5: Foundry Local を使ったAIエージェントの迅速な構築](./05.AIPoweredAgents.md)
**フォーカス**: 高速な GenAI アプリ開発、システムプロンプト、グラウンディング、エージェントアーキテクチャ

**学べる内容:**
- Foundry Local のエージェントアーキテクチャと設計パターン
- エージェントの挙動を制御するシステムプロンプトエンジニアリング
- 信頼性の高いエージェント応答のためのグラウンディング技術
- 高速な GenAI アプリケーション開発ワークフロー
- エージェントのオーケストレーションとマルチエージェントシステム
- AIエージェントの本番展開戦略

**所要時間**: 3～4時間  
**前提条件**: セッション1～4の完了、AIエージェントの基本的な理解

---

### [6: Foundry Local - ツールとしてのモデル](./06.ModelsAsTools.md)
**フォーカス**: モジュール型AIソリューション、オンデバイス展開、エンタープライズスケーリング

**学べる内容:**
- AIモデルをモジュール型でカスタマイズ可能なツールとして扱う方法
- クラウド依存なしのオンデバイス展開
- 低遅延、コスト効率、プライバシー保護を実現する推論
- SDK、API、CLI の統合パターン
- 特定のユースケースに合わせたモデルのカスタマイズ
- ローカルから Azure AI Foundry へのスケーリング戦略
- エンタープライズ対応のAIアプリケーションアーキテクチャ

**所要時間**: 3～4時間  
**前提条件**: すべての前セッションの完了、エンタープライズ開発経験があると望ましい

## 前提条件

### システム要件
- **オペレーティングシステム**: Windows 11 (22H2以降)
- **メモリ**: 16GB RAM（大規模モデルには32GB推奨）
- **ストレージ**: モデルキャッシング用に50GBの空き容量
- **ハードウェア**: NPU対応デバイス推奨（Copilot+ PC）、GPUは任意
- **ネットワーク**: 初回モデルダウンロード用の高速インターネット

### 開発環境
- Visual Studio Code（AI Toolkit 拡張機能付き）
- Python 3.10+ と pip
- Git（バージョン管理用）
- PowerShell またはコマンドプロンプト
- Azure CLI（クラウド統合用、任意）

### 知識要件
- AI/ML 概念の基本的な理解
- コマンドラインの基本的な操作
- Python プログラミングの基礎
- REST API の概念
- プロンプトとモデル推論の基本知識

## モジュールタイムライン

**総所要時間**: 15～20時間

| セッション | フォーカスエリア | 時間 | 難易度 |
|------------|------------------|------|--------|
|  1 | セットアップと基礎 | 2～3時間 | 初級 |
|  2 | AIソリューション | 2～3時間 | 中級 |
|  3 | オープンソース | 2～3時間 | 中級 |
|  4 | 高度なモデル | 3～4時間 | 上級 |
|  5 | AIエージェント | 3～4時間 | 上級 |
|  6 | エンタープライズツール | 3～4時間 | エキスパート |

## 主要リソース

### 主要ドキュメント
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local ドキュメント](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays シリーズ](https://aka.ms/model-mondays)

### コミュニティリソース
- [Foundry Local コミュニティディスカッション](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry サンプル](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI 開発者コミュニティ](https://techcommunity.microsoft.com/category/artificialintelligence)

## 学習成果

このモジュールを完了すると、以下のスキルを習得できます:

### 技術的スキル
- **展開と管理**: 開発および本番環境での Foundry Local のインストールと管理
- **モデル統合**: Microsoft、Hugging Face、コミュニティソースの多様なモデルファミリーとのシームレスな連携
- **アプリケーション構築**: 高度な機能と最適化を備えた本番対応のAIアプリケーションの作成
- **エージェント開発**: グラウンディング、推論、ツール統合を備えた高度なAIエージェントの実装

### 戦略的理解
- **アーキテクチャの選択**: ローカル展開とクラウド展開の間での適切な選択
- **パフォーマンス最適化**: 異なるハードウェア構成での推論パフォーマンスの最適化
- **エンタープライズスケーリング**: ローカルプロトタイプからエンタープライズ展開までスケール可能なアプリケーションの設計
- **プライバシーとセキュリティ**: ローカル推論を活用したプライバシー保護型AIソリューションの実装

### イノベーション能力
- **迅速なプロトタイピング**: AIアプリケーションコンセプトの迅速な構築とテスト
- **コミュニティ統合**: オープンソースモデルの活用とエコシステムへの貢献
- **高度なパターン**: RAG、エージェント、ツール統合を含む最先端のAIパターンの実装
- **未来志向の開発**: 新たなAI技術やパターンに対応可能なアプリケーションの構築

## 始め方

1. **環境を準備**: 推奨ハードウェア仕様を備えた Windows 11 を用意
2. **前提条件をインストール**: 開発ツールと依存関係をセットアップ
3. **セッション1から開始**: Foundry Local のインストールと基本設定から始める
4. **順序通りに進める**: 最適な学習進行のためにセッションを順番に完了
5. **継続的に練習**: 実践的な演習やプロジェクトを通じて概念を適用

## 成功指標

モジュールの進捗を以下で追跡:

- [ ] Foundry Local のインストールと設定を成功させる
- [ ] 少なくとも4つの異なるモデルファミリーを展開して実行
- [ ] データ統合を含む完全なAIソリューションを構築
- [ ] 少なくとも2つのオープンソースモデルを統合
- [ ] 機能的なRAGチャットアプリケーションを作成
- [ ] AIエージェントを開発して展開
- [ ] モデルをツールとして活用するアーキテクチャを実装

## サンプルのクイックスタート

### 1) 環境セットアップ (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) ローカルモデルの起動 (新しいターミナル)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Chainlit デモの実行 (セッション4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) マルチエージェントコーディネーターの実行 (セッション5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

接続エラーが発生した場合、Foundry Local を検証:
```cmd
curl http://localhost:8000/v1/models
```

### ルーター設定 (セッション6)
ルーターはクイックヘルスチェックを実行し、環境ベースの設定をサポート:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

このモジュールは、Microsoft のエンタープライズグレードのツールとオープンソースエコシステムの柔軟性と革新性を組み合わせた、エッジAI開発の最前線を表しています。Foundry Local をマスターすることで、AIアプリケーション開発の最前線に立つことができます。

Azure OpenAI (セッション2) に関しては、必要な環境変数とAPIバージョン設定についてサンプルREADMEを参照してください。

## サンプル概要

- `samples/01`: Foundry Local へのクイックRESTチャット (`chat_quickstart.py`)。
- `samples/02`: OpenAI SDK 統合 (`sdk_quickstart.py`)。
- `samples/03`: モデル探索 + クイックベンチ (`list_and_bench.cmd`)。
- `samples/04`: Chainlit RAG デモ (`app.py`)。
- `samples/05`: マルチエージェントオーケストレーション (`python -m samples.05.agents.coordinator`)。
- `samples/06`: ツールとしてのモデルルーター (`python samples\06\router.py`)。

---

