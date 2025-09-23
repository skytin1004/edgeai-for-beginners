<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-23T01:18:36+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "ro"
}
-->
# Sesiunea 5 Exemplu: Orchestrare Multi-Agent

Acest exemplu demonstrează un model de coordonator + specialiști utilizând endpoint-ul compatibil OpenAI al Foundry Local.

## Rulare (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Validare
```cmd
curl http://localhost:8000/v1/models
```

## Depanare
- Dacă VS Code indică `import specialists` ca nerezolvat în `coordinator.py`, asigură-te că rulezi ca modul și că interpretul indică spre `Module08/.venv`:
	- Rulează: `python -m samples.05.agents.coordinator`
	- Selectează interpretul: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Referințe
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Prezentare generală Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Exemplu de apelare funcții (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

