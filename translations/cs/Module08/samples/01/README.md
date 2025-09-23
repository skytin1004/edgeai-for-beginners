<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-23T01:17:49+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "cs"
}
-->
# Ukázka relace 1: Rychlý chat přes REST

Spusťte minimální požadavek na chatování na Foundry Local pomocí Pythonu `requests`.

## Předpoklady
- Služba Foundry Local běžící na modelu (např. `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Spuštění (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Odkazy
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Přehled API kompatibilního s OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

