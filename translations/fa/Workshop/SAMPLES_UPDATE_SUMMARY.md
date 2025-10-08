<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-08T21:56:32+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "fa"
}
-->
# نمونه‌های کارگاه - خلاصه به‌روزرسانی SDK محلی Foundry

## نمای کلی

تمام نمونه‌های پایتون در پوشه `Workshop/samples` به‌روزرسانی شده‌اند تا از بهترین شیوه‌های SDK محلی Foundry پیروی کنند و هماهنگی در سراسر کارگاه تضمین شود.

**تاریخ**: ۸ اکتبر ۲۰۲۵  
**دامنه**: ۹ فایل پایتون در ۶ جلسه کارگاه  
**تمرکز اصلی**: مدیریت خطا، مستندسازی، الگوهای SDK، تجربه کاربری

---

## فایل‌های به‌روزرسانی‌شده

### جلسه ۰۱: شروع کار
- ✅ `chat_bootstrap.py` - مثال‌های پایه‌ای چت و استریم

### جلسه ۰۲: راه‌حل‌های RAG
- ✅ `rag_pipeline.py` - پیاده‌سازی RAG با embeddings
- ✅ `rag_eval_ragas.py` - ارزیابی RAG با معیارهای RAGAS

### جلسه ۰۳: مدل‌های متن‌باز
- ✅ `benchmark_oss_models.py` - ارزیابی چند مدل

### جلسه ۰۴: مدل‌های پیشرفته
- ✅ `model_compare.py` - مقایسه SLM و LLM

### جلسه ۰۵: عوامل هوش مصنوعی
- ✅ `agents_orchestrator.py` - هماهنگی چند عامل

### جلسه ۰۶: مدل‌ها به‌عنوان ابزار
- ✅ `models_router.py` - مسیریابی مدل بر اساس هدف
- ✅ `models_pipeline.py` - خط لوله چند مرحله‌ای مسیریابی‌شده

### زیرساخت پشتیبانی
- ✅ `workshop_utils.py` - قبلاً از بهترین شیوه‌ها پیروی می‌کرد (نیازی به تغییر نبود)

---

## بهبودهای کلیدی

### ۱. مدیریت خطای پیشرفته

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

**مزایا:**
- مدیریت خطای مؤثر با پیام‌های واضح
- نکات قابل اجرا برای رفع مشکلات
- کدهای خروجی مناسب برای اسکریپت‌ها

### ۲. مدیریت بهتر واردات

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

**مزایا:**
- راهنمایی واضح در صورت نبود وابستگی‌ها
- جلوگیری از خطاهای واردات مبهم
- دستورالعمل‌های نصب کاربرپسند

### ۳. مستندسازی جامع

**اضافه‌شده به تمام نمونه‌ها:**
- مستندسازی متغیرهای محیطی در docstrings
- لینک‌های مرجع SDK
- مثال‌های استفاده
- مستندسازی دقیق توابع/پارامترها
- اشاره‌های نوع برای پشتیبانی بهتر از IDE

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

### ۴. بازخورد بهتر کاربر

**اضافه‌شده: گزارش‌گیری اطلاعاتی:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**شاخص‌های پیشرفت:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**خروجی ساختاریافته:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### ۵. ارزیابی قوی

**بهبودهای جلسه ۰۳:**
- مدیریت خطا برای هر مدل (ادامه در صورت شکست)
- گزارش‌دهی دقیق پیشرفت
- اجرای صحیح دورهای گرم‌سازی
- پشتیبانی از اندازه‌گیری تأخیر اولین توکن
- جداسازی واضح مراحل

### ۶. اشاره‌های نوع سازگار

**اضافه‌شده در سراسر:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**مزایا:**
- تکمیل خودکار بهتر در IDE
- تشخیص زودهنگام خطا
- کد خودمستند

### ۷. مسیریاب مدل پیشرفته

**بهبودهای جلسه ۰۶:**
- مستندسازی جامع تشخیص هدف
- توضیح الگوریتم انتخاب مدل
- گزارش‌های مسیریابی دقیق
- قالب‌بندی خروجی تست
- بازیابی خطا در تست دسته‌ای

### ۸. هماهنگی چند عامل

**بهبودهای جلسه ۰۵:**
- گزارش‌دهی پیشرفت مرحله به مرحله
- مدیریت خطا برای هر عامل
- ساختار واضح خط لوله
- مستندسازی بهتر مدیریت حافظه

---

## چک‌لیست تست

### پیش‌نیازها
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### تست هر نمونه

#### جلسه ۰۱
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### جلسه ۰۲
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### جلسه ۰۳
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### جلسه ۰۴
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### جلسه ۰۵
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### جلسه ۰۶
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## مرجع متغیرهای محیطی

### عمومی (تمام نمونه‌ها)
| متغیر | توضیحات | پیش‌فرض |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | نام مستعار مدل برای استفاده | بسته به نمونه |
| `FOUNDRY_LOCAL_ENDPOINT` | جایگزینی نقطه پایانی سرویس | به‌صورت خودکار شناسایی می‌شود |
| `SHOW_USAGE` | نمایش استفاده از توکن | `0` |
| `RETRY_ON_FAIL` | فعال‌سازی منطق تلاش مجدد | `1` |
| `RETRY_BACKOFF` | تأخیر اولیه تلاش مجدد | `1.0` |

### نمونه‌های خاص
| متغیر | استفاده‌شده توسط | توضیحات |
|----------|---------|-------------|
| `EMBED_MODEL` | جلسه ۰۲ | نام مدل embedding |
| `RAG_QUESTION` | جلسه ۰۲ | سوال تست برای RAG |
| `BENCH_MODELS` | جلسه ۰۳ | مدل‌های جداشده با کاما برای ارزیابی |
| `BENCH_ROUNDS` | جلسه ۰۳ | تعداد دورهای ارزیابی |
| `BENCH_PROMPT` | جلسه ۰۳ | درخواست تست برای ارزیابی |
| `BENCH_STREAM` | جلسه ۰۳ | اندازه‌گیری تأخیر اولین توکن |
| `SLM_ALIAS` | جلسه ۰۴ | مدل زبان کوچک |
| `LLM_ALIAS` | جلسه ۰۴ | مدل زبان بزرگ |
| `COMPARE_PROMPT` | جلسه ۰۴ | درخواست تست مقایسه |
| `AGENT_MODEL_PRIMARY` | جلسه ۰۵ | مدل عامل اصلی |
| `AGENT_MODEL_EDITOR` | جلسه ۰۵ | مدل عامل ویرایشگر |
| `AGENT_QUESTION` | جلسه ۰۵ | سوال تست برای عوامل |
| `PIPELINE_TASK` | جلسه ۰۶ | وظیفه برای خط لوله |

---

## تغییرات شکسته

**هیچ** - تمام تغییرات با نسخه‌های قبلی سازگار هستند.

اسکریپت‌های موجود همچنان کار خواهند کرد. ویژگی‌های جدید عبارتند از:
- متغیرهای محیطی اختیاری
- پیام‌های خطای پیشرفته (عملکرد را خراب نمی‌کنند)
- گزارش‌دهی اضافی (قابل سرکوب)
- اشاره‌های نوع بهتر (بدون تأثیر در زمان اجرا)

---

## بهترین شیوه‌های اجراشده

### ۱. همیشه از Workshop Utils استفاده کنید
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### ۲. الگوی مدیریت خطای مناسب
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### ۳. گزارش‌دهی اطلاعاتی
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### ۴. اشاره‌های نوع
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### ۵. Docstrings جامع
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

### ۶. پشتیبانی از متغیرهای محیطی
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### ۷. کاهش مؤثر
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

## مشکلات رایج و راه‌حل‌ها

### مشکل: خطاهای واردات
**راه‌حل:** نصب وابستگی‌های گم‌شده
```bash
pip install sentence-transformers ragas datasets numpy
```

### مشکل: خطاهای اتصال
**راه‌حل:** اطمینان حاصل کنید که Foundry Local در حال اجرا است
```bash
foundry service status
foundry model run phi-4-mini
```

### مشکل: مدل پیدا نشد
**راه‌حل:** مدل‌های موجود را بررسی کنید
```bash
foundry model ls
foundry model download <alias>
```

### مشکل: عملکرد کند
**راه‌حل:** از مدل‌های کوچک‌تر استفاده کنید یا پارامترها را تنظیم کنید
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## مراحل بعدی

### ۱. تست تمام نمونه‌ها
چک‌لیست تست بالا را اجرا کنید تا مطمئن شوید تمام نمونه‌ها به‌درستی کار می‌کنند.

### ۲. به‌روزرسانی مستندات
- فایل‌های markdown جلسه را با مثال‌های جدید به‌روزرسانی کنید
- بخش رفع مشکلات را به README اصلی اضافه کنید
- راهنمای مرجع سریع ایجاد کنید

### ۳. ایجاد تست‌های یکپارچه‌سازی
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### ۴. اضافه کردن ارزیابی عملکرد
بهبودهای عملکرد ناشی از بهبود مدیریت خطا را پیگیری کنید.

### ۵. بازخورد کاربر
بازخورد شرکت‌کنندگان کارگاه را جمع‌آوری کنید درباره:
- وضوح پیام‌های خطا
- کامل بودن مستندات
- سهولت استفاده

---

## منابع

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **مرجع سریع**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **یادداشت‌های مهاجرت**: `Workshop/SDK_MIGRATION_NOTES.md`
- **مخزن اصلی**: https://github.com/microsoft/Foundry-Local

---

## نگهداری

### اضافه کردن نمونه‌های جدید
هنگام ایجاد نمونه‌های جدید، از این الگوها پیروی کنید:

1. از `workshop_utils` برای مدیریت کلاینت استفاده کنید
2. مدیریت خطای جامع اضافه کنید
3. پشتیبانی از متغیرهای محیطی اضافه کنید
4. اشاره‌های نوع و docstrings اضافه کنید
5. گزارش‌دهی اطلاعاتی ارائه دهید
6. مثال‌های استفاده را در docstring اضافه کنید
7. لینک به مستندات SDK اضافه کنید

### بررسی به‌روزرسانی‌ها
هنگام بررسی به‌روزرسانی نمونه‌ها، بررسی کنید:
- [ ] مدیریت خطا در تمام عملیات I/O
- [ ] اشاره‌های نوع در توابع عمومی
- [ ] Docstrings جامع
- [ ] مستندسازی متغیرهای محیطی
- [ ] بازخورد اطلاعاتی کاربر
- [ ] لینک‌های مرجع SDK
- [ ] سبک کد سازگار

---

**خلاصه**: تمام نمونه‌های پایتون کارگاه اکنون از بهترین شیوه‌های SDK محلی Foundry پیروی می‌کنند با مدیریت خطای پیشرفته، مستندسازی جامع، و تجربه کاربری بهبود‌یافته. هیچ تغییر شکسته‌ای وجود ندارد - تمام عملکردهای موجود حفظ و بهبود یافته‌اند.

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.