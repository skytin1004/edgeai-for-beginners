<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15ab280cc2acd8bbf545cc9a78a408bf",
  "translation_date": "2025-09-23T01:18:09+00:00",
  "source_file": "Module08/samples/01/README.md",
  "language_code": "my"
}
-->
# အစဉ်အလာ ၁ နမူနာ: REST ဖြင့် အမြန်စကားပြောခြင်း

Python `requests` ကို အသုံးပြု၍ Foundry Local သို့ အနည်းဆုံး စကားပြောတောင်းဆိုမှုကို လုပ်ဆောင်ပါ။

## လိုအပ်ချက်များ
- Foundry Local ဝန်ဆောင်မှုသည် မော်ဒယ်တစ်ခု (ဥပမာ `phi-4-mini`) ကို လည်ပတ်နေသည်။
- `pip install -r ../../requirements.txt`

## လုပ်ဆောင်ရန် (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python samples\01\chat_quickstart.py "Write a 1-sentence welcome message."
```

## ရင်းမြစ်များ
- Foundry Local (Learn): https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/
- OpenAI-compatible API overview: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

