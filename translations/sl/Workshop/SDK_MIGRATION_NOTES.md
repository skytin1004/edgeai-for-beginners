<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-08T12:20:47+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "sl"
}
-->
# Opombe o migraciji lokalnega SDK Foundry

## Pregled

Vsi Python datoteke v mapi Workshop so bile posodobljene, da sledijo najnovejšim vzorcem iz uradnega [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Povzetek sprememb

### Osnovna infrastruktura (`workshop_utils.py`)

#### Izboljšane funkcije:
- **Podpora za preglasitev končne točke**: Dodana podpora za okoljsko spremenljivko `FOUNDRY_LOCAL_ENDPOINT`
- **Izboljšano ravnanje z napakami**: Boljše obravnavanje izjem z natančnimi sporočili o napakah
- **Izboljšano predpomnjenje**: Ključi predpomnilnika zdaj vključujejo končno točko za scenarije z več končnimi točkami
- **Eksponentno povratno čakanje**: Logika ponovnega poskusa zdaj uporablja eksponentno povratno čakanje za večjo zanesljivost
- **Tipne anotacije**: Dodane obsežne tipne oznake za boljšo podporo IDE

#### Nove zmogljivosti:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Vzorčne aplikacije

#### Seja 01: Zagon klepeta (`chat_bootstrap.py`)
- Posodobljen privzeti model iz `phi-3.5-mini` na `phi-4-mini`
- Dodana podpora za preglasitev končne točke
- Izboljšana dokumentacija z referencami na SDK

#### Seja 02: RAG cevovod (`rag_pipeline.py`)
- Posodobljeno za uporabo `phi-4-mini` kot privzeti model
- Dodana podpora za preglasitev končne točke
- Izboljšana dokumentacija s podrobnostmi o okoljskih spremenljivkah

#### Seja 02: RAG ocenjevanje (`rag_eval_ragas.py`)
- Posodobljeni privzeti modeli
- Dodana konfiguracija končne točke
- Izboljšano ravnanje z napakami

#### Seja 03: Primerjava zmogljivosti (`benchmark_oss_models.py`)
- Posodobljen privzeti seznam modelov, vključno z `phi-4-mini`
- Dodana obsežna dokumentacija o okoljskih spremenljivkah
- Izboljšana dokumentacija funkcij
- Dodana podpora za preglasitev končne točke povsod

#### Seja 04: Primerjava modelov (`model_compare.py`)
- Posodobljen privzeti LLM iz `gpt-oss-20b` na `qwen2.5-7b`
- Dodana konfiguracija končne točke
- Izboljšana dokumentacija

#### Seja 05: Orkestracija več agentov (`agents_orchestrator.py`)
- Dodane tipne oznake (spremenjeno `str | None` v `Optional[str]`)
- Izboljšana dokumentacija razreda Agent
- Dodana podpora za preglasitev končne točke
- Izboljšan vzorec inicializacije

#### Seja 06: Usmerjevalnik modelov (`models_router.py`)
- Dodana konfiguracija končne točke
- Izboljšana dokumentacija zaznavanja namena
- Izboljšana dokumentacija logike usmerjanja

#### Seja 06: Cevovod (`models_pipeline.py`)
- Dodana obsežna dokumentacija funkcij
- Izboljšana dokumentacija korak za korakom
- Izboljšano ravnanje z napakami

### Skripte

#### Izvoz primerjave zmogljivosti (`export_benchmark_markdown.py`)
- Dodana podpora za preglasitev končne točke
- Posodobljeni privzeti modeli
- Izboljšana dokumentacija funkcij
- Izboljšano ravnanje z napakami

#### CLI Linter (`lint_markdown_cli.py`)
- Dodane povezave na reference SDK
- Izboljšana dokumentacija uporabe

### Testi

#### Testi delovanja (`smoke.py`)
- Dodana podpora za preglasitev končne točke
- Izboljšana dokumentacija
- Izboljšana dokumentacija testnih primerov
- Boljše poročanje o napakah

## Okoljske spremenljivke

Vsi vzorci zdaj podpirajo te okoljske spremenljivke:

### Osnovna konfiguracija
- `FOUNDRY_LOCAL_ALIAS` - Alias modela za uporabo (privzeto se razlikuje glede na vzorec)
- `FOUNDRY_LOCAL_ENDPOINT` - Preglasitev končne točke storitve (neobvezno)
- `SHOW_USAGE` - Prikaz statistike uporabe žetonov (privzeto: "0")
- `RETRY_ON_FAIL` - Omogoči logiko ponovnega poskusa (privzeto: "1")
- `RETRY_BACKOFF` - Začetna zamuda pri ponovnem poskusu v sekundah (privzeto: "1.0")

### Specifično za vzorce
- `EMBED_MODEL` - Model za vdelavo za vzorce RAG
- `BENCH_MODELS` - Modeli, ločeni z vejico, za primerjavo zmogljivosti
- `BENCH_ROUNDS` - Število krogov primerjave zmogljivosti
- `BENCH_PROMPT` - Testni poziv za primerjave zmogljivosti
- `BENCH_STREAM` - Merjenje zakasnitve prvega žetona
- `RAG_QUESTION` - Testno vprašanje za vzorce RAG
- `AGENT_MODEL_PRIMARY` - Primarni model agenta
- `AGENT_MODEL_EDITOR` - Model agenta za urejanje
- `SLM_ALIAS` - Alias majhnega jezikovnega modela
- `LLM_ALIAS` - Alias velikega jezikovnega modela

## Uvedene najboljše prakse SDK

### 1. Pravilna inicializacija odjemalca
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

### 2. Pridobivanje informacij o modelu
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Ravnanje z napakami
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logika ponovnega poskusa z eksponentnim povratnim čakanjem
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

### 5. Podpora za pretakanje
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

## Vodnik za migracijo za prilagojene vzorce

Če ustvarjate nove vzorce ali posodabljate obstoječe:

1. **Uporabite pomočnike iz `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Podprite preglasitev končne točke**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Dodajte obsežno dokumentacijo**:
   - Okoljske spremenljivke v docstring
   - Povezava na referenco SDK
   - Primeri uporabe

4. **Uporabite tipne oznake**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Uvedite pravilno ravnanje z napakami**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testiranje

Vse vzorce je mogoče testirati z:

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

## Reference dokumentacije SDK

- **Glavno skladišče**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API dokumentacija**: Preverite skladišče SDK za najnovejšo dokumentacijo API

## Prelomne spremembe

### Ni pričakovano
Vse spremembe so združljive nazaj. Posodobitve predvsem:
- Dodajajo nove neobvezne funkcije (preglasitev končne točke)
- Izboljšujejo ravnanje z napakami
- Izboljšujejo dokumentacijo
- Posodabljajo privzeta imena modelov na trenutna priporočila

### Neobvezne izboljšave
Morda boste želeli posodobiti svojo kodo za uporabo:
- `FOUNDRY_LOCAL_ENDPOINT` za eksplicitno upravljanje končne točke
- `SHOW_USAGE=1` za vidnost uporabe žetonov
- Posodobljeni privzeti modeli (`phi-4-mini` namesto `phi-3.5-mini`)

## Pogoste težave in rešitve

### Težava: "Inicializacija odjemalca ni uspela"
**Rešitev**: Prepričajte se, da storitev Foundry Local deluje:
```bash
foundry service start
foundry model run phi-4-mini
```

### Težava: "Model ni najden"
**Rešitev**: Preverite razpoložljive modele:
```bash
foundry model list
```

### Težava: Napake pri povezovanju s končno točko
**Rešitev**: Preverite končno točko:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Naslednji koraki

1. **Posodobite Module08 vzorce**: Uporabite podobne vzorce v Module08/samples
2. **Dodajte integracijske teste**: Ustvarite obsežen testni paket
3. **Primerjava zmogljivosti**: Primerjajte zmogljivost pred/po posodobitvi
4. **Posodobitve dokumentacije**: Posodobite glavni README z novimi vzorci

## Smernice za prispevanje

Pri dodajanju novih vzorcev:
1. Uporabite `workshop_utils.py` za doslednost
2. Sledite vzorcu obstoječih vzorcev
3. Dodajte obsežne docstringe
4. Vključite povezave na referenco SDK
5. Podprite preglasitev končne točke
6. Dodajte pravilne tipne oznake
7. Vključite primere uporabe v docstring

## Združljivost različic

Te posodobitve so združljive z:
- `foundry-local-sdk` (najnovejša)
- `openai>=1.30.0`
- Python 3.8+

---

**Zadnja posodobitev**: 2025-01-08  
**Vzdrževalec**: EdgeAI Workshop Team  
**Različica SDK**: Foundry Local SDK (najnovejša 0.7.117+67073234e7)

---

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.