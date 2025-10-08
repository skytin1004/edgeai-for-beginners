<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "135b2658979f1e494bb0ecc6e26d4752",
  "translation_date": "2025-10-08T16:04:18+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tw"
}
-->
# AGENTS.md

> **開發者指南：EdgeAI for Beginners 貢獻說明**
> 
> 本文件為開發者、AI 代理以及貢獻者提供了全面的資訊，涵蓋了設置、開發流程、測試以及最佳實踐。
> 
> **最後更新日期**：2025 年 10 月 | **文件版本**：2.0

## 目錄

- [專案概述](../..)
- [儲存庫結構](../..)
- [先決條件](../..)
- [設置指令](../..)
- [開發流程](../..)
- [測試說明](../..)
- [程式碼風格指南](../..)
- [Pull Request 指南](../..)
- [翻譯系統](../..)
- [Foundry Local 整合](../..)
- [建置與部署](../..)
- [常見問題與疑難排解](../..)
- [其他資源](../..)
- [專案特定備註](../..)
- [獲取幫助](../..)

## 專案概述

EdgeAI for Beginners 是一個全面的教育性儲存庫，旨在教授使用小型語言模型（SLMs）進行 Edge AI 開發。課程涵蓋了 EdgeAI 的基礎知識、模型部署、優化技術以及使用 Microsoft Foundry Local 和多種 AI 框架進行生產級實現。

**主要技術：**
- Python 3.8+（AI/ML 範例的主要語言）
- .NET C#（AI/ML 範例）
- JavaScript/Node.js 與 Electron（用於桌面應用程式）
- Microsoft Foundry Local SDK
- Microsoft Windows ML
- VSCode AI 工具包
- OpenAI SDK
- AI 框架：LangChain、Semantic Kernel、Chainlit
- 模型優化：Llama.cpp、Microsoft Olive、OpenVINO、Apple MLX

**儲存庫類型：** 教育內容儲存庫，包含 8 個模組和 10 個綜合範例應用程式

**架構：** 多模組學習路徑，通過實際範例展示 Edge AI 部署模式

## 儲存庫結構

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## 先決條件

### 必需工具

- **Python 3.8+** - 用於 AI/ML 範例和筆記本
- **Node.js 16+** - 用於 Electron 範例應用程式
- **Git** - 用於版本控制
- **Microsoft Foundry Local** - 用於本地運行 AI 模型

### 推薦工具

- **Visual Studio Code** - 安裝 Python、Jupyter 和 Pylance 擴展
- **Windows Terminal** - 提供更好的命令列體驗（Windows 使用者）
- **Docker** - 用於容器化開發（可選）

### 系統需求

- **記憶體**：最低 8GB，建議 16GB+（多模型場景）
- **儲存空間**：至少 10GB 可用空間，用於模型和依賴項
- **作業系統**：Windows 10/11、macOS 11+ 或 Linux（Ubuntu 20.04+）
- **硬體**：支援 AVX2 的 CPU；建議使用 GPU（CUDA、Qualcomm NPU）

### 知識需求

- 基本的 Python 程式設計知識
- 熟悉命令列介面
- 理解 AI/ML 概念（用於範例開發）
- 熟悉 Git 工作流程和 Pull Request 流程

## 設置指令

### 儲存庫設置

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python 範例設置（Module08 和 Python 範例）

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Node.js 範例設置（範例 08 - Windows 聊天應用程式）

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local 設置

Foundry Local 是運行範例所需的工具。從官方儲存庫下載並安裝：

**安裝：**
- **Windows**：`winget install Microsoft.FoundryLocal`
- **macOS**：`brew tap microsoft/foundrylocal && brew install foundrylocal`
- **手動安裝**：從 [releases page](https://github.com/microsoft/Foundry-Local/releases) 下載

**快速開始：**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-3.5-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**注意：** Foundry Local 會自動為您的硬體選擇最佳模型變體（CUDA GPU、Qualcomm NPU 或 CPU）。

## 開發流程

### 內容開發

此儲存庫主要包含 **Markdown 教育內容**。進行更改時：

1. 編輯適當模組目錄中的 `.md` 文件
2. 遵循現有的格式模式
3. 確保程式碼範例準確且經過測試
4. 必要時更新相應的翻譯內容（或讓自動化處理）

### 範例應用程式開發

對於 Python 範例（範例 01-07, 09-10）：
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

對於 Electron 範例（範例 08）：
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### 測試範例應用程式

Python 範例沒有自動化測試，但可以通過運行進行驗證：
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron 範例具有測試基礎架構：
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## 測試說明

### 內容驗證

儲存庫使用自動化翻譯工作流程。翻譯無需手動測試。

**內容更改的手動驗證：**
1. 通過預覽 `.md` 文件檢查 Markdown 渲染效果
2. 確保所有連結指向有效目標
3. 測試文檔中包含的任何程式碼片段
4. 確保圖片加載正常

### 範例應用程式測試

**Module08/samples/08（Electron 應用程式）具有全面測試：**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python 範例應進行手動測試：**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## 程式碼風格指南

### Markdown 內容

- 使用一致的標題層級（# 用於標題，## 用於主要部分，### 用於子部分）
- 包含帶有語言指定的程式碼塊：```python, ```bash, ```javascript
- 遵循現有的表格、列表和強調格式
- 保持行可讀性（目標約 80-100 字元，但不強制）
- 對內部參考使用相對連結

### Python 程式碼風格

- 遵循 PEP 8 規範
- 適當使用類型提示
- 為函數和類別添加 docstring
- 使用有意義的變數名稱
- 保持函數專注且簡潔

### JavaScript/Node.js 程式碼風格

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**主要規範：**
- 範例 08 提供 ESLint 配置
- 使用 Prettier 進行程式碼格式化
- 使用現代 ES6+ 語法
- 遵循程式碼庫中的現有模式

## Pull Request 指南

### 貢獻工作流程

1. **Fork 此儲存庫** 並從 `main` 分支創建新分支
2. **進行更改**，遵循程式碼風格指南
3. **徹底測試**，使用上述測試說明
4. **提交清晰的訊息**，遵循常規提交格式
5. **推送到您的 Fork** 並創建 Pull Request
6. **回應維護者的反饋**，完成審核

### 分支命名規範

- `feature/<module>-<description>` - 用於新功能或內容
- `fix/<module>-<description>` - 用於錯誤修復
- `docs/<description>` - 用於文檔改進
- `refactor/<description>` - 用於程式碼重構

### 提交訊息格式

遵循 [Conventional Commits](https://www.conventionalcommits.org/)：

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**範例：**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### 標題格式
```
[ModuleXX] Brief description of change
```
或
```
[Module08/samples/XX] Description for sample changes
```

### 行為準則

所有貢獻者必須遵守 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/)。請在貢獻前查看 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

### 提交前檢查

**對於內容更改：**
- 預覽所有修改的 Markdown 文件
- 驗證連結和圖片是否正常
- 檢查拼寫和語法錯誤

**對於範例程式碼更改（Module08/samples/08）：**
```bash
npm run lint
npm test
```

**對於 Python 範例更改：**
- 測試範例是否成功運行
- 驗證錯誤處理是否正常
- 檢查與 Foundry Local 的兼容性

### 審核流程

- 教育內容更改需檢查準確性和清晰度
- 程式碼範例需測試功能性
- 翻譯更新由 GitHub Actions 自動處理

## 翻譯系統

**重要：** 此儲存庫使用 GitHub Actions 自動翻譯。

- 翻譯內容位於 `/translations/` 目錄（支持 50+ 種語言）
- 通過 `co-op-translator.yml` 工作流程自動化
- **請勿手動編輯翻譯文件** - 它們會被覆蓋
- 僅編輯根目錄和模組目錄中的英文原始文件
- 翻譯會在推送到 `main` 分支時自動生成

## Foundry Local 整合

大多數 Module08 範例需要 Microsoft Foundry Local 運行。

### 安裝與設置

**安裝 Foundry Local：**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**安裝 Python SDK：**
```bash
pip install foundry-local-sdk openai
```

### 啟動 Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### SDK 使用（Python）
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-3.5-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### 驗證 Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### 範例的環境變數

大多數範例使用以下環境變數：
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-3.5-mini  # or phi-4-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**注意：** 使用 `FoundryLocalManager` 時，SDK 會自動處理服務發現和模型加載。模型別名（如 `phi-3.5-mini`）確保為您的硬體選擇最佳變體。

## 建置與部署

### 內容部署

此儲存庫主要是文檔內容 - 不需要建置過程。

### 範例應用程式建置

**Electron 應用程式（Module08/samples/08）：**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python 範例：**
無需建置過程 - 範例直接使用 Python 解釋器運行。

## 常見問題與疑難排解

> **提示：** 查看 [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) 了解已知問題和解決方案。

### 關鍵問題（阻塞）

#### Foundry Local 未運行
**問題：** 範例因連接錯誤失敗

**解決方案：**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-3.5-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### 常見問題（中等）

#### Python 虛擬環境問題
**問題：** 模組導入錯誤

**解決方案：**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron 建置問題
**問題：** npm 安裝或建置失敗

**解決方案：**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### 工作流程問題（輕微）

#### 翻譯工作流程衝突
**問題：** 翻譯 PR 與您的更改衝突

**解決方案：**
- 僅編輯英文原始文件
- 讓自動化翻譯工作流程處理翻譯
- 如果發生衝突，在翻譯合併後將 `main` 合併到您的分支

#### 模型下載失敗
**問題：** Foundry Local 無法下載模型

**解決方案：**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## 其他資源

### 學習路徑
- **初學者路徑：** 模組 01-02（7-9 小時）
- **中級路徑：** 模組 03-04（9-11 小時）
- **高級路徑：** 模組 05-07（12-15 小時）
- **專家路徑：** 模組 08（8-10 小時）

### 關鍵模組內容
- **Module01：** EdgeAI 基礎和實際案例研究
- **Module02：** 小型語言模型（SLM）家族和架構
- **Module03：** 本地和雲端部署策略
- **Module04：** 使用多種框架進行模型優化
- **Module05：** SLMOps - 生產運營
- **Module06：** AI 代理和函數調用
- **Module07：** 平台特定實現
- **Module08：** Foundry Local 工具包，包含 10 個綜合範例

### 外部依賴
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - 提供 OpenAI 兼容 API 的本地 AI 模型運行時
  - [文檔](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - 優化框架
- [Microsoft Olive](https://microsoft.github.io/Olive/) - 模型優化工具包
- [OpenVINO](https://docs.openvino.ai/) - Intel 的優化工具包

## 專案特定備註

### Module08 範例應用程式

儲存庫包含 10 個綜合範例應用程式：

1. **01-REST Chat Quickstart** - 基本的 OpenAI SDK 集成
2. **02-OpenAI SDK Integration** - 高級 SDK 功能
3. **03-Model Discovery & Benchmarking** - 模型比較工具
4. **04-Chainlit RAG Application** - 檢索增強生成
5. **05-Multi-Agent Orchestration** - 基本代理協調
6. **06-Models-as-Tools Router** - 智能模型路由
7. **07-Direct API Client** - 低級 API 集成
8. **08-Windows 11 Chat App** - 原生 Electron 桌面應用程式
9. **09-Advanced Multi-Agent System** - 複雜代理協調
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel 集成

每個範例展示了使用 Foundry Local 進行 Edge AI 開發的不同方面。

### 性能考量

- SLMs 已針對邊緣部署進行優化（2-16GB RAM）
- 本地推論提供 50-500 毫秒的響應時間  
- 量化技術可實現 75% 的大小縮減，同時保留 85% 的性能  
- 使用本地模型進行即時對話功能  

### 安全性與隱私

- 所有處理均在本地進行 - 無需將數據發送至雲端  
- 適用於隱私敏感型應用（如醫療、金融）  
- 符合數據主權要求  
- Foundry Local 完全在本地硬件上運行  

## 獲取幫助

### 文件

- **主 README**: [README.md](README.md) - 儲存庫概述及學習路徑  
- **學習指南**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - 學習資源及時間表  
- **支援**: [SUPPORT.md](SUPPORT.md) - 如何獲得幫助  
- **安全性**: [SECURITY.md](SECURITY.md) - 報告安全問題  

### 社群支援

- **GitHub 問題**: [回報錯誤或提出功能需求](https://github.com/microsoft/edgeai-for-beginners/issues)  
- **GitHub 討論**: [提出問題並分享想法](https://github.com/microsoft/edgeai-for-beginners/discussions)  
- **Foundry Local 問題**: [Foundry Local 的技術問題](https://github.com/microsoft/Foundry-Local/issues)  

### 聯絡方式

- **維護者**: 請參閱 [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)  
- **安全問題**: 請遵循 [SECURITY.md](SECURITY.md) 中的負責披露流程  
- **Microsoft 支援**: 如需企業支援，請聯絡 Microsoft 客戶服務  

### 其他資源

- **Microsoft Learn**: [AI 和機器學習學習路徑](https://learn.microsoft.com/training/browse/?products=ai-services)  
- **Foundry Local 文件**: [官方文件](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)  
- **社群範例**: 請查看 [GitHub 討論](https://github.com/microsoft/edgeai-for-beginners/discussions) 中的社群貢獻  

---

**這是一個專注於教授邊緣 AI 開發的教育性儲存庫。主要的貢獻模式是改進教育內容以及新增/增強示範邊緣 AI 概念的範例應用程式。**  

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。