<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T16:37:53+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "nl"
}
-->
# Foundry Local SDK Updates

## Overzicht

De Workshop-notebooks en -hulpprogramma's zijn bijgewerkt om correct gebruik te maken van de **officiële Foundry Local Python SDK**, volgens de patronen van:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Gewijzigde bestanden

### 1. `Workshop/samples/workshop_utils.py`

**Wijzigingen:**
- ✅ Toegevoegd foutafhandelingsmechanisme voor het importeren van het `foundry-local-sdk`-pakket
- ✅ Documentatie verbeterd met officiële SDK-patronen
- ✅ Logging verbeterd met Unicode-symbolen (✓, ✗, ⚠)
- ✅ Uitgebreide docstrings toegevoegd met voorbeelden
- ✅ Betere foutmeldingen met verwijzingen naar CLI-commando's
- ✅ Opmerkingen bijgewerkt om overeen te komen met de officiële SDK-documentatie

**Belangrijke verbeteringen:**

#### Foutafhandeling bij importeren
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Verbeterde `get_client()`-functie
- Gedetailleerde documentatie toegevoegd over het SDK-initialisatiepatroon
- Uitleg gegeven dat `FoundryLocalManager` de service automatisch start
- Modelaliasresolutie naar hardware-geoptimaliseerde varianten uitgelegd
- Logging verbeterd met informatie over de eindpunten
- Betere foutmeldingen met suggesties voor probleemoplossing

#### Verbeterde `chat_once()`-functie
- Uitgebreide docstring toegevoegd met gebruiksvoorbeelden
- OpenAI SDK-compatibiliteit verduidelijkt
- Streamingondersteuning gedocumenteerd (via kwargs)
- Betere foutmeldingen met CLI-commando suggesties
- Opmerkingen toegevoegd over controle van modelbeschikbaarheid

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Wijzigingen:**
- ✅ Alle markdown-cellen bijgewerkt met SDK-verwijzingen
- ✅ Code-opmerkingen verbeterd met uitleg over SDK-patronen
- ✅ Documentatie en uitleg in cellen verbeterd
- ✅ Probleemoplossingsrichtlijnen toegevoegd
- ✅ Modelcatalogus bijgewerkt (vervangen 'gpt-oss-20b' door 'phi-3.5-mini')
- ✅ Betere uitvoeropmaak met visuele indicatoren
- ✅ SDK-links en verwijzingen overal toegevoegd

**Cel-per-cel updates:**

#### Cel 1 (Titel)
- SDK-documentatielinks toegevoegd
- Verwijzingen naar officiële GitHub-repositories toegevoegd

#### Cel 2 (Scenario)
- Opnieuw geformatteerd met genummerde stappen
- Intent-gebaseerd routeringspatroon verduidelijkt
- Voordelen van lokale uitvoering benadrukt

#### Cel 3 (Afhankelijkheden installeren)
- Uitleg toegevoegd over wat elk pakket biedt
- SDK-mogelijkheden gedocumenteerd (aliasresolutie, hardware-optimalisatie)

#### Cel 4 (Omgevingsinstellingen)
- Docstrings van functies verbeterd
- Inline opmerkingen toegevoegd die SDK-patronen uitleggen
- Structuur van modelcatalogus gedocumenteerd
- Prioriteit/capaciteitsmatching verduidelijkt

#### Cel 5 (Cataloguscontrole)
- Visuele vinkjes toegevoegd (✓)
- Uitvoer beter geformatteerd

#### Cel 6 (Intentdetectietest)
- Uitvoer opnieuw geformatteerd als tabelstijl
- Toont zowel intentie als geselecteerd model

#### Cel 7 (Routeringsfunctie)
- Uitgebreide uitleg over SDK-patronen
- Initialisatiestroom gedocumenteerd
- Alle functies opgesomd (retry, tracking, fouten)
- SDK-verwijzingslink toegevoegd

#### Cel 8 (Batchdemo)
- Uitleg verbeterd over wat te verwachten
- Probleemoplossingssectie toegevoegd
- CLI-commando's voor debugging opgenomen
- Uitvoerweergave beter geformatteerd

### 3. `Workshop/notebooks/session06_README.md` (Nieuw bestand)

**Uitgebreide documentatie gemaakt met:**

1. **Overzicht**: Architectuurdiagram en componentuitleg
2. **SDK-integratie**: Codevoorbeelden volgens officiële patronen
3. **Vereisten**: Stapsgewijze installatie-instructies
4. **Gebruik**: Hoe de notebook te draaien en aan te passen
5. **Modelaliassen**: Uitleg over hardware-geoptimaliseerde varianten
6. **Probleemoplossing**: Veelvoorkomende problemen en oplossingen
7. **Uitbreiden**: Hoe intenties, modellen en aangepaste logica toe te voegen
8. **Prestatie-tips**: Best practices voor productiegebruik
9. **Bronnen**: Links naar officiële documentatie en community

## Implementatie van SDK-patronen

### Officieel patroon (uit Foundry Local-documentatie)

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

### Onze implementatie (in workshop_utils)

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

**Voordelen van onze aanpak:**
- ✅ Volgt het officiële SDK-patroon exact
- ✅ Voegt caching toe om herhaalde initialisatie te vermijden
- ✅ Bevat retry-logica voor robuustheid in productie
- ✅ Ondersteunt het bijhouden van tokengebruik
- ✅ Biedt betere foutmeldingen
- ✅ Blijft compatibel met officiële voorbeelden

## Wijzigingen in modelcatalogus

### Voorheen
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Nu
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Reden:** 'gpt-oss-20b' (niet-standaard alias) vervangen door 'phi-3.5-mini' (officiële Foundry Local-alias).

## Afhankelijkheden

### Bijgewerkte requirements.txt

De Workshop requirements.txt bevat al:
```
foundry-local-sdk
openai>=1.30.0
```

Dit zijn de enige pakketten die nodig zijn voor Foundry Local-integratie.

## Updates testen

### 1. Controleer of Foundry Local actief is

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Controleer beschikbare modellen

```bash
foundry model ls
```

Zorg ervoor dat deze modellen beschikbaar zijn of automatisch worden gedownload:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Voer de notebook uit

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Of open in VS Code en voer alle cellen uit.

### 4. Verwacht gedrag

**Cel 1 (Installeren):** Installeert pakketten succesvol  
**Cel 2 (Instellen):** Geen fouten, imports werken  
**Cel 3 (Controleren):** Toont ✓ met modellijst  
**Cel 4 (Intenttest):** Toont intentiedetectieresultaten  
**Cel 5 (Router):** Toont ✓ Routerfunctie gereed  
**Cel 6 (Uitvoeren):** Routeert prompts naar modellen, toont resultaten  

### 5. Probleemoplossing bij verbindingsfouten

Als je `APIConnectionError: Connection error` ziet:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Omgevingsvariabelen

De volgende omgevingsvariabelen worden ondersteund:

| Variabele | Standaard | Beschrijving |
|-----------|-----------|--------------|
| `SHOW_USAGE` | `0` | Stel in op `1` om tokengebruik af te drukken |
| `RETRY_ON_FAIL` | `1` | Retry-logica inschakelen |
| `RETRY_BACKOFF` | `1.0` | Initiële retry-vertraging (seconden) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Service-eindpunt overschrijven |

### Gebruiksvoorbeelden

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migratie van oud patroon

Als je bestaande code hebt die directe API-aanroepen gebruikt, hier is hoe je kunt migreren:

### Voorheen (Directe API)
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

### Nu (SDK)
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

### Voordelen van migratie
- ✅ Automatisch servicemanagement
- ✅ Modelaliasresolutie
- ✅ Hardware-optimalisatie selectie
- ✅ Betere foutafhandeling
- ✅ OpenAI SDK-compatibiliteit
- ✅ Streamingondersteuning

## Verwijzingen

### Officiële documentatie
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK-bron**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI-referentie**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Probleemoplossing**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshopbronnen
- **Sessie 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Voorbeeldnotebook**: `Workshop/notebooks/session06_models_router.ipynb`

### Community
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Volgende stappen

1. **Wijzigingen beoordelen**: Lees de bijgewerkte bestanden door  
2. **Notebook testen**: Voer session06_models_router.ipynb uit  
3. **SDK verifiëren**: Zorg ervoor dat foundry-local-sdk is geïnstalleerd  
4. **Service controleren**: Bevestig dat Foundry Local actief is  
5. **Documentatie verkennen**: Lees de nieuwe session06_README.md  

## Samenvatting

Deze updates zorgen ervoor dat de Workshop-materialen exact de **officiële Foundry Local SDK-patronen** volgen zoals gedocumenteerd in de GitHub-repository. Alle codevoorbeelden, documentatie en hulpprogramma's zijn nu afgestemd op de aanbevolen best practices van Microsoft voor lokale AI-modelimplementatie.

De wijzigingen verbeteren:
- ✅ **Correctheid**: Gebruikt officiële SDK-patronen  
- ✅ **Documentatie**: Uitgebreide uitleg en voorbeelden  
- ✅ **Foutafhandeling**: Betere meldingen en probleemoplossingsrichtlijnen  
- ✅ **Onderhoudbaarheid**: Volgt officiële conventies  
- ✅ **Gebruikerservaring**: Duidelijkere instructies en debugginghulp  

---

**Bijgewerkt:** 8 oktober 2025  
**SDK-versie:** foundry-local-sdk (laatste)  
**Workshop-branch:** Reactor  

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.