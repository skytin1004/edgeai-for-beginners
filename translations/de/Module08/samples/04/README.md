<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T12:58:26+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "de"
}
-->
# Sitzung 4 Beispiel: Chainlit RAG Demo

Führen Sie die minimale Chainlit-App gegen Foundry Local aus.

## Voraussetzungen
- Windows 11, Python 3.10+
- Foundry Local installiert und ein Modell verfügbar (z. B. `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Ausführen (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Validieren
```cmd
curl http://localhost:8000/v1/models
```

## Fehlerbehebung
- Wenn VS Code "chainlit konnte nicht aufgelöst werden" anzeigt:
	- Wählen Sie den Interpreter `Module08/.venv/Scripts/python.exe` aus (Strg+Shift+P → Python: Interpreter auswählen)
	- Stellen Sie sicher, dass die Abhängigkeiten installiert sind: `pip install -r Module08\requirements.txt`

## Referenzen
- Open WebUI Anleitung (Chat-App mit Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Lernen): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

