<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T17:48:01+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "ne"
}
-->
# सत्र ४ नमूना: Chainlit RAG डेमो

Foundry Local विरुद्ध न्यूनतम Chainlit एप चलाउनुहोस्।

## आवश्यकताहरू
- Windows 11, Python 3.10+
- Foundry Local स्थापना गरिएको र एउटा मोडेल उपलब्ध (जस्तै, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## चलाउनुहोस् (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## प्रमाणित गर्नुहोस्
```cmd
curl http://localhost:8000/v1/models
```

## समस्या समाधान
- यदि VS Code ले "chainlit could not be resolved" देखाउँछ भने:
	- इन्टरप्रेटर चयन गर्नुहोस् `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- सुनिश्चित गर्नुहोस् कि निर्भरता स्थापना गरिएको छ: `pip install -r Module08\requirements.txt`

## सन्दर्भहरू
- Open WebUI कसरी गर्ने (Open WebUI सँग च्याट एप): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

