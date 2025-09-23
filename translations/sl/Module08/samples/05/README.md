<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-23T01:18:51+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "sl"
}
-->
# Seja 5 Primer: Orkestracija več agentov

Ta primer prikazuje vzorec koordinatorja + specialistov z uporabo OpenAI-kompatibilne točke Foundry Local.

## Zagon (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Preverjanje
```cmd
curl http://localhost:8000/v1/models
```

## Odpravljanje težav
- Če VS Code označi `import specialists` kot nerešen v datoteki `coordinator.py`, se prepričajte, da izvajate kot modul in da interpreter kaže na `Module08/.venv`:
	- Zagon: `python -m samples.05.agents.coordinator`
	- Izberite interpreter: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Reference
- Foundry Local (Učenje): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Pregled Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Primer klicanja funkcij (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

