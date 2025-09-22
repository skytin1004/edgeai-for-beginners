<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T20:25:53+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "fi"
}
-->
# Istunto 1 Esimerkki: Nopea keskustelu RESTin kautta

Suorita yksinkertainen keskustelupyyntö Foundry Local -palveluun Pythonin `requests`-kirjastolla.

## Esivaatimukset
- Foundry Local -palvelu, jossa on käynnissä malli (esim. `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Suoritus (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Viitteet
- Foundry Local (Oppiminen): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-yhteensopivan API:n yleiskatsaus: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

