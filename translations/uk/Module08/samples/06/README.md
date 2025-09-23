<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-23T01:19:46+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "uk"
}
-->
# Сесія 6 Зразок: Моделі як інструменти

Цей зразок реалізує мінімальний маршрутизатор + реєстр інструментів, який вибирає модель на основі запиту користувача та викликає сумісну з OpenAI кінцеву точку Foundry Local.

## Файли
- `router.py`: простий реєстр і маршрутизація за евристикою; виявлення кінцевої точки + перевірка стану.

## Запуск (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Примітки
- Маршрутизатор використовує прості евристики ключових слів для вибору між інструментами `general`, `reasoning` і `code` та друкує `/v1/models` при запуску.
- Налаштування через змінні середовища:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-distill-qwen-7b"},"code":{"model":"qwen2.5-7b-instruct"}}
```

## Посилання
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Інтеграція з SDK для інференсу: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

