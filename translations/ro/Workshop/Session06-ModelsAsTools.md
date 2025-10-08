<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-08T15:26:58+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "ro"
}
-->
# Sesiunea 6: Foundry Local – Modele ca Instrumente

## Rezumat

Tratează modelele ca instrumente compozabile într-un strat operațional AI local. Această sesiune arată cum să conectezi mai multe apeluri SLM/LLM specializate, să rutezi selectiv sarcinile și să expui o suprafață SDK unificată pentru aplicații. Vei construi un router de modele ușor + un planificator de sarcini, îl vei integra într-un script de aplicație și vei schița calea de scalare către Azure AI Foundry pentru sarcini de producție.

## Obiective de Învățare

- **Conceptualizează** modelele ca instrumente atomice cu capabilități declarate
- **Rutează** cererile pe baza intenției / scorării euristice
- **Conectează** ieșirile în sarcini multi-pas (decompoziție → rezolvare → rafinare)
- **Integrează** un API client unificat pentru aplicațiile downstream
- **Scalează** designul către cloud (același contract compatibil OpenAI)

## Cerințe Prealabile

- Finalizarea sesiunilor 1–5
- Mai multe modele locale cache-uite (ex.: `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Fragment de Mediu Cross-Platform

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

Acces la servicii remote/VM de pe macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Flux Demo (30 min)

### 1. Declarația Capabilităților Instrumentelor (5 min)

Creează `samples/06-tools/models_catalog.py`:

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


### 2. Detectarea Intenției și Rutare (8 min)

Creează `samples/06-tools/router.py`:

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


### 3. Conectarea Sarcinilor Multi-Pas (7 min)

Creează `samples/06-tools/pipeline.py`:

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


### 4. Proiect de Start: Adaptarea `06-models-as-tools` (5 min)

Îmbunătățiri:
- Adaugă suport pentru streaming de tokeni (actualizare progresivă UI)
- Adaugă scorare de încredere: suprapunere lexicală sau rubrică de prompt
- Exportă trace JSON (intenție → model → latență → utilizare tokeni)
- Implementează reutilizarea cache-ului pentru subpași repetați

### 5. Calea de Scalare către Azure (5 min)

| Strat | Local (Foundry) | Cloud (Azure AI Foundry) | Strategie de Tranziție |
|-------|-----------------|--------------------------|-------------------------|
| Rutare | Python euristic | Microserviciu durabil | Containerizează și implementează API |
| Modele | SLM-uri cache-uite | Implementări gestionate | Mapează numele locale la ID-uri de implementare |
| Observabilitate | Statistici CLI/manual | Logare centrală & metrici | Adaugă evenimente structurate de trace |
| Securitate | Doar host local | Autentificare Azure / rețea | Introdu key vault pentru secrete |
| Cost | Resurse dispozitiv | Facturare consum | Adaugă limite de buget |

## Lista de Verificare pentru Validare

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Așteaptă selecția modelului bazată pe intenție și ieșirea finală rafinată.

## Depanare

| Problemă | Cauză | Soluție |
|----------|-------|---------|
| Toate sarcinile rutate către același model | Reguli slabe | Îmbunătățește setul regex INTENT_RULES |
| Pipeline-ul eșuează la mijlocul unui pas | Model lipsă încărcat | Rulează `foundry model run <model>` |
| Coeziune scăzută a ieșirii | Fază de rafinare lipsă | Adaugă un pas de sumarizare/validare |

## Referințe

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentație Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Modele de Calitate Prompt: Vezi Sesiunea 2

---

**Durata Sesiunii**: 30 min  
**Dificultate**: Expert

## Scenariu Exemplu & Mapare Workshop

| Scripturi / Notebook-uri Workshop | Scenariu | Obiectiv | Sursă Dataset / Catalog |
|-----------------------------------|----------|----------|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Asistent pentru dezvoltatori care gestionează prompturi cu intenții mixte (refactorizare, sumarizare, clasificare) | Rutare euristică intenție → alias model cu utilizare tokeni | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Planificare multi-pas & rafinare pentru o sarcină complexă de asistență la codare | Decompoziție → execuție specializată → pas de rafinare sumarizare | Același `CATALOG`; pași derivați din ieșirea planului |

### Narațiunea Scenariului
Un instrument de productivitate pentru inginerie primește sarcini eterogene: refactorizare cod, sumarizare note arhitecturale, clasificare feedback. Pentru a minimiza latența și utilizarea resurselor, un model general mic planifică și sumarizează, un model specializat pe cod gestionează refactorizarea, iar un model ușor capabil de clasificare etichetează feedback-ul. Scriptul pipeline demonstrează conectarea + rafinarea; scriptul router izolează rutarea adaptivă a unui singur prompt.

### Snapshot Catalog
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Exemple de Prompturi de Test
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Extensie Trace (Opțional)
Adaugă linii JSON de trace per-pas pentru `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Euristică de Escalare (Idee)
Dacă planul conține cuvinte cheie precum "optimize", "security" sau lungimea pasului > 280 caractere → escaladează la un model mai mare (ex.: `gpt-oss-20b`) doar pentru acel pas.

### Îmbunătățiri Opționale

| Zonă | Îmbunătățire | Valoare | Indicație |
|------|--------------|---------|-----------|
| Cache | Reutilizarea managerului + obiectelor client | Latență mai mică, mai puțin overhead | Folosește `workshop_utils.get_client` |
| Metrici de Utilizare | Capturarea tokenilor & latenței per-pas | Profilare & optimizare | Cronometrează fiecare apel rutat; stochează în lista de trace |
| Rutare Adaptivă | Conștientă de încredere / cost | Compromis calitate-cost mai bun | Adaugă scorare: dacă promptul > N caractere sau regex-ul se potrivește domeniului → escaladează la un model mai mare |
| Registru Dinamic de Capabilități | Catalog reload dinamic | Fără redeploy restart | Încarcă `catalog.json` la runtime; urmărește timestamp-ul fișierului |
| Strategie de Fallback | Robusteză în caz de eșecuri | Disponibilitate mai mare | Încearcă primar → pe excepție fallback alias |
| Pipeline Streaming | Feedback timpuriu | Îmbunătățire UX | Stream fiecare pas și buffer pentru intrarea finală de rafinare |
| Embedding-uri Vectoriale de Intenție | Rutare mai nuanțată | Acuratețe mai mare a intenției | Embedează promptul, grupează & mapează centroidul → capabilitate |
| Export Trace | Lanț auditabil | Conformitate/raportare | Emet JSON linii: pas, intenție, model, latență_ms, tokeni |
| Simulare Cost | Estimare pre-cloud | Planificare buget | Atribuie cost noțional/token per model & agregă per sarcină |
| Mod Determinist | Reproducibilitate | Benchmarking stabil | Env: `temperature=0`, număr fix de pași |

#### Exemplu Structură Trace

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Schiță Escalare Adaptivă

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Reload Dinamic Catalog Model

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


Iterează treptat—evită supra-ingineria prototipurilor timpurii.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.