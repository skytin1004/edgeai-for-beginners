<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T13:41:19+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "hi"
}
-->
# सत्र 4 नमूना: Chainlit RAG डेमो

Foundry Local के खिलाफ न्यूनतम Chainlit ऐप चलाएं।

## आवश्यकताएँ
- Windows 11, Python 3.10+
- Foundry Local इंस्टॉल किया हुआ और एक मॉडल उपलब्ध (जैसे, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## चलाएँ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## सत्यापन करें
```cmd
curl http://localhost:8000/v1/models
```

## समस्या निवारण
- यदि VS Code "chainlit को हल नहीं किया जा सका" दिखाता है:
	- इंटरप्रेटर चुनें `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- सुनिश्चित करें कि डिपेंडेंसी इंस्टॉल हैं: `pip install -r Module08\requirements.txt`

## संदर्भ
- Open WebUI कैसे करें (Open WebUI के साथ चैट ऐप): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (सीखें): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

