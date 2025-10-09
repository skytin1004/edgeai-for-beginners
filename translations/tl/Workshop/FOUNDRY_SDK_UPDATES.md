<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T19:12:23+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "tl"
}
-->
# Mga Update sa Foundry Local SDK

## Pangkalahatang-ideya

Na-update ang mga Workshop notebook at utilities upang maayos na magamit ang **opisyal na Foundry Local Python SDK** ayon sa mga pattern mula sa:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Mga Binagong File

### 1. `Workshop/samples/workshop_utils.py`

**Mga Pagbabago:**
- ✅ Idinagdag ang error handling para sa import ng package na `foundry-local-sdk`
- ✅ Pinahusay ang dokumentasyon gamit ang mga opisyal na pattern ng SDK
- ✅ Pinahusay ang logging gamit ang mga Unicode na simbolo (✓, ✗, ⚠)
- ✅ Idinagdag ang komprehensibong docstrings na may mga halimbawa
- ✅ Mas malinaw na mga mensahe ng error na tumutukoy sa mga utos ng CLI
- ✅ Na-update ang mga komento upang tumugma sa opisyal na dokumentasyon ng SDK

**Pangunahing Pagpapabuti:**

#### Error Handling sa Import
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Pinahusay na `get_client()` Function
- Idinagdag ang detalyadong dokumentasyon tungkol sa pattern ng pag-initialize ng SDK
- Nilinaw na awtomatikong sinisimulan ng `FoundryLocalManager` ang serbisyo
- Ipinaliwanag ang resolusyon ng model alias sa mga hardware-optimized na variant
- Pinahusay ang logging gamit ang impormasyon ng endpoint
- Mas malinaw na mga mensahe ng error na nagmumungkahi ng mga hakbang sa pag-troubleshoot

#### Pinahusay na `chat_once()` Function
- Idinagdag ang komprehensibong docstring na may mga halimbawa ng paggamit
- Nilinaw ang pagiging tugma sa OpenAI SDK
- Naidokumento ang suporta sa streaming (gamit ang kwargs)
- Pinahusay ang mga mensahe ng error na may mga mungkahi sa utos ng CLI
- Idinagdag ang mga tala tungkol sa pag-check ng availability ng modelo

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Mga Pagbabago:**
- ✅ Na-update ang lahat ng markdown cells na may mga reference sa SDK
- ✅ Pinahusay ang mga komento sa code na may mga paliwanag sa pattern ng SDK
- ✅ Pinahusay ang dokumentasyon at mga paliwanag sa bawat cell
- ✅ Idinagdag ang gabay sa pag-troubleshoot
- ✅ Na-update ang catalog ng modelo (pinalitan ang 'gpt-oss-20b' ng 'phi-3.5-mini')
- ✅ Mas pinahusay na pag-format ng output na may mga visual indicator
- ✅ Idinagdag ang mga link at reference ng SDK sa kabuuan

**Mga Update sa Bawat Cell:**

#### Cell 1 (Pamagat)
- Idinagdag ang mga link sa dokumentasyon ng SDK
- Binanggit ang mga opisyal na repository ng GitHub

#### Cell 2 (Scenario)
- Na-reformat gamit ang mga naka-number na hakbang
- Nilinaw ang pattern ng intent-based routing
- Binibigyang-diin ang mga benepisyo ng lokal na pagpapatupad

#### Cell 3 (Pag-install ng Dependency)
- Idinagdag ang paliwanag kung ano ang ibinibigay ng bawat package
- Naidokumento ang mga kakayahan ng SDK (resolusyon ng alias, hardware optimization)

#### Cell 4 (Setup ng Kapaligiran)
- Pinahusay ang mga docstring ng function
- Idinagdag ang mga inline na komento na nagpapaliwanag ng mga pattern ng SDK
- Naidokumento ang istruktura ng catalog ng modelo
- Nilinaw ang pag-prioritize/pagtutugma ng kakayahan

#### Cell 5 (Pag-check ng Catalog)
- Idinagdag ang mga visual na checkmark (✓)
- Mas pinahusay na pag-format ng output

#### Cell 6 (Pagsubok sa Intent Detection)
- Na-reformat ang output bilang table-style
- Ipinapakita ang parehong intent at napiling modelo

#### Cell 7 (Routing Function)
- Komprehensibong paliwanag ng pattern ng SDK
- Naidokumento ang daloy ng pag-initialize
- Nakalista ang lahat ng mga tampok (retry, tracking, errors)
- Idinagdag ang link ng reference ng SDK

#### Cell 8 (Batch Demo)
- Pinahusay ang paliwanag kung ano ang aasahan
- Idinagdag ang seksyon ng pag-troubleshoot
- Isinama ang mga utos ng CLI para sa debugging
- Mas pinahusay na pag-format ng display ng output

### 3. `Workshop/notebooks/session06_README.md` (Bagong File)

**Nilikha ang komprehensibong dokumentasyon na sumasaklaw sa:**

1. **Pangkalahatang-ideya**: Diagram ng arkitektura at paliwanag ng mga bahagi
2. **Integrasyon ng SDK**: Mga halimbawa ng code na sumusunod sa mga opisyal na pattern
3. **Mga Kinakailangan**: Step-by-step na mga tagubilin sa setup
4. **Paggamit**: Paano patakbuhin at i-customize ang notebook
5. **Mga Alias ng Modelo**: Paliwanag ng mga hardware-optimized na variant
6. **Pag-troubleshoot**: Mga karaniwang isyu at solusyon
7. **Pagpapalawak**: Paano magdagdag ng intents, modelo, at custom na lohika
8. **Mga Tip sa Pagganap**: Mga pinakamahusay na kasanayan para sa paggamit sa produksyon
9. **Mga Mapagkukunan**: Mga link sa opisyal na dokumentasyon at komunidad

## Implementasyon ng Pattern ng SDK

### Opisyal na Pattern (mula sa Foundry Local docs)

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

### Aming Implementasyon (sa workshop_utils)

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

**Mga Benepisyo ng Aming Diskarte:**
- ✅ Sumusunod nang eksakto sa opisyal na pattern ng SDK
- ✅ Nagdaragdag ng caching upang maiwasan ang paulit-ulit na pag-initialize
- ✅ May kasamang retry logic para sa tibay sa produksyon
- ✅ Sinusuportahan ang pagsubaybay sa paggamit ng token
- ✅ Nagbibigay ng mas mahusay na mga mensahe ng error
- ✅ Nanatiling tugma sa mga opisyal na halimbawa

## Mga Pagbabago sa Catalog ng Modelo

### Dati
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Pagkatapos
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Dahilan:** Pinalitan ang 'gpt-oss-20b' (hindi karaniwang alias) ng 'phi-3.5-mini' (opisyal na Foundry Local alias).

## Mga Kinakailangan

### Na-update na requirements.txt

Ang Workshop requirements.txt ay mayroon nang:
```
foundry-local-sdk
openai>=1.30.0
```

Ito lamang ang mga package na kinakailangan para sa integrasyon ng Foundry Local.

## Pagsubok sa Mga Update

### 1. Siguraduhing Tumatakbo ang Foundry Local

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. I-check ang Mga Available na Modelo

```bash
foundry model ls
```

Siguraduhing available ang mga modelong ito o awtomatikong mada-download:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Patakbuhin ang Notebook

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

O buksan sa VS Code at patakbuhin ang lahat ng cells.

### 4. Inaasahang Resulta

**Cell 1 (Install):** Matagumpay na mai-install ang mga package  
**Cell 2 (Setup):** Walang error, gumagana ang mga import  
**Cell 3 (Verify):** Ipinapakita ang ✓ na may listahan ng modelo  
**Cell 4 (Test Intent):** Ipinapakita ang mga resulta ng intent detection  
**Cell 5 (Router):** Ipinapakita ang ✓ Handa na ang route function  
**Cell 6 (Execute):** Ipinapasa ang mga prompt sa mga modelo, ipinapakita ang mga resulta  

### 5. Pag-troubleshoot ng Mga Error sa Koneksyon

Kung makakita ka ng `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Mga Environment Variable

Ang sumusunod na mga environment variable ay sinusuportahan:

| Variable | Default | Paglalarawan |
|----------|---------|--------------|
| `SHOW_USAGE` | `0` | Itakda sa `1` upang ipakita ang paggamit ng token |
| `RETRY_ON_FAIL` | `1` | Paganahin ang retry logic |
| `RETRY_BACKOFF` | `1.0` | Paunang delay sa retry (segundo) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | I-override ang service endpoint |

### Mga Halimbawa ng Paggamit

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Paglipat mula sa Lumang Pattern

Kung mayroon kang umiiral na code na gumagamit ng direktang API calls, narito kung paano lumipat:

### Dati (Direktang API)
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

### Pagkatapos (SDK)
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

### Mga Benepisyo ng Paglipat
- ✅ Awtomatikong pamamahala ng serbisyo
- ✅ Resolusyon ng model alias
- ✅ Pagpili ng hardware optimization
- ✅ Mas mahusay na paghawak ng error
- ✅ Pagiging tugma sa OpenAI SDK
- ✅ Suporta sa streaming

## Mga Sanggunian

### Opisyal na Dokumentasyon
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local  
- **Pinagmulan ng Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md  
- **Pag-troubleshoot**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md  

### Mga Mapagkukunan ng Workshop
- **Session 06 README**: `Workshop/notebooks/session06_README.md`  
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`  
- **Sample Notebook**: `Workshop/notebooks/session06_models_router.ipynb`  

### Komunidad
- **Discord**: https://aka.ms/foundry-local-discord  
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues  

## Mga Susunod na Hakbang

1. **Suriin ang Mga Pagbabago**: Basahin ang mga na-update na file  
2. **Subukan ang Notebook**: Patakbuhin ang session06_models_router.ipynb  
3. **I-verify ang SDK**: Siguraduhing naka-install ang foundry-local-sdk  
4. **I-check ang Serbisyo**: Tiyaking tumatakbo ang Foundry Local  
5. **Suriin ang Mga Dokumento**: Basahin ang bagong session06_README.md  

## Buod

Tinitiyak ng mga update na ito na ang mga materyales ng Workshop ay sumusunod sa **opisyal na mga pattern ng Foundry Local SDK** na eksaktong nakadokumento sa repository ng GitHub. Ang lahat ng mga halimbawa ng code, dokumentasyon, at utilities ay naaayon na ngayon sa mga inirerekomendang pinakamahusay na kasanayan ng Microsoft para sa lokal na pag-deploy ng AI model.

Ang mga pagbabago ay nagpapabuti sa:
- ✅ **Kawastuhan**: Gumagamit ng mga opisyal na pattern ng SDK  
- ✅ **Dokumentasyon**: Komprehensibong paliwanag at mga halimbawa  
- ✅ **Paghawak ng Error**: Mas malinaw na mga mensahe at gabay sa pag-troubleshoot  
- ✅ **Pagpapanatili**: Sumusunod sa mga opisyal na kombensyon  
- ✅ **Karanasan ng Gumagamit**: Mas malinaw na mga tagubilin at tulong sa debugging  

---

**Na-update:** Oktubre 8, 2025  
**Bersyon ng SDK:** foundry-local-sdk (pinakabago)  
**Sangay ng Workshop:** Reactor  

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.