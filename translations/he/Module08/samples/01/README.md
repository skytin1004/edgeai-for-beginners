<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T21:53:29+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "he"
}
-->
# דוגמה למפגש 1: שיחה מהירה באמצעות REST

בצע בקשת שיחה מינימלית ל-Foundry Local באמצעות Python `requests`.

## דרישות מוקדמות
- שירות Foundry Local שמריץ מודל (לדוגמה, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## הפעלה (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## הפניות
- Foundry Local (לימוד): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- סקירה כללית של API תואם OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

