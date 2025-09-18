# Session 5 Sample: Multi-Agent Orchestration

This sample demonstrates a coordinator + specialists pattern using Foundry Local’s OpenAI-compatible endpoint.

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
- If VS Code flags `import specialists` unresolved in `coordinator.py`, ensure you run as a module and the interpreter points to `Module08/.venv`:
	- Run: `python -m samples.05.agents.coordinator`
	- Select interpreter: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
