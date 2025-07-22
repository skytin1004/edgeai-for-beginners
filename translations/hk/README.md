<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "64a53ca0c6f9d7f6d3620adfd1dd1e6e",
  "translation_date": "2025-07-22T02:43:29+00:00",
  "source_file": "README.md",
  "language_code": "hk"
}
-->
# 初學者的 EdgeAI

深入學習 Edge AI 技術的教育旅程，分為三個全面的模組：EdgeAI 基礎、輕量語言模型基礎，以及實際部署策略。本課程從基本概念到高級實現，涵蓋真實案例研究、實作練習和部署範例，展示如何在邊緣設備上有效運行 AI 模型，以提升隱私、降低延遲和提高效率。

![課程封面圖片](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.hk.png)

## 課程架構

### [模組 01：EdgeAI 基礎與轉型](./Module01/README.md)
**主題**：Edge AI 部署的轉型變革

#### 章節結構：
- [**第一節：EdgeAI 基礎**](./Module01/01.EdgeAIFundamentals.md)
  - 傳統雲端 AI 與 Edge AI 的比較
  - 邊緣計算的挑戰與限制
  - 核心技術：模型量化、壓縮優化、輕量語言模型 (SLMs)
  - 硬體加速：NPU、GPU 優化、CPU 優化
  - 優勢：隱私安全、低延遲、離線功能、成本效益

- [**第二節：真實案例研究**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi & Mu 模型生態系統
    - Phi Silica：Windows AI 整合
    - Mu 模型：針對特定任務的微型語言模型
  - 日本航空 AI 報告系統案例研究
  - 市場影響與未來方向
  - 部署考量與最佳實踐

- [**第三節：實作指南**](./Module01/03.PracticalImplementationGuide.md)
  - 開發環境設置 (Python 3.10+，.NET 8+)
  - 硬體需求與推薦配置
  - 核心模型資源
  - 量化與優化工具 (Llama.cpp、Microsoft Olive、Apple MLX)
  - 評估與驗證清單

- [**第四節：Edge AI 部署硬體平台**](./Module01/04.EdgeDeployment.md)
  - Edge AI 部署考量與需求
  - Intel Edge AI 硬體與優化技術
  - Qualcomm 行動與嵌入式系統 AI 解決方案
  - NVIDIA Jetson 與邊緣計算平台
  - 配備 NPU 加速的 Windows AI PC 平台
  - 硬體特定的優化策略

---

### [模組 02：輕量語言模型基礎](./Module02/README.md)
**主題**：SLM 理論原則、實現策略與生產部署

#### 章節結構：
- [**第一節：Microsoft Phi 模型家族基礎**](./Module02/01.PhiFamily.md)
  - 設計理念的演進 (Phi-1 至 Phi-4)
  - 以效率為先的架構設計
  - 專業能力 (推理、多模態、邊緣部署)

- [**第二節：Qwen 模型家族基礎**](./Module02/02.QwenFamily.md)
  - 開源卓越 (Qwen 1.0 至 Qwen3) - 可於 Hugging Face 獲取
  - 具備思考模式能力的高級推理架構
  - 可擴展的部署選項 (0.5B-235B 參數)

- [**第三節：Gemma 模型家族基礎**](./Module02/03.GemmaFamily.md)
  - 以研究為驅動的創新 (Gemma 3 & 3n)
  - 多模態卓越
  - 行動優先架構

- [**第四節：BitNET 模型家族基礎**](./Module02/04.BitNETFamily.md)
  - 革命性的量化技術 (1.58-bit)
  - 專屬推理框架：https://github.com/microsoft/BitNet
  - 通過極致效率實現可持續 AI 領導地位

- [**第五節：Microsoft Mu 模型基礎**](./Module02/05.mumodel.md)
  - 內建於 Windows 11 的裝置優先架構
  - 與 Windows 11 設定的系統整合
  - 保護隱私的離線操作

- [**第六節：Phi-Silica 基礎**](./Module02/06.phisilica.md)
  - 為 Windows 11 Copilot+ PC 優化的 NPU 架構
  - 卓越效率 (650 tokens/second，功耗僅 1.5W)
  - 與 Windows App SDK 的開發者整合

---

### [模組 03：輕量語言模型部署](./Module03/README.md)
**主題**：完整的 SLM 部署生命周期，從理論到生產環境

#### 章節結構：
- [**第一節：SLM 高級學習**](./Module03/01.SLMAdvancedLearning.md)
  - 參數分類框架 (微型 SLM 100M-1.4B，中型 SLM 14B-30B)
  - 高級優化技術 (量化方法，BitNET 1-bit 量化)
  - 模型獲取策略 (Azure AI Foundry 提供 Phi 模型，Hugging Face 提供選定模型)

- [**第二節：本地環境部署**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollama 通用平台部署
  - Microsoft Foundry 本地企業級解決方案
  - 框架比較分析

- [**第三節：容器化雲端部署**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM 高效推理部署
  - Ollama 容器編排
  - ONNX Runtime 邊緣優化實現

---

### [模組 04：模型格式轉換與量化](./Module04/README.md)
**主題**：跨平台邊緣部署的完整模型優化工具包

#### 章節結構：
- [**第一節：模型格式轉換與量化基礎**](./Module04/01.Introduce.md)
  - 精度分類框架 (超低、低、中精度)
  - GGUF 和 ONNX 格式的優勢與使用案例
  - 量化對運行效率的好處
  - 性能基準與記憶體佔用比較

- [**第二節：Llama.cpp 實現指南**](./Module04/02.Llamacpp.md)
  - 跨平台安裝 (Windows、macOS、Linux)
  - GGUF 格式轉換與量化等級 (Q2_K 至 Q8_0)
  - 硬體加速 (CUDA、Metal、OpenCL、Vulkan)
  - Python 整合與 REST API 部署

- [**第三節：Microsoft Olive 優化套件**](./Module04/03.MicrosoftOlive.md)
  - 硬體感知模型優化，內建 40+ 組件
  - 動態與靜態量化的自動優化
  - 與 Azure ML 工作流程的企業整合
  - 支援的熱門模型 (Llama、Phi、選定的 Qwen 模型、Gemma)

- [**第四節：Apple MLX 框架深入探討**](./Module04/04.AppleMLX.md)
  - Apple Silicon 的統一記憶體架構
  - 支援 LLaMA、Mistral、Phi-3、選定的 Qwen 模型
  - LoRA 微調與模型自訂
  - 與 Hugging Face 的整合，支援 4-bit/8-bit 量化

---

### [模組 05：SLMOps - 輕量語言模型運營](./Module05/README.md)
**主題**：從蒸餾到生產部署的完整 SLM 運營生命周期

#### 章節結構：
- [**第一節：SLMOps 簡介**](./Module05/01.IntroduceSLMOps.md)
  - SLMOps 在 AI 運營中的範式轉變
  - 成本效益與隱私優先架構
  - 策略性商業影響與競爭優勢
  - 真實實現的挑戰與解決方案

- [**第二節：模型蒸餾 - 從理論到實踐**](./Module05/02.SLMOps-Distillation.md)
  - 從教師模型到學生模型的知識轉移
  - 兩階段蒸餾過程實現
  - Azure ML 蒸餾工作流程與實際範例
  - 推理時間減少 85%，準確率保留 92%

- [**第三節：微調 - 為特定任務自訂模型**](./Module05/03.SLMOps-Finetuing.md)
  - 參數高效微調 (PEFT) 技術
  - LoRA 與 QLoRA 高級方法
  - Microsoft Olive 微調實現
  - 多適配器訓練與超參數優化

- [**第四節：部署 - 生產就緒實現**](./Module05/04.SLMOps.Deployment.md)
  - 生產用的模型轉換與量化
  - Foundry Local 部署配置
  - 性能基準測試與質量驗證
  - 減少 75% 的模型大小並進行生產監控

---

### [模組 06：SLM Agentic 系統 - AI 代理與功能調用](./Module06/README.md)
**主題**：從基礎到高級功能調用與模型上下文協議整合的 SLM Agentic 系統實現

#### 章節結構：
- [**第一節：AI 代理與輕量語言模型基礎**](./Module06/01.IntroduceAgent.md)
  - 代理分類框架 (反射型、基於模型、目標導向、學習型代理)
  - SLM 基礎與優化策略 (GGUF、量化、邊緣框架)
  - SLM 與 LLM 的權衡分析 (成本降低 10-30 倍，任務效能達 70-80%)
  - 實際部署 (Ollama、VLLM、Microsoft 邊緣解決方案)

- [**第二節：輕量語言模型中的功能調用**](./Module06/02.FunctionCalling.md)
  - 系統化工作流程實現 (意圖檢測、JSON 輸出、外部執行)
  - 平台特定實現 (Phi-4-mini、選定的 Qwen 模型、Microsoft Foundry Local)
  - 高級範例 (多代理協作、動態工具選擇)
  - 生產考量 (速率限制、審計記錄、安全措施)

- [**第三節：模型上下文協議 (MCP) 整合**](./Module06/03.IntroduceMCP.md)
  - 協議架構與分層系統設計
  - 多後端支援 (Ollama 用於開發，vLLM 用於生產)
  - 連接協議 (STDIO 和 SSE 模式)
  - 真實應用 (網頁自動化、數據處理、API 整合)

---

### [模組 07：EdgeAI 實現範例](./Module07/README.md)
**主題**：跨多種平台與框架的全面 EdgeAI 實現

#### 章節結構：
- [**NVIDIA Jetson Orin Nano 的 EdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 信用卡大小的 67 TOPS AI 性能
  - 支援生成式 AI 模型 (視覺變換器、LLM、視覺語言模型)
  - 應用於機器人、無人機、智能相機、自主設備
  - 價格實惠的 $249 平台，推動 AI 開發普及化

- [**使用 .NET MAUI 和 ONNX Runtime GenAI 的行動應用程式 EdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 單一 C# 程式碼庫的跨平台行動 AI
  - 硬體加速支援 (CPU、GPU、行動 AI 處理器)
  - 平台特定優化 (iOS 的 CoreML，Android 的 NNAPI)
  - 完整的生成式 AI 循環實現

- [**Azure 中的 EdgeAI 與輕量語言模型引擎**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - 雲端與邊緣混合部署架構
  - Azure AI 服務與 ONNX Runtime 整合
  - 企業級部署與持續模型管理
  - 用於智能文檔處理的混合 AI 工作流程

- [**使用 Windows ML 的 EdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Windows AI Foundry 為高效能的裝置端推理提供基礎
  - 通用硬體支援 (AMD、Intel、NVIDIA、Qualcomm 晶片)
  - 自動硬體抽象與優化
  - 適用於多樣化 Windows 硬體生態系統的統一框架

- [**使用 Foundry Local 應用程式的 EdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - 以隱私為重點的 RAG 實現，使用本地資源
  - Phi-3 語言模型與語義搜索整合 (僅限 Phi 模型)
  - 支援本地向量數據庫 (SQLite、Qdrant)
  - 數據主權與離線操作能力

## 學習成果概覽

### 模組 01 學習成果：
- 理解雲端與邊緣 AI 架構的基本差異
- 掌握邊緣部署的核心優化技術
- 認識真實應用與成功案例
- 獲得實作 EdgeAI 解決方案的實用技能

### 模組 02 學習成果：
- 深入理解不同 SLM 設計理念及其部署影響
- 掌握基於計算限制與性能需求的策略性決策能力
- 理解部署靈活性的權衡
- 擁有面向未來的高效 AI 架構洞察力

### 模組 03 學習成果：
- 策略性模型選擇能力
- 優化技術的精通
- 部署靈活性的掌握
- 生產就緒配置能力

### 模組 04 學習成果：
- 深入理解量化邊界與實際應用
- 獲得多種優化框架的實作經驗 (Llama.cpp、Olive、MLX)
- 硬體感知的優化選擇能力
- 跨平台邊緣計算環境的生產部署技能

### 模組 05 學習成果：
- 掌握 SLMOps 範式與運營原則
- 實現模型蒸餾以進行知識轉移與效率優化
- 應用微調技術進行領域特定模型自訂
- 部署具備監控與維護策略的生產就緒 SLM 解決方案
### Module 06 學習成果：
- 理解 AI 代理和小型語言模型架構的基本概念  
- 掌握跨多個平台和框架的函數調用實現  
- 整合模型上下文協議 (MCP)，以標準化外部工具互動  
- 建立高級代理系統，減少對人類干預的需求  

### Module 07 學習成果：
- 實際操作多種 EdgeAI 平台及其實現策略  
- 掌握針對 NVIDIA、移動端、Azure 和 Windows 平台的硬件優化技術  
- 理解性能、成本和隱私需求之間的部署取捨  
- 培養在不同生態系統中構建真實 EdgeAI 應用的實用技能  

## 文件結構樹圖

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

## 課程特色

- **漸進式學習**：從基礎概念逐步進階到高級部署  
- **理論與實踐結合**：每個模組包含理論基礎和實際操作  
- **真實案例研究**：基於 Microsoft、阿里巴巴、Google 等的實際案例  
- **動手實踐**：完整的配置文件、API 測試流程和部署腳本  
- **性能基準**：詳細比較推理速度、內存使用和資源需求  
- **企業級考量**：安全實踐、合規框架和數據保護策略  

## 入門指南

推薦學習路徑：  
1. 從 **Module01** 開始，建立 EdgeAI 的基本理解  
2. 進入 **Module02**，深入了解各種 SLM 模型家族  
3. 學習 **Module03**，掌握實際部署技能  
4. 繼續 **Module04**，進行高級模型優化和格式轉換  
5. 完成 **Module05**，掌握 SLMOps 的生產級實現  
6. 探索 **Module06**，理解 SLM 代理系統和函數調用能力  
7. 最後完成 **Module07**，獲得多樣化 EdgeAI 實現範例的實際經驗  

每個模組都設計為獨立完整，但按順序學習能取得最佳效果。

## 學習指南

一份全面的 [學習指南](STUDY_GUIDE.md) 可幫助您最大化學習體驗。學習指南提供：  

- **結構化學習路徑**：優化的課程完成時間表，約 20 小時  
- **時間分配建議**：針對閱讀、練習和項目的具體建議  
- **重點概念聚焦**：每個模組的優先學習目標  
- **自我評估工具**：測試理解的問題和練習  
- **迷你項目創意**：加強學習的實際應用  

學習指南適合密集學習（一週）和兼職學習（三週），即使您只能投入 10 小時，也有清晰的時間分配指導。

---

**EdgeAI 的未來在於持續改進模型架構、量化技術和部署策略，優先考慮效率和專業化，而非通用能力。採用這種範式轉變的組織將能充分利用 AI 的變革潛力，同時保持對數據和運營的控制。**

## 其他課程

我們的團隊還提供其他課程！查看以下內容：  

- [MCP 初學者指南](https://github.com/microsoft/mcp-for-beginners)  
- [AI 代理初學者指南](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [使用 .NET 的生成式 AI 初學者指南](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
- [使用 JavaScript 的生成式 AI 初學者指南](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  
- [生成式 AI 初學者指南](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [機器學習初學者指南](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
- [數據科學初學者指南](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
- [AI 初學者指南](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
- [網絡安全初學者指南](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)  
- [Web 開發初學者指南](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
- [物聯網初學者指南](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
- [XR 開發初學者指南](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  
- [精通 GitHub Copilot 用於 AI 配對編程](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
- [精通 GitHub Copilot 用於 C#/.NET 開發者](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
- [選擇您的 Copilot 冒險](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。