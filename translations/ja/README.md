<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e73444e4fc8f1931ac3979dbd7785e2",
  "translation_date": "2025-09-15T16:54:19+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# 初心者向けEdgeAI

![コース表紙画像](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ja.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)  
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)  
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)  
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)  

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

以下の手順でリソースを利用開始してください：

1. **リポジトリをフォークする**: [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork) をクリック  
2. **リポジトリをクローンする**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**Azure AI Foundry Discordに参加して、専門家や開発者と交流する**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 多言語対応

#### GitHub Actionによるサポート (自動更新・常に最新)

[フランス語](../fr/README.md) | [スペイン語](../es/README.md) | [中国語 (簡体字)](../zh/README.md) | [中国語 (繁体字, マカオ)](../mo/README.md) | [中国語 (繁体字, 香港)](../hk/README.md) | [中国語 (繁体字, 台湾)](../tw/README.md) | [日本語](./README.md) | [韓国語](../ko/README.md)  
**追加の翻訳言語を希望する場合は、[こちら](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)に記載されています**

## はじめに

**EdgeAI for Beginners**へようこそ！このコースは、エッジ人工知能の変革的な世界への包括的な旅を提供します。強力なAI機能とエッジデバイスでの実際の展開を結びつけ、データが生成され、意思決定が必要な場所でAIの可能性を活用できるようにします。

### 学べる内容

このコースでは、基本的な概念から実際の運用準備までをカバーします：
- **エッジ展開に最適化された小型言語モデル (SLM)**
- **多様なプラットフォームにおけるハードウェア対応の最適化**
- **プライバシーを保護するリアルタイム推論**
- **企業向けアプリケーションの運用展開戦略**

### EdgeAIが重要な理由

EdgeAIは、現代の重要な課題に対応するパラダイムシフトを表しています：
- **プライバシーとセキュリティ**: 機密データをクラウドに送信せずにローカルで処理
- **リアルタイム性能**: 時間が重要なアプリケーションでネットワーク遅延を排除
- **コスト効率**: 帯域幅とクラウドコンピューティングの費用を削減
- **耐障害性**: ネットワーク障害時でも機能を維持
- **規制遵守**: データ主権要件を満たす

### EdgeAIとは

EdgeAIは、AIアルゴリズムや言語モデルをローカルのハードウェア上で実行し、データが生成される場所の近くで推論を行うことを指します。これにより、遅延が減少し、プライバシーが向上し、リアルタイムの意思決定が可能になります。

### コア原則:
- **デバイス上での推論**: AIモデルがエッジデバイス（スマートフォン、ルーター、マイクロコントローラー、産業用PC）で実行される
- **オフライン機能**: 常時インターネット接続なしで動作
- **低遅延**: リアルタイムシステムに適した即時応答
- **データ主権**: 機密データをローカルに保持し、セキュリティとコンプライアンスを向上

### 小型言語モデル (SLM)

Phi-4、Mistral-7B、GemmaのようなSLMは、大型LLMの最適化バージョンであり、以下の目的でトレーニングまたは蒸留されています：
- **メモリ使用量の削減**: エッジデバイスの限られたメモリを効率的に利用
- **計算負荷の軽減**: CPUやエッジGPU性能に最適化
- **起動時間の短縮**: 応答性の高いアプリケーションのための迅速な初期化

これらは以下の制約を満たしながら強力なNLP機能を提供します：
- **組み込みシステム**: IoTデバイスや産業用コントローラー
- **モバイルデバイス**: オフライン機能を備えたスマートフォンやタブレット
- **IoTデバイス**: リソースが限られたセンサーやスマートデバイス
- **エッジサーバー**: 限られたGPUリソースを持つローカル処理ユニット
- **パーソナルコンピュータ**: デスクトップやラップトップでの展開シナリオ

## コース構成

### [モジュール01: EdgeAIの基礎と変革](./Module01/README.md)
**テーマ**: EdgeAI展開の変革的なシフト

#### チャプター構成:
- [**セクション1: EdgeAIの基礎**](./Module01/01.EdgeAIFundamentals.md)
  - 従来のクラウドAIとEdgeAIの比較
  - エッジコンピューティングの課題と制約
  - 主要技術: モデル量子化、圧縮最適化、小型言語モデル (SLM)
  - ハードウェアアクセラレーション: NPU、GPU最適化、CPU最適化
  - 利点: プライバシーセキュリティ、低遅延、オフライン機能、コスト効率

- [**セクション2: 実世界のケーススタディ**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi & Muモデルエコシステム
  - 日本航空のAI報告システムのケーススタディ
  - 市場への影響と将来の方向性
  - 展開の考慮事項とベストプラクティス

- [**セクション3: 実践的な実装ガイド**](./Module01/03.PracticalImplementationGuide.md)
  - 開発環境のセットアップ (Python 3.10+、.NET 8+)
  - ハードウェア要件と推奨構成
  - コアモデルファミリーリソース
  - 量子化と最適化ツール (Llama.cpp、Microsoft Olive、Apple MLX)
  - 評価と検証チェックリスト

- [**セクション4: EdgeAI展開ハードウェアプラットフォーム**](./Module01/04.EdgeDeployment.md)
  - EdgeAI展開の考慮事項と要件
  - Intel EdgeAIハードウェアと最適化技術
  - モバイルおよび組み込みシステム向けQualcomm AIソリューション
  - NVIDIA Jetsonとエッジコンピューティングプラットフォーム
  - NPUアクセラレーションを備えたWindows AI PCプラットフォーム
  - ハードウェア固有の最適化戦略

---

### [モジュール02: 小型言語モデルの基礎](./Module02/README.md)
**テーマ**: SLMの理論的原則、実装戦略、運用展開

#### チャプター構成:
- [**セクション1: Microsoft Phiモデルファミリーの基礎**](./Module02/01.PhiFamily.md)
  - デザイン哲学の進化 (Phi-1からPhi-4)
  - 効率重視のアーキテクチャ設計
  - 特化した機能 (推論、マルチモーダル、エッジ展開)

- [**セクション2: Qwenファミリーの基礎**](./Module02/02.QwenFamily.md)
  - オープンソースの卓越性 (Qwen 1.0からQwen3) - Hugging Faceで利用可能
  - 思考モード機能を備えた高度な推論アーキテクチャ
  - スケーラブルな展開オプション (0.5B-235Bパラメータ)

- [**セクション3: Gemmaファミリーの基礎**](./Module02/03.GemmaFamily.md)
  - 研究主導の革新 (Gemma 3 & 3n)
  - マルチモーダルの卓越性
  - モバイル優先のアーキテクチャ

- [**セクション4: BitNETファミリーの基礎**](./Module02/04.BitNETFamily.md)
  - 革新的な量子化技術 (1.58ビット)
  - https://github.com/microsoft/BitNet で提供される特化した推論フレームワーク
  - 極限効率による持続可能なAIリーダーシップ

- [**セクション5: Microsoft Muモデルの基礎**](./Module02/05.mumodel.md)
  - Windows 11に組み込まれたデバイス優先のアーキテクチャ
  - Windows 11設定とのシステム統合
  - プライバシーを保護するオフライン操作

- [**セクション6: Phi-Silicaの基礎**](./Module02/06.phisilica.md)
  - Windows 11 Copilot+ PCに組み込まれたNPU最適化アーキテクチャ
  - 卓越した効率性 (650トークン/秒、1.5W)
  - Windows App SDKとの開発者統合

---

### [モジュール03: 小型言語モデルの展開](./Module03/README.md)
**テーマ**: 理論から運用環境までのSLMライフサイクル展開

#### チャプター構成:
- [**セクション1: SLM高度学習**](./Module03/01.SLMAdvancedLearning.md)
  - パラメータ分類フレームワーク (Micro SLM 100M-1.4B、Medium SLM 14B-30B)
  - 高度な最適化技術 (量子化手法、BitNET 1ビット量子化)
  - モデル取得戦略 (PhiモデルのAzure AI Foundry、選択モデルのHugging Face)

- [**セクション2: ローカル環境での展開**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollamaユニバーサルプラットフォーム展開
  - Microsoft Foundryローカル企業向けソリューション
  - フレームワーク比較分析

- [**セクション3: コンテナ化されたクラウド展開**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM高性能推論展開
  - Ollamaコンテナオーケストレーション
  - ONNX Runtimeエッジ最適化実装

---

### [モジュール04: モデル形式変換と量子化](./Module04/README.md)
**テーマ**: プラットフォームを超えたエッジ展開のための完全なモデル最適化ツールキット

#### チャプター構成:
- [**セクション1: モデル形式変換と量子化の基礎**](./Module04/01.Introduce.md)
  - 精度分類フレームワーク (超低、低、中精度)
  - GGUFとONNX形式の利点と使用例
  - 運用効率向上のための量子化の利点
  - パフォーマンスベンチマークとメモリ使用量比較

- [**セクション2: Llama.cpp実装ガイド**](./Module04/02.Llamacpp.md)
  - クロスプラットフォームインストール (Windows、macOS、Linux)
  - GGUF形式変換と量子化レベル (Q2_KからQ8_0)
  - ハードウェアアクセラレーション (CUDA、Metal、OpenCL、Vulkan)
  - Python統合とREST API展開

- [**セクション3: Microsoft Olive最適化スイート**](./Module04/03.MicrosoftOlive.md)
  - 40以上の組み込みコンポーネントによるハードウェア対応モデル最適化
  - 動的および静的量子化による自動最適化
  - Azure MLワークフローとの企業統合
  - 人気モデルのサポート (Llama、Phi、選択されたQwenモデル、Gemma)

- [**セクション4: OpenVINO Toolkit最適化スイート**](./Module04/04.openvino.md)
  - クロスプラットフォームAI展開のためのIntelのオープンソースツールキット
  - 高度な最適化のためのニューラルネットワーク圧縮フレームワーク (NNCF)
  - 大型言語モデル展開のためのOpenVINO GenAI
  - CPU、GPU、VPU、AIアクセラレータを活用したハードウェアアクセラレーション

- [**セクション5: Apple MLXフレームワークの詳細**](./Module04/05.AppleMLX.md)
  - Apple Siliconの統一メモリアーキテクチャ
  - LLaMA、Mistral、Phi-3、選択されたQwenモデルのサポート
  - LoRA微調整とモデルカスタマイズ
  - 4ビット/8ビット量子化によるHugging Face統合

- [**セクション6: EdgeAI開発ワークフローの統合**](./Module04/06.workflow-synthesis.md)
  - 複数の最適化フレームワークを統合した統一ワークフローアーキテクチャ
  - フレームワーク選択の意思決定ツリーとパフォーマンスのトレードオフ分析
  - 運用準備の検証と包括的な展開戦略
  - 新しいハードウェアとモデルアーキテクチャに対応する将来性のある戦略

---

### [モジュール05: SLMOps - 小型言語モデル運用](./Module05/README.md)
**テーマ**: 蒸留から運用展開までのSLMライフサイクル運用

#### チャプター構成:
- [**セクション1: SLMOpsの紹介**](./Module05/01.IntroduceSLMOps.md)
  - SLMOpsによるAI運用のパラダイムシフト
  - コスト効率とプライバシー重視のアーキテクチャ
  - 戦略的なビジネスインパクトと競争優位性
  - 実世界での実装課題と解決策
- [**セクション2: モデル蒸留 - 理論から実践へ**](./Module05/02.SLMOps-Distillation.md)
  - 教師モデルから生徒モデルへの知識移転
  - 2段階の蒸留プロセスの実装
  - 実践例を用いたAzure ML蒸留ワークフロー
  - 推論時間を85%削減し、92%の精度を維持

- [**セクション3: ファインチューニング - 特定のタスク向けモデルのカスタマイズ**](./Module05/03.SLMOps-Finetuing.md)
  - パラメータ効率の良いファインチューニング（PEFT）技術
  - LoRAおよびQLoRAの高度な手法
  - Microsoft Oliveによるファインチューニングの実装
  - マルチアダプタートレーニングとハイパーパラメータの最適化

- [**セクション4: デプロイメント - 実運用向けの実装**](./Module05/04.SLMOps.Deployment.md)
  - 実運用向けのモデル変換と量子化
  - Foundry Localのデプロイメント設定
  - パフォーマンスベンチマークと品質検証
  - サイズを75%削減し、運用監視を実施

---

### [モジュール06: SLMエージェントシステム - AIエージェントと関数呼び出し](./Module06/README.md)
**テーマ**: 基礎から高度な関数呼び出しおよびモデルコンテキストプロトコル統合までのSLMエージェントシステムの実装

#### チャプター構成:
- [**セクション1: AIエージェントと小型言語モデルの基礎**](./Module06/01.IntroduceAgent.md)
  - エージェント分類フレームワーク（反射型、モデルベース型、目標ベース型、学習型エージェント）
  - SLMの基礎と最適化戦略（GGUF、量子化、エッジフレームワーク）
  - SLMとLLMのトレードオフ分析（10-30倍のコスト削減、70-80%のタスク効率）
  - Ollama、VLLM、Microsoftエッジソリューションを用いた実践的デプロイメント

- [**セクション2: 小型言語モデルにおける関数呼び出し**](./Module06/02.FunctionCalling.md)
  - システマティックなワークフローの実装（意図検出、JSON出力、外部実行）
  - プラットフォーム固有の実装（Phi-4-mini、選択されたQwenモデル、Microsoft Foundry Local）
  - 高度な例（マルチエージェント協力、動的ツール選択）
  - 実運用の考慮事項（レート制限、監査ログ、セキュリティ対策）

- [**セクション3: モデルコンテキストプロトコル（MCP）の統合**](./Module06/03.IntroduceMCP.md)
  - プロトコルアーキテクチャと階層型システム設計
  - マルチバックエンドサポート（開発用Ollama、運用用vLLM）
  - 接続プロトコル（STDIOおよびSSEモード）
  - 実世界のアプリケーション（ウェブ自動化、データ処理、API統合）

---

### [モジュール07: EdgeAI実装サンプル](./Module07/README.md)
**テーマ**: 多様なプラットフォームとフレームワークにわたる包括的なEdgeAI実装

#### チャプター構成:
- [**Visual Studio Code向けAIツールキット**](./Module07/aitoolkit.md)
  - VS Code内での包括的なEdge AI開発環境
  - エッジデプロイメント向けモデルカタログと探索
  - ローカルテスト、最適化、エージェント開発ワークフロー
  - エッジシナリオ向けのパフォーマンス監視と評価

- [**Windows EdgeAI開発ガイド**](./Module07/windowdeveloper.md)
  - Windows AI Foundryプラットフォームの包括的概要
  - 効率的なNPU推論のためのPhi Silica API
  - 画像処理とOCR向けのコンピュータビジョンAPI
  - ローカル開発とテストのためのFoundry Local CLI

- [**NVIDIA Jetson Orin NanoでのEdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - クレジットカードサイズのフォームファクターで67 TOPSのAI性能
  - ジェネレーティブAIモデルのサポート（ビジョントランスフォーマー、LLM、ビジョン言語モデル）
  - ロボティクス、ドローン、インテリジェントカメラ、自律デバイスでの応用
  - AI開発を民主化する手頃な価格の$249プラットフォーム

- [**.NET MAUIとONNX Runtime GenAIを用いたモバイルアプリケーションでのEdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 単一のC#コードベースによるクロスプラットフォームモバイルAI
  - ハードウェアアクセラレーションのサポート（CPU、GPU、モバイルAIプロセッサ）
  - プラットフォーム固有の最適化（iOS向けCoreML、Android向けNNAPI）
  - 完全なジェネレーティブAIループの実装

- [**Azureでの小型言語モデルエンジンを用いたEdgeAI**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - クラウドとエッジのハイブリッドデプロイメントアーキテクチャ
  - ONNX Runtimeを用いたAzure AIサービス統合
  - エンタープライズ規模のデプロイメントと継続的なモデル管理
  - インテリジェントな文書処理のためのハイブリッドAIワークフロー

- [**Windows MLを用いたEdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - 高性能なオンデバイス推論のためのWindows AI Foundry基盤
  - AMD、Intel、NVIDIA、Qualcommシリコンを含むユニバーサルハードウェアサポート
  - 自動ハードウェア抽象化と最適化
  - 多様なWindowsハードウェアエコシステム向けの統一フレームワーク

- [**Foundry Localアプリケーションを用いたEdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - ローカルリソースを用いたプライバシー重視のRAG実装
  - セマンティック検索を伴うPhi-3言語モデル統合（Phiモデルのみ）
  - ローカルベクトルデータベースのサポート（SQLite、Qdrant）
  - データ主権とオフライン操作機能

## コース学習目標

この包括的なEdgeAIコースを修了することで、実運用可能なEdgeAIソリューションを設計、実装、デプロイする専門知識を習得できます。構造化されたアプローチにより、理論的基盤と実践的な実装スキルの両方を習得できます。

### 技術的能力

**基礎知識**
- クラウドベースとエッジベースのAIアーキテクチャの基本的な違いを理解する
- リソース制約環境向けのモデル量子化、圧縮、最適化の原則を習得する
- ハードウェアアクセラレーションオプション（NPU、GPU、CPU）とそのデプロイメントへの影響を理解する

**実装スキル**
- 小型言語モデルを多様なエッジプラットフォーム（モバイル、組み込み、IoT、エッジサーバー）にデプロイする
- Llama.cpp、Microsoft Olive、ONNX Runtime、Apple MLXを含む最適化フレームワークを適用する
- サブセカンド応答要件を持つリアルタイム推論システムを実装する

**運用専門知識**
- エンタープライズアプリケーション向けのスケーラブルなEdgeAIアーキテクチャを設計する
- デプロイされたシステムの監視、保守、更新戦略を実装する
- プライバシー保護型EdgeAI実装のためのセキュリティベストプラクティスを適用する

### 戦略的能力

**意思決定フレームワーク**
- EdgeAIの機会を評価し、ビジネスアプリケーションに適したユースケースを特定する
- モデル精度、推論速度、電力消費、ハードウェアコストのトレードオフを評価する
- 特定のデプロイメント制約に基づいて適切なSLMファミリーと構成を選択する

**システムアーキテクチャ**
- 既存のインフラストラクチャと統合するエンドツーエンドのEdgeAIソリューションを設計する
- 最適なパフォーマンスとコスト効率のためのハイブリッドエッジクラウドアーキテクチャを計画する
- リアルタイムAIアプリケーション向けのデータフローと処理パイプラインを実装する

### 業界応用

**実践的なデプロイメントシナリオ**
- **製造業**: 品質管理システム、予知保全、プロセス最適化
- **医療**: プライバシー保護型診断ツールと患者モニタリングシステム
- **交通**: 自律車両の意思決定と交通管理
- **スマートシティ**: インテリジェントインフラと資源管理システム
- **コンシューマーエレクトロニクス**: AI搭載モバイルアプリケーションとスマートホームデバイス

## 学習成果概要

### モジュール01学習成果:
- クラウドとエッジAIアーキテクチャの基本的な違いを理解する
- エッジデプロイメント向けのコア最適化技術を習得する
- 実世界のアプリケーションと成功事例を認識する
- EdgeAIソリューションを実装するための実践的スキルを習得する

### モジュール02学習成果:
- 異なるSLM設計哲学とそのデプロイメントへの影響を深く理解する
- 計算制約とパフォーマンス要件に基づいた戦略的意思決定能力を習得する
- デプロイメントの柔軟性のトレードオフを理解する
- 効率的なAIアーキテクチャに関する未来志向の洞察を持つ

### モジュール03学習成果:
- 戦略的なモデル選択能力
- 最適化技術の習得
- デプロイメント柔軟性の習得
- 実運用向けの構成能力

### モジュール04学習成果:
- 量子化の境界と実践的な応用を深く理解する
- 複数の最適化フレームワーク（Llama.cpp、Olive、OpenVINO、MLX）を使った実践的な経験
- OpenVINOとNNCFを使ったIntelハードウェア最適化を習得する
- 多様なプラットフォームにわたるハードウェア対応の最適化選択能力
- クロスプラットフォームエッジコンピューティング環境向けの実運用デプロイメントスキル
- 最適なEdgeAIソリューションのための戦略的フレームワーク選択とワークフロー統合

### モジュール05学習成果:
- SLMOpsのパラダイムと運用原則を習得する
- 知識移転と効率最適化のためのモデル蒸留を実装する
- ドメイン固有のモデルカスタマイズのためのファインチューニング技術を適用する
- 監視と保守戦略を伴う実運用可能なSLMソリューションをデプロイする

### モジュール06学習成果:
- AIエージェントと小型言語モデルアーキテクチャの基礎概念を理解する
- 複数のプラットフォームとフレームワークにわたる関数呼び出しの実装を習得する
- モデルコンテキストプロトコル（MCP）を統合して標準化された外部ツールとの相互作用を実現する
- 最小限の人間の介入で高度なエージェントシステムを構築する

### モジュール07学習成果:
- 包括的なEdge AI開発ワークフローのためのVisual Studio Code向けAIツールキットを習得する
- Windows AI FoundryプラットフォームとNPU最適化戦略に関する専門知識を得る
- 多様なEdgeAIプラットフォームと実装戦略に関する実践的な経験を得る
- NVIDIA、モバイル、Azure、Windowsプラットフォームにわたるハードウェア固有の最適化技術を習得する
- パフォーマンス、コスト、プライバシー要件の間のデプロイメントトレードオフを理解する
- 異なるエコシステムにわたる実世界のEdgeAIアプリケーションを構築するための実践的スキルを習得する

## 期待されるコース成果

このコースを成功裏に修了することで、EdgeAIイニシアチブをプロフェッショナルな環境でリードするための知識、スキル、自信を得ることができます。

### プロフェッショナル準備

**技術的リーダーシップ**
- **ソリューションアーキテクチャ**: エンタープライズ要件を満たす包括的なEdgeAIシステムを設計する
- **パフォーマンス最適化**: 精度、速度、リソース消費の間で最適なバランスを達成する
- **クロスプラットフォームデプロイメント**: Windows、Linux、モバイル、組み込みプラットフォームにわたるソリューションを実装する
- **運用管理**: エンタープライズグレードの信頼性を持つEdgeAIシステムを維持および拡張する

**業界専門知識**
- **技術評価**: 特定のビジネス課題に適したEdgeAIソリューションを評価および推奨する
- **実装計画**: EdgeAIプロジェクトの現実的なタイムラインとリソース要件を開発する
- **リスク管理**: EdgeAIデプロイメントにおける技術的および運用上のリスクを特定し軽減する
- **ROI最適化**: EdgeAI実装から測定可能なビジネス価値を示す

### キャリア向上の機会

**プロフェッショナルな役割**
- EdgeAIソリューションアーキテクト
- 機械学習エンジニア（エッジ専門）
- IoT AI開発者
- モバイルAIアプリケーション開発者
- エンタープライズAIコンサルタント

**業界セクター**
- スマート製造とインダストリー4.0
- 自律車両と交通
- 医療技術と医療機器
- 金融技術とセキュリティ
- コンシューマーエレクトロニクスとモバイルアプリケーション

### 認定と検証

**ポートフォリオ開発**
- 実践的な能力を示すエンドツーエンドのEdgeAIプロジェクトを完了する
- 複数のハードウェアプラットフォームにわたる実運用可能なソリューションをデプロイする
- 達成した最適化戦略とパフォーマンス改善を文書化する

**継続的学習パス**
- 高度なAI専門分野への基盤
- クラウドエッジ
**EdgeAIの未来は、モデルアーキテクチャ、量子化技術、そして効率性と専門性を優先する展開戦略の継続的な改善にかかっています。このパラダイムシフトを受け入れる組織は、AIの変革的な可能性を活用しながら、データと運用の管理を維持することができるでしょう。**

## その他のコース

私たちのチームは他にもコースを提供しています！ぜひチェックしてください：

- [MCP初心者向け](https://github.com/microsoft/mcp-for-beginners)
- [AIエージェント初心者向け](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [.NETを使った生成AI初心者向け](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [JavaScriptを使った生成AI初心者向け](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [生成AI初心者向け](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML初心者向け](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [データサイエンス初心者向け](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI初心者向け](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [サイバーセキュリティ初心者向け](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Web開発初心者向け](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT初心者向け](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR開発初心者向け](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [GitHub Copilotを活用したAIペアプログラミングの習得](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [C#/.NET開発者向けGitHub Copilotの習得](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [自分だけのCopilotアドベンチャーを選ぼう](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。