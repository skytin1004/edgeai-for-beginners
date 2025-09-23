<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bf711f77cca7c5500e22ff5c032016f1",
  "translation_date": "2025-09-23T01:21:30+00:00",
  "source_file": "Module08/samples/02/README.md",
  "language_code": "sr"
}
-->
# Сесија 2 Пример: Интеграција SDK-а

Користите OpenAI Python SDK за позивање Foundry Local (компатибилно са OpenAI) или Azure OpenAI.

## Инсталација
```cmd
cd Module08
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Покретање
Foundry Local (подразумевано):
```cmd
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```

Azure OpenAI:
```cmd
set AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
set AZURE_OPENAI_API_KEY=<your-key>
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=<your-deployment-name>
python samples\02\sdk_quickstart.py
```

---

