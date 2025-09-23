<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-23T01:20:08+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "sk"
}
-->
# Ukážka relácie 4: Chainlit RAG Demo

Spustite minimálnu aplikáciu Chainlit proti Foundry Local.

## Predpoklady
- Windows 11, Python 3.10+
- Nainštalovaný Foundry Local a dostupný model (napr. `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Spustenie (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Overenie
```cmd
curl http://localhost:8000/v1/models
```

## Riešenie problémov
- Ak VS Code zobrazí "chainlit nemohol byť rozpoznaný":
	- Vyberte interpret `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Uistite sa, že sú nainštalované závislosti: `pip install -r Module08\requirements.txt`

## Referencie
- Návod na Open WebUI (chatová aplikácia s Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

