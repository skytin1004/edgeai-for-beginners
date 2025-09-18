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
