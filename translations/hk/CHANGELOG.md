<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T16:08:38+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "hk"
}
-->
# 更新日誌

所有與 EdgeAI for Beginners 相關的重要更新都記錄於此。本項目採用基於日期的條目以及 Keep a Changelog 樣式（新增、變更、修復、移除、文檔、移動）。

## 2025-10-08

### 新增 - 工作坊全面更新
- **工作坊 README.md 完整重寫**：
  - 新增全面介紹，解釋 Edge AI 的價值主張（隱私、性能、成本）
  - 制定 6 個核心學習目標及詳細能力要求
  - 添加學習成果表，包括交付物和能力矩陣
  - 包括行業相關的職業技能部分
  - 新增快速入門指南，包括先決條件和三步設置流程
  - 創建 Python 示例資源表（8 個文件及運行時間）
  - 添加 Jupyter notebooks 表（8 個筆記本及難度評級）
  - 創建文檔表（7 個關鍵文檔及“使用時機”指導）
  - 為不同技能水平提供學習路徑建議

- **工作坊驗證和測試基礎設施**：
  - 創建 `scripts/validate_samples.py` - 用於語法、導入和最佳實踐的全面驗證工具
  - 創建 `scripts/test_samples.py` - 用於所有 Python 示例的煙霧測試運行器
  - 在 `scripts/README.md` 中新增驗證文檔

- **全面文檔**：
  - 創建 `SAMPLES_UPDATE_SUMMARY.md` - 400 多行的詳細指南，涵蓋所有改進
  - 創建 `UPDATE_COMPLETE.md` - 更新完成的執行摘要
  - 創建 `QUICK_REFERENCE.md` - 工作坊的快速參考卡

### 變更 - 工作坊 Python 示例現代化
- **所有 8 個 Python 示例更新至最佳實踐**：
  - 增強所有 I/O 操作的錯誤處理，加入 try-except 塊
  - 添加類型提示和全面的文檔字符串
  - 實現一致的 [INFO]/[ERROR]/[RESULT] 日誌模式
  - 為可選導入提供安裝提示保護
  - 改善所有示例中的用戶反饋

- **session01/chat_bootstrap.py**：
  - 增強客戶端初始化，提供全面的錯誤信息
  - 改善流式錯誤處理，加入塊驗證
  - 為服務不可用情況添加更好的異常處理

- **session02/rag_pipeline.py**：
  - 為 sentence-transformers 添加導入保護及安裝提示
  - 增強嵌入和生成操作的錯誤處理
  - 改善輸出格式，提供結構化結果

- **session02/rag_eval_ragas.py**：
  - 保護可選導入（ragas、datasets），提供用戶友好的錯誤信息
  - 添加評估指標的錯誤處理
  - 改善評估結果的輸出格式

- **session03/benchmark_oss_models.py**：
  - 實現優雅降級（模型失敗時繼續運行）
  - 添加詳細的進度報告及每個模型的錯誤處理
  - 增強統計計算，提供全面的錯誤恢復

- **session04/model_compare.py**：
  - 添加類型提示（Tuple 返回類型）
  - 改善輸出格式，提供結構化 JSON 結果
  - 實現每個模型的錯誤處理及恢復

- **session05/agents_orchestrator.py**：
  - 增強 Agent.act()，提供全面的文檔字符串
  - 添加管道錯誤處理，提供逐步日誌記錄
  - 改善內存管理及狀態跟蹤

- **session06/models_router.py**：
  - 增強所有路由組件的函數文檔
  - 在 route() 函數中添加詳細日誌記錄
  - 改善測試輸出，提供結構化結果

- **session06/models_pipeline.py**：
  - 為 chat() 助手函數添加錯誤處理
  - 增強 pipeline()，提供階段日誌記錄及進度報告
  - 改善 main()，提供全面的錯誤恢復

### 文檔 - 工作坊文檔增強
- 更新主 README.md，新增工作坊部分，突出動手學習路徑
- 增強 STUDY_GUIDE.md，新增全面的工作坊部分，包括：
  - 學習目標及學習重點
  - 自我評估問題
  - 動手練習及時間估算
  - 集中學習及兼職學習的時間分配
  - 在進度跟蹤模板中新增工作坊
- 將時間分配指南從 20 小時更新至 30 小時（包括工作坊）
- 在 README 中新增工作坊示例描述及學習成果

### 修復
- 解決工作坊示例中不一致的錯誤處理模式
- 修復可選依賴導入錯誤，加入適當的保護
- 修正關鍵函數中缺失的類型提示
- 解決錯誤場景中用戶反饋不足的問題
- 修復驗證問題，加入全面的測試基礎設施

---

## 2025-09-23

### 變更 - 模塊 08 的重大現代化
- **全面對齊 Microsoft Foundry-Local 存儲庫模式**：
  - 更新所有代碼示例，使用現代化的 `FoundryLocalManager` 和 OpenAI SDK 集成
  - 用正確的 SDK 使用替代過時的手動 `requests` 調用
  - 根據官方 Microsoft 文檔和示例對齊實現模式

- **05.AIPoweredAgents.md 現代化**：
  - 更新多代理協作，使用現代 SDK 模式
  - 增強協調器實現，加入高級功能（反饋循環、性能監控）
  - 添加全面的錯誤處理及服務健康檢查
  - 正確引用本地示例（`samples/05/multi_agent_orchestration.ipynb`）
  - 更新函數調用示例，使用現代化的 `tools` 參數替代過時的 `functions`
  - 添加生產就緒模式，加入監控及統計跟蹤

- **06.ModelsAsTools.md 完整重寫**：
  - 用智能模型路由器實現替代基本工具註冊
  - 添加基於關鍵字的模型選擇，用於不同任務類型（通用、推理、代碼、創意）
  - 集成基於環境的配置，提供靈活的模型分配
  - 增強全面的服務健康監控及錯誤處理
  - 添加生產部署模式，加入請求監控及性能跟蹤
  - 與本地實現對齊（`samples/06/router.py` 和 `samples/06/model_router.ipynb`）

- **文檔結構改進**：
  - 添加概述部分，突出現代化及 SDK 對齊
  - 增強表情符號及更好的格式，改善可讀性
  - 在文檔中正確引用本地示例文件
  - 包括生產就緒實現指導及最佳實踐

### 新增
- 模塊 08 文件中的全面概述部分，突出現代 SDK 集成
- 架構亮點，展示高級功能（多代理系統、智能路由）
- 本地示例實現的直接引用，提供動手體驗
- 生產部署指導，加入監控及錯誤處理模式
- 交互式 Jupyter notebook 示例，包含高級功能及基準測試

### 修復
- 文檔與實際示例實現之間的對齊差異
- 模塊 08 中過時的 SDK 使用模式
- 缺失的全面本地示例庫引用
- 不一致的實現方法，跨不同部分進行修正

---

## 2025-09-18

### 新增
- 模塊 08：Microsoft Foundry Local – 完整開發者工具包
  - 六個會話：設置、Azure AI Foundry 集成、開源模型、尖端演示、代理及模型作為工具
  - 可運行示例位於 `Module08/samples/01`–`06`，附 Windows cmd 指令
    - `01` REST 快速聊天（`chat_quickstart.py`）
    - `02` SDK 快速入門，支持 OpenAI/Foundry Local 和 Azure OpenAI（`sdk_quickstart.py`）
    - `03` CLI 列表及基準測試（`list_and_bench.cmd`）
    - `04` Chainlit 演示（`app.py`）
    - `05` 多代理協作（`python -m samples.05.agents.coordinator`）
    - `06` 模型作為工具路由器（`router.py`）
- Session 2 SDK 示例中新增 Azure OpenAI 支持，加入環境變量配置
- `.vscode/settings.json` 指向 `Module08/.venv`，改善 Python 分析解析
- `.env` 提供 `PYTHONPATH` 提示，支持 VS Code/Pylance

### 變更
- 模塊 08 文檔及示例中的默認模型更新為 `phi-4-mini`；移除剩餘的 `phi-3.5` 提及
- 路由器（`Module08/samples/06/router.py`）改進：
  - 通過 `foundry service status` 進行端點發現，使用正則表達式解析
  - 啟動時進行 `/v1/models` 健康檢查
  - 環境可配置的模型註冊（`GENERAL_MODEL`、`REASONING_MODEL`、`CODE_MODEL`、`TOOL_REGISTRY` JSON）
- 更新需求：`Module08/requirements.txt` 現在包括 `openai`（以及 `requests`、`chainlit`）
- Chainlit 示例指導明確化，新增故障排除；通過工作區設置解決導入問題

### 修復
- 解決導入問題：
  - 路由器不再依賴不存在的 `utils` 模塊；函數已內聯
  - 協調器使用相對導入（`from .specialists import ...`），通過模塊路徑調用
  - VS Code/Pylance 配置解決 `chainlit` 及包導入問題
- 修正 `STUDY_GUIDE.md` 中的小錯字，新增模塊 08 覆蓋範圍

### 移除
- 刪除未使用的 `Module08/infra/obs.py`，移除空的 `infra/` 目錄；可選的可觀測性模式保留在文檔中

### 移動
- 將模塊 08 演示整合至 `Module08/samples`，按會話編號文件夾分類
  - 將 Chainlit 應用移至 `samples/04`
  - 將代理移至 `samples/05`，並添加 `__init__.py` 文件以支持包解析

### 文檔
- 模塊 08 會話文檔及所有示例 README 增強，加入 Microsoft Learn 和可信供應商引用
- `Module08/README.md` 更新，新增示例概述、路由器配置及驗證提示
- `Module07/README.md` Windows Foundry Local 部分根據 Learn 文檔進行驗證
- `STUDY_GUIDE.md` 更新：
  - 在概述、時間表、進度跟蹤器中新增模塊 08
  - 添加全面的參考部分（Foundry Local、Azure AI、Olive、ONNX Runtime、OpenVINO、MLX、Llama.cpp、vLLM、Ollama、AI Toolkit、Windows ML）

---

## 歷史（摘要）
- 課程架構及模塊建立（模塊 01–07）
- 迭代內容現代化、格式標準化及新增案例研究
- 擴展優化框架覆蓋範圍（Llama.cpp、Olive、OpenVINO、Apple MLX）

## 未發布 / 待辦事項（提案）
- 可選的每個示例煙霧測試，用於驗證 Foundry Local 可用性
- 審核翻譯以對齊模型引用（例如 `phi-4-mini`）
- 如果團隊偏好工作區範圍的嚴格性，添加最小的 pyright 配置

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。