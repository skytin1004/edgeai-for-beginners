<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-23T01:17:52+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "sk"
}
-->
# Session 1 Ukážka: Rýchly chat cez REST

Spustite minimálnu požiadavku na chat s Foundry Local pomocou Python `requests`.

## Predpoklady
- Služba Foundry Local, ktorá spúšťa model (napr. `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Spustenie (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Referencie
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Prehľad API kompatibilného s OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

