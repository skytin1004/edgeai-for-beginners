<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-09T14:40:21+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "da"
}
-->
# Session 6: Foundry Local – Modeller som Værktøjer

## Resumé

Behandl modeller som sammensatte værktøjer i et lokalt AI-operativlag. Denne session viser, hvordan man kæder flere specialiserede SLM/LLM-kald sammen, ruter opgaver selektivt og eksponerer en samlet SDK-overflade til applikationer. Du vil bygge en letvægtsmodel-router + opgaveplanlægger, integrere den i et app-script og skitsere skaleringsvejen til Azure AI Foundry for produktionsarbejdsbelastninger.

## Læringsmål

- **Konceptualisere** modeller som atomare værktøjer med deklarerede kapaciteter
- **Rute** forespørgsler baseret på intention / heuristisk scoring
- **Kæde** output på tværs af flertrinsopgaver (dekomponere → løse → forfine)
- **Integrere** en samlet klient-API til downstream-applikationer
- **Skalere** design til skyen (samme OpenAI-kompatible kontrakt)

## Forudsætninger

- Sessioner 1–5 gennemført
- Flere lokale modeller cachet (f.eks. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Cross-Platform Miljøudsnit

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

Fjern-/VM-serviceadgang fra macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (30 min)

### 1. Deklaration af Værktøjskapacitet (5 min)

Opret `samples/06-tools/models_catalog.py`:

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


### 2. Intention Detektion & Routing (8 min)

Opret `samples/06-tools/router.py`:

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


### 3. Flertrinsopgavekædning (7 min)

Opret `samples/06-tools/pipeline.py`:

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


### 4. Startprojekt: Tilpas `06-models-as-tools` (5 min)

Forbedringer:
- Tilføj streaming-token support (progressiv UI-opdatering)
- Tilføj selvtillidsscore: leksikalsk overlap eller prompt-rubrik
- Eksporter trace JSON (intention → model → latenstid → tokenforbrug)
- Implementer cache-genbrug for gentagne deltrin

### 5. Skaleringsvej til Azure (5 min)

| Lag | Lokalt (Foundry) | Skyen (Azure AI Foundry) | Overgangsstrategi |
|-----|------------------|--------------------------|--------------------|
| Routing | Heuristisk Python | Holdbar mikrotjeneste | Containeriser & deploy API |
| Modeller | SLMs cachet | Administrerede deployment | Map lokale navne til deployment-ID'er |
| Observabilitet | CLI-statistik/manual | Central logning & metrikker | Tilføj strukturerede trace-events |
| Sikkerhed | Kun lokal vært | Azure-autentificering/netværk | Introducer key vault til hemmeligheder |
| Omkostninger | Enhedsressource | Forbrugsbaseret fakturering | Tilføj budgetbegrænsninger |

## Valideringscheckliste

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Forvent intention-baseret modelvalg og endeligt forfinet output.

## Fejlfinding

| Problem | Årsag | Løsning |
|---------|-------|---------|
| Alle opgaver rutet til samme model | Svage regler | Berig INTENT_RULES regex-sæt |
| Pipeline fejler midt i trin | Manglende model indlæst | Kør `foundry model run <model>` |
| Lav output-sammenhæng | Ingen forfiningsfase | Tilføj opsummerings-/valideringspassage |

## Referencer

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Promptkvalitetsmønstre: Se Session 2

---

**Sessionsvarighed**: 30 min  
**Sværhedsgrad**: Ekspert

## Eksempelscenarie & Workshopkortlægning

| Workshop-scripts / Notebooks | Scenarie | Mål | Datasæt / Katalogkilde |
|------------------------------|----------|-----|-------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Udviklerassistent håndterer blandede intention-prompter (refaktorere, opsummere, klassificere) | Heuristisk intention → modelalias-routing med tokenforbrug | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Flertrinsplanlægning & forfining for kompleks kodningsassistanceopgave | Dekomponere → specialiseret udførelse → opsummeringsforfiningstrin | Samme `CATALOG`; trin afledt af planoutput |

### Scenariefortælling
Et ingeniørproduktivitetværktøj modtager heterogene opgaver: refaktorere kode, opsummere arkitektoniske noter, klassificere feedback. For at minimere latenstid og ressourceforbrug planlægger og opsummerer en lille generel model, en kode-specialiseret model håndterer refaktorering, og en letvægtsklassifikationsmodel mærker feedback. Pipeline-scriptet demonstrerer kædning + forfining; router-scriptet isolerer adaptiv enkelt-prompt-routing.

### Katalogsnapshot
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Eksempeltestprompter
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Trace-udvidelse (Valgfrit)
Tilføj per-trin trace JSON-linjer for `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Eskaleringsheuristik (Idé)
Hvis planen indeholder nøgleord som "optimere", "sikkerhed" eller trinlængde > 280 tegn → eskaler til større model (f.eks. `gpt-oss-20b`) kun for det trin.

### Valgfrie Forbedringer

| Område | Forbedring | Værdi | Hint |
|-------|------------|-------|------|
| Caching | Genbrug manager + klientobjekter | Lavere latenstid, mindre overhead | Brug `workshop_utils.get_client` |
| Brugsmetrikker | Fang tokens & per-trin latenstid | Profilering & optimering | Tid hver rutet kald; gem i trace-liste |
| Adaptiv Routing | Selvtillid / omkostningsbevidst | Bedre kvalitet-omkostningsafvejning | Tilføj scoring: hvis prompt > N tegn eller regex matcher domæne → eskaler til større model |
| Dynamisk Kapacitetsregister | Hot reload katalog | Ingen genstart genudrulning | Indlæs `catalog.json` ved runtime; overvåg filens tidsstempel |
| Fallback-strategi | Robusthed under fejl | Højere tilgængelighed | Prøv primær → ved undtagelse fallback-alias |
| Streaming Pipeline | Tidlig feedback | UX-forbedring | Stream hvert trin og buffer endelig forfiningsinput |
| Vektorintention Embeddings | Mere nuanceret routing | Højere intentionsnøjagtighed | Embed prompt, cluster & map centroid → kapacitet |
| Trace-eksport | Auditerbar kæde | Overholdelse/rapportering | Udsend JSON-linjer: trin, intention, model, latenstid_ms, tokens |
| Omkostningssimulering | For-skyen estimering | Budgetplanlægning | Tildel notional omkostning/token per model & aggreger per opgave |
| Deterministisk Tilstand | Repro reproducerbarhed | Stabil benchmarking | Miljø: `temperature=0`, fast trinantal |

#### Eksempel på Trace-struktur

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Adaptiv Eskaleringsskitse

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Modelkatalog Hot Reload

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


Iterer gradvist—undgå overengineering af tidlige prototyper.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.