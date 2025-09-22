<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-22T17:47:54+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "bn"
}
-->
# সেশন ৪ উদাহরণ: Chainlit RAG ডেমো

Foundry Local এর বিরুদ্ধে ন্যূনতম Chainlit অ্যাপ চালান।

## পূর্বশর্ত
- Windows 11, Python 3.10+
- Foundry Local ইনস্টল করা এবং একটি মডেল উপলব্ধ (যেমন, `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## চালান (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## যাচাই করুন
```cmd
curl http://localhost:8000/v1/models
```

## সমস্যা সমাধান
- যদি VS Code "chainlit could not be resolved" দেখায়:
	- ইন্টারপ্রেটার নির্বাচন করুন `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- নিশ্চিত করুন যে ডিপেন্ডেন্সিগুলি ইনস্টল করা আছে: `pip install -r Module08\requirements.txt`

## রেফারেন্স
- Open WebUI কিভাবে করবেন (Open WebUI সহ চ্যাট অ্যাপ): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (শিখুন): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

