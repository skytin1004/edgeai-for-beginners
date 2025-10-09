<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "135b2658979f1e494bb0ecc6e26d4752",
  "translation_date": "2025-10-09T07:56:06+00:00",
  "source_file": "AGENTS.md",
  "language_code": "mo"
}
-->
# AGENTS.md

> **開發者指南：EdgeAI 初學者貢獻指南**
> 
> 本文件提供給開發者、AI代理以及貢獻者的全面資訊，涵蓋了本存儲庫的設置、開發工作流程、測試以及最佳實踐。
> 
> **最後更新日期**：2025年10月 | **文件版本**：2.0

## 目錄

- [專案概述](../..)
- [存儲庫結構](../..)
- [先決條件](../..)
- [設置指令](../..)
- [開發工作流程](../..)
- [測試指引](../..)
- [代碼風格指南](../..)
- [拉取請求指南](../..)
- [翻譯系統](../..)
- [Foundry Local 整合](../..)
- [構建與部署](../..)
- [常見問題與故障排除](../..)
- [額外資源](../..)
- [專案特定備註](../..)
- [尋求幫助](../..)

## 專案概述

EdgeAI for Beginners 是一個全面的教育存儲庫，教授使用小型語言模型（SLMs）進行邊緣AI開發。課程涵蓋了EdgeAI基礎知識、模型部署、優化技術以及使用 Microsoft Foundry Local 和各種AI框架的生產級實現。

**核心技術：**
- Python 3.8+（AI/ML範例的主要語言）
- .NET C#（AI/ML範例）
- JavaScript/Node.js 與 Electron（桌面應用程式）
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI 工具包
- OpenAI SDK
- AI框架：LangChain、Semantic Kernel、Chainlit
- 模型優化：Llama.cpp、Microsoft Olive、OpenVINO、Apple MLX

**存儲庫類型：** 教育內容存儲庫，包含8個模組和10個全面的範例應用程式

**架構：** 多模組學習路徑，提供展示邊緣AI部署模式的實用範例

## 存儲庫結構

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

- **Python 3.8+** - 用於AI/ML範例和筆記本
- **Node.js 16+** - 用於Electron範例應用程式
- **Git** - 用於版本控制
- **Microsoft Foundry Local** - 用於本地運行AI模型

### 推薦工具

- **Visual Studio Code** - 配備Python、Jupyter和Pylance擴展
- **Windows Terminal** - 提供更好的命令行體驗（Windows用戶）
- **Docker** - 用於容器化開發（可選）

### 系統需求

- **RAM**：最低8GB，推薦16GB以上以支持多模型場景
- **存儲空間**：至少10GB的可用空間，用於模型和依賴項
- **操作系統**：Windows 10/11、macOS 11+ 或 Linux（Ubuntu 20.04+）
- **硬件**：支持AVX2的CPU；GPU（CUDA、Qualcomm NPU）可選但推薦

### 知識要求

- 基本的Python編程知識
- 熟悉命令行界面
- 理解AI/ML概念（用於範例開發）
- Git工作流程和拉取請求流程

## 設置指令

### 存儲庫設置

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python範例設置（模組08及Python範例）

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

### Node.js範例設置（範例08 - Windows聊天應用程式）

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

### Foundry Local設置

Foundry Local 是運行範例所需的工具。從官方存儲庫下載並安裝：

**安裝：**
- **Windows**：`winget install Microsoft.FoundryLocal`
- **macOS**：`brew tap microsoft/foundrylocal && brew install foundrylocal`
- **手動**：從[版本頁面](https://github.com/microsoft/Foundry-Local/releases)下載

**快速開始：**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-3.5-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**注意**：Foundry Local 會自動選擇最適合您硬件的模型版本（CUDA GPU、Qualcomm NPU 或 CPU）。

## 開發工作流程

### 內容開發

本存儲庫主要包含**Markdown教育內容**。進行更改時：

1. 編輯模組目錄中的 `.md` 文件
2. 遵循現有的格式模式
3. 確保代碼範例準確且已測試
4. 必要時更新相應的翻譯內容（或由自動化處理）

### 範例應用程式開發

對於Python範例（範例01-07、09-10）：
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

對於Electron範例（範例08）：
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### 測試範例應用程式

Python範例沒有自動化測試，但可以通過運行進行驗證：
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron範例有測試基礎設施：
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## 測試指引

### 內容驗證

存儲庫使用自動化翻譯工作流程。翻譯無需手動測試。

**手動驗證內容更改：**
1. 通過預覽 `.md` 文件檢查Markdown渲染
2. 確保所有鏈接指向有效目標
3. 測試文檔中包含的任何代碼片段
4. 確保圖片正確加載

### 範例應用程式測試

**模組08/範例/08（Electron應用程式）具有全面測試：**
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

**Python範例需手動測試：**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## 代碼風格指南

### Markdown內容

- 使用一致的標題層次結構（# 用於標題，## 用於主要部分，### 用於子部分）
- 包含帶有語言指定的代碼塊：```python, ```bash, ```javascript
- 遵循現有的表格、列表和強調格式
- 保持行可讀性（目標約80-100字符，但不嚴格）
- 使用相對鏈接指向內部引用

### Python代碼風格

- 遵循PEP 8規範
- 適當使用類型提示
- 為函數和類添加文檔字符串
- 使用有意義的變量名稱
- 保持函數專注且簡潔

### JavaScript/Node.js代碼風格

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**主要規範：**
- 範例08提供了ESLint配置
- 使用Prettier進行代碼格式化
- 使用現代ES6+語法
- 遵循代碼庫中的現有模式

## 拉取請求指南

### 貢獻工作流程

1. **Fork存儲庫**並從 `main` 創建新分支
2. **進行更改**，遵循代碼風格指南
3. **按照上述測試指引進行全面測試**
4. **使用清晰的消息提交**，遵循常規提交格式
5. **推送到您的Fork**並創建拉取請求
6. **回應維護者在審查過程中的反饋**

### 分支命名規範

- `feature/<module>-<description>` - 用於新功能或內容
- `fix/<module>-<description>` - 用於錯誤修復
- `docs/<description>` - 用於文檔改進
- `refactor/<description>` - 用於代碼重構

### 提交消息格式

遵循[常規提交](https://www.conventionalcommits.org/)：

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

所有貢獻者必須遵守[Microsoft開源行為準則](https://opensource.microsoft.com/codeofconduct/)。請在貢獻前查看 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

### 提交前

**對於內容更改：**
- 預覽所有修改的Markdown文件
- 驗證鏈接和圖片是否正常
- 檢查拼寫和語法錯誤

**對於範例代碼更改（模組08/範例/08）：**
```bash
npm run lint
npm test
```

**對於Python範例更改：**
- 測試範例是否成功運行
- 驗證錯誤處理是否正常
- 檢查與Foundry Local的兼容性

### 審查過程

- 教育內容更改將被審查以確保準確性和清晰度
- 代碼範例將被測試以確保功能正常
- 翻譯更新由GitHub Actions自動處理

## 翻譯系統

**重要事項：** 本存儲庫使用GitHub Actions進行自動翻譯。

- 翻譯存儲在 `/translations/` 目錄中（支持50多種語言）
- 通過 `co-op-translator.yml` 工作流程自動化
- **請勿手動編輯翻譯文件** - 它們將被覆蓋
- 僅編輯根目錄和模組目錄中的英文源文件
- 推送到 `main` 分支時，翻譯將自動生成

## Foundry Local 整合

大多數模組08範例需要Microsoft Foundry Local運行。

### 安裝與設置

**安裝Foundry Local：**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**安裝Python SDK：**
```bash
pip install foundry-local-sdk openai
```

### 啟動Foundry Local
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

### SDK使用（Python）
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

### 驗證Foundry Local
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

**注意**：使用 `FoundryLocalManager` 時，SDK會自動處理服務發現和模型加載。模型別名（如 `phi-3.5-mini`）確保選擇最適合您硬件的版本。

## 構建與部署

### 內容部署

本存儲庫主要是文檔內容 - 無需構建過程。

### 範例應用程式構建

**Electron應用程式（模組08/範例/08）：**
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

**Python範例：**
無需構建過程 - 範例直接使用Python解釋器運行。

## 常見問題與故障排除

> **提示**：檢查 [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) 了解已知問題和解決方案。

### 嚴重問題（阻塞）

#### Foundry Local未運行
**問題：** 範例因連接錯誤而失敗

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

#### Python虛擬環境問題
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

#### Electron構建問題
**問題：** npm安裝或構建失敗

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
**問題：** 翻譯PR與您的更改衝突

**解決方案：**
- 僅編輯英文源文件
- 讓自動翻譯工作流程處理翻譯
- 如果發生衝突，在翻譯合併後將 `main` 合併到您的分支

#### 模型下載失敗
**問題：** Foundry Local無法下載模型

**解決方案：**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## 額外資源

### 學習路徑
- **初學者路徑：** 模組01-02（7-9小時）
- **中級路徑：** 模組03-04（9-11小時）
- **高級路徑：** 模組05-07（12-15小時）
- **專家路徑：** 模組08（8-10小時）

### 核心模組內容
- **模組01：** EdgeAI基礎知識及實際案例研究
- **模組02：** 小型語言模型（SLM）家族及架構
- **模組03：** 本地和雲端部署策略
- **模組04：** 使用多種框架進行模型優化
- **模組05：** SLMOps - 生產運營
- **模組06：** AI代理及函數調用
- **模組07：** 平台特定實現
- **模組08：** Foundry Local工具包及10個全面範例

### 外部依賴項
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - 提供OpenAI兼容API的本地AI模型運行時
  - [文檔](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - 優化框架
- [Microsoft Olive](https://microsoft.github.io/Olive/) - 模型優化工具包
- [OpenVINO](https://docs.openvino.ai/) - Intel的優化工具包

## 專案特定備註

### 模組08範例應用程式

存儲庫包含10個全面範例應用程式：

1. **01-REST聊天快速入門** - 基本OpenAI SDK整合
2. **02-OpenAI SDK整合** - 高級SDK功能
3. **03-模型發現與基準測試** - 模型比較工具
4. **04-Chainlit RAG應用程式** - 檢索增強生成
5. **05-多代理協作** - 基本代理協調
6. **06-模型作為工具路由器** - 智能模型路由
7. **07-直接API客戶端** - 低級API整合
8. **08-Windows 11聊天應用程式** - 原生Electron桌面應用程式
9. **09-高級多代理系統** - 複雜代理協作
10. **10-Foundry工具框架** - LangChain/Semantic Kernel整合

每個範例展示了使用Foundry Local進行邊緣AI開發的不同方面。

### 性能考量

- SLMs已針對邊緣部署進行優化（2-16GB RAM）
- 本地推理提供 50-500 毫秒的響應時間  
- 量化技術實現 75% 的大小縮減，同時保留 85% 的性能  
- 使用本地模型進行即時對話  

### 安全性與隱私

- 所有處理均在本地進行——無需將數據發送至雲端  
- 適用於隱私敏感型應用（如醫療、金融）  
- 符合數據主權要求  
- Foundry Local 完全運行於本地硬件  

## 獲取幫助

### 文件

- **主 README**: [README.md](README.md) - 儲存庫概覽及學習路徑  
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
- **Microsoft 支援**: 對於企業支援，請聯絡 Microsoft 客戶服務  

### 其他資源

- **Microsoft Learn**: [AI 和機器學習學習路徑](https://learn.microsoft.com/training/browse/?products=ai-services)  
- **Foundry Local 文件**: [官方文件](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)  
- **社群範例**: 請查看 [GitHub 討論](https://github.com/microsoft/edgeai-for-beginners/discussions) 中的社群貢獻  

---

**這是一個教育性儲存庫，專注於教授 Edge AI 開發。主要的貢獻模式是改進教育內容以及添加/增強示例應用，以展示 Edge AI 概念。**  

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。