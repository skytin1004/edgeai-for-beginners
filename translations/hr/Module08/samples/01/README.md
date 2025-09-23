<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-23T01:18:03+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "hr"
}
-->
# Sesija 1 Primjer: Brzi Chat putem REST-a

Pokrenite minimalni zahtjev za chat prema Foundry Local koristeći Python `requests`.

## Preduvjeti
- Foundry Local servis koji pokreće model (npr. `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Pokretanje (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Reference
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Pregled OpenAI-kompatibilnog API-ja: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

