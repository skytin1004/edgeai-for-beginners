<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4f786f5ea706270620f8e5dfb088e0c0",
  "translation_date": "2025-09-22T14:25:46+00:00",
  "source_file": "Module08/samples/05/README.md",
  "language_code": "ar"
}
-->
# الجلسة 5: نموذج تنسيق متعدد الوكلاء

يُظهر هذا النموذج نمط المنسق + المتخصصين باستخدام نقطة النهاية المتوافقة مع OpenAI في Foundry Local.

## التشغيل (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## التحقق
```cmd
curl http://localhost:8000/v1/models
```

## استكشاف الأخطاء وإصلاحها
- إذا أشار VS Code إلى أن `import specialists` غير محلولة في `coordinator.py`، تأكد من تشغيلها كـ وحدة وأن المفسر يشير إلى `Module08/.venv`:
	- تشغيل: `python -m samples.05.agents.coordinator`
	- اختيار المفسر: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## المراجع
- Foundry Local (تعلم): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- نظرة عامة على وكلاء Azure AI: https://learn.microsoft.com/azure/ai-services/agents/overview
- نموذج استدعاء الوظائف (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

