<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T18:34:17+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "tr"
}
-->
# Oturum 1 Örneği: REST ile Hızlı Sohbet

Python `requests` kullanarak Foundry Local'a minimal bir sohbet isteği gönderin.

## Ön Koşullar
- Bir modeli çalıştıran Foundry Local servisi (örneğin, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Çalıştırma (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Referanslar
- Foundry Local (Öğren): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI uyumlu API genel bakışı: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

