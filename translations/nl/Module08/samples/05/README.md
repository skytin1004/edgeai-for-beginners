<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-22T21:53:34+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "nl"
}
-->
# Sessie 5 Voorbeeld: Multi-Agent Orchestratie

Dit voorbeeld demonstreert een coördinator + specialisten patroon met behulp van Foundry Local's OpenAI-compatibele endpoint.

## Uitvoeren (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Valideren
```cmd
curl http://localhost:8000/v1/models
```

## Problemen oplossen
- Als VS Code `import specialists` als onopgelost markeert in `coordinator.py`, zorg er dan voor dat je het als een module uitvoert en dat de interpreter wijst naar `Module08/.venv`:
	- Uitvoeren: `python -m samples.05.agents.coordinator`
	- Interpreter selecteren: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Referenties
- Foundry Local (Leer): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents overzicht: https://learn.microsoft.com/azure/ai-services/agents/overview
- Voorbeeld functieaanroep (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

