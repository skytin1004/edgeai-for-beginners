<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-23T01:18:01+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "sr"
}
-->
# Сесија 1 Пример: Брзи разговор преко REST-а

Покрените минимални захтев за разговор ка Foundry Local користећи Python `requests`.

## Предуслови
- Foundry Local сервис који покреће модел (нпр. `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## Покретање (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## Референце
- Foundry Local (Учите): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- Преглед API-ја компатибилног са OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

