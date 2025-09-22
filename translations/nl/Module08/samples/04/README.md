<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T21:53:55+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "nl"
}
-->
# Sessie 4 Voorbeeld: Chainlit RAG Demo

Voer de minimale Chainlit-app uit tegen Foundry Local.

## Vereisten
- Windows 11, Python 3.10+
- Foundry Local geïnstalleerd en een model beschikbaar (bijv. `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Uitvoeren (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Valideren
```cmd
curl http://localhost:8000/v1/models
```

## Problemen oplossen
- Als VS Code "chainlit could not be resolved" toont:
	- Selecteer de interpreter `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Zorg ervoor dat de afhankelijkheden zijn geïnstalleerd: `pip install -r Module08\requirements.txt`

## Referenties
- Open WebUI handleiding (chat-app met Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

