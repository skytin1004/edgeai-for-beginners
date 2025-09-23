<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-23T01:20:04+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "cs"
}
-->
# Ukázka ze Session 4: Chainlit RAG Demo

Spusťte minimální aplikaci Chainlit proti Foundry Local.

## Předpoklady
- Windows 11, Python 3.10+
- Nainstalovaný Foundry Local a dostupný model (např. `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Spuštění (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Ověření
```cmd
curl http://localhost:8000/v1/models
```

## Řešení problémů
- Pokud VS Code zobrazí "chainlit could not be resolved":
	- Vyberte interpret `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Ujistěte se, že jsou závislosti nainstalovány: `pip install -r Module08\requirements.txt`

## Odkazy
- Návod na Open WebUI (chatovací aplikace s Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

