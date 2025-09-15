<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-15T16:59:13+00:00",
  "source_file": "Module07/README.md",
  "language_code": "ja"
}
-->
# 第7章 : EdgeAI サンプル

Edge AIは、人工知能とエッジコンピューティングの融合を表し、クラウド接続に依存せずにデバイス上で直接インテリジェントな処理を可能にします。この章では、異なるプラットフォームとフレームワークを使用した5つの独自のEdgeAI実装を探り、エッジでAIモデルを実行する際の多様性と強力さを紹介します。

## 1. NVIDIA Jetson Orin NanoでのEdgeAI

NVIDIA Jetson Orin Nanoは、コンパクトでクレジットカードサイズのフォームファクターで最大67 TOPSのAI性能を提供する、アクセス可能なエッジAIコンピューティングの革新を代表します。この強力なエッジAIプラットフォームは、ホビイスト、学生、プロの開発者に向けて生成AI開発を民主化します。

### 主な特徴
- 最大67 TOPSのAI性能を提供—前世代比で1.7倍の改善
- 1024 CUDAコアと最大32 TensorコアによるAI処理
- 最大周波数1.5 GHzの6コアArm Cortex-A78AE v8.2 64ビットCPU
- 価格はわずか249ドルで、開発者、学生、メーカーに最も手頃でアクセス可能なプラットフォームを提供

### アプリケーション
Jetson Orin Nanoは、ビジョントランスフォーマー、大規模言語モデル、ビジョンと言語モデルを含む最新の生成AIモデルの実行に優れています。特にGenAIユースケース向けに設計されており、手のひらサイズのデバイスで複数のLLMを実行できます。人気のあるユースケースには、AI搭載ロボット、スマートドローン、インテリジェントカメラ、自律型エッジデバイスが含まれます。

**詳細はこちら**: [NVIDIAのJetson Orin Nanoスーパーコンピュータ: EdgeAIの次の大きな進化](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. .NET MAUIとONNX Runtime GenAIを使用したモバイルアプリケーションでのEdgeAI

このソリューションは、.NET MAUI（マルチプラットフォームApp UI）とONNX Runtime GenAIを使用して、生成AIと大規模言語モデル（LLM）をクロスプラットフォームのモバイルアプリケーションに統合する方法を示します。このアプローチにより、.NET開発者はAndroidおよびiOSデバイス上でネイティブに動作する高度なAI搭載モバイルアプリケーションを構築できます。

### 主な特徴
- .NET MAUIフレームワークに基づき、AndroidおよびiOSアプリケーションの単一コードベースを提供
- ONNX Runtime GenAI統合により、モバイルデバイス上で生成AIモデルを直接実行可能
- CPU、GPU、モバイルAIプロセッサなど、モバイルデバイス向けのさまざまなハードウェアアクセラレータをサポート
- ONNX Runtimeを通じて、iOS向けのCoreMLやAndroid向けのNNAPIなどのプラットフォーム固有の最適化を提供
- 生成AIループ全体を実装（前処理、後処理、推論、ロジット処理、検索とサンプリング、KVキャッシュ管理を含む）

### 開発の利点
.NET MAUIアプローチにより、開発者は既存のC#および.NETスキルを活用しながらクロスプラットフォームAIアプリケーションを構築できます。ONNX Runtime GenAIフレームワークは、Llama、Mistral、Phi、Gemmaなどの複数のモデルアーキテクチャをサポートします。ARM64向けに最適化されたカーネルは、INT4量子化行列乗算を加速し、モバイルハードウェア上で効率的な性能を確保しながら、.NET開発の使い慣れた体験を維持します。

### ユースケース
このソリューションは、.NET技術を使用してAI搭載モバイルアプリケーションを構築したい開発者に最適です。インテリジェントチャットボット、画像認識アプリ、言語翻訳ツール、プライバシーを強化しオフライン機能を備えたパーソナライズされた推薦システムなどが含まれます。

**詳細はこちら**: [.NET MAUI ONNX Runtime GenAI例](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. AzureでのSmall Language Models Engineを使用したEdgeAI

MicrosoftのAzureベースのEdgeAIソリューションは、Small Language Models（SLM）をクラウドエッジハイブリッド環境で効率的に展開することに焦点を当てています。このアプローチは、クラウド規模のAIサービスとエッジ展開要件のギャップを埋めます。

### アーキテクチャの利点
- Azure AIサービスとのシームレスな統合
- ONNX Runtimeを使用して、SLM/LLMおよびマルチモーダルモデルをデバイス上およびクラウドで実行
- エンタープライズ規模の展開に最適化
- 継続的なモデル更新と管理をサポート

### ユースケース
Azure EdgeAI実装は、クラウド管理機能を備えたエンタープライズグレードのAI展開を必要とするシナリオで優れています。これには、インテリジェントな文書処理、リアルタイム分析、クラウドとエッジコンピューティングリソースの両方を活用するハイブリッドAIワークフローが含まれます。

**詳細はこちら**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. Windows MLを使用したEdgeAI

Windows MLは、オンデバイスモデル推論と簡易展開のために最適化されたMicrosoftの最先端ランタイムであり、Windows AI Foundryの基盤として機能します。このプラットフォームにより、開発者はPCハードウェアの全スペクトラムを活用したAI搭載Windowsアプリケーションを作成できます。

### プラットフォームの能力
- バージョン24H2（ビルド26100）以降のすべてのWindows 11 PCで動作
- NPUやGPUを搭載していないPCを含む、すべてのx64およびARM64 PCハードウェアで動作
- 開発者が独自のモデルを持ち込み、AMD、Intel、NVIDIA、Qualcommを含むシリコンパートナーエコシステム全体で効率的に展開可能
- インフラストラクチャAPIを活用し、異なるシリコンをターゲットにした複数のアプリビルドを作成する必要がなくなる

### 開発者の利点
Windows MLはハードウェアと実行プロバイダーを抽象化するため、コードを書くことに集中できます。また、Windows MLは最新のNPU、GPU、CPUがリリースされるたびに自動的に更新されます。このプラットフォームは、多様なWindowsハードウェアエコシステム全体でAI開発の統一されたフレームワークを提供します。

**詳細はこちら**: 
- [Windows ML概要](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI開発ガイド](../windowdeveloper.md) - Windows Edge AI開発の包括的なガイド

## 5. Foundry Localアプリケーションを使用したEdgeAI

Foundry Localは、.NETを使用してローカルリソースで検索拡張生成（RAG）アプリケーションを構築することを可能にします。ローカル言語モデルとセマンティック検索機能を組み合わせたこのアプローチは、完全にローカルインフラストラクチャで動作するプライバシー重視のAIソリューションを提供します。

### 技術アーキテクチャ
- Phi-3言語モデル、ローカル埋め込み、セマンティックカーネルを組み合わせてRAGシナリオを作成
- 埋め込みを浮動小数点値の配列（ベクトル）として使用し、コンテンツとそのセマンティックな意味を表現
- セマンティックカーネルが主要なオーケストレーターとして機能し、Phi-3とスマートコンポーネントを統合してシームレスなRAGパイプラインを作成
- SQLiteやQdrantなどのローカルベクトルデータベースをサポート

### 実装の利点
RAG（検索拡張生成）は、「何かを検索してプロンプトに組み込む」というシンプルな方法を指します。このローカル実装は、データプライバシーを確保しながら、カスタム知識ベースに基づいたインテリジェントな応答を提供します。このアプローチは、データ主権やオフライン操作機能を必要とするエンタープライズシナリオに特に価値があります。

**詳細はこちら**: [Foundry Local RAGサンプル](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Windows EdgeAI開発リソース

Windowsプラットフォームを対象とする開発者向けに、Windows EdgeAIエコシステム全体を網羅した包括的なガイドを作成しました。このリソースは、Windows AI Foundryに関する詳細情報を提供し、Windows上でのEdgeAI開発のためのAPI、ツール、ベストプラクティスを紹介します。

### Windows AI Foundryプラットフォーム
Windows AI Foundryプラットフォームは、Windowsデバイス上でのEdge AI開発専用に設計されたツールとAPIの包括的なスイートを提供します。これには、NPU加速ハードウェア向けの専門的なサポート、Windows ML統合、プラットフォーム固有の最適化技術が含まれます。

**包括的なガイド**: [Windows EdgeAI開発ガイド](../windowdeveloper.md)

このガイドには以下が含まれます:
- Windows AI Foundryプラットフォームの概要とコンポーネント
- NPUハードウェアでの効率的な推論のためのPhi Silica API
- 画像処理とOCRのためのコンピュータビジョンAPI
- Windows MLランタイムの統合と最適化
- ローカル開発とテストのためのFoundry Local CLI
- Windowsデバイス向けのハードウェア最適化戦略
- 実践的な実装例とベストプラクティス

### Edge AI開発のためのAIツールキット
Visual Studio Codeを使用する開発者向けに、AI Toolkit拡張機能はEdge AIアプリケーションの構築、テスト、展開専用に設計された包括的な開発環境を提供します。このツールキットは、VS Code内でのEdge AI開発ワークフロー全体を簡素化します。

**開発ガイド**: [Edge AI開発のためのAIツールキット](../aitoolkit.md)

AI Toolkitガイドには以下が含まれます:
- エッジ展開のためのモデルの発見と選択
- ローカルテストと最適化ワークフロー
- ONNXおよびOllamaのエッジモデル統合
- モデル変換と量子化技術
- エッジシナリオ向けのエージェント開発
- 性能評価とモニタリング
- 展開準備とベストプラクティス

## 結論

これら5つのEdgeAI実装は、今日利用可能なエッジAIソリューションの成熟度と多様性を示しています。Jetson Orin Nanoのようなハードウェア加速エッジデバイスから、ONNX Runtime GenAIやWindows MLのようなソフトウェアフレームワークまで、開発者はエッジでインテリジェントなアプリケーションを展開するための前例のない選択肢を持っています。

これらのプラットフォームに共通するテーマは、AI能力の民主化であり、異なるスキルレベルやユースケースの開発者に高度な機械学習を利用可能にすることです。モバイルアプリケーション、デスクトップソフトウェア、組み込みシステムを構築する際、これらのEdgeAIソリューションは効率的かつプライバシーを重視したエッジで動作する次世代のインテリジェントアプリケーションの基盤を提供します。

各プラットフォームは独自の利点を提供します: Jetson Orin Nanoはハードウェア加速エッジコンピューティング向け、ONNX Runtime GenAIはクロスプラットフォームモバイル開発向け、Azure EdgeAIはエンタープライズクラウドエッジ統合向け、Windows MLはWindowsネイティブアプリケーション向け、Foundry Localはプライバシー重視のRAG実装向けです。これらは、EdgeAI開発の包括的なエコシステムを形成しています。

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。