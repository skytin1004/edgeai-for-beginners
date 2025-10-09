<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-09T21:43:23+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "lt"
}
-->
# Foundry Local SDK Migracijos Pastabos

## Apžvalga

Visi Python failai, esantys Workshop aplanke, buvo atnaujinti pagal naujausius oficialaus [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) šablonus.

## Pakeitimų santrauka

### Pagrindinė infrastruktūra (`workshop_utils.py`)

#### Patobulintos funkcijos:
- **Endpoint Override Palaikymas**: Pridėtas `FOUNDRY_LOCAL_ENDPOINT` aplinkos kintamojo palaikymas
- **Patobulintas klaidų tvarkymas**: Geresnis išimčių tvarkymas su detalesnėmis klaidų žinutėmis
- **Patobulintas kešavimas**: Kešo raktai dabar apima endpoint informaciją, skirtą kelių endpoint scenarijams
- **Eksponentinis atidėjimas**: Pakartotinio bandymo logika dabar naudoja eksponentinį atidėjimą, siekiant didesnio patikimumo
- **Tipų anotacijos**: Pridėtos išsamios tipų užuominos, skirtos geresniam IDE palaikymui

#### Naujos galimybės:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Pavyzdinės programos

#### Sesija 01: Chat Bootstrap (`chat_bootstrap.py`)
- Atnaujintas numatytasis modelis iš `phi-3.5-mini` į `phi-4-mini`
- Pridėtas endpoint override palaikymas
- Patobulinta dokumentacija su SDK nuorodomis

#### Sesija 02: RAG Pipeline (`rag_pipeline.py`)
- Atnaujinta, kad naudotų `phi-4-mini` kaip numatytąjį
- Pridėtas endpoint override palaikymas
- Patobulinta dokumentacija su aplinkos kintamųjų detalėmis

#### Sesija 02: RAG Vertinimas (`rag_eval_ragas.py`)
- Atnaujinti modelių numatytieji nustatymai
- Pridėta endpoint konfigūracija
- Patobulintas klaidų tvarkymas

#### Sesija 03: Benchmarking (`benchmark_oss_models.py`)
- Atnaujintas numatytasis modelių sąrašas, įtraukiant `phi-4-mini`
- Pridėta išsami aplinkos kintamųjų dokumentacija
- Patobulinta funkcijų dokumentacija
- Pridėtas endpoint override palaikymas visame kode

#### Sesija 04: Modelių palyginimas (`model_compare.py`)
- Atnaujintas numatytasis LLM iš `gpt-oss-20b` į `qwen2.5-7b`
- Pridėta endpoint konfigūracija
- Patobulinta dokumentacija

#### Sesija 05: Multi-Agent Orchestration (`agents_orchestrator.py`)
- Pridėtos tipų užuominos (pakeista `str | None` į `Optional[str]`)
- Patobulinta Agent klasės dokumentacija
- Pridėtas endpoint override palaikymas
- Patobulintas inicializacijos šablonas

#### Sesija 06: Modelių maršrutizatorius (`models_router.py`)
- Pridėta endpoint konfigūracija
- Patobulinta ketinimų atpažinimo dokumentacija
- Patobulinta maršrutizavimo logikos dokumentacija

#### Sesija 06: Vamzdynas (`models_pipeline.py`)
- Pridėta išsami funkcijų dokumentacija
- Patobulinta žingsnis po žingsnio dokumentacija
- Patobulintas klaidų tvarkymas

### Skriptai

#### Benchmark Eksportas (`export_benchmark_markdown.py`)
- Pridėtas endpoint override palaikymas
- Atnaujinti numatytieji modeliai
- Patobulinta funkcijų dokumentacija
- Patobulintas klaidų tvarkymas

#### CLI Linteris (`lint_markdown_cli.py`)
- Pridėtos SDK nuorodos
- Patobulinta naudojimo dokumentacija

### Testai

#### Smoke Testai (`smoke.py`)
- Pridėtas endpoint override palaikymas
- Patobulinta dokumentacija
- Patobulinta testų atvejų dokumentacija
- Geresnis klaidų ataskaitų teikimas

## Aplinkos kintamieji

Visi pavyzdžiai dabar palaiko šiuos aplinkos kintamuosius:

### Pagrindinė konfigūracija
- `FOUNDRY_LOCAL_ALIAS` - Naudojamas modelio alias (numatytasis priklauso nuo pavyzdžio)
- `FOUNDRY_LOCAL_ENDPOINT` - Paslaugos endpoint perrašymas (neprivaloma)
- `SHOW_USAGE` - Rodyti žetonų naudojimo statistiką (numatytasis: "0")
- `RETRY_ON_FAIL` - Įjungti pakartotinio bandymo logiką (numatytasis: "1")
- `RETRY_BACKOFF` - Pradinis pakartotinio bandymo atidėjimas sekundėmis (numatytasis: "1.0")

### Specifiniai pavyzdžiams
- `EMBED_MODEL` - RAG pavyzdžių įterpimo modelis
- `BENCH_MODELS` - Modeliai, atskirti kableliais, skirti benchmarkingui
- `BENCH_ROUNDS` - Benchmarking raundų skaičius
- `BENCH_PROMPT` - Testavimo užklausa benchmarkingui
- `BENCH_STREAM` - Pirmojo ženklo vėlavimo matavimas
- `RAG_QUESTION` - Testavimo klausimas RAG pavyzdžiams
- `AGENT_MODEL_PRIMARY` - Pagrindinis agento modelis
- `AGENT_MODEL_EDITOR` - Redaktoriaus agento modelis
- `SLM_ALIAS` - Mažo kalbos modelio alias
- `LLM_ALIAS` - Didelio kalbos modelio alias

## Įgyvendintos SDK geriausios praktikos

### 1. Tinkamas kliento inicializavimas
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

### 2. Modelio informacijos gavimas
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Klaidos tvarkymas
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Pakartotinio bandymo logika su eksponentiniu atidėjimu
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

### 5. Srautinio perdavimo palaikymas
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

## Migracijos vadovas pritaikant individualius pavyzdžius

Jei kuriate naujus pavyzdžius arba atnaujinate esamus:

1. **Naudokite `workshop_utils.py` pagalbines funkcijas**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Palaikykite endpoint override**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Pridėkite išsamią dokumentaciją**:
   - Aplinkos kintamuosius docstring'e
   - SDK nuorodą
   - Naudojimo pavyzdžius

4. **Naudokite tipų užuominas**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Įgyvendinkite tinkamą klaidų tvarkymą**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testavimas

Visi pavyzdžiai gali būti testuojami naudojant:

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

## SDK Dokumentacijos Nuorodos

- **Pagrindinis saugykla**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Dokumentacija**: Naujausią API dokumentaciją rasite SDK saugykloje

## Pagrindiniai pakeitimai

### Nenumatoma
Visi pakeitimai yra suderinami atgal. Atnaujinimai daugiausia:
- Prideda naujas neprivalomas funkcijas (endpoint override)
- Patobulina klaidų tvarkymą
- Pagerina dokumentaciją
- Atnaujina numatytus modelių pavadinimus pagal dabartines rekomendacijas

### Neprivalomi patobulinimai
Galite atnaujinti savo kodą, kad naudotumėte:
- `FOUNDRY_LOCAL_ENDPOINT` aiškiam endpoint valdymui
- `SHOW_USAGE=1` žetonų naudojimo matomumui
- Atnaujintus modelių numatytuosius nustatymus (`phi-4-mini` vietoj `phi-3.5-mini`)

## Dažniausios problemos ir sprendimai

### Problema: "Kliento inicializavimas nepavyko"
**Sprendimas**: Įsitikinkite, kad Foundry Local paslauga veikia:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problema: "Modelis nerastas"
**Sprendimas**: Patikrinkite galimus modelius:
```bash
foundry model list
```

### Problema: Endpoint ryšio klaidos
**Sprendimas**: Patikrinkite endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Tolimesni žingsniai

1. **Atnaujinkite Module08 pavyzdžius**: Taikykite panašius šablonus Module08/samples
2. **Pridėkite integracijos testus**: Sukurkite išsamų testavimo rinkinį
3. **Našumo benchmarkingas**: Palyginkite našumą prieš/po atnaujinimo
4. **Dokumentacijos atnaujinimai**: Atnaujinkite pagrindinį README su naujais šablonais

## Prisidėjimo gairės

Pridedant naujus pavyzdžius:
1. Naudokite `workshop_utils.py` nuoseklumui užtikrinti
2. Sekite esamų pavyzdžių šabloną
3. Pridėkite išsamius docstring'us
4. Įtraukite SDK nuorodas
5. Palaikykite endpoint override
6. Pridėkite tinkamas tipų užuominas
7. Docstring'e įtraukite naudojimo pavyzdžius

## Versijų suderinamumas

Šie atnaujinimai suderinami su:
- `foundry-local-sdk` (naujausia versija)
- `openai>=1.30.0`
- Python 3.8+

---

**Paskutinį kartą atnaujinta**: 2025-01-08  
**Prižiūrėtojas**: EdgeAI Workshop komanda  
**SDK versija**: Foundry Local SDK (naujausia 0.7.117+67073234e7)

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.