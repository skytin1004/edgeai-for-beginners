<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-09T21:42:32+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "hu"
}
-->
# Foundry Local SDK Migrációs Jegyzetek

## Áttekintés

A Workshop mappában található összes Python fájl frissítve lett, hogy kövesse a hivatalos [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) legújabb mintáit.

## Változások összefoglalása

### Alapvető infrastruktúra (`workshop_utils.py`)

#### Fejlesztett funkciók:
- **Végpont felülírás támogatása**: Hozzáadva a `FOUNDRY_LOCAL_ENDPOINT` környezeti változó támogatása
- **Jobb hibakezelés**: Részletesebb hibaüzenetekkel ellátott kivételkezelés
- **Fejlesztett gyorsítótárazás**: A gyorsítótár kulcsai most már tartalmazzák a végpontot több végpontú forgatókönyvekhez
- **Exponenciális visszaállás**: Az újrapróbálkozási logika exponenciális visszaállást használ a megbízhatóság érdekében
- **Típusannotációk**: Átfogó típusjelölések hozzáadva a jobb IDE támogatás érdekében

#### Új képességek:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Példa alkalmazások

#### 01. szekció: Chat Bootstrap (`chat_bootstrap.py`)
- Az alapértelmezett modell frissítve: `phi-3.5-mini` helyett `phi-4-mini`
- Végpont felülírás támogatása hozzáadva
- Dokumentáció bővítése SDK hivatkozásokkal

#### 02. szekció: RAG Pipeline (`rag_pipeline.py`)
- Frissítve, hogy alapértelmezés szerint a `phi-4-mini` modellt használja
- Végpont felülírás támogatása hozzáadva
- Dokumentáció bővítése környezeti változó részletekkel

#### 02. szekció: RAG Értékelés (`rag_eval_ragas.py`)
- Modell alapértelmezések frissítése
- Végpont konfiguráció hozzáadva
- Jobb hibakezelés

#### 03. szekció: Benchmarking (`benchmark_oss_models.py`)
- Az alapértelmezett modell lista frissítése, beleértve a `phi-4-mini` modellt
- Átfogó környezeti változó dokumentáció hozzáadva
- Funkció dokumentáció javítása
- Végpont felülírás támogatása mindenhol

#### 04. szekció: Modell összehasonlítás (`model_compare.py`)
- Az alapértelmezett LLM frissítése: `gpt-oss-20b` helyett `qwen2.5-7b`
- Végpont konfiguráció hozzáadva
- Dokumentáció bővítése

#### 05. szekció: Többügynökös Orkesztráció (`agents_orchestrator.py`)
- Típusjelölések hozzáadása (a `str | None` helyett `Optional[str]`)
- Az Agent osztály dokumentációjának bővítése
- Végpont felülírás támogatása hozzáadva
- Javított inicializálási minta

#### 06. szekció: Modell Router (`models_router.py`)
- Végpont konfiguráció hozzáadva
- Szándékfelismerés dokumentációjának bővítése
- Javított útválasztási logika dokumentáció

#### 06. szekció: Pipeline (`models_pipeline.py`)
- Átfogó funkció dokumentáció hozzáadva
- Lépésről lépésre dokumentáció javítása
- Jobb hibakezelés

### Szkriptek

#### Benchmark Export (`export_benchmark_markdown.py`)
- Végpont felülírás támogatása hozzáadva
- Alapértelmezett modellek frissítése
- Funkció dokumentáció bővítése
- Jobb hibakezelés

#### CLI Linter (`lint_markdown_cli.py`)
- SDK hivatkozási linkek hozzáadása
- Használati dokumentáció javítása

### Tesztek

#### Smoke Tesztek (`smoke.py`)
- Végpont felülírás támogatása hozzáadva
- Dokumentáció bővítése
- Tesztesetek dokumentációjának javítása
- Jobb hiba jelentés

## Környezeti változók

Minden minta támogatja az alábbi környezeti változókat:

### Alapvető konfiguráció
- `FOUNDRY_LOCAL_ALIAS` - Használandó modell alias (minta szerint változik)
- `FOUNDRY_LOCAL_ENDPOINT` - Szolgáltatás végpontjának felülírása (opcionális)
- `SHOW_USAGE` - Token használati statisztikák megjelenítése (alapértelmezett: "0")
- `RETRY_ON_FAIL` - Újrapróbálkozási logika engedélyezése (alapértelmezett: "1")
- `RETRY_BACKOFF` - Kezdeti újrapróbálkozási késleltetés másodpercben (alapértelmezett: "1.0")

### Minta-specifikus
- `EMBED_MODEL` - Beágyazási modell RAG mintákhoz
- `BENCH_MODELS` - Benchmarkinghoz használt modellek vesszővel elválasztva
- `BENCH_ROUNDS` - Benchmark körök száma
- `BENCH_PROMPT` - Teszt prompt benchmarkokhoz
- `BENCH_STREAM` - Első token késleltetés mérése
- `RAG_QUESTION` - Teszt kérdés RAG mintákhoz
- `AGENT_MODEL_PRIMARY` - Elsődleges ügynök modell
- `AGENT_MODEL_EDITOR` - Szerkesztő ügynök modell
- `SLM_ALIAS` - Kis nyelvi modell alias
- `LLM_ALIAS` - Nagy nyelvi modell alias

## SDK Legjobb Gyakorlatok Megvalósítva

### 1. Helyes kliens inicializálás
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

### 2. Modell információ lekérése
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Hibakezelés
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Újrapróbálkozási logika exponenciális visszaállással
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

### 5. Streaming támogatás
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

## Migrációs útmutató egyedi mintákhoz

Ha új mintákat hoz létre vagy meglévőket frissít:

1. **Használja a `workshop_utils.py` segédfunkcióit**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Támogassa a végpont felülírást**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Adjon hozzá átfogó dokumentációt**:
   - Környezeti változók a docstringben
   - SDK hivatkozási link
   - Használati példák

4. **Használjon típusjelöléseket**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Valósítson meg megfelelő hibakezelést**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Tesztelés

Minden minta tesztelhető az alábbiakkal:

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

## SDK Dokumentációs Hivatkozások

- **Fő Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Dokumentáció**: Az SDK repository-ban található legfrissebb API dokumentáció

## Kompatibilitást Megszakító Változások

### Nem várható
Minden változás visszafelé kompatibilis. A frissítések elsősorban:
- Új opcionális funkciókat adnak hozzá (végpont felülírás)
- Javítják a hibakezelést
- Bővítik a dokumentációt
- Frissítik az alapértelmezett modell neveket az aktuális ajánlások szerint

### Opcionális fejlesztések
Érdemes lehet frissíteni a kódot az alábbiak használatára:
- `FOUNDRY_LOCAL_ENDPOINT` az explicit végpont vezérléshez
- `SHOW_USAGE=1` a token használat láthatóságához
- Frissített modell alapértelmezések (`phi-4-mini` a `phi-3.5-mini` helyett)

## Gyakori problémák és megoldások

### Probléma: "Kliens inicializálása sikertelen"
**Megoldás**: Győződjön meg róla, hogy a Foundry Local szolgáltatás fut:
```bash
foundry service start
foundry model run phi-4-mini
```

### Probléma: "Modell nem található"
**Megoldás**: Ellenőrizze az elérhető modelleket:
```bash
foundry model list
```

### Probléma: Végpont csatlakozási hibák
**Megoldás**: Ellenőrizze a végpontot:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Következő lépések

1. **Frissítse a Module08 mintákat**: Alkalmazzon hasonló mintákat a Module08/samples mappában
2. **Adjon hozzá integrációs teszteket**: Hozzon létre átfogó tesztcsomagot
3. **Teljesítmény benchmarking**: Hasonlítsa össze a frissítés előtti és utáni teljesítményt
4. **Dokumentáció frissítések**: Frissítse a fő README-t az új mintákkal

## Hozzájárulási irányelvek

Új minták hozzáadásakor:
1. Használja a `workshop_utils.py` segédfunkcióit a konzisztencia érdekében
2. Kövesse a meglévő minták mintáját
3. Adjon hozzá átfogó docstringeket
4. Tartalmazzon SDK hivatkozási linkeket
5. Támogassa a végpont felülírást
6. Adjon hozzá megfelelő típusjelöléseket
7. Tartalmazzon használati példákat a docstringben

## Verzió kompatibilitás

Ezek a frissítések kompatibilisek az alábbiakkal:
- `foundry-local-sdk` (legújabb)
- `openai>=1.30.0`
- Python 3.8+

---

**Utolsó frissítés**: 2025-01-08  
**Karbantartó**: EdgeAI Workshop Team  
**SDK Verzió**: Foundry Local SDK (legújabb 0.7.117+67073234e7)

---

**Felelősségkizárás**:  
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítószolgáltatás segítségével fordították le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.