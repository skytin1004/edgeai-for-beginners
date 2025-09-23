<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T22:40:55+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "ms"
}
-->
# Sesi 1 Contoh: Sembang Pantas melalui REST

Jalankan permintaan sembang minimum ke Foundry Local menggunakan Python `requests`.

## Prasyarat
- Perkhidmatan Foundry Local menjalankan model (contohnya, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Jalankan (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Rujukan
- Foundry Local (Belajar): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Gambaran keseluruhan API yang serasi dengan OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

