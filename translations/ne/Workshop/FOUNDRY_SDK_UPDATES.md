<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T09:17:59+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "ne"
}
-->
# Foundry Local SDK अपडेटहरू

## अवलोकन

**Foundry Local Python SDK** को आधिकारिक ढाँचाहरू प्रयोग गर्दै **Workshop** नोटबुकहरू र युटिलिटीहरू अद्यावधिक गरिएका छन्:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## संशोधित फाइलहरू

### 1. `Workshop/samples/workshop_utils.py`

**परिवर्तनहरू:**
- ✅ `foundry-local-sdk` प्याकेजको लागि आयात त्रुटि ह्यान्डलिंग थपियो
- ✅ आधिकारिक SDK ढाँचाहरूको साथ दस्तावेजीकरण सुधार गरियो
- ✅ Unicode प्रतीकहरू (✓, ✗, ⚠) सहित लगिङ सुधार गरियो
- ✅ उदाहरणहरू सहित व्यापक डकस्ट्रिङहरू थपियो
- ✅ CLI कमाण्डहरूको सन्दर्भ दिने राम्रो त्रुटि सन्देशहरू थपियो
- ✅ आधिकारिक SDK दस्तावेजीकरणसँग मेल खाने टिप्पणीहरू अद्यावधिक गरियो

**मुख्य सुधारहरू:**

#### आयात त्रुटि ह्यान्डलिंग
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### सुधारिएको `get_client()` फङ्सन
- SDK सुरुवात ढाँचाको बारेमा विस्तृत दस्तावेजीकरण थपियो
- स्पष्ट गरियो कि `FoundryLocalManager` सेवा स्वचालित रूपमा सुरु गर्छ
- हार्डवेयर-अप्टिमाइज्ड भेरियन्टहरूमा मोडेल उपनाम समाधानको व्याख्या गरियो
- अन्त बिन्दु जानकारी सहित लगिङ सुधार गरियो
- समस्या समाधान चरणहरू सुझाव दिने राम्रो त्रुटि सन्देशहरू थपियो

#### सुधारिएको `chat_once()` फङ्सन
- प्रयोगका उदाहरणहरू सहित व्यापक डकस्ट्रिङ थपियो
- OpenAI SDK अनुकूलता स्पष्ट गरियो
- स्ट्रिमिङ समर्थन (kwargs मार्फत) दस्तावेज गरियो
- CLI कमाण्ड सुझाव दिने सुधारिएको त्रुटि सन्देशहरू थपियो
- मोडेल उपलब्धता जाँच गर्ने नोटहरू थपियो

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**परिवर्तनहरू:**
- ✅ सबै मार्कडाउन सेलहरू SDK सन्दर्भहरूसँग अद्यावधिक गरियो
- ✅ SDK ढाँचाको व्याख्या सहित कोड टिप्पणीहरू सुधार गरियो
- ✅ सेल दस्तावेजीकरण र व्याख्या सुधार गरियो
- ✅ समस्या समाधान मार्गदर्शन थपियो
- ✅ मोडेल क्याटलग अद्यावधिक गरियो ('gpt-oss-20b' लाई 'phi-3.5-mini' ले प्रतिस्थापन गरियो)
- ✅ दृश्य संकेतकहरू सहित राम्रो आउटपुट ढाँचाकरण
- ✅ SDK लिंकहरू र सन्दर्भहरू भरमा थपियो

**सेल-दर-सेल अद्यावधिकहरू:**

#### सेल 1 (शीर्षक)
- SDK दस्तावेजीकरण लिंकहरू थपियो
- आधिकारिक GitHub रिपोजिटरीहरूको सन्दर्भ दिइयो

#### सेल 2 (परिदृश्य)
- क्रमबद्ध चरणहरू सहित पुन: ढाँचाकरण गरियो
- उद्देश्य-आधारित राउटिङ ढाँचालाई स्पष्ट गरियो
- स्थानीय कार्यान्वयनका फाइदाहरूलाई जोड दिइयो

#### सेल 3 (निर्भरता स्थापना)
- प्रत्येक प्याकेजले के प्रदान गर्छ भन्ने व्याख्या थपियो
- SDK क्षमताहरू (उपनाम समाधान, हार्डवेयर अप्टिमाइजेशन) दस्तावेज गरियो

#### सेल 4 (पर्यावरण सेटअप)
- फङ्सन डकस्ट्रिङहरू सुधार गरियो
- SDK ढाँचाहरू व्याख्या गर्ने इनलाइन टिप्पणीहरू थपियो
- मोडेल क्याटलग संरचना दस्तावेज गरियो
- प्राथमिकता/क्षमता मिलान स्पष्ट गरियो

#### सेल 5 (क्याटलग जाँच)
- दृश्य चेकमार्कहरू (✓) थपियो
- राम्रो ढाँचाकरण गरिएको आउटपुट

#### सेल 6 (उद्देश्य पत्ता लगाउने परीक्षण)
- आउटपुटलाई तालिका शैलीमा पुन: ढाँचाकरण गरियो
- उद्देश्य र चयन गरिएको मोडेल दुवै देखाउँछ

#### सेल 7 (राउटिङ फङ्सन)
- व्यापक SDK ढाँचाको व्याख्या
- सुरुवात प्रवाह दस्तावेज गरियो
- सबै सुविधाहरू सूचीबद्ध गरियो (पुन: प्रयास, ट्र्याकिङ, त्रुटिहरू)
- SDK सन्दर्भ लिंक थपियो

#### सेल 8 (ब्याच डेमो)
- के अपेक्षा गर्ने भन्ने व्याख्या सुधार गरियो
- समस्या समाधान खण्ड थपियो
- डिबगिङका लागि CLI कमाण्डहरू समावेश गरियो
- राम्रो ढाँचाकरण गरिएको आउटपुट प्रदर्शन

### 3. `Workshop/notebooks/session06_README.md` (नयाँ फाइल)

**व्यापक दस्तावेजीकरण सिर्जना गरियो जसमा समावेश छ:**

1. **अवलोकन**: आर्किटेक्चर डायग्राम र कम्पोनेन्ट व्याख्या
2. **SDK एकीकरण**: आधिकारिक ढाँचाहरू अनुसरण गर्ने कोड उदाहरणहरू
3. **पूर्वापेक्षाहरू**: चरण-दर-चरण सेटअप निर्देशनहरू
4. **प्रयोग**: नोटबुक कसरी चलाउने र अनुकूलन गर्ने
5. **मोडेल उपनामहरू**: हार्डवेयर-अप्टिमाइज्ड भेरियन्टहरूको व्याख्या
6. **समस्या समाधान**: सामान्य समस्याहरू र समाधानहरू
7. **विस्तार गर्ने**: उद्देश्यहरू, मोडेलहरू, र अनुकूलन तर्क थप्ने तरिका
8. **प्रदर्शन सुझावहरू**: उत्पादन प्रयोगका लागि उत्तम अभ्यासहरू
9. **स्रोतहरू**: आधिकारिक दस्तावेज र समुदायका लिंकहरू

## SDK ढाँचाको कार्यान्वयन

### आधिकारिक ढाँचा (Foundry Local दस्तावेजबाट)

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

### हाम्रो कार्यान्वयन (workshop_utils मा)

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

**हाम्रो दृष्टिकोणका फाइदाहरू:**
- ✅ आधिकारिक SDK ढाँचालाई ठ्याक्कै अनुसरण गर्छ
- ✅ बारम्बार सुरुवातबाट बच्न क्यासिङ थप्छ
- ✅ उत्पादन मजबूतीका लागि पुन: प्रयास तर्क समावेश गर्छ
- ✅ टोकन प्रयोग ट्र्याकिङ समर्थन गर्छ
- ✅ राम्रो त्रुटि सन्देशहरू प्रदान गर्छ
- ✅ आधिकारिक उदाहरणहरूसँग अनुकूल रहन्छ

## मोडेल क्याटलग परिवर्तनहरू

### पहिले
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### पछि
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**कारण:** 'gpt-oss-20b' (गैर-मानक उपनाम) लाई 'phi-3.5-mini' (आधिकारिक Foundry Local उपनाम) ले प्रतिस्थापन गरियो।

## निर्भरताहरू

### अद्यावधिक requirements.txt

Workshop requirements.txt पहिले नै समावेश छ:
```
foundry-local-sdk
openai>=1.30.0
```

Foundry Local एकीकरणका लागि आवश्यक पर्ने यिनै प्याकेजहरू हुन्।

## अद्यावधिकहरूको परीक्षण

### 1. Foundry Local चलिरहेको छ भनी पुष्टि गर्नुहोस्

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. उपलब्ध मोडेलहरू जाँच गर्नुहोस्

```bash
foundry model ls
```

पक्का गर्नुहोस् कि यी मोडेलहरू उपलब्ध छन् वा स्वचालित रूपमा डाउनलोड हुनेछन्:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. नोटबुक चलाउनुहोस्

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

वा VS Code मा खोल्नुहोस् र सबै सेलहरू चलाउनुहोस्।

### 4. अपेक्षित व्यवहार

**सेल 1 (स्थापना):** प्याकेजहरू सफलतापूर्वक स्थापना गर्छ
**सेल 2 (सेटअप):** कुनै त्रुटि छैन, आयातहरू काम गर्छ
**सेल 3 (पुष्टि):** मोडेल सूची सहित ✓ देखाउँछ
**सेल 4 (परीक्षण उद्देश्य):** उद्देश्य पत्ता लगाउने परिणाम देखाउँछ
**सेल 5 (राउटर):** ✓ राउट फङ्सन तयार देखाउँछ
**सेल 6 (कार्यान्वयन):** मोडेलहरूमा प्रम्प्टहरू राउट गर्छ, परिणाम देखाउँछ

### 5. जडान त्रुटिहरू समस्या समाधान

यदि तपाईंले `APIConnectionError: Connection error` देख्नुभयो भने:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## वातावरण चरहरू

निम्न वातावरण चरहरू समर्थित छन्:

| चर | डिफल्ट | विवरण |
|-----|--------|--------|
| `SHOW_USAGE` | `0` | टोकन प्रयोग प्रिन्ट गर्न `1` मा सेट गर्नुहोस् |
| `RETRY_ON_FAIL` | `1` | पुन: प्रयास तर्क सक्षम गर्नुहोस् |
| `RETRY_BACKOFF` | `1.0` | प्रारम्भिक पुन: प्रयास ढिलाइ (सेकेन्ड) |
| `FOUNDRY_LOCAL_ENDPOINT` | स्वत: | सेवा अन्त बिन्दु ओभरराइड गर्नुहोस् |

### प्रयोगका उदाहरणहरू

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## पुरानो ढाँचाबाट माइग्रेशन

यदि तपाईंको मौजुदा कोडले प्रत्यक्ष API कलहरू प्रयोग गरिरहेको छ भने, यसरी माइग्रेट गर्नुहोस्:

### पहिले (प्रत्यक्ष API)
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

### पछि (SDK)
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

### माइग्रेशनका फाइदाहरू
- ✅ स्वचालित सेवा व्यवस्थापन
- ✅ मोडेल उपनाम समाधान
- ✅ हार्डवेयर अप्टिमाइजेशन चयन
- ✅ राम्रो त्रुटि ह्यान्डलिंग
- ✅ OpenAI SDK अनुकूलता
- ✅ स्ट्रिमिङ समर्थन

## सन्दर्भहरू

### आधिकारिक दस्तावेजीकरण
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK स्रोत**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI सन्दर्भ**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **समस्या समाधान**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop स्रोतहरू
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **नमूना नोटबुक**: `Workshop/notebooks/session06_models_router.ipynb`

### समुदाय
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## आगामी चरणहरू

1. **परिवर्तनहरूको समीक्षा गर्नुहोस्**: अद्यावधिक फाइलहरू पढ्नुहोस्
2. **नोटबुक परीक्षण गर्नुहोस्**: session06_models_router.ipynb चलाउनुहोस्
3. **SDK पुष्टि गर्नुहोस्**: सुनिश्चित गर्नुहोस् कि foundry-local-sdk स्थापना गरिएको छ
4. **सेवा जाँच गर्नुहोस्**: Foundry Local चलिरहेको छ भनी पुष्टि गर्नुहोस्
5. **दस्तावेज अन्वेषण गर्नुहोस्**: नयाँ session06_README.md पढ्नुहोस्

## सारांश

यी अद्यावधिकहरूले सुनिश्चित गर्छ कि Workshop सामग्रीहरू **Foundry Local SDK ढाँचाहरू** ठ्याक्कै GitHub रिपोजिटरीमा दस्तावेज गरिएको रूपमा अनुसरण गर्छ। सबै कोड उदाहरणहरू, दस्तावेजीकरण, र युटिलिटीहरू अब माइक्रोसफ्टको स्थानीय AI मोडेल परिनियोजनका लागि सिफारिस गरिएका उत्तम अभ्यासहरूसँग मेल खान्छ।

परिवर्तनहरूले सुधार गर्छ:
- ✅ **सहीता**: आधिकारिक SDK ढाँचाहरू प्रयोग गर्छ
- ✅ **दस्तावेजीकरण**: व्यापक व्याख्या र उदाहरणहरू
- ✅ **त्रुटि ह्यान्डलिंग**: राम्रो सन्देशहरू र समस्या समाधान मार्गदर्शन
- ✅ **रखरखाव**: आधिकारिक परम्पराहरू अनुसरण गर्छ
- ✅ **प्रयोगकर्ता अनुभव**: स्पष्ट निर्देशनहरू र डिबगिङ सहयोग

---

**अद्यावधिक गरिएको:** अक्टोबर 8, 2025  
**SDK संस्करण:** foundry-local-sdk (नवीनतम)  
**Workshop शाखा:** Reactor

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।