<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-08T21:51:08+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "fa"
}
-->
# جلسه ۳: مدل‌های متن‌باز در Foundry Local

## چکیده

کشف کنید که چگونه می‌توان مدل‌های Hugging Face و دیگر مدل‌های متن‌باز را به Foundry Local وارد کرد. با استراتژی‌های انتخاب، جریان‌های کاری مشارکت جامعه، روش‌شناسی مقایسه عملکرد و نحوه گسترش Foundry با ثبت مدل‌های سفارشی آشنا شوید. این جلسه با موضوعات اکتشافی هفتگی "دوشنبه‌های مدل" هم‌خوانی دارد و شما را برای ارزیابی و عملیاتی کردن مدل‌های متن‌باز به صورت محلی قبل از مقیاس‌گذاری به Azure آماده می‌کند.

## اهداف یادگیری

در پایان این جلسه شما قادر خواهید بود:

- **کشف و ارزیابی**: شناسایی مدل‌های کاندیدا (mistral، gemma، qwen، deepseek) با توجه به تعادل کیفیت و منابع.
- **بارگذاری و اجرا**: استفاده از CLI Foundry Local برای دانلود، ذخیره و اجرای مدل‌های جامعه.
- **ارزیابی عملکرد**: اعمال معیارهای ثابت برای تأخیر، سرعت تولید توکن و کیفیت.
- **گسترش**: ثبت یا تطبیق یک پوشش مدل سفارشی با الگوهای سازگار با SDK.
- **مقایسه**: تولید مقایسه‌های ساختاریافته برای تصمیم‌گیری در انتخاب SLM در مقابل مدل‌های متوسط LLM.

## پیش‌نیازها

- تکمیل جلسات ۱ و ۲
- محیط پایتون با نصب `foundry-local-sdk`
- حداقل ۱۵ گیگابایت فضای دیسک آزاد برای ذخیره مدل‌های متعدد
- اختیاری: فعال‌سازی شتاب‌دهی GPU/WebGPU (`foundry config list`)

### شروع سریع محیط چند‌پلتفرمی

Windows PowerShell:  
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```
  
macOS / Linux:  
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```
  
هنگام ارزیابی عملکرد از macOS در مقابل سرویس میزبان ویندوز، تنظیم کنید:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## جریان دمو (۳۰ دقیقه)

### ۱. بارگذاری مدل‌های Hugging Face از طریق CLI (۸ دقیقه)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```
  

### ۲. اجرا و بررسی سریع (۵ دقیقه)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```
  

### ۳. اسکریپت ارزیابی عملکرد (۸ دقیقه)

ایجاد فایل `samples/03-oss-models/benchmark_models.py`:  
```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```
  
اجرا:  
```powershell
python samples/03-oss-models/benchmark_models.py
```
  

### ۴. مقایسه عملکرد (۵ دقیقه)

بحث در مورد تعادل‌ها: زمان بارگذاری، مصرف حافظه (مشاهده Task Manager / `nvidia-smi` / مانیتور منابع سیستم‌عامل)، کیفیت خروجی در مقابل سرعت. استفاده از اسکریپت ارزیابی عملکرد پایتون (جلسه ۳) برای تأخیر و سرعت تولید توکن؛ تکرار پس از فعال‌سازی شتاب‌دهی GPU.

### ۵. پروژه شروع‌کننده (۴ دقیقه)

ایجاد یک تولید‌کننده گزارش مقایسه مدل (گسترش اسکریپت ارزیابی عملکرد با خروجی مارک‌داون).

## پروژه شروع‌کننده: گسترش `03-huggingface-models`

نمونه موجود را با موارد زیر بهبود دهید:

1. افزودن تجمیع ارزیابی عملکرد + خروجی CSV/Markdown.
2. پیاده‌سازی امتیازدهی کیفی ساده (مجموعه جفت پرسش + فایل نمونه‌گذاری دستی).
3. معرفی یک تنظیم JSON (`models.json`) برای لیست مدل‌های قابل اتصال و مجموعه پرسش‌ها.

## چک‌لیست اعتبارسنجی

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```
  
تمام مدل‌های هدف باید ظاهر شوند و به درخواست چت آزمایشی پاسخ دهند.

## سناریوی نمونه و نقشه‌برداری کارگاه

| اسکریپت کارگاه | سناریو | هدف | منبع پرسش / مجموعه داده |
|-----------------|----------|------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | تیم پلتفرم Edge انتخاب SLM پیش‌فرض برای خلاصه‌ساز جاسازی‌شده | تولید مقایسه تأخیر + p95 + توکن‌ها در ثانیه بین مدل‌های کاندیدا | متغیر `PROMPT` داخلی + لیست محیطی `BENCH_MODELS` |

### روایت سناریو
مهندسی محصول باید یک مدل خلاصه‌سازی سبک پیش‌فرض برای ویژگی یادداشت‌های جلسه آفلاین انتخاب کند. آن‌ها ارزیابی‌های کنترل‌شده و تعیین‌کننده (temperature=0) را در یک مجموعه پرسش ثابت اجرا می‌کنند (به مثال زیر مراجعه کنید) و معیارهای تأخیر و سرعت تولید توکن را با و بدون شتاب‌دهی GPU جمع‌آوری می‌کنند.

### مثال مجموعه پرسش JSON (قابل گسترش)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```
  
هر پرسش را برای هر مدل اجرا کنید، تأخیر هر پرسش را ثبت کنید تا معیارهای توزیع استخراج شود و نقاط خارج از محدوده شناسایی شوند.

## چارچوب انتخاب مدل

| بعد | معیار | اهمیت |
|----------|--------|----------------|
| تأخیر | میانگین / p95 | ثبات تجربه کاربری |
| سرعت تولید | توکن‌ها در ثانیه | مقیاس‌پذیری دسته‌ای و جریانی |
| حافظه | اندازه مقیم | تناسب دستگاه و هم‌زمانی |
| کیفیت | پرسش‌های معیار | مناسب بودن وظیفه |
| اثر | ذخیره دیسک | توزیع و به‌روزرسانی‌ها |
| مجوز | اجازه استفاده | انطباق تجاری |

## گسترش با مدل سفارشی

الگوی سطح بالا (شبه‌کد):  
```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```
  
به مخزن رسمی برای رابط‌های تطبیق در حال تکامل مراجعه کنید:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  

## رفع اشکال

| مشکل | علت | راه‌حل |
|-------|-------|-----|
| OOM در mistral-7b | رم/GPU ناکافی | توقف مدل‌های دیگر؛ امتحان نسخه کوچک‌تر |
| پاسخ اولیه کند | بارگذاری سرد | با یک پرسش سبک دوره‌ای گرم نگه دارید |
| توقف دانلود | ناپایداری شبکه | تلاش مجدد؛ پیش‌بارگذاری در ساعات کم‌ترافیک |

## منابع

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- دوشنبه‌های مدل: https://aka.ms/model-mondays  
- کشف مدل‌های Hugging Face: https://huggingface.co/models  

---

**مدت زمان جلسه**: ۳۰ دقیقه (+ بررسی عمیق اختیاری)  
**سطح دشواری**: متوسط  

### بهبودهای اختیاری

| بهبود | مزیت | چگونه |
|-------------|---------|-----|
| تأخیر اولین توکن جریانی | اندازه‌گیری پاسخ‌دهی محسوس | اجرای ارزیابی عملکرد با `BENCH_STREAM=1` (اسکریپت بهبود‌یافته در `Workshop/samples/session03`) |
| حالت تعیین‌کننده | مقایسه‌های پایدار رگرسیون | `temperature=0`، مجموعه پرسش ثابت، ثبت خروجی‌های JSON تحت کنترل نسخه |
| امتیازدهی معیار کیفیت | افزودن بعد کیفی | نگهداری `prompts.json` با جنبه‌های مورد انتظار؛ امتیازدهی دستی یا از طریق مدل ثانویه |
| خروجی CSV / Markdown | گزارش قابل اشتراک‌گذاری | گسترش اسکریپت برای نوشتن `benchmark_report.md` با جدول و نکات برجسته |
| برچسب‌های قابلیت مدل | کمک به مسیریابی خودکار بعدی | نگهداری `models.json` با `{alias: {capabilities:[], size_mb:..}}` |
| مرحله گرم کردن حافظه پنهان | کاهش تعصب بارگذاری سرد | اجرای یک دور گرم قبل از حلقه زمان‌گیری (قبلاً پیاده‌سازی شده) |
| دقت درصدی | تأخیر انتهایی قوی | استفاده از درصد numpy (قبلاً در اسکریپت بازسازی‌شده) |
| تقریب هزینه توکن | مقایسه اقتصادی | هزینه تقریبی = (توکن‌ها در ثانیه * میانگین توکن‌ها در هر درخواست) * معیار انرژی |
| پرش خودکار مدل‌های ناموفق | انعطاف‌پذیری در اجراهای دسته‌ای | هر ارزیابی عملکرد را در try/except قرار دهید و فیلد وضعیت را علامت‌گذاری کنید |

#### قطعه خروجی مارک‌داون حداقلی

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```
  

#### مثال مجموعه پرسش تعیین‌کننده

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```
  
لیست ثابت را به جای پرسش‌های تصادفی حلقه کنید تا معیارهای قابل مقایسه در میان کامیت‌ها به دست آید.

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.