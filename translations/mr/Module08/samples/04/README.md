<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T17:47:58+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "mr"
}
-->
# सत्र 4 नमुना: Chainlit RAG डेमो

Foundry Local वर मिनिमल Chainlit अ‍ॅप चालवा.

## पूर्वतयारी
- Windows 11, Python 3.10+
- Foundry Local स्थापित केलेले आणि एक मॉडेल उपलब्ध (उदा., `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## चालवा (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## पडताळणी करा
```cmd
curl http://localhost:8000/v1/models
```

## समस्या निराकरण
- जर VS Code "chainlit could not be resolved" दाखवत असेल:
	- Interpreter निवडा `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- Dependencies स्थापित आहेत याची खात्री करा: `pip install -r Module08\requirements.txt`

## संदर्भ
- Open WebUI कसे करावे (Open WebUI सह चॅट अ‍ॅप): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (शिका): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

