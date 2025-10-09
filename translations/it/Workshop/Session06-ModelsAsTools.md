<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-09T11:02:09+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "it"
}
-->
# Sessione 6: Foundry Local – Modelli come Strumenti

## Abstract

Tratta i modelli come strumenti componibili all'interno di un livello operativo AI locale. Questa sessione mostra come concatenare chiamate multiple a SLM/LLM specializzati, instradare selettivamente i compiti e offrire una superficie SDK unificata alle applicazioni. Costruirai un router di modelli leggero + un pianificatore di compiti, lo integrerai in uno script applicativo e delineerai il percorso di scalabilità verso Azure AI Foundry per carichi di lavoro in produzione.

## Obiettivi di Apprendimento

- **Concettualizzare** i modelli come strumenti atomici con capacità dichiarate
- **Instradare** richieste basate su intenti / punteggi euristici
- **Concatenare** output attraverso compiti multi-step (decomporre → risolvere → affinare)
- **Integrare** un'API client unificata per applicazioni downstream
- **Scalare** il design al cloud (stesso contratto compatibile con OpenAI)

## Prerequisiti

- Completamento delle sessioni 1–5
- Molteplici modelli locali memorizzati nella cache (es. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Snippet Ambiente Cross-Platform

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

Accesso remoto/VM da macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Flusso Demo (30 min)

### 1. Dichiarazione delle Capacità degli Strumenti (5 min)

Crea `samples/06-tools/models_catalog.py`:

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


### 2. Rilevamento Intenti & Instradamento (8 min)

Crea `samples/06-tools/router.py`:

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


### 3. Concatenazione di Compiti Multi-Step (7 min)

Crea `samples/06-tools/pipeline.py`:

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


### 4. Progetto Iniziale: Adatta `06-models-as-tools` (5 min)

Miglioramenti:
- Aggiungi supporto per token in streaming (aggiornamento UI progressivo)
- Aggiungi punteggio di fiducia: sovrapposizione lessicale o rubriche di prompt
- Esporta JSON di traccia (intento → modello → latenza → utilizzo token)
- Implementa il riutilizzo della cache per sottopassi ripetuti

### 5. Percorso di Scalabilità verso Azure (5 min)

| Livello | Locale (Foundry) | Cloud (Azure AI Foundry) | Strategia di Transizione |
|--------|------------------|--------------------------|--------------------------|
| Instradamento | Python euristico | Microservizio durevole | Containerizza e distribuisci API |
| Modelli | SLM memorizzati nella cache | Deployment gestiti | Mappa i nomi locali agli ID di deployment |
| Osservabilità | Statistiche CLI/manuale | Logging centrale & metriche | Aggiungi eventi di traccia strutturati |
| Sicurezza | Solo host locale | Autenticazione Azure / networking | Introduci key vault per segreti |
| Costo | Risorse del dispositivo | Fatturazione a consumo | Aggiungi limiti di budget |

## Checklist di Validazione

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Aspettati selezione del modello basata su intenti e output finale affinato.

## Risoluzione dei Problemi

| Problema | Causa | Soluzione |
|----------|-------|----------|
| Tutti i compiti instradati allo stesso modello | Regole deboli | Arricchisci il set regex INTENT_RULES |
| La pipeline fallisce a metà passo | Modello non caricato | Esegui `foundry model run <model>` |
| Bassa coesione dell'output | Nessuna fase di affinamento | Aggiungi passaggio di sintesi/validazione |

## Riferimenti

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentazione Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Pattern di Qualità dei Prompt: Vedi Sessione 2

---

**Durata della Sessione**: 30 min  
**Difficoltà**: Esperto

## Scenario di Esempio & Mappatura Workshop

| Script Workshop / Notebook | Scenario | Obiettivo | Fonte Dataset / Catalogo |
|----------------------------|----------|-----------|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Assistente per sviluppatori che gestisce prompt con intenti misti (rifattorizzare, sintetizzare, classificare) | Intento euristico → instradamento alias modello con utilizzo token | Inline `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Pianificazione multi-step & affinamento per compiti complessi di assistenza alla codifica | Decomporre → esecuzione specializzata → passaggio di sintesi e affinamento | Stesso `CATALOG`; passi derivati dall'output del piano |

### Narrazione dello Scenario
Uno strumento di produttività ingegneristica riceve compiti eterogenei: rifattorizzare codice, sintetizzare note architetturali, classificare feedback. Per minimizzare latenza e utilizzo delle risorse, un piccolo modello generale pianifica e sintetizza, un modello specializzato per il codice gestisce la rifattorizzazione, e un modello leggero per la classificazione etichetta il feedback. Lo script della pipeline dimostra concatenazione + affinamento; lo script del router isola l'instradamento adattivo di singoli prompt.

### Snapshot del Catalogo
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Esempi di Prompt di Test
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Estensione Traccia (Opzionale)
Aggiungi linee JSON di traccia per ogni passo in `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Euristica di Escalation (Idea)
Se il piano contiene parole chiave come "ottimizzare", "sicurezza", o la lunghezza del passo > 280 caratteri → scala a un modello più grande (es. `gpt-oss-20b`) solo per quel passo.

### Miglioramenti Opzionali

| Area | Miglioramento | Valore | Suggerimento |
|------|--------------|--------|-------------|
| Caching | Riutilizza oggetti manager + client | Minore latenza, meno overhead | Usa `workshop_utils.get_client` |
| Metriche di Utilizzo | Cattura token & latenza per passo | Profilazione & ottimizzazione | Cronometra ogni chiamata instradata; memorizza nella lista di traccia |
| Instradamento Adattivo | Consapevole di fiducia / costo | Migliore trade-off qualità-costo | Aggiungi punteggio: se il prompt > N caratteri o regex corrisponde al dominio → scala a modello più grande |
| Registro Dinamico delle Capacità | Catalogo hot reload | Nessun riavvio o ridistribuzione | Carica `catalog.json` a runtime; osserva timestamp del file |
| Strategia di Fallback | Robustezza in caso di fallimenti | Maggiore disponibilità | Prova primario → su eccezione fallback alias |
| Pipeline Streaming | Feedback anticipato | Miglioramento UX | Stream ogni passo e buffer input finale di affinamento |
| Intent Embedding Vettoriale | Instradamento più sfumato | Maggiore accuratezza degli intenti | Incorpora prompt, cluster & mappa il centroide → capacità |
| Esportazione Traccia | Catena auditabile | Conformità/reportistica | Emetti linee JSON: passo, intento, modello, latenza_ms, token |
| Simulazione Costo | Stima pre-cloud | Pianificazione budget | Assegna costo notionale/token per modello & aggrega per compito |
| Modalità Deterministica | Riproducibilità | Benchmarking stabile | Env: `temperature=0`, numero fisso di passi |

#### Esempio Struttura Traccia

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Schizzo Escalation Adattiva

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Hot Reload Catalogo Modelli

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


Itera gradualmente—evita di sovra-ingegnerizzare i prototipi iniziali.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.