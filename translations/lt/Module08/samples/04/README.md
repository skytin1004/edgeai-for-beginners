<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-23T01:20:38+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "lt"
}
-->
# 4 sesijos pavyzdys: Chainlit RAG demonstracija

Paleiskite minimalų Chainlit programą su Foundry Local.

## Reikalavimai
- Windows 11, Python 3.10+
- Įdiegtas Foundry Local ir pasiekiamas modelis (pvz., `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Paleidimas (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Patikrinimas
```cmd
curl http://localhost:8000/v1/models
```

## Trikčių šalinimas
- Jei VS Code rodo "chainlit could not be resolved":
	- Pasirinkite interpretatorių `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Įsitikinkite, kad priklausomybės įdiegtos: `pip install -r Module08\requirements.txt`

## Nuorodos
- Open WebUI instrukcija (pokalbių programa su Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (mokymosi medžiaga): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

