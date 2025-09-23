<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-23T01:18:15+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "lt"
}
-->
# 1 sesijos pavyzdys: Greitas pokalbis per REST

Atlikite minimalų pokalbio užklausą Foundry Local naudodami Python `requests`.

## Būtinos sąlygos
- Foundry Local paslauga, vykdanti modelį (pvz., `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Paleidimas (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Nuorodos
- Foundry Local (Sužinokite): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI suderinamos API apžvalga: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

