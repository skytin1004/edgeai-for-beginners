<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T16:57:15+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "mo"
}
-->
# 第四節範例：Chainlit RAG 演示

在 Foundry Local 上運行最簡化的 Chainlit 應用程式。

## 先決條件
- Windows 11，Python 3.10+
- 已安裝 Foundry Local 並有可用模型（例如：`phi-4-mini`）
- 執行 `pip install -r Module08\requirements.txt`

## 運行 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## 驗證
```cmd
curl http://localhost:8000/v1/models
```

## 疑難排解
- 如果 VS Code 顯示 "chainlit could not be resolved":
	- 選擇解釋器 `Module08/.venv/Scripts/python.exe`（Ctrl+Shift+P → Python: Select Interpreter）
	- 確保已安裝依賴項：`pip install -r Module08\requirements.txt`

## 參考資料
- Open WebUI 使用指南（使用 Open WebUI 的聊天應用程式）：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local（學習資源）：https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

