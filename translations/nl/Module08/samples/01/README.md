<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T21:53:26+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "nl"
}
-->
# Sessie 1 Voorbeeld: Snelle Chat via REST

Voer een minimale chataanvraag uit naar Foundry Local met behulp van Python `requests`.

## Vereisten
- Foundry Local-service die een model uitvoert (bijv. `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Uitvoeren (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Referenties
- Foundry Local (Leer): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-compatibele API-overzicht: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

