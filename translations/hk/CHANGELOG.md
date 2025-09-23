<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T11:41:12+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "hk"
}
-->
# 更新日誌

這裡記錄了 EdgeAI for Beginners 的所有重要變更。本專案採用基於日期的條目和 Keep a Changelog 的風格（新增、變更、修復、移除、文件、移動）。

## 2025-09-18

### 新增
- 模組 08：Microsoft Foundry Local – 完整開發者工具包
  - 六個課程：設置、Azure AI Foundry 整合、開源模型、前沿演示、代理和模型作為工具
  - 可執行範例位於 `Module08/samples/01`–`06`，附有 Windows cmd 指令
    - `01` REST 快速聊天（`chat_quickstart.py`）
    - `02` SDK 快速入門，支援 OpenAI/Foundry Local 和 Azure OpenAI（`sdk_quickstart.py`）
    - `03` CLI 列表與基準測試（`list_and_bench.cmd`）
    - `04` Chainlit 演示（`app.py`）
    - `05` 多代理協調（`python -m samples.05.agents.coordinator`）
    - `06` 模型作為工具的路由器（`router.py`）
- 在課程 2 的 SDK 範例中新增 Azure OpenAI 支援，並可透過環境變數進行配置
- `.vscode/settings.json` 指向 `Module08/.venv`，以改善 Python 分析解析
- `.env` 文件新增 `PYTHONPATH` 提示，提升 VS Code/Pylance 的辨識能力

### 變更
- 模組 08 文件和範例的預設模型更新為 `phi-4-mini`，移除所有 `phi-3.5` 的相關提及
- 路由器（`Module08/samples/06/router.py`）改進：
  - 通過 `foundry service status` 和正則表達式解析進行端點發現
  - 啟動時執行 `/v1/models` 健康檢查
  - 支援環境變數配置的模型註冊表（`GENERAL_MODEL`、`REASONING_MODEL`、`CODE_MODEL`、`TOOL_REGISTRY` JSON）
- 更新需求：`Module08/requirements.txt` 現在包含 `openai`（與 `requests`、`chainlit` 一同列入）
- 明確 Chainlit 範例指導並新增故障排除；通過工作區設置解決導入問題

### 修復
- 解決導入問題：
  - 路由器不再依賴不存在的 `utils` 模組；相關功能已內嵌
  - 協調器使用相對導入（`from .specialists import ...`），並通過模組路徑調用
  - 配置 VS Code/Pylance 以解決 `chainlit` 和套件導入問題
- 修正 `STUDY_GUIDE.md` 中的小錯字，並新增模組 08 的相關內容

### 移除
- 刪除未使用的 `Module08/infra/obs.py`，並移除空的 `infra/` 目錄；觀察性模式作為可選內容保留在文件中

### 移動
- 將模組 08 的演示統一整合到 `Module08/samples`，並按課程編號分文件夾
  - 將 Chainlit 應用移至 `samples/04`
  - 將代理移至 `samples/05`，並新增 `__init__.py` 文件以解決套件解析問題

### 文件
- 豐富模組 08 的課程文件和所有範例的 README，新增 Microsoft Learn 和可信供應商的參考資料
- 更新 `Module08/README.md`，新增範例概覽、路由器配置和驗證提示
- 驗證 `Module07/README.md` 中的 Windows Foundry Local 部分與 Learn 文件的一致性
- 更新 `STUDY_GUIDE.md`：
  - 在概覽、時間表和進度追蹤中新增模組 08
  - 新增全面的參考資料部分（Foundry Local、Azure AI、Olive、ONNX Runtime、OpenVINO、MLX、Llama.cpp、vLLM、Ollama、AI Toolkit、Windows ML）

---

## 歷史記錄（摘要）
- 建立課程架構和模組（模組 01–07）
- 持續更新內容，標準化格式，並新增案例研究
- 擴展優化框架的覆蓋範圍（Llama.cpp、Olive、OpenVINO、Apple MLX）

## 未發布 / 待辦事項（建議）
- 為每個範例新增可選的煙霧測試，以驗證 Foundry Local 的可用性
- 審核翻譯內容，確保模型參考（如 `phi-4-mini`）的一致性
- 如果團隊偏好全域嚴格模式，新增最小化的 pyright 配置

---

