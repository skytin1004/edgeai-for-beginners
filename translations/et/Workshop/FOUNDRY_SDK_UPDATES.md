<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-11T11:47:05+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "et"
}
-->
# Foundry Local SDK värskendused

## Ülevaade

Töötuba märkmikud ja utiliidid on uuendatud, et kasutada korrektselt **ametlikku Foundry Local Python SDK-d**, järgides mustreid:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Muudetud failid

### 1. `Workshop/samples/workshop_utils.py`

**Muudatused:**
- ✅ Lisatud impordi veakäsitlus `foundry-local-sdk` paketi jaoks
- ✅ Täiustatud dokumentatsiooni ametlike SDK mustritega
- ✅ Parandatud logimist Unicode'i sümbolitega (✓, ✗, ⚠)
- ✅ Lisatud põhjalikud docstringid koos näidetega
- ✅ Paremad veateated, mis viitavad CLI käskudele
- ✅ Kommentaarid uuendatud vastavalt ametlikule SDK dokumentatsioonile

**Peamised täiustused:**

#### Impordi veakäsitlus
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Täiustatud `get_client()` funktsioon
- Lisatud detailne dokumentatsioon SDK initsialiseerimise mustri kohta
- Selgitatud, et `FoundryLocalManager` käivitab teenuse automaatselt
- Selgitatud mudeli aliaste lahendamist riistvarale optimeeritud variantideks
- Parandatud logimist lõpp-punkti teabega
- Paremad veateated koos tõrkeotsingu soovitustega

#### Täiustatud `chat_once()` funktsioon
- Lisatud põhjalik docstring koos kasutusnäidetega
- Selgitatud OpenAI SDK ühilduvust
- Dokumenteeritud voogesituse tugi (kwargs kaudu)
- Parandatud veateated koos CLI käskude soovitustega
- Lisatud märkused mudelite kättesaadavuse kontrollimise kohta

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Muudatused:**
- ✅ Kõik markdown-rakud uuendatud SDK viidetega
- ✅ Täiustatud koodikommentaare SDK mustrite selgitustega
- ✅ Parandatud rakkude dokumentatsiooni ja selgitusi
- ✅ Lisatud tõrkeotsingu juhised
- ✅ Uuendatud mudelikataloog (asendatud 'gpt-oss-20b' 'phi-3.5-mini' vastu)
- ✅ Parem väljundi vormindamine visuaalsete indikaatoritega
- ✅ Lisatud SDK lingid ja viited kogu ulatuses

**Rakkude kaupa uuendused:**

#### Rakk 1 (Pealkiri)
- Lisatud SDK dokumentatsiooni lingid
- Viidatud ametlikele GitHubi repositooriumitele

#### Rakk 2 (Stsenaarium)
- Vormindatud nummerdatud sammudega
- Selgitatud kavatsusepõhist marsruutimise mustrit
- Rõhutatud lokaalse täitmise eeliseid

#### Rakk 3 (Sõltuvuste paigaldamine)
- Lisatud selgitus, mida iga pakett pakub
- Dokumenteeritud SDK võimalused (aliase lahendamine, riistvara optimeerimine)

#### Rakk 4 (Keskkonna seadistamine)
- Täiustatud funktsiooni docstringid
- Lisatud sisekommentaarid, mis selgitavad SDK mustreid
- Dokumenteeritud mudelikataloogi struktuur
- Selgitatud prioriteedi/võimekuse sobitamist

#### Rakk 5 (Kataloogi kontroll)
- Lisatud visuaalsed linnukesed (✓)
- Parem väljundi vormindamine

#### Rakk 6 (Kavatsuse tuvastamise test)
- Vormindatud väljund tabelistiilis
- Näitab nii kavatsust kui ka valitud mudelit

#### Rakk 7 (Marsruutimise funktsioon)
- Põhjalik SDK mustri selgitus
- Dokumenteeritud initsialiseerimise voog
- Loetletud kõik funktsioonid (uuesti proovimine, jälgimine, vead)
- Lisatud SDK viite link

#### Rakk 8 (Partii demo)
- Täiustatud selgitus, mida oodata
- Lisatud tõrkeotsingu sektsioon
- Lisatud CLI käsud silumiseks
- Parem väljundi kuvamise vormindamine

### 3. `Workshop/notebooks/session06_README.md` (uus fail)

**Loodud põhjalik dokumentatsioon, mis hõlmab:**

1. **Ülevaade**: Arhitektuuri diagramm ja komponentide selgitus
2. **SDK integreerimine**: Koodinäited vastavalt ametlikele mustritele
3. **Eeltingimused**: Samm-sammult seadistamise juhised
4. **Kasutamine**: Kuidas märkmikku käivitada ja kohandada
5. **Mudeli aliased**: Riistvarale optimeeritud variantide selgitus
6. **Tõrkeotsing**: Levinud probleemid ja lahendused
7. **Laiendamine**: Kuidas lisada kavatsusi, mudeleid ja kohandatud loogikat
8. **Jõudluse näpunäited**: Parimad tavad tootmiskasutuseks
9. **Ressursid**: Lingid ametlikele dokumentidele ja kogukonnale

## SDK mustri rakendamine

### Ametlik muster (Foundry Local dokumentatsioonist)

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

### Meie rakendus (workshop_utils)

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

**Meie lähenemise eelised:**
- ✅ Järgib täpselt ametlikku SDK mustrit
- ✅ Lisab vahemällu salvestamise, et vältida korduvat initsialiseerimist
- ✅ Sisaldab uuesti proovimise loogikat tootmise töökindluse tagamiseks
- ✅ Toetab tokenite kasutuse jälgimist
- ✅ Pakub paremaid veateateid
- ✅ Ühildub ametlike näidetega

## Mudelikataloogi muudatused

### Enne
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Pärast
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Põhjus:** Asendatud 'gpt-oss-20b' (mitteametlik alias) 'phi-3.5-mini' (ametlik Foundry Local alias) vastu.

## Sõltuvused

### Uuendatud requirements.txt

Workshop requirements.txt sisaldab juba:
```
foundry-local-sdk
openai>=1.30.0
```

Need on ainsad paketid, mis on vajalikud Foundry Local integratsiooniks.

## Uuenduste testimine

### 1. Kontrolli, kas Foundry Local töötab

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Kontrolli saadaolevaid mudeleid

```bash
foundry model ls
```

Veendu, et need mudelid on saadaval või laaditakse automaatselt alla:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Käivita märkmik

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Või ava VS Code'is ja käivita kõik rakud.

### 4. Oodatav käitumine

**Rakk 1 (Paigaldamine):** Paketid paigaldatakse edukalt  
**Rakk 2 (Seadistamine):** Vigu ei esine, impordid töötavad  
**Rakk 3 (Kontroll):** Kuvab ✓ mudelite loendiga  
**Rakk 4 (Testi kavatsust):** Kuvab kavatsuse tuvastamise tulemused  
**Rakk 5 (Marsruuter):** Kuvab ✓ Marsruutimisfunktsioon valmis  
**Rakk 6 (Käivita):** Marsruutib käsud mudelitele, kuvab tulemused  

### 5. Tõrkeotsing ühendusvigade korral

Kui näed `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Keskkonnamuutujad

Järgmised keskkonnamuutujad on toetatud:

| Muutuja | Vaikeväärtus | Kirjeldus |
|---------|--------------|-----------|
| `SHOW_USAGE` | `0` | Määra `1`, et kuvada tokenite kasutust |
| `RETRY_ON_FAIL` | `1` | Luba uuesti proovimise loogika |
| `RETRY_BACKOFF` | `1.0` | Esialgne uuesti proovimise viivitus (sekundites) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Teenuse lõpp-punkti ülekirjutamine |

### Kasutusnäited

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Üleminek vanalt mustrilt

Kui sul on olemasolev kood, mis kasutab otseseid API-kõnesid, siis siin on, kuidas üle minna:

### Enne (otsene API)
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

### Pärast (SDK)
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

### Ülemineku eelised
- ✅ Automaatne teenuse haldamine
- ✅ Mudeli aliase lahendamine
- ✅ Riistvara optimeerimise valik
- ✅ Parem veakäsitlus
- ✅ OpenAI SDK ühilduvus
- ✅ Voogesituse tugi

## Viited

### Ametlik dokumentatsioon
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local  
- **Python SDK allikas**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  
- **CLI viide**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md  
- **Tõrkeotsing**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md  

### Workshopi ressursid
- **Sessioon 06 README**: `Workshop/notebooks/session06_README.md`  
- **Workshopi utiliidid**: `Workshop/samples/workshop_utils.py`  
- **Näidismärkmik**: `Workshop/notebooks/session06_models_router.ipynb`  

### Kogukond
- **Discord**: https://aka.ms/foundry-local-discord  
- **GitHubi probleemid**: https://github.com/microsoft/Foundry-Local/issues  

## Järgmised sammud

1. **Vaata muudatused üle**: Loe uuendatud failid läbi  
2. **Testi märkmikku**: Käivita session06_models_router.ipynb  
3. **Kontrolli SDK-d**: Veendu, et foundry-local-sdk on paigaldatud  
4. **Kontrolli teenust**: Kinnita, et Foundry Local töötab  
5. **Uuri dokumente**: Loe uut session06_README.md  

## Kokkuvõte

Need uuendused tagavad, et Workshopi materjalid järgivad **ametlikke Foundry Local SDK mustreid**, täpselt nagu dokumenteeritud GitHubi repositooriumis. Kõik koodinäited, dokumentatsioon ja utiliidid on nüüd kooskõlas Microsofti soovitatud parimate tavadega kohalike AI mudelite juurutamiseks.

Muudatused parandavad:
- ✅ **Õigsust**: Kasutab ametlikke SDK mustreid  
- ✅ **Dokumentatsiooni**: Põhjalikud selgitused ja näited  
- ✅ **Veakäsitlust**: Paremad teated ja tõrkeotsingu juhised  
- ✅ **Hooldatavust**: Järgib ametlikke konventsioone  
- ✅ **Kasutajakogemust**: Selgemad juhised ja silumistoetus  

---

**Uuendatud:** 8. oktoober 2025  
**SDK versioon:** foundry-local-sdk (viimane)  
**Workshopi haru:** Reactor

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.