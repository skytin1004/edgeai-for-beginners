# Session 1 Sample: Quick Chat via REST

Run a minimal chat request to Foundry Local using Python `requests`.

## Prerequisites
- Foundry Local service running a model (e.g., `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Run (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## References
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-compatible API overview: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
