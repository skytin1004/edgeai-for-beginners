<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-09T14:45:39+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "fi"
}
-->
# Foundry Local SDK:n siirtymismuistiinpanot

## Yleiskatsaus

Kaikki Python-tiedostot Workshop-kansiossa on päivitetty noudattamaan uusimpia malleja virallisesta [Foundry Local Python SDK:sta](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Muutosten yhteenveto

### Ydinrakenteet (`workshop_utils.py`)

#### Parannetut ominaisuudet:
- **Endpointin ohitus**: Lisätty ympäristömuuttujan `FOUNDRY_LOCAL_ENDPOINT` tuki
- **Parannettu virheenkäsittely**: Parempi poikkeusten käsittely yksityiskohtaisilla virheilmoituksilla
- **Tehostettu välimuisti**: Välimuistiavaimet sisältävät nyt endpointin monen endpointin skenaarioita varten
- **Eksponentiaalinen viive**: Uudelleenyrittojen logiikka käyttää eksponentiaalista viivettä luotettavuuden parantamiseksi
- **Tyyppimerkinnät**: Lisätty kattavat tyyppivihjeet parempaa IDE-tukea varten

#### Uudet ominaisuudet:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Esimerkkisovellukset

#### Istunto 01: Chat Bootstrap (`chat_bootstrap.py`)
- Päivitetty oletusmalli `phi-3.5-mini` -> `phi-4-mini`
- Lisätty endpointin ohitus
- Parannettu dokumentaatio SDK-viitteillä

#### Istunto 02: RAG-putki (`rag_pipeline.py`)
- Päivitetty käyttämään `phi-4-mini` oletuksena
- Lisätty endpointin ohitus
- Parannettu dokumentaatio ympäristömuuttujien yksityiskohdilla

#### Istunto 02: RAG-arviointi (`rag_eval_ragas.py`)
- Päivitetty mallin oletukset
- Lisätty endpointin konfigurointi
- Parannettu virheenkäsittely

#### Istunto 03: Mallien vertailu (`benchmark_oss_models.py`)
- Päivitetty oletusmallilista sisältämään `phi-4-mini`
- Lisätty kattava ympäristömuuttujien dokumentaatio
- Parannettu funktioiden dokumentaatio
- Lisätty endpointin ohitus kaikkialle

#### Istunto 04: Mallien vertailu (`model_compare.py`)
- Päivitetty oletus-LLM `gpt-oss-20b` -> `qwen2.5-7b`
- Lisätty endpointin konfigurointi
- Parannettu dokumentaatio

#### Istunto 05: Multi-Agent Orchestration (`agents_orchestrator.py`)
- Lisätty tyyppivihjeet (muutettu `str | None` -> `Optional[str]`)
- Parannettu Agent-luokan dokumentaatio
- Lisätty endpointin ohitus
- Parannettu alustamismalli

#### Istunto 06: Mallien reititys (`models_router.py`)
- Lisätty endpointin konfigurointi
- Parannettu intentin tunnistuksen dokumentaatio
- Parannettu reitityslogiikan dokumentaatio

#### Istunto 06: Putki (`models_pipeline.py`)
- Lisätty kattava funktioiden dokumentaatio
- Parannettu vaiheittainen dokumentaatio
- Tehostettu virheenkäsittely

### Skriptit

#### Benchmark Export (`export_benchmark_markdown.py`)
- Lisätty endpointin ohitus
- Päivitetty oletusmallit
- Parannettu funktioiden dokumentaatio
- Tehostettu virheenkäsittely

#### CLI Linter (`lint_markdown_cli.py`)
- Lisätty SDK-viitelinkit
- Parannettu käyttöohjeet

### Testit

#### Smoke Testit (`smoke.py`)
- Lisätty endpointin ohitus
- Parannettu dokumentaatio
- Parannettu testitapausten dokumentaatio
- Parempi virheraportointi

## Ympäristömuuttujat

Kaikki esimerkit tukevat nyt näitä ympäristömuuttujia:

### Ydinkonfiguraatio
- `FOUNDRY_LOCAL_ALIAS` - Käytettävä mallialias (oletus vaihtelee esimerkin mukaan)
- `FOUNDRY_LOCAL_ENDPOINT` - Palvelun endpointin ohitus (valinnainen)
- `SHOW_USAGE` - Näytä tokenien käyttötilastot (oletus: "0")
- `RETRY_ON_FAIL` - Ota käyttöön uudelleenyrittämislogiikka (oletus: "1")
- `RETRY_BACKOFF` - Alkuperäinen viive uudelleenyrittämisessä sekunteina (oletus: "1.0")

### Esimerkki-kohtaiset
- `EMBED_MODEL` - Upotusmalli RAG-esimerkeille
- `BENCH_MODELS` - Pilkulla erotetut mallit benchmarkingille
- `BENCH_ROUNDS` - Benchmark-kierrosten määrä
- `BENCH_PROMPT` - Testikehotus benchmarkeille
- `BENCH_STREAM` - Mittaa ensimmäisen tokenin viive
- `RAG_QUESTION` - Testikysymys RAG-esimerkeille
- `AGENT_MODEL_PRIMARY` - Ensisijainen agenttimalli
- `AGENT_MODEL_EDITOR` - Editor-agenttimalli
- `SLM_ALIAS` - Pienen kielimallin alias
- `LLM_ALIAS` - Suuren kielimallin alias

## SDK:n parhaat käytännöt

### 1. Oikea asiakasohjelman alustaminen
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

### 2. Mallitietojen haku
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Virheenkäsittely
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Uudelleenyrittäminen eksponentiaalisella viiveellä
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

### 5. Streaming-tuki
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

## Siirtymisopas mukautetuille esimerkeille

Jos luot uusia esimerkkejä tai päivität olemassa olevia:

1. **Käytä `workshop_utils.py` apuvälineitä**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Tuki endpointin ohitukselle**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Lisää kattava dokumentaatio**:
   - Ympäristömuuttujat docstringissä
   - SDK-viitelinkki
   - Käyttöesimerkit

4. **Käytä tyyppivihjeitä**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Toteuta asianmukainen virheenkäsittely**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testaus

Kaikki esimerkit voidaan testata seuraavasti:

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

## SDK-dokumentaatioviitteet

- **Päärepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API-dokumentaatio**: Katso SDK-repositoryn uusimmat API-dokumentit

## Rikkovat muutokset

### Ei odotettavissa
Kaikki muutokset ovat taaksepäin yhteensopivia. Päivitykset pääasiassa:
- Lisäävät uusia valinnaisia ominaisuuksia (endpointin ohitus)
- Parantavat virheenkäsittelyä
- Tehostavat dokumentaatiota
- Päivittävät oletusmallien nimet nykyisiin suosituksiin

### Valinnaiset parannukset
Voit halutessasi päivittää koodisi käyttämään:
- `FOUNDRY_LOCAL_ENDPOINT` endpointin hallintaan
- `SHOW_USAGE=1` tokenien käytön näkyvyyden lisäämiseksi
- Päivitetyt mallin oletukset (`phi-4-mini` `phi-3.5-mini` sijaan)

## Yleiset ongelmat ja ratkaisut

### Ongelma: "Asiakasohjelman alustaminen epäonnistui"
**Ratkaisu**: Varmista, että Foundry Local -palvelu on käynnissä:
```bash
foundry service start
foundry model run phi-4-mini
```

### Ongelma: "Mallia ei löydy"
**Ratkaisu**: Tarkista saatavilla olevat mallit:
```bash
foundry model list
```

### Ongelma: Endpoint-yhteysvirheet
**Ratkaisu**: Varmista endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Seuraavat askeleet

1. **Päivitä Module08-esimerkit**: Sovella samanlaisia malleja Module08/samples-kansioon
2. **Lisää integraatiotestit**: Luo kattava testisarja
3. **Suorituskykyvertailu**: Vertaa suorituskykyä ennen/jälkeen
4. **Dokumentaation päivitykset**: Päivitä pääasiallinen README uusilla malleilla

## Osallistumisohjeet

Kun lisäät uusia esimerkkejä:
1. Käytä `workshop_utils.py` johdonmukaisuuden varmistamiseksi
2. Noudata olemassa olevien esimerkkien mallia
3. Lisää kattavat docstringit
4. Sisällytä SDK-viitelinkit
5. Tue endpointin ohitusta
6. Lisää asianmukaiset tyyppivihjeet
7. Sisällytä käyttöesimerkit docstringiin

## Versioyhteensopivuus

Nämä päivitykset ovat yhteensopivia seuraavien kanssa:
- `foundry-local-sdk` (uusin)
- `openai>=1.30.0`
- Python 3.8+

---

**Viimeksi päivitetty**: 2025-01-08  
**Ylläpitäjä**: EdgeAI Workshop Team  
**SDK-versio**: Foundry Local SDK (uusin 0.7.117+67073234e7)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.