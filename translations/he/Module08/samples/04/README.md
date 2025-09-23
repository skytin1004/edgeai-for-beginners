<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T21:53:59+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "he"
}
-->
# דוגמה למפגש 4: Chainlit RAG Demo

הרצת אפליקציית Chainlit מינימלית מול Foundry Local.

## דרישות מוקדמות
- Windows 11, Python 3.10+
- Foundry Local מותקן ודגם זמין (לדוגמה, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## הרצה (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## אימות
```cmd
curl http://localhost:8000/v1/models
```

## פתרון בעיות
- אם VS Code מציג "chainlit could not be resolved":
	- בחרו את המפרש `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- ודאו שהספריות מותקנות: `pip install -r Module08\requirements.txt`

## מקורות
- מדריך Open WebUI (אפליקציית צ'אט עם Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (לימוד): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

