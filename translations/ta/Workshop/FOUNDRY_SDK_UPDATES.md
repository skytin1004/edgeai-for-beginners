<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-11T11:46:36+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "ta"
}
-->
# Foundry Local SDK புதுப்பிப்புகள்

## கண்ணோட்டம்

**Foundry Local Python SDK**-ஐ சரியாக பயன்படுத்துவதற்கான Workshop நோட்புக் மற்றும் உதவிகளை கீழே உள்ள முறைமைகளின் அடிப்படையில் புதுப்பிக்கப்பட்டது:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## மாற்றப்பட்ட கோப்புகள்

### 1. `Workshop/samples/workshop_utils.py`

**மாற்றங்கள்:**
- ✅ `foundry-local-sdk` பாக்கேஜுக்கான இறக்குமதி பிழை கையாளுதல் சேர்க்கப்பட்டது
- ✅ அதிகாரப்பூர்வ SDK முறைமைகளுடன் ஆவணங்களை மேம்படுத்தியது
- ✅ Unicode சின்னங்களுடன் பதிவு செய்யும் செயல்பாட்டை மேம்படுத்தியது (✓, ✗, ⚠)
- ✅ எடுத்துக்காட்டுகளுடன் விரிவான docstrings சேர்க்கப்பட்டது
- ✅ CLI கட்டளைகளை குறிப்பிடும் சிறந்த பிழை செய்திகளை சேர்த்தது
- ✅ அதிகாரப்பூர்வ SDK ஆவணங்களுக்கு பொருந்தும் வகையில் கருத்துகளை புதுப்பித்தது

**முக்கிய மேம்பாடுகள்:**

#### இறக்குமதி பிழை கையாளுதல்
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### மேம்படுத்தப்பட்ட `get_client()` செயல்பாடு
- SDK தொடக்க முறைமையைப் பற்றிய விரிவான ஆவணங்களைச் சேர்த்தது
- `FoundryLocalManager` சேவையை தானாக தொடங்குவதை விளக்கியது
- மாடல் பெயர்ப் புனைவை hardware-optimized மாறுபாடுகளுக்கு தீர்மானிக்கிறது என்பதை விளக்கியது
- இறுதிப் புள்ளி தகவலுடன் பதிவு செயல்பாட்டை மேம்படுத்தியது
- பிழை செய்திகளைச் சிறப்பாகச் செய்யும் troubleshoot வழிகாட்டுதல்களைச் சேர்த்தது

#### மேம்படுத்தப்பட்ட `chat_once()` செயல்பாடு
- பயன்பாட்டு எடுத்துக்காட்டுகளுடன் விரிவான docstring சேர்க்கப்பட்டது
- OpenAI SDK இணக்கத்தன்மையை விளக்கியது
- Streaming ஆதரவை ஆவணப்படுத்தியது (kwargs மூலம்)
- CLI கட்டளைகளை குறிப்பிடும் சிறந்த பிழை செய்திகளைச் சேர்த்தது
- மாடல் கிடைப்பதற்கான சோதனை குறித்த குறிப்புகளைச் சேர்த்தது

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**மாற்றங்கள்:**
- ✅ SDK குறிப்பு கொண்ட அனைத்து markdown செல்களையும் புதுப்பித்தது
- ✅ SDK முறைமைகளை விளக்க code கருத்துகளை மேம்படுத்தியது
- ✅ செல்களின் ஆவணங்கள் மற்றும் விளக்கங்களை மேம்படுத்தியது
- ✅ Troubleshooting வழிகாட்டுதல்களைச் சேர்த்தது
- ✅ மாடல் பட்டியலை புதுப்பித்தது ('gpt-oss-20b'-ஐ 'phi-3.5-mini'-ஆக மாற்றியது)
- ✅ காட்சி குறியீடுகளுடன் output வடிவமைப்பை மேம்படுத்தியது
- ✅ SDK இணைப்புகள் மற்றும் குறிப்புகளை முழுவதும் சேர்த்தது

**செல்-வாரியாக மேம்பாடுகள்:**

#### செல் 1 (தலைப்பு)
- SDK ஆவண இணைப்புகளைச் சேர்த்தது
- அதிகாரப்பூர்வ GitHub repository-களை குறிப்பிடப்பட்டது

#### செல் 2 (காட்சிப்படுத்தல்)
- எண் அடிப்படையிலான படிகள் மூலம் மறுவடிவமைக்கப்பட்டது
- நோக்கத்திற்கேற்ப வழிமுறையை விளக்கியது
- உள்ளூர் செயல்பாட்டின் நன்மைகளை வலியுறுத்தியது

#### செல் 3 (இணைப்பு நிறுவல்)
- ஒவ்வொரு பாக்கேஜும் என்ன வழங்குகிறது என்பதை விளக்கியது
- SDK திறன்களை ஆவணப்படுத்தியது (alias resolution, hardware optimization)

#### செல் 4 (சுற்றுச்சூழல் அமைப்பு)
- செயல்பாட்டு docstrings-ஐ மேம்படுத்தியது
- SDK முறைமைகளை விளக்கும் inline கருத்துகளைச் சேர்த்தது
- மாடல் பட்டியல் அமைப்பை ஆவணப்படுத்தியது
- முன்னுரிமை/திறன் பொருத்தத்தை விளக்கியது

#### செல் 5 (Catalog Check)
- காட்சி checkmarks (✓) சேர்க்கப்பட்டது
- output சிறப்பாக வடிவமைக்கப்பட்டது

#### செல் 6 (Intent Detection Test)
- output-ஐ அட்டவணை-வகை வடிவமாக மறுவடிவமைக்கப்பட்டது
- intent மற்றும் தேர்ந்தெடுக்கப்பட்ட மாடலைக் காட்டுகிறது

#### செல் 7 (Routing Function)
- விரிவான SDK முறைமையை விளக்கியது
- தொடக்கப் பாய்ச்சலை ஆவணப்படுத்தியது
- அனைத்து அம்சங்களையும் பட்டியலிட்டது (retry, tracking, errors)
- SDK குறிப்பு இணைப்பைச் சேர்த்தது

#### செல் 8 (Batch Demo)
- எதிர்பார்க்க வேண்டியதை விளக்கும் விளக்கத்தை மேம்படுத்தியது
- Troubleshooting பகுதியைச் சேர்த்தது
- Debugging-க்கு CLI கட்டளைகளைச் சேர்த்தது
- output காட்சி வடிவமைப்பை மேம்படுத்தியது

### 3. `Workshop/notebooks/session06_README.md` (புதிய கோப்பு)

**விரிவான ஆவணங்களை உருவாக்கியது:**

1. **கண்ணோட்டம்**: கட்டமைப்பு வரைபடம் மற்றும் கூற விளக்கம்
2. **SDK ஒருங்கிணைப்பு**: அதிகாரப்பூர்வ முறைமைகளைப் பின்பற்றும் code எடுத்துக்காட்டுகள்
3. **முன்னோட்டங்கள்**: படி-படி அமைப்பு வழிகாட்டுதல்
4. **பயன்பாடு**: நோட்புக் இயக்கம் மற்றும் தனிப்பயனாக்கம்
5. **மாடல் பெயர்ப் புனைவை**: hardware-optimized மாறுபாடுகளின் விளக்கம்
6. **Troubleshooting**: பொதுவான பிரச்சினைகள் மற்றும் தீர்வுகள்
7. **விரிவாக்கம்**: intents, models, மற்றும் தனிப்பயன் logic சேர்ப்பது எப்படி
8. **செயல்திறன் குறிப்புகள்**: உற்பத்தி பயன்பாட்டிற்கான சிறந்த நடைமுறைகள்
9. **வளங்கள்**: அதிகாரப்பூர்வ ஆவணங்கள் மற்றும் சமூக இணைப்புகள்

## SDK முறைமை செயல்பாடு

### அதிகாரப்பூர்வ முறைமை (Foundry Local ஆவணங்களில் இருந்து)

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

### எங்கள் செயல்பாடு (workshop_utils-ல்)

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

**எங்கள் அணுகுமுறையின் நன்மைகள்:**
- ✅ அதிகாரப்பூர்வ SDK முறைமையைச் சரியாகப் பின்பற்றுகிறது
- ✅ மீண்டும் தொடக்கத்தைத் தவிர்க்க caching சேர்க்கப்பட்டுள்ளது
- ✅ உற்பத்தி robustness-க்கு retry logic சேர்க்கப்பட்டுள்ளது
- ✅ token பயன்பாட்டை கண்காணிக்க ஆதரிக்கிறது
- ✅ சிறந்த பிழை செய்திகளை வழங்குகிறது
- ✅ அதிகாரப்பூர்வ எடுத்துக்காட்டுகளுடன் இணக்கமாக உள்ளது

## மாடல் பட்டியல் மாற்றங்கள்

### முந்தைய
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### தற்போதைய
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**காரணம்:** 'gpt-oss-20b' (non-standard alias)-ஐ 'phi-3.5-mini' (Foundry Local alias) ஆக மாற்றியது.

## சார்புகள்

### புதுப்பிக்கப்பட்ட requirements.txt

Workshop requirements.txt ஏற்கனவே கீழே உள்ளவற்றை உள்ளடக்கியது:
```
foundry-local-sdk
openai>=1.30.0
```

Foundry Local ஒருங்கிணைப்புக்கு தேவையானவை இவை மட்டுமே.

## புதுப்பிப்புகளை சோதித்தல்

### 1. Foundry Local இயங்குகிறது என்பதை உறுதிப்படுத்தவும்

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. கிடைக்கக்கூடிய மாடல்களைச் சரிபார்க்கவும்

```bash
foundry model ls
```

இந்த மாடல்கள் கிடைக்கின்றன அல்லது தானாக பதிவிறக்கம் செய்யப்படும்:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. நோட்புக் இயக்கவும்

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

அல்லது VS Code-ல் திறந்து அனைத்து செல்களையும் இயக்கவும்.

### 4. எதிர்பார்க்கப்படும் நடத்தை

**செல் 1 (Install):** பாக்கேஜ்கள் வெற்றிகரமாக நிறுவப்படும்
**செல் 2 (Setup):** பிழைகள் இல்லை, இறக்குமதி வேலை செய்கிறது
**செல் 3 (Verify):** ✓ மாடல் பட்டியலுடன் காட்டுகிறது
**செல் 4 (Test Intent):** intent detection முடிவுகளை காட்டுகிறது
**செல் 5 (Router):** ✓ Route செயல்பாடு தயாராக உள்ளது
**செல் 6 (Execute):** கேள்விகளை மாடல்களுக்கு வழிமாற்றுகிறது, முடிவுகளை காட்டுகிறது

### 5. இணைப்பு பிழைகளை Troubleshooting

நீங்கள் `APIConnectionError: Connection error` பார்க்கிறீர்கள் என்றால்:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## சுற்றுச்சூழல் மாறிகள்

கீழே உள்ள சுற்றுச்சூழல் மாறிகள் ஆதரிக்கப்படுகின்றன:

| மாறி | இயல்புநிலை | விளக்கம் |
|------|-----------|----------|
| `SHOW_USAGE` | `0` | token பயன்பாட்டை அச்சிட `1`-ஆக அமைக்கவும் |
| `RETRY_ON_FAIL` | `1` | retry logic-ஐ இயக்கவும் |
| `RETRY_BACKOFF` | `1.0` | தொடக்க retry தாமதம் (வினாடிகள்) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | சேவை இறுதிப்புள்ளியை override செய்யவும் |

### பயன்பாட்டு எடுத்துக்காட்டுகள்

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## பழைய முறைமையிலிருந்து இடமாற்றம்

நீங்கள் நேரடி API அழைப்புகளைப் பயன்படுத்தும் ஏற்கனவே உள்ள code வைத்திருந்தால், இதோ எப்படி இடமாற்றம் செய்யலாம்:

### முந்தைய (நேரடி API)
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

### தற்போதைய (SDK)
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

### இடமாற்றத்தின் நன்மைகள்
- ✅ தானாக சேவை மேலாண்மை
- ✅ மாடல் alias தீர்மானம்
- ✅ hardware optimization தேர்வு
- ✅ சிறந்த பிழை கையாளுதல்
- ✅ OpenAI SDK இணக்கத்தன்மை
- ✅ Streaming ஆதரவு

## குறிப்புகள்

### அதிகாரப்பூர்வ ஆவணங்கள்
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK மூல**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI குறிப்பு**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Troubleshooting**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop Resources
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Sample Notebook**: `Workshop/notebooks/session06_models_router.ipynb`

### சமூக
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## அடுத்த படிகள்

1. **மாற்றங்களை மதிப்பீடு செய்யவும்**: புதுப்பிக்கப்பட்ட கோப்புகளைப் படிக்கவும்
2. **நோட்புக் சோதனை**: session06_models_router.ipynb இயக்கவும்
3. **SDK உறுதிப்படுத்தவும்**: foundry-local-sdk நிறுவப்பட்டுள்ளது என்பதை உறுதிப்படுத்தவும்
4. **சேவைச் சரிபார்க்கவும்**: Foundry Local இயங்குகிறது என்பதை உறுதிப்படுத்தவும்
5. **ஆவணங்களை ஆராயவும்**: புதிய session06_README.md-ஐ படிக்கவும்

## சுருக்கம்

இந்த புதுப்பிப்புகள் Workshop பொருட்கள் **Foundry Local SDK முறைமைகளை** அதிகாரப்பூர்வ GitHub repository-யில் ஆவணப்படுத்தப்பட்டவாறு பின்பற்றுவதை உறுதிப்படுத்துகின்றன. அனைத்து code எடுத்துக்காட்டுகள், ஆவணங்கள், மற்றும் உதவிகள் Microsoft-ன் உள்ளூர் AI மாடல் இடமாற்றத்திற்கான பரிந்துரைக்கப்பட்ட சிறந்த நடைமுறைகளுடன் ஒத்துப்போகின்றன.

மாற்றங்கள் மேம்படுத்துகின்றன:
- ✅ **சரியானது**: அதிகாரப்பூர்வ SDK முறைமைகளைப் பயன்படுத்துகிறது
- ✅ **ஆவணங்கள்**: விரிவான விளக்கங்கள் மற்றும் எடுத்துக்காட்டுகள்
- ✅ **பிழை கையாளுதல்**: சிறந்த செய்திகள் மற்றும் troubleshoot வழிகாட்டுதல்
- ✅ **பராமரிப்பு**: அதிகாரப்பூர்வ ஒழுங்குகளைப் பின்பற்றுகிறது
- ✅ **பயனர் அனுபவம்**: தெளிவான வழிகாட்டுதல்கள் மற்றும் debugging உதவி

---

**புதுப்பிக்கப்பட்டது:** அக்டோபர் 8, 2025  
**SDK பதிப்பு:** foundry-local-sdk (latest)  
**Workshop Branch:** Reactor

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.