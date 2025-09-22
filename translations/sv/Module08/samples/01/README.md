<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T19:22:56+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "sv"
}
-->
# Session 1 Exempel: Snabbchatt via REST

Kör en minimal chattförfrågan till Foundry Local med Python `requests`.

## Förutsättningar
- Foundry Local-tjänst som kör en modell (t.ex. `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Kör (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Referenser
- Foundry Local (Lär dig mer): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-kompatibel API-översikt: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

