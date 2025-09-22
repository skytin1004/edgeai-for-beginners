<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T11:42:24+00:00",
  "source_file": "Module08/README.md",
  "language_code": "hk"
}
-->
# 模組 08：深入了解 Microsoft Foundry Local - 完整開發者工具包

## 概述

Microsoft Foundry Local 代表了邊緣 AI 開發的下一代技術，為開發者提供強大的工具，能夠在本地構建、部署及擴展 AI 應用，同時保持與 Azure AI Foundry 的無縫整合。本模組涵蓋了 Foundry Local 的全面內容，從安裝到高級代理開發。

**核心技術：**
- Microsoft Foundry Local CLI 和 SDK
- Azure AI Foundry 整合
- 設備上的模型推理
- 本地模型緩存及優化
- 基於代理的架構

## 模組學習目標

完成此模組後，您將能夠：

- **掌握 Foundry Local 設置**：安裝、配置及優化 Foundry Local 以進行 Windows 11 開發
- **部署多樣化模型**：使用 CLI 命令在本地運行 phi、qwen、deepseek 和 GPT-OSS-20B 模型
- **構建生產解決方案**：使用高級提示工程和數據整合創建 AI 應用
- **利用開源生態系統**：整合 Hugging Face 模型及社群驅動的擴展
- **比較 AI 架構**：理解 LLMs 與 SLMs 的權衡及部署策略
- **開發 AI 代理**：使用 Foundry Local 的架構及基礎能力構建智能代理
- **實現模型作為工具**：創建模組化、可定制的 AI 解決方案以應對企業應用

## 課程結構

### [1: 開始使用 Foundry Local](./01.FoundryLocalSetup.md)
**重點**：安裝、CLI 設置、模型緩存及硬件加速

**您將學到：**
- 在 Windows 11 上完成 Foundry Local 安裝
- CLI 配置及命令結構
- 優化性能的模型緩存策略
- 硬件加速設置及優化
- 實際部署 phi、qwen、deepseek 和 GPT-OSS-20B 模型

**時長**：2-3 小時  
**先決條件**：Windows 11，基本命令行知識

---

### [2: 使用 Azure AI Foundry 構建 AI 解決方案](./02.AzureAIFoundryIntegration.md)
**重點**：高級提示工程、數據整合及可操作任務

**您將學到：**
- 高級提示工程技術
- 數據整合模式及最佳實踐
- 使用 Foundry Local 構建可操作的 AI 任務
- 無縫的 Azure AI Foundry 整合工作流程
- 性能優化及監控

**時長**：2-3 小時  
**先決條件**：完成第一節課程，Azure 帳戶（可選）

---

### [3: Foundry Local 的開源模型](./03.OpenSourceModels.md)
**重點**：Hugging Face 整合、模型選擇策略及社群驅動的擴展

**您將學到：**
- Hugging Face 模型與 Foundry Local 的整合
- 自帶模型（BYOM）策略及實施
- Model Mondays 系列的洞察及社群貢獻
- 自定義模型部署及優化
- 社群模型評估及選擇標準

**時長**：2-3 小時  
**先決條件**：完成第一至第二節課程，Hugging Face 帳戶

---

### [4: 探索尖端模型 - LLMs、SLMs 及設備推理](./04.CuttingEdgeModels.md)
**重點**：模型比較、使用 Phi 和 ONNX Runtime 的 EdgeAI、高級演示

**您將學到：**
- 全面比較 LLMs 與 SLMs 的使用案例
- 本地與雲端推理的權衡及決策框架
- 使用 Phi 和 ONNX Runtime 的 EdgeAI 實施
- Chainlit RAG 聊天應用的開發及部署
- WebGPU 推理優化技術
- AI PC SDK 整合及功能

**時長**：3-4 小時  
**先決條件**：完成第一至第三節課程，理解推理概念

---

### [5: 使用 Foundry Local 快速構建 AI 驅動代理](./05.AIPoweredAgents.md)
**重點**：快速 GenAI 應用開發、系統提示、基礎及代理架構

**您將學到：**
- Foundry Local 代理架構及設計模式
- 系統提示工程以設計代理行為
- 基礎技術以確保代理可靠回應
- 快速 GenAI 應用開發工作流程
- 代理協調及多代理系統
- AI 代理的生產部署策略

**時長**：3-4 小時  
**先決條件**：完成第一至第四節課程，基本了解 AI 代理

---

### [6: Foundry Local - 模型作為工具](./06.ModelsAsTools.md)
**重點**：模組化 AI 解決方案、設備部署及企業擴展

**您將學到：**
- 將 AI 模型視為模組化、可定制的工具
- 無需雲端依賴的設備部署
- 低延遲、成本效益及隱私保護的推理
- SDK、API 和 CLI 整合模式
- 為特定使用案例定制模型
- 從本地到 Azure AI Foundry 的擴展策略
- 企業級 AI 應用架構

**時長**：3-4 小時  
**先決條件**：完成所有前述課程，有企業開發經驗更佳

## 先決條件

### 系統要求
- **操作系統**：Windows 11（22H2 或更高版本）
- **內存**：16GB RAM（建議 32GB 以支持更大模型）
- **存儲**：50GB 可用空間以進行模型緩存
- **硬件**：建議使用支持 NPU 的設備（如 Copilot+ PC），GPU 可選
- **網絡**：高速網絡以進行初始模型下載

### 開發環境
- Visual Studio Code 及 AI Toolkit 擴展
- Python 3.10+ 及 pip
- Git 以進行版本控制
- PowerShell 或命令提示符
- Azure CLI（可選，用於雲端整合）

### 知識要求
- 基本了解 AI/ML 概念
- 熟悉命令行操作
- Python 編程基礎
- REST API 概念
- 基本了解提示工程及模型推理

## 模組時間表

**總預估時間**：15-20 小時

| 課程 | 重點領域 | 時間 | 複雜度 |
|------|----------|------|--------|
|  1 | 設置及基礎 | 2-3 小時 | 初學者 |
|  2 | AI 解決方案 | 2-3 小時 | 中級 |
|  3 | 開源模型 | 2-3 小時 | 中級 |
|  4 | 高級模型 | 3-4 小時 | 高級 |
|  5 | AI 代理 | 3-4 小時 | 高級 |
|  6 | 企業工具 | 3-4 小時 | 專家 |

## 核心資源

### 主要文檔
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local 文檔](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays 系列](https://aka.ms/model-mondays)

### 社群資源
- [Foundry Local 社群討論](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry 示例](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI 開發者社群](https://techcommunity.microsoft.com/category/artificialintelligence)

## 學習成果

完成此模組後，您將具備以下能力：

### 技術掌握
- **部署及管理**：在開發及生產環境中安裝及管理 Foundry Local
- **整合模型**：無縫使用 Microsoft、Hugging Face 及社群來源的多樣化模型
- **構建應用**：創建具備高級功能及優化的生產級 AI 應用
- **開發代理**：實施具備基礎、推理及工具整合的高級 AI 代理

### 策略理解
- **架構決策**：在本地與雲端部署間做出明智選擇
- **性能優化**：在不同硬件配置中優化推理性能
- **企業擴展**：設計能從本地原型擴展到企業部署的應用
- **隱私及安全**：實施隱私保護的 AI 解決方案，使用本地推理

### 創新能力
- **快速原型**：快速構建及測試 AI 應用概念
- **社群整合**：利用開源模型並為生態系統做出貢獻
- **高級模式**：實施尖端 AI 模式，包括 RAG、代理及工具整合
- **面向未來的開發**：構建適應新興 AI 技術及模式的應用

## 開始使用

1. **準備您的環境**：確保使用 Windows 11 並符合建議的硬件規格
2. **安裝先決條件**：設置開發工具及依賴項
3. **從第一節開始**：從 Foundry Local 安裝及基礎設置開始
4. **按順序進行**：按課程順序完成以獲得最佳學習效果
5. **持續練習**：通過實際操作及項目應用所學概念

## 成功指標

通過以下方式追蹤您的進度：

- [ ] 成功安裝及配置 Foundry Local
- [ ] 部署並運行至少 4 種不同的模型系列
- [ ] 使用數據整合構建完整的 AI 解決方案
- [ ] 整合至少 2 個開源模型
- [ ] 創建功能性 RAG 聊天應用
- [ ] 開發並部署 AI 代理
- [ ] 實施模型作為工具的架構

## 示例快速入門

### 1) 環境設置（Windows cmd.exe）
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) 啟動本地模型（新終端）
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) 運行 Chainlit 演示（第四節課程）
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) 運行多代理協調器（第五節課程）
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

如果出現連接錯誤，請驗證 Foundry Local：
```cmd
curl http://localhost:8000/v1/models
```

### 路由器配置（第六節課程）
路由器執行快速健康檢查並支持基於環境的配置：
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

此模組代表了邊緣 AI 開發的尖端技術，結合了 Microsoft 的企業級工具與開源生態系統的靈活性及創新性。通過掌握 Foundry Local，您將站在 AI 應用開發的最前沿。

關於 Azure OpenAI（第二節課程），請參閱示例 README 以了解所需的環境變數及 API 版本設置。

## 示例概述

- `samples/01`: 快速 REST 聊天至 Foundry Local (`chat_quickstart.py`)。
- `samples/02`: OpenAI SDK 整合 (`sdk_quickstart.py`)。
- `samples/03`: 模型發現 + 快速基準測試 (`list_and_bench.cmd`)。
- `samples/04`: Chainlit RAG 演示 (`app.py`)。
- `samples/05`: 多代理協調 (`python -m samples.05.agents.coordinator`)。
- `samples/06`: 模型作為工具的路由器 (`python samples\06\router.py`)。

---

