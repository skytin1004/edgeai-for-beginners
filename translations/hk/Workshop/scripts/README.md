<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-08T16:38:25+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "hk"
}
-->
# 工作坊腳本

此目錄包含用於維持工作坊材料質量和一致性的自動化及支援腳本。

## 內容

| 文件 | 用途 |
|------|------|
| `lint_markdown_cli.py` | 檢查 Markdown 代碼塊中已棄用的 Foundry Local CLI 命令模式。 |
| `export_benchmark_markdown.py` | 執行多模型延遲基準測試並生成 Markdown 和 JSON 報告。 |

## 1. Markdown CLI 模式檢查工具

`lint_markdown_cli.py` 會掃描所有非翻譯的 `.md` 文件，檢查 **代碼塊內**（``` ... ```）不允許的 Foundry Local CLI 模式。信息性文字仍可提及已棄用的命令以提供歷史背景。

### 已棄用模式（代碼塊內禁止）

檢查工具會阻止使用已棄用的 CLI 模式。請使用現代替代方案。

### 必須替換
| 已棄用 | 替代方案 |
|--------|----------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | 基準測試腳本 + 系統工具（`Task Manager`，`nvidia-smi`） |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### 退出代碼
| 代碼 | 含義 |
|------|------|
| 0 | 未檢測到違規 |
| 1 | 檢測到一個或多個已棄用模式 |

### 本地運行
從倉庫根目錄運行（推薦）：

Windows（PowerShell）：
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux：
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```


### 預提交鉤子（可選）
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
此鉤子會阻止引入已棄用模式的提交。

### CI 集成
GitHub Action 工作流（`.github/workflows/markdown-cli-lint.yml`）會在每次推送和拉取請求到 `main` 和 `Reactor` 分支時運行檢查工具。必須修復失敗的任務才能合併。

### 添加新的已棄用模式
1. 打開 `lint_markdown_cli.py`。
2. 在 `DEPRECATED` 列表中添加一個元組 `(regex, suggestion)`。使用原始字符串並在適當位置包含 `\b` 單詞邊界。
3. 本地運行檢查工具以驗證檢測。
4. 提交並推送；CI 會強制執行新規則。

示例添加：
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```


### 允許解釋性提及
由於僅強制代碼塊，您可以在敘述文字中安全地描述已棄用命令。如果您*必須*在代碼塊中展示它們以作對比，請使用非三引號的代碼塊（例如，縮進或引用）或改寫為偽形式。

### 跳過特定文件（高級）
如有需要，可將遺留示例包裝在倉庫外的單獨文件中，或在草稿期間重命名為不同的擴展名。翻譯副本的意圖性跳過是自動的（路徑包含 `translations`）。

### 疑難排解
| 問題 | 原因 | 解決方案 |
|------|------|---------|
| 檢查工具標記了您更新的行 | 正則表達式過於寬泛 | 使用額外的單詞邊界（`\b`）或錨點縮小模式 |
| CI 失敗但本地通過 | Python 版本不同或未提交的更改 | 本地重新運行，確保工作樹乾淨，檢查工作流 Python 版本（3.11） |
| 需要臨時繞過 | 緊急修復 | 修復後立即應用；考慮使用臨時分支和後續 PR（避免添加繞過開關） |

### 原因
保持文檔與*當前*穩定的 CLI 接口一致可避免工作坊摩擦，減少學習者困惑，並通過維護的 Python 腳本集中性能測量，而非漂移的 CLI 子命令。

---
作為工作坊質量工具鏈的一部分進行維護。如需增強功能（例如，自動修復建議或 HTML 報告生成），請開啟問題或提交 PR。

## 2. 示例驗證腳本

`validate_samples.py` 驗證所有 Python 示例文件的語法、導入和最佳實踐合規性。

### 用法
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```


### 檢查內容
- ✅ Python 語法有效性
- ✅ 必需的導入存在
- ✅ 錯誤處理實現（詳細模式）
- ✅ 類型提示使用（詳細模式）
- ✅ 函數文檔字符串（詳細模式）
- ✅ SDK 參考鏈接（詳細模式）

### 環境變量
- `SKIP_IMPORT_CHECK=1` - 跳過導入驗證
- `SKIP_SYNTAX_CHECK=1` - 跳過語法驗證

### 退出代碼
- `0` - 所有示例通過驗證
- `1` - 一個或多個示例未通過

## 3. 示例測試運行器

`test_samples.py` 對所有示例進行冒煙測試，以驗證它們是否能無錯誤執行。

### 用法
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```


### 先決條件
- Foundry Local 服務正在運行：`foundry service start`
- 模型已加載：`foundry model run phi-4-mini`
- 依賴已安裝：`pip install -r requirements.txt`

### 測試內容
- ✅ 示例能無運行時錯誤執行
- ✅ 生成所需輸出
- ✅ 失敗時正確的錯誤處理
- ✅ 性能（執行時間）

### 環境變量
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - 用於測試的模型
- `TEST_TIMEOUT=30` - 每個示例的超時時間（秒）

### 預期失敗
如果未安裝可選依賴（例如，`ragas`，`sentence-transformers`），某些測試可能失敗。安裝方式：
```bash
pip install sentence-transformers ragas datasets
```


### 退出代碼
- `0` - 所有測試通過
- `1` - 一個或多個測試失敗

## 4. 基準 Markdown 導出器

腳本：`export_benchmark_markdown.py`

為一組模型生成可重現的性能表。

### 用法
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```


### 輸出
| 文件 | 描述 |
|------|------|
| `benchmark_report.md` | Markdown 表格（平均值，p95，每秒令牌數，可選首令牌） |
| `benchmark_report.json` | 用於差異和歷史的原始指標數組 |

### 選項
| 標誌 | 描述 | 默認值 |
|------|------|--------|
| `--models` | 逗號分隔的模型別名 | （必需） |
| `--prompt` | 每輪使用的提示 | （必需） |
| `--rounds` | 每個模型的輪次 | 3 |
| `--output` | Markdown 輸出文件 | `benchmark_report.md` |
| `--json` | JSON 輸出文件 | `benchmark_report.json` |
| `--fail-on-empty` | 如果所有基準測試失敗則退出非零 | 關閉 |

環境變量 `BENCH_STREAM=1` 添加首令牌延遲測量。

### 注意事項
- 重用 `workshop_utils` 以保持模型啟動和緩存的一致性。
- 如果從不同的工作目錄運行，腳本會嘗試路徑回退以定位 `workshop_utils`。
- GPU 比較：運行一次，通過 CLI 配置啟用加速，重新運行並比較 JSON。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。