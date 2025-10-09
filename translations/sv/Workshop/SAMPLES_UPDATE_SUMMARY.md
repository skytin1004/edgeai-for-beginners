<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T13:11:59+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "sv"
}
-->
# Workshop-exempel - Sammanfattning av Foundry Local SDK-uppdatering

## Översikt

Alla Python-exempel i katalogen `Workshop/samples` har uppdaterats för att följa bästa praxis för Foundry Local SDK och säkerställa konsekvens i hela workshopen.

**Datum**: 8 oktober 2025  
**Omfattning**: 9 Python-filer över 6 workshop-sessioner  
**Huvudfokus**: Felhantering, dokumentation, SDK-mönster, användarupplevelse

---

## Uppdaterade filer

### Session 01: Komma igång
- ✅ `chat_bootstrap.py` - Grundläggande exempel på chatt och streaming

### Session 02: RAG-lösningar
- ✅ `rag_pipeline.py` - RAG-implementering med embeddings
- ✅ `rag_eval_ragas.py` - RAG-utvärdering med RAGAS-mått

### Session 03: Öppna källkodsmodeller
- ✅ `benchmark_oss_models.py` - Benchmarking av flera modeller

### Session 04: Banbrytande modeller
- ✅ `model_compare.py` - Jämförelse mellan SLM och LLM

### Session 05: AI-drivna agenter
- ✅ `agents_orchestrator.py` - Koordinering av flera agenter

### Session 06: Modeller som verktyg
- ✅ `models_router.py` - Intentbaserad modellroutning
- ✅ `models_pipeline.py` - Flerstegs routad pipeline

### Stödjande infrastruktur
- ✅ `workshop_utils.py` - Följer redan bästa praxis (inga ändringar behövs)

---

## Viktiga förbättringar

### 1. Förbättrad felhantering

**Tidigare:**
```python
manager, client, model_id = get_client(alias)
```
  
**Efter:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```
  
**Fördelar:**
- Smidig felhantering med tydliga felmeddelanden
- Handlingsbara felsökningsförslag
- Korrekt exit-koder för skript

### 2. Bättre hantering av import

**Tidigare:**
```python
from sentence_transformers import SentenceTransformer
```
  
**Efter:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```
  
**Fördelar:**
- Tydlig vägledning när beroenden saknas
- Förhindrar kryptiska importfel
- Användarvänliga installationsinstruktioner

### 3. Omfattande dokumentation

**Tillagt i alla exempel:**
- Dokumentation av miljövariabler i docstrings
- SDK-referenslänkar
- Användningsexempel
- Detaljerad funktion-/parameterdokumentation
- Typanvisningar för bättre stöd i IDE

**Exempel:**
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
  

### 4. Förbättrad användarfeedback

**Tillagt informativ loggning:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```
  
**Progressindikatorer:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```
  
**Strukturerad output:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```
  

### 5. Robust benchmarking

**Förbättringar i session 03:**
- Felhantering per modell (fortsätter vid fel)
- Detaljerad progressrapportering
- Korrekt utförda uppvärmningsrundor
- Stöd för mätning av latens för första token
- Tydlig separering av steg

### 6. Konsekventa typanvisningar

**Tillagt överallt:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```
  
**Fördelar:**
- Bättre autocomplete i IDE
- Tidig felupptäckt
- Självdokumenterande kod

### 7. Förbättrad modellrouter

**Förbättringar i session 06:**
- Omfattande dokumentation för intentdetektion
- Förklaring av algoritm för modellval
- Detaljerade routningsloggar
- Format för testoutput
- Felåterhämtning vid batchtestning

### 8. Orkestrering av flera agenter

**Förbättringar i session 05:**
- Progressrapportering steg för steg
- Felhantering per agent
- Tydlig pipeline-struktur
- Bättre dokumentation för minneshantering

---

## Testchecklista

### Förutsättningar
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```
  

### Testa varje exempel

#### Session 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```
  
#### Session 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```
  
#### Session 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```
  
#### Session 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```
  
#### Session 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```
  
#### Session 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```
  

---

## Referens för miljövariabler

### Globala (Alla exempel)
| Variabel | Beskrivning | Standardvärde |
|----------|-------------|---------------|
| `FOUNDRY_LOCAL_ALIAS` | Modellalias att använda | Varierar beroende på exempel |
| `FOUNDRY_LOCAL_ENDPOINT` | Åsidosätt tjänstendpunkt | Auto-detekterad |
| `SHOW_USAGE` | Visa tokenanvändning | `0` |
| `RETRY_ON_FAIL` | Aktivera återförsökslogik | `1` |
| `RETRY_BACKOFF` | Initial fördröjning vid återförsök | `1.0` |

### Specifika för exempel
| Variabel | Används av | Beskrivning |
|----------|------------|-------------|
| `EMBED_MODEL` | Session 02 | Namn på embedding-modell |
| `RAG_QUESTION` | Session 02 | Testfråga för RAG |
| `BENCH_MODELS` | Session 03 | Komma-separerade modeller att benchmarka |
| `BENCH_ROUNDS` | Session 03 | Antal benchmarkrundor |
| `BENCH_PROMPT` | Session 03 | Testprompt för benchmarks |
| `BENCH_STREAM` | Session 03 | Mäta latens för första token |
| `SLM_ALIAS` | Session 04 | Liten språkmodell |
| `LLM_ALIAS` | Session 04 | Stor språkmodell |
| `COMPARE_PROMPT` | Session 04 | Testprompt för jämförelse |
| `AGENT_MODEL_PRIMARY` | Session 05 | Primär agentmodell |
| `AGENT_MODEL_EDITOR` | Session 05 | Redigeringsagentmodell |
| `AGENT_QUESTION` | Session 05 | Testfråga för agenter |
| `PIPELINE_TASK` | Session 06 | Uppgift för pipeline |

---

## Störande förändringar

**Inga** - Alla ändringar är bakåtkompatibla.

Befintliga skript kommer att fortsätta fungera. Nya funktioner är:
- Valfria miljövariabler
- Förbättrade felmeddelanden (bryter inte funktionalitet)
- Ytterligare loggning (kan undertryckas)
- Bättre typanvisningar (ingen påverkan på runtime)

---

## Implementerade bästa praxis

### 1. Använd alltid Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```
  
### 2. Korrekt mönster för felhantering
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```
  
### 3. Informativ loggning
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```
  
### 4. Typanvisningar
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```
  
### 5. Omfattande docstrings
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
  
### 6. Stöd för miljövariabler
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```
  
### 7. Smidig nedgradering
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

## Vanliga problem och lösningar

### Problem: Importfel
**Lösning:** Installera saknade beroenden  
```bash
pip install sentence-transformers ragas datasets numpy
```
  

### Problem: Anslutningsfel
**Lösning:** Kontrollera att Foundry Local körs  
```bash
foundry service status
foundry model run phi-4-mini
```
  

### Problem: Modell hittas inte
**Lösning:** Kontrollera tillgängliga modeller  
```bash
foundry model ls
foundry model download <alias>
```
  

### Problem: Långsam prestanda
**Lösning:** Använd mindre modeller eller justera parametrar  
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```
  

---

## Nästa steg

### 1. Testa alla exempel
Gå igenom testchecklistan ovan för att verifiera att alla exempel fungerar korrekt.

### 2. Uppdatera dokumentation
- Uppdatera sessionens markdown-filer med nya exempel
- Lägg till felsökningssektion i huvud-README
- Skapa snabbreferensguide

### 3. Skapa integrationstester
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```
  

### 4. Lägg till prestandabenchmarking
Spåra prestandaförbättringar från förbättringar i felhantering.

### 5. Användarfeedback
Samla feedback från workshopdeltagare om:
- Tydlighet i felmeddelanden
- Fullständighet i dokumentation
- Användarvänlighet

---

## Resurser

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **Snabbreferens**: `Workshop/FOUNDRY_SDK_QUICKREF.md`  
- **Migrationsanteckningar**: `Workshop/SDK_MIGRATION_NOTES.md`  
- **Huvudrepository**: https://github.com/microsoft/Foundry-Local  

---

## Underhåll

### Lägga till nya exempel
Följ dessa mönster när du skapar nya exempel:

1. Använd `workshop_utils` för klienthantering
2. Lägg till omfattande felhantering
3. Inkludera stöd för miljövariabler
4. Lägg till typanvisningar och docstrings
5. Tillhandahåll informativ loggning
6. Inkludera användningsexempel i docstring
7. Länka till SDK-dokumentation

### Granska uppdateringar
När du granskar uppdateringar av exempel, kontrollera:
- [ ] Felhantering på alla I/O-operationer
- [ ] Typanvisningar på publika funktioner
- [ ] Omfattande docstrings
- [ ] Dokumentation av miljövariabler
- [ ] Informativ användarfeedback
- [ ] SDK-referenslänkar
- [ ] Konsekvent kodstil

---

**Sammanfattning**: Alla Python-exempel i workshopen följer nu bästa praxis för Foundry Local SDK med förbättrad felhantering, omfattande dokumentation och förbättrad användarupplevelse. Inga störande förändringar - all befintlig funktionalitet bevarad och förbättrad.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.