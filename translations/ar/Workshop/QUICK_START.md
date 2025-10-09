<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-09T06:41:00+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "ar"
}
-->
# دليل البدء السريع للورشة

## المتطلبات الأساسية

### 1. تثبيت Foundry Local

اتبع دليل التثبيت الرسمي:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. تثبيت تبعيات Python

من دليل الورشة:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## تشغيل أمثلة الورشة

### الجلسة 01: الدردشة الأساسية

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**المتغيرات البيئية:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### الجلسة 02: خط أنابيب RAG

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**المتغيرات البيئية:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### الجلسة 02: تقييم RAG (Ragas)

```bash
python rag_eval_ragas.py
```

**ملاحظة**: يتطلب تثبيت تبعيات إضافية عبر `requirements.txt`

### الجلسة 03: قياس الأداء

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**المتغيرات البيئية:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**الناتج**: JSON يحتوي على مقاييس التأخير، الإنتاجية، وأول رمز

### الجلسة 04: مقارنة النماذج

```bash
cd Workshop/samples/session04
python model_compare.py
```

**المتغيرات البيئية:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### الجلسة 05: تنسيق متعدد الوكلاء

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**المتغيرات البيئية:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### الجلسة 06: موجه النماذج

```bash
cd Workshop/samples/session06
python models_router.py
```

**اختبار منطق التوجيه** مع نوايا متعددة (كود، تلخيص، تصنيف)

### الجلسة 06: خط الأنابيب

```bash
python models_pipeline.py
```

**خط أنابيب متعدد الخطوات معقد** يتضمن التخطيط، التنفيذ، والتحسين

## السكربتات

### تصدير تقرير قياس الأداء

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**الناتج**: جدول Markdown + مقاييس JSON

### فحص أنماط CLI في Markdown

```bash
python lint_markdown_cli.py --verbose
```

**الغرض**: اكتشاف أنماط CLI المهملة في التوثيق

## الاختبارات

### اختبارات الدخان

```bash
cd Workshop
python -m tests.smoke
```

**الاختبارات**: التحقق من الوظائف الأساسية للأمثلة الرئيسية

## استكشاف الأخطاء وإصلاحها

### الخدمة لا تعمل

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### أخطاء استيراد الوحدات

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### أخطاء الاتصال

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### النموذج غير موجود

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## مرجع المتغيرات البيئية

### التكوين الأساسي
| المتغير | الافتراضي | الوصف |
|---------|-----------|-------|
| `FOUNDRY_LOCAL_ALIAS` | يختلف | الاسم المستعار للنموذج المستخدم |
| `FOUNDRY_LOCAL_ENDPOINT` | تلقائي | تجاوز نقطة نهاية الخدمة |
| `SHOW_USAGE` | `0` | عرض إحصائيات استخدام الرموز |
| `RETRY_ON_FAIL` | `1` | تمكين منطق إعادة المحاولة |
| `RETRY_BACKOFF` | `1.0` | تأخير إعادة المحاولة الأولي (بالثواني) |

### خاص بالجلسة
| المتغير | الافتراضي | الوصف |
|---------|-----------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | نموذج التضمين |
| `RAG_QUESTION` | انظر المثال | سؤال اختبار RAG |
| `BENCH_MODELS` | يختلف | النماذج مفصولة بفواصل |
| `BENCH_ROUNDS` | `3` | تكرارات قياس الأداء |
| `BENCH_PROMPT` | انظر المثال | موجه قياس الأداء |
| `BENCH_STREAM` | `0` | قياس تأخير أول رمز |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | النموذج الأساسي للوكيل |
| `AGENT_MODEL_EDITOR` | الأساسي | نموذج وكيل المحرر |
| `SLM_ALIAS` | `phi-4-mini` | نموذج اللغة الصغيرة |
| `LLM_ALIAS` | `qwen2.5-7b` | نموذج اللغة الكبير |
| `COMPARE_PROMPT` | انظر المثال | موجه المقارنة |

## النماذج الموصى بها

### التطوير والاختبار
- **phi-4-mini** - توازن بين الجودة والسرعة
- **qwen2.5-0.5b** - سريع جدًا للتصنيف
- **gemma-2-2b** - جودة جيدة وسرعة معتدلة

### سيناريوهات الإنتاج
- **phi-4-mini** - للأغراض العامة
- **deepseek-coder-1.3b** - لتوليد الأكواد
- **qwen2.5-7b** - استجابات عالية الجودة

## توثيق SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  

## الحصول على المساعدة

1. تحقق من حالة الخدمة: `foundry service status`  
2. عرض السجلات: تحقق من سجلات خدمة Foundry Local  
3. تحقق من توثيق SDK: https://github.com/microsoft/Foundry-Local  
4. مراجعة الكود التجريبي: جميع الأمثلة تحتوي على تعليقات توضيحية مفصلة  

## الخطوات التالية

1. أكمل جميع جلسات الورشة بالترتيب  
2. جرب نماذج مختلفة  
3. قم بتعديل الأمثلة لتناسب حالات الاستخدام الخاصة بك  
4. راجع `SDK_MIGRATION_NOTES.md` للحصول على أنماط متقدمة  

---

**آخر تحديث**: 2025-01-08  
**إصدار الورشة**: الأحدث  
**SDK**: Foundry Local Python SDK  

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.