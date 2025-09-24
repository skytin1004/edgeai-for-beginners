<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T14:24:10+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "mo"
}
-->
# 更新日誌

這裡記錄了 EdgeAI for Beginners 的所有重要變更。本專案採用基於日期的條目記錄，並遵循 Keep a Changelog 的風格（新增、變更、修復、移除、文件、移動）。

## 2025-09-23

### 變更 - 模組 08 的重大現代化更新
- **全面對齊 Microsoft Foundry-Local 的倉庫模式**
  - 更新所有程式碼範例以使用現代化的 `FoundryLocalManager` 和 OpenAI SDK 整合
  - 將已棄用的手動 `requests` 呼叫替換為正確的 SDK 使用方式
  - 實現模式與官方 Microsoft 文件和範例保持一致

- **05.AIPoweredAgents.md 的現代化**：
  - 更新多代理協作以使用現代 SDK 模式
  - 增強協調器實現，加入進階功能（反饋迴路、效能監控）
  - 增加全面的錯誤處理和服務健康檢查
  - 正確整合本地範例參考（`samples/05/multi_agent_orchestration.ipynb`）
  - 更新函數呼叫範例以使用現代化的 `tools` 參數，取代已棄用的 `functions`
  - 增加具備監控和統計追蹤的生產級模式

- **06.ModelsAsTools.md 的全面重寫**：
  - 用智能模型路由器實現取代基本工具註冊
  - 增加基於關鍵字的模型選擇功能，適用於不同任務類型（通用、推理、程式碼、創意）
  - 整合基於環境的配置，提供靈活的模型分配
  - 加強服務健康監控和錯誤處理
  - 增加生產部署模式，包含請求監控和效能追蹤
  - 與本地實現對齊（`samples/06/router.py` 和 `samples/06/model_router.ipynb`）

- **文件結構改進**：
  - 增加概述部分，強調現代化和 SDK 對齊
  - 使用表情符號和更佳的格式提升可讀性
  - 在文件中正確加入本地範例檔案的參考
  - 包含生產級實現指導和最佳實踐

### 新增
- 模組 08 文件中的全面概述部分，強調現代 SDK 整合
- 架構亮點，展示進階功能（多代理系統、智能路由）
- 直接參考本地範例實現，提供實作體驗
- 生產部署指導，包含監控和錯誤處理模式
- 互動式 Jupyter notebook 範例，包含進階功能和基準測試

### 修復
- 文件與實際範例實現之間的對齊差異
- 模組 08 中過時的 SDK 使用模式
- 缺少對全面本地範例庫的參考
- 不一致的實現方式，跨不同部分進行統一

---

## 2025-09-18

### 新增
- 模組 08：Microsoft Foundry Local – 完整開發工具包
  - 六個課程：設置、Azure AI Foundry 整合、開源模型、前沿演示、代理和模型作為工具
  - 可執行範例位於 `Module08/samples/01`–`06`，附帶 Windows cmd 指令
    - `01` REST 快速聊天（`chat_quickstart.py`）
    - `02` 使用 OpenAI/Foundry Local 和 Azure OpenAI 支援的 SDK 快速入門（`sdk_quickstart.py`）
    - `03` CLI 列表與基準測試（`list_and_bench.cmd`）
    - `04` Chainlit 演示（`app.py`）
    - `05` 多代理協作（`python -m samples.05.agents.coordinator`）
    - `06` 模型作為工具的路由器（`router.py`）
- 在 Session 2 SDK 範例中新增 Azure OpenAI 支援，並配置環境變數
- `.vscode/settings.json` 指向 `Module08/.venv`，改善 Python 分析解析
- `.env` 提供 `PYTHONPATH` 提示，增強 VS Code/Pylance 的辨識能力

### 變更
- 模組 08 文件和範例的預設模型更新為 `phi-4-mini`；移除所有 `phi-3.5` 的提及
- 路由器（`Module08/samples/06/router.py`）改進：
  - 通過 `foundry service status` 和正則表達式解析進行端點發現
  - 啟動時執行 `/v1/models` 健康檢查
  - 環境可配置的模型註冊（`GENERAL_MODEL`、`REASONING_MODEL`、`CODE_MODEL`、`TOOL_REGISTRY` JSON）
- 更新需求：`Module08/requirements.txt` 現在包含 `openai`（以及 `requests`、`chainlit`）
- 明確 Chainlit 範例指導並新增故障排除；通過工作區設置解決導入問題

### 修復
- 解決導入問題：
  - 路由器不再依賴不存在的 `utils` 模組；相關功能已內嵌
  - 協調器使用相對導入（`from .specialists import ...`），並通過模組路徑調用
  - VS Code/Pylance 配置解決 `chainlit` 和套件導入問題
- 修正 `STUDY_GUIDE.md` 中的小錯字，並新增模組 08 的覆蓋範圍

### 移除
- 刪除未使用的 `Module08/infra/obs.py`，並移除空的 `infra/` 目錄；觀察模式作為可選內容保留在文件中

### 移動
- 將模組 08 的演示統一移至 `Module08/samples`，並按課程編號分文件夾
  - 將 Chainlit 應用移至 `samples/04`
  - 將代理移至 `samples/05`，並新增 `__init__.py` 文件以解決套件解析問題

### 文件
- 豐富模組 08 的課程文件和所有範例的 README，加入 Microsoft Learn 和可信供應商的參考
- 更新 `Module08/README.md`，新增範例概述、路由器配置和驗證提示
- 驗證 `Module07/README.md` 中的 Windows Foundry Local 部分，與 Learn 文件保持一致
- 更新 `STUDY_GUIDE.md`：
  - 在概述、課程表和進度追蹤中新增模組 08
  - 增加全面的參考部分（Foundry Local、Azure AI、Olive、ONNX Runtime、OpenVINO、MLX、Llama.cpp、vLLM、Ollama、AI Toolkit、Windows ML）

---

## 歷史記錄（摘要）
- 建立課程架構和模組（模組 01–07）
- 持續進行內容現代化、格式標準化，並新增案例研究
- 擴展優化框架的覆蓋範圍（Llama.cpp、Olive、OpenVINO、Apple MLX）

## 未發布 / 待辦事項（建議）
- 為每個範例新增可選的煙霧測試，以驗證 Foundry Local 的可用性
- 審查翻譯，確保模型參考（例如 `phi-4-mini`）的一致性
- 如果團隊偏好工作區級別的嚴格性，新增最小化的 pyright 配置

---

