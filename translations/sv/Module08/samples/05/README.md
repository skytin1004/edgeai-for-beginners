<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-22T19:23:08+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "sv"
}
-->
# Session 5 Exempel: Orkestrering av flera agenter

Det här exemplet visar ett koordinator + specialistmönster med Foundry Locals OpenAI-kompatibla endpoint.

## Kör (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Validera
```cmd
curl http://localhost:8000/v1/models
```

## Felsökning
- Om VS Code markerar `import specialists` som olöst i `coordinator.py`, se till att du kör som en modul och att tolken pekar på `Module08/.venv`:
	- Kör: `python -m samples.05.agents.coordinator`
	- Välj tolk: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Referenser
- Foundry Local (Lär dig mer): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Översikt över Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Exempel på funktionsanrop (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

