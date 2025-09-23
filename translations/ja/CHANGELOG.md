<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T12:20:01+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ja"
}
-->
# 変更履歴

EdgeAI for Beginners のすべての重要な変更はここに記録されています。このプロジェクトでは、日付ベースのエントリと Keep a Changelog スタイル（追加、変更、修正、削除、ドキュメント、移動）を使用しています。

## 2025-09-18

### 追加
- モジュール 08: Microsoft Foundry Local – 完全な開発者ツールキット
  - 6つのセッション: セットアップ、Azure AI Foundry 統合、オープンソースモデル、最先端デモ、エージェント、モデルをツールとして活用
  - `Module08/samples/01`–`06` に実行可能なサンプルを追加（Windows cmd の指示付き）
    - `01` REST クイックチャット (`chat_quickstart.py`)
    - `02` OpenAI/Foundry Local および Azure OpenAI サポートを含む SDK クイックスタート (`sdk_quickstart.py`)
    - `03` CLI リスト＆ベンチ (`list_and_bench.cmd`)
    - `04` Chainlit デモ (`app.py`)
    - `05` マルチエージェントオーケストレーション (`python -m samples.05.agents.coordinator`)
    - `06` モデルをツールとして活用するルーター (`router.py`)
- セッション 2 SDK サンプルに Azure OpenAI サポートを追加（環境変数設定による）
- `.vscode/settings.json` を `Module08/.venv` にポイントし、Python 分析解決を改善
- `.env` に VS Code/Pylance の認識向上のための `PYTHONPATH` ヒントを追加

### 変更
- モジュール 08 のドキュメントとサンプル全体でデフォルトモデルを `phi-4-mini` に更新；モジュール 08 内の `phi-3.5` の記載を削除
- ルーター (`Module08/samples/06/router.py`) の改善:
  - `foundry service status` を使用した正規表現解析によるエンドポイント検出
  - 起動時の `/v1/models` ヘルスチェック
  - 環境変数で設定可能なモデルレジストリ (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- 必要条件を更新: `Module08/requirements.txt` に `openai` を追加（`requests`, `chainlit` と共に）
- Chainlit サンプルのガイダンスを明確化し、トラブルシューティングを追加；ワークスペース設定によるインポート解決を強化

### 修正
- インポートの問題を解決:
  - ルーターが存在しない `utils` モジュールに依存しなくなり、関数をインライン化
  - コーディネーターが相対インポートを使用するように修正 (`from .specialists import ...`)、モジュールパス経由で呼び出し
  - VS Code/Pylance 設定で `chainlit` およびパッケージインポートを解決
- `STUDY_GUIDE.md` の軽微なタイプミスを修正し、モジュール 08 の内容を追加

### 削除
- 未使用の `Module08/infra/obs.py` を削除し、空の `infra/` ディレクトリを削除；オプションとしてドキュメントに観測パターンを保持

### 移動
- モジュール 08 のデモを `Module08/samples` に統合し、セッション番号付きフォルダーに移動
  - Chainlit アプリを `samples/04` に移動
  - エージェントを `samples/05` に移動し、パッケージ解決のために `__init__.py` ファイルを追加

### ドキュメント
- モジュール 08 のセッションドキュメントとすべてのサンプル README を Microsoft Learn および信頼できるベンダーの参照情報で充実化
- `Module08/README.md` を更新し、サンプル概要、ルーター設定、検証のヒントを追加
- `Module07/README.md` の Windows Foundry Local セクションを Learn ドキュメントに基づいて検証
- `STUDY_GUIDE.md` を更新:
  - モジュール 08 を概要、スケジュール、進捗トラッカーに追加
  - 包括的な参照セクションを追加（Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML）

---

## 過去の履歴（概要）
- コース構成とモジュールの確立（モジュール 01–07）
- コンテンツの段階的な最新化、フォーマットの標準化、ケーススタディの追加
- 最適化フレームワークのカバレッジ拡大（Llama.cpp, Olive, OpenVINO, Apple MLX）

## 未リリース / バックログ（提案）
- Foundry Local の利用可能性を検証するためのオプションのサンプルごとのスモークテスト
- モデル参照（例: `phi-4-mini`）を整合させるための翻訳レビュー
- チームがワークスペース全体で厳密性を好む場合の最小限の pyright 設定の追加

---

