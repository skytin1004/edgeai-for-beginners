<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a189d7d9d47816a518ca119d79dc19b",
  "translation_date": "2025-09-22T12:05:56+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# 初心者向けEdgeAI

![コースカバー画像](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ja.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

以下の手順に従って、このリソースを使い始めましょう：

1. **リポジトリをフォークする**: [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork) をクリック
2. **リポジトリをクローンする**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Azure AI Foundry Discordに参加して、専門家や開発者仲間と交流する**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 多言語対応

#### GitHub Actionによるサポート (自動化 & 常に最新)

[アラビア語](../ar/README.md) | [ベンガル語](../bn/README.md) | [ブルガリア語](../bg/README.md) | [ビルマ語 (ミャンマー)](../my/README.md) | [中国語 (簡体字)](../zh/README.md) | [中国語 (繁体字, 香港)](../hk/README.md) | [中国語 (繁体字, マカオ)](../mo/README.md) | [中国語 (繁体字, 台湾)](../tw/README.md) | [クロアチア語](../hr/README.md) | [チェコ語](../cs/README.md) | [デンマーク語](../da/README.md) | [オランダ語](../nl/README.md) | [フィンランド語](../fi/README.md) | [フランス語](../fr/README.md) | [ドイツ語](../de/README.md) | [ギリシャ語](../el/README.md) | [ヘブライ語](../he/README.md) | [ヒンディー語](../hi/README.md) | [ハンガリー語](../hu/README.md) | [インドネシア語](../id/README.md) | [イタリア語](../it/README.md) | [日本語](./README.md) | [韓国語](../ko/README.md) | [マレー語](../ms/README.md) | [マラーティー語](../mr/README.md) | [ネパール語](../ne/README.md) | [ノルウェー語](../no/README.md) | [ペルシャ語 (ファルシー)](../fa/README.md) | [ポーランド語](../pl/README.md) | [ポルトガル語 (ブラジル)](../br/README.md) | [ポルトガル語 (ポルトガル)](../pt/README.md) | [パンジャブ語 (グルムキー)](../pa/README.md) | [ルーマニア語](../ro/README.md) | [ロシア語](../ru/README.md) | [セルビア語 (キリル文字)](../sr/README.md) | [スロバキア語](../sk/README.md) | [スロベニア語](../sl/README.md) | [スペイン語](../es/README.md) | [スワヒリ語](../sw/README.md) | [スウェーデン語](../sv/README.md) | [タガログ語 (フィリピン)](../tl/README.md) | [タイ語](../th/README.md) | [トルコ語](../tr/README.md) | [ウクライナ語](../uk/README.md) | [ウルドゥー語](../ur/README.md) | [ベトナム語](../vi/README.md)

**追加の翻訳を希望する場合、サポートされている言語は [こちら](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) に記載されています**

## はじめに

**EdgeAI for Beginners**へようこそ！このコースは、エッジ人工知能の変革的な世界への包括的な旅を提供します。強力なAI機能とエッジデバイスでの実際の展開を結びつけ、データが生成され、意思決定が必要な場所で直接AIの可能性を活用できるようにします。

### 学べる内容

このコースでは、基本的な概念から実際の運用準備までをカバーします：
- **エッジ展開に最適化された小型言語モデル (SLMs)**
- **多様なプラットフォームでのハードウェア対応の最適化**
- **プライバシーを保護するリアルタイム推論**
- **企業向けアプリケーションの運用展開戦略**

### EdgeAIが重要な理由

EdgeAIは、現代の重要な課題に対応するパラダイムシフトを表しています：
- **プライバシーとセキュリティ**: クラウドにデータを送信せずに、ローカルで機密データを処理
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

Phi-4、Mistral-7B、GemmaのようなSLMsは、大型LLMsの最適化バージョンであり、以下の目的でトレーニングまたは蒸留されています：
- **メモリ使用量の削減**: エッジデバイスの限られたメモリを効率的に使用
- **計算負荷の軽減**: CPUやエッジGPUでの性能向上
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
  - 主要技術: モデル量子化、圧縮最適化、小型言語モデル (SLMs)
  - ハードウェアアクセラレーション: NPU、GPU最適化、CPU最適化
  - 利点: プライバシーとセキュリティ、低遅延、オフライン機能、コスト効率

- [**セクション2: 実世界のケーススタディ**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi & Muモデルエコシステム
  - 日本航空のAI報告システムのケーススタディ
  - 市場への影響と将来の方向性
  - 展開の考慮事項とベストプラクティス

- [**セクション3: 実践的な実装ガイド**](./Module01/03.PracticalImplementationGuide.md)
  - 開発環境のセットアップ (Python 3.10+, .NET 8+)
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
  - 効率性を重視したアーキテクチャ設計
  - 特化した機能 (推論、マルチモーダル、エッジ展開)

- [**セクション2: Qwenファミリーの基礎**](./Module02/02.QwenFamily.md)
  - オープンソースの優位性 (Qwen 1.0からQwen3) - Hugging Faceで利用可能
  - 思考モード機能を備えた高度な推論アーキテクチャ
  - スケーラブルな展開オプション (0.5B-235Bパラメータ)

- [**セクション3: Gemmaファミリーの基礎**](./Module02/03.GemmaFamily.md)
  - 研究主導の革新 (Gemma 3 & 3n)
  - マルチモーダルの卓越性
  - モバイル優先のアーキテクチャ

- [**セクション4: BitNETファミリーの基礎**](./Module02/04.BitNETFamily.md)
  - 革新的な量子化技術 (1.58ビット)
  - https://github.com/microsoft/BitNet から提供される特化した推論フレームワーク
  - 極限効率による持続可能なAIリーダーシップ

- [**セクション5: Microsoft Muモデルの基礎**](./Module02/05.mumodel.md)
  - Windows 11に組み込まれたデバイス優先のアーキテクチャ
  - Windows 11設定とのシステム統合
  - プライバシーを保護するオフライン操作

- [**セクション6: Phi-Silicaの基礎**](./Module02/06.phisilica.md)
  - Windows 11 Copilot+ PCに組み込まれたNPU最適化アーキテクチャ
  - 卓越した効率性 (1.5Wで650トークン/秒)
  - Windows App SDKとの開発者統合

---

### [モジュール03: 小型言語モデルの展開](./Module03/README.md)
**テーマ**: 理論から運用環境までのSLMライフサイクル展開

#### チャプター構成:
- [**セクション1: SLM高度学習**](./Module03/01.SLMAdvancedLearning.md)
  - パラメータ分類フレームワーク (Micro SLM 100M-1.4B、Medium SLM 14B-30B)
  - 高度な最適化技術 (量子化手法、BitNET 1ビット量子化)
  - モデル取得戦略 (Phiモデル用Azure AI Foundry、選択モデル用Hugging Face)

- [**セクション2: ローカル環境での展開**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollamaユニバーサルプラットフォーム展開
  - Microsoft Foundryローカル企業向けソリューション
  - フレームワークの比較分析

- [**セクション3: コンテナ化されたクラウド展開**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM高性能推論展開
  - Ollamaコンテナオーケストレーション
  - ONNX Runtimeエッジ最適化実装

---

### [モジュール04: モデル形式変換と量子化](./Module04/README.md)
**テーマ**: プラットフォーム全体でのエッジ展開のための完全なモデル最適化ツールキット

#### チャプター構成:
- [**セクション1: モデル形式変換と量子化の基礎**](./Module04/01.Introduce.md)
  - 精度分類フレームワーク (超低、低、中精度)
  - GGUFとONNX形式の利点と使用例
  - 運用効率向上のための量子化の利点
  - パフォーマンスベンチマークとメモリ使用量の比較
- [**セクション2: Llama.cpp 実装ガイド**](./Module04/02.Llamacpp.md)
  - クロスプラットフォームインストール (Windows、macOS、Linux)
  - GGUF形式の変換と量子化レベル (Q2_KからQ8_0)
  - ハードウェアアクセラレーション (CUDA、Metal、OpenCL、Vulkan)
  - Python統合とREST APIデプロイ

- [**セクション3: Microsoft Olive 最適化スイート**](./Module04/03.MicrosoftOlive.md)
  - 40以上の組み込みコンポーネントによるハードウェア対応モデル最適化
  - 動的および静的量子化による自動最適化
  - Azure MLワークフローとのエンタープライズ統合
  - 人気モデル対応 (Llama、Phi、選択されたQwenモデル、Gemma)

- [**セクション4: OpenVINO Toolkit 最適化スイート**](./Module04/04.openvino.md)
  - IntelのオープンソースツールキットによるクロスプラットフォームAIデプロイ
  - 高度な最適化のためのNeural Network Compression Framework (NNCF)
  - 大規模言語モデルデプロイのためのOpenVINO GenAI
  - CPU、GPU、VPU、AIアクセラレータを活用したハードウェアアクセラレーション

- [**セクション5: Apple MLX フレームワーク徹底解説**](./Module04/05.AppleMLX.md)
  - Apple Silicon向け統一メモリアーキテクチャ
  - LLaMA、Mistral、Phi、選択されたQwenモデルのサポート
  - LoRAによる微調整とモデルカスタマイズ
  - 4ビット/8ビット量子化を用いたHugging Face統合

- [**セクション6: Edge AI 開発ワークフローの統合**](./Module04/06.workflow-synthesis.md)
  - 複数の最適化フレームワークを統合した統一ワークフローアーキテクチャ
  - フレームワーク選択の意思決定ツリーとパフォーマンスのトレードオフ分析
  - 生産準備の検証と包括的なデプロイ戦略
  - 新しいハードウェアとモデルアーキテクチャに対応する将来性のある戦略

---

### [モジュール05: SLMOps - 小型言語モデル運用](./Module05/README.md)
**テーマ**: 蒸留から本番デプロイまでのSLMライフサイクル運用の完全ガイド

#### 章構成:
- [**セクション1: SLMOpsの概要**](./Module05/01.IntroduceSLMOps.md)
  - AI運用におけるSLMOpsのパラダイムシフト
  - コスト効率とプライバシー重視のアーキテクチャ
  - 戦略的なビジネスインパクトと競争優位性
  - 実際の実装課題と解決策

- [**セクション2: モデル蒸留 - 理論から実践へ**](./Module05/02.SLMOps-Distillation.md)
  - 教師モデルから生徒モデルへの知識移転
  - 2段階蒸留プロセスの実装
  - 実践例を含むAzure ML蒸留ワークフロー
  - 推論時間を85%削減しつつ92%の精度を維持

- [**セクション3: 微調整 - 特定タスク向けモデルのカスタマイズ**](./Module05/03.SLMOps-Finetuing.md)
  - パラメータ効率の良い微調整 (PEFT) 技術
  - LoRAおよびQLoRAの高度な手法
  - Microsoft Oliveによる微調整の実装
  - マルチアダプタートレーニングとハイパーパラメータ最適化

- [**セクション4: デプロイ - 本番対応の実装**](./Module05/04.SLMOps.Deployment.md)
  - 本番向けのモデル変換と量子化
  - Foundry Localのデプロイ設定
  - パフォーマンスベンチマークと品質検証
  - サイズを75%削減しつつ本番監視を実施

---

### [モジュール06: SLMエージェントシステム - AIエージェントと関数呼び出し](./Module06/README.md)
**テーマ**: 基礎から高度な関数呼び出し、モデルコンテキストプロトコル統合までのSLMエージェントシステムの実装

#### 章構成:
- [**セクション1: AIエージェントと小型言語モデルの基礎**](./Module06/01.IntroduceAgent.md)
  - エージェント分類フレームワーク (反射型、モデルベース型、目標ベース型、学習型エージェント)
  - SLMの基礎と最適化戦略 (GGUF、量子化、エッジフレームワーク)
  - SLMとLLMのトレードオフ分析 (10-30倍のコスト削減、70-80%のタスク効率)
  - Ollama、VLLM、Microsoftエッジソリューションを用いた実践的デプロイ

- [**セクション2: 小型言語モデルにおける関数呼び出し**](./Module06/02.FunctionCalling.md)
  - 意図検出、JSON出力、外部実行を含む体系的なワークフロー実装
  - プラットフォーム固有の実装 (Phi-4-mini、選択されたQwenモデル、Microsoft Foundry Local)
  - 高度な例 (マルチエージェント協力、動的ツール選択)
  - 本番環境での考慮事項 (レート制限、監査ログ、セキュリティ対策)

- [**セクション3: モデルコンテキストプロトコル (MCP) 統合**](./Module06/03.IntroduceMCP.md)
  - プロトコルアーキテクチャと階層型システム設計
  - マルチバックエンドサポート (開発用Ollama、運用用vLLM)
  - 接続プロトコル (STDIOおよびSSEモード)
  - 実際のアプリケーション (ウェブ自動化、データ処理、API統合)

---

### [モジュール07: EdgeAI 実装サンプル](./Module07/README.md)
**テーマ**: 多様なプラットフォームとフレームワークを活用した包括的なEdgeAI実装

#### 章構成:
- [**Visual Studio Code向けAIツールキット**](./Module07/aitoolkit.md)
  - VS Code内での包括的なEdge AI開発環境
  - エッジデプロイ向けモデルカタログと探索
  - ローカルテスト、最適化、エージェント開発ワークフロー
  - エッジシナリオ向けのパフォーマンス監視と評価

- [**Windows EdgeAI 開発ガイド**](./Module07/windowdeveloper.md)
  - Windows AI Foundryプラットフォームの包括的概要
  - 効率的なNPU推論のためのPhi Silica API
  - 画像処理とOCR向けのコンピュータビジョンAPI
  - ローカル開発とテストのためのFoundry Local CLI

- [**NVIDIA Jetson Orin NanoでのEdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - クレジットカードサイズのフォームファクターで67 TOPSのAI性能
  - ジェネレーティブAIモデルのサポート (ビジョントランスフォーマー、LLM、ビジョン言語モデル)
  - ロボティクス、ドローン、インテリジェントカメラ、自律デバイスでの応用
  - AI開発を民主化する手頃な$249プラットフォーム

- [**.NET MAUIとONNX Runtime GenAIを用いたモバイルアプリでのEdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 単一のC#コードベースによるクロスプラットフォームモバイルAI
  - ハードウェアアクセラレーションサポート (CPU、GPU、モバイルAIプロセッサ)
  - プラットフォーム固有の最適化 (iOS向けCoreML、Android向けNNAPI)
  - 完全なジェネレーティブAIループの実装

- [**Azureでの小型言語モデルエンジンを用いたEdgeAI**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - クラウドとエッジのハイブリッドデプロイアーキテクチャ
  - ONNX Runtimeを活用したAzure AIサービス統合
  - エンタープライズ規模のデプロイと継続的なモデル管理
  - インテリジェントな文書処理のためのハイブリッドAIワークフロー

- [**Windows MLを用いたEdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - 高性能なオンデバイス推論のためのWindows AI Foundry基盤
  - AMD、Intel、NVIDIA、Qualcommシリコンを含むユニバーサルハードウェアサポート
  - 自動ハードウェア抽象化と最適化
  - 多様なWindowsハードウェアエコシステム向けの統一フレームワーク

- [**Foundry Localアプリケーションを用いたEdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - プライバシー重視のRAG実装とローカルリソース
  - Phi-4言語モデルとセマンティック検索 (Phiモデルのみ)
  - ローカルベクトルデータベースサポート (SQLite、Qdrant)
  - データ主権とオフライン操作機能

### [モジュール08: Microsoft Foundry Local – 完全な開発者ツールキット](./Module08/README.md)
**テーマ**: Foundry Localを用いてAIをローカルで構築、実行、統合し、Azure AI Foundryでスケールとハイブリッド化

#### 章構成:
- [**1: Foundry Localの始め方**](./Module08/01.FoundryLocalSetup.md)
- [**2: Azure AI Foundryを用いたAIソリューションの構築**](./Module08/02.AzureAIFoundryIntegration.md)
- [**3: オープンソースモデルのFoundry Local**](./Module08/03.OpenSourceModels.md)
- [**4: 最先端モデルとオンデバイス推論**](./Module08/04.CuttingEdgeModels.md)
- [**5: Foundry Localを用いたAIエージェント**](./Module08/05.AIPoweredAgents.md)
- [**6: ツールとしてのモデル**](./Module08/06.ModelsAsTools.md)

## コース学習目標

この包括的なEdgeAIコースを修了することで、実践的なEdgeAIソリューションを設計、実装、デプロイする専門知識を習得できます。理論的基礎と実践的スキルの両方をマスターできる構造化されたアプローチを提供します。

### 技術的能力

**基礎知識**
- クラウドベースとエッジベースのAIアーキテクチャの基本的な違いを理解する
- リソース制約環境向けのモデル量子化、圧縮、最適化の原則を習得する
- ハードウェアアクセラレーションオプション (NPU、GPU、CPU) とそのデプロイへの影響を理解する

**実装スキル**
- 小型言語モデルを多様なエッジプラットフォーム (モバイル、組み込み、IoT、エッジサーバー) にデプロイする
- Llama.cpp、Microsoft Olive、ONNX Runtime、Apple MLXを含む最適化フレームワークを適用する
- サブセカンド応答要件を満たすリアルタイム推論システムを実装する

**生産能力**
- エンタープライズアプリケーション向けのスケーラブルなEdgeAIアーキテクチャを設計する
- デプロイ済みシステムの監視、保守、更新戦略を実施する
- プライバシー保護型EdgeAI実装のためのセキュリティベストプラクティスを適用する

### 戦略的能力

**意思決定フレームワーク**
- EdgeAIの機会を評価し、ビジネスアプリケーションに適したユースケースを特定する
- モデル精度、推論速度、消費電力、ハードウェアコストのトレードオフを評価する
- 特定のデプロイ制約に基づいて適切なSLMファミリーと構成を選択する

**システムアーキテクチャ**
- 既存のインフラストラクチャと統合するエンドツーエンドのEdgeAIソリューションを設計する
- 最適なパフォーマンスとコスト効率を実現するためのハイブリッドエッジクラウドアーキテクチャを計画する
- リアルタイムAIアプリケーション向けのデータフローと処理パイプラインを実装する

### 業界応用

**実践的なデプロイシナリオ**
- **製造業**: 品質管理システム、予測保守、プロセス最適化
- **医療**: プライバシー保護型診断ツールと患者モニタリングシステム
- **交通**: 自律車両の意思決定と交通管理
- **スマートシティ**: インテリジェントインフラと資源管理システム
- **コンシューマーエレクトロニクス**: AI搭載モバイルアプリとスマートホームデバイス

## 学習成果概要

### モジュール01学習成果:
- クラウドとエッジAIアーキテクチャの基本的な違いを理解する
- エッジデプロイ向けの主要な最適化技術を習得する
- 実際のアプリケーションと成功事例を認識する
- EdgeAIソリューションを実装するための実践的スキルを習得する

### モジュール02学習成果:
- 異なるSLM設計哲学とそのデプロイへの影響を深く理解する
- 計算制約とパフォーマンス要件に基づいた戦略的意思決定能力を習得する
- デプロイの柔軟性に関するトレードオフを理解する
- 効率的なAIアーキテクチャに関する将来対応の洞察を持つ

### モジュール03学習成果:
- 戦略的なモデル選択能力
- 最適化技術の習得
- デプロイ柔軟性の習得
- 本番対応の構成能力

### モジュール04学習成果:
- 量子化の境界と実際の応用を深く理解する
- 複数の最適化フレームワーク (Llama.cpp、Olive、OpenVINO、MLX) を実践的に経験する
- OpenVINOとNNCFを用いたIntelハードウェア最適化を習得する
- 多様なプラットフォームにわたるハードウェア対応の最適化選択能力
- クロスプラットフォームエッジコンピューティング環境向けの本番デプロイスキル
- 最適なEdgeAIソリューションのための戦略的フレームワーク選択とワークフロー統合

### モジュール05学習成果:
- SLMOpsのパラダイムと運用原則を習得する
- 知識移転と効率最適化のためのモデル蒸留を実装する
- ドメイン固有のモデルカスタマイズのための微調整技術を適用する
- 監視と保守戦略を備えた本番対応SLMソリューションをデプロイする

### モジュール06学習成果:
- AIエージェントと小型言語モデルアーキテクチャの基礎概念を理解する
-
- **リスク管理**: EdgeAIの導入における技術的および運用上のリスクを特定し、軽減する  
- **ROI最適化**: EdgeAIの実装から測定可能なビジネス価値を示す  

### キャリア向上の機会  

**専門職**  
- EdgeAIソリューションアーキテクト  
- 機械学習エンジニア（Edge特化）  
- IoT AI開発者  
- モバイルAIアプリケーション開発者  
- エンタープライズAIコンサルタント  

**業界セクター**  
- スマート製造とインダストリー4.0  
- 自律走行車と交通分野  
- ヘルステクノロジーと医療機器  
- フィンテックとセキュリティ  
- 消費者向け電子機器とモバイルアプリケーション  

### 認定と検証  

**ポートフォリオ開発**  
- 実践的な能力を示すエンドツーエンドのEdgeAIプロジェクトを完了する  
- 複数のハードウェアプラットフォームで実運用可能なソリューションを展開する  
- 最適化戦略と達成した性能向上を文書化する  

**継続的学習パス**  
- 高度なAI専門分野への基盤を構築  
- クラウドとエッジのハイブリッドアーキテクチャの準備  
- 新興AI技術とフレームワークへのゲートウェイ  

このコースは、AI技術の導入の最前線に立つことを目指しており、現代生活を支えるデバイスやシステムにインテリジェントな機能をシームレスに統合します。  

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
│   ├── 04.openvino.md
│   ├── 05.AppleMLX.md
│   ├── 06.workflow-synthesis.md
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
│   ├── aitoolkit.md
│   ├── windowdeveloper.md
│   └── README.md
├── Module08/ (Hands on with Foundry Local)
│   ├── 01.FoundryLocalSetup.md
│   ├── 02.AzureAIFoundryIntegration.md
│   ├── 03.OpenSourceModels.md
│   ├── 04.CuttingEdgeModels.md
│   ├── 05.AIPoweredAgents.md
│   ├── 06.ModelsAsTools.md
│   └── README.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md (This file)
├── SECURITY.md
├── STUDY_GUIDE.md
└── SUPPORT.md
```
  

## コースの特徴  

- **段階的学習**: 基本概念から高度な展開まで徐々に進む  
- **理論と実践の統合**: 各モジュールには理論的基盤と実践的操作が含まれる  
- **実際のケーススタディ**: Microsoft、Alibaba、Googleなどの実例に基づく  
- **実践的な練習**: 完全な構成ファイル、APIテスト手順、展開スクリプトを完了する  
- **性能ベンチマーク**: 推論速度、メモリ使用量、リソース要件の詳細な比較  
- **エンタープライズ向け考慮事項**: セキュリティ実践、コンプライアンスフレームワーク、データ保護戦略  

## 始め方  

推奨学習パス:  
1. **Module01**から始めてEdgeAIの基本的な理解を構築する  
2. **Module02**に進み、さまざまなSLMモデルファミリーを深く理解する  
3. **Module03**を学び、実践的な展開スキルを習得する  
4. **Module04**を続けて、高度なモデル最適化、フォーマット変換、フレームワーク統合を学ぶ  
5. **Module05**を完了して、実運用可能なSLMOpsを習得する  
6. **Module06**を探求し、SLMエージェンティックシステムと機能呼び出し能力を理解する  
7. **Module07**を終了して、AIツールキットと多様なEdgeAI実装サンプルで実践的な経験を得る  
8. **Module08**を探求し、完全なFoundry Local開発者ツールキット（ローカル優先開発とハイブリッドAzure統合）を学ぶ  

各モジュールは独立して完結するよう設計されていますが、順序立てた学習が最良の結果をもたらします。  

## 学習ガイド  

包括的な[学習ガイド](STUDY_GUIDE.md)が用意されており、学習体験を最大化するのに役立ちます。この学習ガイドには以下が含まれます:  

- **構造化された学習パス**: 20時間でコースを完了するための最適化されたスケジュール  
- **時間配分の指針**: 読書、演習、プロジェクトのバランスを取るための具体的な推奨事項  
- **重要な概念の焦点**: 各モジュールの優先学習目標  
- **自己評価ツール**: 理解度をテストするための質問と演習  
- **ミニプロジェクトのアイデア**: 学習を強化するための実践的な応用  

この学習ガイドは、集中的な学習（1週間）とパートタイム学習（3週間）の両方に対応しており、コースに10時間しか割けない場合でも効果的に時間を配分する方法を明確に示します。  

---  

**EdgeAIの未来は、モデルアーキテクチャ、量子化技術、展開戦略の継続的な改善にあります。効率性と専門性を優先し、汎用的な能力を超えることが重要です。このパラダイムシフトを受け入れる組織は、AIの変革的な可能性を活用しながら、データと運用の管理を維持することができます。**  

## その他のコース  

私たちのチームは他にもコースを提供しています！以下をご覧ください:  

- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners)  
- [AI Agents For Beginners](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
- [Generative AI for Beginners using JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [ML for Beginners](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
- [Data Science for Beginners](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
- [AI for Beginners](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)  
- [Web Dev for Beginners](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
- [IoT for Beginners](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
- [XR Development for Beginners](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [Mastering GitHub Copilot for AI Paired Programming](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
- [Mastering GitHub Copilot for C#/.NET Developers](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
- [Choose Your Own Copilot Adventure](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  

---

