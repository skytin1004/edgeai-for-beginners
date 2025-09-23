<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T13:40:40+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "hi"
}
-->
# सत्र 1 नमूना: REST के माध्यम से त्वरित चैट

Python `requests` का उपयोग करके Foundry Local पर एक न्यूनतम चैट अनुरोध चलाएं।

## आवश्यकताएँ
- Foundry Local सेवा जो एक मॉडल चला रही हो (जैसे, `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## चलाएँ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## संदर्भ
- Foundry Local (सीखें): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-संगत API अवलोकन: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

