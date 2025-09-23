<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T22:41:32+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "tl"
}
-->
# Session 4 Sample: Chainlit RAG Demo

Patakbuhin ang minimal na Chainlit app laban sa Foundry Local.

## Mga Kinakailangan
- Windows 11, Python 3.10+
- Nakainstall ang Foundry Local at may model na available (hal., `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Patakbuhin (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Beripikahin
```cmd
curl http://localhost:8000/v1/models
```

## Pag-aayos ng Problema
- Kung nagpapakita ang VS Code ng "chainlit could not be resolved":
	- Piliin ang interpreter `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Siguraduhing naka-install ang mga dependencies: `pip install -r Module08\requirements.txt`

## Mga Sanggunian
- Open WebUI how-to (chat app gamit ang Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

