<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "64a53ca0c6f9d7f6d3620adfd1dd1e6e",
  "translation_date": "2025-07-22T02:45:46+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# 初心者のためのEdgeAI

エッジAI技術を深く学ぶための教育プログラム。3つの包括的なモジュール（EdgeAIの基礎、小型言語モデル（SLM）の基盤、実践的な展開戦略）で構成されています。このコースでは、基本的な概念から高度な実装までを学び、実際のケーススタディ、ハンズオン演習、展開例を通じて、エッジデバイス上でAIモデルを効果的に実行する方法を紹介します。これにより、プライバシーの向上、レイテンシの削減、効率性の向上を実現します。

![コースカバー画像](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ja.png)

## コース構成

### [モジュール01: EdgeAIの基礎と変革](./Module01/README.md)
**テーマ**: エッジAI展開の変革的シフト

#### チャプター構成:
- [**セクション1: EdgeAIの基礎**](./Module01/01.EdgeAIFundamentals.md)
  - 従来のクラウドAIとエッジAIの比較
  - エッジコンピューティングの課題と制約
  - 主要技術: モデル量子化、圧縮最適化、小型言語モデル（SLM）
  - ハードウェアアクセラレーション: NPU、GPU最適化、CPU最適化
  - 利点: プライバシーとセキュリティ、低レイテンシ、オフライン機能、コスト効率

- [**セクション2: 実際のケーススタディ**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi & Muモデルエコシステム
    - Phi Silica: Windows AI統合
    - Muモデル: タスク特化型マイクロ言語モデル
  - 日本航空のAIレポートシステムのケーススタディ
  - 市場への影響と将来の方向性
  - 展開時の考慮事項とベストプラクティス

- [**セクション3: 実践的な実装ガイド**](./Module01/03.PracticalImplementationGuide.md)
  - 開発環境のセットアップ（Python 3.10+、.NET 8+）
  - ハードウェア要件と推奨構成
  - コアモデルファミリーのリソース
  - 量子化と最適化ツール（Llama.cpp、Microsoft Olive、Apple MLX）
  - 評価と検証のチェックリスト

- [**セクション4: エッジAI展開ハードウェアプラットフォーム**](./Module01/04.EdgeDeployment.md)
  - エッジAI展開の考慮事項と要件
  - IntelエッジAIハードウェアと最適化技術
  - モバイルおよび組み込みシステム向けのQualcomm AIソリューション
  - NVIDIA Jetsonとエッジコンピューティングプラットフォーム
  - NPUアクセラレーションを備えたWindows AI PCプラットフォーム
  - ハードウェア特化型最適化戦略

---

### [モジュール02: 小型言語モデル（SLM）の基盤](./Module02/README.md)
**テーマ**: SLMの理論的原則、実装戦略、実運用展開

#### チャプター構成:
- [**セクション1: Microsoft Phiモデルファミリーの基礎**](./Module02/01.PhiFamily.md)
  - デザイン哲学の進化（Phi-1からPhi-4）
  - 効率性を重視したアーキテクチャ設計
  - 特化型機能（推論、マルチモーダル、エッジ展開）

- [**セクション2: Qwenファミリーの基礎**](./Module02/02.QwenFamily.md)
  - オープンソースの卓越性（Qwen 1.0からQwen3） - Hugging Faceで利用可能
  - 思考モード機能を備えた高度な推論アーキテクチャ
  - スケーラブルな展開オプション（0.5B-235Bパラメータ）

- [**セクション3: Gemmaファミリーの基礎**](./Module02/03.GemmaFamily.md)
  - 研究主導の革新（Gemma 3 & 3n）
  - マルチモーダルの卓越性
  - モバイルファーストのアーキテクチャ

- [**セクション4: BitNETファミリーの基礎**](./Module02/04.BitNETFamily.md)
  - 革新的な量子化技術（1.58ビット）
  - https://github.com/microsoft/BitNet からの特化型推論フレームワーク
  - 極限の効率性を通じた持続可能なAIリーダーシップ

- [**セクション5: Microsoft Muモデルの基礎**](./Module02/05.mumodel.md)
  - Windows 11に組み込まれたデバイスファーストアーキテクチャ
  - Windows 11設定とのシステム統合
  - プライバシーを保護するオフライン操作

- [**セクション6: Phi-Silicaの基礎**](./Module02/06.phisilica.md)
  - Windows 11 Copilot+ PCに組み込まれたNPU最適化アーキテクチャ
  - 卓越した効率性（1.5Wで650トークン/秒）
  - Windows App SDKを使用した開発者統合

---

### [モジュール03: 小型言語モデルの展開](./Module03/README.md)
**テーマ**: 理論から実運用環境までのSLMライフサイクル展開

#### チャプター構成:
- [**セクション1: SLMの高度な学習**](./Module03/01.SLMAdvancedLearning.md)
  - パラメータ分類フレームワーク（Micro SLM 100M-1.4B、Medium SLM 14B-30B）
  - 高度な最適化技術（量子化手法、BitNET 1ビット量子化）
  - モデル取得戦略（Phiモデル用Azure AI Foundry、選択モデル用Hugging Face）

- [**セクション2: ローカル環境での展開**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollamaユニバーサルプラットフォーム展開
  - Microsoft Foundryのローカルエンタープライズグレードソリューション
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
  - 精度分類フレームワーク（超低精度、低精度、中精度）
  - GGUFおよびONNX形式の利点とユースケース
  - 運用効率のための量子化の利点
  - パフォーマンスベンチマークとメモリフットプリントの比較

- [**セクション2: Llama.cpp実装ガイド**](./Module04/02.Llamacpp.md)
  - クロスプラットフォームインストール（Windows、macOS、Linux）
  - GGUF形式変換と量子化レベル（Q2_KからQ8_0）
  - ハードウェアアクセラレーション（CUDA、Metal、OpenCL、Vulkan）
  - Python統合とREST API展開

- [**セクション3: Microsoft Olive最適化スイート**](./Module04/03.MicrosoftOlive.md)
  - 40以上の組み込みコンポーネントを使用したハードウェア対応モデル最適化
  - 動的および静的量子化による自動最適化
  - Azure MLワークフローとのエンタープライズ統合
  - 人気モデルのサポート（Llama、Phi、選択されたQwenモデル、Gemma）

- [**セクション4: Apple MLXフレームワークの深掘り**](./Module04/04.AppleMLX.md)
  - Apple Siliconの統一メモリアーキテクチャ
  - LLaMA、Mistral、Phi-3、選択されたQwenモデルのサポート
  - LoRAファインチューニングとモデルカスタマイズ
  - 4ビット/8ビット量子化によるHugging Face統合

---

### [モジュール05: SLMOps - 小型言語モデルの運用](./Module05/README.md)
**テーマ**: 蒸留から実運用展開までのSLMライフサイクル運用

#### チャプター構成:
- [**セクション1: SLMOpsの紹介**](./Module05/01.IntroduceSLMOps.md)
  - SLMOpsのAI運用におけるパラダイムシフト
  - コスト効率とプライバシーファーストアーキテクチャ
  - 戦略的ビジネスインパクトと競争優位性
  - 実際の実装課題と解決策

- [**セクション2: モデル蒸留 - 理論から実践へ**](./Module05/02.SLMOps-Distillation.md)
  - 教師モデルから生徒モデルへの知識移転
  - 2段階の蒸留プロセスの実装
  - 実践例を含むAzure ML蒸留ワークフロー
  - 推論時間を85%削減し、92%の精度を維持

- [**セクション3: ファインチューニング - 特定タスク向けモデルのカスタマイズ**](./Module05/03.SLMOps-Finetuing.md)
  - パラメータ効率の高いファインチューニング（PEFT）技術
  - LoRAおよびQLoRAの高度な手法
  - Microsoft Oliveによるファインチューニングの実装
  - マルチアダプタートレーニングとハイパーパラメータ最適化

- [**セクション4: 展開 - 実運用対応の実装**](./Module05/04.SLMOps.Deployment.md)
  - 実運用向けのモデル変換と量子化
  - Foundry Local展開構成
  - パフォーマンスベンチマークと品質検証
  - 75%のサイズ削減と運用監視

---

### [モジュール06: SLMエージェントシステム - AIエージェントと関数呼び出し](./Module06/README.md)
**テーマ**: 基礎から高度な関数呼び出しおよびモデルコンテキストプロトコル（MCP）統合までのSLMエージェントシステムの実装

#### チャプター構成:
- [**セクション1: AIエージェントと小型言語モデルの基礎**](./Module06/01.IntroduceAgent.md)
  - エージェント分類フレームワーク（反射型、モデルベース型、目標ベース型、学習型エージェント）
  - SLMの基礎と最適化戦略（GGUF、量子化、エッジフレームワーク）
  - SLMとLLMのトレードオフ分析（コスト10-30倍削減、タスク効果70-80%）
  - Ollama、VLLM、Microsoftエッジソリューションを用いた実践的展開

- [**セクション2: 小型言語モデルにおける関数呼び出し**](./Module06/02.FunctionCalling.md)
  - システマチックなワークフロー実装（意図検出、JSON出力、外部実行）
  - プラットフォーム固有の実装（Phi-4-mini、選択されたQwenモデル、Microsoft Foundry Local）
  - 高度な例（マルチエージェント協調、動的ツール選択）
  - 実運用の考慮事項（レート制限、監査ログ、セキュリティ対策）

- [**セクション3: モデルコンテキストプロトコル（MCP）の統合**](./Module06/03.IntroduceMCP.md)
  - プロトコルアーキテクチャとレイヤードシステム設計
  - マルチバックエンドサポート（開発用Ollama、実運用用vLLM）
  - 接続プロトコル（STDIOおよびSSEモード）
  - 実際のアプリケーション（ウェブ自動化、データ処理、API統合）

---

### [モジュール07: EdgeAI実装サンプル](./Module07/README.md)
**テーマ**: 多様なプラットフォームとフレームワークにおける包括的なEdgeAI実装

#### チャプター構成:
- [**NVIDIA Jetson Orin NanoでのEdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - クレジットカードサイズのフォームファクターで67 TOPSのAI性能
  - ジェネレーティブAIモデルのサポート（ビジョントランスフォーマー、LLM、ビジョンと言語モデル）
  - ロボティクス、ドローン、インテリジェントカメラ、自律デバイスでの応用
  - AI開発を民主化するための手頃な$249プラットフォーム

- [**.NET MAUIとONNX Runtime GenAIを使用したモバイルアプリケーションでのEdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 単一のC#コードベースによるクロスプラットフォームモバイルAI
  - ハードウェアアクセラレーションのサポート（CPU、GPU、モバイルAIプロセッサ）
  - プラットフォーム固有の最適化（iOS用CoreML、Android用NNAPI）
  - 完全なジェネレーティブAIループの実装

- [**Azureでの小型言語モデルエンジンを使用したEdgeAI**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - クラウドとエッジのハイブリッド展開アーキテクチャ
  - Azure AIサービスとONNX Runtimeの統合
  - エンタープライズ規模の展開と継続的なモデル管理
  - インテリジェントな文書処理のためのハイブリッドAIワークフロー

- [**Windows MLを使用したEdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - 高性能なオンデバイス推論のためのWindows AI Foundry基盤
  - ユニバーサルハードウェアサポート（AMD、Intel、NVIDIA、Qualcommシリコン）
  - 自動ハードウェア抽象化と最適化
  - 多様なWindowsハードウェアエコシステム向けの統一フレームワーク

- [**Foundry Localアプリケーションを使用したEdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - ローカルリソースを使用したプライバシー重視のRAG実装
  - セマンティック検索を備えたPhi-3言語モデル統合（Phiモデルのみ）
  - ローカルベクターデータベースのサポート（SQLite、Qdrant）
  - データ主権とオフライン操作機能

## 学習成果の概要

### モジュール01の学習成果:
- クラウドAIとエッジAIアーキテクチャの基本的な違いを理解する
- エッジ展開のための主要な最適化技術を習得する
- 実際のアプリケーションと成功事例を認識する
- EdgeAIソリューションを実装するための実践的なスキルを習得する

### モジュール02の学習成果:
- 各SLMの設計哲学とその展開への影響を深く理解する
- 計算制約と性能要件に
### モジュール06 学習成果:
- AIエージェントと小型言語モデル（SLM）アーキテクチャの基礎概念を理解する
- 複数のプラットフォームとフレームワークでの関数呼び出しの実装を習得する
- 標準化された外部ツールとの相互作用のためにModel Context Protocol (MCP)を統合する
- 最小限の人間の介入で高度なエージェントシステムを構築する

### モジュール07 学習成果:
- 多様なEdgeAIプラットフォームと実装戦略を実践的に体験する
- NVIDIA、モバイル、Azure、Windowsプラットフォームにおけるハードウェア特化の最適化技術を習得する
- パフォーマンス、コスト、プライバシー要件間のデプロイメントのトレードオフを理解する
- 異なるエコシステムで実際のEdgeAIアプリケーションを構築するための実践的スキルを開発する

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

- **段階的学習**: 基本概念から高度なデプロイメントまで徐々に進む
- **理論と実践の統合**: 各モジュールには理論的基盤と実践的操作が含まれる
- **実際のケーススタディ**: Microsoft、Alibaba、Googleなどの実例に基づく
- **実践的な練習**: 完全な構成ファイル、APIテスト手順、デプロイメントスクリプトを含む
- **パフォーマンスベンチマーク**: 推論速度、メモリ使用量、リソース要件の詳細な比較
- **企業向け考慮事項**: セキュリティ対策、コンプライアンスフレームワーク、データ保護戦略

## 学習の始め方

推奨学習パス:
1. **Module01**から始めてEdgeAIの基本的な理解を構築する
2. **Module02**に進み、さまざまなSLMモデルファミリーを深く理解する
3. **Module03**を学び、実践的なデプロイメントスキルを習得する
4. **Module04**で高度なモデル最適化とフォーマット変換を学ぶ
5. **Module05**を完了し、SLMOpsを習得して実運用に対応する
6. **Module06**を探求し、SLMエージェントシステムと関数呼び出しの能力を理解する
7. **Module07**を終了し、多様なEdgeAI実装サンプルを実践的に体験する

各モジュールは独立して完結していますが、順序立てた学習が最良の結果をもたらします。

## 学習ガイド

包括的な[学習ガイド](STUDY_GUIDE.md)が用意されており、学習体験を最大化するのに役立ちます。この学習ガイドには以下が含まれます:

- **構造化された学習パス**: 20時間でコースを完了するための最適化されたスケジュール
- **時間配分の指針**: 読書、演習、プロジェクトのバランスを取るための具体的な推奨事項
- **重要な概念の重点化**: 各モジュールの優先学習目標
- **自己評価ツール**: 理解度をテストするための質問と演習
- **ミニプロジェクトのアイデア**: 学習を強化するための実践的な応用

この学習ガイドは、集中的な学習（1週間）とパートタイム学習（3週間）の両方に対応しており、コースに10時間しか割けない場合でも効果的に時間を配分する方法を明確に示しています。

---

**EdgeAIの未来は、モデルアーキテクチャ、量子化技術、効率性と専門性を優先するデプロイメント戦略の継続的な改善にあります。このパラダイムシフトを受け入れる組織は、AIの変革的な可能性を活用しながら、データと運用の管理を維持することができます。**

## その他のコース

私たちのチームは他にもコースを提供しています！以下をチェックしてください:

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

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。