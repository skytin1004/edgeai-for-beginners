<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T11:06:17+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "it"
}
-->
# Esempi del Workshop - Riepilogo aggiornamento SDK locale di Foundry

## Panoramica

Tutti gli esempi Python nella directory `Workshop/samples` sono stati aggiornati per seguire le migliori pratiche dell'SDK locale di Foundry e garantire coerenza in tutto il workshop.

**Data**: 8 ottobre 2025  
**Ambito**: 9 file Python in 6 sessioni del workshop  
**Focus principale**: Gestione degli errori, documentazione, modelli SDK, esperienza utente

---

## File aggiornati

### Sessione 01: Introduzione
- ✅ `chat_bootstrap.py` - Esempi base di chat e streaming

### Sessione 02: Soluzioni RAG
- ✅ `rag_pipeline.py` - Implementazione RAG con embeddings
- ✅ `rag_eval_ragas.py` - Valutazione RAG con metriche RAGAS

### Sessione 03: Modelli Open Source
- ✅ `benchmark_oss_models.py` - Benchmarking multi-modello

### Sessione 04: Modelli all'avanguardia
- ✅ `model_compare.py` - Confronto tra SLM e LLM

### Sessione 05: Agenti potenziati dall'IA
- ✅ `agents_orchestrator.py` - Coordinamento multi-agente

### Sessione 06: Modelli come strumenti
- ✅ `models_router.py` - Routing basato sull'intento
- ✅ `models_pipeline.py` - Pipeline multi-step con routing

### Infrastruttura di supporto
- ✅ `workshop_utils.py` - Già conforme alle migliori pratiche (nessuna modifica necessaria)

---

## Miglioramenti principali

### 1. Miglior gestione degli errori

**Prima:**
```python
manager, client, model_id = get_client(alias)
```

**Dopo:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Vantaggi:**
- Gestione degli errori più fluida con messaggi chiari
- Suggerimenti pratici per la risoluzione dei problemi
- Codici di uscita appropriati per gli script

### 2. Migliore gestione delle importazioni

**Prima:**
```python
from sentence_transformers import SentenceTransformer
```

**Dopo:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Vantaggi:**
- Indicazioni chiare in caso di dipendenze mancanti
- Prevenzione di errori di importazione criptici
- Istruzioni di installazione user-friendly

### 3. Documentazione completa

**Aggiunto a tutti gli esempi:**
- Documentazione delle variabili d'ambiente nei docstring
- Link di riferimento all'SDK
- Esempi di utilizzo
- Documentazione dettagliata di funzioni/parametri
- Suggerimenti sui tipi per un miglior supporto IDE

**Esempio:**
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

### 4. Feedback migliorato per l'utente

**Aggiunto logging informativo:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Indicatori di progresso:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Output strutturato:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Benchmarking robusto

**Miglioramenti nella sessione 03:**
- Gestione degli errori per modello (continua in caso di errore)
- Report dettagliati sul progresso
- Esecuzione corretta dei round di riscaldamento
- Supporto per la misurazione della latenza del primo token
- Chiara separazione delle fasi

### 6. Coerenza nei suggerimenti sui tipi

**Aggiunti ovunque:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Vantaggi:**
- Miglior completamento automatico nell'IDE
- Rilevamento precoce degli errori
- Codice auto-documentante

### 7. Router dei modelli migliorato

**Miglioramenti nella sessione 06:**
- Documentazione completa del rilevamento degli intenti
- Spiegazione dell'algoritmo di selezione del modello
- Log dettagliati sul routing
- Formattazione dell'output dei test
- Recupero degli errori nei test batch

### 8. Orchestrazione multi-agente

**Miglioramenti nella sessione 05:**
- Report sul progresso fase per fase
- Gestione degli errori per agente
- Struttura chiara della pipeline
- Documentazione migliorata sulla gestione della memoria

---

## Lista di controllo per i test

### Prerequisiti
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testare ogni esempio

#### Sessione 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### Sessione 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### Sessione 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### Sessione 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### Sessione 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### Sessione 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## Riferimento alle variabili d'ambiente

### Globali (tutti gli esempi)
| Variabile | Descrizione | Predefinito |
|-----------|-------------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Alias del modello da utilizzare | Varia in base all'esempio |
| `FOUNDRY_LOCAL_ENDPOINT` | Sovrascrive l'endpoint del servizio | Rilevato automaticamente |
| `SHOW_USAGE` | Mostra l'utilizzo dei token | `0` |
| `RETRY_ON_FAIL` | Abilita la logica di ripetizione | `1` |
| `RETRY_BACKOFF` | Ritardo iniziale per il retry | `1.0` |

### Specifiche per esempio
| Variabile | Utilizzata da | Descrizione |
|-----------|---------------|-------------|
| `EMBED_MODEL` | Sessione 02 | Nome del modello di embedding |
| `RAG_QUESTION` | Sessione 02 | Domanda di test per RAG |
| `BENCH_MODELS` | Sessione 03 | Modelli da testare separati da virgola |
| `BENCH_ROUNDS` | Sessione 03 | Numero di round di benchmark |
| `BENCH_PROMPT` | Sessione 03 | Prompt di test per i benchmark |
| `BENCH_STREAM` | Sessione 03 | Misura della latenza del primo token |
| `SLM_ALIAS` | Sessione 04 | Modello linguistico piccolo |
| `LLM_ALIAS` | Sessione 04 | Modello linguistico grande |
| `COMPARE_PROMPT` | Sessione 04 | Prompt di test per il confronto |
| `AGENT_MODEL_PRIMARY` | Sessione 05 | Modello agente primario |
| `AGENT_MODEL_EDITOR` | Sessione 05 | Modello agente editor |
| `AGENT_QUESTION` | Sessione 05 | Domanda di test per gli agenti |
| `PIPELINE_TASK` | Sessione 06 | Task per la pipeline |

---

## Modifiche che interrompono la compatibilità

**Nessuna** - Tutte le modifiche sono retrocompatibili.

Gli script esistenti continueranno a funzionare. Le nuove funzionalità includono:
- Variabili d'ambiente opzionali
- Messaggi di errore migliorati (non interrompono la funzionalità)
- Logging aggiuntivo (può essere disattivato)
- Migliori suggerimenti sui tipi (nessun impatto a runtime)

---

## Migliori pratiche implementate

### 1. Utilizzare sempre Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Modello di gestione degli errori adeguato
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Logging informativo
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Suggerimenti sui tipi
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Docstring completi
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

### 6. Supporto per le variabili d'ambiente
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Degradazione graduale
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

## Problemi comuni e soluzioni

### Problema: Errori di importazione
**Soluzione:** Installa le dipendenze mancanti
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problema: Errori di connessione
**Soluzione:** Assicurati che Foundry Local sia in esecuzione
```bash
foundry service status
foundry model run phi-4-mini
```

### Problema: Modello non trovato
**Soluzione:** Controlla i modelli disponibili
```bash
foundry model ls
foundry model download <alias>
```

### Problema: Prestazioni lente
**Soluzione:** Usa modelli più piccoli o regola i parametri
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Prossimi passi

### 1. Testare tutti gli esempi
Segui la lista di controllo dei test sopra per verificare che tutti gli esempi funzionino correttamente.

### 2. Aggiornare la documentazione
- Aggiorna i file markdown delle sessioni con i nuovi esempi
- Aggiungi una sezione di risoluzione dei problemi al README principale
- Crea una guida di riferimento rapido

### 3. Creare test di integrazione
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Aggiungere benchmark sulle prestazioni
Monitora i miglioramenti delle prestazioni derivanti dai miglioramenti nella gestione degli errori.

### 5. Feedback degli utenti
Raccogli feedback dai partecipanti al workshop su:
- Chiarezza dei messaggi di errore
- Completezza della documentazione
- Facilità d'uso

---

## Risorse

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **Riferimento rapido**: `Workshop/FOUNDRY_SDK_QUICKREF.md`  
- **Note di migrazione**: `Workshop/SDK_MIGRATION_NOTES.md`  
- **Repository principale**: https://github.com/microsoft/Foundry-Local  

---

## Manutenzione

### Aggiunta di nuovi esempi
Segui questi modelli quando crei nuovi esempi:

1. Usa `workshop_utils` per la gestione del client
2. Aggiungi una gestione completa degli errori
3. Includi il supporto per le variabili d'ambiente
4. Aggiungi suggerimenti sui tipi e docstring
5. Fornisci un logging informativo
6. Includi esempi di utilizzo nei docstring
7. Collega la documentazione dell'SDK

### Revisione degli aggiornamenti
Quando rivedi gli aggiornamenti degli esempi, verifica:
- [ ] Gestione degli errori su tutte le operazioni I/O
- [ ] Suggerimenti sui tipi per le funzioni pubbliche
- [ ] Docstring completi
- [ ] Documentazione delle variabili d'ambiente
- [ ] Feedback informativo per l'utente
- [ ] Link di riferimento all'SDK
- [ ] Stile del codice coerente

---

**Riepilogo**: Tutti gli esempi Python del Workshop ora seguono le migliori pratiche dell'SDK locale di Foundry con una gestione degli errori migliorata, documentazione completa e un'esperienza utente ottimizzata. Nessuna modifica che interrompa la compatibilità: tutte le funzionalità esistenti sono state mantenute e migliorate.

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.