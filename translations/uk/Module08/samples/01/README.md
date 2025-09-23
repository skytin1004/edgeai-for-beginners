<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-23T01:18:12+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "uk"
}
-->
# Сесія 1 Зразок: Швидкий чат через REST

Запустіть мінімальний запит чату до Foundry Local за допомогою Python `requests`.

## Попередні умови
- Сервіс Foundry Local, який працює з моделлю (наприклад, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Запуск (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Посилання
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Огляд API, сумісного з OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

