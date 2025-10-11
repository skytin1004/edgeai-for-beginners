<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-11T11:50:27+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "ta"
}
-->
# அமர்வு 5: Foundry Local மூலம் AI சக்திவாய்ந்த முகவர்களை விரைவாக உருவாக்குங்கள்

## சுருக்கம்

Foundry Local இன் குறைந்த தாமதம் மற்றும் தனியுரிமை பாதுகாக்கும் runtime-ஐ பயன்படுத்தி பல வேட AI முகவர்களை வடிவமைத்து ஒருங்கிணைக்கவும். நீங்கள் முகவர்களின் வேடங்கள், நினைவக உத்திகள், கருவி அழைப்பு முறைமைகள் மற்றும் செயல்பாட்டு வரைபடங்களை வரையறுப்பீர்கள். இந்த அமர்வு Chainlit அல்லது LangGraph மூலம் நீட்டிக்கக்கூடிய scaffolding முறைமைகளை அறிமுகப்படுத்துகிறது. Starter திட்டம் உள்ளடக்க நினைவக நிலைத்தன்மை மற்றும் மதிப்பீட்டு hooks சேர்க்கும் வகையில் ஏற்கனவே உள்ள முகவர் கட்டமைப்பு மாதிரியை விரிவாக்குகிறது.

## கற்றல் நோக்கங்கள்

- **வேடங்களை வரையறுக்கவும்**: அமைப்பு உந்துதல்கள் மற்றும் திறன் எல்லைகள்
- **நினைவகத்தை செயல்படுத்தவும்**: குறுகிய கால (உரையாடல்), நீண்ட கால (வெக்டர் / கோப்பு), தற்காலிக scratchpads
- **செயல்முறைகளை Scaffold செய்யவும்**: தொடர்ச்சியான, கிளை மற்றும் இணை முகவர் படிகள்
- **கருவிகளை ஒருங்கிணைக்கவும்**: எளிய செயல்பாட்டு கருவி அழைப்பு முறை
- **மதிப்பீடு செய்யவும்**: அடிப்படை trace + rubric-ஆல் இயக்கப்படும் முடிவு மதிப்பீடு

## முன் தேவைகள்

- அமர்வுகள் 1–4 முடிக்கப்பட்டிருக்க வேண்டும்
- Python மற்றும் `foundry-local-sdk`, `openai`, விருப்பமான `chainlit`
- உள்ளூர் மாடல்கள் இயக்கம் (`phi-4-mini` குறைந்தபட்சம்)

### பல்வேறு தள சூழல் குறிப்பு

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

macOS-இல் இருந்து ஒரு தொலை Windows ஹோஸ்ட் சேவையை எதிர்த்து முகவர்களை இயக்கும்போது:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## டெமோ ஓட்டம் (30 நிமிடங்கள்)

### 1. முகவர் வேடங்கள் மற்றும் நினைவகத்தை வரையறுக்கவும் (7 நிமிடங்கள்)

`samples/05-agents/agents_core.py` உருவாக்கவும்:

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


### 2. CLI Scaffolding Pattern (3 நிமிடங்கள்)

```powershell
python samples/05-agents/agents_core.py
```


### 3. கருவி அழைப்பைச் சேர்க்கவும் (7 நிமிடங்கள்)

`samples/05-agents/tools.py` மூலம் விரிவாக்கவும்:

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

`agents_core.py`-ஐ மாற்றி எளிய கருவி syntax-ஐ அனுமதிக்கவும்: பயனர் `#tool:get_time` எழுதுகிறார், முகவர் உருவாக்கத்திற்கு முன் சூழலில் கருவி வெளியீட்டை விரிவாக்குகிறார்.

### 4. ஒருங்கிணைக்கப்பட்ட செயல்முறை (6 நிமிடங்கள்)

`samples/05-agents/orchestrator.py` உருவாக்கவும்:

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


### 5. Starter Project: `05-agent-architecture`-ஐ விரிவாக்கவும் (7 நிமிடங்கள்)

சேர்க்கவும்:
1. நிலையான நினைவக அடுக்கு (எ.கா., உரையாடல்களின் JSON வரிகள் இணைப்பு)
2. எளிய மதிப்பீட்டு rubric: உண்மைத்தன்மை / தெளிவு / பாணி placeholders
3. விருப்பமான Chainlit முன்புறம் (இரண்டு தாவல்கள்: உரையாடல் & traces)
4. விருப்பமான LangGraph பாணி நிலை இயந்திரம் (இணைப்பு dependency சேர்க்கும்போது) கிளை முடிவுகளுக்கு

## சரிபார்ப்பு சோதனை பட்டியல்

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

கருவி சேர்க்கும் குறிப்புடன் அமைந்த குழாய் வெளியீட்டை எதிர்பார்க்கவும்.

## நினைவக உத்திகள் கண்ணோட்டம்

| அடுக்கு | நோக்கம் | உதாரணம் |
|--------|---------|---------|
| குறுகிய கால | உரையாடல் தொடர்ச்சி | கடைசி N செய்திகள் |
| நிகழ்வுக்கான | அமர்வு நினைவகம் | ஒவ்வொரு அமர்வுக்கும் JSON |
| அர்த்தபூர்வமான | நீண்டகால மீட்பு | சுருக்கங்களின் வெக்டர் சேமிப்பு |
| Scratchpad | காரணமுடைய படிகள் | Inline chain-of-thought (தனியுரிமை) |

## மதிப்பீட்டு hooks (கோட்பாடு)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## சிக்கல்களை சரிசெய்தல்

| சிக்கல் | காரணம் | தீர்வு |
|--------|--------|-------|
| மீண்டும் மீண்டும் பதில்கள் | சூழல் சாளரம் மிகப் பெரியது/சிறியது | நினைவக சாளர அளவுருவை சரிசெய்க |
| கருவி அழைக்கப்படவில்லை | தவறான syntax | `#tool:tool_name` வடிவத்தைப் பயன்படுத்தவும் |
| மெதுவான ஒருங்கிணைப்பு | பல குளிர்ந்த மாடல்கள் | முன்-இயக்க warmup உந்துதல்கள் |

## குறிப்புகள்

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (விருப்பமான கோட்பாடு): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**அமர்வு காலம்**: 30 நிமிடங்கள்  
**சிரமம்**: மேம்பட்டது

## மாதிரி சூழல் & பணிக்கூட வரைபடம்

| பணிக்கூட ஸ்கிரிப்ட் | சூழல் | நோக்கம் | உதாரண உந்துதல் |
|--------------------|-------|---------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | நிர்வாகத்திற்கான சுருக்கங்களை உருவாக்கும் அறிவு ஆராய்ச்சி பாட் | இரண்டு முகவர் குழாய் (ஆராய்ச்சி → ஆசிரியர் மெருகூட்டல்) விருப்பமான தனித்த மாடல்களுடன் | compliance-க்கு edge inference ஏன் முக்கியம் என்பதை விளக்கவும். |
| (விரிவாக்கம்) `tools.py` கோட்பாடு | நேரம் & token மதிப்பீட்டு கருவிகளைச் சேர்க்கவும் | எளிய கருவி அழைப்பு முறைமையை விளக்கவும் | #tool:get_time |

### சூழல் கதை
Compliance ஆவணக்குழு உள்ளூர் அறிவிலிருந்து விரைவான உள்நாட்டு சுருக்கங்களை உருவாக்க வேண்டும், ஆனால் வரைபடங்களை cloud சேவைகளுக்கு அனுப்ப விரும்பவில்லை. ஆராய்ச்சியாளர் முகவர் சுருக்கமான உண்மையான புள்ளிகளை சேகரிக்கிறார்; ஆசிரியர் முகவர் நிர்வாக தெளிவுக்காக மீண்டும் எழுதுகிறார். தாமதத்தை மேம்படுத்த distinct மாடல் alias-களை ஒதுக்கலாம் (வேகமான SLM) vs பாணி மெருகூட்டல் (தேவையான போது மட்டுமே பெரிய மாடல்).

### உதாரண பல மாடல் சூழல்
```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```


### Trace அமைப்பு (விருப்பம்)
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

ஒவ்வொரு படியையும் JSONL கோப்பில் நிலைத்துவைக்க rubric மதிப்பீட்டிற்காக.

### விருப்பமான மேம்பாடுகள்

| தீம் | மேம்பாடு | நன்மை | செயல்பாட்டு வரைபடம் |
|-----|---------|-------|--------------------|
| பல மாடல் வேடங்கள் | ஒவ்வொரு முகவருக்கும் தனித்த மாடல்கள் (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | சிறப்பு மற்றும் வேகம் | alias சூழல் மாறிகளைத் தேர்ந்தெடுக்கவும், ஒவ்வொரு வேட alias-க்கும் `chat_once` அழைக்கவும் |
| அமைந்த Traces | ஒவ்வொரு செயல்(tool,input,latency,tokens) JSON trace | Debug & மதிப்பீடு | dict-ஐ பட்டியலில் சேர்க்கவும்; முடிவில் `.jsonl` எழுதவும் |
| நினைவக நிலைத்தன்மை | மீண்டும் ஏற்றக்கூடிய உரையாடல் சூழல் | அமர்வு தொடர்ச்சி | `Agent.memory`-ஐ `sessions/<ts>.json`-க்கு dump செய்யவும் |
| கருவி பதிவேடு | மாறும் கருவி கண்டறிதல் | விரிவாக்கத்தன்மை | `TOOLS` dict-ஐ பராமரிக்கவும் & பெயர்கள்/விளக்கங்களை introspect செய்யவும் |
| மீண்டும் முயற்சி & Backoff | நீண்ட சங்கிலிகள் உறுதியாக | தற்காலிக தோல்விகளை குறைக்கவும் | `act`-ஐ try/except + exponential backoff-இன் மூலம் சுற்றவும் |
| Rubric மதிப்பீடு | தானியங்கி தரமான லேபிள்கள் | மேம்பாடுகளைப் பின்தொடரவும் | இரண்டாம் pass prompting மாடல்: "Rate clarity 1-5" |
| வெக்டர் நினைவகம் | அர்த்தபூர்வமான மீட்பு | செறிவான நீண்டகால சூழல் | சுருக்கங்களை embed செய்யவும், system message-க்கு top-k-ஐ retrieve செய்யவும் |
| ஸ்ட்ரீமிங் பதில்கள் | வேகமான perceived பதில் | UX மேம்பாடு | ஸ்ட்ரீமிங் கிடைக்கும் போது பயன்படுத்தவும் மற்றும் partial tokens flush செய்யவும் |
| தீர்மானமான சோதனைகள் | Regression கட்டுப்பாடு | நிலையான CI | `temperature=0`, fixed prompt seeds-இன் மூலம் இயக்கவும் |
| இணை கிளை | வேகமான ஆராய்ச்சி | Throughput | சுயாதீன முகவர் படிகளுக்கு `concurrent.futures` பயன்படுத்தவும் |

#### Trace பதிவு உதாரணம்

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### எளிய மதிப்பீட்டு உந்துதல்

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

(`answer`, `rating`) ஜோடிகளை நிலைத்துவைத்து வரலாற்று தரத்திற்கான வரைபடத்தை உருவாக்கவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரச்சிறப்பிற்காக முயற்சி செய்கிறோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.