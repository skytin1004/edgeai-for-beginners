<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a405c29d4e4241d954e24c47bedd739a",
  "translation_date": "2025-07-22T09:59:09+00:00",
  "source_file": "README.md",
  "language_code": "hk"
}
-->
# EdgeAI 初學者指南

![課程封面圖片](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.hk.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)  
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)  
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)  
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)  

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

按照以下步驟開始使用這些資源：

1. **Fork 此倉庫**：點擊 [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
2. **Clone 此倉庫**：`git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**加入 Azure AI Foundry Discord，與專家及其他開發者交流**](https://discord.com/invite/ByRwuEEgH4)  

### 🌐 多語言支持

#### 透過 GitHub Action 支援（自動化且始終保持最新）

[法文](../fr/README.md) | [西班牙文](../es/README.md) | [中文（簡體）](../zh/README.md) | [中文（繁體，澳門）](../mo/README.md) | [中文（繁體，香港）](./README.md) | [中文（繁體，台灣）](../tw/README.md) | [日文](../ja/README.md) | [韓文](../ko/README.md)  

歡迎來到 EdgeAI 初學者指南，這裡結合了語言模型的強大功能與本地設備的高效性。本課程介紹了如何在邊緣硬件（如智能手機、物聯網板卡和小型伺服器）上直接運行小型、優化的語言模型（SLMs），而無需依賴雲端。您將探索即時、注重隱私的 AI 推理如何通過輕量化部署改變智能家居、工業監控和離線應用，並且專注於速度、安全性和模塊化。

**邊緣 AI**

邊緣 AI 是指在本地硬件上運行 AI 算法和語言模型——靠近數據生成的地方——而不依賴雲端資源進行推理。它降低了延遲，增強了隱私，並支持即時決策。

核心原則：
- 設備端推理：AI 模型在邊緣設備（如手機、路由器、微控制器、工業 PC）上運行。
- 離線能力：無需持續的互聯網連接即可運行。
- 低延遲：適合即時系統的快速響應。
- 數據主權：將敏感數據保留在本地，提高安全性和合規性。

**小型語言模型（SLMs）**

像 Phi-4、Mistral-7B 或 Gemma 這樣的 SLMs 是大型 LLMs 的優化版本——通過訓練或蒸餾實現：
- 減少內存佔用
- 降低計算需求
- 更快的啟動時間

它們在滿足以下限制的同時解鎖了強大的 NLP 功能：
- 嵌入式系統
- 移動設備
- 物聯網設備
- GPU 限制的邊緣伺服器
- 個人電腦

## 課程架構

### [模組 01：邊緣 AI 基礎與轉型](./Module01/README.md)
**主題**：邊緣 AI 部署的變革性轉變

#### 章節結構：
- [**第一節：邊緣 AI 基礎**](./Module01/01.EdgeAIFundamentals.md)  
  - 傳統雲端 AI 與邊緣 AI 的比較  
  - 邊緣計算的挑戰與限制  
  - 關鍵技術：模型量化、壓縮優化、小型語言模型（SLMs）  
  - 硬件加速：NPUs、GPU 優化、CPU 優化  
  - 優勢：隱私安全、低延遲、離線能力、成本效益  

- [**第二節：實際案例研究**](./Module01/02.RealWorldCaseStudies.md)  
  - Microsoft Phi & Mu 模型生態系統  
  - 日本航空 AI 報告系統案例研究  
  - 市場影響與未來方向  
  - 部署考量與最佳實踐  

- [**第三節：實踐實施指南**](./Module01/03.PracticalImplementationGuide.md)  
  - 開發環境設置（Python 3.10+，.NET 8+）  
  - 硬件需求與推薦配置  
  - 核心模型資源  
  - 量化與優化工具（Llama.cpp、Microsoft Olive、Apple MLX）  
  - 評估與驗證清單  

- [**第四節：邊緣 AI 部署硬件平台**](./Module01/04.EdgeDeployment.md)  
  - 邊緣 AI 部署的考量與需求  
  - Intel 邊緣 AI 硬件與優化技術  
  - Qualcomm 移動與嵌入式系統 AI 解決方案  
  - NVIDIA Jetson 與邊緣計算平台  
  - Windows AI PC 平台與 NPU 加速  
  - 硬件特定的優化策略  

---

### [模組 02：小型語言模型基礎](./Module02/README.md)
**主題**：SLM 理論原則、實施策略與生產部署

#### 章節結構：
- [**第一節：Microsoft Phi 模型家族基礎**](./Module02/01.PhiFamily.md)  
  - 設計理念演變（Phi-1 至 Phi-4）  
  - 以效率為先的架構設計  
  - 專業化能力（推理、多模態、邊緣部署）  

- [**第二節：Qwen 模型家族基礎**](./Module02/02.QwenFamily.md)  
  - 開源卓越（Qwen 1.0 至 Qwen3）——可在 Hugging Face 獲得  
  - 具有思維模式能力的高級推理架構  
  - 可擴展部署選項（0.5B-235B 參數）  

- [**第三節：Gemma 模型家族基礎**](./Module02/03.GemmaFamily.md)  
  - 以研究為驅動的創新（Gemma 3 & 3n）  
  - 多模態卓越  
  - 移動優先架構  

- [**第四節：BitNET 模型家族基礎**](./Module02/04.BitNETFamily.md)  
  - 革命性的量化技術（1.58-bit）  
  - 專業化推理框架來自 https://github.com/microsoft/BitNet  
  - 通過極端效率實現可持續 AI 領導力  

- [**第五節：Microsoft Mu 模型基礎**](./Module02/05.mumodel.md)  
  - 為設備優先架構設計，內建於 Windows 11  
  - 與 Windows 11 設置的系統集成  
  - 保護隱私的離線操作  

- [**第六節：Phi-Silica 模型基礎**](./Module02/06.phisilica.md)  
  - 為 Windows 11 Copilot+ PC 優化的 NPU 架構  
  - 卓越效率（650 tokens/second，功耗僅 1.5W）  
  - 與 Windows App SDK 的開發者集成  

---

### [模組 03：小型語言模型部署](./Module03/README.md)
**主題**：完整的 SLM 部署生命周期，從理論到生產環境

#### 章節結構：
- [**第一節：SLM 高級學習**](./Module03/01.SLMAdvancedLearning.md)  
  - 參數分類框架（微型 SLM 100M-1.4B，中型 SLM 14B-30B）  
  - 高級優化技術（量化方法、BitNET 1-bit 量化）  
  - 模型獲取策略（Azure AI Foundry 提供 Phi 模型，Hugging Face 提供選定模型）  

- [**第二節：本地環境部署**](./Module03/02.DeployingSLMinLocalEnv.md)  
  - Ollama 通用平台部署  
  - Microsoft Foundry 本地企業級解決方案  
  - 框架比較分析  

- [**第三節：容器化雲端部署**](./Module03/03.DeployingSLMinCloud.md)  
  - vLLM 高性能推理部署  
  - Ollama 容器編排  
  - ONNX Runtime 邊緣優化實現  

---

### [模組 04：模型格式轉換與量化](./Module04/README.md)
**主題**：跨平台邊緣部署的完整模型優化工具包

#### 章節結構：
- [**第一節：模型格式轉換與量化基礎**](./Module04/01.Introduce.md)  
  - 精度分類框架（超低、低、中精度）  
  - GGUF 和 ONNX 格式的優勢與使用場景  
  - 量化對運行效率的好處  
  - 性能基準與內存佔用比較  

- [**第二節：Llama.cpp 實施指南**](./Module04/02.Llamacpp.md)  
  - 跨平台安裝（Windows、macOS、Linux）  
  - GGUF 格式轉換與量化級別（Q2_K 至 Q8_0）  
  - 硬件加速（CUDA、Metal、OpenCL、Vulkan）  
  - Python 集成與 REST API 部署  

- [**第三節：Microsoft Olive 優化套件**](./Module04/03.MicrosoftOlive.md)  
  - 硬件感知模型優化，內建 40+ 組件  
  - 動態與靜態量化的自動優化  
  - 與 Azure ML 工作流的企業集成  
  - 支持的流行模型（Llama、Phi、選定 Qwen 模型、Gemma）  

- [**第四節：Apple MLX 框架深度解析**](./Module04/04.AppleMLX.md)  
  - 為 Apple Silicon 設計的統一內存架構  
  - 支持 LLaMA、Mistral、Phi-3、選定 Qwen 模型  
  - LoRA 微調與模型定制  
  - 與 Hugging Face 集成，支持 4-bit/8-bit 量化  

---

### [模組 05：SLMOps - 小型語言模型運營](./Module05/README.md)
**主題**：從蒸餾到生產部署的完整 SLM 運營生命周期

#### 章節結構：
- [**第一節：SLMOps 簡介**](./Module05/01.IntroduceSLMOps.md)  
  - SLMOps 在 AI 運營中的範式轉變  
  - 成本效益與隱私優先架構  
  - 戰略商業影響與競爭優勢  
  - 實際實施中的挑戰與解決方案  

- [**第二節：模型蒸餾——從理論到實踐**](./Module05/02.SLMOps-Distillation.md)  
  - 從教師模型到學生模型的知識轉移  
  - 兩階段蒸餾過程實施  
  - Azure ML 蒸餾工作流與實際示例  
  - 推理時間減少 85%，準確率保留 92%  

- [**第三節：微調——為特定任務定制模型**](./Module05/03.SLMOps-Finetuing.md)  
  - 參數高效微調（PEFT）技術  
  - LoRA 和 QLoRA 高級方法  
  - Microsoft Olive 微調實施  
  - 多適配器訓練與超參數優化  

- [**第四節：部署——生產就緒實施**](./Module05/04.SLMOps.Deployment.md)  
  - 生產模型的轉換與量化  
  - Foundry Local 部署配置  
  - 性能基準測試與質量驗證  
  - 尺寸減少 75%，並進行生產監控  

---

### [模組 06：SLM Agentic 系統——AI 代理與功能調用](./Module06/README.md)
**主題**：從基礎到高級功能調用及模型上下文協議集成的 SLM Agentic 系統實施

#### 章節結構：
- [**第一節：AI 代理與小型語言模型基礎**](./Module06/01.IntroduceAgent.md)  
  - 代理分類框架（反射型、基於模型、基於目標、學習型代理）  
  - SLM 基礎與優化策略（GGUF、量化、邊緣框架）  
  - SLM 與 LLM 的權衡分析（成本降低 10-30 倍，任務有效性達 70-80%）  
  - 使用 Ollama、VLLM 和 Microsoft 邊緣解決方案進行實際部署  

- [**第二節：小型語言模型中的功能調用**](./Module06/02.FunctionCalling.md)  
- 系統化工作流程實施（意圖檢測、JSON輸出、外部執行）
- 平台特定實施（Phi-4-mini、選定的Qwen模型、Microsoft Foundry Local）
- 高級範例（多代理協作、動態工具選擇）
- 生產考量（速率限制、審計記錄、安全措施）

- [**第3章：模型上下文協議（MCP）整合**](./Module06/03.IntroduceMCP.md)
  - 協議架構及分層系統設計
  - 多後端支持（Ollama用於開發，vLLM用於生產）
  - 連接協議（STDIO和SSE模式）
  - 真實世界應用（網頁自動化、數據處理、API整合）

---

### [第7章：EdgeAI實施範例](./Module07/README.md)
**主題**：涵蓋多平台及框架的全面EdgeAI實施

#### 章節結構：
- [**NVIDIA Jetson Orin Nano中的EdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 信用卡大小的形式因子提供67 TOPS AI性能
  - 支持生成式AI模型（視覺變換器、LLM、視覺語言模型）
  - 應用於機器人、無人機、智能相機、自主設備
  - 價格實惠的$249平台，推動AI開發普及化

- [**使用.NET MAUI和ONNX Runtime GenAI的移動應用EdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 單一C#代碼庫的跨平台移動AI
  - 硬件加速支持（CPU、GPU、移動AI處理器）
  - 平台特定優化（iOS的CoreML，Android的NNAPI）
  - 完整的生成式AI循環實施

- [**Azure中的EdgeAI與小型語言模型引擎**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - 雲端-邊緣混合部署架構
  - Azure AI服務與ONNX Runtime整合
  - 企業級部署及持續模型管理
  - 智能文檔處理的混合AI工作流程

- [**使用Windows ML的EdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Windows AI Foundry基礎，支持高效的設備端推理
  - 通用硬件支持（AMD、Intel、NVIDIA、Qualcomm芯片）
  - 自動硬件抽象及優化
  - 為多樣化Windows硬件生態系統提供統一框架

- [**使用Foundry Local應用的EdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - 注重隱私的RAG實施，使用本地資源
  - Phi-3語言模型整合語義搜索（僅限Phi模型）
  - 支持本地向量數據庫（SQLite、Qdrant）
  - 數據主權及離線操作能力

## 學習成果概覽

### 第1章學習成果：
- 理解雲端與邊緣AI架構的基本差異
- 掌握邊緣部署的核心優化技術
- 認識真實世界應用及成功案例
- 獲得實施EdgeAI解決方案的實用技能

### 第2章學習成果：
- 深入理解不同SLM設計理念及其部署影響
- 掌握基於計算約束及性能需求的戰略決策能力
- 理解部署靈活性的權衡
- 擁有面向未來的高效AI架構洞察力

### 第3章學習成果：
- 戰略模型選擇能力
- 優化技術精通
- 部署靈活性精通
- 生產就緒配置能力

### 第4章學習成果：
- 深入理解量化邊界及實際應用
- 熟悉多種優化框架（Llama.cpp、Olive、MLX）的操作
- 硬件感知的優化選擇能力
- 跨平台邊緣計算環境的生產部署技能

### 第5章學習成果：
- 掌握SLMOps範式及運營原則
- 實施模型蒸餾以進行知識轉移及效率優化
- 應用微調技術進行領域特定模型定制
- 部署生產就緒的SLM解決方案，並具備監控及維護策略

### 第6章學習成果：
- 理解AI代理及小型語言模型架構的基礎概念
- 掌握跨多平台及框架的函數調用實施
- 整合模型上下文協議（MCP），實現標準化的外部工具交互
- 構建複雜的代理系統，減少人工干預需求

### 第7章學習成果：
- 獲得多樣化EdgeAI平台及實施策略的實踐經驗
- 掌握針對NVIDIA、移動端、Azure及Windows平台的硬件特定優化技術
- 理解性能、成本及隱私需求之間的部署權衡
- 開發跨不同生態系統的真實世界EdgeAI應用的實用技能

## 文件結構樹狀圖

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
- **理論與實踐結合**：每個章節包含理論基礎及實際操作
- **真實案例研究**：基於Microsoft、阿里巴巴、Google等的實際案例
- **動手實踐**：完整配置文件、API測試流程及部署腳本
- **性能基準**：詳細比較推理速度、內存使用及資源需求
- **企業級考量**：安全實踐、合規框架及數據保護策略

## 入門指南

推薦學習路徑：
1. 從**第1章**開始，建立EdgeAI的基礎理解
2. 進入**第2章**，深入了解各種SLM模型家族
3. 學習**第3章**，掌握實際部署技能
4. 繼續**第4章**，進行高級模型優化及格式轉換
5. 完成**第5章**，掌握生產就緒的SLMOps實施
6. 探索**第6章**，理解SLM代理系統及函數調用能力
7. 最後完成**第7章**，獲得多樣化EdgeAI實施範例的實踐經驗

每個章節都設計為獨立完整，但按順序學習將獲得最佳效果。

## 學習指南

提供全面的[學習指南](STUDY_GUIDE.md)，幫助您最大化學習效果。學習指南包括：

- **結構化學習路徑**：優化的課程完成時間表（20小時）
- **時間分配建議**：平衡閱讀、練習及項目的具體建議
- **關鍵概念重點**：每章節的優先學習目標
- **自我評估工具**：測試理解的問題及練習
- **迷你項目創意**：加強學習的實際應用

學習指南適合密集學習（1週）及兼職學習（3週），即使您只能投入10小時，也有清晰的時間分配指導。

---

**EdgeAI的未來在於持續改進模型架構、量化技術及部署策略，優先考慮效率及專業化而非通用能力。採用這種範式轉變的組織將能充分利用AI的變革潛力，同時保持對數據及運營的控制。**

## 其他課程

我們的團隊還提供其他課程！查看以下內容：

- [MCP入門](https://github.com/microsoft/mcp-for-beginners)
- [AI代理入門](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [使用.NET的生成式AI入門](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [使用JavaScript的生成式AI入門](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [生成式AI入門](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [機器學習入門](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [數據科學入門](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [人工智能入門](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [網絡安全入門](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Web開發入門](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [物聯網入門](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR開發入門](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [掌握GitHub Copilot進行AI配對編程](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [掌握GitHub Copilot進行C#/.NET開發](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [選擇您的Copilot冒險](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。