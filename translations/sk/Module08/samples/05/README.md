<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-23T01:18:32+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "sk"
}
-->
# Ukážka relácie 5: Orchestrácia viacerých agentov

Táto ukážka demonštruje vzor koordinátora + špecialistov pomocou OpenAI-kompatibilného koncového bodu Foundry Local.

## Spustenie (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Overenie
```cmd
curl http://localhost:8000/v1/models
```

## Riešenie problémov
- Ak VS Code označí `import specialists` ako nevyriešený v súbore `coordinator.py`, uistite sa, že spúšťate ako modul a interpret smeruje na `Module08/.venv`:
	- Spustite: `python -m samples.05.agents.coordinator`
	- Vyberte interpret: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Referencie
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Prehľad Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Ukážka volania funkcií (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

