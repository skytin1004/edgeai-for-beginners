<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-22T13:40:34+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "fa"
}
-->
# نمونه جلسه ۱: گفتگوی سریع از طریق REST

اجرای یک درخواست چت ساده به Foundry Local با استفاده از `requests` در پایتون.

## پیش‌نیازها
- سرویس Foundry Local که یک مدل را اجرا می‌کند (مثلاً `phi-4-mini`)
- `pip install -r ../../requirements.txt`

## اجرا (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```


## منابع
- Foundry Local (آموزش): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- نمای کلی API سازگار با OpenAI: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

