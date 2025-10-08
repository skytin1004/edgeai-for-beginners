<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-08T12:03:48+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "my"
}
-->
# အခန်း ၅: Foundry Local ဖြင့် AI အင်ဂျင်များကို အလျင်အမြန် တည်ဆောက်ခြင်း

## အကျဉ်းချုပ်

Foundry Local ၏ အနိမ့်လက်ဆွဲနှုန်းနှင့် ကိုယ်ရေးအချက်အလက်များကို ကာကွယ်ထားသော runtime ကို အသုံးပြု၍ အခန်းအနားများစွာရှိသော AI အင်ဂျင်များကို ဒီဇိုင်းဆွဲပြီး စီမံခန့်ခွဲပါ။ သင်သည် အင်ဂျင်၏ အခန်းကဏ္ဍများ၊ မှတ်ဉာဏ်နည်းလမ်းများ၊ ကိရိယာခေါ်ယူမှုပုံစံများနှင့် အကောင်အထည်ဖော်မှုဇယားများကို သတ်မှတ်မည်ဖြစ်သည်။ ဒီအခန်းတွင် Chainlit သို့မဟုတ် LangGraph ဖြင့် တိုးချဲ့နိုင်သော scaffolding ပုံစံများကို မိတ်ဆက်ပေးပါမည်။ Starter project သည် memory persistence နှင့် အကဲဖြတ်မှု hooks ထည့်သွင်းရန် ရှိပြီးသား agent architecture နမူနာကို တိုးချဲ့ပေးသည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

- **အခန်းများ သတ်မှတ်ခြင်း**: စနစ်အကြံပေးချက်များနှင့် စွမ်းရည်ကန့်သတ်ချက်များ
- **မှတ်ဉာဏ် အကောင်အထည်ဖော်ခြင်း**: အတိုချုပ် (စကားဝိုင်း), ရေရှည် (ဗက်တာ / ဖိုင်), ယာယီ scratchpads
- **Workflow များကို Scaffold လုပ်ခြင်း**: အဆက်မပြတ်၊ အခွဲအခြာနှင့် အပြိုင်အဆိုင် agent အဆင့်များ
- **ကိရိယာများ ထည့်သွင်းခြင်း**: အလွယ်တကူ function tool ခေါ်ယူမှုပုံစံ
- **အကဲဖြတ်ခြင်း**: အခြေခံ trace + rubric အခြေခံသော ရလဒ်အဆင့်သတ်မှတ်ခြင်း

## ကြိုတင်လိုအပ်ချက်များ

- အခန်း ၁–၄ ပြီးစီးထား
- Python နှင့် `foundry-local-sdk`, `openai`, optional `chainlit`
- `phi-4-mini` အနည်းဆုံးဖြင့် ဒေသခံမော်ဒယ်များ လည်ပတ်နေ

### Cross-Platform Environment Snippet

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS မှ Windows host service ကို remote မှာ agent များကို လည်ပတ်စေချင်ပါက:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (၃၀ မိနစ်)

### ၁. အင်ဂျင်၏ အခန်းများနှင့် မှတ်ဉာဏ် သတ်မှတ်ခြင်း (၇ မိနစ်)

`samples/05-agents/agents_core.py` ဖန်တီးပါ:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### ၂. CLI Scaffolding Pattern (၃ မိနစ်)

```powershell
python samples/05-agents/agents_core.py
```


### ၃. ကိရိယာခေါ်ယူမှု ထည့်သွင်းခြင်း (၇ မိနစ်)

`samples/05-agents/tools.py` ဖြင့် တိုးချဲ့ပါ:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```

`agents_core.py` ကို ပြင်ဆင်ပြီး ကိရိယာ syntax ကို လွယ်ကူစေပါ: အသုံးပြုသူသည် `#tool:get_time` ရေးပြီး အင်ဂျင်သည် generation မတိုင်မီ context ထဲသို့ ကိရိယာ output ကို ထည့်သွင်းပါမည်။

### ၄. Orchestrated Workflow (၆ မိနစ်)

`samples/05-agents/orchestrator.py` ဖန်တီးပါ:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### ၅. Starter Project: `05-agent-architecture` ကို တိုးချဲ့ပါ (၇ မိနစ်)

ထည့်သွင်းရန်:
1. Persistent memory layer (ဥပမာ- စကားဝိုင်းများကို JSON lines append)
2. အကဲဖြတ်မှု rubric ရိုးရှင်းသော- factuality / clarity / style placeholders
3. Optional Chainlit front-end (tab နှစ်ခု: စကားဝိုင်း & traces)
4. Optional LangGraph style state machine (dependency ထည့်သွင်းပါက) အခွဲအခြာဆုံးဖြတ်မှုများအတွက်

## Validation Checklist

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Tool injection မှတ်ချက်ပါရှိသော structured pipeline output ကို မျှော်လင့်ပါ။

## Memory Strategies Overview

| Layer | ရည်ရွယ်ချက် | ဥပမာ |
|-------|-------------|-------|
| အတိုချုပ် | စကားဝိုင်းဆက်လက်မှု | နောက်ဆုံး N မက်ဆေ့များ |
| Episodic | အစည်းအဝေးမှတ်ဉာဏ် | JSON per session |
| Semantic | ရေရှည်ပြန်လည်ရယူမှု | အကျဉ်းချုပ်များ၏ ဗက်တာ store |
| Scratchpad | Reasoning အဆင့်များ | Inline chain-of-thought (private) |

## Evaluation Hooks (အယူအဆ)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Troubleshooting

| ပြဿနာ | အကြောင်းရင်း | ဖြေရှင်းနည်း |
|-------|-------------|-------------|
| အကြောင်းပြန်များ ထပ်နေ | Context window အကြီး/အသေး | memory window parameter ကို tune လုပ်ပါ |
| ကိရိယာ မခေါ်ယူနိုင် | Syntax မှားနေ | `#tool:tool_name` format ကို အသုံးပြုပါ |
| Orchestration နှေးနေ | မော်ဒယ်များ အေးနေ | warmup prompts ကို ကြို run လုပ်ပါ |

## References

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (optional concept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Session Duration**: ၃၀ မိနစ်  
**အခက်အခဲအဆင့်**: အဆင့်မြင့်

## နမူနာအခြေအနေနှင့် Workshop Mapping

| Workshop Script | အခြေအနေ | ရည်မှန်းချက် | ဥပမာ Prompt |
|-----------------|----------|--------------|-------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | အမှုဆောင်များအတွက် အကျဉ်းချုပ်များ ထုတ်လုပ်သော အတတ်ပညာရှာဖွေမှု bot | အင်ဂျင်နှစ်ခု pipeline (research → editorial polish) distinct models optional | Edge inference compliance အရေးကြီးမှုကို ရှင်းပြပါ။ |
| (Extended) `tools.py` concept | အချိန်နှင့် token ခန့်မှန်းမှု tools ထည့်သွင်း | Lightweight tool invocation pattern ကို ပြသပါ | #tool:get_time |

### အခြေအနေအကြောင်းအရာ
Compliance documentation အဖွဲ့သည် cloud services သို့ မပို့ဘဲ ဒေသခံ knowledge မှ အတွင်းရေးအကျဉ်းချုပ်များကို အလျင်အမြန်လိုအပ်သည်။ Researcher agent သည် အတိုချုပ်သော အချက်အလက်များကို စုဆောင်းပြီး editor agent သည် အမှုဆောင်များအတွက် ရှင်းလင်းမှုရှိသော စာသားများကို ပြန်ရေးသည်။ Latency (fast SLM) နှင့် stylistic refinement (အကြီးမော်ဒယ်) ကို optimize လုပ်ရန် distinct model aliases သတ်မှတ်နိုင်သည်။

### နမူနာ Multi-Model Environment
```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```


### Trace Structure (Optional)
```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

တစ်ခုချင်းစီကို JSONL ဖိုင်တွင် rubric scoring အတွက် later persist လုပ်ပါ။

### Optional Enhancements

| Theme | Enhancement | အကျိုးကျေးဇူး | Implementation Sketch |
|-------|------------|--------------|-----------------------|
| Multi-Model Roles | Distinct models per agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specialization & speed | alias env vars ကို ရွေးချယ်ပြီး per-role alias ဖြင့် `chat_once` ကို ခေါ်ပါ |
| Structured Traces | act(tool,input,latency,tokens) တစ်ခုချင်း JSON trace | Debug & evaluation | dict ကို list ထဲသို့ append လုပ်ပြီး `.jsonl` ကို အဆုံးတွင် ရေးပါ |
| Memory Persistence | Reloadable dialog context | Session continuity | `Agent.memory` ကို `sessions/<ts>.json` သို့ dump လုပ်ပါ |
| Tool Registry | Dynamic tool discovery | Extensibility | `TOOLS` dict ကို maintain လုပ်ပြီး names/desc ကို introspect လုပ်ပါ |
| Retry & Backoff | Robust long chains | Reduce transient failures | `act` ကို try/except + exponential backoff ဖြင့် wrap လုပ်ပါ |
| Rubric Scoring | Automated qualitative labels | Track improvements | Secondary pass prompting model: "Rate clarity 1-5" |
| Vector Memory | Semantic recall | Rich long-term context | အကျဉ်းချုပ်များကို embed လုပ်ပြီး top-k ကို system message ထဲသို့ retrieve လုပ်ပါ |
| Streaming Replies | Faster perceived response | UX improvement | Streaming ကို အသုံးပြုပြီး partial tokens ကို flush လုပ်ပါ |
| Deterministic Tests | Regression control | Stable CI | `temperature=0`, fixed prompt seeds ဖြင့် run လုပ်ပါ |
| Parallel Branching | Faster exploration | Throughput | Independent agent steps အတွက် `concurrent.futures` ကို အသုံးပြုပါ |

#### Trace Record Example

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Simple Evaluation Prompt

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

(`answer`, `rating`) pairs ကို persist လုပ်ပြီး historical quality graph တည်ဆောက်ပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။