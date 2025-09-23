<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-23T01:17:55+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "ro"
}
-->
# Sesiunea 1 Exemplu: Chat Rapid prin REST

Execută o cerere minimă de chat către Foundry Local folosind `requests` din Python.

## Cerințe preliminare
- Serviciul Foundry Local care rulează un model (de exemplu, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Executare (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Referințe
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Prezentare generală API compatibilă cu OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

