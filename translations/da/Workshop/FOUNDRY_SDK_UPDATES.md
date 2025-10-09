<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T14:22:19+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "da"
}
-->
# Foundry Local SDK-opdateringer

## Oversigt

Workshop-notebooks og værktøjer er blevet opdateret til korrekt at bruge den **officielle Foundry Local Python SDK** i henhold til mønstrene fra:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Ændrede filer

### 1. `Workshop/samples/workshop_utils.py`

**Ændringer:**
- ✅ Tilføjet fejlhåndtering ved import af `foundry-local-sdk`-pakken
- ✅ Forbedret dokumentation med officielle SDK-mønstre
- ✅ Forbedret logning med Unicode-symboler (✓, ✗, ⚠)
- ✅ Tilføjet omfattende docstrings med eksempler
- ✅ Bedre fejlmeddelelser med henvisning til CLI-kommandoer
- ✅ Opdaterede kommentarer, så de matcher den officielle SDK-dokumentation

**Vigtige forbedringer:**

#### Fejlhåndtering ved import
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Forbedret `get_client()`-funktion
- Tilføjet detaljeret dokumentation om SDK-initialiseringsmønsteret
- Klargjort, at `FoundryLocalManager` automatisk starter tjenesten
- Forklaret modelalias-opløsning til hardwareoptimerede varianter
- Forbedret logning med endpoint-information
- Bedre fejlmeddelelser med forslag til fejlfinding

#### Forbedret `chat_once()`-funktion
- Tilføjet omfattende docstring med brugseksempler
- Klargjort OpenAI SDK-kompatibilitet
- Dokumenteret streaming-understøttelse (via kwargs)
- Forbedrede fejlmeddelelser med CLI-kommandoforslag
- Tilføjet noter om kontrol af modeltilgængelighed

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Ændringer:**
- ✅ Opdateret alle markdown-celler med SDK-referencer
- ✅ Forbedret kodekommentarer med forklaringer af SDK-mønstre
- ✅ Forbedret celle-dokumentation og forklaringer
- ✅ Tilføjet vejledning til fejlfinding
- ✅ Opdateret modelkatalog (erstattet 'gpt-oss-20b' med 'phi-3.5-mini')
- ✅ Bedre outputformatering med visuelle indikatorer
- ✅ Tilføjet SDK-links og referencer gennem hele dokumentet

**Opdateringer celle for celle:**

#### Celle 1 (Titel)
- Tilføjet SDK-dokumentationslinks
- Refereret officielle GitHub-repositorier

#### Celle 2 (Scenario)
- Omformateret med nummererede trin
- Klargjort mønster for intent-baseret routing
- Fremhævet fordelene ved lokal eksekvering

#### Celle 3 (Afhængighedsinstallation)
- Tilføjet forklaring af, hvad hver pakke tilbyder
- Dokumenteret SDK-funktioner (alias-opløsning, hardwareoptimering)

#### Celle 4 (Miljøopsætning)
- Forbedret funktion-docstrings
- Tilføjet inline-kommentarer, der forklarer SDK-mønstre
- Dokumenteret modelkatalogstruktur
- Klargjort prioritet/kapabilitetsmatching

#### Celle 5 (Katalogkontrol)
- Tilføjet visuelle flueben (✓)
- Bedre formateret output

#### Celle 6 (Intent-detektionstest)
- Omformateret output som tabelstil
- Viser både intent og valgt model

#### Celle 7 (Routing-funktion)
- Omfattende forklaring af SDK-mønster
- Dokumenteret initialiseringsflow
- Listet alle funktioner (retry, tracking, fejl)
- Tilføjet SDK-referencelink

#### Celle 8 (Batch-demo)
- Forbedret forklaring af, hvad man kan forvente
- Tilføjet fejlfindingssektion
- Inkluderet CLI-kommandoer til debugging
- Bedre formateret outputvisning

### 3. `Workshop/notebooks/session06_README.md` (Ny fil)

**Oprettet omfattende dokumentation, der dækker:**

1. **Oversigt**: Arkitekturdiagram og komponentforklaring
2. **SDK-integration**: Kodeeksempler, der følger officielle mønstre
3. **Forudsætninger**: Trinvise opsætningsinstruktioner
4. **Brug**: Sådan køres og tilpasses notebooken
5. **Modelaliaser**: Forklaring af hardwareoptimerede varianter
6. **Fejlfinding**: Almindelige problemer og løsninger
7. **Udvidelse**: Sådan tilføjes intents, modeller og brugerdefineret logik
8. **Ydelsestips**: Bedste praksis til produktion
9. **Ressourcer**: Links til officielle dokumenter og fællesskab

## Implementering af SDK-mønster

### Officielt mønster (fra Foundry Local-dokumentation)

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

### Vores implementering (i workshop_utils)

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

**Fordele ved vores tilgang:**
- ✅ Følger det officielle SDK-mønster præcist
- ✅ Tilføjer caching for at undgå gentagen initialisering
- ✅ Inkluderer retry-logik for robusthed i produktion
- ✅ Understøtter sporing af tokenbrug
- ✅ Giver bedre fejlmeddelelser
- ✅ Forbliver kompatibel med officielle eksempler

## Ændringer i modelkatalog

### Før
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Efter
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Årsag:** Erstattet 'gpt-oss-20b' (ikke-standard alias) med 'phi-3.5-mini' (officielt Foundry Local-alias).

## Afhængigheder

### Opdateret requirements.txt

Workshop requirements.txt inkluderer allerede:
```
foundry-local-sdk
openai>=1.30.0
```

Disse er de eneste pakker, der er nødvendige for Foundry Local-integration.

## Test af opdateringerne

### 1. Bekræft, at Foundry Local kører

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Kontroller tilgængelige modeller

```bash
foundry model ls
```

Sørg for, at disse modeller er tilgængelige eller vil blive automatisk downloadet:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Kør notebooken

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Eller åbn i VS Code og kør alle celler.

### 4. Forventet adfærd

**Celle 1 (Installér):** Installationen af pakker lykkes
**Celle 2 (Opsætning):** Ingen fejl, import fungerer
**Celle 3 (Bekræft):** Viser ✓ med modelliste
**Celle 4 (Test Intent):** Viser resultater af intent-detektion
**Celle 5 (Router):** Viser ✓ Route-funktion klar
**Celle 6 (Eksekvér):** Router prompts til modeller, viser resultater

### 5. Fejlfinding af forbindelsesfejl

Hvis du ser `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Miljøvariabler

Følgende miljøvariabler understøttes:

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | Sæt til `1` for at udskrive tokenbrug |
| `RETRY_ON_FAIL` | `1` | Aktiver retry-logik |
| `RETRY_BACKOFF` | `1.0` | Initial retry-forsinkelse (sekunder) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Overstyr tjenesteendpoint |

### Brugseksempler

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migration fra gammelt mønster

Hvis du har eksisterende kode, der bruger direkte API-kald, her er hvordan du migrerer:

### Før (Direkte API)
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

### Efter (SDK)
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

### Fordele ved migration
- ✅ Automatisk tjenestestyring
- ✅ Modelalias-opløsning
- ✅ Hardwareoptimeringsvalg
- ✅ Bedre fejlhåndtering
- ✅ OpenAI SDK-kompatibilitet
- ✅ Streaming-understøttelse

## Referencer

### Officiel dokumentation
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK-kilde**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI-reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Fejlfinding**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop-ressourcer
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Eksempel-notebook**: `Workshop/notebooks/session06_models_router.ipynb`

### Fællesskab
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Næste skridt

1. **Gennemgå ændringer**: Læs de opdaterede filer
2. **Test notebook**: Kør session06_models_router.ipynb
3. **Bekræft SDK**: Sørg for, at foundry-local-sdk er installeret
4. **Kontrollér tjeneste**: Bekræft, at Foundry Local kører
5. **Udforsk dokumenter**: Læs den nye session06_README.md

## Resumé

Disse opdateringer sikrer, at Workshop-materialerne følger de **officielle Foundry Local SDK-mønstre** præcist som dokumenteret i GitHub-repositoriet. Alle kodeeksempler, dokumentation og værktøjer er nu i overensstemmelse med Microsofts anbefalede bedste praksis for lokal AI-modeludrulning.

Ændringerne forbedrer:
- ✅ **Korrekthed**: Bruger officielle SDK-mønstre
- ✅ **Dokumentation**: Omfattende forklaringer og eksempler
- ✅ **Fejlhåndtering**: Bedre meddelelser og vejledning til fejlfinding
- ✅ **Vedligeholdelse**: Følger officielle konventioner
- ✅ **Brugeroplevelse**: Klarere instruktioner og hjælp til debugging

---

**Opdateret:** 8. oktober 2025  
**SDK-version:** foundry-local-sdk (seneste)  
**Workshop-gren:** Reactor

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.