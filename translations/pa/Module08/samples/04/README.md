<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T18:34:54+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "pa"
}
-->
# ਸੈਸ਼ਨ 4 ਨਮੂਨਾ: ਚੇਨਲਿਟ RAG ਡੈਮੋ

Foundry Local ਦੇ ਖਿਲਾਫ ਘੱਟੋ-ਘੱਟ Chainlit ਐਪ ਚਲਾਓ।

## ਪੂਰਵ ਸ਼ਰਤਾਂ
- Windows 11, Python 3.10+
- Foundry Local ਇੰਸਟਾਲ ਕੀਤਾ ਹੋਇਆ ਅਤੇ ਇੱਕ ਮਾਡਲ ਉਪਲਬਧ (ਜਿਵੇਂ ਕਿ `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## ਚਲਾਓ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## ਪ੍ਰਮਾਣਿਤ ਕਰੋ
```cmd
curl http://localhost:8000/v1/models
```

## ਸਮੱਸਿਆ ਹੱਲ
- ਜੇ VS Code "chainlit could not be resolved" ਦਿਖਾਉਂਦਾ ਹੈ:
	- ਇੰਟਰਪ੍ਰੀਟਰ ਚੁਣੋ `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- ਯਕੀਨੀ ਬਣਾਓ ਕਿ deps ਇੰਸਟਾਲ ਕੀਤੇ ਗਏ ਹਨ: `pip install -r Module08\requirements.txt`

## ਸੰਦਰਭ
- Open WebUI how-to (ਚੈਟ ਐਪ ਨਾਲ Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (ਸਿੱਖੋ): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

