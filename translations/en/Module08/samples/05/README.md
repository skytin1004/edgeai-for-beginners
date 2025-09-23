<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-23T01:18:18+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "en"
}
-->
# Session 5 Sample: Multi-Agent Orchestration

This sample showcases a coordinator + specialists pattern using Foundry Local’s OpenAI-compatible endpoint.

## Run (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Validate
```cmd
curl http://localhost:8000/v1/models
```

## Troubleshooting
- If VS Code marks `import specialists` as unresolved in `coordinator.py`, make sure to run it as a module and verify that the interpreter is set to `Module08/.venv`:
	- Run: `python -m samples.05.agents.coordinator`
	- Select interpreter: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## References
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents overview: https://learn.microsoft.com/azure/ai-services/agents/overview
- Function calling sample (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

