<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "94b65d49961cabc07f76062d09a5d09c",
  "translation_date": "2025-10-08T12:15:58+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "sl"
}
-->
# Seansa 6: Foundry Local – Modeli kot orodja

## Povzetek

Modeli so obravnavani kot sestavljiva orodja znotraj lokalne AI operativne plasti. V tej seansi se boste naučili, kako povezati več specializiranih klicev SLM/LLM, selektivno usmerjati naloge in aplikacijam omogočiti enotno SDK površino. Zgradili boste lahek usmerjevalnik modelov + načrtovalec nalog, ga integrirali v skripto aplikacije in začrtali pot za skaliranje na Azure AI Foundry za produkcijske obremenitve.

## Cilji učenja

- **Razumeti** modele kot osnovna orodja z deklariranimi zmožnostmi
- **Usmerjati** zahteve na podlagi namena / heurističnega točkovanja
- **Povezovati** rezultate skozi večstopenjske naloge (razčleniti → rešiti → izpopolniti)
- **Integrirati** enoten API za odjemalce za aplikacije
- **Skalirati** zasnovo v oblak (enaka pogodba, združljiva z OpenAI)

## Predpogoji

- Zaključene seanse 1–5
- Več lokalnih modelov v predpomnilniku (npr. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Izsek za večplatformsko okolje

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

Dostop do oddaljene storitve/VM iz macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Potek demonstracije (30 min)

### 1. Deklaracija zmožnosti orodij (5 min)

Ustvarite `samples/06-tools/models_catalog.py`:

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


### 2. Zaznavanje namena in usmerjanje (8 min)

Ustvarite `samples/06-tools/router.py`:

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


### 3. Povezovanje večstopenjskih nalog (7 min)

Ustvarite `samples/06-tools/pipeline.py`:

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


### 4. Začetni projekt: Prilagodite `06-models-as-tools` (5 min)

Izboljšave:
- Dodajte podporo za pretakanje tokenov (postopna posodobitev uporabniškega vmesnika)
- Dodajte točkovanje zaupanja: leksikalno prekrivanje ali rubriko poziva
- Izvozite sled JSON (namen → model → zakasnitev → uporaba tokenov)
- Implementirajte ponovno uporabo predpomnilnika za ponavljajoče se podkorake

### 5. Pot do skaliranja na Azure (5 min)

| Plast | Lokalno (Foundry) | Oblačno (Azure AI Foundry) | Strategija prehoda |
|-------|-------------------|---------------------------|---------------------|
| Usmerjanje | Heuristični Python | Trajnostna mikrostoritev | Kontejnerizirajte in uvedite API |
| Modeli | Predpomnjeni SLM-ji | Upravljane uvedbe | Preslikajte lokalna imena v ID-je uvedb |
| Opazovanje | Statistika CLI/ročna | Centralizirano beleženje in meritve | Dodajte strukturirane dogodke sledenja |
| Varnost | Samo lokalni gostitelj | Azure avtentikacija / omrežje | Uvedite ključni trezor za skrivnosti |
| Stroški | Viri naprave | Obračunavanje porabe | Dodajte varovalke za proračun |

## Preveritveni seznam za validacijo

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Pričakujte izbiro modela na podlagi namena in končni izpopolnjeni rezultat.

## Odpravljanje težav

| Težava | Vzrok | Rešitev |
|--------|-------|---------|
| Vse naloge so usmerjene na isti model | Slaba pravila | Obogatite niz regex INTENT_RULES |
| Cevovod se ustavi na sredini koraka | Manjka naložen model | Zaženite `foundry model run <model>` |
| Nizka kohezija rezultatov | Brez faze izpopolnjevanja | Dodajte povzetek/preverjanje |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Docs: https://learn.microsoft.com/azure/ai-foundry
- Vzorci kakovosti pozivov: Glejte seanso 2

---

**Trajanje seanse**: 30 min  
**Težavnost**: Strokovno

## Vzorec scenarija in preslikava delavnice

| Skripte / Beležnice delavnice | Scenarij | Cilj | Vir podatkov / Katalog |
|-------------------------------|----------|------|-------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Pomočnik razvijalca, ki obravnava mešane pozive glede namena (preoblikovanje, povzemanje, razvrščanje) | Heuristični namen → usmerjanje modela z uporabo tokenov | Vgrajen `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Večstopenjsko načrtovanje in izpopolnjevanje za kompleksno nalogo pomoči pri kodiranju | Razčlenitev → specializirana izvedba → korak povzetka in izpopolnjevanja | Isti `CATALOG`; koraki izpeljani iz izhoda načrta |

### Pripoved scenarija
Orodje za povečanje produktivnosti inženirjev prejema heterogene naloge: preoblikovanje kode, povzemanje arhitekturnih zapiskov, razvrščanje povratnih informacij. Za zmanjšanje zakasnitve in porabe virov majhen splošni model načrtuje in povzame, model, specializiran za kodo, obravnava preoblikovanje, lahek model za razvrščanje pa označuje povratne informacije. Skripta cevovoda prikazuje povezovanje + izpopolnjevanje; skripta usmerjevalnika izolira prilagodljivo usmerjanje posameznih pozivov.

### Posnetek kataloga
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Primeri testnih pozivov
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Razširitev sledenja (neobvezno)
Dodajte sledenje JSON po korakih za `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Heuristika za eskalacijo (ideja)
Če načrt vsebuje ključne besede, kot so "optimizacija", "varnost" ali dolžina koraka > 280 znakov → eskalirajte na večji model (npr. `gpt-oss-20b`) samo za ta korak.

### Neobvezne izboljšave

| Področje | Izboljšava | Vrednost | Namig |
|----------|------------|----------|-------|
| Predpomnjenje | Ponovna uporaba upravitelja + odjemalcev | Nižja zakasnitev, manjša obremenitev | Uporabite `workshop_utils.get_client` |
| Meritve uporabe | Zajemanje tokenov in zakasnitve po korakih | Profiliranje in optimizacija | Izmerite vsak usmerjen klic; shranite v seznam sledenja |
| Prilagodljivo usmerjanje | Zavedanje zaupanja / stroškov | Boljša kakovost-stroškovna učinkovitost | Dodajte točkovanje: če je poziv > N znakov ali regex ustreza področju → eskalirajte na večji model |
| Dinamični register zmožnosti | Vroče nalaganje kataloga | Brez ponovnega zagona uvedbe | Naložite `catalog.json` med izvajanjem; spremljajte časovni žig datoteke |
| Strategija rezervnega načrta | Robustnost pri napakah | Večja razpoložljivost | Poskusite primarno → ob izjemi rezervni vzdevek |
| Pretakanje cevovoda | Zgodnje povratne informacije | Izboljšanje uporabniške izkušnje | Pretakajte vsak korak in medpomnite končni vhod za izpopolnjevanje |
| Vektorske vdelave namena | Bolj natančno usmerjanje | Višja natančnost namena | Vdelajte poziv, združite in preslikajte težišče → zmožnost |
| Izvoz sledenja | Verižna revizija | Skladnost/poročanje | Oddajte JSON vrstice: korak, namen, model, zakasnitev_ms, tokeni |
| Simulacija stroškov | Ocena pred oblakom | Načrtovanje proračuna | Dodelite notionalne stroške/token na model in jih združite po nalogi |
| Deterministični način | Reproducibilnost | Stabilno primerjanje | Okolje: `temperature=0`, fiksno število korakov |

#### Primer strukture sledenja

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Skica prilagodljive eskalacije

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Vroče nalaganje kataloga modelov

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


Postopoma iterirajte—izogibajte se pretiranemu inženiringu v zgodnjih prototipih.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.