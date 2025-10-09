<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T07:55:35+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "mo"
}
-->
# 更新日誌

所有 EdgeAI for Beginners 的重要更新都記錄於此。本專案採用基於日期的條目以及「保持更新日誌」的風格（新增、變更、修復、移除、文件、移動）。

## 2025-10-08

### 新增 - 工作坊全面更新
- **工作坊 README.md 完整重寫**：
  - 新增全面介紹，說明 Edge AI 的價值主張（隱私、性能、成本）
  - 建立 6 個核心學習目標及詳細能力描述
  - 新增學習成果表格，包括交付物和能力矩陣
  - 增加行業相關的職業技能部分
  - 新增快速入門指南，包括先決條件和三步設置流程
  - 建立 Python 範例資源表（8 個檔案及執行時間）
  - 新增 Jupyter 筆記本表格（8 個筆記本及難度評級）
  - 建立文件表格（7 個關鍵文件及「使用時機」指導）
  - 新增針對不同技能水平的學習路徑建議

- **工作坊驗證和測試基礎設施**：
  - 建立 `scripts/validate_samples.py` - 全面驗證工具，用於語法、匯入和最佳實踐檢查
  - 建立 `scripts/test_samples.py` - 用於所有 Python 範例的煙霧測試執行器
  - 在 `scripts/README.md` 中新增驗證文件

- **全面文件**：
  - 建立 `SAMPLES_UPDATE_SUMMARY.md` - 400+ 行詳細指南，涵蓋所有改進
  - 建立 `UPDATE_COMPLETE.md` - 更新完成的執行摘要
  - 建立 `QUICK_REFERENCE.md` - 工作坊快速參考卡

### 變更 - 工作坊 Python 範例現代化
- **所有 8 個 Python 範例更新至最佳實踐**：
  - 增強所有 I/O 操作的錯誤處理，加入 try-except 塊
  - 新增類型提示和全面的文檔字符串
  - 實施一致的 [INFO]/[ERROR]/[RESULT] 日誌模式
  - 為可選匯入提供安裝提示保護
  - 改善所有範例中的用戶反饋

- **session01/chat_bootstrap.py**：
  - 增強客戶端初始化，提供全面的錯誤訊息
  - 改善流式錯誤處理，加入塊驗證
  - 增加服務不可用的更好異常處理

- **session02/rag_pipeline.py**：
  - 為 sentence-transformers 新增匯入保護及安裝提示
  - 增強嵌入和生成操作的錯誤處理
  - 改善輸出格式，提供結構化結果

- **session02/rag_eval_ragas.py**：
  - 保護可選匯入（ragas、datasets），提供用戶友好的錯誤訊息
  - 新增評估指標的錯誤處理
  - 改善評估結果的輸出格式

- **session03/benchmark_oss_models.py**：
  - 實施優雅降級（在模型失敗時繼續執行）
  - 新增詳細進度報告及每模型錯誤處理
  - 增強統計計算，提供全面的錯誤恢復

- **session04/model_compare.py**：
  - 新增類型提示（Tuple 返回類型）
  - 改善輸出格式，提供結構化 JSON 結果
  - 實施每模型錯誤處理及恢復

- **session05/agents_orchestrator.py**：
  - 增強 Agent.act()，提供全面的文檔字符串
  - 新增管道錯誤處理，提供逐步日誌記錄
  - 改善記憶體管理及狀態追蹤

- **session06/models_router.py**：
  - 增強所有路由組件的函數文檔
  - 在 route() 函數中新增詳細日誌記錄
  - 改善測試輸出，提供結構化結果

- **session06/models_pipeline.py**：
  - 新增 chat() 輔助函數的錯誤處理
  - 增強 pipeline()，提供階段日誌記錄及進度報告
  - 改善 main()，提供全面的錯誤恢復

### 文件 - 工作坊文件增強
- 更新主 README.md，新增工作坊部分，突顯動手學習路徑
- 增強 STUDY_GUIDE.md，新增全面的工作坊部分，包括：
  - 學習目標及學習重點領域
  - 自我評估問題
  - 動手練習及時間估算
  - 集中及兼職學習的時間分配
  - 新增工作坊至進度追蹤模板
- 將時間分配指南從 20 小時更新至 30 小時（包括工作坊）
- 新增工作坊範例描述及學習成果至 README

### 修復
- 解決工作坊範例中不一致的錯誤處理模式
- 修復可選依賴匯入錯誤，加入正確的保護
- 修正關鍵函數中缺失的類型提示
- 解決錯誤場景中用戶反饋不足的問題
- 修復驗證問題，加入全面的測試基礎設施

---

## 2025-09-23

### 變更 - 模組 08 重大現代化
- **全面對齊 Microsoft Foundry-Local 儲存庫模式**：
  - 更新所有代碼範例，使用現代 `FoundryLocalManager` 和 OpenAI SDK 集成
  - 用正確的 SDK 使用取代過時的手動 `requests` 調用
  - 將實現模式與官方 Microsoft 文件及範例對齊

- **05.AIPoweredAgents.md 現代化**：
  - 更新多代理協作，使用現代 SDK 模式
  - 增強協調器實現，加入高級功能（反饋迴路、性能監控）
  - 新增全面的錯誤處理及服務健康檢查
  - 正確引用本地範例（`samples/05/multi_agent_orchestration.ipynb`）
  - 更新函數調用範例，使用現代 `tools` 參數取代過時的 `functions`
  - 新增生產就緒模式，加入監控及統計追蹤

- **06.ModelsAsTools.md 完整重寫**：
  - 用智能模型路由器實現取代基本工具註冊
  - 新增基於關鍵字的模型選擇，用於不同任務類型（通用、推理、代碼、創意）
  - 集成基於環境的配置，提供靈活的模型分配
  - 增強全面的服務健康監控及錯誤處理
  - 新增生產部署模式，加入請求監控及性能追蹤
  - 與本地實現對齊（`samples/06/router.py` 和 `samples/06/model_router.ipynb`）

- **文件結構改進**：
  - 新增概述部分，突顯現代化及 SDK 對齊
  - 增強表情符號及更好的格式，改善可讀性
  - 在文件中正確引用本地範例檔案
  - 包括生產就緒實現指導及最佳實踐

### 新增
- 模組 08 文件中的全面概述部分，突顯現代 SDK 集成
- 架構亮點，展示高級功能（多代理系統、智能路由）
- 本地範例實現的直接引用，提供動手體驗
- 生產部署指導，加入監控及錯誤處理模式
- 互動式 Jupyter 筆記本範例，包含高級功能及基準測試

### 修復
- 文件與實際範例實現之間的對齊差異
- 模組 08 中過時的 SDK 使用模式
- 缺失的全面本地範例庫引用
- 不一致的實現方法，跨不同部分

---

## 2025-09-18

### 新增
- 模組 08：Microsoft Foundry Local – 完整開發者工具包
  - 六個會話：設置、Azure AI Foundry 集成、開源模型、尖端演示、代理及模型作為工具
  - 可執行範例位於 `Module08/samples/01`–`06`，附 Windows cmd 指令
    - `01` REST 快速聊天（`chat_quickstart.py`）
    - `02` SDK 快速入門，支持 OpenAI/Foundry Local 和 Azure OpenAI（`sdk_quickstart.py`）
    - `03` CLI 列表及基準測試（`list_and_bench.cmd`）
    - `04` Chainlit 演示（`app.py`）
    - `05` 多代理協作（`python -m samples.05.agents.coordinator`）
    - `06` 模型作為工具路由器（`router.py`）
- Session 2 SDK 範例中的 Azure OpenAI 支持，加入環境變數配置
- `.vscode/settings.json` 指向 `Module08/.venv`，改善 Python 分析解析
- `.env` 提供 `PYTHONPATH` 提示，支持 VS Code/Pylance

### 變更
- 模組 08 文件及範例中的默認模型更新為 `phi-4-mini`；移除剩餘的 `phi-3.5` 提及
- 路由器（`Module08/samples/06/router.py`）改進：
  - 通過 `foundry service status` 進行端點發現，使用正則表達式解析
  - 啟動時進行 `/v1/models` 健康檢查
  - 環境可配置的模型註冊（`GENERAL_MODEL`、`REASONING_MODEL`、`CODE_MODEL`、`TOOL_REGISTRY` JSON）
- 要求更新：`Module08/requirements.txt` 現在包括 `openai`（以及 `requests`、`chainlit`）
- Chainlit 範例指導明確化，新增故障排除；通過工作區設置解決匯入問題

### 修復
- 解決匯入問題：
  - 路由器不再依賴不存在的 `utils` 模組；函數已內聯
  - 協調器使用相對匯入（`from .specialists import ...`），並通過模組路徑調用
  - VS Code/Pylance 配置解決 `chainlit` 和套件匯入
- 修正 `STUDY_GUIDE.md` 中的小錯字，新增模組 08 覆蓋範圍

### 移除
- 刪除未使用的 `Module08/infra/obs.py`，並移除空的 `infra/` 目錄；可選的可觀察性模式保留在文件中

### 移動
- 將模組 08 演示整合至 `Module08/samples`，按會話編號文件夾分類
  - 將 Chainlit 應用移至 `samples/04`
  - 將代理移至 `samples/05`，並新增 `__init__.py` 文件以支持套件解析

### 文件
- 模組 08 會話文件及所有範例 README 增強，加入 Microsoft Learn 和可信供應商引用
- `Module08/README.md` 更新，新增範例概述、路由器配置及驗證提示
- `Module07/README.md` Windows Foundry Local 部分已根據 Learn 文件驗證
- `STUDY_GUIDE.md` 更新：
  - 新增模組 08 至概述、時間表、進度追蹤器
  - 新增全面的參考部分（Foundry Local、Azure AI、Olive、ONNX Runtime、OpenVINO、MLX、Llama.cpp、vLLM、Ollama、AI Toolkit、Windows ML）

---

## 歷史（摘要）
- 課程架構及模組建立（模組 01–07）
- 內容現代化、格式標準化及新增案例研究的迭代更新
- 擴展優化框架覆蓋範圍（Llama.cpp、Olive、OpenVINO、Apple MLX）

## 未發布 / 待辦事項（提案）
- 可選的每範例煙霧測試，用於驗證 Foundry Local 可用性
- 審查翻譯以對齊模型引用（例如 `phi-4-mini`）
- 如果團隊偏好工作區範圍的嚴格性，新增最小的 pyright 配置

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。