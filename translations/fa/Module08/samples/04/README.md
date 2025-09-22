<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T13:41:11+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "fa"
}
-->
# نمونه جلسه ۴: دموی Chainlit RAG

اجرای برنامه حداقلی Chainlit در برابر Foundry Local.

## پیش‌نیازها
- ویندوز ۱۱، پایتون ۳.۱۰ یا بالاتر
- نصب Foundry Local و دسترسی به یک مدل (مثلاً `phi-4-mini`)
- اجرای دستور `pip install -r Module08\requirements.txt`

## اجرا (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```


## اعتبارسنجی
```cmd
curl http://localhost:8000/v1/models
```


## رفع اشکال
- اگر VS Code پیام "chainlit could not be resolved" را نشان داد:
	- مفسر `Module08/.venv/Scripts/python.exe` را انتخاب کنید (Ctrl+Shift+P → Python: Select Interpreter)
	- مطمئن شوید که وابستگی‌ها نصب شده‌اند: `pip install -r Module08\requirements.txt`

## منابع
- راهنمای Open WebUI (برنامه چت با Open WebUI): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (یادگیری): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

