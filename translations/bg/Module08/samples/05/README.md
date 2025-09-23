<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-23T01:18:40+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "bg"
}
-->
# Сесия 5 Пример: Оркестрация на множество агенти

Този пример демонстрира модел на координатор + специалисти, използвайки OpenAI-съвместимия край на Foundry Local.

## Стартиране (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Валидиране
```cmd
curl http://localhost:8000/v1/models
```

## Отстраняване на проблеми
- Ако VS Code маркира `import specialists` като нерешен в `coordinator.py`, уверете се, че стартирате като модул и интерпретаторът сочи към `Module08/.venv`:
	- Стартиране: `python -m samples.05.agents.coordinator`
	- Избор на интерпретатор: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Референции
- Foundry Local (Научете): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Преглед на Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Пример за извикване на функции (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

