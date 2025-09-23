<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T14:25:32+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "ru"
}
-->
# Сессия 1 Пример: Быстрый чат через REST

Выполните минимальный запрос чата к Foundry Local с использованием Python `requests`.

## Предварительные требования
- Сервис Foundry Local с запущенной моделью (например, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Запуск (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Ссылки
- Foundry Local (Учебник): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Обзор API, совместимого с OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

