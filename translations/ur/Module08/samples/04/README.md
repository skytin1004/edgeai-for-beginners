<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T14:26:14+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "ur"
}
-->
# سیشن 4 نمونہ: Chainlit RAG ڈیمو

Foundry Local کے خلاف کم سے کم Chainlit ایپ چلائیں۔

## ضروریات
- ونڈوز 11، Python 3.10+
- Foundry Local انسٹال ہو اور ایک ماڈل دستیاب ہو (مثلاً، `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## چلائیں (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## تصدیق کریں
```cmd
curl http://localhost:8000/v1/models
```

## مسائل کا حل
- اگر VS Code "chainlit could not be resolved" دکھائے:
	- انٹرپریٹر منتخب کریں `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- یقینی بنائیں کہ dependencies انسٹال ہیں: `pip install -r Module08\requirements.txt`

## حوالہ جات
- Open WebUI کا طریقہ (Open WebUI کے ساتھ چیٹ ایپ): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (سیکھیں): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

