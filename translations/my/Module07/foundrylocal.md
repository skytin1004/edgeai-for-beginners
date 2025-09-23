<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "070a706937c5ac9feb45693b8c572d25",
  "translation_date": "2025-09-23T01:23:25+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "my"
}
-->
# Foundry Local ကို Windows တွင် (Validated)

ဤလမ်းညွှန်သည် Microsoft Foundry Local ကို Windows တွင် ထည့်သွင်းခြင်း၊ အလုပ်လုပ်ခြင်းနှင့် ပေါင်းစည်းခြင်းအတွက် အကူအညီပေးပါသည်။ အဆင့်များနှင့် အမိန့်များကို Microsoft Learn စာရွက်စာတမ်းများနှင့် အတည်ပြုထားပါသည်။

- စတင်အသုံးပြုရန်: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architecture: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI Reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKs ပေါင်းစည်းခြင်း: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF Models (BYOM) ကို Compile လုပ်ခြင်း: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local နှင့် Cloud နှိုင်းယှဉ်ခြင်း: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Windows တွင် Install / Upgrade

- Install:
```cmd
winget install Microsoft.FoundryLocal
```
- Upgrade:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Version check:
```cmd
foundry --version
```

## 2) CLI အခြေခံ (အမျိုးအစား ၃ မျိုး)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Service:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Cache:
```cmd
foundry cache --help
foundry cache list
```

မှတ်ချက်များ:
- Service သည် OpenAI-compatible REST API ကို ဖွင့်ပေးသည်။ Endpoint port ကို dynamic အနေဖြင့် သတ်မှတ်ပေးသည်။ `foundry service status` ကို အသုံးပြု၍ port ကို ရှာဖွေပါ။
- SDKs ကို အသုံးပြုပါက အဆင်ပြေပါသည်။ SDKs သည် endpoint discovery ကို support ရှိသောနေရာများတွင် အလိုအလျောက် စီမံပေးပါသည်။

## 3) Local Endpoint ကို ရှာဖွေခြင်း (Dynamic Port)

Foundry Local သည် service စတင်တိုင်း dynamic port ကို သတ်မှတ်ပေးသည်:
```cmd
foundry service status
```
Report ပြထားသော `http://localhost:<PORT>` ကို OpenAI-compatible paths (ဥပမာ၊ `/v1/chat/completions`) နှင့် `base_url` အဖြစ် အသုံးပြုပါ။

## 4) OpenAI Python SDK ဖြင့် အမြန်စမ်းသပ်ခြင်း

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
References:
- SDK Integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) ကိုယ်ပိုင် Model (Olive ဖြင့် Compile လုပ်ပါ)

Catalog တွင် မပါဝင်သော model တစ်ခုလိုအပ်ပါက Olive ကို အသုံးပြု၍ Foundry Local အတွက် ONNX အဖြစ် Compile လုပ်ပါ။

အဆင့်မြင့် flow (အဆင့်များအတွက် စာရွက်စာတမ်းကို ကြည့်ပါ):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Docs:
- BYOM compile: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Troubleshooting

- Service status နှင့် logs ကို စစ်ဆေးပါ:
```cmd
foundry service status
foundry service diag
```
- Cache ကို ရှင်းလင်းခြင်း သို့မဟုတ် ရွှေ့ခြင်း:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- နောက်ဆုံး preview version သို့ update လုပ်ပါ:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Windows Developer Experience နှင့် ဆက်စပ်မှု

- Windows local နှင့် cloud AI ရွေးချယ်မှုများ၊ Foundry Local နှင့် Windows ML အပါအဝင်:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit ကို Foundry Local နှင့် အသုံးပြုခြင်း (chat endpoint URL ကို ရယူရန် `foundry service status` ကို အသုံးပြုပါ):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

---

