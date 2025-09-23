<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-23T01:19:57+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "sw"
}
-->
# Kipindi cha 4 Mfano: Chainlit RAG Demo

Endesha programu ndogo ya Chainlit dhidi ya Foundry Local.

## Mahitaji ya Awali
- Windows 11, Python 3.10+
- Foundry Local imewekwa na modeli inapatikana (mfano, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Endesha (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Thibitisha
```cmd
curl http://localhost:8000/v1/models
```

## Utatuzi wa Matatizo
- Ikiwa VS Code inaonyesha "chainlit could not be resolved":
	- Chagua interpreter `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Hakikisha utegemezi vimewekwa: `pip install -r Module08\requirements.txt`

## Marejeleo
- Jinsi ya kufungua WebUI (programu ya mazungumzo na Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Jifunze): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

