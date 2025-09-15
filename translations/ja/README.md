<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3c232b8e9dac492a43b9c189f4cb04df",
  "translation_date": "2025-09-15T15:36:37+00:00",
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

以下の手順に従って、このリソースを活用してください：

1. **リポジトリをフォークする**: [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork) をクリック
2. **リポジトリをクローンする**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Azure AI Foundry Discordに参加して、専門家や開発者仲間と交流する**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 多言語対応

#### GitHub Actionによるサポート (自動化 & 常に最新)

[フランス語](../fr/README.md) | [スペイン語](../es/README.md) | [中国語 (簡体字)](../zh/README.md) | [中国語 (繁体字, マカオ)](../mo/README.md) | [中国語 (繁体字, 香港)](../hk/README.md) | [中国語 (繁体字, 台湾)](../tw/README.md) | [日本語](./README.md) | [韓国語](../ko/README.md) |  
**追加の翻訳を希望する場合は、対応可能な言語が [こちら](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) に記載されています**

## はじめに

**EdgeAI for Beginners**へようこそ！このコースは、エッジ人工知能の変革的な世界への包括的な旅を提供します。強力なAI機能とエッジデバイスでの実際の展開を結びつけ、データが生成され、意思決定が必要な場所でAIの可能性を活用できるようにします。

### 学べる内容

このコースでは、基礎概念から実際の運用までをカバーします：
- **エッジ展開に最適化された小型言語モデル (SLMs)**
- **多様なプラットフォームにおけるハードウェア対応の最適化**
- **プライバシーを保護しながらのリアルタイム推論**
- **企業向けアプリケーションの運用展開戦略**

### EdgeAIが重要な理由

EdgeAIは、現代の重要な課題に対応するパラダイムシフトを提供します：
- **プライバシーとセキュリティ**: 機密データをクラウドに送信せずにローカルで処理
- **リアルタイム性能**: 時間が重要なアプリケーションでネットワーク遅延を排除
- **コスト効率**: 帯域幅とクラウドコンピューティングの費用を削減
- **耐障害性**: ネットワーク障害時でも機能を維持
- **規制遵守**: データ主権要件を満たす

### EdgeAIとは

EdgeAIは、AIアルゴリズムや言語モデルをローカルのハードウェア上で実行し、データが生成される場所の近くで推論を行うことを指します。これにより、遅延が減少し、プライバシーが向上し、リアルタイムの意思決定が可能になります。

### コア原則:
- **デバイス上での推論**: AIモデルがエッジデバイス（スマートフォン、ルーター、マイクロコントローラー、産業用PC）上で実行
- **オフライン機能**: 常時インターネット接続なしで動作
- **低遅延**: リアルタイムシステムに適した即時応答
- **データ主権**: 機密データをローカルに保持し、セキュリティとコンプライアンスを向上

### 小型言語モデル (SLMs)

Phi-4、Mistral-7B、GemmaのようなSLMsは、大型LLMsをトレーニングまたは蒸留して最適化されたバージョンです：
- **メモリ使用量の削減**: エッジデバイスの限られたメモリを効率的に活用
- **計算負荷の軽減**: CPUやエッジGPU性能に最適化
- **起動時間の短縮**: 応答性の高いアプリケーション向けに迅速な初期化

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
  - 主要技術: モデル量子化、圧縮最適化、小型言語モデル (SLMs)
  - ハードウェアアクセラレーション: NPU、GPU最適化、CPU最適化
  - 利点: プライバシーセキュリティ、低遅延、オフライン機能、コスト効率

- [**セクション2: 実世界のケーススタディ**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi & Muモデルエコシステム
  - 日本航空のAI報告システムのケーススタディ
  - 市場への影響と将来の方向性
  - 展開の考慮事項とベストプラクティス

- [**セクション3: 実践的な実装ガイド**](./Module01/03.PracticalImplementationGuide.md)
  - 開発環境のセットアップ (Python 3.10+, .NET 8+)
  - ハードウェア要件と推奨構成
  - コアモデルファミリーリソース
  - 量子化と最適化ツール (Llama.cpp, Microsoft Olive, Apple MLX)
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
  - https://github.com/microsoft/BitNet からの特化した推論フレームワーク
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
  - パラメータ分類フレームワーク (Micro SLM 100M-1.4B, Medium SLM 14B-30B)
  - 高度な最適化技術 (量子化方法、BitNET 1ビット量子化)
  - モデル取得戦略 (PhiモデルはAzure AI Foundry、選択モデルはHugging Face)

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
**テーマ**: プラットフォーム全体でのエッジ展開向け完全モデル最適化ツールキット

#### チャプター構成:
- [**セクション1: モデル形式変換と量子化の基礎**](./Module04/01.Introduce.md)
  - 精度分類フレームワーク (超低、低、中精度)
  - GGUFとONNX形式の利点と使用例
  - 運用効率向上のための量子化の利点
  - パフォーマンスベンチマークとメモリ使用量比較

- [**セクション2: Llama.cpp実装ガイド**](./Module04/02.Llamacpp.md)
  - クロスプラットフォームインストール (Windows, macOS, Linux)
  - GGUF形式変換と量子化レベル (Q2_KからQ8_0)
  - ハードウェアアクセラレーション (CUDA, Metal, OpenCL, Vulkan)
  - Python統合とREST API展開

- [**セクション3: Microsoft Olive最適化スイート**](./Module04/03.MicrosoftOlive.md)
  - 40以上の組み込みコンポーネントによるハードウェア対応モデル最適化
  - 動的および静的量子化による自動最適化
  - Azure MLワークフローとの企業統合
  - 人気モデルのサポート (Llama, Phi, 選択されたQwenモデル, Gemma)

- [**セクション4: Apple MLXフレームワーク徹底解説**](./Module04/04.AppleMLX.md)
  - Apple Siliconの統一メモリアーキテクチャ
  - LLaMA, Mistral, Phi-3, 選択されたQwenモデルのサポート
  - LoRA微調整とモデルカスタマイズ
  - 4ビット/8ビット量子化によるHugging Face統合

---

### [モジュール05: SLMOps - 小型言語モデル運用](./Module05/README.md)
**テーマ**: 蒸留から運用展開までのSLMライフサイクル運用

#### チャプター構成:
- [**セクション1: SLMOpsの紹介**](./Module05/01.IntroduceSLMOps.md)
  - SLMOpsによるAI運用のパラダイムシフト
  - コスト効率とプライバシー重視のアーキテクチャ
  - 戦略的なビジネスインパクトと競争上の優位性
  - 実世界での実装課題と解決策

- [**セクション2: モデル蒸留 - 理論から実践へ**](./Module05/02.SLMOps-Distillation.md)
  - 教師モデルから生徒モデルへの知識移転
  - 2段階蒸留プロセスの実装
  - 実践例を含むAzure ML蒸留ワークフロー
  - 推論時間を85%削減し、92%の精度を維持

- [**セクション3: 微調整 - 特定タスク向けモデルのカスタマイズ**](./Module05/03.SLMOps-Finetuing.md)
  - パラメータ効率の高い微調整 (PEFT) 技術
  - LoRAとQLoRAの高度な方法
  - Microsoft Oliveによる微調整実装
  - マルチアダプタートレーニングとハイパーパラメータ最適化
- [**セクション 4: デプロイメント - 本番環境向け実装**](./Module05/04.SLMOps.Deployment.md)
  - 本番環境向けのモデル変換と量子化
  - Foundry Localのデプロイメント設定
  - パフォーマンスベンチマークと品質検証
  - 本番監視による75%のサイズ削減

---

### [モジュール 06: SLMエージェントシステム - AIエージェントと関数呼び出し](./Module06/README.md)
**テーマ**: 基礎から高度な関数呼び出し、モデルコンテキストプロトコル統合までのSLMエージェントシステムの実装

#### 章構成:
- [**セクション 1: AIエージェントと小型言語モデルの基礎**](./Module06/01.IntroduceAgent.md)
  - エージェント分類フレームワーク（反射型、モデルベース型、目標ベース型、学習型エージェント）
  - SLMの基礎と最適化戦略（GGUF、量子化、エッジフレームワーク）
  - SLMとLLMのトレードオフ分析（10-30倍のコスト削減、70-80%のタスク効率）
  - Ollama、VLLM、Microsoftエッジソリューションを用いた実践的デプロイメント

- [**セクション 2: 小型言語モデルにおける関数呼び出し**](./Module06/02.FunctionCalling.md)
  - システマティックなワークフロー実装（意図検出、JSON出力、外部実行）
  - プラットフォーム固有の実装（Phi-4-mini、選択されたQwenモデル、Microsoft Foundry Local）
  - 高度な例（マルチエージェント協力、動的ツール選択）
  - 本番環境の考慮事項（レート制限、監査ログ、セキュリティ対策）

- [**セクション 3: モデルコンテキストプロトコル（MCP）の統合**](./Module06/03.IntroduceMCP.md)
  - プロトコルアーキテクチャと階層型システム設計
  - マルチバックエンドサポート（開発用Ollama、本番用vLLM）
  - 接続プロトコル（STDIOおよびSSEモード）
  - 実際のアプリケーション（ウェブ自動化、データ処理、API統合）

---

### [モジュール 07: EdgeAI実装サンプル](./Module07/README.md)
**テーマ**: 多様なプラットフォームとフレームワークにわたる包括的なEdgeAI実装

#### 章構成:
- [**NVIDIA Jetson Orin NanoにおけるEdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - クレジットカードサイズのフォームファクターで67 TOPSのAI性能
  - ジェネレーティブAIモデルのサポート（ビジョントランスフォーマー、LLM、ビジョン言語モデル）
  - ロボティクス、ドローン、インテリジェントカメラ、自律デバイスでの応用
  - AI開発を民主化する手頃な価格の$249プラットフォーム

- [**.NET MAUIとONNX Runtime GenAIを使用したモバイルアプリケーションにおけるEdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 単一のC#コードベースによるクロスプラットフォームモバイルAI
  - ハードウェアアクセラレーションサポート（CPU、GPU、モバイルAIプロセッサ）
  - プラットフォーム固有の最適化（iOS向けCoreML、Android向けNNAPI）
  - 完全なジェネレーティブAIループの実装

- [**Azureにおける小型言語モデルエンジンを使用したEdgeAI**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - クラウドとエッジのハイブリッドデプロイメントアーキテクチャ
  - ONNX Runtimeを使用したAzure AIサービス統合
  - エンタープライズ規模のデプロイメントと継続的なモデル管理
  - インテリジェントな文書処理のためのハイブリッドAIワークフロー

- [**Windows MLを使用したEdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - 高性能なオンデバイス推論のためのWindows AI Foundry基盤
  - 普遍的なハードウェアサポート（AMD、Intel、NVIDIA、Qualcommシリコン）
  - 自動ハードウェア抽象化と最適化
  - 多様なWindowsハードウェアエコシステム向けの統一フレームワーク

- [**Foundry Localアプリケーションを使用したEdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - ローカルリソースを使用したプライバシー重視のRAG実装
  - Phi-3言語モデルとセマンティック検索の統合（Phiモデルのみ）
  - ローカルベクトルデータベースのサポート（SQLite、Qdrant）
  - データ主権とオフライン操作機能

## コース学習目標

この包括的なEdgeAIコースを修了することで、本番環境向けのEdgeAIソリューションを設計、実装、デプロイする専門知識を習得できます。構造化されたアプローチにより、理論的基盤と実践的な実装スキルの両方を確実に習得できます。

### 技術的能力

**基礎知識**
- クラウドベースとエッジベースのAIアーキテクチャの基本的な違いを理解する
- リソース制約環境向けのモデル量子化、圧縮、最適化の原則を習得する
- ハードウェアアクセラレーションオプション（NPU、GPU、CPU）とそのデプロイメントへの影響を理解する

**実装スキル**
- 小型言語モデルを多様なエッジプラットフォーム（モバイル、組み込み、IoT、エッジサーバー）にデプロイする
- Llama.cpp、Microsoft Olive、ONNX Runtime、Apple MLXなどの最適化フレームワークを適用する
- サブセカンド応答要件を満たすリアルタイム推論システムを実装する

**本番環境の専門知識**
- エンタープライズアプリケーション向けのスケーラブルなEdgeAIアーキテクチャを設計する
- デプロイされたシステムの監視、保守、更新戦略を実装する
- プライバシー保護型EdgeAI実装のためのセキュリティベストプラクティスを適用する

### 戦略的能力

**意思決定フレームワーク**
- EdgeAIの機会を評価し、ビジネスアプリケーションに適したユースケースを特定する
- モデルの精度、推論速度、消費電力、ハードウェアコストのトレードオフを評価する
- 特定のデプロイメント制約に基づいて適切なSLMファミリーと構成を選択する

**システムアーキテクチャ**
- 既存のインフラストラクチャと統合するエンドツーエンドのEdgeAIソリューションを設計する
- 最適なパフォーマンスとコスト効率を実現するハイブリッドエッジクラウドアーキテクチャを計画する
- リアルタイムAIアプリケーションのためのデータフローと処理パイプラインを実装する

### 業界応用

**実践的なデプロイメントシナリオ**
- **製造業**: 品質管理システム、予測保守、プロセス最適化
- **ヘルスケア**: プライバシー保護型診断ツールと患者モニタリングシステム
- **交通**: 自律車両の意思決定と交通管理
- **スマートシティ**: インテリジェントインフラと資源管理システム
- **コンシューマーエレクトロニクス**: AI搭載モバイルアプリケーションとスマートホームデバイス

## 学習成果概要

### モジュール 01 学習成果:
- クラウドとエッジAIアーキテクチャの基本的な違いを理解する
- エッジデプロイメントのためのコア最適化技術を習得する
- 実際のアプリケーションと成功事例を認識する
- EdgeAIソリューションを実装するための実践的スキルを習得する

### モジュール 02 学習成果:
- 異なるSLM設計哲学とそのデプロイメントへの影響を深く理解する
- 計算制約とパフォーマンス要件に基づく戦略的意思決定能力を習得する
- デプロイメントの柔軟性に関するトレードオフを理解する
- 効率的なAIアーキテクチャに関する将来志向の洞察を持つ

### モジュール 03 学習成果:
- 戦略的なモデル選択能力
- 最適化技術の習得
- デプロイメント柔軟性の習得
- 本番環境向けの構成能力

### モジュール 04 学習成果:
- 量子化の境界と実際の応用を深く理解する
- 複数の最適化フレームワーク（Llama.cpp、Olive、MLX）を使用した実践的経験
- ハードウェアに基づいた最適化選択能力
- クロスプラットフォームエッジコンピューティング環境向けの本番デプロイメントスキル

### モジュール 05 学習成果:
- SLMOpsのパラダイムと運用原則を習得する
- 知識移転と効率最適化のためのモデル蒸留を実装する
- ドメイン固有のモデルカスタマイズのための微調整技術を適用する
- 監視と保守戦略を備えた本番環境向けSLMソリューションをデプロイする

### モジュール 06 学習成果:
- AIエージェントと小型言語モデルアーキテクチャの基礎概念を理解する
- 複数のプラットフォームとフレームワークにわたる関数呼び出しの実装を習得する
- モデルコンテキストプロトコル（MCP）を統合して標準化された外部ツールとの相互作用を実現する
- 最小限の人間の介入で高度なエージェントシステムを構築する

### モジュール 07 学習成果:
- 多様なEdgeAIプラットフォームと実装戦略に関する実践的経験を得る
- NVIDIA、モバイル、Azure、Windowsプラットフォームにわたるハードウェア固有の最適化技術を習得する
- パフォーマンス、コスト、プライバシー要件間のデプロイメントトレードオフを理解する
- 異なるエコシステムにわたる実際のEdgeAIアプリケーションを構築するための実践的スキルを開発する

## 期待されるコース成果

このコースを成功裏に修了することで、プロフェッショナルな環境でEdgeAIイニシアチブを主導するための知識、スキル、自信を身につけることができます。

### プロフェッショナル準備

**技術的リーダーシップ**
- **ソリューションアーキテクチャ**: エンタープライズ要件を満たす包括的なEdgeAIシステムを設計する
- **パフォーマンス最適化**: 精度、速度、リソース消費の最適なバランスを達成する
- **クロスプラットフォームデプロイメント**: Windows、Linux、モバイル、組み込みプラットフォームにわたるソリューションを実装する
- **本番運用**: エンタープライズグレードの信頼性でEdgeAIシステムを維持および拡張する

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
- ヘルステクノロジーと医療機器
- 金融テクノロジーとセキュリティ
- コンシューマーエレクトロニクスとモバイルアプリケーション

### 認定と検証

**ポートフォリオ開発**
- 実践的な能力を示すエンドツーエンドのEdgeAIプロジェクトを完了する
- 複数のハードウェアプラットフォームにわたる本番環境向けソリューションをデプロイする
- 達成した最適化戦略とパフォーマンス改善を文書化する

**継続的学習パス**
- 高度なAI専門分野の基礎
- クラウドエッジハイブリッドアーキテクチャの準備
- 新興AI技術とフレームワークへのゲートウェイ

このコースは、AI技術のデプロイメントの最前線に立つ位置を提供し、現代生活を支えるデバイスやシステムにインテリジェントな機能をシームレスに統合します。

## ファイル構造ツリーダイアグラム

```
edgeai-for-beginners/
├── imgs/
│   └── cover.png
├── Module01/ (EdgeAI Fundamentals and Transformation)
│   ├── 01.EdgeAIFundamentals.md
│   ├── 02.RealWorldCaseStudies.md
│   ├── 03.PracticalImplementationGuide.md
│   ├── 04.EdgeDeployment.md
│   └── README.md
├── Module02/ (Small Language Model Foundations)
│   ├── 01.PhiFamily.md
│   ├── 02.QwenFamily.md
│   ├── 03.GemmaFamily.md
│   ├── 04.BitNETFamily.md
│   ├── 05.mumodel.md
│   ├── 06.phisilica.md
│   └── README.md
├── Module03/ (SLM Deployment Practice)
│   ├── 01.SLMAdvancedLearning.md
│   ├── 02.DeployingSLMinLocalEnv.md
│   ├── 03.DeployingSLMinCloud.md
│   └── README.md
├── Module04/ (Model Format Conversion and Quantization)
│   ├── 01.Introduce.md
│   ├── 02.Llamacpp.md
│   ├── 03.MicrosoftOlive.md
│   ├── 04.AppleMLX.md
│   └── README.md
├── Module05/ (SLMOps - Small Language Model Operations)
│   ├── 01.IntroduceSLMOps.md
│   ├── 02.SLMOps-Distillation.md
│   ├── 03.SLMOps-Finetuing.md
│   ├── 04.SLMOps.Deployment.md
│   └── README.md
├── Module06/ (SLM Agentic Systems)
│   ├── 01.IntroduceAgent.md
│   ├── 02.FunctionCalling.md
│   ├── 03.IntroduceMCP.md
│   └── README.md
├── Module07/ (EdgeAI Implementation Samples)
│   └── README.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md (This file)
├── SECURITY.md
├── STUDY_GUIDE.md
└── SUPPORT.md
```

## コースの特徴

- **段階的学習**: 基本概念から高度なデプロイメントへと徐々に進む
- **理論と実践の統合**: 各モジュールには理論的基盤と実践的操作の両方が含まれる
- **実際のケーススタディ**: Microsoft、Alibaba、Googleなどの実際のケースに基づく
- **実践的な練習**: 完全な構成ファイル、APIテスト手順、デプロイメントスクリプト
- **パフォーマンスベンチマーク**: 推論速度、メモリ使用量、リソース要件の詳細な比較
- **エンタープライズグレードの考慮事項**: セキュリティプラクティス、コンプライアンスフレームワーク、データ保護戦略

## 始め方

推奨学習パス:
1. **モジュール01**から始めてEdgeAIの基本的な理解を構築する
2. **モジュール02**に進んで、さまざまなSLMモデルファミリーを深く理解する
3. **モジュール03**を学び、実践的なデプロイメントスキルを習得する
4. **モジュール04**で高度なモデル最適化とフォーマット変換を学ぶ
5. **モジュール05**を完了して、本番環境向けのSLMOpsを習得する
6. **モジュール06**を探索して、SLMエージェントシステムと関数呼び出し機能を理解する
7. **モジュール07**で多様なEdgeAI実装サンプルを実践的に経験する

各モジュールは独
- [IoT初心者向け](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
- [XR開発初心者向け](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [GitHub Copilotを活用したAIペアプログラミングの習得](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
- [C#/.NET開発者向けGitHub Copilotの習得](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
- [自分で選ぶCopilotの冒険](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。