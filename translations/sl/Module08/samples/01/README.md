<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-23T01:18:06+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "sl"
}
-->
# Seja 1 Vzorec: Hitri klepet prek REST

Izvedite minimalno zahtevo za klepet do Foundry Local z uporabo Python `requests`.

## Predpogoji
- Storitev Foundry Local, ki izvaja model (npr. `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Zagon (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Reference
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Pregled API-ja, združljivega z OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

