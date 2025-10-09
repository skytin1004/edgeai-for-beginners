<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-09T10:41:17+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "pa"
}
-->
# ਸੈਸ਼ਨ 5: Foundry Local ਨਾਲ AI-ਚਲਿਤ ਏਜੰਟ ਤੇਜ਼ੀ ਨਾਲ ਬਣਾਓ

## ਸਾਰ

Foundry Local ਦੇ ਘੱਟ-ਵਿਲੰਬੀ, ਗੋਪਨੀਯਤਾ-ਸੁਰੱਖਿਅਤ ਰਨਟਾਈਮ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬਹੁ-ਭੂਮਿਕਾ AI ਏਜੰਟਾਂ ਨੂੰ ਡਿਜ਼ਾਈਨ ਅਤੇ ਸੰਚਾਲਿਤ ਕਰੋ। ਤੁਸੀਂ ਏਜੰਟ ਦੀਆਂ ਭੂਮਿਕਾਵਾਂ, ਯਾਦਾਂ ਦੀਆਂ ਰਣਨੀਤੀਆਂ, ਟੂਲ ਕਾਲਿੰਗ ਪੈਟਰਨ, ਅਤੇ ਐਗਜ਼ਿਕਿਊਸ਼ਨ ਗ੍ਰਾਫਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋਗੇ। ਸੈਸ਼ਨ ਵਿੱਚ ਉਹ ਪੈਟਰਨ ਸ਼ਾਮਲ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਤੁਸੀਂ Chainlit ਜਾਂ LangGraph ਨਾਲ ਵਧਾ ਸਕਦੇ ਹੋ। ਸ਼ੁਰੂਆਤੀ ਪ੍ਰੋਜੈਕਟ ਮੌਜੂਦਾ ਏਜੰਟ ਆਰਕੀਟੈਕਚਰ ਨਮੂਨੇ ਨੂੰ ਯਾਦਾਂ ਦੀ ਸਥਿਰਤਾ + ਮੁਲਾਂਕਣ ਹੁੱਕਸ ਸ਼ਾਮਲ ਕਰਨ ਲਈ ਵਧਾਉਂਦਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

- **ਭੂਮਿਕਾਵਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ**: ਸਿਸਟਮ ਪ੍ਰੋੰਪਟ ਅਤੇ ਸਮਰੱਥਾ ਦੀਆਂ ਹੱਦਾਂ
- **ਯਾਦਾਂ ਲਾਗੂ ਕਰੋ**: ਛੋਟੇ ਸਮੇਂ ਦੀ (ਗੱਲਬਾਤ), ਲੰਬੇ ਸਮੇਂ ਦੀ (ਵੇਕਟਰ / ਫਾਈਲ), ਅਸਥਾਈ ਸਕ੍ਰੈਚਪੈਡ
- **ਵਰਕਫਲੋਜ਼ ਬਣਾਓ**: ਲਗਾਤਾਰ, ਸ਼ਾਖਾਵਾਂ ਵਾਲੇ, ਅਤੇ ਸਮਾਂਤਰ ਏਜੰਟ ਕਦਮ
- **ਟੂਲਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰੋ**: ਹਲਕਾ ਫੰਕਸ਼ਨ ਟੂਲ ਕਾਲਿੰਗ ਪੈਟਰਨ
- **ਮੁਲਾਂਕਣ ਕਰੋ**: ਬੁਨਿਆਦੀ ਟ੍ਰੇਸ + ਰੂਬ੍ਰਿਕ-ਚਲਿਤ ਨਤੀਜਾ ਸਕੋਰਿੰਗ

## ਪੂਰਵ ਸ਼ਰਤਾਂ

- ਸੈਸ਼ਨ 1–4 ਪੂਰੇ ਕੀਤੇ ਹੋਣ
- Python ਨਾਲ `foundry-local-sdk`, `openai`, ਵਿਕਲਪਿਕ `chainlit`
- ਸਥਾਨਕ ਮਾਡਲ ਚੱਲ ਰਹੇ (ਘੱਟੋ-ਘੱਟ `phi-4-mini`)

### ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਵਾਤਾਵਰਣ ਸਨਿੱਪਟ

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

ਜੇ macOS ਤੋਂ ਦੂਰ Windows ਹੋਸਟ ਸੇਵਾ ਦੇ ਖਿਲਾਫ ਏਜੰਟ ਚਲਾਏ ਜਾ ਰਹੇ ਹਨ:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## ਡੈਮੋ ਫਲੋ (30 ਮਿੰਟ)

### 1. ਏਜੰਟ ਦੀਆਂ ਭੂਮਿਕਾਵਾਂ ਅਤੇ ਯਾਦਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ (7 ਮਿੰਟ)

`samples/05-agents/agents_core.py` ਬਣਾਓ:

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


### 2. CLI ਸਕੈਫੋਲਡਿੰਗ ਪੈਟਰਨ (3 ਮਿੰਟ)

```powershell
python samples/05-agents/agents_core.py
```


### 3. ਟੂਲ ਕਾਲਿੰਗ ਸ਼ਾਮਲ ਕਰੋ (7 ਮਿੰਟ)

`samples/05-agents/tools.py` ਨਾਲ ਵਧਾਓ:

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


`agents_core.py` ਨੂੰ ਸੋਧੋ ਤਾਂ ਜੋ ਸਧਾਰਨ ਟੂਲ ਸਿੰਟੈਕਸ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੋਵੇ: ਯੂਜ਼ਰ ਲਿਖਦਾ ਹੈ `#tool:get_time` ਅਤੇ ਏਜੰਟ ਜਨਰੇਸ਼ਨ ਤੋਂ ਪਹਿਲਾਂ ਸੰਦਰਭ ਵਿੱਚ ਟੂਲ ਆਉਟਪੁੱਟ ਨੂੰ ਵਧਾਉਂਦਾ ਹੈ।

### 4. ਸੰਚਾਲਿਤ ਵਰਕਫਲੋ (6 ਮਿੰਟ)

`samples/05-agents/orchestrator.py` ਬਣਾਓ:

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


### 5. ਸ਼ੁਰੂਆਤੀ ਪ੍ਰੋਜੈਕਟ: `05-agent-architecture` ਨੂੰ ਵਧਾਓ (7 ਮਿੰਟ)

ਸ਼ਾਮਲ ਕਰੋ:
1. ਸਥਿਰ ਯਾਦਾਂ ਦੀ ਪਰਤ (ਜਿਵੇਂ ਕਿ ਗੱਲਬਾਤਾਂ ਦੇ JSON ਲਾਈਨਾਂ ਐਪੈਂਡ)
2. ਸਧਾਰਨ ਮੁਲਾਂਕਣ ਰੂਬ੍ਰਿਕ: ਤਥਤਾ / ਸਪਸ਼ਟਤਾ / ਸ਼ੈਲੀ ਪਲੇਸਹੋਲਡਰ
3. ਵਿਕਲਪਿਕ Chainlit ਫਰੰਟ-ਐਂਡ (ਦੋ ਟੈਬ: ਗੱਲਬਾਤ ਅਤੇ ਟ੍ਰੇਸ)
4. ਵਿਕਲਪਿਕ LangGraph ਸ਼ੈਲੀ ਸਟੇਟ ਮਸ਼ੀਨ (ਜੇ ਡਿਪੈਂਡੈਂਸੀ ਸ਼ਾਮਲ ਕਰ ਰਹੇ ਹੋ) ਸ਼ਾਖਾਵਾਂ ਦੇ ਫੈਸਲੇ ਲਈ

## ਵੈਧਤਾ ਚੈੱਕਲਿਸਟ

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```


ਟੂਲ ਇੰਜੈਕਸ਼ਨ ਨੋਟ ਨਾਲ ਸੰਰਚਿਤ ਪਾਈਪਲਾਈਨ ਆਉਟਪੁੱਟ ਦੀ ਉਮੀਦ ਕਰੋ।

## ਯਾਦਾਂ ਦੀਆਂ ਰਣਨੀਤੀਆਂ ਦਾ ਜਾਇਜ਼ਾ

| ਪਰਤ | ਉਦੇਸ਼ | ਉਦਾਹਰਨ |
|-----|-------|---------|
| ਛੋਟੇ ਸਮੇਂ ਦੀ | ਗੱਲਬਾਤ ਦੀ ਲਗਾਤਾਰਤਾ | ਪਿਛਲੇ N ਸੁਨੇਹੇ |
| ਐਪੀਸੋਡਿਕ | ਸੈਸ਼ਨ ਯਾਦ | ਪ੍ਰਤੀ ਸੈਸ਼ਨ JSON |
| ਸੈਮੈਂਟਿਕ | ਲੰਬੇ ਸਮੇਂ ਦੀ ਰਿਕਾਲ | ਸੰਖੇਪਾਂ ਦੇ ਵੇਕਟਰ ਸਟੋਰ |
| ਸਕ੍ਰੈਚਪੈਡ | ਤਰਕ ਕਦਮ | ਇਨਲਾਈਨ ਚੇਨ-ਆਫ-ਥਾਟ (ਨਿੱਜੀ) |

## ਮੁਲਾਂਕਣ ਹੁੱਕਸ (ਧਾਰਨਾ)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## ਸਮੱਸਿਆ ਹੱਲ

| ਸਮੱਸਿਆ | ਕਾਰਨ | ਹੱਲ |
|--------|------|-----|
| ਦੁਹਰਾਏ ਜਾ ਰਹੇ ਜਵਾਬ | ਸੰਦਰਭ ਵਿੰਡੋ ਬਹੁਤ ਵੱਡੀ/ਛੋਟੀ | ਯਾਦਾਂ ਦੀ ਵਿੰਡੋ ਪੈਰਾਮੀਟਰ ਨੂੰ ਟਿਊਨ ਕਰੋ |
| ਟੂਲ ਕਾਲ ਨਹੀਂ ਹੋਇਆ | ਗਲਤ ਸਿੰਟੈਕਸ | `#tool:tool_name` ਫਾਰਮੈਟ ਦੀ ਵਰਤੋਂ ਕਰੋ |
| ਧੀਮੀ ਸੰਚਾਲਨਾ | ਕਈ ਠੰਡੇ ਮਾਡਲ | ਪ੍ਰੀ-ਰਨ ਵਾਰਮਅਪ ਪ੍ਰੋੰਪਟ |

## ਸੰਦਰਭ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (ਵਿਕਲਪਿਕ ਧਾਰਨਾ): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**ਸੈਸ਼ਨ ਦੀ ਮਿਆਦ**: 30 ਮਿੰਟ  
**ਕਠਿਨਾਈ**: ਉੱਚ-ਸਤਹ

## ਨਮੂਨਾ ਦ੍ਰਿਸ਼ ਅਤੇ ਵਰਕਸ਼ਾਪ ਮੈਪਿੰਗ

| ਵਰਕਸ਼ਾਪ ਸਕ੍ਰਿਪਟ | ਦ੍ਰਿਸ਼ | ਉਦੇਸ਼ | ਉਦਾਹਰਨ ਪ੍ਰੋੰਪਟ |
|------------------|-------|-------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | ਗਿਆਨ ਖੋਜ ਬੋਟ ਜੋ ਕਾਰਜਕਾਰੀ-ਅਨੁਕੂਲ ਸੰਖੇਪ ਪੈਦਾ ਕਰਦਾ ਹੈ | ਦੋ-ਏਜੰਟ ਪਾਈਪਲਾਈਨ (ਖੋਜ → ਸੰਪਾਦਕੀ ਪਾਲਿਸ਼) ਨਾਲ ਵਿਕਲਪਿਕ ਵੱਖਰੇ ਮਾਡਲ | ਸਮਝਾਓ ਕਿ ਕCompliance ਲਈ edge inference ਕਿਉਂ ਮਹੱਤਵਪੂਰਨ ਹੈ। |
| (ਵਧਾਇਆ) `tools.py` ਧਾਰਨਾ | ਸਮਾਂ ਅਤੇ ਟੋਕਨ ਅਨੁਮਾਨ ਟੂਲ ਸ਼ਾਮਲ ਕਰੋ | ਹਲਕੇ ਟੂਲ ਕਾਲਿੰਗ ਪੈਟਰਨ ਦਾ ਪ੍ਰਦਰਸ਼ਨ ਕਰੋ | #tool:get_time |

### ਦ੍ਰਿਸ਼ ਕਹਾਣੀ

Compliance ਦਸਤਾਵੇਜ਼ੀ ਟੀਮ ਨੂੰ ਸਥਾਨਕ ਗਿਆਨ ਤੋਂ ਤੇਜ਼ ਅੰਦਰੂਨੀ ਸੰਖੇਪ ਚਾਹੀਦੇ ਹਨ ਬਿਨਾਂ ਡ੍ਰਾਫਟਾਂ ਨੂੰ ਕਲਾਉਡ ਸੇਵਾਵਾਂ ਨੂੰ ਭੇਜਣ ਦੇ। ਇੱਕ ਖੋਜਕਰਤਾ ਏਜੰਟ ਸੰਖੇਪ ਤਥੀਕ ਬੁਲੇਟਸ ਇਕੱਠੇ ਕਰਦਾ ਹੈ; ਇੱਕ ਸੰਪਾਦਕ ਏਜੰਟ ਕਾਰਜਕਾਰੀ ਸਪਸ਼ਟਤਾ ਲਈ ਦੁਬਾਰਾ ਲਿਖਦਾ ਹੈ। ਵਿਲੰਬੀਤਾ ਨੂੰ ਠੀਕ ਕਰਨ ਲਈ ਵੱਖਰੇ ਮਾਡਲ ਅਲਿਆਸ ਸੌਂਪੇ ਜਾ ਸਕਦੇ ਹਨ (ਤੇਜ਼ SLM) ਵਿਰੁੱਧ ਸ਼ੈਲੀਕ ਸੁਧਾਰ (ਵੱਡਾ ਮਾਡਲ ਸਿਰਫ ਜਦੋਂ ਲੋੜੀਂਦਾ ਹੋਵੇ)।

### ਉਦਾਹਰਨ ਬਹੁ-ਮਾਡਲ ਵਾਤਾਵਰਣ

```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```


### ਟ੍ਰੇਸ ਸਟ੍ਰਕਚਰ (ਵਿਕਲਪਿਕ)

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


ਹਰ ਕਦਮ ਨੂੰ JSONL ਫਾਈਲ ਵਿੱਚ ਬਾਅਦ ਦੇ ਰੂਬ੍ਰਿਕ ਸਕੋਰਿੰਗ ਲਈ ਸਥਿਰ ਕਰੋ।

### ਵਿਕਲਪਿਕ ਸੁਧਾਰ

| ਥੀਮ | ਸੁਧਾਰ | ਲਾਭ | ਲਾਗੂ ਕਰਨ ਦਾ ਖਾਕਾ |
|------|-------|-----|------------------|
| ਬਹੁ-ਮਾਡਲ ਭੂਮਿਕਾਵਾਂ | ਪ੍ਰਤੀ ਏਜੰਟ ਵੱਖਰੇ ਮਾਡਲ (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | ਵਿਸ਼ੇਸ਼ਤਾ ਅਤੇ ਗਤੀ | ਅਲਿਆਸ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਚੁਣੋ, ਪ੍ਰਤੀ-ਭੂਮਿਕਾ ਅਲਿਆਸ ਨਾਲ `chat_once` ਕਾਲ ਕਰੋ |
| ਸੰਰਚਿਤ ਟ੍ਰੇਸ | ਹਰ ਕਦਮ(tool,input,latency,tokens) ਦਾ JSON ਟ੍ਰੇਸ | ਡਿਬੱਗ ਅਤੇ ਮੁਲਾਂਕਣ | ਡਿਕਟ ਨੂੰ ਸੂਚੀ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ; ਅੰਤ ਵਿੱਚ `.jsonl` ਲਿਖੋ |
| ਯਾਦਾਂ ਦੀ ਸਥਿਰਤਾ | ਮੁੜ ਲੋਡ ਕਰਨ ਯੋਗ ਗੱਲਬਾਤ ਸੰਦਰਭ | ਸੈਸ਼ਨ ਲਗਾਤਾਰਤਾ | `Agent.memory` ਨੂੰ `sessions/<ts>.json` ਵਿੱਚ ਡੰਪ ਕਰੋ |
| ਟੂਲ ਰਜਿਸਟਰੀ | ਗਤੀਸ਼ੀਲ ਟੂਲ ਖੋਜ | ਵਧਾਉਣਯੋਗਤਾ | `TOOLS` ਡਿਕਟ ਨੂੰ ਰੱਖੋ ਅਤੇ ਨਾਮ/ਵਰਣਨ ਦੀ ਜਾਂਚ ਕਰੋ |
| ਰੀਟ੍ਰਾਈ ਅਤੇ ਬੈਕਆਫ | ਮਜ਼ਬੂਤ ਲੰਬੀਆਂ ਚੇਨ | ਅਸਥਾਈ ਨਾਕਾਮੀਆਂ ਘਟਾਓ | `act` ਨੂੰ try/except + exponential backoff ਨਾਲ ਲਪੇਟੋ |
| ਰੂਬ੍ਰਿਕ ਸਕੋਰਿੰਗ | ਸਵੈਚਾਲਿਤ ਗੁਣਾਤਮਕ ਲੇਬਲ | ਸੁਧਾਰਾਂ ਨੂੰ ਟ੍ਰੈਕ ਕਰੋ | ਮਾਡਲ ਨੂੰ ਦੂਜਾ ਪਾਸ ਪ੍ਰੋੰਪਟ: "Rate clarity 1-5" |
| ਵੇਕਟਰ ਯਾਦ | ਸੈਮੈਂਟਿਕ ਰਿਕਾਲ | ਧਨਾਢ ਲੰਬੇ ਸਮੇਂ ਦਾ ਸੰਦਰਭ | ਸੰਖੇਪਾਂ ਨੂੰ ਐਮਬੈਡ ਕਰੋ, ਸਿਸਟਮ ਸੁਨੇਹੇ ਵਿੱਚ top-k ਨੂੰ ਰੀਟ੍ਰੀਵ ਕਰੋ |
| ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬ | ਤੇਜ਼ ਮਹਿਸੂ ਕੀਤੀ ਗਤੀ | UX ਸੁਧਾਰ | ਸਟ੍ਰੀਮਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰੋ ਜਦੋਂ ਉਪਲਬਧ ਹੋਵੇ ਅਤੇ ਅੰਸ਼ਿਕ ਟੋਕਨ ਫਲਸ਼ ਕਰੋ |
| ਨਿਰਧਾਰਤ ਟੈਸਟ | ਰਿਗਰੈਸ਼ਨ ਕੰਟਰੋਲ | ਸਥਿਰ CI | `temperature=0`, ਫਿਕਸਡ ਪ੍ਰੋੰਪਟ ਸੀਡ ਨਾਲ ਚਲਾਓ |
| ਸਮਾਂਤਰ ਸ਼ਾਖਾਵਾਂ | ਤੇਜ਼ ਪੜਤਾਲ | throughput | ਸਵਤੰਤਰ ਏਜੰਟ ਕਦਮਾਂ ਲਈ `concurrent.futures` ਦੀ ਵਰਤੋਂ ਕਰੋ |

#### ਟ੍ਰੇਸ ਰਿਕਾਰਡ ਉਦਾਹਰਨ

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### ਸਧਾਰਨ ਮੁਲਾਂਕਣ ਪ੍ਰੋੰਪਟ

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```


(`answer`, `rating`) ਜੋੜਿਆਂ ਨੂੰ ਸਥਿਰ ਕਰੋ ਤਾਂ ਜੋ ਇਤਿਹਾਸਕ ਗੁਣਵੱਤਾ ਗ੍ਰਾਫ ਬਣਾਇਆ ਜਾ ਸਕੇ।

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।