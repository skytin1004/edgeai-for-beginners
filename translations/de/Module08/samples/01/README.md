<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T12:57:50+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "de"
}
-->
# Sitzung 1 Beispiel: Schneller Chat über REST

Führen Sie eine minimale Chat-Anfrage an Foundry Local mit Python `requests` aus.

## Voraussetzungen
- Foundry Local-Dienst, der ein Modell ausführt (z. B. `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Ausführen (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Referenzen
- Foundry Local (Lernen): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-kompatible API-Übersicht: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

