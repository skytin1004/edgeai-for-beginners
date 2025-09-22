<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T13:40:37+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "pl"
}
-->
# Sesja 1 Przykład: Szybki czat przez REST

Uruchom minimalne zapytanie czatu do Foundry Local za pomocą biblioteki `requests` w Pythonie.

## Wymagania wstępne
- Usługa Foundry Local uruchamiająca model (np. `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Uruchomienie (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Odnośniki
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Przegląd API kompatybilnego z OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

