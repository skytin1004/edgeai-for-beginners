<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-08T15:29:11+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "sk"
}
-->
# Poznámky k migrácii Foundry Local SDK

## Prehľad

Všetky súbory Python v priečinku Workshop boli aktualizované tak, aby nasledovali najnovšie vzory z oficiálneho [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Zhrnutie zmien

### Základná infraštruktúra (`workshop_utils.py`)

#### Vylepšené funkcie:
- **Podpora pre prepísanie koncového bodu**: Pridaná podpora pre environmentálnu premennú `FOUNDRY_LOCAL_ENDPOINT`
- **Zlepšené spracovanie chýb**: Lepšie spracovanie výnimiek s podrobnými chybovými správami
- **Vylepšené cachovanie**: Cache kľúče teraz zahŕňajú koncový bod pre scenáre s viacerými koncovými bodmi
- **Exponenciálne oneskorenie**: Logika opakovania teraz používa exponenciálne oneskorenie pre lepšiu spoľahlivosť
- **Typové anotácie**: Pridané komplexné typové anotácie pre lepšiu podporu IDE

#### Nové schopnosti:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Ukážkové aplikácie

#### Session 01: Chat Bootstrap (`chat_bootstrap.py`)
- Aktualizovaný predvolený model z `phi-3.5-mini` na `phi-4-mini`
- Pridaná podpora pre prepísanie koncového bodu
- Vylepšená dokumentácia s odkazmi na SDK

#### Session 02: RAG Pipeline (`rag_pipeline.py`)
- Aktualizované na používanie `phi-4-mini` ako predvoleného modelu
- Pridaná podpora pre prepísanie koncového bodu
- Zlepšená dokumentácia s podrobnosťami o environmentálnych premenných

#### Session 02: RAG Evaluation (`rag_eval_ragas.py`)
- Aktualizované predvolené modely
- Pridaná konfigurácia koncového bodu
- Vylepšené spracovanie chýb

#### Session 03: Benchmarking (`benchmark_oss_models.py`)
- Aktualizovaný zoznam predvolených modelov, vrátane `phi-4-mini`
- Pridaná komplexná dokumentácia environmentálnych premenných
- Zlepšená dokumentácia funkcií
- Pridaná podpora pre prepísanie koncového bodu

#### Session 04: Porovnanie modelov (`model_compare.py`)
- Aktualizovaný predvolený LLM z `gpt-oss-20b` na `qwen2.5-7b`
- Pridaná konfigurácia koncového bodu
- Vylepšená dokumentácia

#### Session 05: Orchestrácia viacerých agentov (`agents_orchestrator.py`)
- Pridané typové anotácie (zmenené `str | None` na `Optional[str]`)
- Vylepšená dokumentácia triedy Agent
- Pridaná podpora pre prepísanie koncového bodu
- Zlepšený inicializačný vzor

#### Session 06: Router modelov (`models_router.py`)
- Pridaná konfigurácia koncového bodu
- Vylepšená dokumentácia detekcie zámerov
- Zlepšená dokumentácia logiky smerovania

#### Session 06: Pipeline (`models_pipeline.py`)
- Pridaná komplexná dokumentácia funkcií
- Zlepšená dokumentácia krok za krokom
- Vylepšené spracovanie chýb

### Skripty

#### Export benchmarkov (`export_benchmark_markdown.py`)
- Pridaná podpora pre prepísanie koncového bodu
- Aktualizované predvolené modely
- Vylepšená dokumentácia funkcií
- Zlepšené spracovanie chýb

#### CLI Linter (`lint_markdown_cli.py`)
- Pridané odkazy na SDK
- Zlepšená dokumentácia použitia

### Testy

#### Smoke Testy (`smoke.py`)
- Pridaná podpora pre prepísanie koncového bodu
- Vylepšená dokumentácia
- Zlepšená dokumentácia testovacích prípadov
- Lepšie hlásenie chýb

## Environmentálne premenné

Všetky ukážky teraz podporujú tieto environmentálne premenné:

### Základná konfigurácia
- `FOUNDRY_LOCAL_ALIAS` - Alias modelu na použitie (predvolené sa líši podľa ukážky)
- `FOUNDRY_LOCAL_ENDPOINT` - Prepísanie koncového bodu služby (voliteľné)
- `SHOW_USAGE` - Zobrazenie štatistík používania tokenov (predvolené: "0")
- `RETRY_ON_FAIL` - Povolenie logiky opakovania (predvolené: "1")
- `RETRY_BACKOFF` - Počiatočné oneskorenie opakovania v sekundách (predvolené: "1.0")

### Špecifické pre ukážky
- `EMBED_MODEL` - Model pre embedding pre RAG ukážky
- `BENCH_MODELS` - Modely oddelené čiarkou pre benchmarking
- `BENCH_ROUNDS` - Počet kôl benchmarkingu
- `BENCH_PROMPT` - Testovací prompt pre benchmarking
- `BENCH_STREAM` - Meranie latencie prvého tokenu
- `RAG_QUESTION` - Testovacia otázka pre RAG ukážky
- `AGENT_MODEL_PRIMARY` - Primárny model agenta
- `AGENT_MODEL_EDITOR` - Editor modelu agenta
- `SLM_ALIAS` - Alias malého jazykového modelu
- `LLM_ALIAS` - Alias veľkého jazykového modelu

## Implementované najlepšie praktiky SDK

### 1. Správna inicializácia klienta
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

### 2. Získanie informácií o modeli
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Spracovanie chýb
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logika opakovania s exponenciálnym oneskorením
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

### 5. Podpora streamovania
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

## Príručka migrácie pre vlastné ukážky

Ak vytvárate nové ukážky alebo aktualizujete existujúce:

1. **Používajte pomocné funkcie z `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Podporte prepísanie koncového bodu**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Pridajte komplexnú dokumentáciu**:
   - Environmentálne premenné v docstringu
   - Odkaz na SDK
   - Príklady použitia

4. **Používajte typové anotácie**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementujte správne spracovanie chýb**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testovanie

Všetky ukážky je možné testovať pomocou:

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

## Odkazy na dokumentáciu SDK

- **Hlavné úložisko**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API dokumentácia**: Pozrite si najnovšiu dokumentáciu API v úložisku SDK

## Zmeny, ktoré môžu narušiť kompatibilitu

### Neočakávané
Všetky zmeny sú spätne kompatibilné. Aktualizácie primárne:
- Pridávajú nové voliteľné funkcie (prepísanie koncového bodu)
- Zlepšujú spracovanie chýb
- Vylepšujú dokumentáciu
- Aktualizujú predvolené názvy modelov na aktuálne odporúčania

### Voliteľné vylepšenia
Môžete aktualizovať svoj kód na používanie:
- `FOUNDRY_LOCAL_ENDPOINT` pre explicitnú kontrolu koncového bodu
- `SHOW_USAGE=1` pre viditeľnosť používania tokenov
- Aktualizované predvolené modely (`phi-4-mini` namiesto `phi-3.5-mini`)

## Bežné problémy a riešenia

### Problém: "Inicializácia klienta zlyhala"
**Riešenie**: Uistite sa, že služba Foundry Local beží:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problém: "Model nebol nájdený"
**Riešenie**: Skontrolujte dostupné modely:
```bash
foundry model list
```

### Problém: Chyby pripojenia ku koncovému bodu
**Riešenie**: Overte koncový bod:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Ďalšie kroky

1. **Aktualizujte ukážky z Module08**: Použite podobné vzory v Module08/samples
2. **Pridajte integračné testy**: Vytvorte komplexný testovací balík
3. **Benchmarking výkonu**: Porovnajte výkon pred a po aktualizácii
4. **Aktualizácie dokumentácie**: Aktualizujte hlavný README s novými vzormi

## Pravidlá prispievania

Pri pridávaní nových ukážok:
1. Používajte `workshop_utils.py` pre konzistenciu
2. Nasledujte vzor existujúcich ukážok
3. Pridajte komplexné docstringy
4. Zahrňte odkazy na SDK
5. Podporte prepísanie koncového bodu
6. Pridajte správne typové anotácie
7. Zahrňte príklady použitia v docstringu

## Kompatibilita verzií

Tieto aktualizácie sú kompatibilné s:
- `foundry-local-sdk` (najnovšia verzia)
- `openai>=1.30.0`
- Python 3.8+

---

**Posledná aktualizácia**: 2025-01-08  
**Správca**: Tím EdgeAI Workshop  
**Verzia SDK**: Foundry Local SDK (najnovšia 0.7.117+67073234e7)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.