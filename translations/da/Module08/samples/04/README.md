<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T20:26:19+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "da"
}
-->
# Session 4 Eksempel: Chainlit RAG Demo

Kør den minimale Chainlit-app mod Foundry Local.

## Forudsætninger
- Windows 11, Python 3.10+
- Foundry Local installeret og en model tilgængelig (f.eks. `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Kør (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Valider
```cmd
curl http://localhost:8000/v1/models
```

## Fejlfinding
- Hvis VS Code viser "chainlit kunne ikke blive fundet":
	- Vælg interpreter `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Vælg Interpreter)
	- Sørg for, at afhængigheder er installeret: `pip install -r Module08\requirements.txt`

## Referencer
- Open WebUI vejledning (chat-app med Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Lær): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

