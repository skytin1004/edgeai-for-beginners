<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T14:26:11+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "ar"
}
-->
# الجلسة 4: عرض توضيحي لـ Chainlit RAG

تشغيل تطبيق Chainlit البسيط باستخدام Foundry Local.

## المتطلبات الأساسية
- ويندوز 11، بايثون 3.10+
- تثبيت Foundry Local وتوفر نموذج (مثل `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## التشغيل (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## التحقق
```cmd
curl http://localhost:8000/v1/models
```

## استكشاف الأخطاء وإصلاحها
- إذا ظهرت رسالة في VS Code تقول "chainlit could not be resolved":
	- اختر المفسر `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- تأكد من تثبيت التبعيات: `pip install -r Module08\requirements.txt`

## المراجع
- كيفية فتح WebUI (تطبيق دردشة باستخدام Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (تعلم): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

