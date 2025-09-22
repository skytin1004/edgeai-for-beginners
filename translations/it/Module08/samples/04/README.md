<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T18:35:02+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "it"
}
-->
# Sessione 4 Esempio: Demo Chainlit RAG

Esegui l'app Chainlit minima con Foundry Local.

## Prerequisiti
- Windows 11, Python 3.10+
- Foundry Local installato e un modello disponibile (ad esempio, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Esecuzione (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Validazione
```cmd
curl http://localhost:8000/v1/models
```

## Risoluzione dei problemi
- Se VS Code mostra "chainlit could not be resolved":
	- Seleziona l'interprete `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Assicurati che le dipendenze siano installate: `pip install -r Module08\requirements.txt`

## Riferimenti
- Guida WebUI (app di chat con Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

