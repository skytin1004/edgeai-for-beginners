<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T12:47:28+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "sv"
}
-->
# Foundry Local SDK Uppdateringar

## Översikt

Uppdaterade Workshop-notebooks och verktyg för att korrekt använda **den officiella Foundry Local Python SDK** enligt mönstren från:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Modifierade Filer

### 1. `Workshop/samples/workshop_utils.py`

**Ändringar:**
- ✅ Lade till felhantering vid import av paketet `foundry-local-sdk`
- ✅ Förbättrade dokumentationen med officiella SDK-mönster
- ✅ Förbättrade loggning med Unicode-symboler (✓, ✗, ⚠)
- ✅ Lade till omfattande docstrings med exempel
- ✅ Bättre felmeddelanden som hänvisar till CLI-kommandon
- ✅ Uppdaterade kommentarer för att matcha officiell SDK-dokumentation

**Viktiga Förbättringar:**

#### Felhantering vid Import
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Förbättrad `get_client()` Funktion
- Lade till detaljerad dokumentation om SDK-initialiseringsmönstret
- Förklarade att `FoundryLocalManager` startar tjänsten automatiskt
- Beskrev aliasupplösning för modeller till hårdvaruoptimerade varianter
- Förbättrade loggning med information om endpoint
- Bättre felmeddelanden med förslag på felsökningssteg

#### Förbättrad `chat_once()` Funktion
- Lade till omfattande docstring med användningsexempel
- Klargjorde kompatibilitet med OpenAI SDK
- Dokumenterade stöd för streaming (via kwargs)
- Förbättrade felmeddelanden med CLI-kommandoförslag
- Lade till anteckningar om kontroll av modelltillgänglighet

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Ändringar:**
- ✅ Uppdaterade alla markdown-celler med SDK-referenser
- ✅ Förbättrade kodkommentarer med förklaringar av SDK-mönster
- ✅ Förbättrade celldokumentation och förklaringar
- ✅ Lade till felsökningsvägledning
- ✅ Uppdaterade modellkatalogen (ersatte 'gpt-oss-20b' med 'phi-3.5-mini')
- ✅ Bättre utdataformat med visuella indikatorer
- ✅ Lade till SDK-länkar och referenser genomgående

**Cell-för-Cell Uppdateringar:**

#### Cell 1 (Titel)
- Lade till SDK-dokumentationslänkar
- Hänvisade till officiella GitHub-repositorier

#### Cell 2 (Scenario)
- Omformaterade med numrerade steg
- Klargjorde mönstret för intent-baserad routing
- Betonade fördelarna med lokal körning

#### Cell 3 (Installera Beroenden)
- Lade till förklaring av vad varje paket tillhandahåller
- Dokumenterade SDK-funktioner (aliasupplösning, hårdvaruoptimering)

#### Cell 4 (Miljöinställning)
- Förbättrade funktionens docstrings
- Lade till inline-kommentarer som förklarar SDK-mönster
- Dokumenterade struktur för modellkatalogen
- Klargjorde prioritet/förmågematchning

#### Cell 5 (Katalogkontroll)
- Lade till visuella checkmarkeringar (✓)
- Bättre formaterad utdata

#### Cell 6 (Intentdetektionstest)
- Omformaterade utdata som tabellstil
- Visar både intent och vald modell

#### Cell 7 (Routingfunktion)
- Omfattande förklaring av SDK-mönster
- Dokumenterade initialiseringsflödet
- Listade alla funktioner (retry, tracking, errors)
- Lade till SDK-referenslänk

#### Cell 8 (Batchdemo)
- Förbättrade förklaringen av vad man kan förvänta sig
- Lade till felsökningssektion
- Inkluderade CLI-kommandon för debugging
- Bättre formaterad utdisplay

### 3. `Workshop/notebooks/session06_README.md` (Ny Fil)

**Skapade omfattande dokumentation som täcker:**

1. **Översikt**: Arkitekturdiagram och komponentförklaring
2. **SDK Integration**: Kodexempel enligt officiella mönster
3. **Förutsättningar**: Steg-för-steg installationsinstruktioner
4. **Användning**: Hur man kör och anpassar notebooken
5. **Modellalias**: Förklaring av hårdvaruoptimerade varianter
6. **Felsökning**: Vanliga problem och lösningar
7. **Utökning**: Hur man lägger till intents, modeller och anpassad logik
8. **Prestandatips**: Bästa praxis för produktion
9. **Resurser**: Länkar till officiell dokumentation och community

## Implementering av SDK-mönster

### Officiellt Mönster (från Foundry Local-dokumentation)

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

### Vår Implementering (i workshop_utils)

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

**Fördelar med Vår Metod:**
- ✅ Följer officiellt SDK-mönster exakt
- ✅ Lägger till caching för att undvika upprepad initialisering
- ✅ Inkluderar retry-logik för produktionsrobusthet
- ✅ Stödjer spårning av tokenanvändning
- ✅ Ger bättre felmeddelanden
- ✅ Förblir kompatibel med officiella exempel

## Ändringar i Modellkatalogen

### Före
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

**Anledning:** Ersatte 'gpt-oss-20b' (icke-standard alias) med 'phi-3.5-mini' (officiellt Foundry Local-alias).

## Beroenden

### Uppdaterad requirements.txt

Workshopens requirements.txt innehåller redan:
```
foundry-local-sdk
openai>=1.30.0
```

Dessa är de enda paketen som behövs för Foundry Local-integrering.

## Testning av Uppdateringarna

### 1. Verifiera att Foundry Local Körs

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Kontrollera Tillgängliga Modeller

```bash
foundry model ls
```

Säkerställ att dessa modeller är tillgängliga eller kommer att laddas ner automatiskt:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Kör Notebooken

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Eller öppna i VS Code och kör alla celler.

### 4. Förväntat Beteende

**Cell 1 (Installera):** Installerar paket framgångsrikt  
**Cell 2 (Setup):** Inga fel, import fungerar  
**Cell 3 (Verifiera):** Visar ✓ med modellista  
**Cell 4 (Testa Intent):** Visar resultat för intentdetektion  
**Cell 5 (Router):** Visar ✓ Routingfunktion redo  
**Cell 6 (Utför):** Riktar prompts till modeller, visar resultat  

### 5. Felsökning av Anslutningsfel

Om du ser `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Miljövariabler

Följande miljövariabler stöds:

| Variabel | Standard | Beskrivning |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | Ställ in till `1` för att skriva ut tokenanvändning |
| `RETRY_ON_FAIL` | `1` | Aktivera retry-logik |
| `RETRY_BACKOFF` | `1.0` | Initial retry-fördröjning (sekunder) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Åsidosätt tjänstens endpoint |

### Användningsexempel

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migrering från Gammalt Mönster

Om du har befintlig kod som använder direkta API-anrop, här är hur du migrerar:

### Före (Direkt API)
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

### Fördelar med Migrering
- ✅ Automatisk tjänstehantering
- ✅ Modellaliasupplösning
- ✅ Val av hårdvaruoptimering
- ✅ Bättre felhantering
- ✅ Kompatibilitet med OpenAI SDK
- ✅ Stöd för streaming

## Referenser

### Officiell Dokumentation
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK Källa**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI Referens**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Felsökning**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshopresurser
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Exempel Notebook**: `Workshop/notebooks/session06_models_router.ipynb`

### Community
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Nästa Steg

1. **Granska Ändringar**: Läs igenom de uppdaterade filerna  
2. **Testa Notebook**: Kör session06_models_router.ipynb  
3. **Verifiera SDK**: Säkerställ att foundry-local-sdk är installerad  
4. **Kontrollera Tjänsten**: Bekräfta att Foundry Local körs  
5. **Utforska Dokumentation**: Läs den nya session06_README.md  

## Sammanfattning

Dessa uppdateringar säkerställer att Workshop-materialen följer **officiella Foundry Local SDK-mönster** exakt som dokumenterat i GitHub-repositoriet. Alla kodexempel, dokumentation och verktyg är nu i linje med Microsofts rekommenderade bästa praxis för lokal AI-modellimplementering.

Förbättringarna leder till:
- ✅ **Korrekthet**: Använder officiella SDK-mönster  
- ✅ **Dokumentation**: Omfattande förklaringar och exempel  
- ✅ **Felhantering**: Bättre meddelanden och felsökningsvägledning  
- ✅ **Underhållbarhet**: Följer officiella konventioner  
- ✅ **Användarupplevelse**: Tydligare instruktioner och hjälp med debugging  

---

**Uppdaterad:** 8 oktober 2025  
**SDK Version:** foundry-local-sdk (senaste)  
**Workshop Branch:** Reactor  

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.