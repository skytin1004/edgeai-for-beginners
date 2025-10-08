<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T11:56:44+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "sl"
}
-->
# Posodobitve lokalnega SDK Foundry

## Pregled

Posodobljeni zvezki Workshop in pripomočki za pravilno uporabo **uradnega lokalnega Python SDK Foundry** po vzorcih iz:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Spremenjene datoteke

### 1. `Workshop/samples/workshop_utils.py`

**Spremembe:**
- ✅ Dodano obravnavanje napak pri uvozu paketa `foundry-local-sdk`
- ✅ Izboljšana dokumentacija z uradnimi vzorci SDK
- ✅ Izboljšano beleženje z Unicode simboli (✓, ✗, ⚠)
- ✅ Dodani obsežni docstringi z zgledi
- ✅ Boljša sporočila o napakah, ki se sklicujejo na ukaze CLI
- ✅ Posodobljeni komentarji, da ustrezajo uradni dokumentaciji SDK

**Ključne izboljšave:**

#### Obravnava napak pri uvozu
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Izboljšana funkcija `get_client()`
- Dodana podrobna dokumentacija o vzorcu inicializacije SDK
- Pojasnjeno, da `FoundryLocalManager` samodejno zažene storitev
- Razložena razrešitev vzdevkov modelov na strojno optimizirane različice
- Izboljšano beleženje z informacijami o končni točki
- Boljša sporočila o napakah z nasveti za odpravljanje težav

#### Izboljšana funkcija `chat_once()`
- Dodan obsežen docstring z zgledi uporabe
- Pojasnjena združljivost z OpenAI SDK
- Dokumentirana podpora za pretakanje (prek kwargs)
- Izboljšana sporočila o napakah z nasveti za ukaze CLI
- Dodane opombe o preverjanju razpoložljivosti modelov

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Spremembe:**
- ✅ Posodobljene vse celice z markdownom z referencami SDK
- ✅ Izboljšani komentarji kode z razlagami vzorcev SDK
- ✅ Izboljšana dokumentacija celic in razlage
- ✅ Dodano vodstvo za odpravljanje težav
- ✅ Posodobljen katalog modelov (zamenjan 'gpt-oss-20b' z 'phi-3.5-mini')
- ✅ Boljše oblikovanje izhodnih podatkov z vizualnimi indikatorji
- ✅ Dodane povezave in reference SDK skozi celoten zvezek

**Posodobitve po celicah:**

#### Celica 1 (Naslov)
- Dodane povezave do dokumentacije SDK
- Sklic na uradne GitHub repozitorije

#### Celica 2 (Scenarij)
- Preoblikovano s številčenjem korakov
- Pojasnjen vzorec usmerjanja na podlagi namena
- Poudarjene prednosti lokalnega izvajanja

#### Celica 3 (Namestitev odvisnosti)
- Dodana razlaga, kaj zagotavlja vsak paket
- Dokumentirane zmogljivosti SDK (razrešitev vzdevkov, strojna optimizacija)

#### Celica 4 (Nastavitev okolja)
- Izboljšani docstringi funkcij
- Dodani komentarji v vrsticah, ki pojasnjujejo vzorce SDK
- Dokumentirana struktura kataloga modelov
- Pojasnjeno ujemanje prednosti/zmožnosti

#### Celica 5 (Preverjanje kataloga)
- Dodani vizualni kljukici (✓)
- Boljše oblikovanje izhodnih podatkov

#### Celica 6 (Test zaznavanja namena)
- Preoblikovan izhod v tabelarni slog
- Prikazuje tako namen kot izbrani model

#### Celica 7 (Funkcija usmerjanja)
- Obsežna razlaga vzorca SDK
- Dokumentiran potek inicializacije
- Naštete vse funkcije (ponovni poskus, sledenje, napake)
- Dodana povezava na referenco SDK

#### Celica 8 (Demonstracija serije)
- Izboljšana razlaga, kaj pričakovati
- Dodan razdelek za odpravljanje težav
- Vključeni ukazi CLI za odpravljanje napak
- Boljše oblikovanje prikaza izhodnih podatkov

### 3. `Workshop/notebooks/session06_README.md` (Nova datoteka)

**Ustvarjena obsežna dokumentacija, ki zajema:**

1. **Pregled**: Diagram arhitekture in razlaga komponent
2. **Integracija SDK**: Zgledi kode po uradnih vzorcih
3. **Predpogoji**: Navodila za nastavitev korak za korakom
4. **Uporaba**: Kako zagnati in prilagoditi zvezek
5. **Vzdevki modelov**: Razlaga strojno optimiziranih različic
6. **Odpravljanje težav**: Pogoste težave in rešitve
7. **Razširitev**: Kako dodati namene, modele in logiko po meri
8. **Nasveti za zmogljivost**: Najboljše prakse za uporabo v produkciji
9. **Viri**: Povezave do uradne dokumentacije in skupnosti

## Implementacija vzorca SDK

### Uradni vzorec (iz dokumentacije Foundry Local)

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

### Naša implementacija (v workshop_utils)

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

**Prednosti našega pristopa:**
- ✅ Natančno sledi uradnemu vzorcu SDK
- ✅ Dodano predpomnjenje za preprečevanje ponovne inicializacije
- ✅ Vključuje logiko ponovnega poskusa za robustnost v produkciji
- ✅ Podpira sledenje uporabi žetonov
- ✅ Zagotavlja boljša sporočila o napakah
- ✅ Ostaja združljiv z uradnimi zgledi

## Spremembe kataloga modelov

### Prej
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Potem
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Razlog:** Zamenjan 'gpt-oss-20b' (nestandardni vzdevek) z 'phi-3.5-mini' (uradni vzdevek Foundry Local).

## Odvisnosti

### Posodobljen requirements.txt

Datoteka requirements.txt za Workshop že vključuje:
```
foundry-local-sdk
openai>=1.30.0
```

To so edini paketi, potrebni za integracijo Foundry Local.

## Testiranje posodobitev

### 1. Preverite, ali Foundry Local deluje

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Preverite razpoložljive modele

```bash
foundry model ls
```

Prepričajte se, da so ti modeli na voljo ali se bodo samodejno prenesli:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Zaženite zvezek

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Ali odprite v VS Code in zaženite vse celice.

### 4. Pričakovano vedenje

**Celica 1 (Namestitev):** Uspešno namesti pakete  
**Celica 2 (Nastavitev):** Brez napak, uvozi delujejo  
**Celica 3 (Preverjanje):** Prikaže ✓ z seznamom modelov  
**Celica 4 (Test namena):** Prikaže rezultate zaznavanja namena  
**Celica 5 (Usmerjevalnik):** Prikaže ✓ Funkcija usmerjanja pripravljena  
**Celica 6 (Izvedba):** Usmerja pozive na modele, prikaže rezultate  

### 5. Odpravljanje težav pri napakah povezave

Če vidite `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Spremenljivke okolja

Podprte so naslednje spremenljivke okolja:

| Spremenljivka | Privzeto | Opis |
|---------------|----------|------|
| `SHOW_USAGE` | `0` | Nastavite na `1`, da natisnete uporabo žetonov |
| `RETRY_ON_FAIL` | `1` | Omogočite logiko ponovnega poskusa |
| `RETRY_BACKOFF` | `1.0` | Začetna zamuda pri ponovnem poskusu (sekunde) |
| `FOUNDRY_LOCAL_ENDPOINT` | Samodejno | Prepišite končno točko storitve |

### Zgledi uporabe

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migracija iz starega vzorca

Če imate obstoječo kodo, ki uporablja neposredne klice API, tukaj je, kako migrirati:

### Prej (Neposredni API)
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

### Potem (SDK)
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

### Prednosti migracije
- ✅ Samodejno upravljanje storitev
- ✅ Razrešitev vzdevkov modelov
- ✅ Izbor strojne optimizacije
- ✅ Boljše obravnavanje napak
- ✅ Združljivost z OpenAI SDK
- ✅ Podpora za pretakanje

## Reference

### Uradna dokumentacija
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK Source**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Troubleshooting**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Viri za Workshop
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Vzorec zvezka**: `Workshop/notebooks/session06_models_router.ipynb`

### Skupnost
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Naslednji koraki

1. **Preglejte spremembe**: Preberite posodobljene datoteke  
2. **Testirajte zvezek**: Zaženite session06_models_router.ipynb  
3. **Preverite SDK**: Prepričajte se, da je foundry-local-sdk nameščen  
4. **Preverite storitev**: Potrdite, da Foundry Local deluje  
5. **Raziskujte dokumentacijo**: Preberite nov session06_README.md  

## Povzetek

Te posodobitve zagotavljajo, da gradivo Workshop natančno sledi **uradnim vzorcem SDK Foundry Local**, kot je dokumentirano v GitHub repozitoriju. Vsi zgledi kode, dokumentacija in pripomočki so zdaj usklajeni z Microsoftovimi priporočenimi najboljšimi praksami za lokalno uvajanje modelov AI.

Spremembe izboljšujejo:
- ✅ **Pravilnost**: Uporablja uradne vzorce SDK  
- ✅ **Dokumentacijo**: Obsežne razlage in zgledi  
- ✅ **Obravnavanje napak**: Boljša sporočila in vodstvo za odpravljanje težav  
- ✅ **Vzdrževanje**: Sledi uradnim konvencijam  
- ✅ **Uporabniško izkušnjo**: Jasnejša navodila in pomoč pri odpravljanju napak  

---

**Posodobljeno:** 8. oktober 2025  
**Različica SDK:** foundry-local-sdk (zadnja)  
**Branch Workshop:** Reactor  

---

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.