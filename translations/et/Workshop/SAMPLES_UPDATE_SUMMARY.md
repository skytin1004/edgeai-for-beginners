<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-11T12:02:07+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "et"
}
-->
# Workshopi Näidised - Foundry Local SDK Uuenduste Kokkuvõte

## Ülevaade

Kõik Python-näidised kataloogis `Workshop/samples` on uuendatud, et järgida Foundry Local SDK parimaid tavasid ja tagada järjepidevus kogu workshopi ulatuses.

**Kuupäev**: 8. oktoober 2025  
**Ulatus**: 9 Python-faili 6 workshopi sessioonis  
**Peamine Fookus**: Vigade käsitlemine, dokumentatsioon, SDK mustrid, kasutajakogemus

---

## Uuendatud Failid

### Sessioon 01: Alustamine
- ✅ `chat_bootstrap.py` - Põhilised vestluse ja voogesituse näited

### Sessioon 02: RAG Lahendused
- ✅ `rag_pipeline.py` - RAG-i rakendamine koos sisseehitustega
- ✅ `rag_eval_ragas.py` - RAG-i hindamine RAGAS-i mõõdikutega

### Sessioon 03: Avatud Lähtekoodiga Mudelid
- ✅ `benchmark_oss_models.py` - Mitme mudeli võrdlus

### Sessioon 04: Tipptasemel Mudelid
- ✅ `model_compare.py` - SLM vs LLM võrdlus

### Sessioon 05: AI-põhised Agendid
- ✅ `agents_orchestrator.py` - Mitme agendi koordineerimine

### Sessioon 06: Mudelid Tööriistadena
- ✅ `models_router.py` - Kavatsusepõhine mudelite suunamine
- ✅ `models_pipeline.py` - Mitmeastmeline suunatud torustik

### Tugistruktuur
- ✅ `workshop_utils.py` - Juba järgib parimaid tavasid (muudatusi ei tehtud)

---

## Peamised Parandused

### 1. Täiustatud Vigade Käsitlemine

**Enne:**
```python
manager, client, model_id = get_client(alias)
```

**Pärast:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Eelised:**
- Sujuv vigade käsitlemine selgete veateadetega
- Tegutsemiseks vajalikud vihjed
- Skriptide jaoks sobivad väljumiskoodid

### 2. Parem Impordi Haldamine

**Enne:**
```python
from sentence_transformers import SentenceTransformer
```

**Pärast:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Eelised:**
- Selged juhised, kui sõltuvused puuduvad
- Väldib segaseid impordivigu
- Kasutajasõbralikud paigaldusjuhised

### 3. Põhjalik Dokumentatsioon

**Lisatud kõigile näidistele:**
- Keskkonnamuutujate dokumentatsioon docstringides
- SDK viited
- Kasutusnäited
- Üksikasjalik funktsioonide/parameetrite dokumentatsioon
- Tüüpide vihjed parema IDE toe jaoks

**Näide:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Parendatud Kasutajate Tagasiside

**Lisatud informatiivne logimine:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Edenemise indikaatorid:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Struktureeritud väljund:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Tugev Võrdlus

**Sessioon 03 parandused:**
- Mudelipõhine vigade käsitlemine (jätkab ebaõnnestumise korral)
- Üksikasjalik edenemise aruandlus
- Soojendusringid korralikult teostatud
- Esimese märgi latentsuse mõõtmise tugi
- Etappide selge eristamine

### 6. Järjepidevad Tüüpide Vihjed

**Lisatud kõikjal:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Eelised:**
- Parem IDE automaatne täitmine
- Varajane vigade tuvastamine
- Ise dokumenteeriv kood

### 7. Täiustatud Mudelite Suunaja

**Sessioon 06 parandused:**
- Põhjalik kavatsuste tuvastamise dokumentatsioon
- Mudeli valiku algoritmi selgitus
- Üksikasjalikud suunamislogid
- Testi väljundi vormindamine
- Vigade taastamine partiitestides

### 8. Mitme Agendi Orkestreerimine

**Sessioon 05 parandused:**
- Etappide kaupa edenemise aruandlus
- Agendipõhine vigade käsitlemine
- Selge torustiku struktuur
- Parem mäluhalduse dokumentatsioon

---

## Testimise Kontrollnimekiri

### Eeltingimused
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testi Iga Näidis

#### Sessioon 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### Sessioon 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### Sessioon 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### Sessioon 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### Sessioon 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### Sessioon 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## Keskkonnamuutujate Viited

### Üldine (Kõik Näidised)
| Muutuja | Kirjeldus | Vaikimisi |
|---------|-----------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | Kasutatav mudeli alias | Erinev näidise järgi |
| `FOUNDRY_LOCAL_ENDPOINT` | Teenuse lõpp-punkti ülekirjutamine | Automaatne tuvastamine |
| `SHOW_USAGE` | Näita tokenite kasutust | `0` |
| `RETRY_ON_FAIL` | Luba uuesti proovimise loogika | `1` |
| `RETRY_BACKOFF` | Esialgne uuesti proovimise viivitus | `1.0` |

### Näidise Spetsiifiline
| Muutuja | Kasutaja | Kirjeldus |
|---------|----------|-----------|
| `EMBED_MODEL` | Sessioon 02 | Sisseehituse mudeli nimi |
| `RAG_QUESTION` | Sessioon 02 | Testküsimus RAG-i jaoks |
| `BENCH_MODELS` | Sessioon 03 | Komaga eraldatud mudelid võrdluseks |
| `BENCH_ROUNDS` | Sessioon 03 | Võrdlusringide arv |
| `BENCH_PROMPT` | Sessioon 03 | Testi küsimus võrdluseks |
| `BENCH_STREAM` | Sessioon 03 | Esimese märgi latentsuse mõõtmine |
| `SLM_ALIAS` | Sessioon 04 | Väike keelemudel |
| `LLM_ALIAS` | Sessioon 04 | Suur keelemudel |
| `COMPARE_PROMPT` | Sessioon 04 | Võrdluse testküsimus |
| `AGENT_MODEL_PRIMARY` | Sessioon 05 | Peamine agendi mudel |
| `AGENT_MODEL_EDITOR` | Sessioon 05 | Toimetaja agendi mudel |
| `AGENT_QUESTION` | Sessioon 05 | Testküsimus agentidele |
| `PIPELINE_TASK` | Sessioon 06 | Torustiku ülesanne |

---

## Muutused, Mis Võivad Funktsionaalsust Mõjutada

**Puuduvad** - Kõik muudatused on tagasiühilduvad.

Olemasolevad skriptid töötavad edasi. Uued funktsioonid on:
- Valikulised keskkonnamuutujad
- Täiustatud veateated (ei riku funktsionaalsust)
- Lisatud logimine (saab maha suruda)
- Paremad tüüpide vihjed (ei mõjuta käitusaega)

---

## Rakendatud Parimad Tavad

### 1. Kasuta Alati Workshop Utilse
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Õige Vigade Käsitlemise Muster
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informatiivne Logimine
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Tüüpide Vihjed
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Põhjalikud Docstringid
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Keskkonnamuutujate Tugi
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Sujuv Degradatsioon
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Levinud Probleemid ja Lahendused

### Probleem: Impordivead
**Lahendus:** Paigalda puuduvad sõltuvused
```bash
pip install sentence-transformers ragas datasets numpy
```

### Probleem: Ühenduse Vead
**Lahendus:** Veendu, et Foundry Local töötab
```bash
foundry service status
foundry model run phi-4-mini
```

### Probleem: Mudelit Ei Leitud
**Lahendus:** Kontrolli saadaval olevaid mudeleid
```bash
foundry model ls
foundry model download <alias>
```

### Probleem: Aeglane Jõudlus
**Lahendus:** Kasuta väiksemaid mudeleid või kohanda parameetreid
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Järgmised Sammud

### 1. Testi Kõiki Näidiseid
Läbi testimise kontrollnimekiri, et veenduda kõigi näidiste korrektses töös.

### 2. Uuenda Dokumentatsiooni
- Uuenda sessiooni markdown-failid uute näidetega
- Lisa tõrkeotsingu sektsioon peamisse README-sse
- Loo kiirviite juhend

### 3. Loo Integratsioonitestid
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Lisa Jõudluse Võrdlused
Jälgi jõudluse parandusi vigade käsitlemise täiustustest.

### 5. Kasutajate Tagasiside
Kogu tagasisidet workshopi osalejatelt:
- Veateadete selguse kohta
- Dokumentatsiooni täielikkuse kohta
- Kasutamise lihtsuse kohta

---

## Ressursid

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Kiirviide**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migreerimise Märkmed**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Peamine Repositoorium**: https://github.com/microsoft/Foundry-Local

---

## Hooldus

### Uute Näidiste Lisamine
Järgi neid mustreid uute näidiste loomisel:

1. Kasuta `workshop_utils` kliendi haldamiseks
2. Lisa põhjalik vigade käsitlemine
3. Kaasa keskkonnamuutujate tugi
4. Lisa tüüpide vihjed ja docstringid
5. Paku informatiivset logimist
6. Kaasa kasutusnäited docstringis
7. Lisa viited SDK dokumentatsioonile

### Uuenduste Ülevaatamine
Uuenduste ülevaatamisel kontrolli:
- [ ] Vigade käsitlemist kõigil I/O operatsioonidel
- [ ] Tüüpide vihjeid avalikel funktsioonidel
- [ ] Põhjalikke docstringe
- [ ] Keskkonnamuutujate dokumentatsiooni
- [ ] Informatiivset kasutajate tagasisidet
- [ ] SDK viiteid
- [ ] Järjepidevat koodistiili

---

**Kokkuvõte**: Kõik Workshopi Python-näidised järgivad nüüd Foundry Local SDK parimaid tavasid, pakkudes täiustatud vigade käsitlemist, põhjalikku dokumentatsiooni ja parendatud kasutajakogemust. Funktsionaalsust ei ole rikutud - kõik olemasolevad funktsioonid on säilinud ja täiustatud.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.