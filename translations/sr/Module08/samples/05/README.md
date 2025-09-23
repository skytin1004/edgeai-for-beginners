<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-23T01:18:44+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "sr"
}
-->
# Сесија 5 Пример: Оркестрација више агената

Овај пример демонстрира образац координатора + специјалиста користећи OpenAI-компатибилни крајњи тачку Foundry Local-а.

## Покрени (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Потврди
```cmd
curl http://localhost:8000/v1/models
```

## Решавање проблема
- Ако VS Code означи `import specialists` као нерешен у `coordinator.py`, уверите се да покрећете као модул и да интерпретер показује на `Module08/.venv`:
	- Покрени: `python -m samples.05.agents.coordinator`
	- Изабери интерпретер: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Референце
- Foundry Local (Учите): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Преглед Azure AI агената: https://learn.microsoft.com/azure/ai-services/agents/overview
- Пример позивања функција (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

