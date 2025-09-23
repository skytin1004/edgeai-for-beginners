<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-23T01:17:47+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "hu"
}
-->
# 1. munkamenet példa: Gyors csevegés REST-en keresztül

Futtass egy minimális csevegési kérést a Foundry Local segítségével Python `requests` használatával.

## Előfeltételek
- Foundry Local szolgáltatás, amely egy modellt futtat (pl. `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Futtatás (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Hivatkozások
- Foundry Local (Tanulás): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-kompatibilis API áttekintés: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

