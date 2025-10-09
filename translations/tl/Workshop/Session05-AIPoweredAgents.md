<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-09T19:17:14+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "tl"
}
-->
# Session 5: Mabilis na Pagbuo ng AI-Powered Agents gamit ang Foundry Local

## Abstrak

Magdisenyo at mag-orchestrate ng multi-role AI agents gamit ang low-latency at privacy-preserving runtime ng Foundry Local. Magtatakda ka ng mga role ng agent, memory strategies, tool invocation patterns, at execution graphs. Ang session ay nagpapakilala ng scaffolding patterns na maaari mong palawakin gamit ang Chainlit o LangGraph. Ang starter project ay nagpapalawak sa umiiral na sample ng agent architecture upang magdagdag ng memory persistence + evaluation hooks.

## Mga Layunin sa Pagkatuto

- **Tukuyin ang Mga Role**: System prompts at capability boundaries
- **Ipatupad ang Memory**: Short-term (conversation), long-term (vector / file), ephemeral scratchpads
- **Scaffold Workflows**: Sequential, branching, at parallel agent steps
- **Integrate Tools**: Magaan na function tool calling pattern
- **Evaluate**: Basic trace + rubric-driven outcome scoring

## Mga Kinakailangan

- Nakumpleto ang Sessions 1–4
- Python na may `foundry-local-sdk`, `openai`, optional na `chainlit`
- Lokal na mga modelo na tumatakbo (hindi bababa sa `phi-4-mini`)

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

Kung nagpapatakbo ng agents mula sa macOS laban sa remote Windows host service:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (30 min)

### 1. Tukuyin ang Mga Role ng Agent at Memory (7 min)

Gumawa ng `samples/05-agents/agents_core.py`:

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


### 2. CLI Scaffolding Pattern (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Magdagdag ng Tool Invocation (7 min)

Palawakin gamit ang `samples/05-agents/tools.py`:

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

Baguhin ang `agents_core.py` upang pahintulutan ang simpleng syntax ng tool: ang user ay nagsusulat ng `#tool:get_time` at ang agent ay nagpapalawak ng output ng tool sa konteksto bago ang generation.

### 4. Orchestrated Workflow (6 min)

Gumawa ng `samples/05-agents/orchestrator.py`:

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


### 5. Starter Project: Palawakin ang `05-agent-architecture` (7 min)

Magdagdag:
1. Persistent memory layer (hal., JSON lines append ng mga pag-uusap)
2. Simpleng evaluation rubric: factuality / clarity / style placeholders
3. Opsyonal na Chainlit front-end (dalawang tab: conversation & traces)
4. Opsyonal na LangGraph style state machine (kung magdadagdag ng dependency) para sa branching decisions

## Validation Checklist

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Asahan ang structured pipeline output na may tool injection note.

## Memory Strategies Overview

| Layer | Layunin | Halimbawa |
|-------|---------|-----------|
| Short-term | Pagpapatuloy ng dialogue | Huling N na mga mensahe |
| Episodic | Pag-alala sa session | JSON bawat session |
| Semantic | Pangmatagalang retrieval | Vector store ng mga buod |
| Scratchpad | Mga hakbang sa pag-iisip | Inline chain-of-thought (pribado) |

## Evaluation Hooks (Konseptwal)

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

| Isyu | Sanhi | Resolusyon |
|------|-------|-----------|
| Paulit-ulit na sagot | Context window masyadong malaki/maliit | I-tune ang memory window parameter |
| Tool hindi na-invoke | Mali ang syntax | Gamitin ang format na `#tool:tool_name` |
| Mabagal na orchestration | Maraming cold models | Pre-run warmup prompts |

## Mga Sanggunian

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (opsyonal na konsepto): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Tagal ng Session**: 30 min  
**Kahirapan**: Advanced

## Sample Scenario & Workshop Mapping

| Workshop Script | Scenario | Layunin | Halimbawa ng Prompt |
|-----------------|----------|---------|----------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Knowledge research bot na gumagawa ng executive-friendly summaries | Two-agent pipeline (research → editorial polish) na may opsyonal na distinct models | Ipaliwanag kung bakit mahalaga ang edge inference para sa compliance. |
| (Pinalawak) `tools.py` na konsepto | Magdagdag ng time & token estimation tools | Ipakita ang magaan na tool invocation pattern | #tool:get_time |

### Scenario Narrative

Ang compliance documentation team ay nangangailangan ng mabilis na internal briefs na sourced mula sa lokal na kaalaman nang hindi ipinapadala ang drafts sa cloud services. Ang researcher agent ay nangongolekta ng concise factual bullets; ang editor agent ay nagre-rewrite para sa executive clarity. Maaaring magtalaga ng distinct model aliases upang i-optimize ang latency (mabilis na SLM) vs stylistic refinement (mas malaking modelo kapag kinakailangan lamang).

### Halimbawa ng Multi-Model Environment

```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```


### Trace Structure (Opsyonal)

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

I-persist ang bawat hakbang sa isang JSONL file para sa rubric scoring sa hinaharap.

### Opsyonal na Mga Pagpapahusay

| Tema | Pagpapahusay | Benepisyo | Sketch ng Implementasyon |
|------|-------------|-----------|--------------------------|
| Multi-Model Roles | Distinct models bawat agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specialization & bilis | Piliin ang alias env vars, tawagin ang `chat_once` gamit ang per-role alias |
| Structured Traces | JSON trace ng bawat act(tool,input,latency,tokens) | Debug & evaluation | I-append ang dict sa isang list; isulat ang `.jsonl` sa dulo |
| Memory Persistence | Reloadable dialog context | Pagpapatuloy ng session | I-dump ang `Agent.memory` sa `sessions/<ts>.json` |
| Tool Registry | Dynamic tool discovery | Extensibility | Panatilihin ang `TOOLS` dict at i-introspect ang mga pangalan/desc |
| Retry & Backoff | Robust long chains | Bawasan ang transient failures | I-wrap ang `act` gamit ang try/except + exponential backoff |
| Rubric Scoring | Automated qualitative labels | Subaybayan ang mga pagpapabuti | Secondary pass prompting model: "Rate clarity 1-5" |
| Vector Memory | Semantic recall | Rich long-term context | Embed summaries, i-retrieve ang top-k sa system message |
| Streaming Replies | Mas mabilis na perceived response | UX improvement | Gamitin ang streaming kapag available at i-flush ang partial tokens |
| Deterministic Tests | Regression control | Stable CI | Patakbuhin gamit ang `temperature=0`, fixed prompt seeds |
| Parallel Branching | Mas mabilis na exploration | Throughput | Gamitin ang `concurrent.futures` para sa independent agent steps |

#### Halimbawa ng Trace Record

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Simpleng Evaluation Prompt

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

I-persist ang (`answer`, `rating`) pairs upang makabuo ng historical quality graph.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.