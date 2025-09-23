<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T17:47:22+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "ne"
}
-->
# सत्र १ नमूना: REST मार्फत छिटो कुराकानी

Python `requests` प्रयोग गरेर Foundry Local मा न्यूनतम च्याट अनुरोध चलाउनुहोस्।

## आवश्यकताहरू
- Foundry Local सेवा चलिरहेको मोडेल (जस्तै, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## चलाउनुहोस् (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## सन्दर्भहरू
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-संगत API अवलोकन: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

