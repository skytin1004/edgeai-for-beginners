# Session 4 Sample: Chainlit RAG Demo

Run the minimal Chainlit app against Foundry Local.

## Prerequisites
- Windows 11, Python 3.10+
- Foundry Local installed and a model available (e.g., `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Run (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Validate
```cmd
curl http://localhost:8000/v1/models
```

## Troubleshooting
- If VS Code shows "chainlit could not be resolved":
	- Select the interpreter `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Ensure deps are installed: `pip install -r Module08\requirements.txt`
