<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-09T21:15:11+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "lt"
}
-->
# 5 sesija: Greitas AI valdomų agentų kūrimas su Foundry Local

## Santrauka

Kurkite ir koordinuokite daugelio vaidmenų AI agentus, naudodami Foundry Local mažo delsos ir privatumo užtikrinimo vykdymo aplinką. Apibrėšite agentų vaidmenis, atminties strategijas, įrankių iškvietimo modelius ir vykdymo grafikus. Sesijoje bus pristatyti šablonai, kuriuos galėsite išplėsti naudodami Chainlit arba LangGraph. Pradinis projektas išplečia esamą agentų architektūros pavyzdį, pridedant atminties išsaugojimą ir vertinimo kabliukus.

## Mokymosi tikslai

- **Apibrėžti vaidmenis**: Sistemos raginimai ir galimybių ribos
- **Įgyvendinti atmintį**: Trumpalaikė (pokalbių), ilgalaikė (vektorinė / failų), laikina atmintis
- **Sukurti darbo eigas**: Sekos, šakotieji ir lygiagretūs agentų žingsniai
- **Integruoti įrankius**: Lengvas funkcijų įrankių iškvietimo modelis
- **Įvertinti**: Pagrindinis sekimo ir rezultatų vertinimas pagal rubriką

## Būtinos sąlygos

- Užbaigtos 1–4 sesijos
- Python su `foundry-local-sdk`, `openai`, pasirinktinai `chainlit`
- Vietiniai modeliai (bent jau `phi-4-mini`)

### Kryžminės platformos aplinkos fragmentas

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

Jei agentai vykdomi iš macOS prieš nuotolinę Windows paslaugą:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demonstracijos eiga (30 min)

### 1. Apibrėžkite agentų vaidmenis ir atmintį (7 min)

Sukurkite `samples/05-agents/agents_core.py`:

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


### 2. CLI šablono modelis (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Pridėkite įrankių iškvietimą (7 min)

Pratęskite su `samples/05-agents/tools.py`:

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

Pakeiskite `agents_core.py`, kad būtų leidžiama paprasta įrankių sintaksė: vartotojas rašo `#tool:get_time`, o agentas prieš generavimą įtraukia įrankio išvestį į kontekstą.

### 4. Koordinuota darbo eiga (6 min)

Sukurkite `samples/05-agents/orchestrator.py`:

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


### 5. Pradinis projektas: Išplėskite `05-agent-architecture` (7 min)

Pridėkite:
1. Nuolatinės atminties sluoksnį (pvz., JSON linijų pokalbių priedą)
2. Paprastą vertinimo rubriką: faktualumo / aiškumo / stiliaus vietos laikiklius
3. Pasirenkamą Chainlit sąsają (dvi kortelės: pokalbis ir sekimas)
4. Pasirenkamą LangGraph stiliaus būsenos mašiną (jei pridedama priklausomybė) šakotų sprendimų priėmimui

## Patikrinimo sąrašas

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Tikėkitės struktūrizuotos dujotiekio išvesties su įrankių įterpimo pastaba.

## Atminties strategijų apžvalga

| Sluoksnis | Tikslas | Pavyzdys |
|-----------|---------|----------|
| Trumpalaikė | Pokalbio tęstinumas | Paskutinės N žinutės |
| Epizodinė | Sesijos prisiminimas | JSON kiekvienai sesijai |
| Semantinė | Ilgalaikis atgaminimas | Santraukų vektorinė saugykla |
| Laikina atmintis | Mąstymo žingsniai | Vidinė mąstymo grandinė (privati) |

## Vertinimo kabliukai (koncepcija)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Trikčių šalinimas

| Problema | Priežastis | Sprendimas |
|----------|------------|------------|
| Pasikartojantys atsakymai | Per didelis / mažas konteksto langas | Sureguliuokite atminties lango parametrą |
| Įrankis neiškviečiamas | Neteisinga sintaksė | Naudokite `#tool:tool_name` formatą |
| Lėta koordinacija | Keli šaltieji modeliai | Iš anksto paleiskite šildymo raginimus |

## Nuorodos

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (pasirenkama koncepcija): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Sesijos trukmė**: 30 min  
**Sudėtingumas**: Pažengęs

## Pavyzdinė situacija ir dirbtuvių susiejimas

| Dirbtuvių scenarijus | Situacija | Tikslas | Pavyzdinis raginimas |
|-----------------------|-----------|---------|----------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Žinių tyrimų botas, kuriantis vadovams pritaikytas santraukas | Dviejų agentų dujotiekis (tyrimas → redakcinis tobulinimas) su pasirenkamais skirtingais modeliais | Paaiškinkite, kodėl kraštinis įžvalgos apdorojimas svarbus atitikties užtikrinimui. |
| (Išplėstas) `tools.py` konceptas | Pridėkite laiko ir žetonų skaičiavimo įrankius | Pademonstruokite lengvą įrankių iškvietimo modelį | #tool:get_time |

### Situacijos pasakojimas
Atitikties dokumentacijos komanda reikalauja greitų vidinių santraukų, gautų iš vietinių žinių, nesiunčiant juodraščių į debesų paslaugas. Tyrimų agentas surenka glaustus faktinius punktus; redaktoriaus agentas perrašo juos, kad būtų aiškiau vadovams. Gali būti priskirti skirtingi modelių pavadinimai, siekiant optimizuoti delsą (greitas SLM) ir stilistinį tobulinimą (didesnis modelis tik prireikus).

### Pavyzdinė kelių modelių aplinka
```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```


### Sekimo struktūra (pasirenkama)
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

Išsaugokite kiekvieną žingsnį JSONL faile, kad vėliau galėtumėte vertinti pagal rubriką.

### Pasirenkami patobulinimai

| Tema | Patobulinimas | Nauda | Įgyvendinimo eskizas |
|------|---------------|-------|-----------------------|
| Kelių modelių vaidmenys | Skirtingi modeliai kiekvienam agentui (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Specializacija ir greitis | Pasirinkite aplinkos kintamuosius, iškvieskite `chat_once` su kiekvieno vaidmens pavadinimu |
| Struktūrizuotas sekimas | JSON sekimas kiekvienam veiksmui (įrankis, įvestis, delsimas, žetonai) | Derinimas ir vertinimas | Pridėkite žodyną į sąrašą; rašykite `.jsonl` failą pabaigoje |
| Atminties išsaugojimas | Perkraunamas pokalbio kontekstas | Sesijos tęstinumas | Išsaugokite `Agent.memory` į `sessions/<ts>.json` |
| Įrankių registras | Dinaminis įrankių aptikimas | Išplėstinumą | Tvarkykite `TOOLS` žodyną ir tikrinkite pavadinimus / aprašymus |
| Pakartojimas ir atidėjimas | Patikimos ilgos grandinės | Sumažinkite laikinus gedimus | Apgaubkite `act` su try/except + eksponentiniu atidėjimu |
| Rubrikos vertinimas | Automatiniai kokybiniai įvertinimai | Stebėkite patobulinimus | Antrinis modelio raginimas: "Įvertinkite aiškumą 1-5" |
| Vektorinė atmintis | Semantinis atgaminimas | Turtingas ilgalaikis kontekstas | Įterpkite santraukas, atgaukite top-k į sisteminę žinutę |
| Srautinis atsakymas | Greitesnis suvokiamas atsakas | Vartotojo patirties gerinimas | Naudokite srautą, kai tik jis bus prieinamas, ir išvalykite dalinius žetonus |
| Determinuoti testai | Regresijos kontrolė | Stabilus CI | Paleiskite su `temperature=0`, fiksuotais raginimo sėklomis |
| Lygiagretus šakojimasis | Greitesnė analizė | Pralaidumas | Naudokite `concurrent.futures` nepriklausomiems agentų žingsniams |

#### Sekimo įrašo pavyzdys

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Paprastas vertinimo raginimas

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Išsaugokite (`atsakymas`, `įvertinimas`) poras, kad sukurtumėte istorinio kokybės grafiko.

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius naudojant šį vertimą.