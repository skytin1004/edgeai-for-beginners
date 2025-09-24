<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T10:27:29+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ja"
}
-->
# Changelog

EdgeAI for Beginnersのすべての重要な変更はここに記録されています。このプロジェクトは日付ベースのエントリーとKeep a Changelogスタイル（Added, Changed, Fixed, Removed, Docs, Moved）を使用しています。

## 2025-09-23

### Changed - モジュール08の大規模なモダナイゼーション
- **Microsoft Foundry-Localリポジトリパターンとの包括的な整合性**
  - すべてのコード例を最新の`FoundryLocalManager`とOpenAI SDK統合を使用するよう更新
  - 非推奨の手動`requests`呼び出しを適切なSDK使用に置き換え
  - 実装パターンを公式Microsoftドキュメントとサンプルに整合

- **05.AIPoweredAgents.mdのモダナイゼーション**:
  - 最新のSDKパターンを使用したマルチエージェントオーケストレーションを更新
  - 高度な機能（フィードバックループ、パフォーマンスモニタリング）を備えたコーディネーター実装を強化
  - 包括的なエラーハンドリングとサービスの健全性チェックを追加
  - ローカルサンプルへの適切な参照を統合（`samples/05/multi_agent_orchestration.ipynb`）
  - 非推奨の`functions`ではなく最新の`tools`パラメータを使用した関数呼び出し例を更新
  - モニタリングと統計追跡を備えた本番対応パターンを追加

- **06.ModelsAsTools.mdの完全な書き直し**:
  - 基本的なツールレジストリをインテリジェントなモデルルーター実装に置き換え
  - 異なるタスクタイプ（一般、推論、コード、クリエイティブ）に基づくキーワード選択を追加
  - 柔軟なモデル割り当てを可能にする環境ベースの設定を統合
  - 包括的なサービス健全性モニタリングとエラーハンドリングを強化
  - リクエストモニタリングとパフォーマンス追跡を備えた本番展開パターンを追加
  - ローカル実装に整合（`samples/06/router.py`および`samples/06/model_router.ipynb`）

- **ドキュメント構造の改善**:
  - モダナイゼーションとSDK整合性を強調する概要セクションを追加
  - 読みやすさを向上させるために絵文字とフォーマットを強化
  - ドキュメント全体でローカルサンプルファイルへの適切な参照を追加
  - 本番対応の実装ガイダンスとベストプラクティスを含む

### Added
- モジュール08ファイルにおける最新SDK統合を強調する包括的な概要セクション
- 高度な機能（マルチエージェントシステム、インテリジェントルーティング）を示すアーキテクチャのハイライト
- 実践的な経験のためのローカルサンプル実装への直接参照
- モニタリングとエラーハンドリングパターンを備えた本番展開ガイダンス
- 高度な機能とベンチマークを備えたインタラクティブなJupyterノートブック例

### Fixed
- ドキュメントと実際のサンプル実装間の整合性の不一致
- モジュール08全体での古いSDK使用パターン
- 包括的なローカルサンプルライブラリへの参照不足
- 異なるセクション間での実装アプローチの不一致

---

## 2025-09-18

### Added
- モジュール08: Microsoft Foundry Local – 完全な開発者ツールキット
  - 6つのセッション: セットアップ、Azure AI Foundry統合、オープンソースモデル、最先端デモ、エージェント、モデルをツールとして活用
  - `Module08/samples/01`–`06`に実行可能なサンプルを追加（Windows cmd指示付き）
    - `01` RESTクイックチャット（`chat_quickstart.py`）
    - `02` SDKクイックスタート（OpenAI/Foundry LocalおよびAzure OpenAI対応）（`sdk_quickstart.py`）
    - `03` CLIリストとベンチ（`list_and_bench.cmd`）
    - `04` Chainlitデモ（`app.py`）
    - `05` マルチエージェントオーケストレーション（`python -m samples.05.agents.coordinator`）
    - `06` モデルをツールとして活用するルーター（`router.py`）
- セッション2 SDKサンプルにAzure OpenAI対応を追加（環境変数設定付き）
- `.vscode/settings.json`を`Module08/.venv`にポイントし、Python解析解決を改善
- `.env`に`PYTHONPATH`ヒントを追加し、VS Code/Pylanceの認識を向上

### Changed
- モジュール08のドキュメントとサンプル全体でデフォルトモデルを`phi-4-mini`に更新；モジュール08内の残りの`phi-3.5`言及を削除
- ルーター（`Module08/samples/06/router.py`）の改善:
  - 正規表現解析を使用した`foundry service status`によるエンドポイント検出
  - 起動時の`/v1/models`健全性チェック
  - 環境設定可能なモデルレジストリ（`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON）
- 要件を更新: `Module08/requirements.txt`に`openai`を追加（`requests`, `chainlit`とともに）
- Chainlitサンプルガイダンスを明確化し、トラブルシューティングを追加；ワークスペース設定によるインポート解決

### Fixed
- インポート問題を解決:
  - ルーターが存在しない`utils`モジュールに依存しなくなり、関数がインライン化
  - コーディネーターが相対インポート（`from .specialists import ...`）を使用し、モジュールパス経由で呼び出される
  - VS Code/Pylance設定で`chainlit`とパッケージインポートを解決
- `STUDY_GUIDE.md`の軽微な誤字を修正し、モジュール08のカバレッジを追加

### Removed
- 未使用の`Module08/infra/obs.py`を削除し、空の`infra/`ディレクトリを削除；観測パターンはドキュメント内でオプションとして保持

### Moved
- モジュール08のデモを`Module08/samples`内のセッション番号付きフォルダに統合
  - Chainlitアプリを`samples/04`に移動
  - エージェントを`samples/05`に移動し、パッケージ解決のために`__init__.py`ファイルを追加

### Docs
- モジュール08セッションドキュメントとすべてのサンプルREADMEをMicrosoft Learnおよび信頼できるベンダー参照で充実化
- `Module08/README.md`をサンプル概要、ルーター設定、検証のヒントで更新
- `Module07/README.md`のWindows Foundry LocalセクションをLearnドキュメントに基づいて検証
- `STUDY_GUIDE.md`を更新:
  - 概要、スケジュール、進捗トラッカーにモジュール08を追加
  - 包括的な参照セクションを追加（Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML）

---

## Historical (summary)
- コースアーキテクチャとモジュール（モジュール01–07）を確立
- コンテンツの逐次モダナイゼーション、フォーマット標準化、ケーススタディの追加
- 最適化フレームワークのカバレッジ拡大（Llama.cpp, Olive, OpenVINO, Apple MLX）

## Unreleased / Backlog (proposals)
- Foundry Localの利用可能性を検証するためのオプションのサンプルごとのスモークテスト
- モデル参照（例: `phi-4-mini`）を適切に整合させるための翻訳レビュー
- チームがワークスペース全体で厳密性を好む場合の最小限のpyright設定を追加

---

