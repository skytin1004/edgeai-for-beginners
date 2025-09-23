<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T14:25:59+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "ar"
}
-->
# نموذج الجلسة 6: النماذج كأدوات

يُظهر هذا المثال تنفيذًا بسيطًا لموجه + سجل أدوات يقوم باختيار نموذج بناءً على طلب المستخدم واستدعاء نقطة النهاية المتوافقة مع OpenAI الخاصة بـ Foundry Local.

## الملفات
- `router.py`: سجل بسيط وتوجيه يعتمد على الاستدلال؛ اكتشاف نقطة النهاية + التحقق من الصحة.

## التشغيل (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## ملاحظات
- يستخدم الموجه استدلالات بسيطة تعتمد على الكلمات المفتاحية للاختيار بين أدوات `general` و`reasoning` و`code` ويعرض `/v1/models` عند بدء التشغيل.
- يمكن التهيئة عبر متغيرات البيئة:
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

## المراجع
- Foundry Local (تعلم): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- التكامل مع حزم SDK للاستدلال: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

