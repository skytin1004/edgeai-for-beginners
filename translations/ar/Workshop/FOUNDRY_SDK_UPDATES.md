<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T06:39:47+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "ar"
}
-->
# تحديثات SDK المحلية لـ Foundry

## نظرة عامة

تم تحديث دفاتر الملاحظات والأدوات في الورشة لاستخدام **SDK المحلية الرسمية لـ Foundry بلغة Python** بشكل صحيح، وفقًا للأنماط الواردة في:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## الملفات المعدلة

### 1. `Workshop/samples/workshop_utils.py`

**التغييرات:**
- ✅ إضافة معالجة أخطاء الاستيراد لحزمة `foundry-local-sdk`
- ✅ تحسين التوثيق باستخدام أنماط SDK الرسمية
- ✅ تحسين تسجيل الأحداث باستخدام رموز Unicode (✓، ✗، ⚠)
- ✅ إضافة تعليقات توضيحية شاملة مع أمثلة
- ✅ تحسين رسائل الأخطاء بالإشارة إلى أوامر CLI
- ✅ تحديث التعليقات لتتوافق مع توثيق SDK الرسمي

**التحسينات الرئيسية:**

#### معالجة أخطاء الاستيراد
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### تحسين وظيفة `get_client()`
- إضافة توثيق مفصل حول نمط تهيئة SDK
- توضيح أن `FoundryLocalManager` يبدأ الخدمة تلقائيًا
- شرح حل الأسماء المستعارة للنماذج إلى النسخ المحسّنة للأجهزة
- تحسين تسجيل الأحداث بمعلومات حول نقطة النهاية
- تحسين رسائل الأخطاء مع اقتراح خطوات استكشاف الأخطاء وإصلاحها

#### تحسين وظيفة `chat_once()`
- إضافة تعليقات توضيحية شاملة مع أمثلة الاستخدام
- توضيح توافق SDK مع OpenAI
- توثيق دعم البث (عبر kwargs)
- تحسين رسائل الأخطاء مع اقتراح أوامر CLI
- إضافة ملاحظات حول التحقق من توفر النماذج

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**التغييرات:**
- ✅ تحديث جميع خلايا Markdown بالإشارات إلى SDK
- ✅ تحسين تعليقات الكود مع شرح أنماط SDK
- ✅ تحسين توثيق الخلايا وشرحها
- ✅ إضافة إرشادات استكشاف الأخطاء وإصلاحها
- ✅ تحديث كتالوج النماذج (استبدال 'gpt-oss-20b' بـ 'phi-3.5-mini')
- ✅ تحسين تنسيق المخرجات باستخدام مؤشرات بصرية
- ✅ إضافة روابط SDK وإشارات في جميع أنحاء الملف

**التحديثات لكل خلية:**

#### الخلية 1 (العنوان)
- إضافة روابط توثيق SDK
- الإشارة إلى مستودعات GitHub الرسمية

#### الخلية 2 (السيناريو)
- إعادة التنسيق باستخدام خطوات مرقمة
- توضيح نمط التوجيه القائم على النوايا
- التأكيد على فوائد التنفيذ المحلي

#### الخلية 3 (تثبيت التبعيات)
- إضافة شرح لما يوفره كل حزمة
- توثيق قدرات SDK (حل الأسماء المستعارة، تحسين الأجهزة)

#### الخلية 4 (إعداد البيئة)
- تحسين التعليقات التوضيحية للوظائف
- إضافة تعليقات داخلية تشرح أنماط SDK
- توثيق هيكل كتالوج النماذج
- توضيح مطابقة الأولوية/القدرات

#### الخلية 5 (التحقق من الكتالوج)
- إضافة علامات تحقق بصرية (✓)
- تحسين تنسيق المخرجات

#### الخلية 6 (اختبار الكشف عن النوايا)
- إعادة تنسيق المخرجات بأسلوب الجدول
- عرض النوايا والنموذج المختار

#### الخلية 7 (وظيفة التوجيه)
- شرح شامل لنمط SDK
- توثيق تدفق التهيئة
- سرد جميع الميزات (إعادة المحاولة، التتبع، الأخطاء)
- إضافة رابط SDK

#### الخلية 8 (عرض الدفعات)
- تحسين شرح ما يمكن توقعه
- إضافة قسم استكشاف الأخطاء وإصلاحها
- تضمين أوامر CLI للتصحيح
- تحسين عرض تنسيق المخرجات

### 3. `Workshop/notebooks/session06_README.md` (ملف جديد)

**تم إنشاء توثيق شامل يغطي:**

1. **نظرة عامة**: مخطط معماري وشرح المكونات
2. **تكامل SDK**: أمثلة على الكود تتبع الأنماط الرسمية
3. **المتطلبات**: تعليمات الإعداد خطوة بخطوة
4. **الاستخدام**: كيفية تشغيل وتخصيص دفتر الملاحظات
5. **أسماء النماذج المستعارة**: شرح النسخ المحسّنة للأجهزة
6. **استكشاف الأخطاء وإصلاحها**: المشكلات الشائعة والحلول
7. **التوسيع**: كيفية إضافة نوايا، نماذج، ومنطق مخصص
8. **نصائح الأداء**: أفضل الممارسات للاستخدام في الإنتاج
9. **الموارد**: روابط إلى الوثائق الرسمية والمجتمع

## تنفيذ نمط SDK

### النمط الرسمي (من وثائق Foundry Local)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### تنفيذنا (في workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**فوائد نهجنا:**
- ✅ يتبع نمط SDK الرسمي تمامًا
- ✅ يضيف التخزين المؤقت لتجنب التهيئة المتكررة
- ✅ يتضمن منطق إعادة المحاولة لتحسين الإنتاجية
- ✅ يدعم تتبع استخدام الرموز
- ✅ يوفر رسائل أخطاء أفضل
- ✅ يظل متوافقًا مع الأمثلة الرسمية

## تغييرات كتالوج النماذج

### قبل
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### بعد
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**السبب:** استبدال 'gpt-oss-20b' (اسم مستعار غير قياسي) بـ 'phi-3.5-mini' (اسم مستعار رسمي لـ Foundry Local).

## التبعيات

### تحديث requirements.txt

يتضمن ملف requirements.txt الخاص بالورشة بالفعل:
```
foundry-local-sdk
openai>=1.30.0
```

هذه هي الحزم الوحيدة المطلوبة لتكامل Foundry Local.

## اختبار التحديثات

### 1. التحقق من تشغيل Foundry Local

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. التحقق من النماذج المتاحة

```bash
foundry model ls
```

تأكد من توفر هذه النماذج أو أنها ستُحمّل تلقائيًا:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. تشغيل دفتر الملاحظات

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

أو افتحه في VS Code وقم بتشغيل جميع الخلايا.

### 4. السلوك المتوقع

**الخلية 1 (التثبيت):** تثبيت الحزم بنجاح  
**الخلية 2 (الإعداد):** لا توجد أخطاء، تعمل عمليات الاستيراد  
**الخلية 3 (التحقق):** تظهر ✓ مع قائمة النماذج  
**الخلية 4 (اختبار النوايا):** تظهر نتائج الكشف عن النوايا  
**الخلية 5 (التوجيه):** تظهر ✓ وظيفة التوجيه جاهزة  
**الخلية 6 (التنفيذ):** توجه المطالبات إلى النماذج، وتظهر النتائج  

### 5. استكشاف أخطاء اتصال API وإصلاحها

إذا رأيت `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## متغيرات البيئة

المتغيرات البيئية التالية مدعومة:

| المتغير | الافتراضي | الوصف |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | اضبطه على `1` لطباعة استخدام الرموز |
| `RETRY_ON_FAIL` | `1` | تمكين منطق إعادة المحاولة |
| `RETRY_BACKOFF` | `1.0` | تأخير إعادة المحاولة الأولي (بالثواني) |
| `FOUNDRY_LOCAL_ENDPOINT` | تلقائي | تجاوز نقطة نهاية الخدمة |

### أمثلة الاستخدام

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## الانتقال من النمط القديم

إذا كان لديك كود موجود يستخدم استدعاءات API مباشرة، إليك كيفية الانتقال:

### قبل (استدعاء API مباشر)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### بعد (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### فوائد الانتقال
- ✅ إدارة الخدمة تلقائيًا
- ✅ حل الأسماء المستعارة للنماذج
- ✅ اختيار تحسين الأجهزة
- ✅ معالجة أخطاء أفضل
- ✅ توافق مع SDK الخاص بـ OpenAI
- ✅ دعم البث

## المراجع

### الوثائق الرسمية
- **GitHub لـ Foundry Local**: https://github.com/microsoft/Foundry-Local
- **مصدر SDK بلغة Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **مرجع CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **استكشاف الأخطاء وإصلاحها**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### موارد الورشة
- **README للجلسة 06**: `Workshop/notebooks/session06_README.md`
- **أدوات الورشة**: `Workshop/samples/workshop_utils.py`
- **دفتر الملاحظات النموذجي**: `Workshop/notebooks/session06_models_router.ipynb`

### المجتمع
- **Discord**: https://aka.ms/foundry-local-discord
- **مشكلات GitHub**: https://github.com/microsoft/Foundry-Local/issues

## الخطوات التالية

1. **مراجعة التغييرات**: اقرأ الملفات المحدثة  
2. **اختبار دفتر الملاحظات**: تشغيل session06_models_router.ipynb  
3. **التحقق من SDK**: تأكد من تثبيت foundry-local-sdk  
4. **التحقق من الخدمة**: تأكد من تشغيل Foundry Local  
5. **استكشاف الوثائق**: اقرأ الملف الجديد session06_README.md  

## الملخص

تضمن هذه التحديثات أن مواد الورشة تتبع **أنماط SDK الرسمية لـ Foundry Local** تمامًا كما هو موثق في مستودع GitHub. جميع أمثلة الكود، التوثيق، والأدوات الآن تتماشى مع أفضل الممارسات الموصى بها من Microsoft لنشر نماذج الذكاء الاصطناعي محليًا.

التغييرات تحسن:
- ✅ **الدقة**: استخدام أنماط SDK الرسمية  
- ✅ **التوثيق**: شروحات وأمثلة شاملة  
- ✅ **معالجة الأخطاء**: رسائل أفضل وإرشادات استكشاف الأخطاء  
- ✅ **سهولة الصيانة**: اتباع الاتفاقيات الرسمية  
- ✅ **تجربة المستخدم**: تعليمات أوضح ومساعدة في التصحيح  

---

**تاريخ التحديث:** 8 أكتوبر 2025  
**إصدار SDK:** foundry-local-sdk (الأحدث)  
**فرع الورشة:** Reactor

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.