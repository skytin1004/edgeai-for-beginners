<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T19:23:32+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "sv"
}
-->
# Session 4 Exempel: Chainlit RAG Demo

Kör den minimala Chainlit-appen mot Foundry Local.

## Förutsättningar
- Windows 11, Python 3.10+
- Foundry Local installerat och en modell tillgänglig (t.ex. `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Kör (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Validera
```cmd
curl http://localhost:8000/v1/models
```

## Felsökning
- Om VS Code visar "chainlit could not be resolved":
	- Välj tolken `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Kontrollera att beroenden är installerade: `pip install -r Module08\requirements.txt`

## Referenser
- Open WebUI guide (chattapp med Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Lär dig mer): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

