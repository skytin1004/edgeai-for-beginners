<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T14:43:27+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "no"
}
-->
# Workshop Eksempler - Oppsummering av Oppdatering for Foundry Local SDK

## Oversikt

Alle Python-eksempler i `Workshop/samples`-mappen er oppdatert for å følge beste praksis for Foundry Local SDK og sikre konsistens på tvers av workshoppen.

**Dato**: 8. oktober 2025  
**Omfang**: 9 Python-filer fordelt på 6 workshop-økter  
**Hovedfokus**: Feilhåndtering, dokumentasjon, SDK-mønstre, brukeropplevelse

---

## Oppdaterte Filer

### Økt 01: Kom i Gang
- ✅ `chat_bootstrap.py` - Grunnleggende eksempler på chat og streaming

### Økt 02: RAG-løsninger
- ✅ `rag_pipeline.py` - RAG-implementasjon med embeddings
- ✅ `rag_eval_ragas.py` - RAG-evaluering med RAGAS-metrikker

### Økt 03: Åpen Kildekode Modeller
- ✅ `benchmark_oss_models.py` - Benchmarking av flere modeller

### Økt 04: Banebrytende Modeller
- ✅ `model_compare.py` - Sammenligning av SLM og LLM

### Økt 05: AI-drevne Agenter
- ✅ `agents_orchestrator.py` - Koordinering av flere agenter

### Økt 06: Modeller som Verktøy
- ✅ `models_router.py` - Intent-basert modellruting
- ✅ `models_pipeline.py` - Flertrinns rutet pipeline

### Støttende Infrastruktur
- ✅ `workshop_utils.py` - Følger allerede beste praksis (ingen endringer nødvendig)

---

## Viktige Forbedringer

### 1. Forbedret Feilhåndtering

**Før:**
```python
manager, client, model_id = get_client(alias)
```

**Etter:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Fordeler:**
- Smidig feilhåndtering med tydelige feilmeldinger
- Handlingsrettede feilsøkingshint
- Korrekte avslutningskoder for skript

### 2. Bedre Importhåndtering

**Før:**
```python
from sentence_transformers import SentenceTransformer
```

**Etter:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Fordeler:**
- Klar veiledning når avhengigheter mangler
- Forhindrer kryptiske importfeil
- Brukervennlige installasjonsinstruksjoner

### 3. Omfattende Dokumentasjon

**Lagt til i alle eksempler:**
- Dokumentasjon av miljøvariabler i docstrings
- SDK-referanselenker
- Brukseksempler
- Detaljert funksjons-/parameterdokumentasjon
- Type hints for bedre IDE-støtte

**Eksempel:**
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

### 4. Forbedret Brukerfeedback

**Lagt til informativ logging:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Fremdriftsindikatorer:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Strukturert utdata:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Robust Benchmarking

**Forbedringer i Økt 03:**
- Feilhåndtering per modell (fortsetter ved feil)
- Detaljert fremdriftsrapportering
- Korrekt utførelse av oppvarmingsrunder
- Støtte for måling av første-token-latens
- Klar separasjon av stadier

### 6. Konsistente Type Hints

**Lagt til overalt:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Fordeler:**
- Bedre autoutfylling i IDE
- Tidlig feildeteksjon
- Selvforklarende kode

### 7. Forbedret Modellruter

**Forbedringer i Økt 06:**
- Omfattende dokumentasjon av intensjonsdeteksjon
- Forklaring av modellvalg-algoritme
- Detaljerte rutelogger
- Testutdataformattering
- Feilhåndtering i batch-testing

### 8. Orkestrering av Flere Agenter

**Forbedringer i Økt 05:**
- Fremdriftsrapportering trinn for trinn
- Feilhåndtering per agent
- Klar pipeline-struktur
- Bedre dokumentasjon av minnehåndtering

---

## Test Sjekkliste

### Forutsetninger
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Test Hvert Eksempel

#### Økt 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### Økt 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### Økt 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### Økt 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### Økt 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### Økt 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## Referanse for Miljøvariabler

### Globale (Alle Eksempler)
| Variabel | Beskrivelse | Standard |
|----------|-------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Modellalias som skal brukes | Varierer per eksempel |
| `FOUNDRY_LOCAL_ENDPOINT` | Overstyr tjenesteendepunkt | Auto-detektert |
| `SHOW_USAGE` | Vis tokenbruk | `0` |
| `RETRY_ON_FAIL` | Aktiver retry-logikk | `1` |
| `RETRY_BACKOFF` | Startforsinkelse for retry | `1.0` |

### Eksempelspesifikke
| Variabel | Brukt av | Beskrivelse |
|----------|----------|-------------|
| `EMBED_MODEL` | Økt 02 | Navn på embedding-modell |
| `RAG_QUESTION` | Økt 02 | Testspørsmål for RAG |
| `BENCH_MODELS` | Økt 03 | Kommaseparerte modeller for benchmarking |
| `BENCH_ROUNDS` | Økt 03 | Antall benchmark-runder |
| `BENCH_PROMPT` | Økt 03 | Testprompt for benchmarking |
| `BENCH_STREAM` | Økt 03 | Mål første-token-latens |
| `SLM_ALIAS` | Økt 04 | Liten språkmodell |
| `LLM_ALIAS` | Økt 04 | Stor språkmodell |
| `COMPARE_PROMPT` | Økt 04 | Testprompt for sammenligning |
| `AGENT_MODEL_PRIMARY` | Økt 05 | Primær agentmodell |
| `AGENT_MODEL_EDITOR` | Økt 05 | Redigeringsagentmodell |
| `AGENT_QUESTION` | Økt 05 | Testspørsmål for agenter |
| `PIPELINE_TASK` | Økt 06 | Oppgave for pipeline |

---

## Endringer som Bryter Kompatibilitet

**Ingen** - Alle endringer er bakoverkompatible.

Eksisterende skript vil fortsatt fungere. Nye funksjoner er:
- Valgfrie miljøvariabler
- Forbedrede feilmeldinger (bryter ikke funksjonalitet)
- Ekstra logging (kan undertrykkes)
- Bedre type hints (ingen innvirkning på kjøretid)

---

## Implementerte Beste Praksiser

### 1. Bruk Alltid Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Korrekt Mønster for Feilhåndtering
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informativ Logging
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Type Hints
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Omfattende Docstrings
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

### 6. Støtte for Miljøvariabler
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Smidig Degradering
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

## Vanlige Problemer og Løsninger

### Problem: Importfeil
**Løsning:** Installer manglende avhengigheter
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problem: Tilkoblingsfeil
**Løsning:** Sørg for at Foundry Local kjører
```bash
foundry service status
foundry model run phi-4-mini
```

### Problem: Modell Ikke Funnet
**Løsning:** Sjekk tilgjengelige modeller
```bash
foundry model ls
foundry model download <alias>
```

### Problem: Treg Ytelse
**Løsning:** Bruk mindre modeller eller juster parametere
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Neste Steg

### 1. Test Alle Eksempler
Gå gjennom test-sjekklisten ovenfor for å verifisere at alle eksempler fungerer korrekt.

### 2. Oppdater Dokumentasjon
- Oppdater markdown-filene for øktene med nye eksempler
- Legg til feilsøkingsseksjon i hoved-README
- Lag en hurtigreferanseguide

### 3. Lag Integrasjonstester
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Legg til Ytelsesbenchmarking
Spor ytelsesforbedringer fra forbedret feilhåndtering.

### 5. Brukerfeedback
Samle tilbakemeldinger fra workshop-deltakere om:
- Klarhet i feilmeldinger
- Fullstendighet i dokumentasjon
- Brukervennlighet

---

## Ressurser

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Hurtigreferanse**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migreringsnotater**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Hovedrepository**: https://github.com/microsoft/Foundry-Local

---

## Vedlikehold

### Legge til Nye Eksempler
Følg disse mønstrene når du lager nye eksempler:

1. Bruk `workshop_utils` for klienthåndtering
2. Legg til omfattende feilhåndtering
3. Inkluder støtte for miljøvariabler
4. Legg til type hints og docstrings
5. Gi informativ logging
6. Inkluder brukseksempler i docstring
7. Lenke til SDK-dokumentasjon

### Gjennomgang av Oppdateringer
Når du gjennomgår oppdateringer av eksempler, sjekk for:
- [ ] Feilhåndtering på alle I/O-operasjoner
- [ ] Type hints på offentlige funksjoner
- [ ] Omfattende docstrings
- [ ] Dokumentasjon av miljøvariabler
- [ ] Informativ brukerfeedback
- [ ] SDK-referanselenker
- [ ] Konsistent kodestil

---

**Oppsummering**: Alle Workshop Python-eksempler følger nå beste praksis for Foundry Local SDK med forbedret feilhåndtering, omfattende dokumentasjon og forbedret brukeropplevelse. Ingen endringer som bryter kompatibilitet - all eksisterende funksjonalitet er bevart og forbedret.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.