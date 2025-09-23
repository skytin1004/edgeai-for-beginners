<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bf711f77cca7c5500e22ff5c032016f1",
  "translation_date": "2025-09-22T18:35:26+00:00",
  "source_file": "Module08/samples/02/README.md",
  "language_code": "tr"
}
-->
# Oturum 2 Örneği: SDK Entegrasyonu

OpenAI Python SDK'sini kullanarak Foundry Local (OpenAI uyumlu) veya Azure OpenAI'yi çağırın.

## Kurulum
```cmd
cd Module08
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Çalıştırma
Foundry Local (varsayılan):
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

