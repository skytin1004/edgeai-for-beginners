<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T20:26:23+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "no"
}
-->
# Sesjon 4 Eksempel: Chainlit RAG Demo

Kjør den minimale Chainlit-appen mot Foundry Local.

## Forutsetninger
- Windows 11, Python 3.10+
- Foundry Local installert og en modell tilgjengelig (f.eks. `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Kjør (cmd.exe)
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

## Feilsøking
- Hvis VS Code viser "chainlit could not be resolved":
	- Velg tolken `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Sørg for at avhengigheter er installert: `pip install -r Module08\requirements.txt`

## Referanser
- Open WebUI veiledning (chat-app med Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Lær): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

