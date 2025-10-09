<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T21:04:37+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "sw"
}
-->
# Sasisho za Foundry Local SDK

## Muhtasari

Tumeboresha daftari za Workshop na zana ili kutumia **Foundry Local Python SDK rasmi** kwa kufuata mifumo kutoka:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Mafaili Yaliyorekebishwa

### 1. `Workshop/samples/workshop_utils.py`

**Mabadiliko:**
- ✅ Imeongezwa utunzaji wa makosa ya kuingiza kwa kifurushi cha `foundry-local-sdk`
- ✅ Imeboreshwa nyaraka kwa mifumo rasmi ya SDK
- ✅ Imeboreshwa uandishi wa kumbukumbu kwa alama za Unicode (✓, ✗, ⚠)
- ✅ Imeongezwa maelezo ya kina ya docstrings na mifano
- ✅ Ujumbe wa makosa bora unaorejelea amri za CLI
- ✅ Imeboreshwa maoni ili yaendane na nyaraka rasmi za SDK

**Maboresho Muhimu:**

#### Utunzaji wa Makosa ya Kuingiza
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Kazi Iliyoboreshwa ya `get_client()`
- Imeongezwa nyaraka za kina kuhusu muundo wa kuanzisha SDK
- Imefafanua kuwa `FoundryLocalManager` huanzisha huduma moja kwa moja
- Imeelezea utatuzi wa alias ya modeli kwa varianiti zilizoboreshwa kwa vifaa
- Imeboreshwa uandishi wa kumbukumbu na taarifa za endpoint
- Ujumbe bora wa makosa unaopendekeza hatua za kutatua matatizo

#### Kazi Iliyoboreshwa ya `chat_once()`
- Imeongezwa docstring ya kina na mifano ya matumizi
- Imefafanua utangamano wa SDK ya OpenAI
- Imeandika msaada wa utiririshaji (kupitia kwargs)
- Ujumbe bora wa makosa unaopendekeza amri za CLI
- Imeongezwa maelezo kuhusu ukaguzi wa upatikanaji wa modeli

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Mabadiliko:**
- ✅ Imeboreshwa seli zote za markdown na marejeleo ya SDK
- ✅ Imeboreshwa maoni ya msimbo na maelezo ya mifumo ya SDK
- ✅ Imeboreshwa nyaraka za seli na maelezo
- ✅ Imeongezwa mwongozo wa kutatua matatizo
- ✅ Imeboreshwa katalogi ya modeli (imebadilisha 'gpt-oss-20b' na 'phi-3.5-mini')
- ✅ Uwasilishaji bora wa matokeo na viashiria vya kuona
- ✅ Imeongezwa viungo na marejeleo ya SDK kote

**Mabadiliko ya Seli kwa Seli:**

#### Seli ya 1 (Kichwa)
- Imeongezwa viungo vya nyaraka za SDK
- Imeelezea hifadhi rasmi za GitHub

#### Seli ya 2 (Hali)
- Imeundwa upya kwa hatua zilizoorodheshwa
- Imefafanua muundo wa usambazaji wa nia
- Imeangazia faida za utekelezaji wa ndani

#### Seli ya 3 (Usakinishaji wa Mahitaji)
- Imeelezea kile kila kifurushi kinachotoa
- Imeandika uwezo wa SDK (utatuzi wa alias, uboreshaji wa vifaa)

#### Seli ya 4 (Usanidi wa Mazingira)
- Imeboreshwa docstrings za kazi
- Imeongezwa maoni ya ndani yanayoelezea mifumo ya SDK
- Imeandika muundo wa katalogi ya modeli
- Imefafanua upendeleo/matching wa uwezo

#### Seli ya 5 (Ukaguzi wa Katalogi)
- Imeongezwa alama za ukaguzi wa kuona (✓)
- Imeboreshwa uwasilishaji wa matokeo

#### Seli ya 6 (Jaribio la Kugundua Nia)
- Imeundwa upya matokeo kama mtindo wa jedwali
- Inaonyesha nia na modeli iliyochaguliwa

#### Seli ya 7 (Kazi ya Usambazaji)
- Maelezo ya kina ya muundo wa SDK
- Imeandika mtiririko wa kuanzisha
- Imeorodhesha vipengele vyote (retry, ufuatiliaji, makosa)
- Imeongezwa kiungo cha marejeleo ya SDK

#### Seli ya 8 (Demo ya Batch)
- Maelezo yaliyoboreshwa ya kile cha kutarajia
- Imeongezwa sehemu ya kutatua matatizo
- Imejumuisha amri za CLI kwa urekebishaji
- Uwasilishaji bora wa matokeo

### 3. `Workshop/notebooks/session06_README.md` (Faili Mpya)

**Imeundwa nyaraka za kina zinazojumuisha:**

1. **Muhtasari**: Mchoro wa usanifu na maelezo ya vipengele
2. **Ujumuishaji wa SDK**: Mifano ya msimbo inayofuata mifumo rasmi
3. **Mahitaji**: Maelekezo ya hatua kwa hatua ya usanidi
4. **Matumizi**: Jinsi ya kuendesha na kubinafsisha daftari
5. **Alias za Modeli**: Maelezo ya varianiti zilizoboreshwa kwa vifaa
6. **Kutatua Matatizo**: Masuala ya kawaida na suluhisho
7. **Kupanua**: Jinsi ya kuongeza nia, modeli, na mantiki maalum
8. **Vidokezo vya Utendaji**: Mbinu bora kwa matumizi ya uzalishaji
9. **Rasilimali**: Viungo vya nyaraka rasmi na jamii

## Utekelezaji wa Muundo wa SDK

### Muundo Rasmi (kutoka nyaraka za Foundry Local)

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

### Utekelezaji Wetu (katika workshop_utils)

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

**Faida za Mbinu Yetu:**
- ✅ Inafuata muundo rasmi wa SDK kikamilifu
- ✅ Inaongeza caching ili kuepuka kuanzisha mara kwa mara
- ✅ Inajumuisha mantiki ya retry kwa uimara wa uzalishaji
- ✅ Inasaidia ufuatiliaji wa matumizi ya tokeni
- ✅ Inatoa ujumbe bora wa makosa
- ✅ Inabaki sambamba na mifano rasmi

## Mabadiliko ya Katalogi ya Modeli

### Kabla
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Baada
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Sababu:** Imebadilisha 'gpt-oss-20b' (alias isiyo rasmi) na 'phi-3.5-mini' (alias rasmi ya Foundry Local).

## Mahitaji

### Sasisho la requirements.txt

Faili ya requirements.txt ya Workshop tayari inajumuisha:
```
foundry-local-sdk
openai>=1.30.0
```

Haya ndiyo tu mahitaji ya ujumuishaji wa Foundry Local.

## Kupima Sasisho

### 1. Hakikisha Foundry Local Inaendesha

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Angalia Modeli Zinazopatikana

```bash
foundry model ls
```

Hakikisha modeli hizi zinapatikana au zitapakuliwa moja kwa moja:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Endesha Daftari

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Au fungua katika VS Code na endesha seli zote.

### 4. Tabia Inayotarajiwa

**Seli ya 1 (Usakinishaji):** Inasakinisha vifurushi kwa mafanikio  
**Seli ya 2 (Usanidi):** Hakuna makosa, uingizaji unafanya kazi  
**Seli ya 3 (Ukaguzi):** Inaonyesha ✓ na orodha ya modeli  
**Seli ya 4 (Jaribio la Nia):** Inaonyesha matokeo ya kugundua nia  
**Seli ya 5 (Router):** Inaonyesha ✓ Kazi ya usambazaji iko tayari  
**Seli ya 6 (Tekeleza):** Inasambaza maelekezo kwa modeli, inaonyesha matokeo  

### 5. Kutatua Makosa ya Muunganisho

Ikiwa utaona `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Vigezo vya Mazingira

Vigezo vifuatavyo vya mazingira vinasaidiwa:

| Kigezo | Chaguo-msingi | Maelezo |
|--------|--------------|---------|
| `SHOW_USAGE` | `0` | Weka `1` ili kuchapisha matumizi ya tokeni |
| `RETRY_ON_FAIL` | `1` | Washa mantiki ya retry |
| `RETRY_BACKOFF` | `1.0` | Muda wa kuchelewa wa retry wa awali (sekunde) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Badilisha endpoint ya huduma |

### Mifano ya Matumizi

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Kuhama kutoka Muundo wa Zamani

Ikiwa una msimbo uliopo unaotumia miito ya moja kwa moja ya API, hapa kuna jinsi ya kuhama:

### Kabla (API ya Moja kwa Moja)
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

### Baada (SDK)
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

### Faida za Kuhama
- ✅ Usimamizi wa huduma moja kwa moja
- ✅ Utatuzi wa alias ya modeli
- ✅ Uchaguzi wa uboreshaji wa vifaa
- ✅ Utunzaji bora wa makosa
- ✅ Utangamano wa SDK ya OpenAI
- ✅ Msaada wa utiririshaji

## Marejeleo

### Nyaraka Rasmi
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Chanzo cha SDK ya Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Marejeleo ya CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Kutatua Matatizo**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Rasilimali za Workshop
- **README ya Session 06**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Daftari la Mfano**: `Workshop/notebooks/session06_models_router.ipynb`

### Jamii
- **Discord**: https://aka.ms/foundry-local-discord
- **Masuala ya GitHub**: https://github.com/microsoft/Foundry-Local/issues

## Hatua Zifuatazo

1. **Kagua Mabadiliko**: Soma faili zilizosasishwa
2. **Jaribu Daftari**: Endesha session06_models_router.ipynb
3. **Hakiki SDK**: Hakikisha foundry-local-sdk imewekwa
4. **Angalia Huduma**: Thibitisha Foundry Local inaendesha
5. **Chunguza Nyaraka**: Soma session06_README.md mpya

## Muhtasari

Sasisho hizi zinahakikisha vifaa vya Workshop vinafuata **mifumo rasmi ya Foundry Local SDK** kama ilivyoandikwa katika hifadhi ya GitHub. Mifano yote ya msimbo, nyaraka, na zana sasa zinaendana na mbinu bora zinazopendekezwa na Microsoft kwa usambazaji wa modeli za AI za ndani.

Mabadiliko haya yanaboresha:
- ✅ **Usahihi**: Inatumia mifumo rasmi ya SDK
- ✅ **Nyaraka**: Maelezo ya kina na mifano
- ✅ **Utunzaji wa Makosa**: Ujumbe bora na mwongozo wa kutatua matatizo
- ✅ **Uwezo wa Kutunza**: Inafuata mikataba rasmi
- ✅ **Uzoefu wa Mtumiaji**: Maelekezo wazi na msaada wa urekebishaji

---

**Imesasishwa:** Oktoba 8, 2025  
**Toleo la SDK:** foundry-local-sdk (la hivi karibuni)  
**Tawi la Workshop:** Reactor

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.