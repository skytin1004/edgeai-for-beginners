<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-22T13:40:57+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "fa"
}
-->
# نمونه جلسه ۶: مدل‌ها به عنوان ابزار

این نمونه یک روتر ساده + ثبت ابزار را پیاده‌سازی می‌کند که بر اساس درخواست کاربر یک مدل را انتخاب کرده و نقطه پایانی سازگار با OpenAI در Foundry Local را فراخوانی می‌کند.

## فایل‌ها
- `router.py`: ثبت ساده و مسیریابی مبتنی بر اکتشافی؛ کشف نقطه پایانی + بررسی سلامت.

## اجرا (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## نکات
- روتر از اکتشافات ساده کلیدواژه‌ای برای انتخاب بین ابزارهای `general`، `reasoning` و `code` استفاده می‌کند و در شروع `/v1/models` را چاپ می‌کند.
- تنظیمات از طریق متغیرهای محیطی:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-distill-qwen-7b"},"code":{"model":"qwen2.5-7b-instruct"}}
```

## منابع
- Foundry Local (آموزش): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- ادغام با SDK‌های استنتاج: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

