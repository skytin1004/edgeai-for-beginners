<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-09T21:42:59+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "cs"
}
-->
# Poznámky k migraci Foundry Local SDK

## Přehled

Všechny soubory Python ve složce Workshop byly aktualizovány podle nejnovějších vzorů z oficiálního [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Shrnutí změn

### Základní infrastruktura (`workshop_utils.py`)

#### Vylepšené funkce:
- **Podpora přepsání endpointu**: Přidána podpora proměnné prostředí `FOUNDRY_LOCAL_ENDPOINT`
- **Vylepšené zpracování chyb**: Lepší zpracování výjimek s podrobnými chybovými zprávami
- **Vylepšené ukládání do mezipaměti**: Klíče mezipaměti nyní zahrnují endpoint pro scénáře s více endpointy
- **Exponenciální zpoždění**: Logika opakování nyní používá exponenciální zpoždění pro vyšší spolehlivost
- **Typové anotace**: Přidány komplexní typové anotace pro lepší podporu v IDE

#### Nové schopnosti:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Ukázkové aplikace

#### Sezení 01: Chat Bootstrap (`chat_bootstrap.py`)
- Aktualizován výchozí model z `phi-3.5-mini` na `phi-4-mini`
- Přidána podpora přepsání endpointu
- Vylepšena dokumentace s odkazy na SDK

#### Sezení 02: RAG Pipeline (`rag_pipeline.py`)
- Aktualizováno na použití `phi-4-mini` jako výchozího modelu
- Přidána podpora přepsání endpointu
- Vylepšena dokumentace s detaily o proměnných prostředí

#### Sezení 02: RAG Evaluation (`rag_eval_ragas.py`)
- Aktualizovány výchozí modely
- Přidána konfigurace endpointu
- Vylepšeno zpracování chyb

#### Sezení 03: Benchmarking (`benchmark_oss_models.py`)
- Aktualizován seznam výchozích modelů, včetně `phi-4-mini`
- Přidána komplexní dokumentace proměnných prostředí
- Vylepšena dokumentace funkcí
- Přidána podpora přepsání endpointu

#### Sezení 04: Porovnání modelů (`model_compare.py`)
- Aktualizován výchozí LLM z `gpt-oss-20b` na `qwen2.5-7b`
- Přidána konfigurace endpointu
- Vylepšena dokumentace

#### Sezení 05: Orchestrace více agentů (`agents_orchestrator.py`)
- Přidány typové anotace (změna `str | None` na `Optional[str]`)
- Vylepšena dokumentace třídy Agent
- Přidána podpora přepsání endpointu
- Vylepšen vzor inicializace

#### Sezení 06: Směrování modelů (`models_router.py`)
- Přidána konfigurace endpointu
- Vylepšena dokumentace detekce záměru
- Vylepšena dokumentace logiky směrování

#### Sezení 06: Pipeline (`models_pipeline.py`)
- Přidána komplexní dokumentace funkcí
- Vylepšena dokumentace krok za krokem
- Vylepšeno zpracování chyb

### Skripty

#### Export benchmarků (`export_benchmark_markdown.py`)
- Přidána podpora přepsání endpointu
- Aktualizovány výchozí modely
- Vylepšena dokumentace funkcí
- Vylepšeno zpracování chyb

#### CLI Linter (`lint_markdown_cli.py`)
- Přidány odkazy na SDK
- Vylepšena dokumentace použití

### Testy

#### Smoke testy (`smoke.py`)
- Přidána podpora přepsání endpointu
- Vylepšena dokumentace
- Vylepšena dokumentace testovacích případů
- Lepší hlášení chyb

## Proměnné prostředí

Všechny ukázky nyní podporují tyto proměnné prostředí:

### Základní konfigurace
- `FOUNDRY_LOCAL_ALIAS` - Alias modelu k použití (výchozí se liší podle ukázky)
- `FOUNDRY_LOCAL_ENDPOINT` - Přepsání endpointu služby (volitelné)
- `SHOW_USAGE` - Zobrazení statistik využití tokenů (výchozí: "0")
- `RETRY_ON_FAIL` - Povolení logiky opakování (výchozí: "1")
- `RETRY_BACKOFF` - Počáteční zpoždění opakování v sekundách (výchozí: "1.0")

### Specifické pro ukázky
- `EMBED_MODEL` - Model pro vkládání pro ukázky RAG
- `BENCH_MODELS` - Modely oddělené čárkou pro benchmarking
- `BENCH_ROUNDS` - Počet kol benchmarkingu
- `BENCH_PROMPT` - Testovací prompt pro benchmarking
- `BENCH_STREAM` - Měření latence prvního tokenu
- `RAG_QUESTION` - Testovací otázka pro ukázky RAG
- `AGENT_MODEL_PRIMARY` - Primární model agenta
- `AGENT_MODEL_EDITOR` - Editor modelu agenta
- `SLM_ALIAS` - Alias malého jazykového modelu
- `LLM_ALIAS` - Alias velkého jazykového modelu

## Implementované osvědčené postupy SDK

### 1. Správná inicializace klienta
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

### 2. Získání informací o modelu
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Zpracování chyb
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logika opakování s exponenciálním zpožděním
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

### 5. Podpora streamování
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

## Průvodce migrací pro vlastní ukázky

Pokud vytváříte nové ukázky nebo aktualizujete stávající:

1. **Používejte pomocné funkce z `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Podporujte přepsání endpointu**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Přidejte komplexní dokumentaci**:
   - Proměnné prostředí v docstringu
   - Odkaz na SDK
   - Příklady použití

4. **Používejte typové anotace**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementujte správné zpracování chyb**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testování

Všechny ukázky lze testovat pomocí:

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

## Odkazy na dokumentaci SDK

- **Hlavní repozitář**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API dokumentace**: Podívejte se na repozitář SDK pro nejnovější dokumentaci API

## Změny, které mohou způsobit problémy

### Neočekávají se žádné
Všechny změny jsou zpětně kompatibilní. Aktualizace primárně:
- Přidávají nové volitelné funkce (přepsání endpointu)
- Zlepšují zpracování chyb
- Vylepšují dokumentaci
- Aktualizují výchozí názvy modelů podle aktuálních doporučení

### Volitelná vylepšení
Možná budete chtít aktualizovat svůj kód na použití:
- `FOUNDRY_LOCAL_ENDPOINT` pro explicitní kontrolu endpointu
- `SHOW_USAGE=1` pro viditelnost využití tokenů
- Aktualizované výchozí modely (`phi-4-mini` místo `phi-3.5-mini`)

## Běžné problémy a jejich řešení

### Problém: "Inicializace klienta selhala"
**Řešení**: Ujistěte se, že služba Foundry Local běží:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problém: "Model nebyl nalezen"
**Řešení**: Zkontrolujte dostupné modely:
```bash
foundry model list
```

### Problém: Chyby připojení k endpointu
**Řešení**: Ověřte endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Další kroky

1. **Aktualizujte ukázky Module08**: Použijte podobné vzory pro Module08/samples
2. **Přidejte integrační testy**: Vytvořte komplexní testovací sadu
3. **Benchmarking výkonu**: Porovnejte výkon před/po
4. **Aktualizace dokumentace**: Aktualizujte hlavní README s novými vzory

## Pokyny pro přispěvatele

Při přidávání nových ukázek:
1. Používejte `workshop_utils.py` pro konzistenci
2. Dodržujte vzor v existujících ukázkách
3. Přidejte komplexní docstringy
4. Zahrňte odkazy na SDK
5. Podporujte přepsání endpointu
6. Přidejte správné typové anotace
7. Zahrňte příklady použití v docstringu

## Kompatibilita verzí

Tyto aktualizace jsou kompatibilní s:
- `foundry-local-sdk` (nejnovější)
- `openai>=1.30.0`
- Python 3.8+

---

**Poslední aktualizace**: 8. ledna 2025  
**Správce**: Tým EdgeAI Workshop  
**Verze SDK**: Foundry Local SDK (nejnovější 0.7.117+67073234e7)

---

**Upozornění**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.