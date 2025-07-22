<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0f8da2fde263594c60dab5c40e0fffc",
  "translation_date": "2025-07-22T07:47:27+00:00",
  "source_file": "README.md",
  "language_code": "hk"
}
-->
# EdgeAI 初學者指南

深入探索 Edge AI 技術的教育旅程，分為三個全面的模組：EdgeAI 基礎、輕量語言模型基礎，以及實際部署策略。本課程從基本概念到高階實作，涵蓋真實案例研究、實作練習，以及展示如何有效地在邊緣設備上直接運行 AI 模型的部署範例，以提升隱私、降低延遲並提高效率。

![課程封面圖片](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.hk.png)

[![GitHub 貢獻者](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)  
[![GitHub 問題](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)  
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)  
[![歡迎 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  

[![GitHub 觀察者](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)  
[![GitHub 分叉](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
[![GitHub 星標](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)  

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

按照以下步驟開始使用這些資源：  
1. **分叉此倉庫**：點擊 [![GitHub 分叉](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)  
2. **克隆此倉庫**：`git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**加入 Azure AI Foundry Discord，與專家和開發者交流**](https://discord.com/invite/ByRwuEEgH4)  

### 🌐 多語言支持

#### 通過 GitHub Action 支持（自動化且始終保持最新）

[法文](../fr/README.md) | [西班牙文](../es/README.md) | [中文（簡體）](../zh/README.md) | [中文（繁體，澳門）](../mo/README.md) | [中文（繁體，香港）](./README.md) | [中文（繁體，台灣）](../tw/README.md) | [日文](../ja/README.md) | [韓文](../ko/README.md) |  

歡迎來到 EdgeAI 初學者指南，這裡結合了語言模型的強大功能與本地設備的高效運行。本課程介紹了如何在邊緣硬件（如智能手機、IoT 板卡和小型伺服器）上直接運行小型、優化的語言模型（SLMs），無需依賴雲端。您將探索即時、注重隱私的 AI 推理如何通過輕量化部署，徹底改變智能家居、工業監控和離線應用，實現速度、安全性和模組化的平衡。

**Edge AI**

Edge AI 是指在本地硬件上運行 AI 演算法和語言模型，靠近數據生成的地方，無需依賴雲端資源進行推理。它能降低延遲、增強隱私，並實現即時決策。

核心原則：
- **設備端推理**：AI 模型在邊緣設備（如手機、路由器、微控制器、工業 PC）上運行。
- **離線能力**：無需持續的網絡連接即可運行。
- **低延遲**：適合即時系統的快速響應。
- **數據主權**：將敏感數據保留在本地，提升安全性和合規性。

**小型語言模型（SLMs）**

像 Phi-4、Mistral-7B 或 Gemma 這樣的 SLM 是大型語言模型（LLMs）的優化版本，經過訓練或蒸餾以實現：
- 減少內存佔用
- 降低計算需求
- 更快的啟動時間

它們在以下限制條件下釋放了強大的自然語言處理能力：
- 嵌入式系統
- 移動設備
- IoT 設備
- GPU 資源有限的邊緣伺服器
- 個人電腦

## 課程架構

### [模組 01：EdgeAI 基礎與轉型](./Module01/README.md)
**主題**：邊緣 AI 部署的變革性轉變

#### 章節結構：
- [**第一節：EdgeAI 基礎**](./Module01/01.EdgeAIFundamentals.md)
  - 傳統雲端 AI 與邊緣 AI 的比較
  - 邊緣計算的挑戰與限制
  - 關鍵技術：模型量化、壓縮優化、小型語言模型（SLMs）
  - 硬件加速：NPU、GPU 優化、CPU 優化
  - 優勢：隱私安全、低延遲、離線能力、成本效益

- [**第二節：真實案例研究**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi & Mu 模型生態系統
    - Phi Silica：Windows AI 集成
    - Mu 模型：特定任務的微型語言模型
  - 日本航空 AI 報告系統案例研究
  - 市場影響與未來方向
  - 部署考量與最佳實踐

- [**第三節：實用實施指南**](./Module01/03.PracticalImplementationGuide.md)
  - 開發環境設置（Python 3.10+，.NET 8+）
  - 硬件需求與推薦配置
  - 核心模型資源
  - 量化與優化工具（Llama.cpp、Microsoft Olive、Apple MLX）
  - 評估與驗證清單

- [**第四節：Edge AI 部署硬件平台**](./Module01/04.EdgeDeployment.md)
  - 邊緣 AI 部署的考量與需求
  - Intel 邊緣 AI 硬件與優化技術
  - Qualcomm 移動與嵌入式系統的 AI 解決方案
  - NVIDIA Jetson 與邊緣計算平台
  - 配備 NPU 加速的 Windows AI PC 平台
  - 硬件特定的優化策略

---

### [模組 02：小型語言模型基礎](./Module02/README.md)
**主題**：SLM 理論原則、實施策略與生產部署

#### 章節結構：
- [**第一節：Microsoft Phi 模型家族基礎**](./Module02/01.PhiFamily.md)
  - 設計理念的演變（Phi-1 至 Phi-4）
  - 以效率為核心的架構設計
  - 專業能力（推理、多模態、邊緣部署）

- [**第二節：Qwen 模型家族基礎**](./Module02/02.QwenFamily.md)
  - 開源卓越（Qwen 1.0 至 Qwen3）- 可通過 Hugging Face 獲取
  - 具備思考模式能力的高級推理架構
  - 可擴展的部署選項（0.5B-235B 參數）

- [**第三節：Gemma 模型家族基礎**](./Module02/03.GemmaFamily.md)
  - 以研究為驅動的創新（Gemma 3 & 3n）
  - 多模態卓越
  - 移動優先架構

- [**第四節：BitNET 模型家族基礎**](./Module02/04.BitNETFamily.md)
  - 革命性的量化技術（1.58-bit）
  - 專用推理框架：https://github.com/microsoft/BitNet
  - 通過極致效率實現可持續 AI 領導地位

- [**第五節：Microsoft Mu 模型基礎**](./Module02/05.mumodel.md)
  - 為設備優化的架構，內建於 Windows 11
  - 與 Windows 11 設定的系統集成
  - 保護隱私的離線操作

- [**第六節：Phi-Silica 基礎**](./Module02/06.phisilica.md)
  - 為 NPU 優化的架構，內建於 Windows 11 Copilot+ PC
  - 卓越效率（650 tokens/second，功耗僅 1.5W）
  - 與 Windows App SDK 的開發者集成

---

### [模組 03：小型語言模型部署](./Module03/README.md)
**主題**：完整的 SLM 生命周期部署，從理論到生產環境

#### 章節結構：
- [**第一節：SLM 高階學習**](./Module03/01.SLMAdvancedLearning.md)
  - 參數分類框架（微型 SLM 100M-1.4B，中型 SLM 14B-30B）
  - 高級優化技術（量化方法，BitNET 1-bit 量化）
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
  - 與 Azure ML 工作流程的企業集成
  - 支持的熱門模型（Llama、Phi、選定的 Qwen 模型、Gemma）

- [**第四節：Apple MLX 框架深入探討**](./Module04/04.AppleMLX.md)
  - Apple Silicon 的統一內存架構
  - 支持 LLaMA、Mistral、Phi-3、選定的 Qwen 模型
  - LoRA 微調與模型定制
  - 與 Hugging Face 的 4-bit/8-bit 量化集成

---

### [模組 05：SLMOps - 小型語言模型運營](./Module05/README.md)
**主題**：從蒸餾到生產部署的完整 SLM 生命周期運營

#### 章節結構：
- [**第一節：SLMOps 簡介**](./Module05/01.IntroduceSLMOps.md)
  - SLMOps 在 AI 運營中的範式轉變
  - 成本效益與隱私優先架構
  - 戰略商業影響與競爭優勢
  - 真實實施挑戰與解決方案

- [**第二節：模型蒸餾 - 從理論到實踐**](./Module05/02.SLMOps-Distillation.md)
  - 從教師模型到學生模型的知識轉移
  - 兩階段蒸餾過程實施
  - Azure ML 蒸餾工作流程與實際範例
  - 推理時間減少 85%，準確率保留 92%

- [**第三節：微調 - 為特定任務定制模型**](./Module05/03.SLMOps-Finetuing.md)
  - 參數高效微調（PEFT）技術
  - LoRA 與 QLoRA 高級方法
  - Microsoft Olive 微調實現
  - 多適配器訓練與超參數優化

- [**第四節：部署 - 生產就緒實現**](./Module05/04.SLMOps.Deployment.md)
  - 生產環境的模型轉換與量化
  - Foundry Local 部署配置
  - 性能基準測試與質量驗證
  - 減少 75% 的模型大小並進行生產監控

---

### [模組 06：SLM Agentic 系統 - AI 代理與功能調用](./Module06/README.md)
**主題**：從基礎到高級功能調用與模型上下文協議集成的 SLM Agentic 系統實施

#### 章節結構：
- [**第一節：AI 代理與小型語言模型基礎**](./Module06/01.IntroduceAgent.md)
- 智能代理分類框架（反射型、基於模型、基於目標、學習型代理）
- SLM 基礎知識及優化策略（GGUF、量化、邊緣框架）
- SLM 與 LLM 的權衡分析（成本降低 10-30 倍，任務效能達 70-80%）
- 使用 Ollama、VLLM 和 Microsoft 邊緣解決方案進行實際部署

- [**第二部分：小型語言模型中的函數調用**](./Module06/02.FunctionCalling.md)
  - 系統化工作流程實現（意圖檢測、JSON 輸出、外部執行）
  - 平台特定實現（Phi-4-mini、選定的 Qwen 模型、Microsoft Foundry Local）
  - 高級示例（多代理協作、動態工具選擇）
  - 生產考量（速率限制、審計日誌、安全措施）

- [**第三部分：模型上下文協議（MCP）整合**](./Module06/03.IntroduceMCP.md)
  - 協議架構及分層系統設計
  - 多後端支持（Ollama 用於開發，vLLM 用於生產）
  - 連接協議（STDIO 和 SSE 模式）
  - 實際應用（網頁自動化、數據處理、API 整合）

---

### [模組 07：EdgeAI 實施範例](./Module07/README.md)
**主題**：跨多平台和框架的全面 EdgeAI 實施

#### 章節結構：
- [**NVIDIA Jetson Orin Nano 的 EdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 信用卡大小的設備提供 67 TOPS AI 性能
  - 支持生成式 AI 模型（視覺變壓器、LLM、視覺語言模型）
  - 應用於機器人、無人機、智能攝像頭、自主設備
  - 價格實惠的 $249 平台，推動 AI 開發普及化

- [**使用 .NET MAUI 和 ONNX Runtime GenAI 的移動應用 EdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 單一 C# 代碼庫的跨平台移動 AI
  - 硬件加速支持（CPU、GPU、移動 AI 處理器）
  - 平台特定優化（iOS 的 CoreML，Android 的 NNAPI）
  - 完整的生成式 AI 循環實現

- [**使用小型語言模型引擎的 Azure EdgeAI**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - 雲端與邊緣混合部署架構
  - Azure AI 服務與 ONNX Runtime 整合
  - 企業級部署及持續模型管理
  - 用於智能文檔處理的混合 AI 工作流

- [**使用 Windows ML 的 EdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Windows AI Foundry 提供高效的設備端推理基礎
  - 通用硬件支持（AMD、Intel、NVIDIA、Qualcomm 芯片）
  - 自動硬件抽象及優化
  - 適用於多樣化 Windows 硬件生態系統的統一框架

- [**使用 Foundry Local 應用的 EdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - 注重隱私的 RAG 實現，使用本地資源
  - Phi-3 語言模型與語義搜索整合（僅限 Phi 模型）
  - 支持本地向量數據庫（SQLite、Qdrant）
  - 數據主權及離線操作能力

## 學習成果概覽

### 模組 01 學習成果：
- 理解雲端與邊緣 AI 架構的基本差異
- 掌握邊緣部署的核心優化技術
- 認識實際應用及成功案例
- 獲得實施 EdgeAI 解決方案的實用技能

### 模組 02 學習成果：
- 深入理解不同 SLM 設計理念及其部署影響
- 掌握基於計算限制和性能需求的戰略決策能力
- 理解部署靈活性的權衡
- 擁有面向未來的高效 AI 架構洞察力

### 模組 03 學習成果：
- 戰略模型選擇能力
- 優化技術掌握
- 部署靈活性掌握
- 生產就緒配置能力

### 模組 04 學習成果：
- 深入理解量化邊界及實際應用
- 實際操作多種優化框架（Llama.cpp、Olive、MLX）
- 硬件感知的優化選擇能力
- 跨平台邊緣計算環境的生產部署技能

### 模組 05 學習成果：
- 掌握 SLMOps 範式及運營原則
- 實施模型蒸餾以進行知識轉移及效率優化
- 應用微調技術進行領域特定模型定制
- 部署生產就緒的 SLM 解決方案，並進行監控和維護

### 模組 06 學習成果：
- 理解 AI 代理及小型語言模型架構的基礎概念
- 掌握跨多平台和框架的函數調用實現
- 整合模型上下文協議（MCP），實現標準化的外部工具交互
- 構建高級代理系統，減少人工干預需求

### 模組 07 學習成果：
- 獲得多樣化 EdgeAI 平台及實施策略的實際操作經驗
- 掌握針對 NVIDIA、移動、Azure 和 Windows 平台的硬件特定優化技術
- 理解性能、成本及隱私需求之間的部署權衡
- 開發跨不同生態系統的實際 EdgeAI 應用技能

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
- **理論與實踐結合**：每個模組包含理論基礎和實際操作
- **真實案例研究**：基於 Microsoft、阿里巴巴、Google 等的實際案例
- **動手操作**：完整配置文件、API 測試流程及部署腳本
- **性能基準**：詳細比較推理速度、內存使用及資源需求
- **企業級考量**：安全實踐、合規框架及數據保護策略

## 入門指南

推薦學習路徑：
1. 從 **模組 01** 開始，建立 EdgeAI 的基礎理解
2. 進入 **模組 02**，深入了解各種 SLM 模型家族
3. 學習 **模組 03**，掌握實際部署技能
4. 繼續 **模組 04**，進行高級模型優化及格式轉換
5. 完成 **模組 05**，掌握 SLMOps，實現生產就緒的應用
6. 探索 **模組 06**，理解 SLM 代理系統及函數調用能力
7. 最後完成 **模組 07**，獲得多樣化 EdgeAI 實施範例的實際操作經驗

每個模組都設計為獨立完整，但按順序學習將獲得最佳效果。

## 學習指南

提供全面的 [學習指南](STUDY_GUIDE.md)，幫助您最大化學習效果。學習指南包括：

- **結構化學習路徑**：優化的課程完成時間表（20 小時）
- **時間分配指導**：平衡閱讀、練習和項目的具體建議
- **關鍵概念重點**：每個模組的優先學習目標
- **自我評估工具**：測試理解的問題和練習
- **迷你項目創意**：加強學習的實際應用

學習指南適合密集學習（1 周）和兼職學習（3 周），即使您只能投入 10 小時，也有清晰的時間分配指導。

---

**EdgeAI 的未來在於持續改進模型架構、量化技術及部署策略，優先考慮效率和專業化，而非通用能力。採用這一範式轉變的組織將能充分利用 AI 的變革潛力，同時保持對數據和運營的控制。**

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
- [掌握 GitHub Copilot 用於 AI 配對編程](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [掌握 GitHub Copilot 用於 C#/.NET 開發者](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [選擇您的 Copilot 冒險](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。