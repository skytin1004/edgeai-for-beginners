<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bf711f77cca7c5500e22ff5c032016f1",
  "translation_date": "2025-09-23T01:21:19+00:00",
  "source_file": "Module08/samples/02/README.md",
  "language_code": "hu"
}
-->
# 2. munkamenet példa: SDK integráció

Használja az OpenAI Python SDK-t, hogy hívásokat kezdeményezzen Foundry Local (OpenAI-kompatibilis) vagy Azure OpenAI felé.

## Telepítés
```cmd
cd Module08
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Futtatás
Foundry Local (alapértelmezett):
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

