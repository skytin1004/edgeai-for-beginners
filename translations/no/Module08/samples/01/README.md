<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T20:25:50+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "no"
}
-->
# Sesjon 1 Eksempel: Rask Chat via REST

Utfør en minimal chat-forespørsel til Foundry Local ved hjelp av Python `requests`.

## Forutsetninger
- Foundry Local-tjeneste som kjører en modell (f.eks. `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Kjøring (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Referanser
- Foundry Local (Lær): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-kompatibel API-oversikt: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

