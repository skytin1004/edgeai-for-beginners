<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T14:25:39+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "ur"
}
-->
# سیشن 1 نمونہ: REST کے ذریعے فوری چیٹ

Python `requests` کا استعمال کرتے ہوئے Foundry Local پر ایک مختصر چیٹ درخواست چلائیں۔

## ضروریات
- Foundry Local سروس جو ایک ماڈل چلا رہی ہو (مثلاً، `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## چلائیں (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## حوالہ جات
- Foundry Local (سیکھیں): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-compatible API کا جائزہ: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

