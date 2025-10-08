<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T11:57:48+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "my"
}
-->
# Foundry Local SDK အပ်ဒိတ်များ

## အကျဉ်းချုပ်

Workshop notebooks နှင့် utilities များကို **Foundry Local Python SDK** ၏ တရားဝင် pattern များအတိုင်း အသုံးပြုနိုင်ရန် အပ်ဒိတ်လုပ်ပြီး အောက်ပါ GitHub repository များမှ pattern များကို အခြေခံထားသည်။
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## ပြင်ဆင်ထားသော ဖိုင်များ

### 1. `Workshop/samples/workshop_utils.py`

**ပြောင်းလဲမှုများ:**
- ✅ `foundry-local-sdk` package အတွက် import error ကို handle လုပ်နိုင်ရန် ထည့်သွင်းထားသည်
- ✅ တရားဝင် SDK pattern များနှင့် ကိုက်ညီသော documentation ကို မြှင့်တင်ထားသည်
- ✅ Unicode symbols (✓, ✗, ⚠) အသုံးပြု၍ logging ကို မြှင့်တင်ထားသည်
- ✅ ဥပမာများပါဝင်သော docstring များကို ထည့်သွင်းထားသည်
- ✅ CLI command များကို ရည်ညွှန်းထားသော error message များကို မြှင့်တင်ထားသည်
- ✅ တရားဝင် SDK documentation နှင့် ကိုက်ညီသော comment များကို ပြင်ဆင်ထားသည်

**အဓိက မြှင့်တင်မှုများ:**

#### Import Error Handling
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### မြှင့်တင်ထားသော `get_client()` Function
- SDK initialization pattern အကြောင်းကို အသေးစိတ် documentation ထည့်သွင်းထားသည်
- `FoundryLocalManager` သည် service ကို auto-start လုပ်သည်ဟု ရှင်းပြထားသည်
- hardware-optimized variant များသို့ model alias resolution ကို ရှင်းပြထားသည်
- endpoint အချက်အလက်များနှင့် logging ကို မြှင့်တင်ထားသည်
- troubleshooting အဆင့်များကို အကြံပြုထားသော error message များကို မြှင့်တင်ထားသည်

#### မြှင့်တင်ထားသော `chat_once()` Function
- အသုံးပြုမှု ဥပမာများပါဝင်သော docstring ကို ထည့်သွင်းထားသည်
- OpenAI SDK compatibility ကို ရှင်းပြထားသည်
- streaming support (kwargs ဖြင့်) ကို documentation ထည့်သွင်းထားသည်
- CLI command များကို ရည်ညွှန်းထားသော error message များကို မြှင့်တင်ထားသည်
- model availability checking အကြောင်းကို မှတ်ချက်ထည့်ထားသည်

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**ပြောင်းလဲမှုများ:**
- ✅ SDK references ဖြင့် markdown cells များကို အပ်ဒိတ်လုပ်ထားသည်
- ✅ SDK pattern explanation များပါဝင်သော code comment များကို မြှင့်တင်ထားသည်
- ✅ cell documentation နှင့် ရှင်းပြချက်များကို မြှင့်တင်ထားသည်
- ✅ troubleshooting အကြံပြုချက်များကို ထည့်သွင်းထားသည်
- ✅ model catalog ကို အပ်ဒိတ်လုပ်ထားသည် ('gpt-oss-20b' ကို 'phi-3.5-mini' ဖြင့် အစားထိုးထားသည်)
- ✅ visual indicators ဖြင့် output formatting ကို မြှင့်တင်ထားသည်
- ✅ SDK links နှင့် references များကို ထည့်သွင်းထားသည်

**Cell-by-Cell Updates:**

#### Cell 1 (ခေါင်းစဉ်)
- SDK documentation links ကို ထည့်သွင်းထားသည်
- တရားဝင် GitHub repositories ကို ရည်ညွှန်းထားသည်

#### Cell 2 (Scenario)
- အဆင့်များကို နံပါတ်ဖြင့် ပြန်လည်ဖွဲ့စည်းထားသည်
- intent-based routing pattern ကို ရှင်းပြထားသည်
- local execution ၏ အကျိုးကျေးဇူးများကို အထူးပြောထားသည်

#### Cell 3 (Dependency Installation)
- package တစ်ခုချင်းစီ၏ အကျိုးကျေးဇူးကို ရှင်းပြထားသည်
- SDK ၏ capability များ (alias resolution, hardware optimization) ကို documentation ထည့်သွင်းထားသည်

#### Cell 4 (Environment Setup)
- function docstring များကို မြှင့်တင်ထားသည်
- SDK pattern များကို ရှင်းပြထားသော inline comment များကို ထည့်သွင်းထားသည်
- model catalog structure ကို documentation ထည့်သွင်းထားသည်
- priority/capability matching ကို ရှင်းပြထားသည်

#### Cell 5 (Catalog Check)
- visual checkmarks (✓) ကို ထည့်သွင်းထားသည်
- output ကို ပိုမိုကောင်းမွန်စွာ format ပြုလုပ်ထားသည်

#### Cell 6 (Intent Detection Test)
- output ကို table-style ဖြင့် ပြန်လည်ဖွဲ့စည်းထားသည်
- intent နှင့် ရွေးချယ်ထားသော model ကို ပြသထားသည်

#### Cell 7 (Routing Function)
- SDK pattern explanation ကို ပြည့်စုံစွာ ရှင်းပြထားသည်
- initialization flow ကို documentation ထည့်သွင်းထားသည်
- feature များအားလုံး (retry, tracking, errors) ကို စာရင်းပြုစုထားသည်
- SDK reference link ကို ထည့်သွင်းထားသည်

#### Cell 8 (Batch Demo)
- မျှော်လင့်ရမည့် အချက်အလက်များကို ရှင်းပြထားသည်
- troubleshooting အပိုင်းကို ထည့်သွင်းထားသည်
- debugging အတွက် CLI command များကို ထည့်သွင်းထားသည်
- output display ကို ပိုမိုကောင်းမွန်စွာ format ပြုလုပ်ထားသည်

### 3. `Workshop/notebooks/session06_README.md` (ဖိုင်အသစ်)

**အောက်ပါအကြောင်းအရာများပါဝင်သော documentation ကို ဖန်တီးထားသည်:**

1. **အကျဉ်းချုပ်**: Architecture diagram နှင့် component ရှင်းပြချက်
2. **SDK Integration**: တရားဝင် pattern များအတိုင်း code ဥပမာများ
3. **Prerequisites**: အဆင့်ဆင့် setup လုပ်နည်း
4. **အသုံးပြုမှု**: notebook ကို run လုပ်နည်းနှင့် customize လုပ်နည်း
5. **Model Aliases**: hardware-optimized variant များအကြောင်း ရှင်းပြချက်
6. **Troubleshooting**: အများဆုံးဖြစ်နိုင်သော ပြဿနာများနှင့် ဖြေရှင်းနည်းများ
7. **Extending**: intents, models, နှင့် custom logic များ ထည့်သွင်းနည်း
8. **Performance Tips**: production အတွက် အကောင်းဆုံး လုပ်နည်းများ
9. **Resources**: တရားဝင် documentation နှင့် community link များ

## SDK Pattern Implementation

### တရားဝင် Pattern (Foundry Local docs မှ)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Workshop Utils တွင် ကျွန်ုပ်တို့၏ Implementation
```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**ကျွန်ုပ်တို့၏ အားသာချက်များ:**
- ✅ တရားဝင် SDK pattern ကို တိကျစွာ လိုက်နာထားသည်
- ✅ caching ကို ထည့်သွင်းထားပြီး initialization ကို ထပ်မလုပ်ရအောင် ကာကွယ်ထားသည်
- ✅ production robustness အတွက် retry logic ထည့်သွင်းထားသည်
- ✅ token usage tracking ကို support ပြုလုပ်ထားသည်
- ✅ error message များကို ပိုမိုကောင်းမွန်စွာ ပြသထားသည်
- ✅ တရားဝင် ဥပမာများနှင့် compatibility ရှိသည်

## Model Catalog Changes

### အရင်
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### အခု
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**အကြောင်းရင်း:** 'gpt-oss-20b' (non-standard alias) ကို 'phi-3.5-mini' (Foundry Local ၏ တရားဝင် alias) ဖြင့် အစားထိုးထားသည်။

## Dependencies

### Updated requirements.txt

Workshop requirements.txt တွင် အောက်ပါများပါဝင်ပြီးသားဖြစ်သည်။
```
foundry-local-sdk
openai>=1.30.0
```

Foundry Local integration အတွက် လိုအပ်သော packages များသာပါဝင်သည်။

## Updates ကို စမ်းသပ်ခြင်း

### 1. Foundry Local ရှိ/မရှိ စစ်ဆေးရန်

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. ရရှိနိုင်သော Models များ စစ်ဆေးရန်

```bash
foundry model ls
```

အောက်ပါ models များ ရရှိနိုင်ရန် သို့မဟုတ် auto-download လုပ်ရန် သေချာပါစေ။
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Notebook ကို Run လုပ်ရန်

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

သို့မဟုတ် VS Code တွင် ဖွင့်ပြီး cell အားလုံးကို run လုပ်ပါ။

### 4. မျှော်လင့်ရသော အပြုသဘော

**Cell 1 (Install):** packages များကို အောင်မြင်စွာ install လုပ်သည်  
**Cell 2 (Setup):** error မရှိဘဲ import လုပ်နိုင်သည်  
**Cell 3 (Verify):** ✓ နှင့် model list ကို ပြသသည်  
**Cell 4 (Test Intent):** intent detection ရလဒ်များကို ပြသသည်  
**Cell 5 (Router):** ✓ Route function အဆင်သင့်ဖြစ်သည်ဟု ပြသသည်  
**Cell 6 (Execute):** prompts များကို models သို့ route လုပ်ပြီး ရလဒ်များကို ပြသသည်  

### 5. Connection Error များ Troubleshooting

`APIConnectionError: Connection error` ဖြစ်ပါက:
```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```


## Environment Variables

အောက်ပါ environment variables များကို support ပြုလုပ်ထားသည်:

| Variable | Default | Description |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | token usage ကို print လုပ်ရန် `1` သတ်မှတ်ပါ |
| `RETRY_ON_FAIL` | `1` | retry logic ကို enable လုပ်ရန် |
| `RETRY_BACKOFF` | `1.0` | retry delay (seconds) ကို သတ်မှတ်ရန် |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | service endpoint ကို override လုပ်ရန် |

### အသုံးပြုမှု ဥပမာများ

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```


## Old Pattern မှ မိုက်ဂရိတ်လုပ်ခြင်း

Direct API calls အသုံးပြုထားသော code ရှိပါက မိုက်ဂရိတ်လုပ်နည်း:

### အရင် (Direct API)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### အခု (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### မိုက်ဂရိတ်လုပ်ခြင်း၏ အကျိုးကျေးဇူးများ
- ✅ service ကို auto-manage လုပ်နိုင်သည်
- ✅ model alias resolution ကို support ပြုလုပ်သည်
- ✅ hardware optimization ကို ရွေးချယ်ပေးသည်
- ✅ error handling ကို မြှင့်တင်ထားသည်
- ✅ OpenAI SDK compatibility ရှိသည်
- ✅ streaming support ရှိသည်

## References

### တရားဝင် Documentation
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK Source**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Troubleshooting**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop Resources
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Sample Notebook**: `Workshop/notebooks/session06_models_router.ipynb`

### Community
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## နောက်ထပ်အဆင့်များ

1. **ပြောင်းလဲမှုများကို ပြန်လည်သုံးသပ်ပါ**: updated files များကို ဖတ်ပါ  
2. **Notebook ကို စမ်းသပ်ပါ**: session06_models_router.ipynb ကို run လုပ်ပါ  
3. **SDK ကို စစ်ဆေးပါ**: foundry-local-sdk install လုပ်ထားသည်ကို သေချာပါစေ  
4. **Service ကို စစ်ဆေးပါ**: Foundry Local ရှိ/မရှိကို အတည်ပြုပါ  
5. **Docs ကို လေ့လာပါ**: အသစ်ထည့်ထားသော session06_README.md ကို ဖတ်ပါ  

## အကျဉ်းချုပ်

Workshop materials များသည် **Foundry Local SDK patterns** ၏ တရားဝင် GitHub repository တွင် ရှင်းပြထားသောအတိုင်း လိုက်နာထားသည်ကို သေချာစေသော updates များဖြစ်သည်။ code ဥပမာများ၊ documentation နှင့် utilities များသည် Microsoft ၏ local AI model deployment အတွက် အကောင်းဆုံး လုပ်နည်းများနှင့် ကိုက်ညီစွာ ပြင်ဆင်ထားသည်။

ပြောင်းလဲမှုများသည် အောက်ပါအချက်များကို မြှင့်တင်ပေးသည်။
- ✅ **တိကျမှု**: တရားဝင် SDK patterns ကို အသုံးပြုထားသည်  
- ✅ **Documentation**: ရှင်းပြချက်များနှင့် ဥပမာများကို ပြည့်စုံစွာ ထည့်သွင်းထားသည်  
- ✅ **Error Handling**: troubleshooting အတွက် ပိုမိုကောင်းမွန်သော message များ  
- ✅ **Maintainability**: တရားဝင် convention များကို လိုက်နာထားသည်  
- ✅ **User Experience**: ပိုမိုရှင်းလင်းသော လမ်းညွှန်ချက်များနှင့် debugging အကူအညီ  

---

**Updated:** October 8, 2025  
**SDK Version:** foundry-local-sdk (latest)  
**Workshop Branch:** Reactor  

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။