<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T11:48:35+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "tw"
}
-->
# Session 1 範例：通過 REST 快速聊天

使用 Python `requests` 向 Foundry Local 發送最小化的聊天請求。

## 先決條件
- Foundry Local 服務正在運行模型（例如，`phi-4-mini`）
- `pip install -r ../../requirements.txt`

## 執行（cmd.exe）
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## 參考資料
- Foundry Local（學習）：https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI 兼容 API 概述：https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

