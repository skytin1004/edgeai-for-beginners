<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-23T01:20:00+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "hu"
}
-->
# 4. szekció minta: Chainlit RAG bemutató

Futtassa a minimális Chainlit alkalmazást a Foundry Local ellen.

## Előfeltételek
- Windows 11, Python 3.10+
- Foundry Local telepítve és egy elérhető modell (pl. `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Futtatás (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Ellenőrzés
```cmd
curl http://localhost:8000/v1/models
```

## Hibakeresés
- Ha a VS Code azt jelzi, hogy "chainlit nem oldható fel":
	- Válassza ki az értelmezőt: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Győződjön meg róla, hogy a függőségek telepítve vannak: `pip install -r Module08\requirements.txt`

## Hivatkozások
- Open WebUI útmutató (chat alkalmazás Open WebUI-val): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Tanulás): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

