<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T09:42:04+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "tw"
}
-->
# 更新日誌

所有 EdgeAI for Beginners 的重要更新都記錄於此。本專案採用基於日期的條目以及 Keep a Changelog 樣式（新增、變更、修復、移除、文件、移動）。

## 2025-09-23

### 變更 - 模組 08 大幅現代化
- **全面對齊 Microsoft Foundry-Local 儲存庫模式**
  - 更新所有程式碼範例以使用現代化的 `FoundryLocalManager` 和 OpenAI SDK 整合
  - 將已棄用的手動 `requests` 呼叫替換為正確的 SDK 使用方式
  - 實現模式與官方 Microsoft 文件和範例保持一致

- **05.AIPoweredAgents.md 現代化**：
  - 更新多代理協作以使用現代 SDK 模式
  - 增強協調器實現，加入高級功能（反饋迴路、性能監控）
  - 添加全面的錯誤處理和服務健康檢查
  - 正確引用本地範例（`samples/05/multi_agent_orchestration.ipynb`）
  - 更新函數調用範例以使用現代 `tools` 參數，替代已棄用的 `functions`
  - 添加具備監控和統計追蹤的生產級模式

- **06.ModelsAsTools.md 完全重寫**：
  - 用智能模型路由器實現替代基本工具註冊
  - 添加基於關鍵字的模型選擇，用於不同任務類型（通用、推理、程式碼、創意）
  - 整合基於環境的配置，提供靈活的模型分配
  - 加強服務健康監控和錯誤處理
  - 添加生產部署模式，包含請求監控和性能追蹤
  - 與本地實現保持一致（`samples/06/router.py` 和 `samples/06/model_router.ipynb`）

- **文件結構改進**：
  - 添加概述部分，突出現代化和 SDK 對齊
  - 使用表情符號和更好的格式提升可讀性
  - 在文件中正確引用本地範例檔案
  - 包括生產級實現指導和最佳實踐

### 新增
- 模組 08 文件中新增全面概述部分，突出現代 SDK 整合
- 架構亮點，展示高級功能（多代理系統、智能路由）
- 直接引用本地範例實現，提供實操體驗
- 生產部署指導，包含監控和錯誤處理模式
- 互動式 Jupyter notebook 範例，包含高級功能和基準測試

### 修復
- 文件與實際範例實現之間的對齊差異
- 模組 08 中過時的 SDK 使用模式
- 缺少對全面本地範例庫的引用
- 不一致的實現方法，跨不同部分進行修正

---

## 2025-09-18

### 新增
- 模組 08：Microsoft Foundry Local – 完整開發者工具包
  - 六個課程：設置、Azure AI Foundry 整合、開源模型、尖端演示、代理和模型作為工具
  - 可執行範例位於 `Module08/samples/01`–`06`，附有 Windows cmd 指令
    - `01` REST 快速聊天（`chat_quickstart.py`）
    - `02` SDK 快速入門，支援 OpenAI/Foundry Local 和 Azure OpenAI（`sdk_quickstart.py`）
    - `03` CLI 列表與基準測試（`list_and_bench.cmd`）
    - `04` Chainlit 演示（`app.py`）
    - `05` 多代理協作（`python -m samples.05.agents.coordinator`）
    - `06` 模型作為工具的路由器（`router.py`）
- Session 2 SDK 範例中新增 Azure OpenAI 支援，使用環境變數配置
- `.vscode/settings.json` 指向 `Module08/.venv`，改善 Python 分析解析
- `.env` 提供 `PYTHONPATH` 提示，增強 VS Code/Pylance 的識別能力

### 變更
- 模組 08 文件和範例中預設模型更新為 `phi-4-mini`；移除剩餘的 `phi-3.5` 提及
- 路由器（`Module08/samples/06/router.py`）改進：
  - 通過 `foundry service status` 使用正則表達式解析進行端點發現
  - 啟動時進行 `/v1/models` 健康檢查
  - 環境可配置的模型註冊（`GENERAL_MODEL`、`REASONING_MODEL`、`CODE_MODEL`、`TOOL_REGISTRY` JSON）
- 需求更新：`Module08/requirements.txt` 現在包含 `openai`（以及 `requests`、`chainlit`）
- Chainlit 範例指導進一步明確，並添加故障排除；通過工作區設置解決導入問題

### 修復
- 解決導入問題：
  - 路由器不再依賴不存在的 `utils` 模組；函數已內嵌
  - 協調器使用相對導入（`from .specialists import ...`），並通過模組路徑調用
  - VS Code/Pylance 配置解決 `chainlit` 和套件導入問題
- 修正 `STUDY_GUIDE.md` 中的小錯字，並新增模組 08 覆蓋範圍

### 移除
- 刪除未使用的 `Module08/infra/obs.py`，並移除空的 `infra/` 目錄；可選的可觀察性模式保留在文件中

### 移動
- 將模組 08 演示整合至 `Module08/samples`，並按課程編號分文件夾
  - 將 Chainlit 應用移至 `samples/04`
  - 將代理移至 `samples/05`，並添加 `__init__.py` 文件以解決套件解析問題

### 文件
- 模組 08 課程文件和所有範例 README 增強，加入 Microsoft Learn 和可信供應商的引用
- 更新 `Module08/README.md`，新增範例概述、路由器配置和驗證提示
- 驗證 `Module07/README.md` 中的 Windows Foundry Local 部分，與 Learn 文件保持一致
- 更新 `STUDY_GUIDE.md`：
  - 新增模組 08 至概述、課程表、進度追蹤器
  - 新增全面的參考部分（Foundry Local、Azure AI、Olive、ONNX Runtime、OpenVINO、MLX、Llama.cpp、vLLM、Ollama、AI Toolkit、Windows ML）

---

## 歷史（摘要）
- 建立課程架構和模組（模組 01–07）
- 迭代內容現代化、格式標準化，並新增案例研究
- 擴展優化框架覆蓋範圍（Llama.cpp、Olive、OpenVINO、Apple MLX）

## 未發布 / 待辦事項（提案）
- 可選的每個範例煙霧測試以驗證 Foundry Local 可用性
- 審查翻譯以對齊模型引用（例如 `phi-4-mini`）
- 添加最小的 pyright 配置，以便團隊偏好工作區範圍的嚴格性

---

