<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T14:22:48+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "no"
}
-->
# Oppdateringer for Foundry Local SDK

## Oversikt

Oppdaterte Workshop-notatbøker og verktøy for å bruke **den offisielle Foundry Local Python SDK** i henhold til mønstrene fra:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Endrede filer

### 1. `Workshop/samples/workshop_utils.py`

**Endringer:**
- ✅ La til håndtering av importfeil for `foundry-local-sdk`-pakken
- ✅ Forbedret dokumentasjon med offisielle SDK-mønstre
- ✅ Bedre logging med Unicode-symboler (✓, ✗, ⚠)
- ✅ La til omfattende docstrings med eksempler
- ✅ Bedre feilmeldinger med referanser til CLI-kommandoer
- ✅ Oppdaterte kommentarer for å samsvare med offisiell SDK-dokumentasjon

**Viktige forbedringer:**

#### Håndtering av importfeil
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Forbedret `get_client()`-funksjon
- La til detaljert dokumentasjon om SDK-initialiseringsmønsteret
- Klargjorde at `FoundryLocalManager` starter tjenesten automatisk
- Forklarte aliasoppløsning for modeller til maskinvareoptimaliserte varianter
- Forbedret logging med informasjon om endepunkt
- Bedre feilmeldinger med forslag til feilsøking

#### Forbedret `chat_once()`-funksjon
- La til omfattende docstring med bruksanvisninger
- Klargjorde kompatibilitet med OpenAI SDK
- Dokumenterte støtte for streaming (via kwargs)
- Forbedret feilmeldinger med CLI-kommando-forslag
- La til notater om tilgjengelighetssjekk for modeller

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Endringer:**
- ✅ Oppdaterte alle markdown-celler med SDK-referanser
- ✅ Forbedret kodekommentarer med forklaringer på SDK-mønstre
- ✅ Bedre celle-dokumentasjon og forklaringer
- ✅ La til feilsøkingsveiledning
- ✅ Oppdaterte modellkatalogen (erstattet 'gpt-oss-20b' med 'phi-3.5-mini')
- ✅ Bedre utdataformat med visuelle indikatorer
- ✅ La til SDK-lenker og referanser gjennom hele dokumentet

**Oppdateringer celle for celle:**

#### Celle 1 (Tittel)
- La til lenker til SDK-dokumentasjon
- Refererte til offisielle GitHub-repositorier

#### Celle 2 (Scenario)
- Reformaterte med nummererte trinn
- Klargjorde mønster for intensjonsbasert ruting
- Fremhevet fordelene med lokal kjøring

#### Celle 3 (Avhengighetsinstallasjon)
- La til forklaring på hva hver pakke tilbyr
- Dokumenterte SDK-funksjoner (aliasoppløsning, maskinvareoptimalisering)

#### Celle 4 (Miljøoppsett)
- Forbedret funksjonsdocstrings
- La til inline-kommentarer som forklarer SDK-mønstre
- Dokumenterte struktur for modellkatalog
- Klargjorde prioritering/kapabilitetsmatching

#### Celle 5 (Katalogsjekk)
- La til visuelle sjekksymboler (✓)
- Bedre formatert utdata

#### Celle 6 (Test av intensjonsdeteksjon)
- Reformaterte utdata som tabellstil
- Viser både intensjon og valgt modell

#### Celle 7 (Ruterfunksjon)
- Omfattende forklaring på SDK-mønster
- Dokumenterte initialiseringsflyt
- Listet opp alle funksjoner (retry, sporing, feil)
- La til lenke til SDK-referanse

#### Celle 8 (Batch-demo)
- Forbedret forklaring på hva man kan forvente
- La til feilsøkingsseksjon
- Inkluderte CLI-kommandoer for debugging
- Bedre formatert utdata

### 3. `Workshop/notebooks/session06_README.md` (Ny fil)

**Opprettet omfattende dokumentasjon som dekker:**

1. **Oversikt**: Arkitekturdiagram og komponentforklaring
2. **SDK-integrasjon**: Kodeeksempler som følger offisielle mønstre
3. **Forutsetninger**: Trinnvise oppsettinstruksjoner
4. **Bruk**: Hvordan kjøre og tilpasse notatboken
5. **Modellaliaser**: Forklaring på maskinvareoptimaliserte varianter
6. **Feilsøking**: Vanlige problemer og løsninger
7. **Utvidelse**: Hvordan legge til intensjoner, modeller og tilpasset logikk
8. **Ytelsestips**: Beste praksis for produksjonsbruk
9. **Ressurser**: Lenker til offisiell dokumentasjon og fellesskap

## Implementering av SDK-mønster

### Offisielt mønster (fra Foundry Local-dokumentasjon)

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

### Vår implementering (i workshop_utils)

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

**Fordeler med vår tilnærming:**
- ✅ Følger offisielt SDK-mønster nøyaktig
- ✅ Legger til caching for å unngå gjentatt initialisering
- ✅ Inkluderer retry-logikk for robusthet i produksjon
- ✅ Støtter sporing av tokenbruk
- ✅ Gir bedre feilmeldinger
- ✅ Forblir kompatibel med offisielle eksempler

## Endringer i modellkatalog

### Før
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Etter
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Årsak:** Erstattet 'gpt-oss-20b' (ikke-standard alias) med 'phi-3.5-mini' (offisielt Foundry Local-alias).

## Avhengigheter

### Oppdatert requirements.txt

Workshop requirements.txt inkluderer allerede:
```
foundry-local-sdk
openai>=1.30.0
```

Dette er de eneste pakkene som trengs for Foundry Local-integrasjon.

## Testing av oppdateringene

### 1. Verifiser at Foundry Local kjører

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Sjekk tilgjengelige modeller

```bash
foundry model ls
```

Sørg for at disse modellene er tilgjengelige eller vil bli automatisk lastet ned:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Kjør notatboken

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Eller åpne i VS Code og kjør alle celler.

### 4. Forventet oppførsel

**Celle 1 (Installering):** Pakker installeres vellykket  
**Celle 2 (Oppsett):** Ingen feil, import fungerer  
**Celle 3 (Verifisering):** Viser ✓ med modelliste  
**Celle 4 (Test intensjon):** Viser resultater for intensjonsdeteksjon  
**Celle 5 (Ruter):** Viser ✓ Ruterfunksjon klar  
**Celle 6 (Utfør):** Ruter forespørsler til modeller, viser resultater  

### 5. Feilsøking av tilkoblingsfeil

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

Følgende miljøvariabler støttes:

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | Sett til `1` for å skrive ut tokenbruk |
| `RETRY_ON_FAIL` | `1` | Aktiver retry-logikk |
| `RETRY_BACKOFF` | `1.0` | Startforsinkelse for retry (sekunder) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Overstyr tjenesteendepunkt |

### Brukseksempler

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migrering fra gammelt mønster

Hvis du har eksisterende kode som bruker direkte API-kall, slik migrerer du:

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

### Etter (SDK)
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

### Fordeler med migrering
- ✅ Automatisk tjenestestyring
- ✅ Aliasoppløsning for modeller
- ✅ Maskinvareoptimalisering
- ✅ Bedre feilbehandling
- ✅ Kompatibilitet med OpenAI SDK
- ✅ Støtte for streaming

## Referanser

### Offisiell dokumentasjon
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK-kilde**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI-referanse**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Feilsøking**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop-ressurser
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Eksempeldokument**: `Workshop/notebooks/session06_models_router.ipynb`

### Fellesskap
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Neste steg

1. **Gjennomgå endringer**: Les gjennom de oppdaterte filene  
2. **Test notatbok**: Kjør session06_models_router.ipynb  
3. **Verifiser SDK**: Sørg for at foundry-local-sdk er installert  
4. **Sjekk tjeneste**: Bekreft at Foundry Local kjører  
5. **Utforsk dokumentasjon**: Les den nye session06_README.md  

## Sammendrag

Disse oppdateringene sikrer at Workshop-materialene følger **offisielle Foundry Local SDK-mønstre** nøyaktig som dokumentert i GitHub-repositoriet. Alle kodeeksempler, dokumentasjon og verktøy er nå i tråd med Microsofts anbefalte beste praksis for lokal AI-modellutplassering.

Endringene forbedrer:
- ✅ **Korrekthet**: Bruker offisielle SDK-mønstre  
- ✅ **Dokumentasjon**: Omfattende forklaringer og eksempler  
- ✅ **Feilhåndtering**: Bedre meldinger og feilsøkingsveiledning  
- ✅ **Vedlikeholdbarhet**: Følger offisielle konvensjoner  
- ✅ **Brukeropplevelse**: Klarere instruksjoner og hjelp til debugging  

---

**Oppdatert:** 8. oktober 2025  
**SDK-versjon:** foundry-local-sdk (siste)  
**Workshop-gren:** Reactor  

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.