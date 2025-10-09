<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T07:00:49+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "ur"
}
-->
# ورکشاپ سیمپلز - فاؤنڈری لوکل SDK اپڈیٹ کا خلاصہ

## جائزہ

`Workshop/samples` ڈائریکٹری میں موجود تمام Python سیمپلز کو فاؤنڈری لوکل SDK کی بہترین پریکٹسز کے مطابق اپڈیٹ کیا گیا ہے تاکہ ورکشاپ میں مستقل مزاجی کو یقینی بنایا جا سکے۔

**تاریخ**: 8 اکتوبر، 2025  
**دائرہ کار**: 6 ورکشاپ سیشنز میں 9 Python فائلز  
**اہم توجہ**: ایرر ہینڈلنگ، دستاویزات، SDK پیٹرنز، صارف کے تجربے میں بہتری

---

## اپڈیٹ شدہ فائلز

### سیشن 01: شروعات
- ✅ `chat_bootstrap.py` - بنیادی چیٹ اور اسٹریمنگ کی مثالیں

### سیشن 02: RAG سلوشنز
- ✅ `rag_pipeline.py` - ایمبیڈنگ کے ساتھ RAG کا نفاذ
- ✅ `rag_eval_ragas.py` - RAGAS میٹرکس کے ساتھ RAG کی تشخیص

### سیشن 03: اوپن سورس ماڈلز
- ✅ `benchmark_oss_models.py` - ملٹی ماڈل بینچ مارکنگ

### سیشن 04: جدید ماڈلز
- ✅ `model_compare.py` - SLM بمقابلہ LLM کا موازنہ

### سیشن 05: AI سے چلنے والے ایجنٹس
- ✅ `agents_orchestrator.py` - ملٹی ایجنٹ کوآرڈینیشن

### سیشن 06: ماڈلز بطور ٹولز
- ✅ `models_router.py` - انٹینٹ پر مبنی ماڈل روٹنگ
- ✅ `models_pipeline.py` - ملٹی اسٹیپ روٹڈ پائپ لائن

### معاون انفراسٹرکچر
- ✅ `workshop_utils.py` - پہلے ہی بہترین پریکٹسز پر عمل کر رہا ہے (کوئی تبدیلی نہیں کی گئی)

---

## اہم بہتریاں

### 1. بہتر ایرر ہینڈلنگ

**پہلے:**
```python
manager, client, model_id = get_client(alias)
```

**بعد میں:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**فوائد:**
- واضح ایرر میسجز کے ساتھ شائستہ ایرر ہینڈلنگ
- قابل عمل ٹربل شوٹنگ ہدایات
- اسکرپٹنگ کے لیے مناسب ایگزٹ کوڈز

### 2. بہتر امپورٹ مینجمنٹ

**پہلے:**
```python
from sentence_transformers import SentenceTransformer
```

**بعد میں:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**فوائد:**
- جب ڈیپینڈنسیز غائب ہوں تو واضح رہنمائی
- مبہم امپورٹ ایررز کو روکنا
- صارف دوست انسٹالیشن ہدایات

### 3. جامع دستاویزات

**تمام سیمپلز میں شامل کیا گیا:**
- ڈوک اسٹرنگز میں ماحول کے متغیرات کی دستاویزات
- SDK حوالہ جات کے لنکس
- استعمال کی مثالیں
- تفصیلی فنکشن/پیرامیٹر دستاویزات
- بہتر IDE سپورٹ کے لیے ٹائپ ہنٹس

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

### 4. بہتر صارف کی رائے

**معلوماتی لاگنگ شامل کی گئی:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**پروگریس انڈیکیٹرز:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**منظم آؤٹ پٹ:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. مضبوط بینچ مارکنگ

**سیشن 03 میں بہتریاں:**
- ہر ماڈل کے لیے ایرر ہینڈلنگ (ناکامی پر جاری رہتا ہے)
- تفصیلی پروگریس رپورٹنگ
- وارم اپ راؤنڈز کو مناسب طریقے سے انجام دیا گیا
- فرسٹ ٹوکن لیٹنسی پیمائش کی حمایت
- مراحل کی واضح علیحدگی

### 6. مستقل ٹائپ ہنٹس

**ہر جگہ شامل کیا گیا:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**فوائد:**
- بہتر IDE آٹو کمپلیٹ
- ابتدائی ایرر کا پتہ لگانا
- خود وضاحتی کوڈ

### 7. بہتر ماڈل روٹر

**سیشن 06 میں بہتریاں:**
- انٹینٹ ڈیٹیکشن کی جامع دستاویزات
- ماڈل سلیکشن الگورتھم کی وضاحت
- تفصیلی روٹنگ لاگز
- ٹیسٹ آؤٹ پٹ فارمیٹنگ
- بیچ ٹیسٹنگ میں ایرر ریکوری

### 8. ملٹی ایجنٹ آرکسٹریشن

**سیشن 05 میں بہتریاں:**
- مرحلہ وار پروگریس رپورٹنگ
- ہر ایجنٹ کے لیے ایرر ہینڈلنگ
- واضح پائپ لائن اسٹرکچر
- بہتر میموری مینجمنٹ دستاویزات

---

## ٹیسٹنگ چیک لسٹ

### ضروریات
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### ہر سیمپل کو ٹیسٹ کریں

#### سیشن 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### سیشن 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### سیشن 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### سیشن 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### سیشن 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### سیشن 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## ماحول کے متغیرات کا حوالہ

### عالمی (تمام سیمپلز)
| متغیر | وضاحت | ڈیفالٹ |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | استعمال کرنے کے لیے ماڈل کا عرف | سیمپل کے لحاظ سے مختلف |
| `FOUNDRY_LOCAL_ENDPOINT` | سروس اینڈ پوائنٹ کو اووررائیڈ کریں | خودکار طور پر پتہ لگایا گیا |
| `SHOW_USAGE` | ٹوکن کے استعمال کو دکھائیں | `0` |
| `RETRY_ON_FAIL` | ریٹری لاجک کو فعال کریں | `1` |
| `RETRY_BACKOFF` | ابتدائی ریٹری تاخیر | `1.0` |

### سیمپل کے لحاظ سے مخصوص
| متغیر | استعمال شدہ | وضاحت |
|----------|---------|-------------|
| `EMBED_MODEL` | سیشن 02 | ایمبیڈنگ ماڈل کا نام |
| `RAG_QUESTION` | سیشن 02 | RAG کے لیے ٹیسٹ سوال |
| `BENCH_MODELS` | سیشن 03 | بینچ مارک کرنے کے لیے کاما سے جدا ماڈلز |
| `BENCH_ROUNDS` | سیشن 03 | بینچ مارک راؤنڈز کی تعداد |
| `BENCH_PROMPT` | سیشن 03 | بینچ مارکس کے لیے ٹیسٹ پرامپٹ |
| `BENCH_STREAM` | سیشن 03 | فرسٹ ٹوکن لیٹنسی کی پیمائش کریں |
| `SLM_ALIAS` | سیشن 04 | چھوٹا لینگویج ماڈل |
| `LLM_ALIAS` | سیشن 04 | بڑا لینگویج ماڈل |
| `COMPARE_PROMPT` | سیشن 04 | موازنہ ٹیسٹ پرامپٹ |
| `AGENT_MODEL_PRIMARY` | سیشن 05 | پرائمری ایجنٹ ماڈل |
| `AGENT_MODEL_EDITOR` | سیشن 05 | ایڈیٹر ایجنٹ ماڈل |
| `AGENT_QUESTION` | سیشن 05 | ایجنٹس کے لیے ٹیسٹ سوال |
| `PIPELINE_TASK` | سیشن 06 | پائپ لائن کے لیے ٹاسک |

---

## بریکنگ تبدیلیاں

**کوئی نہیں** - تمام تبدیلیاں پچھلے ورژن کے ساتھ مطابقت رکھتی ہیں۔

موجودہ اسکرپٹس کام کرتے رہیں گے۔ نئی خصوصیات:
- اختیاری ماحول کے متغیرات
- بہتر ایرر میسجز (فنکشنلٹی کو متاثر نہیں کرتے)
- اضافی لاگنگ (دبایا جا سکتا ہے)
- بہتر ٹائپ ہنٹس (رن ٹائم پر اثر نہیں)

---

## نافذ کردہ بہترین پریکٹسز

### 1. ہمیشہ ورکشاپ Utils استعمال کریں
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. مناسب ایرر ہینڈلنگ پیٹرن
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. معلوماتی لاگنگ
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. ٹائپ ہنٹس
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. جامع ڈوک اسٹرنگز
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

### 6. ماحول کے متغیرات کی حمایت
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. شائستہ تنزلی
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

## عام مسائل اور حل

### مسئلہ: امپورٹ ایررز
**حل:** غائب ڈیپینڈنسیز انسٹال کریں
```bash
pip install sentence-transformers ragas datasets numpy
```

### مسئلہ: کنکشن ایررز
**حل:** یقینی بنائیں کہ فاؤنڈری لوکل چل رہا ہے
```bash
foundry service status
foundry model run phi-4-mini
```

### مسئلہ: ماڈل نہیں ملا
**حل:** دستیاب ماڈلز چیک کریں
```bash
foundry model ls
foundry model download <alias>
```

### مسئلہ: سست کارکردگی
**حل:** چھوٹے ماڈلز استعمال کریں یا پیرامیٹرز کو ایڈجسٹ کریں
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## اگلے اقدامات

### 1. تمام سیمپلز کو ٹیسٹ کریں
اوپر دی گئی ٹیسٹنگ چیک لسٹ کے ذریعے تمام سیمپلز کی درستگی کو یقینی بنائیں۔

### 2. دستاویزات کو اپڈیٹ کریں
- سیشن مارک ڈاؤن فائلز کو نئے مثالوں کے ساتھ اپڈیٹ کریں
- مین README میں ٹربل شوٹنگ سیکشن شامل کریں
- فوری حوالہ گائیڈ بنائیں

### 3. انٹیگریشن ٹیسٹس بنائیں
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. کارکردگی کے بینچ مارکس شامل کریں
ایرر ہینڈلنگ میں بہتری سے حاصل ہونے والی کارکردگی کو ٹریک کریں۔

### 5. صارف کی رائے
ورکشاپ کے شرکاء سے درج ذیل پر رائے جمع کریں:
- ایرر میسجز کی وضاحت
- دستاویزات کی مکملیت
- استعمال میں آسانی

---

## وسائل

- **فاؤنڈری لوکل SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **فوری حوالہ**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **مائیگریشن نوٹس**: `Workshop/SDK_MIGRATION_NOTES.md`
- **مین ریپوزٹری**: https://github.com/microsoft/Foundry-Local

---

## دیکھ بھال

### نئے سیمپلز شامل کرنا
نئے سیمپلز بناتے وقت ان پیٹرنز پر عمل کریں:

1. کلائنٹ مینجمنٹ کے لیے `workshop_utils` استعمال کریں
2. جامع ایرر ہینڈلنگ شامل کریں
3. ماحول کے متغیرات کی حمایت شامل کریں
4. ٹائپ ہنٹس اور ڈوک اسٹرنگز شامل کریں
5. معلوماتی لاگنگ فراہم کریں
6. ڈوک اسٹرنگ میں استعمال کی مثالیں شامل کریں
7. SDK دستاویزات کے لنکس شامل کریں

### اپڈیٹس کا جائزہ لینا
سیمپلز اپڈیٹس کا جائزہ لیتے وقت چیک کریں:
- [ ] تمام I/O آپریشنز پر ایرر ہینڈلنگ
- [ ] پبلک فنکشنز پر ٹائپ ہنٹس
- [ ] جامع ڈوک اسٹرنگز
- [ ] ماحول کے متغیرات کی دستاویزات
- [ ] معلوماتی صارف کی رائے
- [ ] SDK حوالہ جات کے لنکس
- [ ] مستقل کوڈ اسٹائل

---

**خلاصہ**: تمام ورکشاپ Python سیمپلز اب فاؤنڈری لوکل SDK کی بہترین پریکٹسز پر عمل کرتے ہیں، جن میں بہتر ایرر ہینڈلنگ، جامع دستاویزات، اور بہتر صارف تجربہ شامل ہے۔ کوئی بریکنگ تبدیلیاں نہیں - تمام موجودہ فنکشنلٹی محفوظ اور بہتر کی گئی ہے۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔