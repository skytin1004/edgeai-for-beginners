<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c817161ba08864340737d623f761b9ae",
  "translation_date": "2025-09-17T10:26:49+00:00",
  "source_file": "README.md",
  "language_code": "tw"
}
-->
# EdgeAI 初學者指南

![課程封面圖片](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.tw.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

按照以下步驟開始使用這些資源：

1. **Fork 儲存庫**：點擊 [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clone 儲存庫**：`git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord，與專家和開發者交流**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 多語言支援

#### 透過 GitHub Action 支援（自動化且始終保持最新）

[阿拉伯文](../ar/README.md) | [孟加拉文](../bn/README.md) | [保加利亞文](../bg/README.md) | [緬甸文](../my/README.md) | [中文（簡體）](../zh/README.md) | [中文（繁體，香港）](../hk/README.md) | [中文（繁體，澳門）](../mo/README.md) | [中文（繁體，台灣）](./README.md) | [克羅埃西亞文](../hr/README.md) | [捷克文](../cs/README.md) | [丹麥文](../da/README.md) | [荷蘭文](../nl/README.md) | [芬蘭文](../fi/README.md) | [法文](../fr/README.md) | [德文](../de/README.md) | [希臘文](../el/README.md) | [希伯來文](../he/README.md) | [印地文](../hi/README.md) | [匈牙利文](../hu/README.md) | [印尼文](../id/README.md) | [義大利文](../it/README.md) | [日文](../ja/README.md) | [韓文](../ko/README.md) | [馬來文](../ms/README.md) | [馬拉地文](../mr/README.md) | [尼泊爾文](../ne/README.md) | [挪威文](../no/README.md) | [波斯文](../fa/README.md) | [波蘭文](../pl/README.md) | [葡萄牙文（巴西）](../br/README.md) | [葡萄牙文（葡萄牙）](../pt/README.md) | [旁遮普文](../pa/README.md) | [羅馬尼亞文](../ro/README.md) | [俄文](../ru/README.md) | [塞爾維亞文（西里爾字母）](../sr/README.md) | [斯洛伐克文](../sk/README.md) | [斯洛文尼亞文](../sl/README.md) | [西班牙文](../es/README.md) | [斯瓦希里文](../sw/README.md) | [瑞典文](../sv/README.md) | [他加祿文（菲律賓）](../tl/README.md) | [泰文](../th/README.md) | [土耳其文](../tr/README.md) | [烏克蘭文](../uk/README.md) | [烏爾都文](../ur/README.md) | [越南文](../vi/README.md)

**如果希望支援其他語言，請參考 [此處](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## 簡介

歡迎來到 **EdgeAI 初學者指南**——這是一個全面探索邊緣人工智慧世界的旅程。本課程將強大的 AI 能力與邊緣設備上的實際部署相結合，幫助您直接在數據生成和決策需要的地方發揮 AI 的潛力。

### 您將掌握的內容

本課程涵蓋從基礎概念到生產級實現的全過程，包括：
- **小型語言模型（SLMs）**，針對邊緣部署進行優化
- **硬體感知優化**，適用於多種平台
- **即時推理**，具備隱私保護功能
- **生產部署**，適用於企業應用的策略

### 為什麼 EdgeAI 很重要

邊緣 AI 是一種解決現代關鍵挑戰的全新模式：
- **隱私與安全**：在本地處理敏感數據，避免雲端暴露
- **即時性能**：消除網絡延遲，適用於時間敏感的應用
- **成本效益**：降低帶寬和雲端計算成本
- **運行韌性**：在網絡中斷期間保持功能
- **法規合規**：滿足數據主權要求

### 邊緣 AI

邊緣 AI 是指在硬體上本地運行 AI 算法和語言模型——靠近數據生成的地方——而不依賴雲端資源進行推理。它能降低延遲、增強隱私並支持即時決策。

### 核心原則：
- **設備端推理**：AI 模型在邊緣設備（手機、路由器、微控制器、工業 PC）上運行
- **離線能力**：無需持續的網絡連接即可運行
- **低延遲**：即時響應，適合即時系統
- **數據主權**：將敏感數據保留在本地，提升安全性和合規性

### 小型語言模型（SLMs）

像 Phi-4、Mistral-7B 和 Gemma 這樣的 SLMs 是大型 LLMs 的優化版本——經過訓練或蒸餾以實現：
- **減少記憶體佔用**：有效利用有限的邊緣設備記憶體
- **降低計算需求**：針對 CPU 和邊緣 GPU 性能進行優化
- **更快的啟動時間**：快速初始化，適用於響應式應用

它們在滿足以下限制的同時解鎖強大的 NLP 功能：
- **嵌入式系統**：物聯網設備和工業控制器
- **移動設備**：具備離線能力的智能手機和平板電腦
- **物聯網設備**：資源有限的感測器和智能設備
- **邊緣伺服器**：資源有限的本地處理單元
- **個人電腦**：桌面和筆記本電腦的部署場景

## 課程架構

### [模組 01：邊緣 AI 基礎與轉型](./Module01/README.md)
**主題**：邊緣 AI 部署的轉型

#### 章節結構：
- [**第 1 節：邊緣 AI 基礎**](./Module01/01.EdgeAIFundamentals.md)
  - 傳統雲端 AI 與邊緣 AI 的比較
  - 邊緣計算的挑戰與限制
  - 關鍵技術：模型量化、壓縮優化、小型語言模型（SLMs）
  - 硬體加速：NPUs、GPU 優化、CPU 優化
  - 優勢：隱私安全、低延遲、離線能力、成本效益

- [**第 2 節：實際案例研究**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi & Mu 模型生態系統
  - 日本航空 AI 報告系統案例研究
  - 市場影響與未來方向
  - 部署考量與最佳實踐

- [**第 3 節：實際實現指南**](./Module01/03.PracticalImplementationGuide.md)
  - 開發環境設置（Python 3.10+、.NET 8+）
  - 硬體需求與推薦配置
  - 核心模型家族資源
  - 量化與優化工具（Llama.cpp、Microsoft Olive、Apple MLX）
  - 評估與驗證清單

- [**第 4 節：邊緣 AI 部署硬體平台**](./Module01/04.EdgeDeployment.md)
  - 邊緣 AI 部署考量與需求
  - Intel 邊緣 AI 硬體與優化技術
  - Qualcomm AI 解決方案，適用於移動和嵌入式系統
  - NVIDIA Jetson 與邊緣計算平台
  - Windows AI PC 平台，具備 NPU 加速
  - 硬體特定的優化策略

---

### [模組 02：小型語言模型基礎](./Module02/README.md)
**主題**：SLM 理論原則、實現策略與生產部署

#### 章節結構：
- [**第 1 節：Microsoft Phi 模型家族基礎**](./Module02/01.PhiFamily.md)
  - 設計理念演變（Phi-1 至 Phi-4）
  - 以效率為先的架構設計
  - 專業能力（推理、多模態、邊緣部署）

- [**第 2 節：Qwen 模型家族基礎**](./Module02/02.QwenFamily.md)
  - 開源卓越（Qwen 1.0 至 Qwen3）——可透過 Hugging Face 獲取
  - 具備思考模式能力的高級推理架構
  - 可擴展部署選項（0.5B-235B 參數）

- [**第 3 節：Gemma 模型家族基礎**](./Module02/03.GemmaFamily.md)
  - 以研究驅動的創新（Gemma 3 & 3n）
  - 多模態卓越
  - 移動優先架構

- [**第 4 節：BitNET 模型家族基礎**](./Module02/04.BitNETFamily.md)
  - 革命性的量化技術（1.58-bit）
  - 專業推理框架，來自 https://github.com/microsoft/BitNet
  - 通過極端效率實現可持續 AI 領導力

- [**第 5 節：Microsoft Mu 模型基礎**](./Module02/05.mumodel.md)
  - 內建於 Windows 11 的設備優先架構
  - 與 Windows 11 設定的系統整合
  - 隱私保護的離線操作

- [**第 6 節：Phi-Silica 基礎**](./Module02/06.phisilica.md)
  - 內建於 Windows 11 Copilot+ PC 的 NPU 優化架構
  - 卓越效率（650 tokens/second，功耗僅 1.5W）
  - 與 Windows App SDK 的開發者整合

---

### [模組 03：小型語言模型部署](./Module03/README.md)
**主題**：完整的 SLM 生命周期部署，從理論到生產環境

#### 章節結構：
- [**第 1 節：SLM 高級學習**](./Module03/01.SLMAdvancedLearning.md)
  - 參數分類框架（微型 SLM 100M-1.4B、中型 SLM 14B-30B）
  - 高級優化技術（量化方法、BitNET 1-bit 量化）
  - 模型獲取策略（Azure AI Foundry 提供 Phi 模型，Hugging Face 提供選定模型）

- [**第 2 節：本地環境部署**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollama 通用平台部署
  - Microsoft Foundry 本地企業級解決方案
  - 框架比較分析

- [**第 3 節：容器化雲端部署**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM 高性能推理部署
  - Ollama 容器編排
  - ONNX Runtime 邊緣優化實現

---

### [模組 04：模型格式轉換與量化](./Module04/README.md)
**主題**：完整的模型優化工具包，適用於跨平台的邊緣部署

#### 章節結構：
- [**第 1 節：模型格式轉換與量化基礎**](./Module04/01.Introduce.md)
  - 精度分類框架（超低、低、中等精度）
  - GGUF 和 ONNX 格式的優勢與使用案例
  - 量化對運行效率的好處
  - 性能基準與記憶體佔用比較
- [**第 2 節：Llama.cpp 實作指南**](./Module04/02.Llamacpp.md)
  - 跨平台安裝（Windows、macOS、Linux）
  - GGUF 格式轉換及量化等級（Q2_K 至 Q8_0）
  - 硬體加速（CUDA、Metal、OpenCL、Vulkan）
  - Python 整合及 REST API 部署

- [**第 3 節：Microsoft Olive 優化套件**](./Module04/03.MicrosoftOlive.md)
  - 硬體感知模型優化，內建超過 40 種元件
  - 動態及靜態量化的自動優化
  - 與 Azure ML 工作流程的企業整合
  - 支援熱門模型（Llama、Phi、部分 Qwen 模型、Gemma）

- [**第 4 節：OpenVINO 工具包優化套件**](./Module04/04.openvino.md)
  - Intel 的開源工具包，用於跨平台 AI 部署
  - 神經網路壓縮框架（NNCF）進行高級優化
  - OpenVINO GenAI 用於大型語言模型部署
  - 支援 CPU、GPU、VPU 和 AI 加速器的硬體加速

- [**第 5 節：Apple MLX 框架深入探討**](./Module04/05.AppleMLX.md)
  - Apple Silicon 的統一記憶體架構
  - 支援 LLaMA、Mistral、Phi-3、部分 Qwen 模型
  - LoRA 微調及模型自訂化
  - 與 Hugging Face 整合，支援 4-bit/8-bit 量化

- [**第 6 節：Edge AI 開發工作流程綜合**](./Module04/06.workflow-synthesis.md)
  - 整合多種優化框架的統一工作流程架構
  - 框架選擇決策樹及效能權衡分析
  - 生產準備驗證及全面部署策略
  - 為新興硬體及模型架構制定未來規劃策略

---

### [模組 05：SLMOps - 小型語言模型操作](./Module05/README.md)
**主題**：從模型蒸餾到生產部署的完整 SLM 操作生命周期

#### 章節結構：
- [**第 1 節：SLMOps 簡介**](./Module05/01.IntroduceSLMOps.md)
  - SLMOps 在 AI 操作中的範式轉變
  - 成本效益及隱私優先架構
  - 策略性商業影響及競爭優勢
  - 實際實施挑戰及解決方案

- [**第 2 節：模型蒸餾 - 從理論到實踐**](./Module05/02.SLMOps-Distillation.md)
  - 從教師模型到學生模型的知識轉移
  - 兩階段蒸餾過程的實作
  - Azure ML 蒸餾工作流程及實際範例
  - 85% 推理時間減少，保留 92% 準確率

- [**第 3 節：微調 - 為特定任務自訂模型**](./Module05/03.SLMOps-Finetuing.md)
  - 參數高效微調（PEFT）技術
  - LoRA 和 QLoRA 高級方法
  - Microsoft Olive 微調實作
  - 多適配器訓練及超參數優化

- [**第 4 節：部署 - 生產就緒實作**](./Module05/04.SLMOps.Deployment.md)
  - 模型轉換及量化以進行生產部署
  - Foundry Local 部署配置
  - 效能基準測試及品質驗證
  - 75% 尺寸縮減及生產監控

---

### [模組 06：SLM Agentic Systems - AI 代理及函數調用](./Module06/README.md)
**主題**：SLM 代理系統的實作，從基礎到高級函數調用及模型上下文協議整合

#### 章節結構：
- [**第 1 節：AI 代理及小型語言模型基礎**](./Module06/01.IntroduceAgent.md)
  - 代理分類框架（反射型、基於模型、基於目標、學習型代理）
  - SLM 基礎及優化策略（GGUF、量化、邊緣框架）
  - SLM 與 LLM 的權衡分析（成本減少 10-30 倍，任務效能達 70-80%）
  - 使用 Ollama、VLLM 和 Microsoft 邊緣解決方案進行實際部署

- [**第 2 節：小型語言模型中的函數調用**](./Module06/02.FunctionCalling.md)
  - 系統化工作流程實作（意圖檢測、JSON 輸出、外部執行）
  - 平台特定實作（Phi-4-mini、部分 Qwen 模型、Microsoft Foundry Local）
  - 高級範例（多代理協作、動態工具選擇）
  - 生產考量（速率限制、審計記錄、安全措施）

- [**第 3 節：模型上下文協議（MCP）整合**](./Module06/03.IntroduceMCP.md)
  - 協議架構及分層系統設計
  - 多後端支援（Ollama 用於開發，vLLM 用於生產）
  - 連接協議（STDIO 和 SSE 模式）
  - 實際應用（網頁自動化、數據處理、API 整合）

---

### [模組 07：EdgeAI 實作範例](./Module07/README.md)
**主題**：涵蓋多平台及框架的全面 EdgeAI 實作

#### 章節結構：
- [**Visual Studio Code 的 AI 工具包**](./Module07/aitoolkit.md)
  - VS Code 中的全面 Edge AI 開發環境
  - 模型目錄及邊緣部署的探索
  - 本地測試、優化及代理開發工作流程
  - 邊緣場景的效能監控及評估

- [**Windows EdgeAI 開發指南**](./Module07/windowdeveloper.md)
  - Windows AI Foundry 平台的全面概述
  - Phi Silica API 用於高效 NPU 推理
  - 用於影像處理及 OCR 的電腦視覺 API
  - Foundry Local CLI 用於本地開發及測試

- [**NVIDIA Jetson Orin Nano 的 EdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 信用卡大小的 67 TOPS AI 效能
  - 支援生成式 AI 模型（視覺變壓器、LLM、視覺語言模型）
  - 應用於機器人、無人機、智能相機、自主設備
  - 價格實惠的 $249 平台，推動 AI 開發普及化

- [**使用 .NET MAUI 和 ONNX Runtime GenAI 的移動應用 EdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 單一 C# 程式碼庫的跨平台移動 AI
  - 硬體加速支援（CPU、GPU、移動 AI 處理器）
  - 平台特定優化（iOS 的 CoreML，Android 的 NNAPI）
  - 完整生成式 AI 循環實作

- [**Azure 中的小型語言模型引擎的 EdgeAI**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - 雲端-邊緣混合部署架構
  - Azure AI 服務與 ONNX Runtime 的整合
  - 企業級部署及持續模型管理
  - 用於智能文件處理的混合 AI 工作流程

- [**使用 Windows ML 的 EdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Windows AI Foundry 基礎，用於高效能的設備端推理
  - 通用硬體支援（AMD、Intel、NVIDIA、Qualcomm 矽片）
  - 自動硬體抽象及優化
  - 用於多樣化 Windows 硬體生態系統的統一框架

- [**使用 Foundry Local 應用的 EdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - 隱私導向的 RAG 實作，使用本地資源
  - Phi-3 語言模型整合語義搜索（僅限 Phi 模型）
  - 本地向量數據庫支援（SQLite、Qdrant）
  - 數據主權及離線操作能力

## 課程學習目標

完成這門全面的 EdgeAI 課程後，您將具備設計、實作及部署生產就緒 EdgeAI 解決方案的專業技能。我們的結構化方法確保您掌握理論基礎及實際應用技能。

### 技術能力

**基礎知識**
- 理解雲端 AI 架構與邊緣 AI 架構的基本差異
- 掌握模型量化、壓縮及優化的原則，適用於資源受限環境
- 理解硬體加速選項（NPUs、GPUs、CPUs）及其部署影響

**實作技能**
- 在多樣化邊緣平台（移動、嵌入式、物聯網、邊緣伺服器）部署小型語言模型
- 應用優化框架，包括 Llama.cpp、Microsoft Olive、ONNX Runtime 和 Apple MLX
- 實作具有亞秒級響應需求的即時推理系統

**生產專業知識**
- 設計可擴展的 EdgeAI 架構，用於企業應用
- 實作已部署系統的監控、維護及更新策略
- 應用隱私保護 EdgeAI 實作的安全最佳實踐

### 策略能力

**決策框架**
- 評估 EdgeAI 機會並識別適合的商業應用案例
- 分析模型準確性、推理速度、功耗及硬體成本之間的權衡
- 根據特定部署限制選擇合適的 SLM 家族及配置

**系統架構**
- 設計端到端 EdgeAI 解決方案，與現有基礎設施整合
- 規劃混合邊緣-雲端架構，以實現最佳效能及成本效益
- 實作即時 AI 應用的數據流及處理管道

### 行業應用

**實際部署場景**
- **製造業**：質量控制系統、預測性維護及流程優化
- **醫療保健**：隱私保護診斷工具及患者監控系統
- **交通運輸**：自主車輛決策及交通管理
- **智慧城市**：智能基礎設施及資源管理系統
- **消費電子**：AI 驅動的移動應用及智能家居設備

## 學習成果概述

### 模組 01 學習成果：
- 理解雲端與邊緣 AI 架構的基本差異
- 掌握邊緣部署的核心優化技術
- 認識實際應用及成功案例
- 獲得實作 EdgeAI 解決方案的實際技能

### 模組 02 學習成果：
- 深入理解不同 SLM 設計理念及其部署影響
- 掌握基於計算限制及效能需求的策略性決策能力
- 理解部署靈活性權衡
- 擁有未來準備的高效 AI 架構洞察力

### 模組 03 學習成果：
- 策略性模型選擇能力
- 優化技術精通
- 部署靈活性精通
- 生產就緒配置能力

### 模組 04 學習成果：
- 深入理解量化界限及實際應用
- 實際操作多種優化框架（Llama.cpp、Olive、OpenVINO、MLX）
- 精通使用 OpenVINO 和 NNCF 進行 Intel 硬體優化
- 在多樣化平台中選擇硬體感知優化的能力
- 跨平台邊緣計算環境的生產部署技能
- 為最佳 Edge AI 解決方案進行策略性框架選擇及工作流程綜合

### 模組 05 學習成果：
- 掌握 SLMOps 範式及操作原則
- 實作模型蒸餾以進行知識轉移及效率優化
- 應用微調技術進行領域特定模型自訂化
- 部署具有監控及維護策略的生產就緒 SLM 解決方案

### 模組 06 學習成果：
- 理解 AI 代理及小型語言模型架構的基礎概念
- 精通多平台及框架的函數調用實作
- 整合模型上下文協議（MCP），進行標準化外部工具互動
- 構建複雜代理系統，減少人工干預需求

### 模組 07 學習成果：
- 精通 Visual Studio Code 的 AI 工具包，用於全面 Edge AI 開發工作流程
- 獲得 Windows AI Foundry 平台及 NPU 優化策略的專業知識
- 獲得多樣化 EdgeAI 平台及實作策略的實際操作經驗
- 精通 NVIDIA、移動、Azure 和 Windows 平台的硬體特定優化技術
- 理解效能、成本及隱私需求之間的部署權衡
- 開發跨不同生態系統的實際 EdgeAI 應用技能

## 預期課程成果

成功完成本課程後，您將具備知識、技能及信心，能在專業環境中領導 EdgeAI 項目。

### 專業準備

**技術領導力**
- **解決方案架構**：設計符合企業需求的全面 EdgeAI 系統
- **效能優化**：在準確性、速度及資源消耗之間達成最佳平衡
- **跨平台部署**：在 Windows、Linux、移動及嵌入式平台上實作解決方案
- **生產操作**：以企業級可靠性維護及擴展 EdgeAI 系統

**行業專業知識**
- **技術評估**：評估並推薦適合特定商業挑戰的 EdgeAI 解決方案
- **實作規劃**：為 EdgeAI 項目制定現實的時間表及資源需求
- **風險管理**：識別並減輕 EdgeAI 部署中的技術及操作風險
- **投資回報優化**：展示 EdgeAI 實作帶來的可衡量商業價值

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
- 在多個硬體平台上部署生產就緒解決方案
- 記錄優化策略及效能改進成果

**持續學習路徑**
- 為高級 AI 專業化奠定基礎
- 為雲端-邊緣混合架構做準備
- 成為新興 AI 技術及框架的入門途徑
本課程將您置於人工智慧技術部署的最前沿，智能功能無縫整合到驅動現代生活的設備和系統中。

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
- **理論與實踐結合**：每個模組包含理論基礎和實際操作
- **真實案例研究**：基於 Microsoft、阿里巴巴、Google 等公司的實際案例
- **動手實踐**：完成配置文件、API 測試程序和部署腳本
- **性能基準**：詳細比較推理速度、記憶體使用情況和資源需求
- **企業級考量**：安全實踐、合規框架和數據保護策略

## 入門指南

推薦學習路徑：
1. 從 **Module01** 開始，建立 EdgeAI 的基本理解
2. 接著學習 **Module02**，深入了解各種 SLM 模型家族
3. 學習 **Module03**，掌握實際部署技能
4. 繼續學習 **Module04**，進行高級模型優化、格式轉換和框架整合
5. 完成 **Module05**，掌握 SLMOps，實現生產級應用
6. 探索 **Module06**，了解 SLM 主動系統和函數調用功能
7. 最後完成 **Module07**，獲得 AI 工具包和多樣化 EdgeAI 實現範例的實踐經驗

每個模組都設計為獨立完整，但按順序學習將能獲得最佳效果。

## 學習指南

提供了一份全面的 [學習指南](STUDY_GUIDE.md)，幫助您最大化學習效果。學習指南包括：

- **結構化學習路徑**：優化的課程完成時間表，20 小時內完成課程
- **時間分配建議**：針對閱讀、練習和項目平衡的具體建議
- **重點概念聚焦**：每個模組的優先學習目標
- **自我評估工具**：測試理解的問題和練習
- **迷你項目點子**：加強學習的實際應用

學習指南適合密集學習（一週完成）和兼職學習（三週完成），即使您只能投入 10 小時，也有清晰的時間分配指導。

---

**EdgeAI 的未來在於持續改進模型架構、量化技術和部署策略，優先考慮效率和專業化，而非通用能力。採用這種範式轉變的組織將能充分利用人工智慧的變革潛力，同時保持對數據和運營的控制。**

## 其他課程

我們的團隊還提供其他課程！查看以下內容：

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

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。