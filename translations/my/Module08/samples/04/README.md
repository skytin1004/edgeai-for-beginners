<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9e55b8feba71ce09355b66e3a25b6ff",
  "translation_date": "2025-09-23T01:20:30+00:00",
  "source_file": "Module08/samples/04/README.md",
  "language_code": "my"
}
-->
# အခန်း ၄ နမူနာ: Chainlit RAG အကြံပေးမှု

Foundry Local ကို အသုံးပြု၍ အနည်းဆုံး Chainlit app ကို အလုပ်လုပ်စေပါ။

## လိုအပ်ချက်များ
- Windows 11, Python 3.10+
- Foundry Local ကို ထည့်သွင်းပြီး မော်ဒယ်တစ်ခုရရှိထားရန် (ဥပမာ `phi-4-mini`)
- `pip install -r Module08\requirements.txt`

## အလုပ်လုပ်ရန် (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
chainlit run samples\04\app.py -w
```

## အတည်ပြုရန်
```cmd
curl http://localhost:8000/v1/models
```

## ပြဿနာဖြေရှင်းခြင်း
- VS Code မှ "chainlit could not be resolved" ဟု ပြပါက:
	- Interpreter ကို ရွေးပါ `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)
	- လိုအပ်သော dependencies များကို ထည့်သွင်းထားကြောင်း သေချာပါ: `pip install -r Module08\requirements.txt`

## ရင်းမြစ်များ
- Open WebUI how-to (Open WebUI ဖြင့် chat app): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-chat-application-with-open-web-ui
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/

---

