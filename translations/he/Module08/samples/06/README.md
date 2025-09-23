<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T21:53:48+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "he"
}
-->
# דוגמה למפגש 6: מודלים ככלים

הדוגמה הזו מיישמת רישום כלים + נתב מינימלי שבוחר מודל על בסיס בקשת המשתמש ומבצע קריאה לנקודת הקצה של Foundry Local התואמת ל-OpenAI.

## קבצים
- `router.py`: רישום פשוט וניתוב לפי היגיון; גילוי נקודת קצה + בדיקת תקינות.

## הפעלה (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## הערות
- הנתב משתמש בהיגיון פשוט של מילות מפתח כדי לבחור בין כלים `general`, `reasoning`, ו-`code` ומדפיס `/v1/models` בעת ההפעלה.
- ניתן להגדיר באמצעות משתני סביבה:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-distill-qwen-7b"},"code":{"model":"qwen2.5-7b-instruct"}}
```

## מקורות
- Foundry Local (לימוד): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- אינטגרציה עם SDKs להסקה: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

