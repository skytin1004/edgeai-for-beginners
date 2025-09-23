<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-22T13:40:48+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "pl"
}
-->
# Sesja 5 Przykład: Orkiestracja Wieloagentowa

Ten przykład demonstruje wzorzec koordynatora + specjalistów, korzystając z kompatybilnego z OpenAI punktu końcowego Foundry Local.

## Uruchom (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Walidacja
```cmd
curl http://localhost:8000/v1/models
```

## Rozwiązywanie problemów
- Jeśli VS Code oznacza `import specialists` jako nierozwiązane w `coordinator.py`, upewnij się, że uruchamiasz jako moduł, a interpreter wskazuje na `Module08/.venv`:
	- Uruchom: `python -m samples.05.agents.coordinator`
	- Wybierz interpreter: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Odnośniki
- Foundry Local (Nauka): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Przegląd agentów Azure AI: https://learn.microsoft.com/azure/ai-services/agents/overview
- Przykład wywoływania funkcji (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

