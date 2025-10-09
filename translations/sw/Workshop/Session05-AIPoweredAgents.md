<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-09T21:12:56+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "sw"
}
-->
# Kipindi cha 5: Jenga Mawakala Wenye Nguvu za AI Haraka kwa Kutumia Foundry Local

## Muhtasari

Buni na ratibu mawakala wa AI wenye majukumu mbalimbali kwa kutumia Foundry Local, ambayo ina muda wa majibu wa chini na inahifadhi faragha. Utatambua majukumu ya mawakala, mikakati ya kumbukumbu, mifumo ya kuitisha zana, na grafu za utekelezaji. Kipindi hiki kinaanzisha mifumo ya msingi ambayo unaweza kupanua kwa kutumia Chainlit au LangGraph. Mradi wa kuanzia unapanua sampuli ya usanifu wa mawakala iliyopo ili kuongeza uhifadhi wa kumbukumbu + ndoano za tathmini.

## Malengo ya Kujifunza

- **Tambua Majukumu**: Maelekezo ya mfumo & mipaka ya uwezo
- **Tekeleza Kumbukumbu**: Muda mfupi (mazungumzo), muda mrefu (vector / faili), scratchpads za muda mfupi
- **Buni Mifumo ya Kazi**: Hatua za mawakala za mfululizo, matawi, na sambamba
- **Unganisha Zana**: Mfano mwepesi wa kuitisha zana kwa kutumia kazi
- **Tathmini**: Ufuatiliaji wa msingi + upimaji wa matokeo kwa kutumia rubriki

## Mahitaji ya Awali

- Vipindi 1–4 vimekamilika
- Python na `foundry-local-sdk`, `openai`, `chainlit` (hiari)
- Miundo ya ndani inayoendesha (angalau `phi-4-mini`)

### Kipande cha Mazingira ya Msalaba

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

Ikiwa unaendesha mawakala kutoka macOS dhidi ya huduma ya mwenyeji ya Windows ya mbali:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Mtiririko wa Demo (Dakika 30)

### 1. Tambua Majukumu ya Mawakala & Kumbukumbu (Dakika 7)

Unda `samples/05-agents/agents_core.py`:

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


### 2. Mfano wa Msingi wa CLI (Dakika 3)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Ongeza Kuitisha Zana (Dakika 7)

Panua kwa kutumia `samples/05-agents/tools.py`:

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

Badilisha `agents_core.py` ili kuruhusu sintaksia rahisi ya zana: mtumiaji aandike `#tool:get_time` na wakala aongeze matokeo ya zana kwenye muktadha kabla ya kizazi.

### 4. Mtiririko wa Kazi Ulioandaliwa (Dakika 6)

Unda `samples/05-agents/orchestrator.py`:

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


### 5. Mradi wa Kuanzia: Panua `05-agent-architecture` (Dakika 7)

Ongeza:
1. Safu ya kumbukumbu ya kudumu (mfano, kuongeza mistari ya JSON ya mazungumzo)
2. Rubriki rahisi ya tathmini: ukweli / uwazi / mitindo
3. Chainlit ya mbele (hiari) (vichupo viwili: mazungumzo & ufuatiliaji)
4. Mashine ya hali ya mtindo wa LangGraph (hiari ikiwa unaongeza utegemezi) kwa maamuzi ya matawi

## Orodha ya Ukaguzi wa Uthibitishaji

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Tegemea matokeo ya mtiririko wa kazi yaliyo na maelezo ya kuingiza zana.

## Muhtasari wa Mikakati ya Kumbukumbu

| Safu | Kusudi | Mfano |
|------|--------|-------|
| Muda mfupi | Mwendelezo wa mazungumzo | Ujumbe N za mwisho |
| Kipindi | Kumbukumbu ya kikao | JSON kwa kila kikao |
| Semantiki | Urejeshaji wa muda mrefu | Hifadhi ya vector ya muhtasari |
| Scratchpad | Hatua za kufikiri | Mnyororo wa mawazo wa ndani (binafsi) |

## Ndoano za Tathmini (Kifupi)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Utatuzi wa Matatizo

| Tatizo | Sababu | Suluhisho |
|--------|--------|-----------|
| Majibu yanayojirudia | Dirisha la muktadha kubwa sana/ndogo sana | Rekebisha parameta ya dirisha la kumbukumbu |
| Zana haijaitishwa | Sintaksia isiyo sahihi | Tumia muundo `#tool:tool_name` |
| Uratibu wa polepole | Miundo mingi baridi | Tumia maelekezo ya joto kabla ya kuanza |

## Marejeleo

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (dhana ya hiari): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Muda wa Kipindi**: Dakika 30  
**Ugumu**: Juu

## Mfano wa Hali & Ulinganisho wa Warsha

| Script ya Warsha | Hali | Lengo | Mfano wa Maelekezo |
|------------------|------|-------|--------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot ya utafiti wa maarifa inayozalisha muhtasari unaofaa kwa watendaji | Mtiririko wa mawakala wawili (utafiti → uhariri wa kitaalamu) na miundo tofauti ya hiari | Eleza kwa nini utambuzi wa ukingo ni muhimu kwa kufuata sheria. |
| (Imepanuliwa) dhana ya `tools.py` | Ongeza zana za muda & makadirio ya tokeni | Onyesha mfano mwepesi wa kuitisha zana | #tool:get_time |

### Simulizi ya Hali
Timu ya nyaraka za kufuata inahitaji muhtasari wa haraka wa ndani unaotokana na maarifa ya ndani bila kutuma rasimu kwa huduma za wingu. Wakala wa utafiti hukusanya pointi za ukweli kwa ufupi; wakala wa mhariri huandika upya kwa uwazi wa watendaji. Miundo tofauti inaweza kutengwa ili kuboresha muda wa majibu (SLM ya haraka) dhidi ya uboreshaji wa mitindo (muundo mkubwa tu inapohitajika).

### Mfano wa Mazingira ya Miundo Mingi
```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```


### Muundo wa Ufuatiliaji (Hiari)
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

Hifadhi kila hatua kwenye faili ya JSONL kwa upimaji wa rubriki baadaye.

### Uboreshaji wa Hiari

| Mada | Uboreshaji | Faida | Mfano wa Utekelezaji |
|------|-----------|-------|---------------------|
| Majukumu ya Miundo Mingi | Miundo tofauti kwa kila wakala (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Utaalamu & kasi | Chagua env vars za alias, piga `chat_once` na alias kwa kila jukumu |
| Ufuatiliaji Ulioandaliwa | Ufuatiliaji wa JSON wa kila hatua (zana, pembejeo, muda wa majibu, tokeni) | Ufuatiliaji & tathmini | Ongeza kamusi kwenye orodha; andika `.jsonl` mwishoni |
| Uhifadhi wa Kumbukumbu | Muktadha wa mazungumzo unaoweza kupakiwa tena | Mwendelezo wa kikao | Hifadhi `Agent.memory` kwenye `sessions/<ts>.json` |
| Usajili wa Zana | Ugunduzi wa zana wa nguvu | Uwezo wa kupanua | Dhibiti kamusi ya `TOOLS` na angalia majina/maelezo |
| Jaribu Tena & Rudisha Nyuma | Mnyororo mrefu wenye nguvu | Punguza kushindwa kwa muda mfupi | Funga `act` na jaribu/except + rudisha nyuma kwa kasi |
| Upimaji wa Rubriki | Lebo za ubora za kiotomatiki | Fuatilia maboresho | Pasi ya pili ya kuomba muundo: "Pima uwazi 1-5" |
| Kumbukumbu ya Vector | Urejeshaji wa semantiki | Muktadha wa muda mrefu wenye utajiri | Ingiza muhtasari, rejesha juu-k katika ujumbe wa mfumo |
| Majibu ya Kutiririka | Majibu ya haraka yanayoonekana | Uboreshaji wa UX | Tumia kutiririka mara tu inapatikana na toa tokeni za sehemu |
| Majaribio ya Kiamua | Udhibiti wa kurudi nyuma | CI thabiti | Endesha na `temperature=0`, mbegu za maelekezo zilizowekwa |
| Matawi Sambamba | Uchunguzi wa haraka | Uwezo wa kazi | Tumia `concurrent.futures` kwa hatua huru za wakala |

#### Mfano wa Rekodi ya Ufuatiliaji

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Maelekezo Rahisi ya Tathmini

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Hifadhi jozi (`answer`, `rating`) ili kujenga grafu ya ubora wa kihistoria.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.