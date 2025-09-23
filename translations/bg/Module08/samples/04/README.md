<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-23T01:20:15+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "bg"
}
-->
# Сесия 4 Пример: Chainlit RAG Демонстрация

Стартирайте минималното приложение Chainlit срещу Foundry Local.

## Предпоставки
- Windows 11, Python 3.10+
- Инсталиран Foundry Local и наличен модел (например `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## Стартиране (cmd.exe)
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

## Отстраняване на проблеми
- Ако VS Code показва "chainlit could not be resolved":
	- Изберете интерпретатора `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Уверете се, че зависимостите са инсталирани: `pip install -r Module08\requirements.txt`

## Референции
- Ръководство за Open WebUI (чат приложение с Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Научете): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

