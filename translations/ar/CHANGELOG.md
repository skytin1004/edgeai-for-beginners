<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T14:16:30+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ar"
}
-->
# سجل التغييرات

جميع التغييرات الملحوظة في EdgeAI للمبتدئين موثقة هنا. يستخدم هذا المشروع إدخالات تعتمد على التاريخ وأسلوب "Keep a Changelog" (تمت الإضافة، التغيير، الإصلاح، الإزالة، التوثيق، النقل).

## 2025-09-18

### تمت الإضافة
- الوحدة 08: Microsoft Foundry Local – مجموعة أدوات المطور الكاملة
  - ست جلسات: الإعداد، تكامل Azure AI Foundry، النماذج مفتوحة المصدر، العروض التوضيحية المتقدمة، الوكلاء، والنماذج كأدوات
  - عينات قابلة للتشغيل تحت `Module08/samples/01`–`06` مع تعليمات Windows cmd
    - `01` دردشة REST السريعة (`chat_quickstart.py`)
    - `02` بدء سريع باستخدام SDK مع دعم OpenAI/Foundry Local وAzure OpenAI (`sdk_quickstart.py`)
    - `03` قائمة واختبار عبر CLI (`list_and_bench.cmd`)
    - `04` عرض Chainlit (`app.py`)
    - `05` تنسيق متعدد الوكلاء (`python -m samples.05.agents.coordinator`)
    - `06` توجيه النماذج كأدوات (`router.py`)
- دعم Azure OpenAI في عينة SDK للجلسة الثانية مع تكوين متغير البيئة
- `.vscode/settings.json` للإشارة إلى `Module08/.venv` وتحسين تحليل Python
- `.env` مع تلميح `PYTHONPATH` لوعي VS Code/Pylance

### تم التغيير
- تحديث النموذج الافتراضي إلى `phi-4-mini` عبر مستندات وعينات الوحدة 08؛ إزالة الإشارات المتبقية إلى `phi-3.5` داخل الوحدة 08
- تحسينات على التوجيه (`Module08/samples/06/router.py`):
  - اكتشاف النقاط النهائية عبر `foundry service status` مع تحليل regex
  - فحص صحة `/v1/models` عند بدء التشغيل
  - سجل النماذج القابل للتكوين عبر البيئة (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- تحديث المتطلبات: `Module08/requirements.txt` الآن يشمل `openai` (إلى جانب `requests`, `chainlit`)
- توضيح إرشادات عينة Chainlit وإضافة استكشاف الأخطاء وإصلاحها؛ حل الاستيراد عبر إعدادات مساحة العمل

### تم الإصلاح
- حل مشكلات الاستيراد:
  - لم يعد التوجيه يعتمد على وحدة `utils` غير موجودة؛ الوظائف مدمجة
  - يستخدم المنسق استيرادًا نسبيًا (`from .specialists import ...`) ويتم استدعاؤه عبر مسار الوحدة
  - تكوين VS Code/Pylance لحل استيرادات `chainlit` والحزم
- تصحيح خطأ مطبعي بسيط في `STUDY_GUIDE.md` وإضافة تغطية الوحدة 08

### تم الإزالة
- حذف `Module08/infra/obs.py` غير المستخدم وإزالة دليل `infra/` الفارغ؛ أنماط المراقبة محتفظ بها كاختيارية في المستندات

### تم النقل
- دمج عروض الوحدة 08 تحت `Module08/samples` مع مجلدات مرقمة للجلسات
  - نقل تطبيق Chainlit إلى `samples/04`
  - نقل الوكلاء إلى `samples/05` وإضافة ملفات `__init__.py` لحل الحزم

### التوثيق
- إثراء مستندات جلسات الوحدة 08 وجميع ملفات README الخاصة بالعينات بمراجع Microsoft Learn والموردين الموثوقين
- تحديث `Module08/README.md` مع نظرة عامة على العينات، تكوين التوجيه، ونصائح التحقق
- التحقق من قسم Windows Foundry Local في `Module07/README.md` مقابل مستندات Learn
- تحديث `STUDY_GUIDE.md`:
  - إضافة الوحدة 08 إلى النظرة العامة، الجداول الزمنية، متتبع التقدم
  - إضافة قسم مراجع شامل (Foundry Local، Azure AI، Olive، ONNX Runtime، OpenVINO، MLX، Llama.cpp، vLLM، Ollama، AI Toolkit، Windows ML)

---

## تاريخي (ملخص)
- إنشاء هيكل الدورة والوحدات (الوحدات 01–07)
- تحديث المحتوى بشكل تدريجي، توحيد التنسيق، وإضافة دراسات حالة
- توسيع تغطية أطر التحسين (Llama.cpp، Olive، OpenVINO، Apple MLX)

## غير منشور / قيد الانتظار (اقتراحات)
- اختبارات دخان اختيارية لكل عينة للتحقق من توفر Foundry Local
- مراجعة الترجمات لتنسيق إشارات النماذج (مثل `phi-4-mini`) حيثما كان ذلك مناسبًا
- إضافة تكوين pyright بسيط إذا فضل الفرق الصرامة على مستوى مساحة العمل

---

