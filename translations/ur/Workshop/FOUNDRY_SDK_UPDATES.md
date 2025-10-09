<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T06:40:12+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "ur"
}
-->
# فاؤنڈری لوکل SDK اپ ڈیٹس

## جائزہ

ورکشاپ نوٹ بکس اور یوٹیلیٹیز کو اپ ڈیٹ کیا گیا تاکہ **فاؤنڈری لوکل پائتھون SDK** کے آفیشل پیٹرنز کو صحیح طریقے سے استعمال کیا جا سکے:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## تبدیل شدہ فائلیں

### 1. `Workshop/samples/workshop_utils.py`

**تبدیلیاں:**
- ✅ `foundry-local-sdk` پیکج کے لیے امپورٹ ایرر ہینڈلنگ شامل کی گئی
- ✅ آفیشل SDK پیٹرنز کے ساتھ دستاویزات کو بہتر بنایا گیا
- ✅ یونیکوڈ سمبلز (✓, ✗, ⚠) کے ساتھ لاگنگ کو بہتر بنایا گیا
- ✅ مثالوں کے ساتھ جامع ڈاکسٹرنگز شامل کی گئیں
- ✅ CLI کمانڈز کے حوالے سے بہتر ایرر میسیجز شامل کیے گئے
- ✅ آفیشل SDK دستاویزات کے مطابق کمنٹس کو اپ ڈیٹ کیا گیا

**اہم بہتریاں:**

#### امپورٹ ایرر ہینڈلنگ
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### بہتر `get_client()` فنکشن
- SDK انیشیالائزیشن پیٹرن کے بارے میں تفصیلی دستاویزات شامل کی گئیں
- وضاحت کی گئی کہ `FoundryLocalManager` خودکار طور پر سروس شروع کرتا ہے
- ماڈل الیاس ریزولوشن کو ہارڈویئر-آپٹمائزڈ ویریئنٹس میں واضح کیا گیا
- اینڈ پوائنٹ معلومات کے ساتھ لاگنگ کو بہتر بنایا گیا
- ٹربل شوٹنگ کے اقدامات تجویز کرنے والے بہتر ایرر میسیجز شامل کیے گئے

#### بہتر `chat_once()` فنکشن
- استعمال کی مثالوں کے ساتھ جامع ڈاکسٹرنگ شامل کی گئی
- OpenAI SDK مطابقت کو واضح کیا گیا
- اسٹریمنگ سپورٹ کو دستاویز کیا گیا (kwargs کے ذریعے)
- CLI کمانڈ تجاویز کے ساتھ بہتر ایرر میسیجز شامل کیے گئے
- ماڈل دستیابی چیک کرنے کے نوٹس شامل کیے گئے

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**تبدیلیاں:**
- ✅ تمام مارک ڈاؤن سیلز کو SDK حوالہ جات کے ساتھ اپ ڈیٹ کیا گیا
- ✅ کوڈ کمنٹس کو SDK پیٹرنز کی وضاحت کے ساتھ بہتر بنایا گیا
- ✅ سیل دستاویزات اور وضاحتوں کو بہتر بنایا گیا
- ✅ ٹربل شوٹنگ گائیڈنس شامل کی گئی
- ✅ ماڈل کیٹلاگ کو اپ ڈیٹ کیا گیا (گپٹ-او ایس ایس-20بی کو 'phi-3.5-mini' سے تبدیل کیا گیا)
- ✅ بصری اشاروں کے ساتھ آؤٹ پٹ فارمیٹنگ کو بہتر بنایا گیا
- ✅ SDK لنکس اور حوالہ جات پورے میں شامل کیے گئے

**سیل بہ سیل اپ ڈیٹس:**

#### سیل 1 (عنوان)
- SDK دستاویزات کے لنکس شامل کیے گئے
- آفیشل GitHub ریپوزیٹریز کا حوالہ دیا گیا

#### سیل 2 (منظر نامہ)
- نمبر شدہ مراحل کے ساتھ دوبارہ فارمیٹ کیا گیا
- ارادے پر مبنی روٹنگ پیٹرن کو واضح کیا گیا
- مقامی عملدرآمد کے فوائد پر زور دیا گیا

#### سیل 3 (ڈپینڈنسی انسٹالیشن)
- ہر پیکج کیا فراہم کرتا ہے اس کی وضاحت شامل کی گئی
- SDK صلاحیتوں کو دستاویز کیا گیا (الیاس ریزولوشن، ہارڈویئر آپٹمائزیشن)

#### سیل 4 (ماحول کی ترتیب)
- فنکشن ڈاکسٹرنگز کو بہتر بنایا گیا
- SDK پیٹرنز کی وضاحت کرنے والے ان لائن کمنٹس شامل کیے گئے
- ماڈل کیٹلاگ کی ساخت کو دستاویز کیا گیا
- ترجیح/صلاحیت کے ملاپ کو واضح کیا گیا

#### سیل 5 (کیٹلاگ چیک)
- بصری چیک مارکس (✓) شامل کیے گئے
- آؤٹ پٹ کو بہتر فارمیٹ کیا گیا

#### سیل 6 (ارادے کا پتہ لگانے کا ٹیسٹ)
- آؤٹ پٹ کو ٹیبل اسٹائل کے طور پر دوبارہ فارمیٹ کیا گیا
- ارادے اور منتخب ماڈل دونوں کو دکھاتا ہے

#### سیل 7 (روٹنگ فنکشن)
- جامع SDK پیٹرن وضاحت
- انیشیالائزیشن فلو کو دستاویز کیا گیا
- تمام خصوصیات کی فہرست دی گئی (ریٹری، ٹریکنگ، ایررز)
- SDK حوالہ لنک شامل کیا گیا

#### سیل 8 (بیچ ڈیمو)
- کیا توقع کی جائے اس کی وضاحت کو بہتر بنایا گیا
- ٹربل شوٹنگ سیکشن شامل کیا گیا
- ڈیبگنگ کے لیے CLI کمانڈز شامل کیے گئے
- آؤٹ پٹ ڈسپلے فارمیٹنگ کو بہتر بنایا گیا

### 3. `Workshop/notebooks/session06_README.md` (نئی فائل)

**جامع دستاویزات تخلیق کی گئی جس میں شامل ہیں:**

1. **جائزہ**: آرکیٹیکچر ڈایاگرام اور اجزاء کی وضاحت
2. **SDK انضمام**: آفیشل پیٹرنز کے مطابق کوڈ کی مثالیں
3. **پیشگی شرائط**: سیٹ اپ کے مرحلہ وار ہدایات
4. **استعمال**: نوٹ بک کو چلانے اور حسب ضرورت بنانے کا طریقہ
5. **ماڈل الیاسز**: ہارڈویئر-آپٹمائزڈ ویریئنٹس کی وضاحت
6. **ٹربل شوٹنگ**: عام مسائل اور ان کے حل
7. **توسیع**: ارادے، ماڈلز، اور حسب ضرورت منطق شامل کرنے کا طریقہ
8. **کارکردگی کے نکات**: پروڈکشن کے لیے بہترین طریقے
9. **وسائل**: آفیشل دستاویزات اور کمیونٹی کے لنکس

## SDK پیٹرن کا نفاذ

### آفیشل پیٹرن (فاؤنڈری لوکل دستاویزات سے)

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

### ہمارا نفاذ (workshop_utils میں)

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

**ہمارے طریقہ کار کے فوائد:**
- ✅ آفیشل SDK پیٹرن کی بالکل پیروی کرتا ہے
- ✅ بار بار انیشیالائزیشن سے بچنے کے لیے کیشنگ شامل کرتا ہے
- ✅ پروڈکشن مضبوطی کے لیے ریٹری لاجک شامل کرتا ہے
- ✅ ٹوکن استعمال کی ٹریکنگ کو سپورٹ کرتا ہے
- ✅ بہتر ایرر میسیجز فراہم کرتا ہے
- ✅ آفیشل مثالوں کے ساتھ مطابقت رکھتا ہے

## ماڈل کیٹلاگ میں تبدیلیاں

### پہلے
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### بعد میں
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**وجہ:** 'gpt-oss-20b' (غیر معیاری الیاس) کو 'phi-3.5-mini' (آفیشل فاؤنڈری لوکل الیاس) سے تبدیل کیا گیا۔

## ڈپینڈنسیز

### اپ ڈیٹ شدہ requirements.txt

ورکشاپ requirements.txt پہلے ہی شامل کرتا ہے:
```
foundry-local-sdk
openai>=1.30.0
```

یہی وہ پیکجز ہیں جو فاؤنڈری لوکل انضمام کے لیے ضروری ہیں۔

## اپ ڈیٹس کی جانچ

### 1. تصدیق کریں کہ فاؤنڈری لوکل چل رہا ہے

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. دستیاب ماڈلز چیک کریں

```bash
foundry model ls
```

یقینی بنائیں کہ یہ ماڈلز دستیاب ہیں یا خودکار طور پر ڈاؤن لوڈ ہوں گے:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. نوٹ بک چلائیں

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

یا VS کوڈ میں کھولیں اور تمام سیلز چلائیں۔

### 4. متوقع رویہ

**سیل 1 (انسٹال):** کامیابی سے پیکجز انسٹال کرتا ہے  
**سیل 2 (سیٹ اپ):** کوئی ایرر نہیں، امپورٹس کام کرتے ہیں  
**سیل 3 (تصدیق):** ماڈل لسٹ کے ساتھ ✓ دکھاتا ہے  
**سیل 4 (ارادے کا ٹیسٹ):** ارادے کا پتہ لگانے کے نتائج دکھاتا ہے  
**سیل 5 (روٹر):** ✓ روٹ فنکشن تیار دکھاتا ہے  
**سیل 6 (عملدرآمد):** پرامپٹس کو ماڈلز پر روٹ کرتا ہے، نتائج دکھاتا ہے  

### 5. کنکشن ایررز کی ٹربل شوٹنگ

اگر آپ کو `APIConnectionError: Connection error` نظر آئے:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## ماحول کے متغیرات

درج ذیل ماحول کے متغیرات سپورٹ کیے گئے ہیں:

| متغیر | ڈیفالٹ | وضاحت |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | ٹوکن استعمال پرنٹ کرنے کے لیے `1` پر سیٹ کریں |
| `RETRY_ON_FAIL` | `1` | ریٹری لاجک کو فعال کریں |
| `RETRY_BACKOFF` | `1.0` | ابتدائی ریٹری تاخیر (سیکنڈز) |
| `FOUNDRY_LOCAL_ENDPOINT` | خودکار | سروس اینڈ پوائنٹ کو اووررائیڈ کریں |

### استعمال کی مثالیں

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## پرانے پیٹرن سے منتقلی

اگر آپ کے پاس موجودہ کوڈ ہے جو براہ راست API کالز استعمال کرتا ہے، تو یہاں منتقلی کا طریقہ ہے:

### پہلے (براہ راست API)
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

### بعد میں (SDK)
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

### منتقلی کے فوائد
- ✅ خودکار سروس مینجمنٹ
- ✅ ماڈل الیاس ریزولوشن
- ✅ ہارڈویئر آپٹمائزیشن کا انتخاب
- ✅ بہتر ایرر ہینڈلنگ
- ✅ OpenAI SDK مطابقت
- ✅ اسٹریمنگ سپورٹ

## حوالہ جات

### آفیشل دستاویزات
- **فاؤنڈری لوکل GitHub**: https://github.com/microsoft/Foundry-Local
- **پائتھون SDK سورس**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI حوالہ**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **ٹربل شوٹنگ**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### ورکشاپ وسائل
- **سیشن 06 README**: `Workshop/notebooks/session06_README.md`
- **ورکشاپ یوٹیلیٹیز**: `Workshop/samples/workshop_utils.py`
- **نمونہ نوٹ بک**: `Workshop/notebooks/session06_models_router.ipynb`

### کمیونٹی
- **ڈسکارڈ**: https://aka.ms/foundry-local-discord
- **GitHub مسائل**: https://github.com/microsoft/Foundry-Local/issues

## اگلے اقدامات

1. **تبدیلیوں کا جائزہ لیں**: اپ ڈیٹ شدہ فائلوں کو پڑھیں  
2. **نوٹ بک ٹیسٹ کریں**: session06_models_router.ipynb چلائیں  
3. **SDK کی تصدیق کریں**: یقینی بنائیں کہ foundry-local-sdk انسٹال ہے  
4. **سروس چیک کریں**: تصدیق کریں کہ فاؤنڈری لوکل چل رہا ہے  
5. **دستاویزات دریافت کریں**: نئی session06_README.md پڑھیں  

## خلاصہ

یہ اپ ڈیٹس یقینی بناتی ہیں کہ ورکشاپ مواد **آفیشل فاؤنڈری لوکل SDK پیٹرنز** کی بالکل پیروی کرتا ہے جیسا کہ GitHub ریپوزیٹری میں دستاویز کیا گیا ہے۔ تمام کوڈ کی مثالیں، دستاویزات، اور یوٹیلیٹیز اب مائیکروسافٹ کے مقامی AI ماڈل ڈیپلائمنٹ کے لیے تجویز کردہ بہترین طریقوں کے مطابق ہیں۔

تبدیلیاں بہتر کرتی ہیں:
- ✅ **درستگی**: آفیشل SDK پیٹرنز استعمال کرتا ہے  
- ✅ **دستاویزات**: جامع وضاحتیں اور مثالیں  
- ✅ **ایرر ہینڈلنگ**: بہتر میسیجز اور ٹربل شوٹنگ گائیڈنس  
- ✅ **قابل دیکھ بھال**: آفیشل کنونشنز کی پیروی کرتا ہے  
- ✅ **صارف کا تجربہ**: واضح ہدایات اور ڈیبگنگ مدد  

---

**اپ ڈیٹ شدہ:** 8 اکتوبر، 2025  
**SDK ورژن:** foundry-local-sdk (تازہ ترین)  
**ورکشاپ برانچ:** ری ایکٹر

---

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔