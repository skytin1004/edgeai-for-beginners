<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-23T01:20:11+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "ro"
}
-->
# Sesiunea 4 Exemplu: Chainlit RAG Demo

Rulează aplicația minimală Chainlit împotriva Foundry Local.

## Cerințe preliminare
- Windows 11, Python 3.10+
- Foundry Local instalat și un model disponibil (de exemplu, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Rulare (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Validare
```cmd
curl http://localhost:8000/v1/models
```

## Depanare
- Dacă VS Code afișează "chainlit could not be resolved":
	- Selectează interpretul `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Asigură-te că dependențele sunt instalate: `pip install -r Module08\requirements.txt`

## Referințe
- Cum să deschizi WebUI (aplicație de chat cu Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

