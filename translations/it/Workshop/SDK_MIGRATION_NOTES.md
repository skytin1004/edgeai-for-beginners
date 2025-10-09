<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-09T11:08:03+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "it"
}
-->
# Note di Migrazione SDK Locale Foundry

## Panoramica

Tutti i file Python nella cartella Workshop sono stati aggiornati per seguire gli ultimi modelli dell'[SDK Python Locale Foundry](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Riepilogo delle Modifiche

### Infrastruttura Core (`workshop_utils.py`)

#### Funzionalità Migliorate:
- **Supporto per Override dell'Endpoint**: Aggiunto supporto per la variabile di ambiente `FOUNDRY_LOCAL_ENDPOINT`
- **Gestione degli Errori Migliorata**: Gestione delle eccezioni più dettagliata con messaggi di errore esplicativi
- **Caching Avanzato**: Le chiavi di cache ora includono l'endpoint per scenari multi-endpoint
- **Backoff Esponenziale**: La logica di retry utilizza ora il backoff esponenziale per una maggiore affidabilità
- **Annotazioni di Tipo**: Aggiunti suggerimenti di tipo completi per un miglior supporto IDE

#### Nuove Capacità:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Applicazioni di Esempio

#### Sessione 01: Bootstrap Chat (`chat_bootstrap.py`)
- Modello predefinito aggiornato da `phi-3.5-mini` a `phi-4-mini`
- Aggiunto supporto per override dell'endpoint
- Documentazione migliorata con riferimenti all'SDK

#### Sessione 02: Pipeline RAG (`rag_pipeline.py`)
- Aggiornato per utilizzare `phi-4-mini` come modello predefinito
- Aggiunto supporto per override dell'endpoint
- Documentazione migliorata con dettagli sulle variabili di ambiente

#### Sessione 02: Valutazione RAG (`rag_eval_ragas.py`)
- Modelli predefiniti aggiornati
- Configurazione dell'endpoint aggiunta
- Gestione degli errori migliorata

#### Sessione 03: Benchmarking (`benchmark_oss_models.py`)
- Lista di modelli predefiniti aggiornata per includere `phi-4-mini`
- Documentazione completa sulle variabili di ambiente aggiunta
- Documentazione delle funzioni migliorata
- Supporto per override dell'endpoint aggiunto ovunque

#### Sessione 04: Confronto Modelli (`model_compare.py`)
- Modello LLM predefinito aggiornato da `gpt-oss-20b` a `qwen2.5-7b`
- Configurazione dell'endpoint aggiunta
- Documentazione migliorata

#### Sessione 05: Orchestrazione Multi-Agent (`agents_orchestrator.py`)
- Aggiunti suggerimenti di tipo (modificato `str | None` in `Optional[str]`)
- Documentazione della classe Agent migliorata
- Supporto per override dell'endpoint aggiunto
- Modello di inizializzazione migliorato

#### Sessione 06: Router Modelli (`models_router.py`)
- Configurazione dell'endpoint aggiunta
- Documentazione migliorata per il rilevamento delle intenzioni
- Documentazione della logica di routing migliorata

#### Sessione 06: Pipeline (`models_pipeline.py`)
- Documentazione completa delle funzioni aggiunta
- Documentazione passo-passo migliorata
- Gestione degli errori migliorata

### Script

#### Esportazione Benchmark (`export_benchmark_markdown.py`)
- Supporto per override dell'endpoint aggiunto
- Modelli predefiniti aggiornati
- Documentazione delle funzioni migliorata
- Gestione degli errori migliorata

#### Linter CLI (`lint_markdown_cli.py`)
- Aggiunti link di riferimento all'SDK
- Documentazione sull'uso migliorata

### Test

#### Test di Smoke (`smoke.py`)
- Supporto per override dell'endpoint aggiunto
- Documentazione migliorata
- Documentazione dei casi di test migliorata
- Report degli errori migliorato

## Variabili di Ambiente

Tutti gli esempi ora supportano queste variabili di ambiente:

### Configurazione Core
- `FOUNDRY_LOCAL_ALIAS` - Alias del modello da utilizzare (predefinito varia in base all'esempio)
- `FOUNDRY_LOCAL_ENDPOINT` - Override dell'endpoint del servizio (opzionale)
- `SHOW_USAGE` - Mostra statistiche sull'uso dei token (predefinito: "0")
- `RETRY_ON_FAIL` - Abilita la logica di retry (predefinito: "1")
- `RETRY_BACKOFF` - Ritardo iniziale del retry in secondi (predefinito: "1.0")

### Specifiche per Esempio
- `EMBED_MODEL` - Modello di embedding per gli esempi RAG
- `BENCH_MODELS` - Modelli separati da virgola per benchmarking
- `BENCH_ROUNDS` - Numero di round di benchmarking
- `BENCH_PROMPT` - Prompt di test per benchmarking
- `BENCH_STREAM` - Misura la latenza del primo token
- `RAG_QUESTION` - Domanda di test per gli esempi RAG
- `AGENT_MODEL_PRIMARY` - Modello principale dell'agente
- `AGENT_MODEL_EDITOR` - Modello editor dell'agente
- `SLM_ALIAS` - Alias del modello linguistico piccolo
- `LLM_ALIAS` - Alias del modello linguistico grande

## Best Practices dell'SDK Implementate

### 1. Inizializzazione Corretta del Client
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Recupero Informazioni sul Modello
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Gestione degli Errori
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logica di Retry con Backoff Esponenziale
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Supporto per Streaming
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Guida alla Migrazione per Esempi Personalizzati

Se stai creando nuovi esempi o aggiornando quelli esistenti:

1. **Usa gli helper di `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Supporta l'override dell'endpoint**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Aggiungi documentazione completa**:
   - Variabili di ambiente nella docstring
   - Link di riferimento all'SDK
   - Esempi di utilizzo

4. **Usa suggerimenti di tipo**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementa una gestione degli errori corretta**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Test

Tutti gli esempi possono essere testati con:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
python Workshop/samples/session01/chat_bootstrap.py "Test question"
python Workshop/samples/session02/rag_pipeline.py

# Run benchmark
python Workshop/samples/session03/benchmark_oss_models.py

# Run smoke tests
python -m Workshop.tests.smoke
```

## Riferimenti alla Documentazione dell'SDK

- **Repository Principale**: https://github.com/microsoft/Foundry-Local
- **SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Documentazione API**: Consulta il repository SDK per la documentazione API più recente

## Modifiche Incompatibili

### Nessuna Prevista
Tutte le modifiche sono retrocompatibili. Gli aggiornamenti principalmente:
- Aggiungono nuove funzionalità opzionali (override dell'endpoint)
- Migliorano la gestione degli errori
- Potenziano la documentazione
- Aggiornano i nomi dei modelli predefiniti alle raccomandazioni attuali

### Miglioramenti Opzionali
Potresti voler aggiornare il tuo codice per utilizzare:
- `FOUNDRY_LOCAL_ENDPOINT` per un controllo esplicito dell'endpoint
- `SHOW_USAGE=1` per la visibilità sull'uso dei token
- Modelli predefiniti aggiornati (`phi-4-mini` invece di `phi-3.5-mini`)

## Problemi Comuni e Soluzioni

### Problema: "Inizializzazione del client fallita"
**Soluzione**: Assicurati che il servizio Foundry Locale sia in esecuzione:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problema: "Modello non trovato"
**Soluzione**: Controlla i modelli disponibili:
```bash
foundry model list
```

### Problema: Errori di connessione all'endpoint
**Soluzione**: Verifica l'endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Prossimi Passi

1. **Aggiorna gli esempi di Module08**: Applica modelli simili agli esempi di Module08
2. **Aggiungi test di integrazione**: Crea una suite di test completa
3. **Benchmark delle prestazioni**: Confronta le prestazioni prima/dopo
4. **Aggiornamenti alla documentazione**: Aggiorna il README principale con i nuovi modelli

## Linee Guida per i Contributi

Quando aggiungi nuovi esempi:
1. Usa `workshop_utils.py` per coerenza
2. Segui il modello degli esempi esistenti
3. Aggiungi docstring complete
4. Includi link di riferimento all'SDK
5. Supporta l'override dell'endpoint
6. Aggiungi suggerimenti di tipo corretti
7. Includi esempi di utilizzo nella docstring

## Compatibilità Versioni

Questi aggiornamenti sono compatibili con:
- `foundry-local-sdk` (ultima versione)
- `openai>=1.30.0`
- Python 3.8+

---

**Ultimo Aggiornamento**: 08-01-2025  
**Manutentore**: EdgeAI Workshop Team  
**Versione SDK**: Foundry Local SDK (ultima 0.7.117+67073234e7)

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.