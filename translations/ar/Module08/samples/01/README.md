<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T14:25:35+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "ar"
}
-->
# الجلسة 1: مثال دردشة سريعة عبر REST

قم بتشغيل طلب دردشة بسيط إلى Foundry Local باستخدام مكتبة `requests` في بايثون.

## المتطلبات الأساسية
- خدمة Foundry Local تعمل بنموذج (مثل `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## التشغيل (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## المراجع
- Foundry Local (تعلم): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- نظرة عامة على واجهة برمجة التطبيقات المتوافقة مع OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

