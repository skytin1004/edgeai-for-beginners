<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T20:26:26+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "fi"
}
-->
# Istunto 4 Esimerkki: Chainlit RAG Demo

Aja minimaalinen Chainlit-sovellus Foundry Localia vastaan.

## Esivaatimukset
- Windows 11, Python 3.10+
- Foundry Local asennettuna ja malli saatavilla (esim. `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Suorita (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Vahvista
```cmd
curl http://localhost:8000/v1/models
```

## Vianmääritys
- Jos VS Code näyttää "chainlit could not be resolved":
	- Valitse tulkki `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Varmista, että riippuvuudet on asennettu: `pip install -r Module08\requirements.txt`

## Viitteet
- Open WebUI -ohje (chat-sovellus Open WebUI:lla): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

