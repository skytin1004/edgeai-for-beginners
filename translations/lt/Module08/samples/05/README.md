<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-23T01:19:03+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "lt"
}
-->
# 5 sesijos pavyzdys: Daugelio agentų koordinavimas

Šiame pavyzdyje demonstruojamas koordinatoriaus + specialistų modelis naudojant Foundry Local OpenAI suderinamą galinį tašką.

## Paleidimas (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Patikrinimas
```cmd
curl http://localhost:8000/v1/models
```

## Trikčių šalinimas
- Jei VS Code pažymi `import specialists` kaip neišspręstą `coordinator.py` faile, įsitikinkite, kad paleidžiate kaip modulį ir interpretatorius nukreiptas į `Module08/.venv`:
	- Paleiskite: `python -m samples.05.agents.coordinator`
	- Pasirinkite interpretatorių: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Nuorodos
- Foundry Local (Mokymasis): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI agentų apžvalga: https://learn.microsoft.com/azure/ai-services/agents/overview
- Funkcijų kvietimo pavyzdys (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

