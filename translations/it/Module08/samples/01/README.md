<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T18:34:14+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "it"
}
-->
# Sessione 1 Esempio: Chat Rapida tramite REST

Esegui una richiesta di chat minima a Foundry Local utilizzando `requests` di Python.

## Prerequisiti
- Servizio Foundry Local che esegue un modello (ad esempio, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Esecuzione (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Riferimenti
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Panoramica API compatibile con OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

