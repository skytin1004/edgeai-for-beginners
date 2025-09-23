<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bf711f77cca7c5500e22ff5c032016f1",
  "translation_date": "2025-09-22T13:41:35+00:00",
  "source_file": "Module08/samples/02/README.md",
  "language_code": "hi"
}
-->
# सत्र 2 नमूना: SDK एकीकरण

OpenAI Python SDK का उपयोग करके या तो Foundry Local (OpenAI-संगत) या Azure OpenAI को कॉल करें।

## इंस्टॉल
```cmd
cd Module08
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## चलाएं
Foundry Local (डिफ़ॉल्ट):
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

