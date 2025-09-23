<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d28c8fdf6c32d02120403c7b4526392b",
  "translation_date": "2025-09-23T01:19:42+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "my"
}
-->
# အခန်း ၆ နမူနာ: ကိရိယာများအဖြစ် မော်ဒယ်များ

ဒီနမူနာက အသုံးပြုသူရဲ့ prompt အပေါ်မူတည်ပြီး မော်ဒယ်ကို ရွေးချယ်ပြီး Foundry Local ရဲ့ OpenAI-compatible endpoint ကို ခေါ်ယူတဲ့ အနည်းဆုံး router + tool registry ကို အကောင်အထည်ဖော်ထားပါတယ်။

## ဖိုင်များ
- `router.py`: ရိုးရှင်းတဲ့ registry နဲ့ heuristic routing; endpoint ရှာဖွေမှု + ကျန်းမာရေးစစ်ဆေးမှု။

## အလုပ်လုပ်ရန် (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b-instruct
foundry model run deepseek-r1-distill-qwen-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## မှတ်ချက်များ
- Router က `general`, `reasoning`, နဲ့ `code` tools တွေကို ရွေးချယ်ဖို့ ရိုးရှင်းတဲ့ keyword heuristics ကို အသုံးပြုပြီး စတင်ချိန်မှာ `/v1/models` ကို print လုပ်ပါတယ်။
- Environment variables တွေကို အသုံးပြုပြီး အဆင်ပြေစွာ ပြင်ဆင်နိုင်ပါတယ်:
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

## ရင်းမြစ်များ
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Inference SDKs တွေနဲ့ ပေါင်းစပ်မှု: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

