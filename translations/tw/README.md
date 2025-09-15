<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e73444e4fc8f1931ac3979dbd7785e2",
  "translation_date": "2025-09-15T16:38:42+00:00",
  "source_file": "README.md",
  "language_code": "tw"
}
-->
# EdgeAI 初學者指南

![課程封面圖片](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.tw.png)

[![GitHub 貢獻者](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)  
[![GitHub 問題](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)  
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)  
[![歡迎提交 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  

[![GitHub 追蹤者](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)  
[![GitHub 分叉](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
[![GitHub 星星](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)  

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

按照以下步驟開始使用這些資源：

1. **分叉此倉庫**：點擊 [![GitHub 分叉](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
2. **克隆此倉庫**：`git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**加入 Azure AI Foundry Discord，與專家和開發者交流**](https://discord.com/invite/ByRwuEEgH4)  

### 🌐 多語言支持

#### 通過 GitHub Action 支持（自動化且始終保持最新）

[法語](../fr/README.md) | [西班牙語](../es/README.md) | [中文（簡體）](../zh/README.md) | [中文（繁體，澳門）](../mo/README.md) | [中文（繁體，香港）](../hk/README.md) | [中文（繁體，台灣）](./README.md) | [日語](../ja/README.md) | [韓語](../ko/README.md)  
**如果希望支持更多語言，請參考 [此處](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## 簡介

歡迎來到 **EdgeAI 初學者指南**——這是一個全面探索邊緣人工智慧世界的旅程。本課程將強大的 AI 能力與邊緣設備上的實際部署相結合，幫助您直接在數據生成和決策需要的地方發揮 AI 的潛力。

### 您將掌握的內容

本課程涵蓋從基礎概念到生產級實現的全過程，包括：
- **小型語言模型（SLMs）**，針對邊緣部署進行優化  
- **硬體感知優化**，適用於多種平台  
- **隱私保護的即時推理**  
- **企業應用的生產部署策略**  

### 為什麼邊緣 AI 很重要

邊緣 AI 是一種解決現代關鍵挑戰的全新模式：
- **隱私與安全**：在本地處理敏感數據，避免雲端暴露  
- **即時性能**：消除網絡延遲，適用於時間敏感的應用  
- **成本效益**：減少帶寬和雲計算開支  
- **穩健運行**：在網絡中斷時仍能保持功能  
- **合規性**：滿足數據主權要求  

### 邊緣 AI

邊緣 AI 是指在硬體上本地運行 AI 算法和語言模型——靠近數據生成的地方——而不依賴雲端資源進行推理。它能降低延遲、增強隱私並實現即時決策。

### 核心原則：
- **設備上的推理**：AI 模型在邊緣設備（手機、路由器、微控制器、工業 PC）上運行  
- **離線能力**：無需持續的網絡連接即可運行  
- **低延遲**：適合即時系統的快速響應  
- **數據主權**：本地保存敏感數據，提升安全性和合規性  

### 小型語言模型（SLMs）

像 Phi-4、Mistral-7B 和 Gemma 這樣的 SLMs 是大型語言模型的優化版本——通過訓練或蒸餾實現：
- **減少內存佔用**：有效利用邊緣設備有限的內存  
- **降低計算需求**：針對 CPU 和邊緣 GPU 性能進行優化  
- **更快的啟動時間**：快速初始化以支持響應式應用  

它們在以下場景中解鎖了強大的自然語言處理能力：
- **嵌入式系統**：物聯網設備和工業控制器  
- **移動設備**：支持離線功能的智能手機和平板電腦  
- **物聯網設備**：資源有限的傳感器和智能設備  
- **邊緣伺服器**：具有有限 GPU 資源的本地處理單元  
- **個人電腦**：桌面和筆記本電腦的部署場景  

## 課程架構

### [模組 01：邊緣 AI 基礎與轉型](./Module01/README.md)  
**主題**：邊緣 AI 部署的變革性轉變  

#### 章節結構：
- [**第一節：邊緣 AI 基礎**](./Module01/01.EdgeAIFundamentals.md)  
  - 傳統雲端 AI 與邊緣 AI 的比較  
  - 邊緣計算的挑戰與限制  
  - 關鍵技術：模型量化、壓縮優化、小型語言模型（SLMs）  
  - 硬體加速：NPUs、GPU 優化、CPU 優化  
  - 優勢：隱私安全、低延遲、離線能力、成本效益  

- [**第二節：實際案例研究**](./Module01/02.RealWorldCaseStudies.md)  
  - Microsoft Phi & Mu 模型生態系統  
  - 日本航空 AI 報告系統案例研究  
  - 市場影響與未來方向  
  - 部署考量與最佳實踐  

- [**第三節：實踐實現指南**](./Module01/03.PracticalImplementationGuide.md)  
  - 開發環境設置（Python 3.10+、.NET 8+）  
  - 硬體需求與推薦配置  
  - 核心模型資源  
  - 量化與優化工具（Llama.cpp、Microsoft Olive、Apple MLX）  
  - 評估與驗證清單  

- [**第四節：邊緣 AI 部署硬體平台**](./Module01/04.EdgeDeployment.md)  
  - 邊緣 AI 部署考量與需求  
  - Intel 邊緣 AI 硬體與優化技術  
  - Qualcomm 移動與嵌入式系統 AI 解決方案  
  - NVIDIA Jetson 與邊緣計算平台  
  - Windows AI PC 平台與 NPU 加速  
  - 硬體特定的優化策略  

---

### [模組 02：小型語言模型基礎](./Module02/README.md)  
**主題**：SLM 理論原則、實現策略與生產部署  

#### 章節結構：
- [**第一節：Microsoft Phi 模型家族基礎**](./Module02/01.PhiFamily.md)  
  - 設計理念演變（Phi-1 至 Phi-4）  
  - 以效率為先的架構設計  
  - 專業能力（推理、多模態、邊緣部署）  

- [**第二節：Qwen 模型家族基礎**](./Module02/02.QwenFamily.md)  
  - 開源卓越（Qwen 1.0 至 Qwen3）——可通過 Hugging Face 獲得  
  - 具有思考模式能力的高級推理架構  
  - 可擴展部署選項（0.5B-235B 參數）  

- [**第三節：Gemma 模型家族基礎**](./Module02/03.GemmaFamily.md)  
  - 以研究驅動的創新（Gemma 3 & 3n）  
  - 多模態卓越  
  - 移動優先架構  

- [**第四節：BitNET 模型家族基礎**](./Module02/04.BitNETFamily.md)  
  - 革命性的量化技術（1.58-bit）  
  - 專業推理框架：https://github.com/microsoft/BitNet  
  - 通過極端效率實現可持續 AI 領導力  

- [**第五節：Microsoft Mu 模型基礎**](./Module02/05.mumodel.md)  
  - 內置於 Windows 11 的設備優先架構  
  - 與 Windows 11 設置的系統集成  
  - 隱私保護的離線操作  

- [**第六節：Phi-Silica 基礎**](./Module02/06.phisilica.md)  
  - 內置於 Windows 11 Copilot+ PC 的 NPU 優化架構  
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
  - 精度分類框架（超低、低、中等精度）  
  - GGUF 和 ONNX 格式的優勢與使用場景  
  - 量化對運行效率的好處  
  - 性能基準與內存佔用比較  

- [**第二節：Llama.cpp 實現指南**](./Module04/02.Llamacpp.md)  
  - 跨平台安裝（Windows、macOS、Linux）  
  - GGUF 格式轉換與量化級別（Q2_K 至 Q8_0）  
  - 硬體加速（CUDA、Metal、OpenCL、Vulkan）  
  - Python 集成與 REST API 部署  

- [**第三節：Microsoft Olive 優化套件**](./Module04/03.MicrosoftOlive.md)  
  - 具有 40+ 內置組件的硬體感知模型優化  
  - 動態與靜態量化的自動優化  
  - 與 Azure ML 工作流程的企業集成  
  - 支持的流行模型（Llama、Phi、選定 Qwen 模型、Gemma）  

- [**第四節：OpenVINO 工具包優化套件**](./Module04/04.openvino.md)  
  - Intel 的開源工具包，用於跨平台 AI 部署  
  - 神經網絡壓縮框架（NNCF）進行高級優化  
  - OpenVINO GenAI 用於大型語言模型部署  
  - CPU、GPU、VPU 和 AI 加速器的硬體加速  

- [**第五節：Apple MLX 框架深度解析**](./Module04/05.AppleMLX.md)  
  - Apple Silicon 的統一內存架構  
  - 支持 LLaMA、Mistral、Phi-3、選定 Qwen 模型  
  - LoRA 微調與模型定制  
  - 與 Hugging Face 集成，支持 4-bit/8-bit 量化  

- [**第六節：邊緣 AI 開發工作流程綜合**](./Module04/06.workflow-synthesis.md)  
  - 整合多種優化框架的統一工作流程架構  
  - 框架選擇決策樹與性能權衡分析  
  - 生產準備驗證與全面部署策略  
  - 面向新興硬體與模型架構的未來保障策略  

---

### [模組 05：SLMOps - 小型語言模型運營](./Module05/README.md)  
**主題**：從蒸餾到生產部署的完整 SLM 運營生命周期  

#### 章節結構：
- [**第一節：SLMOps 簡介**](./Module05/01.IntroduceSLMOps.md)  
  - SLMOps 在 AI 運營中的模式轉變  
  - 成本效益與隱私優先架構  
  - 戰略商業影響與競爭優勢  
  - 實際實現中的挑戰與解決方案  
- [**第 2 節：模型蒸餾 - 從理論到實踐**](./Module05/02.SLMOps-Distillation.md)
  - 從教師模型向學生模型進行知識轉移
  - 實現兩階段蒸餾過程
  - Azure ML 蒸餾工作流程及實際範例
  - 推理時間減少 85%，準確率保留 92%

- [**第 3 節：微調 - 為特定任務定制模型**](./Module05/03.SLMOps-Finetuing.md)
  - 參數高效微調（PEFT）技術
  - LoRA 和 QLoRA 高級方法
  - Microsoft Olive 微調實現
  - 多適配器訓練及超參數優化

- [**第 4 節：部署 - 生產就緒的實現**](./Module05/04.SLMOps.Deployment.md)
  - 模型轉換及量化以適應生產需求
  - Foundry Local 部署配置
  - 性能基準測試及質量驗證
  - 尺寸減少 75%，並進行生產監控

---

### [模組 06：SLM Agentic 系統 - AI 代理及函數調用](./Module06/README.md)
**主題**：SLM Agentic 系統的實現，從基礎到高級函數調用及模型上下文協議（MCP）整合

#### 章節結構：
- [**第 1 節：AI 代理及小型語言模型基礎**](./Module06/01.IntroduceAgent.md)
  - 代理分類框架（反射型、基於模型、基於目標、學習型代理）
  - SLM 基礎及優化策略（GGUF、量化、邊緣框架）
  - SLM 與 LLM 的權衡分析（成本降低 10-30 倍，任務有效性達 70-80%）
  - 使用 Ollama、VLLM 和 Microsoft 邊緣解決方案進行實際部署

- [**第 2 節：小型語言模型中的函數調用**](./Module06/02.FunctionCalling.md)
  - 系統化工作流程實現（意圖檢測、JSON 輸出、外部執行）
  - 平台特定實現（Phi-4-mini、選定的 Qwen 模型、Microsoft Foundry Local）
  - 高級範例（多代理協作、動態工具選擇）
  - 生產考量（速率限制、審計記錄、安全措施）

- [**第 3 節：模型上下文協議（MCP）整合**](./Module06/03.IntroduceMCP.md)
  - 協議架構及分層系統設計
  - 多後端支持（Ollama 用於開發，vLLM 用於生產）
  - 連接協議（STDIO 和 SSE 模式）
  - 實際應用（網頁自動化、數據處理、API 整合）

---

### [模組 07：EdgeAI 實現範例](./Module07/README.md)
**主題**：跨多平台及框架的全面 EdgeAI 實現

#### 章節結構：
- [**Visual Studio Code 的 AI 工具包**](./Module07/aitoolkit.md)
  - 在 VS Code 中的全面 Edge AI 開發環境
  - 用於邊緣部署的模型目錄及發現
  - 本地測試、優化及代理開發工作流程
  - 用於邊緣場景的性能監控及評估

- [**Windows EdgeAI 開發指南**](./Module07/windowdeveloper.md)
  - Windows AI Foundry 平台的全面概述
  - Phi Silica API 用於高效 NPU 推理
  - 用於圖像處理及 OCR 的計算機視覺 API
  - Foundry Local CLI 用於本地開發及測試

- [**NVIDIA Jetson Orin Nano 的 EdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 信用卡大小的設備提供 67 TOPS AI 性能
  - 支持生成式 AI 模型（視覺變換器、LLM、視覺語言模型）
  - 應用於機器人、無人機、智能攝像頭、自主設備
  - 價格僅 $249 的平台，推動 AI 開發普及化

- [**使用 .NET MAUI 和 ONNX Runtime GenAI 的移動應用 EdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 使用單一 C# 代碼庫的跨平台移動 AI
  - 硬件加速支持（CPU、GPU、移動 AI 處理器）
  - 平台特定優化（iOS 的 CoreML，Android 的 NNAPI）
  - 完整的生成式 AI 循環實現

- [**Azure 中的小型語言模型引擎的 EdgeAI**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - 雲-邊緣混合部署架構
  - Azure AI 服務與 ONNX Runtime 的整合
  - 企業級部署及持續模型管理
  - 用於智能文檔處理的混合 AI 工作流程

- [**使用 Windows ML 的 EdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Windows AI Foundry 基礎，用於高效的設備端推理
  - 通用硬件支持（AMD、Intel、NVIDIA、Qualcomm 芯片）
  - 自動硬件抽象及優化
  - 用於多樣化 Windows 硬件生態系統的統一框架

- [**使用 Foundry Local 應用的 EdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - 注重隱私的 RAG 實現，使用本地資源
  - Phi-3 語言模型與語義搜索整合（僅限 Phi 模型）
  - 本地向量數據庫支持（SQLite、Qdrant）
  - 數據主權及離線操作能力

## 課程學習目標

完成這門全面的 EdgeAI 課程後，您將具備設計、實現及部署生產就緒 EdgeAI 解決方案的專業技能。我們的結構化方法確保您掌握理論基礎及實際操作技能。

### 技術能力

**基礎知識**
- 理解基於雲端與邊緣的 AI 架構的基本差異
- 掌握模型量化、壓縮及優化的原則，適用於資源受限環境
- 理解硬件加速選項（NPU、GPU、CPU）及其部署影響

**實現技能**
- 在多樣化邊緣平台（移動、嵌入式、物聯網、邊緣服務器）上部署小型語言模型
- 應用優化框架，包括 Llama.cpp、Microsoft Olive、ONNX Runtime 和 Apple MLX
- 實現具有亞秒級響應要求的實時推理系統

**生產專業知識**
- 設計可擴展的 EdgeAI 架構，用於企業應用
- 實施已部署系統的監控、維護及更新策略
- 應用隱私保護的 EdgeAI 安全最佳實踐

### 策略能力

**決策框架**
- 評估 EdgeAI 機會並識別適合的業務應用場景
- 衡量模型準確性、推理速度、功耗及硬件成本之間的權衡
- 根據特定部署限制選擇合適的 SLM 家族及配置

**系統架構**
- 設計與現有基礎設施整合的端到端 EdgeAI 解決方案
- 規劃混合邊緣-雲架構以實現最佳性能及成本效率
- 實現用於實時 AI 應用的數據流及處理管道

### 行業應用

**實際部署場景**
- **製造業**：質量控制系統、預測性維護及流程優化
- **醫療保健**：隱私保護的診斷工具及患者監測系統
- **交通運輸**：自主車輛決策及交通管理
- **智慧城市**：智能基礎設施及資源管理系統
- **消費電子**：AI 驅動的移動應用及智能家居設備

## 學習成果概述

### 模組 01 學習成果：
- 理解雲端與邊緣 AI 架構的基本差異
- 掌握邊緣部署的核心優化技術
- 認識實際應用及成功案例
- 獲得實現 EdgeAI 解決方案的實際技能

### 模組 02 學習成果：
- 深入理解不同 SLM 設計理念及其部署影響
- 掌握基於計算限制及性能需求的策略性決策能力
- 理解部署靈活性權衡
- 擁有面向未來的高效 AI 架構洞察力

### 模組 03 學習成果：
- 策略性模型選擇能力
- 優化技術精通
- 部署靈活性精通
- 生產就緒配置能力

### 模組 04 學習成果：
- 深入理解量化邊界及實際應用
- 掌握多種優化框架（Llama.cpp、Olive、OpenVINO、MLX）的實際操作
- 精通使用 OpenVINO 和 NNCF 進行 Intel 硬件優化
- 跨多平台選擇硬件感知優化能力
- 生產部署技能，用於跨平台邊緣計算環境
- 策略性框架選擇及工作流程綜合能力，用於最佳 Edge AI 解決方案

### 模組 05 學習成果：
- 掌握 SLMOps 範式及運行原則
- 實現模型蒸餾，用於知識轉移及效率優化
- 應用微調技術，用於領域特定模型定制
- 部署生產就緒的 SLM 解決方案，並實施監控及維護策略

### 模組 06 學習成果：
- 理解 AI 代理及小型語言模型架構的基礎概念
- 掌握跨多平台及框架的函數調用實現
- 整合模型上下文協議（MCP），用於標準化外部工具交互
- 構建高級代理系統，減少人工干預需求

### 模組 07 學習成果：
- 精通 Visual Studio Code 的 AI 工具包，用於全面的 Edge AI 開發工作流程
- 獲得 Windows AI Foundry 平台及 NPU 優化策略的專業知識
- 獲得多樣化 EdgeAI 平台及實現策略的實際操作經驗
- 精通跨 NVIDIA、移動、Azure 和 Windows 平台的硬件特定優化技術
- 理解性能、成本及隱私要求之間的部署權衡
- 開發實際技能，用於構建跨不同生態系統的真實世界 EdgeAI 應用

## 預期課程成果

成功完成本課程後，您將具備知識、技能及信心，能在專業環境中領導 EdgeAI 項目。

### 職業準備

**技術領導力**
- **解決方案架構**：設計滿足企業需求的全面 EdgeAI 系統
- **性能優化**：在準確性、速度及資源消耗之間實現最佳平衡
- **跨平台部署**：在 Windows、Linux、移動及嵌入式平台上實現解決方案
- **生產運營**：以企業級可靠性維護及擴展 EdgeAI 系統

**行業專業知識**
- **技術評估**：評估並推薦適合特定業務挑戰的 EdgeAI 解決方案
- **實施規劃**：為 EdgeAI 項目制定現實的時間表及資源需求
- **風險管理**：識別並減輕 EdgeAI 部署中的技術及運營風險
- **投資回報優化**：展示 EdgeAI 實現的可衡量業務價值

### 職業發展機會

**專業角色**
- EdgeAI 解決方案架構師
- 機器學習工程師（邊緣專業化）
- 物聯網 AI 開發者
- 移動 AI 應用開發者
- 企業 AI 顧問

**行業領域**
- 智能製造及工業 4.0
- 自主車輛及交通運輸
- 醫療技術及醫療設備
- 金融技術及安全
- 消費電子及移動應用

### 認證及驗證

**作品集開發**
- 完成端到端 EdgeAI 項目，展示實際能力
- 在多個硬件平台上部署生產就緒解決方案
- 記錄實現的優化策略及性能改進

**持續學習路徑**
- 為高級 AI 專業化奠定基礎
- 為雲-邊緣混合架構做好準備
- 成為新興 AI 技術及框架的入口

本課程將您定位於 AI 技術部署的前沿，智能能力無縫整合到現代生活所需的設備及系統中。

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
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md (This file)
├── SECURITY.md
├── STUDY_GUIDE.md
└── SUPPORT.md
```

## 課程特色

- **漸進式學習**：從基礎概念逐步進階到高級部署
- **理論與實踐結合**：每個模組均包含理論基礎及實際操作
- **真實案例研究**：基於 Microsoft、阿里巴巴、Google 等的實際案例
- **動手實踐**：完整配置文件、API 測試程序及部署腳本
- **性能基準**：詳細比較推理速度、內存使用及資源需求
- **企業級考量**：安全實踐、合規框架及數據保護策略

## 入門指南

推薦學習路徑：
1. 從 **模組 01** 開始，建立 EdgeAI 的基礎理解
2. 進入 **模組 02**，深入了解各種 SLM 模型家族
3. 學習 **模組 03**，掌握實際部署技能
4. 繼續 **模組 04**，進行高級模型優化、格式轉換及框架綜合
5. 完成 **模組 05**，掌握 SLMOps 用於生產就緒的實現
6. 探索 **模組 06**，理解 SLM Agentic 系統及函數調用能力
7. 最後完成 **模組 07**，獲得 AI 工具包及多樣化 EdgeAI 實現範例的實際經驗

每個模組均設計為獨立完整，但按順序學習將提供最佳效果。

## 學習指南

提供全面的 [學習指南](STUDY_GUIDE.md)，幫助您最大化學習體驗。學習指南包括：

- **結構化學習路徑**：優化的課程完成時間表（20 小時）
- **時間分配建議**：具體建議，用於平衡閱讀、練習及項目
- **關鍵概念重點**：每個模組的優先學習目標
- **自我評估工具**：測試理解的問題及練習
- **迷你項目創意**：加強學習的實際應用

學習指南設計為適應密集學習（1 周）及兼職學習（3 周），即使您僅能投入 10 小時，也有清晰的時間分配指導。

---
**EdgeAI 的未來在於持續改進模型架構、量化技術以及部署策略，這些策略優先考慮效率和專業化，而非通用能力。那些能夠接受這種範式轉變的組織，將能夠充分利用 AI 的變革潛力，同時保持對其數據和運營的掌控。**

## 其他課程

我們的團隊還製作了其他課程！快來看看：

- [MCP 初學者指南](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents 初學者指南](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [使用 .NET 的生成式 AI 初學者指南](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [使用 JavaScript 的生成式 AI 初學者指南](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [生成式 AI 初學者指南](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML 初學者指南](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [數據科學初學者指南](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI 初學者指南](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [網絡安全初學者指南](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Web 開發初學者指南](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT 初學者指南](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR 開發初學者指南](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [精通 GitHub Copilot 的 AI 配對編程](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [精通 GitHub Copilot 的 C#/.NET 開發](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [選擇你的 Copilot 冒險](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。