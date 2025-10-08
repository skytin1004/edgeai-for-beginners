<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-08T12:17:40+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "my"
}
-->
# အစည်းအဝေး ၆: Foundry Local – ကိရိယာများအဖြစ် မော်ဒယ်များ

## အကျဉ်းချုပ်

မော်ဒယ်များကို ဒေသခံ AI အလုပ်လည်ပတ်မှုအလွှာအတွင်းတွင် ပေါင်းစပ်နိုင်သော ကိရိယာများအဖြစ် သတ်မှတ်ပါ။ ဒီအစည်းအဝေးမှာ အထူးပြု SLM/LLM ခေါ်ဆိုမှုများကို ချိတ်ဆက်ခြင်း၊ တာဝန်များကို ရွေးချယ်၍ လမ်းကြောင်းသတ်မှတ်ခြင်း၊ အပလီကေးရှင်းများအတွက် SDK မျက်နှာပြင်တစ်ခုတည်းကို ဖော်ထုတ်ခြင်း စသည်တို့ကို ပြသပါမည်။ သင်သည် ပေါ့ပါးသော မော်ဒယ်လမ်းကြောင်းသတ်မှတ်သူ + တာဝန်စီမံသူတစ်ခုကို တည်ဆောက်ပြီး၊ ၎င်းကို အပလီကေးရှင်း script ထဲတွင် ပေါင်းစပ်ပြီး Azure AI Foundry သို့ ထုတ်လုပ်မှုအလုပ်များအတွက် အဆင့်မြှင့်လမ်းကြောင်းကို အကြမ်းဖျဉ်းရေးသားပါမည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

- မော်ဒယ်များကို အတိအကျ သတ်မှတ်ထားသော စွမ်းရည်များနှင့်အတူ အတိအကျ သတ်မှတ်နိုင်ရန် **စိတ်ကူးပုံဖော်ခြင်း**
- ရည်ရွယ်ချက် / ဟန်ချက်ညီမှု အဆင့်သတ်မှတ်ခြင်းအပေါ် အခြေခံ၍ **တောင်းဆိုမှုများကို လမ်းကြောင်းသတ်မှတ်ခြင်း**
- အဆင့်များစွာသော တာဝန်များအတွက် အထွေထွေထွက်ကုန်များကို **ချိတ်ဆက်ခြင်း** (ခွဲခြမ်း → ဖြေရှင်း → ပြင်ဆင်)
- အောက်ခြေ အပလီကေးရှင်းများအတွက် **SDK API တစ်ခုတည်းကို ပေါင်းစပ်ခြင်း**
- Cloud သို့ **အဆင့်မြှင့်ခြင်း** (OpenAI-compatible စာချုပ်တစ်ခုတည်း)

## ကြိုတင်လိုအပ်ချက်များ

- အစည်းအဝေး ၁–၅ ပြီးစီးထားရမည်
- ဒေသခံမော်ဒယ်များစွာကို cache ထားရမည် (ဥပမာ - `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Cross-Platform ပတ်ဝန်းကျင် Snippet

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS မှ Remote/VM ဝန်ဆောင်မှုကို ဝင်ရောက်ရန်:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## အတန်းသရုပ်ပြစဉ် (၃၀ မိနစ်)

### ၁။ ကိရိယာစွမ်းရည် ကြေညာချက် (၅ မိနစ်)

`samples/06-tools/models_catalog.py` ဖိုင်ကို ဖန်တီးပါ:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### ၂။ ရည်ရွယ်ချက်ဖော်ထုတ်ခြင်းနှင့် လမ်းကြောင်းသတ်မှတ်ခြင်း (၈ မိနစ်)

`samples/06-tools/router.py` ဖိုင်ကို ဖန်တီးပါ:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### ၃။ အဆင့်များစွာသော တာဝန်ချိတ်ဆက်ခြင်း (၇ မိနစ်)

`samples/06-tools/pipeline.py` ဖိုင်ကို ဖန်တီးပါ:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### ၄။ စတင်မည့် ပရောဂျက်: `06-models-as-tools` ကို ပြင်ဆင်ခြင်း (၅ မိနစ်)

တိုးတက်မှုများ:
- Streaming token ပံ့ပိုးမှု ထည့်သွင်းပါ (UI အဆင့်ဆင့် အပ်ဒိတ်)
- ယုံကြည်မှု အဆင့်သတ်မှတ်ခြင်း ထည့်ပါ: စကားလုံးဆိုင်ရာ တူညီမှု သို့မဟုတ် prompt စံချိန်စံညွှန်း
- Trace JSON ကို ထုတ်ပေးပါ (ရည်ရွယ်ချက် → မော်ဒယ် → နောက်ကျမှု → token အသုံးပြုမှု)
- အဆင့်ခွဲခြားမှုများကို ထပ်မံအသုံးပြုနိုင်ရန် cache ကို အကောင်းဆုံးအသုံးပြုပါ

### ၅။ Azure သို့ အဆင့်မြှင့်ခြင်း လမ်းကြောင်း (၅ မိနစ်)

| အလွှာ | ဒေသခံ (Foundry) | Cloud (Azure AI Foundry) | အဆင့်မြှင့်လမ်းကြောင်း |
|-------|-----------------|--------------------------|---------------------|
| လမ်းကြောင်းသတ်မှတ်ခြင်း | Heuristic Python | တည်ငြိမ်သော microservice | API ကို containerize လုပ်ပြီး deploy လုပ်ပါ |
| မော်ဒယ်များ | SLMs cached | စီမံခန့်ခွဲမှု deployment | ဒေသခံအမည်များကို deployment IDs သို့ map လုပ်ပါ |
| ကြည့်ရှုမှု | CLI stats/manual | အလယ်ပိုင်း log နှင့် metrics | ဖွဲ့စည်းထားသော trace အဖြစ်အပျက်များ ထည့်ပါ |
| လုံခြုံရေး | ဒေသခံ host သာ | Azure auth / networking | key vault ကို ထည့်သွင်းပါ |
| ကုန်ကျစရိတ် | စက်ပစ္စည်းအရင်းအမြစ် | အသုံးပြုမှုအပေါ် အခြေခံသော ငွေတောင်းခံမှု | ဘတ်ဂျက် ကန့်သတ်ချက်များ ထည့်ပါ |

## အတည်ပြု စစ်ဆေးရန် စာရင်း

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

ရည်ရွယ်ချက်အပေါ် မော်ဒယ်ရွေးချယ်မှုနှင့် နောက်ဆုံး ပြင်ဆင်ထားသော ထွက်ကုန်ကို မျှော်လင့်ပါ။

## ပြဿနာဖြေရှင်းခြင်း

| ပြဿနာ | အကြောင်းရင်း | ဖြေရှင်းနည်း |
|---------|-------|-----|
| တာဝန်အားလုံးကို တစ်မျိုးတည်းသော မော်ဒယ်သို့ လမ်းကြောင်းသတ်မှတ်ထားသည် | စည်းမျဉ်းများ မခိုင်မာခြင်း | INTENT_RULES regex set ကို တိုးချဲ့ပါ |
| Pipeline အဆင့်တစ်ခုတွင် မအောင်မြင်ခြင်း | မော်ဒယ်မတင်ထားခြင်း | `foundry model run <model>` ကို run လုပ်ပါ |
| ထွက်ကုန်အညီအမျှမရှိခြင်း | ပြင်ဆင်မှုအဆင့်မရှိခြင်း | အကျဉ်းချုပ်/အတည်ပြုမှု အဆင့်ကို ထည့်ပါ |

## ကိုးကားချက်များ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Prompt Quality Patterns: Session 2 ကိုကြည့်ပါ

---

**အစည်းအဝေး ကြာချိန်**: ၃၀ မိနစ်  
**အဆင့်အခက်အခဲ**: ကျွမ်းကျင်

## နမူနာ အခြေအနေ & အလုပ်ရုံဆွေးနွေးမှု Mapping

| အလုပ်ရုံဆွေးနွေးမှု Scripts / Notebooks | အခြေအနေ | ရည်မှန်းချက် | Dataset / Catalog အရင်းအမြစ် |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | ရည်ရွယ်ချက်အမျိုးမျိုးပါဝင်သော prompt များကို ကိုင်တွယ်သော Developer assistant | Heuristic ရည်ရွယ်ချက် → မော်ဒယ်အမည်လမ်းကြောင်းသတ်မှတ်ခြင်းနှင့် token အသုံးပြုမှု | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | ရှုပ်ထွေးသော coding assistance တာဝန်အတွက် အဆင့်ဆင့် စီမံခြင်းနှင့် ပြင်ဆင်ခြင်း | ခွဲခြမ်း → အထူးပြုအကောင်အထည်ဖော်မှု → အကျဉ်းချုပ်ပြင်ဆင်မှု | အတူတူသော `CATALOG`; အဆင့်များကို စီမံချက်ထွက်ကုန်မှ ဆွဲယူ |

### အခြေအနေ အကြောင်းအရာ
အင်ဂျင်နီယာ ထုတ်လုပ်မှုကိရိယာတစ်ခုသည် ရည်ရွယ်ချက်အမျိုးမျိုးပါဝင်သော တာဝန်များကို လက်ခံရရှိသည်: ကုဒ်ပြုပြင်ခြင်း၊ ဖွဲ့စည်းမှုမှတ်စုများကို အကျဉ်းချုပ်ခြင်း၊ တုံ့ပြန်ချက်များကို အမျိုးအစားခွဲခြင်း။ နောက်ကျမှုနှင့် အရင်းအမြစ်အသုံးပြုမှုကို လျှော့ချရန်၊ မော်ဒယ်အသေးစားတစ်ခုက စီမံချက်ရေးဆွဲခြင်းနှင့် အကျဉ်းချုပ်ခြင်းကို လုပ်ဆောင်ပြီး၊ ကုဒ်အထူးပြုမော်ဒယ်က ပြုပြင်ခြင်းကို လုပ်ဆောင်ပြီး၊ အလေးချိန်နည်းသော အမျိုးအစားခွဲနိုင်သော မော်ဒယ်က တုံ့ပြန်ချက်များကို အမျိုးအစားခွဲသည်။ Pipeline script သည် ချိတ်ဆက်မှု + ပြင်ဆင်မှုကို ပြသပြီး၊ router script သည် တစ်ခုတည်းသော prompt လမ်းကြောင်းသတ်မှတ်မှုကို ခွဲခြားပြသသည်။

### Catalog Snapshot
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```

### နမူနာ စမ်းသပ်မှု Prompts
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```

### Trace Extension (Optional)
`models_pipeline.py` အတွက် အဆင့်တစ်ခုစီ Trace JSON လိုင်းများ ထည့်ပါ:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```

### Escalation Heuristic (Idea)
စီမံချက်တွင် "optimize", "security" စသည့် keyword များ ပါဝင်ပါက သို့မဟုတ် အဆင့်အရှည် > 280 စာလုံးရှိပါက → အဆိုပါအဆင့်အတွက်သာ မော်ဒယ်ကြီး (ဥပမာ - `gpt-oss-20b`) သို့ အဆင့်မြှင့်ပါ။

### အပိုတိုးတက်မှုများ

| နယ်ပယ် | တိုးတက်မှု | တန်ဖိုး | အကြံပြုချက် |
|------|-------------|-------|------|
| Caching | Reuse manager + client objects | နောက်ကျမှုနည်း၊ အလားအလာနည်း | `workshop_utils.get_client` ကို အသုံးပြုပါ |
| Usage Metrics | Tokens & အဆင့်တစ်ခုစီ၏ နောက်ကျမှုကို ဖမ်းယူပါ | အရည်အသွေးမြှင့်တင်ခြင်းနှင့် အချိန်တိုင်းတာခြင်း | Routed call တစ်ခုစီကို အချိန်တိုင်းပါ; trace စာရင်းတွင် သိမ်းဆည်းပါ |
| Adaptive Routing | ယုံကြည်မှု / ကုန်ကျစရိတ်ကို သိရှိခြင်း | အရည်အသွေး-ကုန်ကျစရိတ် အချိန်ညှိခြင်း | Scoring ထည့်ပါ: prompt > N စာလုံး သို့မဟုတ် regex domain ကို တွေ့ပါက → မော်ဒယ်ကြီးသို့ အဆင့်မြှင့်ပါ |
| Dynamic Capability Registry | Catalog ကို hot reload လုပ်ပါ | Restart / redeploy မလိုအပ် | Runtime တွင် `catalog.json` ကို load လုပ်ပါ; ဖိုင်အချိန်တံဆိပ်ကို ကြည့်ပါ |
| Fallback Strategy | Failures အောက်တွင် ခိုင်မာမှု | ရရှိနိုင်မှုမြင့်မား | Primary ကို စမ်းပါ → exception ဖြစ်ပါက fallback alias ကို စမ်းပါ |
| Streaming Pipeline | အစောပိုင်းတုံ့ပြန်မှု | UX တိုးတက်မှု | အဆင့်တစ်ခုစီကို stream လုပ်ပြီး နောက်ဆုံး refine input ကို buffer လုပ်ပါ |
| Vector Intent Embeddings | Routing ကို ပိုမိုတိကျစေခြင်း | ရည်ရွယ်ချက်တိကျမှု မြင့်မား | Prompt ကို embed လုပ်ပြီး cluster & map centroid → capability |
| Trace Export | ချိတ်ဆက်မှုကို စစ်ဆေးနိုင်မှု | အညွှန်း/အစီရင်ခံစာရေးခြင်း | JSON လိုင်းများထုတ်ပေးပါ: step, intent, model, latency_ms, tokens |
| Cost Simulation | Cloud မတိုင်မီ ခန့်မှန်းခြင်း | ဘတ်ဂျက်စီမံခြင်း | မော်ဒယ်တစ်ခုစီအတွက် token တစ်ခုချင်းစီ၏ ကုန်ကျစရိတ်ကို သတ်မှတ်ပြီး တာဝန်တစ်ခုစီအတွက် စုစုပေါင်းတွက်ချက်ပါ |
| Deterministic Mode | Repro reproducibility | စံချိန်စမ်းသပ်မှု | Env: `temperature=0`, fixed steps count |

#### Trace Structure နမူနာ

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```

#### Adaptive Escalation Sketch

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```

#### Model Catalog Hot Reload

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

အဆင့်ဆင့် တိုးတက်မှုများကို လုပ်ဆောင်ပါ—အစောပိုင်း prototype များကို အလွန်အမင်း အင်ဂျင်နီယာလုပ်ခြင်းမှ ရှောင်ကြဉ်ပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် ရှုယူသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။