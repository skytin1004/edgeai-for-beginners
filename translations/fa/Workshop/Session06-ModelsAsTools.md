<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-08T21:53:31+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "fa"
}
-->
# جلسه ۶: Foundry Local – مدل‌ها به‌عنوان ابزار

## خلاصه

مدل‌ها را به‌عنوان ابزارهای ترکیبی در یک لایه عملیاتی محلی هوش مصنوعی در نظر بگیرید. این جلسه نشان می‌دهد که چگونه می‌توان چندین فراخوانی تخصصی SLM/LLM را زنجیره‌ای کرد، وظایف را به‌صورت انتخابی مسیریابی کرد و یک سطح SDK یکپارچه را برای برنامه‌ها ارائه داد. شما یک مسیریاب مدل سبک + برنامه‌ریز وظیفه خواهید ساخت، آن را در یک اسکریپت برنامه ادغام خواهید کرد و مسیر مقیاس‌پذیری به Azure AI Foundry برای بارهای کاری تولیدی را ترسیم خواهید کرد.

## اهداف یادگیری

- **مفهوم‌سازی** مدل‌ها به‌عنوان ابزارهای اتمی با قابلیت‌های تعریف‌شده  
- **مسیریابی** درخواست‌ها بر اساس قصد / امتیازدهی اکتشافی  
- **زنجیره‌سازی** خروجی‌ها در وظایف چندمرحله‌ای (تجزیه → حل → اصلاح)  
- **ادغام** یک API مشتری یکپارچه برای برنامه‌های پایین‌دستی  
- **مقیاس‌دهی** طراحی به فضای ابری (همان قرارداد سازگار با OpenAI)  

## پیش‌نیازها

- تکمیل جلسات ۱ تا ۵  
- چندین مدل محلی ذخیره‌شده (مانند `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)  

### قطعه کد محیط چندپلتفرمی

Windows PowerShell:  
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
macOS / Linux:  
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
دسترسی به سرویس Remote/VM از macOS:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## جریان دمو (۳۰ دقیقه)

### ۱. اعلام قابلیت ابزار (۵ دقیقه)

ایجاد فایل `samples/06-tools/models_catalog.py`:  

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```
  

### ۲. تشخیص قصد و مسیریابی (۸ دقیقه)

ایجاد فایل `samples/06-tools/router.py`:  

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```
  

### ۳. زنجیره‌سازی وظایف چندمرحله‌ای (۷ دقیقه)

ایجاد فایل `samples/06-tools/pipeline.py`:  

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```
  

### ۴. پروژه آغازین: تطبیق `06-models-as-tools` (۵ دقیقه)

بهبودها:  
- افزودن پشتیبانی از توکن‌های استریم (به‌روزرسانی تدریجی UI)  
- افزودن امتیازدهی اعتماد: همپوشانی لغوی یا معیار درخواست  
- صادرات JSON ردیابی (قصد → مدل → تأخیر → استفاده از توکن)  
- پیاده‌سازی استفاده مجدد از کش برای زیرمراحل تکراری  

### ۵. مسیر مقیاس‌دهی به Azure (۵ دقیقه)

| لایه | محلی (Foundry) | ابری (Azure AI Foundry) | استراتژی انتقال |
|------|----------------|-------------------------|------------------|
| مسیریابی | Python اکتشافی | میکروسرویس پایدار | کانتینری‌سازی و استقرار API |
| مدل‌ها | SLM‌های ذخیره‌شده | استقرارهای مدیریت‌شده | نگاشت نام‌های محلی به شناسه‌های استقرار |
| مشاهده‌پذیری | آمار CLI/دستی | ثبت مرکزی و معیارها | افزودن رویدادهای ردیابی ساختاریافته |
| امنیت | فقط میزبان محلی | احراز هویت Azure / شبکه‌سازی | معرفی key vault برای اسرار |
| هزینه | منابع دستگاه | صورتحساب مصرف | افزودن محافظ‌های بودجه |

## چک‌لیست اعتبارسنجی

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```
  
انتظار انتخاب مدل بر اساس قصد و خروجی نهایی اصلاح‌شده.

## رفع اشکال

| مشکل | علت | راه‌حل |
|------|-----|--------|
| همه وظایف به یک مدل مسیریابی می‌شوند | قوانین ضعیف | مجموعه regex INTENT_RULES را غنی کنید |
| زنجیره وظایف در مرحله میانی شکست می‌خورد | مدل بارگذاری نشده | اجرای `foundry model run <model>` |
| انسجام خروجی پایین | مرحله اصلاح وجود ندارد | افزودن مرحله خلاصه‌سازی/اعتبارسنجی |

## منابع

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- مستندات Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry  
- الگوهای کیفیت درخواست: مراجعه به جلسه ۲  

---

**مدت زمان جلسه**: ۳۰ دقیقه  
**سطح دشواری**: پیشرفته  

## سناریوی نمونه و نقشه‌برداری کارگاه

| اسکریپت‌ها / نوت‌بوک‌های کارگاه | سناریو | هدف | منبع مجموعه داده / کاتالوگ |
|--------------------------------|---------|------|----------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | دستیار توسعه‌دهنده که درخواست‌های مختلط را مدیریت می‌کند (بازنویسی، خلاصه‌سازی، طبقه‌بندی) | مسیریابی قصد اکتشافی → نام مستعار مدل با استفاده از توکن | `CATALOG` داخلی + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | برنامه‌ریزی چندمرحله‌ای و اصلاح برای وظیفه پیچیده کمک به کدنویسی | تجزیه → اجرای تخصصی → مرحله اصلاح خلاصه‌سازی | همان `CATALOG`; مراحل مشتق‌شده از خروجی برنامه |

### روایت سناریو
یک ابزار بهره‌وری مهندسی وظایف متنوعی دریافت می‌کند: بازنویسی کد، خلاصه‌سازی یادداشت‌های معماری، طبقه‌بندی بازخورد. برای کاهش تأخیر و استفاده از منابع، یک مدل عمومی کوچک برنامه‌ریزی و خلاصه‌سازی را انجام می‌دهد، یک مدل تخصصی کدنویسی بازنویسی را مدیریت می‌کند، و یک مدل سبک طبقه‌بندی بازخورد را برچسب‌گذاری می‌کند. اسکریپت زنجیره‌ای + اصلاح را نشان می‌دهد؛ اسکریپت مسیریاب مسیریابی تطبیقی درخواست‌های تک‌مرحله‌ای را جدا می‌کند.

### عکس فوری کاتالوگ
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```
  

### نمونه درخواست‌های آزمایشی
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```
  

### گسترش ردیابی (اختیاری)
افزودن خطوط JSON ردیابی مرحله‌ای برای `models_pipeline.py`:  
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```
  

### ایده اکتشافی تشدید
اگر برنامه شامل کلمات کلیدی مانند "بهینه‌سازی"، "امنیت"، یا طول مرحله > ۲۸۰ کاراکتر باشد → تشدید به مدل بزرگ‌تر (مانند `gpt-oss-20b`) فقط برای آن مرحله.

### بهبودهای اختیاری

| حوزه | بهبود | ارزش | نکته |
|------|-------|------|------|
| کش | استفاده مجدد از مدیر + اشیاء مشتری | کاهش تأخیر، کاهش سربار | استفاده از `workshop_utils.get_client` |
| معیارهای استفاده | ضبط توکن‌ها و تأخیر مرحله‌ای | پروفایل‌سازی و بهینه‌سازی | زمان‌بندی هر فراخوانی مسیریابی‌شده؛ ذخیره در لیست ردیابی |
| مسیریابی تطبیقی | آگاه به اعتماد / هزینه | تجارت بهتر کیفیت-هزینه | افزودن امتیازدهی: اگر درخواست > N کاراکتر یا regex دامنه را مطابقت دهد → تشدید به مدل بزرگ‌تر |
| ثبت قابلیت پویا | بارگذاری کاتالوگ در زمان اجرا | بدون نیاز به راه‌اندازی مجدد | بارگذاری `catalog.json` در زمان اجرا؛ مشاهده timestamp فایل |
| استراتژی پشتیبان | مقاومت در برابر شکست‌ها | دسترسی بالاتر | تلاش اولیه → در صورت استثنا نام مستعار پشتیبان |
| زنجیره استریم | بازخورد اولیه | بهبود تجربه کاربری | استریم هر مرحله و بافر ورودی اصلاح نهایی |
| جاسازی‌های قصد برداری | مسیریابی دقیق‌تر | دقت بالاتر قصد | جاسازی درخواست، خوشه‌بندی و نگاشت مرکز → قابلیت |
| صادرات ردیابی | زنجیره قابل حسابرسی | انطباق/گزارش‌دهی | انتشار خطوط JSON: مرحله، قصد، مدل، تأخیر_ms، توکن‌ها |
| شبیه‌سازی هزینه | تخمین پیش‌ابری | برنامه‌ریزی بودجه | تخصیص هزینه فرضی/توکن برای هر مدل و جمع‌آوری برای هر وظیفه |
| حالت تعیین‌کننده | بازتولید قابل اعتماد | معیارگذاری پایدار | محیط: `temperature=0`, تعداد مراحل ثابت |

#### مثال ساختار ردیابی

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```
  

#### طرح تشدید تطبیقی

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```
  

#### بارگذاری داغ کاتالوگ مدل

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```
  

به‌صورت تدریجی تکرار کنید—از پیچیده‌سازی بیش از حد نمونه‌های اولیه اولیه خودداری کنید.

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه انسانی حرفه‌ای استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.