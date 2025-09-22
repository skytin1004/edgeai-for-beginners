<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-22T11:49:56+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "tw"
}
-->
# 在 Windows 上使用 Foundry Local（已驗證）

本指南將幫助您在 Windows 上安裝、運行並整合 Microsoft Foundry Local。所有步驟和命令均已根據 Microsoft Learn 文檔進行驗證。

- 開始使用：https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- 架構概述：https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI 參考：https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- 整合 SDKs：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- 編譯 HF 模型（自帶模型 BYOM）：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI：本地與雲端比較：https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) 在 Windows 上安裝 / 升級

- 安裝：
```cmd
winget install Microsoft.FoundryLocal
```
- 升級：
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- 檢查版本：
```cmd
foundry --version
```


## 2) CLI 基本操作（三大類別）

- 模型：
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- 服務：
```cmd
foundry service --help
foundry service status
foundry service ps
```
- 快取：
```cmd
foundry cache --help
foundry cache list
```

注意事項：
- 該服務提供與 OpenAI 兼容的 REST API。端點埠是動態分配的，可使用 `foundry service status` 來查詢。
- 建議使用 SDKs，因為它們會自動處理端點發現（在支持的情況下）。

## 3) 發現本地端點（動態埠）

Foundry Local 每次啟動服務時都會分配一個動態埠：
```cmd
foundry service status
```
使用報告的 `http://localhost:<PORT>` 作為您的 `base_url`，並搭配 OpenAI 兼容的路徑（例如 `/v1/chat/completions`）。

## 4) 通過 OpenAI Python SDK 快速測試

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
參考資料：
- SDK 整合：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) 自帶模型（使用 Olive 編譯）

如果需要使用目錄中沒有的模型，可以使用 Olive 將其編譯為 ONNX 格式以供 Foundry Local 使用。

高層次流程（具體步驟請參考文檔）：
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
文檔：
- BYOM 編譯：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) 疑難排解

- 檢查服務狀態和日誌：
```cmd
foundry service status
foundry service diag
```
- 清除或移動快取：
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- 更新至最新預覽版：
```cmd
winget upgrade --id Microsoft.FoundryLocal
```


## 7) 相關的 Windows 開發者體驗

- Windows 本地與雲端 AI 選擇，包括 Foundry Local 和 Windows ML：
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI 工具包與 Foundry Local 整合（使用 `foundry service status` 獲取聊天端點 URL）：
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

