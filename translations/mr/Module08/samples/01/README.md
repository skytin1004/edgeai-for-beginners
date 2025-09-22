<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T17:47:20+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "mr"
}
-->
# सत्र 1 नमुना: REST च्या माध्यमातून जलद चॅट

Python `requests` वापरून Foundry Local वर एक साधा चॅट विनंती चालवा.

## पूर्वतयारी
- Foundry Local सेवा चालू असलेली मॉडेल (उदा., `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## चालवा (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## संदर्भ
- Foundry Local (शिका): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-सुसंगत API विहंगावलोकन: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

