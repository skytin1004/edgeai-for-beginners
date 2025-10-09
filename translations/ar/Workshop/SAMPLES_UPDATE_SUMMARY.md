<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T07:00:20+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "ar"
}
-->
# عينات ورشة العمل - ملخص تحديث SDK المحلي لـ Foundry

## نظرة عامة

تم تحديث جميع عينات Python في دليل `Workshop/samples` لتتبع أفضل الممارسات لـ Foundry Local SDK وضمان التناسق عبر ورشة العمل.

**التاريخ**: 8 أكتوبر 2025  
**النطاق**: 9 ملفات Python عبر 6 جلسات ورشة عمل  
**التركيز الأساسي**: معالجة الأخطاء، التوثيق، أنماط SDK، تجربة المستخدم

---

## الملفات المحدثة

### الجلسة 01: البداية
- ✅ `chat_bootstrap.py` - أمثلة أساسية للدردشة والبث

### الجلسة 02: حلول RAG
- ✅ `rag_pipeline.py` - تنفيذ RAG باستخدام التضمينات
- ✅ `rag_eval_ragas.py` - تقييم RAG باستخدام مقاييس RAGAS

### الجلسة 03: نماذج مفتوحة المصدر
- ✅ `benchmark_oss_models.py` - قياس أداء متعدد النماذج

### الجلسة 04: نماذج متقدمة
- ✅ `model_compare.py` - مقارنة بين SLM و LLM

### الجلسة 05: وكلاء مدعومون بالذكاء الاصطناعي
- ✅ `agents_orchestrator.py` - تنسيق متعدد الوكلاء

### الجلسة 06: النماذج كأدوات
- ✅ `models_router.py` - توجيه النماذج بناءً على النوايا
- ✅ `models_pipeline.py` - خط أنابيب متعدد الخطوات موجه

### البنية التحتية الداعمة
- ✅ `workshop_utils.py` - يتبع بالفعل أفضل الممارسات (لا حاجة للتغييرات)

---

## التحسينات الرئيسية

### 1. تحسين معالجة الأخطاء

**قبل:**
```python
manager, client, model_id = get_client(alias)
```

**بعد:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**الفوائد:**
- معالجة الأخطاء بسلاسة مع رسائل خطأ واضحة
- نصائح قابلة للتنفيذ لاستكشاف الأخطاء وإصلاحها
- رموز خروج مناسبة للبرمجة النصية

### 2. إدارة أفضل للاستيراد

**قبل:**
```python
from sentence_transformers import SentenceTransformer
```

**بعد:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**الفوائد:**
- إرشادات واضحة عند فقدان التبعيات
- منع أخطاء الاستيراد الغامضة
- تعليمات تثبيت سهلة الاستخدام

### 3. توثيق شامل

**تمت الإضافة إلى جميع العينات:**
- توثيق متغيرات البيئة في docstrings
- روابط مرجعية لـ SDK
- أمثلة الاستخدام
- توثيق مفصل للوظائف/المعلمات
- تلميحات الأنواع لدعم أفضل في IDE

**مثال:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. تحسين ردود فعل المستخدم

**إضافة تسجيل معلوماتي:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**مؤشرات التقدم:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**إخراج منظم:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. قياس أداء قوي

**تحسينات الجلسة 03:**
- معالجة الأخطاء لكل نموذج (يستمر عند الفشل)
- تقارير تقدم مفصلة
- تنفيذ جولات الإحماء بشكل صحيح
- دعم قياس زمن الاستجابة لأول رمز
- فصل واضح للمراحل

### 6. تلميحات الأنواع المتسقة

**تمت الإضافة في جميع الأنحاء:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**الفوائد:**
- إكمال تلقائي أفضل في IDE
- اكتشاف الأخطاء مبكرًا
- كود موثق ذاتيًا

### 7. تحسين توجيه النماذج

**تحسينات الجلسة 06:**
- توثيق شامل لاكتشاف النوايا
- شرح خوارزمية اختيار النموذج
- سجلات توجيه مفصلة
- تنسيق إخراج الاختبار
- استرداد الأخطاء في اختبار الدُفعات

### 8. تنسيق متعدد الوكلاء

**تحسينات الجلسة 05:**
- تقارير تقدم مرحلة بمرحلة
- معالجة الأخطاء لكل وكيل
- هيكل خط أنابيب واضح
- توثيق أفضل لإدارة الذاكرة

---

## قائمة التحقق للاختبار

### المتطلبات الأساسية
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### اختبار كل عينة

#### الجلسة 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### الجلسة 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### الجلسة 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### الجلسة 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### الجلسة 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### الجلسة 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## مرجع متغيرات البيئة

### عالمي (جميع العينات)
| المتغير | الوصف | الافتراضي |
|---------|-------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | الاسم المستعار للنموذج المستخدم | يختلف حسب العينة |
| `FOUNDRY_LOCAL_ENDPOINT` | تجاوز نقطة خدمة | يتم اكتشافها تلقائيًا |
| `SHOW_USAGE` | عرض استخدام الرموز | `0` |
| `RETRY_ON_FAIL` | تمكين منطق إعادة المحاولة | `1` |
| `RETRY_BACKOFF` | تأخير إعادة المحاولة الأولي | `1.0` |

### خاص بالعينة
| المتغير | مستخدم بواسطة | الوصف |
|---------|---------------|-------|
| `EMBED_MODEL` | الجلسة 02 | اسم نموذج التضمين |
| `RAG_QUESTION` | الجلسة 02 | سؤال اختبار لـ RAG |
| `BENCH_MODELS` | الجلسة 03 | نماذج مفصولة بفواصل لقياس الأداء |
| `BENCH_ROUNDS` | الجلسة 03 | عدد جولات قياس الأداء |
| `BENCH_PROMPT` | الجلسة 03 | موجه اختبار لقياس الأداء |
| `BENCH_STREAM` | الجلسة 03 | قياس زمن الاستجابة لأول رمز |
| `SLM_ALIAS` | الجلسة 04 | نموذج لغة صغير |
| `LLM_ALIAS` | الجلسة 04 | نموذج لغة كبير |
| `COMPARE_PROMPT` | الجلسة 04 | موجه اختبار المقارنة |
| `AGENT_MODEL_PRIMARY` | الجلسة 05 | نموذج الوكيل الأساسي |
| `AGENT_MODEL_EDITOR` | الجلسة 05 | نموذج وكيل المحرر |
| `AGENT_QUESTION` | الجلسة 05 | سؤال اختبار للوكلاء |
| `PIPELINE_TASK` | الجلسة 06 | مهمة لخط الأنابيب |

---

## تغييرات كبيرة

**لا توجد** - جميع التغييرات متوافقة مع الإصدارات السابقة.

ستستمر البرامج النصية الحالية في العمل. الميزات الجديدة هي:
- متغيرات البيئة اختيارية
- رسائل خطأ محسنة (لا تكسر الوظائف)
- تسجيل إضافي (يمكن قمعه)
- تلميحات الأنواع الأفضل (لا تأثير على وقت التشغيل)

---

## أفضل الممارسات المنفذة

### 1. استخدام دائم لـ Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. نمط معالجة الأخطاء المناسب
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. تسجيل معلوماتي
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. تلميحات الأنواع
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Docstrings شاملة
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. دعم متغيرات البيئة
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. تدهور سلس
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## المشكلات الشائعة والحلول

### المشكلة: أخطاء الاستيراد
**الحل:** تثبيت التبعيات المفقودة
```bash
pip install sentence-transformers ragas datasets numpy
```

### المشكلة: أخطاء الاتصال
**الحل:** تأكد من تشغيل Foundry Local
```bash
foundry service status
foundry model run phi-4-mini
```

### المشكلة: النموذج غير موجود
**الحل:** تحقق من النماذج المتاحة
```bash
foundry model ls
foundry model download <alias>
```

### المشكلة: الأداء البطيء
**الحل:** استخدم نماذج أصغر أو قم بضبط المعلمات
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## الخطوات التالية

### 1. اختبار جميع العينات
قم بتنفيذ قائمة التحقق للاختبار أعلاه للتحقق من عمل جميع العينات بشكل صحيح.

### 2. تحديث التوثيق
- تحديث ملفات Markdown للجلسات بأمثلة جديدة
- إضافة قسم استكشاف الأخطاء وإصلاحها إلى README الرئيسي
- إنشاء دليل مرجعي سريع

### 3. إنشاء اختبارات تكامل
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. إضافة قياسات الأداء
تتبع تحسينات الأداء الناتجة عن تحسينات معالجة الأخطاء.

### 5. ردود فعل المستخدم
جمع ردود الفعل من المشاركين في ورشة العمل حول:
- وضوح رسائل الخطأ
- اكتمال التوثيق
- سهولة الاستخدام

---

## الموارد

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **المرجع السريع**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **ملاحظات الترحيل**: `Workshop/SDK_MIGRATION_NOTES.md`
- **المستودع الرئيسي**: https://github.com/microsoft/Foundry-Local

---

## الصيانة

### إضافة عينات جديدة
اتبع هذه الأنماط عند إنشاء عينات جديدة:

1. استخدم `workshop_utils` لإدارة العميل
2. أضف معالجة شاملة للأخطاء
3. قم بتضمين دعم متغيرات البيئة
4. أضف تلميحات الأنواع و docstrings
5. قدم تسجيل معلوماتي
6. قم بتضمين أمثلة الاستخدام في docstring
7. قم بالربط بتوثيق SDK

### مراجعة التحديثات
عند مراجعة تحديثات العينات، تحقق من:
- [ ] معالجة الأخطاء في جميع عمليات الإدخال/الإخراج
- [ ] تلميحات الأنواع في الوظائف العامة
- [ ] Docstrings شاملة
- [ ] توثيق متغيرات البيئة
- [ ] ردود فعل المستخدم المعلوماتية
- [ ] روابط مرجعية لـ SDK
- [ ] نمط كود متسق

---

**الملخص**: جميع عينات Python في ورشة العمل تتبع الآن أفضل الممارسات لـ Foundry Local SDK مع تحسين معالجة الأخطاء، توثيق شامل، وتجربة مستخدم محسنة. لا توجد تغييرات كبيرة - تم الحفاظ على جميع الوظائف الحالية وتحسينها.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.