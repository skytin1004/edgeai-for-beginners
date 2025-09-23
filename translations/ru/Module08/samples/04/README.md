<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T14:26:07+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "ru"
}
-->
# Сессия 4 Пример: Chainlit RAG Демонстрация

Запустите минимальное приложение Chainlit с Foundry Local.

## Предварительные требования
- Windows 11, Python 3.10+
- Установлен Foundry Local и доступна модель (например, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Запуск (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## Проверка
```cmd
curl http://localhost:8000/v1/models
```

## Устранение неполадок
- Если VS Code показывает "chainlit could not be resolved":
	- Выберите интерпретатор `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Убедитесь, что зависимости установлены: `pip install -r Module08\requirements.txt`

## Ссылки
- Руководство по Open WebUI (чат-приложение с Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Учебные материалы): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

