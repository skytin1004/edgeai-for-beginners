<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-23T01:17:58+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "bg"
}
-->
# Сесия 1 Пример: Бърз чат чрез REST

Изпълнете минимална заявка за чат към Foundry Local, използвайки Python `requests`.

## Предпоставки
- Услугата Foundry Local, която изпълнява модел (например, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Изпълнение (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Референции
- Foundry Local (Научете): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Преглед на API, съвместим с OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

