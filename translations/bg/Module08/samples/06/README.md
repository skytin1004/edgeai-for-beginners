<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-23T01:19:28+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "bg"
}
-->
# Сесия 6 Пример: Модели като инструменти

Този пример реализира минимален рутер + регистър на инструменти, който избира модел въз основа на потребителския въпрос и извиква OpenAI-съвместимия крайна точка на Foundry Local.

## Файлове
- `router.py`: прост регистър и евристично маршрутизиране; откриване на крайна точка + проверка на състоянието.

## Стартиране (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Бележки
- Рутерът използва прости евристики с ключови думи, за да избере между инструментите `general`, `reasoning` и `code` и отпечатва `/v1/models` при стартиране.
- Конфигуриране чрез променливи на средата:
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

## Референции
- Foundry Local (Научи): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Интеграция с SDK за изводи: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

