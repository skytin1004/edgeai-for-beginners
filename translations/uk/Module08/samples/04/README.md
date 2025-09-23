<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-23T01:20:34+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "uk"
}
-->
# Сесія 4: Демонстрація Chainlit RAG

Запустіть мінімальний додаток Chainlit з Foundry Local.

## Передумови
- Windows 11, Python 3.10+
- Встановлений Foundry Local і доступна модель (наприклад, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Запуск (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Перевірка
```cmd
curl http://localhost:8000/v1/models
```

## Вирішення проблем
- Якщо VS Code показує "chainlit could not be resolved":
	- Виберіть інтерпретатор `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Переконайтеся, що залежності встановлені: `pip install -r Module08\requirements.txt`

## Посилання
- Інструкція Open WebUI (чат-додаток з Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

