<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T16:03:44+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "tw"
}
-->
# 更新日誌

所有關於 EdgeAI for Beginners 的重要更新都記錄於此。本專案採用基於日期的條目以及「保持更新日誌」的風格（新增、變更、修正、移除、文件、移動）。

## 2025-10-08

### 新增 - 工作坊全面更新
- **工作坊 README.md 完整重寫**：
  - 新增全面介紹，說明 Edge AI 的價值主張（隱私、效能、成本）
  - 建立 6 個核心學習目標及詳細能力要求
  - 新增學習成果表，包括交付項目及能力矩陣
  - 加入職業技能部分，突顯行業相關性
  - 新增快速入門指南，包括先決條件及三步驟設置
  - 建立 Python 範例資源表（8 個檔案及執行時間）
  - 新增 Jupyter 筆記本表（8 個筆記本及難度評級）
  - 建立文件表（7 個關鍵文件及「使用時機」指導）
  - 新增針對不同技能水平的學習路徑建議

- **工作坊驗證及測試基礎設施**：
  - 建立 `scripts/validate_samples.py` - 全面驗證工具，用於語法、匯入及最佳實踐
  - 建立 `scripts/test_samples.py` - 用於所有 Python 範例的煙霧測試執行器
  - 在 `scripts/README.md` 中新增驗證文件

- **全面文件**：
  - 建立 `SAMPLES_UPDATE_SUMMARY.md` - 超過 400 行的詳細指南，涵蓋所有改進
  - 建立 `UPDATE_COMPLETE.md` - 更新完成的執行摘要
  - 建立 `QUICK_REFERENCE.md` - 工作坊的快速參考卡

### 變更 - 工作坊 Python 範例現代化
- **所有 8 個 Python 範例更新至最佳實踐**：
  - 增強所有 I/O 操作的錯誤處理，加入 try-except 塊
  - 新增類型提示及全面的 docstrings
  - 實施一致的 [INFO]/[ERROR]/[RESULT] 日誌模式
  - 為可選匯入提供安裝提示保護
  - 改善所有範例中的用戶反饋

- **session01/chat_bootstrap.py**：
  - 增強客戶端初始化，提供全面的錯誤訊息
  - 改善流式錯誤處理，加入塊驗證
  - 增加服務不可用的更好例外處理

- **session02/rag_pipeline.py**：
  - 為 sentence-transformers 新增匯入保護及安裝提示
  - 增強嵌入及生成操作的錯誤處理
  - 改善輸出格式，提供結構化結果

- **session02/rag_eval_ragas.py**：
  - 保護可選匯入（ragas、datasets），提供用戶友好的錯誤訊息
  - 新增評估指標的錯誤處理
  - 改善評估結果的輸出格式

- **session03/benchmark_oss_models.py**：
  - 實施優雅降級（模型失敗時繼續執行）
  - 新增詳細進度報告及每模型錯誤處理
  - 增強統計計算，提供全面的錯誤恢復

- **session04/model_compare.py**：
  - 新增類型提示（Tuple 返回類型）
  - 改善輸出格式，提供結構化 JSON 結果
  - 實施每模型錯誤處理及恢復

- **session05/agents_orchestrator.py**：
  - 增強 Agent.act()，提供全面的 docstrings
  - 新增管道錯誤處理，提供逐階段日誌
  - 改善記憶體管理及狀態追蹤

- **session06/models_router.py**：
  - 增強所有路由組件的函數文件
  - 在 route() 函數中新增詳細日誌
  - 改善測試輸出，提供結構化結果

- **session06/models_pipeline.py**：
  - 新增 chat() 輔助函數的錯誤處理
  - 增強 pipeline()，提供階段日誌及進度報告
  - 改善 main()，提供全面的錯誤恢復

### 文件 - 工作坊文件增強
- 更新主 README.md，新增工作坊部分，突顯動手學習路徑
- 增強 STUDY_GUIDE.md，新增全面的工作坊部分，包括：
  - 學習目標及學習重點
  - 自我評估問題
  - 動手練習及時間估算
  - 集中及兼職學習的時間分配
  - 在進度追蹤模板中新增工作坊
- 將時間分配指南從 20 小時更新至 30 小時（包括工作坊）
- 在 README 中新增工作坊範例描述及學習成果

### 修正
- 解決工作坊範例中不一致的錯誤處理模式
- 修正可選依賴匯入錯誤，加入正確的保護
- 修正關鍵函數中缺失的類型提示
- 解決錯誤場景中用戶反饋不足的問題
- 修正驗證問題，提供全面的測試基礎設施

---

## 2025-09-23

### 變更 - 模組 08 的重大現代化
- **全面對齊 Microsoft Foundry-Local 儲存庫模式**：
  - 更新所有程式碼範例，使用現代 `FoundryLocalManager` 及 OpenAI SDK 整合
  - 用正確的 SDK 使用取代過時的手動 `requests` 呼叫
  - 將實現模式與官方 Microsoft 文件及範例對齊

- **05.AIPoweredAgents.md 現代化**：
  - 更新多代理協作，使用現代 SDK 模式
  - 增強協調器實現，加入高級功能（反饋迴路、效能監控）
  - 新增全面的錯誤處理及服務健康檢查
  - 正確引用本地範例（`samples/05/multi_agent_orchestration.ipynb`）
  - 更新函數調用範例，使用現代 `tools` 參數取代過時的 `functions`
  - 新增生產就緒模式，提供監控及統計追蹤

- **06.ModelsAsTools.md 完整重寫**：
  - 用智能模型路由器實現取代基本工具註冊表
  - 新增基於關鍵字的模型選擇，用於不同任務類型（通用、推理、程式碼、創意）
  - 整合基於環境的配置，提供靈活的模型分配
  - 增強全面的服務健康監控及錯誤處理
  - 新增生產部署模式，提供請求監控及效能追蹤
  - 與本地實現對齊（`samples/06/router.py` 及 `samples/06/model_router.ipynb`）

- **文件結構改進**：
  - 新增概述部分，突顯現代化及 SDK 對齊
  - 增強表情符號及更好的格式，改善可讀性
  - 在文件中正確引用本地範例檔案
  - 包括生產就緒實現指導及最佳實踐

### 新增
- 模組 08 文件中的全面概述部分，突顯現代 SDK 整合
- 架構亮點，展示高級功能（多代理系統、智能路由）
- 直接引用本地範例實現，提供動手體驗
- 生產部署指導，提供監控及錯誤處理模式
- 互動式 Jupyter 筆記本範例，包含高級功能及基準測試

### 修正
- 文件與實際範例實現之間的對齊差異
- 模組 08 中過時的 SDK 使用模式
- 缺失的全面本地範例庫引用
- 不一致的實現方法，跨不同部分

---

## 2025-09-18

### 新增
- 模組 08：Microsoft Foundry Local – 完整開發者工具包
  - 六個會話：設置、Azure AI Foundry 整合、開源模型、尖端演示、代理及模型作為工具
  - 可執行範例位於 `Module08/samples/01`–`06`，附 Windows cmd 指令
    - `01` REST 快速聊天（`chat_quickstart.py`）
    - `02` SDK 快速入門，支援 OpenAI/Foundry Local 及 Azure OpenAI（`sdk_quickstart.py`）
    - `03` CLI 列表及基準測試（`list_and_bench.cmd`）
    - `04` Chainlit 演示（`app.py`）
    - `05` 多代理協作（`python -m samples.05.agents.coordinator`）
    - `06` 模型作為工具路由器（`router.py`）
- Session 2 SDK 範例中的 Azure OpenAI 支援，提供環境變數配置
- `.vscode/settings.json` 指向 `Module08/.venv`，改善 Python 分析解析
- `.env` 提供 `PYTHONPATH` 提示，支援 VS Code/Pylance

### 變更
- 模組 08 文件及範例中的預設模型更新為 `phi-4-mini`；移除模組 08 中剩餘的 `phi-3.5` 提及
- 路由器（`Module08/samples/06/router.py`）改進：
  - 通過 `foundry service status` 進行端點發現，使用正則表達式解析
  - 啟動時進行 `/v1/models` 健康檢查
  - 環境可配置的模型註冊表（`GENERAL_MODEL`、`REASONING_MODEL`、`CODE_MODEL`、`TOOL_REGISTRY` JSON）
- 要求更新：`Module08/requirements.txt` 現在包括 `openai`（以及 `requests`、`chainlit`）
- Chainlit 範例指導明確化，新增故障排除；通過工作區設置解析匯入

### 修正
- 解決匯入問題：
  - 路由器不再依賴不存在的 `utils` 模組；函數已內聯
  - 協調器使用相對匯入（`from .specialists import ...`），並通過模組路徑調用
  - VS Code/Pylance 配置，解析 `chainlit` 及套件匯入
- 修正 `STUDY_GUIDE.md` 中的小錯字，新增模組 08 覆蓋範圍

### 移除
- 刪除未使用的 `Module08/infra/obs.py`，移除空的 `infra/` 目錄；可選的可觀察性模式保留在文件中

### 移動
- 將模組 08 演示整合至 `Module08/samples`，按會話編號的文件夾分類
  - 將 Chainlit 應用移至 `samples/04`
  - 將代理移至 `samples/05`，並新增 `__init__.py` 文件以解析套件

### 文件
- 模組 08 會話文件及所有範例 README 增強，加入 Microsoft Learn 及可信供應商引用
- `Module08/README.md` 更新，新增範例概述、路由器配置及驗證提示
- `Module07/README.md` Windows Foundry Local 部分已根據 Learn 文件驗證
- `STUDY_GUIDE.md` 更新：
  - 在概述、時間表、進度追蹤器中新增模組 08
  - 新增全面的引用部分（Foundry Local、Azure AI、Olive、ONNX Runtime、OpenVINO、MLX、Llama.cpp、vLLM、Ollama、AI Toolkit、Windows ML）

---

## 歷史（摘要）
- 課程架構及模組建立（模組 01–07）
- 內容逐步現代化、格式標準化及新增案例研究
- 擴展優化框架覆蓋範圍（Llama.cpp、Olive、OpenVINO、Apple MLX）

## 未發布 / 待辦事項（提案）
- 可選的每範例煙霧測試，用於驗證 Foundry Local 可用性
- 審查翻譯以對齊模型引用（例如 `phi-4-mini`）
- 如果團隊偏好工作區範圍的嚴格性，新增最小的 pyright 配置

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。