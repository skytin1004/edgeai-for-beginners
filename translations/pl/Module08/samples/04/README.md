<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T13:41:15+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "pl"
}
-->
# Sesja 4 Przykład: Chainlit RAG Demo

Uruchom minimalną aplikację Chainlit w środowisku Foundry Local.

## Wymagania wstępne
- Windows 11, Python 3.10+
- Zainstalowany Foundry Local i dostępny model (np. `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Uruchomienie (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Walidacja
```cmd
curl http://localhost:8000/v1/models
```

## Rozwiązywanie problemów
- Jeśli VS Code wyświetla komunikat "chainlit could not be resolved":
	- Wybierz interpreter `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Upewnij się, że zależności są zainstalowane: `pip install -r Module08\requirements.txt`

## Odnośniki
- Instrukcja Open WebUI (aplikacja czatu z Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

