<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-23T01:20:25+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "sl"
}
-->
# Seansa 4 Primer: Chainlit RAG Demo

Zaženite minimalno Chainlit aplikacijo proti Foundry Local.

## Predpogoji
- Windows 11, Python 3.10+
- Nameščen Foundry Local in na voljo model (npr. `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Zagon (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Preverjanje
```cmd
curl http://localhost:8000/v1/models
```

## Odpravljanje težav
- Če VS Code prikaže "chainlit could not be resolved":
	- Izberite interpreter `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Prepričajte se, da so odvisnosti nameščene: `pip install -r Module08\requirements.txt`

## Reference
- Navodila za Open WebUI (aplikacija za klepet z Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Učenje): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

