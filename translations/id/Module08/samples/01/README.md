<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T22:40:53+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "id"
}
-->
# Sesi 1 Contoh: Obrolan Cepat via REST

Jalankan permintaan obrolan minimal ke Foundry Local menggunakan Python `requests`.

## Prasyarat
- Layanan Foundry Local menjalankan model (misalnya, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Jalankan (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Referensi
- Foundry Local (Pelajari): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Ikhtisar API yang kompatibel dengan OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

