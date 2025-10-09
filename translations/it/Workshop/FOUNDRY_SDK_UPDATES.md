<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T10:35:38+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "it"
}
-->
# Aggiornamenti del Foundry Local SDK

## Panoramica

Aggiornati i notebook e le utility del Workshop per utilizzare correttamente il **Foundry Local Python SDK ufficiale**, seguendo i modelli da:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## File Modificati

### 1. `Workshop/samples/workshop_utils.py`

**Modifiche:**
- ✅ Aggiunta gestione degli errori di importazione per il pacchetto `foundry-local-sdk`
- ✅ Migliorata la documentazione con i modelli ufficiali dell’SDK
- ✅ Logging migliorato con simboli Unicode (✓, ✗, ⚠)
- ✅ Aggiunti docstring completi con esempi
- ✅ Messaggi di errore più chiari con riferimenti ai comandi CLI
- ✅ Commenti aggiornati per allinearsi alla documentazione ufficiale dell’SDK

**Miglioramenti principali:**

#### Gestione degli errori di importazione
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Funzione migliorata `get_client()`
- Documentazione dettagliata sul modello di inizializzazione dell’SDK
- Chiarito che `FoundryLocalManager` avvia automaticamente il servizio
- Spiegata la risoluzione degli alias dei modelli per varianti ottimizzate per l’hardware
- Logging migliorato con informazioni sugli endpoint
- Messaggi di errore più chiari con suggerimenti per la risoluzione dei problemi

#### Funzione migliorata `chat_once()`
- Aggiunto un docstring completo con esempi di utilizzo
- Chiarita la compatibilità con l’SDK OpenAI
- Documentato il supporto allo streaming (tramite kwargs)
- Migliorati i messaggi di errore con suggerimenti sui comandi CLI
- Aggiunte note sul controllo della disponibilità dei modelli

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Modifiche:**
- ✅ Aggiornate tutte le celle markdown con riferimenti all’SDK
- ✅ Commenti al codice migliorati con spiegazioni sui modelli dell’SDK
- ✅ Documentazione e spiegazioni delle celle migliorate
- ✅ Aggiunta guida alla risoluzione dei problemi
- ✅ Aggiornato il catalogo dei modelli (sostituito 'gpt-oss-20b' con 'phi-3.5-mini')
- ✅ Migliorato il formato dell’output con indicatori visivi
- ✅ Aggiunti collegamenti e riferimenti all’SDK

**Aggiornamenti cella per cella:**

#### Cella 1 (Titolo)
- Aggiunti collegamenti alla documentazione dell’SDK
- Riferimenti ai repository GitHub ufficiali

#### Cella 2 (Scenario)
- Riformattato con passaggi numerati
- Chiarito il modello di routing basato sull’intento
- Enfatizzati i vantaggi dell’esecuzione locale

#### Cella 3 (Installazione delle dipendenze)
- Aggiunta spiegazione di cosa fornisce ogni pacchetto
- Documentate le capacità dell’SDK (risoluzione degli alias, ottimizzazione hardware)

#### Cella 4 (Configurazione dell’ambiente)
- Docstring delle funzioni migliorati
- Aggiunti commenti in linea che spiegano i modelli dell’SDK
- Documentata la struttura del catalogo dei modelli
- Chiarita la corrispondenza priorità/capacità

#### Cella 5 (Controllo del catalogo)
- Aggiunti segni di spunta visivi (✓)
- Migliorato il formato dell’output

#### Cella 6 (Test di rilevamento dell’intento)
- Output riformattato in stile tabella
- Mostra sia l’intento che il modello selezionato

#### Cella 7 (Funzione di routing)
- Spiegazione completa del modello dell’SDK
- Documentato il flusso di inizializzazione
- Elencate tutte le funzionalità (retry, tracking, errori)
- Aggiunto collegamento di riferimento all’SDK

#### Cella 8 (Demo batch)
- Spiegazione migliorata di cosa aspettarsi
- Aggiunta sezione di risoluzione dei problemi
- Inclusi comandi CLI per il debug
- Migliorato il formato dell’output

### 3. `Workshop/notebooks/session06_README.md` (Nuovo File)

**Creata documentazione completa che copre:**

1. **Panoramica**: Diagramma dell’architettura e spiegazione dei componenti
2. **Integrazione SDK**: Esempi di codice che seguono i modelli ufficiali
3. **Prerequisiti**: Istruzioni passo-passo per la configurazione
4. **Utilizzo**: Come eseguire e personalizzare il notebook
5. **Alias dei modelli**: Spiegazione delle varianti ottimizzate per l’hardware
6. **Risoluzione dei problemi**: Problemi comuni e soluzioni
7. **Estensioni**: Come aggiungere intenti, modelli e logica personalizzata
8. **Consigli sulle prestazioni**: Best practice per l’uso in produzione
9. **Risorse**: Collegamenti alla documentazione ufficiale e alla community

## Implementazione del Modello SDK

### Modello ufficiale (dai documenti di Foundry Local)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### La nostra implementazione (in workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Vantaggi del nostro approccio:**
- ✅ Segue esattamente il modello ufficiale dell’SDK
- ✅ Aggiunge caching per evitare inizializzazioni ripetute
- ✅ Include logica di retry per una maggiore robustezza in produzione
- ✅ Supporta il monitoraggio dell’utilizzo dei token
- ✅ Fornisce messaggi di errore migliori
- ✅ Rimane compatibile con gli esempi ufficiali

## Modifiche al Catalogo dei Modelli

### Prima
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Dopo
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Motivo:** Sostituito 'gpt-oss-20b' (alias non standard) con 'phi-3.5-mini' (alias ufficiale di Foundry Local).

## Dipendenze

### Aggiornato requirements.txt

Il file requirements.txt del Workshop include già:
```
foundry-local-sdk
openai>=1.30.0
```

Questi sono gli unici pacchetti necessari per l’integrazione con Foundry Local.

## Test degli Aggiornamenti

### 1. Verifica che Foundry Local sia in esecuzione

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Controlla i modelli disponibili

```bash
foundry model ls
```

Assicurati che questi modelli siano disponibili o verranno scaricati automaticamente:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Esegui il Notebook

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Oppure aprilo in VS Code ed esegui tutte le celle.

### 4. Comportamento previsto

**Cella 1 (Installazione):** Installazione dei pacchetti completata con successo  
**Cella 2 (Configurazione):** Nessun errore, importazioni funzionanti  
**Cella 3 (Verifica):** Mostra ✓ con l’elenco dei modelli  
**Cella 4 (Test Intent):** Mostra i risultati del rilevamento dell’intento  
**Cella 5 (Router):** Mostra ✓ Funzione di routing pronta  
**Cella 6 (Esecuzione):** Instrada i prompt ai modelli, mostra i risultati  

### 5. Risoluzione dei problemi di connessione

Se vedi `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Variabili d’Ambiente

Le seguenti variabili d’ambiente sono supportate:

| Variabile | Predefinito | Descrizione |
|-----------|-------------|-------------|
| `SHOW_USAGE` | `0` | Imposta a `1` per stampare l’utilizzo dei token |
| `RETRY_ON_FAIL` | `1` | Abilita la logica di retry |
| `RETRY_BACKOFF` | `1.0` | Ritardo iniziale del retry (secondi) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Sovrascrive l’endpoint del servizio |

### Esempi di utilizzo

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migrazione dal Vecchio Modello

Se hai codice esistente che utilizza chiamate API dirette, ecco come migrare:

### Prima (API Diretta)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### Dopo (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Vantaggi della Migrazione
- ✅ Gestione automatica del servizio
- ✅ Risoluzione degli alias dei modelli
- ✅ Selezione dell’ottimizzazione hardware
- ✅ Migliore gestione degli errori
- ✅ Compatibilità con l’SDK OpenAI
- ✅ Supporto allo streaming

## Riferimenti

### Documentazione ufficiale
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Sorgente Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Riferimento CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Risoluzione dei problemi**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Risorse del Workshop
- **Sessione 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Notebook di esempio**: `Workshop/notebooks/session06_models_router.ipynb`

### Community
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Prossimi Passi

1. **Rivedi le modifiche**: Leggi i file aggiornati
2. **Testa il Notebook**: Esegui session06_models_router.ipynb
3. **Verifica l’SDK**: Assicurati che foundry-local-sdk sia installato
4. **Controlla il Servizio**: Conferma che Foundry Local sia in esecuzione
5. **Esplora la Documentazione**: Leggi il nuovo session06_README.md

## Sommario

Questi aggiornamenti assicurano che i materiali del Workshop seguano esattamente i **modelli ufficiali del Foundry Local SDK** come documentato nel repository GitHub. Tutti gli esempi di codice, la documentazione e le utility ora sono allineati alle best practice raccomandate da Microsoft per il deployment locale di modelli AI.

Le modifiche migliorano:
- ✅ **Correttezza**: Utilizzo dei modelli ufficiali dell’SDK
- ✅ **Documentazione**: Spiegazioni ed esempi completi
- ✅ **Gestione degli errori**: Messaggi migliori e guida alla risoluzione dei problemi
- ✅ **Manutenibilità**: Conformità alle convenzioni ufficiali
- ✅ **Esperienza utente**: Istruzioni più chiare e aiuto per il debug

---

**Aggiornato:** 8 ottobre 2025  
**Versione SDK:** foundry-local-sdk (ultima)  
**Branch del Workshop:** Reactor

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.