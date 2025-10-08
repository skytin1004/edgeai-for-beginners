<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-08T15:29:37+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "ro"
}
-->
# Note de Migrare pentru SDK-ul Local Foundry

## Prezentare Generală

Toate fișierele Python din folderul Workshop au fost actualizate pentru a urma cele mai recente modele din [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Rezumatul Modificărilor

### Infrastructură de Bază (`workshop_utils.py`)

#### Funcționalități Îmbunătățite:
- **Suport pentru Suprascrierea Endpoint-ului**: Adăugat suport pentru variabila de mediu `FOUNDRY_LOCAL_ENDPOINT`
- **Gestionare Îmbunătățită a Erorilor**: Gestionare mai bună a excepțiilor cu mesaje de eroare detaliate
- **Caching Îmbunătățit**: Cheile de cache includ acum endpoint-ul pentru scenarii cu mai multe endpoint-uri
- **Backoff Exponențial**: Logica de retry utilizează acum backoff exponențial pentru o fiabilitate mai mare
- **Adnotări de Tip**: Adăugate adnotări de tip cuprinzătoare pentru suport mai bun în IDE

#### Capacități Noi:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Aplicații de Exemplu

#### Sesiunea 01: Bootstrap Chat (`chat_bootstrap.py`)
- Modelul implicit actualizat de la `phi-3.5-mini` la `phi-4-mini`
- Adăugat suport pentru suprascrierea endpoint-ului
- Documentație îmbunătățită cu referințe la SDK

#### Sesiunea 02: Pipeline RAG (`rag_pipeline.py`)
- Actualizat pentru a utiliza `phi-4-mini` ca model implicit
- Adăugat suport pentru suprascrierea endpoint-ului
- Documentație îmbunătățită cu detalii despre variabilele de mediu

#### Sesiunea 02: Evaluare RAG (`rag_eval_ragas.py`)
- Actualizate valorile implicite ale modelului
- Adăugat configurarea endpoint-ului
- Gestionare îmbunătățită a erorilor

#### Sesiunea 03: Benchmarking (`benchmark_oss_models.py`)
- Lista de modele implicite actualizată pentru a include `phi-4-mini`
- Documentație cuprinzătoare despre variabilele de mediu adăugată
- Documentația funcțiilor îmbunătățită
- Suport pentru suprascrierea endpoint-ului adăugat

#### Sesiunea 04: Compararea Modelului (`model_compare.py`)
- Modelul LLM implicit actualizat de la `gpt-oss-20b` la `qwen2.5-7b`
- Configurarea endpoint-ului adăugată
- Documentație îmbunătățită

#### Sesiunea 05: Orchestrarea Multi-Agent (`agents_orchestrator.py`)
- Adăugate adnotări de tip (modificat `str | None` la `Optional[str]`)
- Documentația clasei Agent îmbunătățită
- Suport pentru suprascrierea endpoint-ului adăugat
- Model de inițializare îmbunătățit

#### Sesiunea 06: Router de Model (`models_router.py`)
- Configurarea endpoint-ului adăugată
- Documentația pentru detectarea intenției îmbunătățită
- Documentația logicii de rutare îmbunătățită

#### Sesiunea 06: Pipeline (`models_pipeline.py`)
- Documentație cuprinzătoare a funcțiilor adăugată
- Documentație pas cu pas îmbunătățită
- Gestionare îmbunătățită a erorilor

### Scripturi

#### Export Benchmark (`export_benchmark_markdown.py`)
- Suport pentru suprascrierea endpoint-ului adăugat
- Modele implicite actualizate
- Documentația funcțiilor îmbunătățită
- Gestionare îmbunătățită a erorilor

#### CLI Linter (`lint_markdown_cli.py`)
- Link-uri de referință la SDK adăugate
- Documentația utilizării îmbunătățită

### Teste

#### Teste de Fum (`smoke.py`)
- Suport pentru suprascrierea endpoint-ului adăugat
- Documentația îmbunătățită
- Documentația cazurilor de test îmbunătățită
- Raportare mai bună a erorilor

## Variabile de Mediu

Toate exemplele suportă acum aceste variabile de mediu:

### Configurare de Bază
- `FOUNDRY_LOCAL_ALIAS` - Alias-ul modelului utilizat (implicit variază în funcție de exemplu)
- `FOUNDRY_LOCAL_ENDPOINT` - Suprascrierea endpoint-ului serviciului (opțional)
- `SHOW_USAGE` - Afișează statistici de utilizare a token-urilor (implicit: "0")
- `RETRY_ON_FAIL` - Activează logica de retry (implicit: "1")
- `RETRY_BACKOFF` - Întârzierea inițială pentru retry în secunde (implicit: "1.0")

### Specific pentru Exemple
- `EMBED_MODEL` - Model de embedding pentru exemplele RAG
- `BENCH_MODELS` - Modele separate prin virgulă pentru benchmarking
- `BENCH_ROUNDS` - Numărul de runde de benchmark
- `BENCH_PROMPT` - Prompt de test pentru benchmark-uri
- `BENCH_STREAM` - Măsoară latența primului token
- `RAG_QUESTION` - Întrebare de test pentru exemplele RAG
- `AGENT_MODEL_PRIMARY` - Modelul agentului principal
- `AGENT_MODEL_EDITOR` - Modelul agentului editor
- `SLM_ALIAS` - Alias-ul modelului de limbaj mic
- `LLM_ALIAS` - Alias-ul modelului de limbaj mare

## Cele Mai Bune Practici SDK Implementate

### 1. Inițializare Corectă a Clientului
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

### 2. Recuperarea Informațiilor despre Model
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Gestionarea Erorilor
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logica de Retry cu Backoff Exponențial
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

### 5. Suport pentru Streaming
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

## Ghid de Migrare pentru Exemple Personalizate

Dacă creați exemple noi sau actualizați unele existente:

1. **Utilizați ajutoarele din `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Suportați suprascrierea endpoint-ului**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Adăugați documentație cuprinzătoare**:
   - Variabile de mediu în docstring
   - Link de referință la SDK
   - Exemple de utilizare

4. **Utilizați adnotări de tip**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementați gestionarea corectă a erorilor**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testare

Toate exemplele pot fi testate cu:

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

## Referințe la Documentația SDK

- **Repository Principal**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Documentația API**: Verificați repository-ul SDK pentru cele mai recente documentații API

## Modificări Majore

### Niciuna Așteptată
Toate modificările sunt compatibile retroactiv. Actualizările includ în principal:
- Adăugarea de funcționalități opționale noi (suprascrierea endpoint-ului)
- Îmbunătățirea gestionării erorilor
- Îmbunătățirea documentației
- Actualizarea numelor implicite ale modelelor conform recomandărilor curente

### Îmbunătățiri Opționale
Este posibil să doriți să vă actualizați codul pentru a utiliza:
- `FOUNDRY_LOCAL_ENDPOINT` pentru control explicit al endpoint-ului
- `SHOW_USAGE=1` pentru vizibilitatea utilizării token-urilor
- Modele implicite actualizate (`phi-4-mini` în loc de `phi-3.5-mini`)

## Probleme Comune & Soluții

### Problemă: "Inițializarea clientului a eșuat"
**Soluție**: Asigurați-vă că serviciul Foundry Local rulează:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problemă: "Modelul nu a fost găsit"
**Soluție**: Verificați modelele disponibile:
```bash
foundry model list
```

### Problemă: Erori de conexiune la endpoint
**Soluție**: Verificați endpoint-ul:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Pași Următori

1. **Actualizați exemplele din Module08**: Aplicați modele similare la Module08/samples
2. **Adăugați teste de integrare**: Creați o suită de teste cuprinzătoare
3. **Benchmarking de performanță**: Comparați performanța înainte/după
4. **Actualizări ale documentației**: Actualizați README-ul principal cu noile modele

## Ghid pentru Contribuții

Când adăugați exemple noi:
1. Utilizați `workshop_utils.py` pentru consistență
2. Urmați modelul din exemplele existente
3. Adăugați docstring-uri cuprinzătoare
4. Includeți link-uri de referință la SDK
5. Suportați suprascrierea endpoint-ului
6. Adăugați adnotări de tip corecte
7. Includeți exemple de utilizare în docstring

## Compatibilitate Versiuni

Aceste actualizări sunt compatibile cu:
- `foundry-local-sdk` (ultima versiune)
- `openai>=1.30.0`
- Python 3.8+

---

**Ultima Actualizare**: 2025-01-08  
**Responsabil**: Echipa EdgeAI Workshop  
**Versiunea SDK**: Foundry Local SDK (ultima 0.7.117+67073234e7)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.