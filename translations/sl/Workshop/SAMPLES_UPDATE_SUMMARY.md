<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-08T12:18:50+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "sl"
}
-->
# Vzorci delavnice - Povzetek posodobitev lokalnega SDK Foundry

## Pregled

Vsi vzorci v Pythonu v imeniku `Workshop/samples` so bili posodobljeni, da sledijo najboljšim praksam lokalnega SDK Foundry in zagotavljajo doslednost v celotni delavnici.

**Datum**: 8. oktober 2025  
**Obseg**: 9 datotek v Pythonu v 6 delavniških sklopih  
**Glavni poudarek**: Obvladovanje napak, dokumentacija, vzorci SDK, uporabniška izkušnja

---

## Posodobljene datoteke

### Sklop 01: Začetek
- ✅ `chat_bootstrap.py` - Osnovni primeri klepeta in pretakanja

### Sklop 02: RAG rešitve
- ✅ `rag_pipeline.py` - Implementacija RAG z vdelavami
- ✅ `rag_eval_ragas.py` - Evalvacija RAG z metrikami RAGAS

### Sklop 03: Modeli odprte kode
- ✅ `benchmark_oss_models.py` - Primerjava več modelov

### Sklop 04: Napredni modeli
- ✅ `model_compare.py` - Primerjava SLM in LLM

### Sklop 05: Agenti, ki jih poganja AI
- ✅ `agents_orchestrator.py` - Koordinacija več agentov

### Sklop 06: Modeli kot orodja
- ✅ `models_router.py` - Usmerjanje modelov na podlagi namena
- ✅ `models_pipeline.py` - Večstopenjski usmerjeni cevovod

### Podporna infrastruktura
- ✅ `workshop_utils.py` - Že sledi najboljšim praksam (ni potrebnih sprememb)

---

## Ključne izboljšave

### 1. Izboljšano obvladovanje napak

**Prej:**
```python
manager, client, model_id = get_client(alias)
```

**Potem:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Prednosti:**
- Elegantno obvladovanje napak z jasnimi sporočili o napakah
- Koristni namigi za odpravljanje težav
- Pravilne kode za izhod pri skriptiranju

### 2. Boljše upravljanje uvozov

**Prej:**
```python
from sentence_transformers import SentenceTransformer
```

**Potem:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Prednosti:**
- Jasna navodila, ko manjkajo odvisnosti
- Preprečevanje nejasnih napak pri uvozu
- Prijazna navodila za namestitev

### 3. Celovita dokumentacija

**Dodano v vse vzorce:**
- Dokumentacija okoljskih spremenljivk v docstringih
- Povezave na referenčno dokumentacijo SDK
- Primeri uporabe
- Podrobna dokumentacija funkcij/parametrov
- Namigi tipov za boljšo podporo IDE

**Primer:**
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

### 4. Izboljšana povratna informacija uporabnikom

**Dodano informativno beleženje:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Kazalniki napredka:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Strukturiran izhod:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Zanesljivo primerjanje

**Izboljšave v sklopu 03:**
- Obvladovanje napak za vsak model (nadaljuje ob napaki)
- Podrobno poročanje o napredku
- Pravilno izvedeni ogrevalni krogi
- Podpora za merjenje zakasnitve prvega žetona
- Jasna ločitev faz

### 6. Dosledni namigi tipov

**Dodano povsod:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Prednosti:**
- Boljša samodokončanja v IDE
- Zgodnje odkrivanje napak
- Samodokumentiranje kode

### 7. Izboljšan usmerjevalnik modelov

**Izboljšave v sklopu 06:**
- Celovita dokumentacija zaznavanja namena
- Razlaga algoritma za izbiro modela
- Podrobni dnevniki usmerjanja
- Oblikovanje testnih izhodov
- Obnova napak pri testiranju v serijah

### 8. Orkestracija več agentov

**Izboljšave v sklopu 05:**
- Poročanje o napredku po fazah
- Obvladovanje napak za vsakega agenta
- Jasna struktura cevovoda
- Boljša dokumentacija upravljanja pomnilnika

---

## Preveritveni seznam testiranja

### Predpogoji
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testiranje vsakega vzorca

#### Sklop 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### Sklop 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### Sklop 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### Sklop 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### Sklop 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### Sklop 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## Referenca okoljskih spremenljivk

### Globalno (vsi vzorci)
| Spremenljivka | Opis | Privzeto |
|---------------|------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias modela za uporabo | Različno glede na vzorec |
| `FOUNDRY_LOCAL_ENDPOINT` | Prepis končne točke storitve | Samodejno zaznano |
| `SHOW_USAGE` | Prikaz uporabe žetonov | `0` |
| `RETRY_ON_FAIL` | Omogoči logiko ponovnega poskusa | `1` |
| `RETRY_BACKOFF` | Začetna zakasnitev ponovnega poskusa | `1.0` |

### Specifično za vzorec
| Spremenljivka | Uporablja | Opis |
|---------------|----------|------|
| `EMBED_MODEL` | Sklop 02 | Ime modela za vdelave |
| `RAG_QUESTION` | Sklop 02 | Testno vprašanje za RAG |
| `BENCH_MODELS` | Sklop 03 | Modeli za primerjanje, ločeni z vejico |
| `BENCH_ROUNDS` | Sklop 03 | Število krogov primerjanja |
| `BENCH_PROMPT` | Sklop 03 | Testni poziv za primerjanja |
| `BENCH_STREAM` | Sklop 03 | Merjenje zakasnitve prvega žetona |
| `SLM_ALIAS` | Sklop 04 | Majhen jezikovni model |
| `LLM_ALIAS` | Sklop 04 | Velik jezikovni model |
| `COMPARE_PROMPT` | Sklop 04 | Testni poziv za primerjavo |
| `AGENT_MODEL_PRIMARY` | Sklop 05 | Primarni model agenta |
| `AGENT_MODEL_EDITOR` | Sklop 05 | Model agenta za urejanje |
| `AGENT_QUESTION` | Sklop 05 | Testno vprašanje za agente |
| `PIPELINE_TASK` | Sklop 06 | Naloga za cevovod |

---

## Prelomne spremembe

**Ni** - Vse spremembe so združljive nazaj.

Obstoječi skripti bodo še naprej delovali. Nove funkcije so:
- Izbirne okoljske spremenljivke
- Izboljšana sporočila o napakah (ne prekinjajo funkcionalnosti)
- Dodatno beleženje (lahko se zatre)
- Boljši namigi tipov (brez vpliva na izvajanje)

---

## Uvedene najboljše prakse

### 1. Vedno uporabljajte Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Pravilni vzorec obvladovanja napak
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informativno beleženje
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Namigi tipov
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Celoviti docstringi
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

### 6. Podpora okoljskim spremenljivkam
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Elegantno poslabšanje
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

## Pogoste težave in rešitve

### Težava: Napake pri uvozu
**Rešitev:** Namestite manjkajoče odvisnosti
```bash
pip install sentence-transformers ragas datasets numpy
```

### Težava: Napake pri povezavi
**Rešitev:** Prepričajte se, da Foundry Local deluje
```bash
foundry service status
foundry model run phi-4-mini
```

### Težava: Model ni najden
**Rešitev:** Preverite razpoložljive modele
```bash
foundry model ls
foundry model download <alias>
```

### Težava: Počasna zmogljivost
**Rešitev:** Uporabite manjše modele ali prilagodite parametre
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Naslednji koraki

### 1. Testirajte vse vzorce
Izvedite preveritveni seznam testiranja zgoraj, da preverite, ali vsi vzorci delujejo pravilno.

### 2. Posodobite dokumentacijo
- Posodobite markdown datoteke sklopov z novimi primeri
- Dodajte razdelek za odpravljanje težav v glavni README
- Ustvarite priročnik za hitro referenco

### 3. Ustvarite integracijske teste
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Dodajte primerjave zmogljivosti
Spremljajte izboljšave zmogljivosti zaradi izboljšanega obvladovanja napak.

### 5. Povratne informacije uporabnikov
Zberite povratne informacije udeležencev delavnice o:
- Jasnosti sporočil o napakah
- Celovitosti dokumentacije
- Enostavnosti uporabe

---

## Viri

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Hitri priročnik**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Opombe o migraciji**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Glavno skladišče**: https://github.com/microsoft/Foundry-Local

---

## Vzdrževanje

### Dodajanje novih vzorcev
Sledite tem vzorcem pri ustvarjanju novih vzorcev:

1. Uporabite `workshop_utils` za upravljanje odjemalcev
2. Dodajte celovito obvladovanje napak
3. Vključite podporo okoljskim spremenljivkam
4. Dodajte namige tipov in docstringe
5. Zagotovite informativno beleženje
6. Vključite primere uporabe v docstring
7. Povežite se na dokumentacijo SDK

### Pregledovanje posodobitev
Pri pregledovanju posodobitev vzorcev preverite:
- [ ] Obvladovanje napak pri vseh operacijah I/O
- [ ] Namige tipov pri javnih funkcijah
- [ ] Celovite docstringe
- [ ] Dokumentacijo okoljskih spremenljivk
- [ ] Informativne povratne informacije uporabnikom
- [ ] Povezave na referenčno dokumentacijo SDK
- [ ] Dosleden slog kode

---

**Povzetek**: Vsi vzorci v Pythonu za delavnico zdaj sledijo najboljšim praksam lokalnega SDK Foundry z izboljšanim obvladovanjem napak, celovito dokumentacijo in izboljšano uporabniško izkušnjo. Brez prelomnih sprememb - vsa obstoječa funkcionalnost je ohranjena in izboljšana.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.