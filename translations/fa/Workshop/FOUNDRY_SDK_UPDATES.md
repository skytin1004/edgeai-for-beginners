<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T21:36:35+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "fa"
}
-->
# به‌روزرسانی‌های SDK محلی Foundry

## نمای کلی

دفترچه‌های Workshop و ابزارهای کمکی به‌روزرسانی شده‌اند تا به‌درستی از **SDK رسمی پایتون Foundry Local** استفاده کنند، مطابق با الگوهای زیر:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## فایل‌های تغییر یافته

### 1. `Workshop/samples/workshop_utils.py`

**تغییرات:**
- ✅ اضافه کردن مدیریت خطا برای وارد کردن بسته `foundry-local-sdk`
- ✅ بهبود مستندسازی با الگوهای رسمی SDK
- ✅ ارتقای لاگ‌گذاری با نمادهای یونیکد (✓، ✗، ⚠)
- ✅ اضافه کردن توضیحات جامع با مثال‌ها
- ✅ پیام‌های خطای بهتر با ارجاع به دستورات CLI
- ✅ به‌روزرسانی نظرات برای تطابق با مستندات رسمی SDK

**بهبودهای کلیدی:**

#### مدیریت خطای وارد کردن
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### بهبود تابع `get_client()`
- اضافه کردن مستندسازی دقیق درباره الگوی اولیه‌سازی SDK
- توضیح اینکه `FoundryLocalManager` سرویس را به‌طور خودکار راه‌اندازی می‌کند
- توضیح حل نام مستعار مدل به نسخه‌های بهینه‌شده سخت‌افزاری
- ارتقای لاگ‌گذاری با اطلاعات نقطه پایانی
- پیام‌های خطای بهتر با پیشنهاد مراحل عیب‌یابی

#### بهبود تابع `chat_once()`
- اضافه کردن توضیحات جامع با مثال‌های استفاده
- توضیح سازگاری با SDK OpenAI
- مستندسازی پشتیبانی از جریان (از طریق kwargs)
- پیام‌های خطای بهتر با پیشنهاد دستورات CLI
- اضافه کردن نکات درباره بررسی دسترسی مدل‌ها

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**تغییرات:**
- ✅ به‌روزرسانی تمام سلول‌های مارک‌داون با ارجاعات SDK
- ✅ بهبود نظرات کد با توضیحات الگوهای SDK
- ✅ ارتقای مستندسازی سلول‌ها و توضیحات
- ✅ اضافه کردن راهنمایی‌های عیب‌یابی
- ✅ به‌روزرسانی کاتالوگ مدل (جایگزینی 'gpt-oss-20b' با 'phi-3.5-mini')
- ✅ قالب‌بندی بهتر خروجی با نشانگرهای بصری
- ✅ اضافه کردن لینک‌ها و ارجاعات SDK در سراسر

**به‌روزرسانی‌های سلول به سلول:**

#### سلول 1 (عنوان)
- اضافه کردن لینک‌های مستندات SDK
- ارجاع به مخازن رسمی GitHub

#### سلول 2 (سناریو)
- قالب‌بندی مجدد با مراحل شماره‌گذاری شده
- توضیح الگوی مسیریابی مبتنی بر قصد
- تأکید بر مزایای اجرای محلی

#### سلول 3 (نصب وابستگی‌ها)
- اضافه کردن توضیح درباره اینکه هر بسته چه چیزی ارائه می‌دهد
- مستندسازی قابلیت‌های SDK (حل نام مستعار، بهینه‌سازی سخت‌افزاری)

#### سلول 4 (تنظیم محیط)
- ارتقای توضیحات توابع
- اضافه کردن نظرات داخلی برای توضیح الگوهای SDK
- مستندسازی ساختار کاتالوگ مدل
- توضیح تطابق اولویت/قابلیت

#### سلول 5 (بررسی کاتالوگ)
- اضافه کردن علامت‌های چک (✓)
- قالب‌بندی بهتر خروجی

#### سلول 6 (آزمون تشخیص قصد)
- قالب‌بندی خروجی به سبک جدول
- نمایش هر دو قصد و مدل انتخاب‌شده

#### سلول 7 (تابع مسیریابی)
- توضیح جامع الگوی SDK
- مستندسازی جریان اولیه‌سازی
- فهرست کردن تمام ویژگی‌ها (تلاش مجدد، ردیابی، خطاها)
- اضافه کردن لینک ارجاع SDK

#### سلول 8 (دموی دسته‌ای)
- توضیح بهتر درباره انتظارات
- اضافه کردن بخش عیب‌یابی
- شامل دستورات CLI برای اشکال‌زدایی
- قالب‌بندی بهتر نمایش خروجی

### 3. `Workshop/notebooks/session06_README.md` (فایل جدید)

**ایجاد مستندسازی جامع شامل:**

1. **نمای کلی**: نمودار معماری و توضیح اجزا
2. **یکپارچه‌سازی SDK**: مثال‌های کد مطابق با الگوهای رسمی
3. **پیش‌نیازها**: دستورالعمل‌های تنظیم مرحله‌به‌مرحله
4. **استفاده**: نحوه اجرا و سفارشی‌سازی دفترچه
5. **نام مستعار مدل‌ها**: توضیح نسخه‌های بهینه‌شده سخت‌افزاری
6. **عیب‌یابی**: مشکلات رایج و راه‌حل‌ها
7. **گسترش**: نحوه اضافه کردن قصدها، مدل‌ها و منطق سفارشی
8. **نکات عملکردی**: بهترین شیوه‌ها برای استفاده در تولید
9. **منابع**: لینک به مستندات رسمی و جامعه

## پیاده‌سازی الگوی SDK

### الگوی رسمی (از مستندات Foundry Local)

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

### پیاده‌سازی ما (در workshop_utils)

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

**مزایای رویکرد ما:**
- ✅ دقیقاً مطابق با الگوی رسمی SDK
- ✅ اضافه کردن کش برای جلوگیری از اولیه‌سازی‌های مکرر
- ✅ شامل منطق تلاش مجدد برای استحکام تولید
- ✅ پشتیبانی از ردیابی استفاده از توکن
- ✅ پیام‌های خطای بهتر
- ✅ سازگاری با مثال‌های رسمی

## تغییرات کاتالوگ مدل

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

**دلیل:** جایگزینی 'gpt-oss-20b' (نام مستعار غیر استاندارد) با 'phi-3.5-mini' (نام مستعار رسمی Foundry Local).

## وابستگی‌ها

### به‌روزرسانی requirements.txt

فایل requirements.txt در Workshop شامل موارد زیر است:
```
foundry-local-sdk
openai>=1.30.0
```

این‌ها تنها بسته‌های مورد نیاز برای یکپارچه‌سازی Foundry Local هستند.

## آزمایش به‌روزرسانی‌ها

### 1. تأیید اجرای Foundry Local

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. بررسی مدل‌های موجود

```bash
foundry model ls
```

اطمینان حاصل کنید که این مدل‌ها موجود هستند یا به‌طور خودکار دانلود می‌شوند:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. اجرای دفترچه

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

یا در VS Code باز کنید و تمام سلول‌ها را اجرا کنید.

### 4. رفتار مورد انتظار

**سلول 1 (نصب):** بسته‌ها با موفقیت نصب می‌شوند  
**سلول 2 (تنظیم):** بدون خطا، واردات کار می‌کند  
**سلول 3 (تأیید):** نمایش ✓ با لیست مدل‌ها  
**سلول 4 (آزمون قصد):** نمایش نتایج تشخیص قصد  
**سلول 5 (مسیریاب):** نمایش ✓ تابع مسیریابی آماده  
**سلول 6 (اجرا):** مسیریابی درخواست‌ها به مدل‌ها، نمایش نتایج  

### 5. عیب‌یابی خطاهای اتصال

اگر خطای `APIConnectionError: Connection error` را مشاهده کردید:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## متغیرهای محیطی

متغیرهای محیطی زیر پشتیبانی می‌شوند:

| متغیر | پیش‌فرض | توضیح |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | برای چاپ استفاده از توکن به `1` تنظیم کنید |
| `RETRY_ON_FAIL` | `1` | فعال کردن منطق تلاش مجدد |
| `RETRY_BACKOFF` | `1.0` | تأخیر اولیه تلاش مجدد (ثانیه) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | بازنویسی نقطه پایانی سرویس |

### مثال‌های استفاده

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## مهاجرت از الگوی قدیمی

اگر کدی دارید که از تماس‌های مستقیم API استفاده می‌کند، در اینجا نحوه مهاجرت آمده است:

### قبل (API مستقیم)
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

### مزایای مهاجرت
- ✅ مدیریت خودکار سرویس
- ✅ حل نام مستعار مدل
- ✅ انتخاب بهینه‌سازی سخت‌افزاری
- ✅ مدیریت خطای بهتر
- ✅ سازگاری با SDK OpenAI
- ✅ پشتیبانی از جریان

## منابع

### مستندات رسمی
- **GitHub Foundry Local**: https://github.com/microsoft/Foundry-Local
- **منبع SDK پایتون**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **مرجع CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **API REST**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **عیب‌یابی**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### منابع Workshop
- **README جلسه 06**: `Workshop/notebooks/session06_README.md`
- **ابزارهای کمکی Workshop**: `Workshop/samples/workshop_utils.py`
- **دفترچه نمونه**: `Workshop/notebooks/session06_models_router.ipynb`

### جامعه
- **Discord**: https://aka.ms/foundry-local-discord
- **مشکلات GitHub**: https://github.com/microsoft/Foundry-Local/issues

## مراحل بعدی

1. **بررسی تغییرات**: فایل‌های به‌روزرسانی شده را بخوانید  
2. **آزمایش دفترچه**: دفترچه session06_models_router.ipynb را اجرا کنید  
3. **تأیید SDK**: اطمینان حاصل کنید که foundry-local-sdk نصب شده است  
4. **بررسی سرویس**: تأیید کنید که Foundry Local در حال اجرا است  
5. **مطالعه مستندات**: فایل جدید session06_README.md را بخوانید  

## خلاصه

این به‌روزرسانی‌ها اطمینان حاصل می‌کنند که مواد Workshop دقیقاً مطابق با **الگوهای رسمی SDK Foundry Local** همان‌طور که در مخزن GitHub مستند شده است، هستند. تمام مثال‌های کد، مستندات و ابزارهای کمکی اکنون با بهترین شیوه‌های توصیه‌شده مایکروسافت برای استقرار مدل‌های هوش مصنوعی محلی همسو هستند.

تغییرات بهبود می‌بخشند:
- ✅ **درستی**: استفاده از الگوهای رسمی SDK  
- ✅ **مستندسازی**: توضیحات و مثال‌های جامع  
- ✅ **مدیریت خطا**: پیام‌های بهتر و راهنمایی‌های عیب‌یابی  
- ✅ **نگهداری‌پذیری**: پیروی از کنوانسیون‌های رسمی  
- ✅ **تجربه کاربری**: دستورالعمل‌های واضح‌تر و کمک به اشکال‌زدایی  

---

**به‌روزرسانی شده:** 8 اکتبر 2025  
**نسخه SDK:** foundry-local-sdk (آخرین نسخه)  
**شاخه Workshop:** Reactor  

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.