<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:25:40+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hk"
}
-->
# AGENTS.md

## 項目概覽

EdgeAI for Beginners 是一個全面的教育資源庫，教授使用小型語言模型 (SLMs) 進行邊緣 AI 開發。課程涵蓋邊緣 AI 基礎知識、模型部署、優化技術以及使用 Microsoft Foundry Local 和各種 AI 框架的生產級實現。

**主要技術：**
- Python 3.8+（AI/ML 示例的主要語言）
- .NET C#（AI/ML 示例）
- JavaScript/Node.js 與 Electron（用於桌面應用程式）
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI 框架：LangChain、Semantic Kernel、Chainlit
- 模型優化：Llama.cpp、Microsoft Olive、OpenVINO、Apple MLX

**資源庫類型：** 教育內容資源庫，包含 8 個模組和 10 個全面的示例應用程式

**架構：** 多模組學習路徑，提供展示邊緣 AI 部署模式的實用示例

## 資源庫結構

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

## 設置指令

### 資源庫設置

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python 示例設置（模組08和Python示例）

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Node.js 示例設置（示例08 - Windows 聊天應用程式）

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

模組08的示例需要 Foundry Local：

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## 開發工作流程

### 內容開發

此資源庫主要包含 **Markdown 教育內容**。進行更改時：

1. 編輯適當模組目錄中的 `.md` 文件
2. 遵循現有的格式模式
3. 確保代碼示例準確且已測試
4. 如果需要，更新相應的翻譯內容（或讓自動化處理）

### 示例應用程式開發

對於 Python 示例（示例 01-07, 09-10）：
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

對於 Electron 示例（示例 08）：
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### 測試示例應用程式

Python 示例沒有自動化測試，但可以通過運行它們進行驗證：
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron 示例具有測試基礎架構：
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## 測試指引

### 內容驗證

資源庫使用自動翻譯工作流程。翻譯不需要手動測試。

**內容更改的手動驗證：**
1. 通過預覽 `.md` 文件檢查 Markdown 渲染
2. 確保所有鏈接指向有效目標
3. 測試文檔中包含的任何代碼片段
4. 確保圖片正確加載

### 示例應用程式測試

**模組08/samples/08（Electron 應用程式）具有全面測試：**
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

**Python 示例需要手動測試：**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## 代碼風格指引

### Markdown 內容

- 使用一致的標題層次結構（# 用於標題，## 用於主要部分，### 用於子部分）
- 包含帶有語言指定的代碼塊：```python, ```bash, ```javascript
- 遵循現有的表格、列表和強調格式
- 保持行可讀性（目標約 80-100 字符，但不嚴格）
- 使用相對鏈接進行內部引用

### Python 代碼風格

- 遵循 PEP 8 規範
- 適當使用類型提示
- 為函數和類添加文檔字符串
- 使用有意義的變量名稱
- 保持函數專注且簡潔

### JavaScript/Node.js 代碼風格

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**主要規範：**
- 示例 08 提供 ESLint 配置
- 使用 Prettier 進行代碼格式化
- 使用現代 ES6+ 語法
- 遵循代碼庫中的現有模式

## 拉取請求指引

### 標題格式
```
[ModuleXX] Brief description of change
```
或
```
[Module08/samples/XX] Description for sample changes
```

### 提交前

**對於內容更改：**
- 預覽所有修改的 Markdown 文件
- 驗證鏈接和圖片是否正常工作
- 檢查拼寫和語法錯誤

**對於示例代碼更改（模組08/samples/08）：**
```bash
npm run lint
npm test
```

**對於 Python 示例更改：**
- 測試示例是否成功運行
- 驗證錯誤處理是否正常
- 檢查與 Foundry Local 的兼容性

### 審核流程

- 教育內容更改需檢查準確性和清晰度
- 代碼示例需測試功能性
- 翻譯更新由 GitHub Actions 自動處理

## 翻譯系統

**重要：** 此資源庫使用 GitHub Actions 進行自動翻譯。

- 翻譯存放於 `/translations/` 目錄（50+ 語言）
- 通過 `co-op-translator.yml` 工作流程自動化
- **請勿手動編輯翻譯文件** - 它們將被覆蓋
- 僅編輯根目錄和模組目錄中的英文源文件
- 翻譯會在推送到 `main` 分支時自動生成

## Foundry Local 集成

大多數模組08示例需要運行 Microsoft Foundry Local：

### 啟動 Foundry Local
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### 驗證 Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### 示例的環境變數

大多數示例使用以下環境變數：
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## 構建與部署

### 內容部署

此資源庫主要是文檔內容 - 不需要構建過程。

### 示例應用程式構建

**Electron 應用程式（模組08/samples/08）：**
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

**Python 示例：**
無需構建過程 - 示例直接使用 Python 解釋器運行。

## 常見問題與故障排除

### Foundry Local 未運行
**問題：** 示例因連接錯誤而失敗

**解決方案：**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python 虛擬環境問題
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

### Electron 構建問題
**問題：** npm 安裝或構建失敗

**解決方案：**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### 翻譯工作流程衝突
**問題：** 翻譯 PR 與您的更改衝突

**解決方案：**
- 僅編輯英文源文件
- 讓自動翻譯工作流程處理翻譯
- 如果發生衝突，在翻譯合併後將 `main` 合併到您的分支

## 附加資源

### 學習路徑
- **初學者路徑：** 模組 01-02（7-9 小時）
- **中級路徑：** 模組 03-04（9-11 小時）
- **高級路徑：** 模組 05-07（12-15 小時）
- **專家路徑：** 模組 08（8-10 小時）

### 主要模組內容
- **模組01：** 邊緣 AI 基礎知識和實際案例研究
- **模組02：** 小型語言模型 (SLM) 家族和架構
- **模組03：** 本地和雲端部署策略
- **模組04：** 使用多種框架進行模型優化
- **模組05：** SLMOps - 生產運營
- **模組06：** AI 代理和函數調用
- **模組07：** 平台特定實現
- **模組08：** Foundry Local 工具包與 10 個全面示例

### 外部依賴
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - 本地 AI 模型運行時
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - 優化框架
- [Microsoft Olive](https://microsoft.github.io/Olive/) - 模型優化工具包
- [OpenVINO](https://docs.openvino.ai/) - Intel 的優化工具包

## 項目特定備註

### 模組08示例應用程式

資源庫包含 10 個全面的示例應用程式：

1. **01-REST 聊天快速入門** - 基本 OpenAI SDK 集成
2. **02-OpenAI SDK 集成** - 高級 SDK 功能
3. **03-模型發現與基準測試** - 模型比較工具
4. **04-Chainlit RAG 應用程式** - 檢索增強生成
5. **05-多代理協調** - 基本代理協作
6. **06-模型作為工具路由器** - 智能模型路由
7. **07-直接 API 客戶端** - 低級 API 集成
8. **08-Windows 11 聊天應用程式** - 原生 Electron 桌面應用程式
9. **09-高級多代理系統** - 複雜代理協作
10. **10-Foundry 工具框架** - LangChain/Semantic Kernel 集成

每個示例展示了使用 Foundry Local 進行邊緣 AI 開發的不同方面。

### 性能考量

- SLMs 已針對邊緣部署進行優化（2-16GB RAM）
- 本地推理提供 50-500ms 響應時間
- 量化技術實現 75% 的大小減少，保留 85% 的性能
- 使用本地模型進行實時對話能力

### 安全性與隱私

- 所有處理均在本地進行 - 無數據發送到雲端
- 適合隱私敏感型應用（醫療、金融）
- 符合數據主權要求
- Foundry Local 完全在本地硬件上運行

---

**這是一個專注於教授邊緣 AI 開發的教育資源庫。主要貢獻模式是改進教育內容以及添加/增強示例應用程式，以展示邊緣 AI 概念。**

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。