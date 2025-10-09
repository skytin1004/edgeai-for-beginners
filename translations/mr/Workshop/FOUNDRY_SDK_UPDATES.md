<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T09:17:25+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "mr"
}
-->
# Foundry Local SDK अद्यतन

## आढावा

**Foundry Local Python SDK** च्या अधिकृत पद्धतींचा वापर करून Workshop नोटबुक्स आणि युटिलिटीज अद्यतनित केल्या आहेत. संदर्भ:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## बदललेली फाइल्स

### 1. `Workshop/samples/workshop_utils.py`

**बदल:**
- ✅ `foundry-local-sdk` पॅकेजसाठी आयात त्रुटी हाताळणी जोडली
- ✅ अधिकृत SDK पद्धतींसह दस्तऐवजीकरण सुधारित केले
- ✅ Unicode चिन्हांसह लॉगिंग सुधारित केले (✓, ✗, ⚠)
- ✅ उदाहरणांसह व्यापक docstrings जोडले
- ✅ CLI कमांड्स संदर्भित करणारे चांगले त्रुटी संदेश जोडले
- ✅ अधिकृत SDK दस्तऐवजीकरणाशी जुळणारे टिप्पण्या अद्यतनित केल्या

**मुख्य सुधारणा:**

#### आयात त्रुटी हाताळणी
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### सुधारित `get_client()` फंक्शन
- SDK प्रारंभ पद्धतीबद्दल तपशीलवार दस्तऐवजीकरण जोडले
- स्पष्ट केले की `FoundryLocalManager` सेवा आपोआप सुरू करते
- हार्डवेअर-ऑप्टिमाइझ्ड प्रकारांमध्ये मॉडेल उपनाम रिझोल्यूशन स्पष्ट केले
- एंडपॉइंट माहिती असलेल्या लॉगिंगमध्ये सुधारणा केली
- समस्या निवारण चरण सुचवणारे चांगले त्रुटी संदेश जोडले

#### सुधारित `chat_once()` फंक्शन
- वापर उदाहरणांसह व्यापक docstring जोडले
- OpenAI SDK सुसंगतता स्पष्ट केली
- स्ट्रीमिंग समर्थन (kwargs द्वारे) दस्तऐवजीकरण केले
- CLI कमांड्स सुचवणारे सुधारित त्रुटी संदेश जोडले
- मॉडेल उपलब्धता तपासणीबद्दल नोट्स जोडल्या

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**बदल:**
- ✅ SDK संदर्भांसह सर्व markdown सेल्स अद्यतनित केले
- ✅ SDK पद्धतींच्या स्पष्टीकरणांसह कोड टिप्पण्या सुधारित केल्या
- ✅ सेल दस्तऐवजीकरण आणि स्पष्टीकरण सुधारित केले
- ✅ समस्या निवारण मार्गदर्शन जोडले
- ✅ मॉडेल कॅटलॉग अद्यतनित केला ('gpt-oss-20b' ऐवजी 'phi-3.5-mini' जोडले)
- ✅ व्हिज्युअल इंडिकेटर्ससह आउटपुट स्वरूपन सुधारित केले
- ✅ SDK लिंक्स आणि संदर्भ सर्वत्र जोडले

**सेल-बाय-सेल अद्यतन:**

#### सेल 1 (शीर्षक)
- SDK दस्तऐवजीकरण लिंक्स जोडले
- अधिकृत GitHub रिपॉझिटरीज संदर्भित केल्या

#### सेल 2 (परिस्थिती)
- क्रमांकित चरणांसह पुनर्रचना केली
- हेतू-आधारित राउटिंग पद्धती स्पष्ट केली
- स्थानिक अंमलबजावणीचे फायदे अधोरेखित केले

#### सेल 3 (अवलंबित्व स्थापना)
- प्रत्येक पॅकेज काय प्रदान करते याचे स्पष्टीकरण जोडले
- SDK क्षमता दस्तऐवजीकरण केल्या (उपनाम रिझोल्यूशन, हार्डवेअर ऑप्टिमायझेशन)

#### सेल 4 (पर्यावरण सेटअप)
- फंक्शन docstrings सुधारित केल्या
- SDK पद्धती स्पष्ट करणाऱ्या इनलाइन टिप्पण्या जोडल्या
- मॉडेल कॅटलॉग संरचना दस्तऐवजीकरण केली
- प्राधान्य/क्षमता जुळणी स्पष्ट केली

#### सेल 5 (कॅटलॉग तपासणी)
- व्हिज्युअल चेकमार्क्स (✓) जोडले
- आउटपुट चांगल्या प्रकारे स्वरूपित केले

#### सेल 6 (हेतू शोध चाचणी)
- आउटपुट टेबल-शैलीत पुनर्रचना केली
- हेतू आणि निवडलेले मॉडेल दोन्ही दर्शवते

#### सेल 7 (राउटिंग फंक्शन)
- व्यापक SDK पद्धतीचे स्पष्टीकरण
- प्रारंभ प्रवाह दस्तऐवजीकरण केला
- सर्व वैशिष्ट्ये सूचीबद्ध केली (पुनः प्रयत्न, ट्रॅकिंग, त्रुटी)
- SDK संदर्भ लिंक जोडली

#### सेल 8 (बॅच डेमो)
- काय अपेक्षित आहे याचे स्पष्टीकरण सुधारित केले
- समस्या निवारण विभाग जोडला
- डीबगिंगसाठी CLI कमांड्स समाविष्ट केल्या
- आउटपुट प्रदर्शन चांगल्या प्रकारे स्वरूपित केले

### 3. `Workshop/notebooks/session06_README.md` (नवीन फाइल)

**व्यापक दस्तऐवजीकरण तयार केले:**

1. **आढावा**: आर्किटेक्चर डायग्राम आणि घटक स्पष्टीकरण
2. **SDK एकत्रीकरण**: अधिकृत पद्धतींचे कोड उदाहरणे
3. **पूर्वअटी**: चरण-दर-चरण सेटअप सूचना
4. **वापर**: नोटबुक कसे चालवायचे आणि सानुकूलित करायचे
5. **मॉडेल उपनाम**: हार्डवेअर-ऑप्टिमाइझ्ड प्रकारांचे स्पष्टीकरण
6. **समस्या निवारण**: सामान्य समस्या आणि उपाय
7. **विस्तार**: हेतू, मॉडेल्स आणि सानुकूल लॉजिक कसे जोडायचे
8. **कामगिरी टिप्स**: उत्पादन वापरासाठी सर्वोत्तम पद्धती
9. **संसाधने**: अधिकृत दस्तऐवजीकरण आणि समुदाय लिंक्स

## SDK पद्धतीची अंमलबजावणी

### अधिकृत पद्धत (Foundry Local दस्तऐवजीकरणातून)

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

### आमची अंमलबजावणी (workshop_utils मध्ये)

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

**आमच्या दृष्टिकोनाचे फायदे:**
- ✅ अधिकृत SDK पद्धतीचे अचूक पालन करते
- ✅ वारंवार प्रारंभ टाळण्यासाठी कॅशिंग जोडले
- ✅ उत्पादन मजबुतीसाठी पुनः प्रयत्न लॉजिक समाविष्ट करते
- ✅ टोकन वापर ट्रॅकिंगला समर्थन देते
- ✅ चांगले त्रुटी संदेश प्रदान करते
- ✅ अधिकृत उदाहरणांसह सुसंगत राहते

## मॉडेल कॅटलॉग बदल

### पूर्वी
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### नंतर
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**कारण:** 'gpt-oss-20b' (अमानक उपनाम) ऐवजी 'phi-3.5-mini' (अधिकृत Foundry Local उपनाम) जोडले.

## अवलंबित्व

### अद्यतनित requirements.txt

Workshop च्या requirements.txt मध्ये आधीच समाविष्ट आहे:
```
foundry-local-sdk
openai>=1.30.0
```

Foundry Local एकत्रीकरणासाठी आवश्यक असलेल्या फक्त या पॅकेजेस आहेत.

## अद्यतनांची चाचणी

### 1. Foundry Local चालू असल्याचे सत्यापित करा

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. उपलब्ध मॉडेल्स तपासा

```bash
foundry model ls
```

खालील मॉडेल्स उपलब्ध आहेत किंवा स्वयंचलितपणे डाउनलोड होतील याची खात्री करा:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. नोटबुक चालवा

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

किंवा VS Code मध्ये उघडा आणि सर्व सेल्स चालवा.

### 4. अपेक्षित वर्तन

**सेल 1 (स्थापना):** पॅकेजेस यशस्वीरित्या स्थापित करते  
**सेल 2 (सेटअप):** कोणतीही त्रुटी नाही, आयात कार्य करते  
**सेल 3 (तपासा):** मॉडेल सूचीसह ✓ दर्शवते  
**सेल 4 (हेतू चाचणी):** हेतू शोध परिणाम दर्शवते  
**सेल 5 (राउटर):** ✓ राउट फंक्शन तयार दर्शवते  
**सेल 6 (अंमलबजावणी):** मॉडेल्सकडे प्रॉम्प्ट्स राउट करते, परिणाम दर्शवते  

### 5. कनेक्शन त्रुटी समस्या निवारण

जर तुम्हाला `APIConnectionError: Connection error` दिसत असेल:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## पर्यावरणीय व्हेरिएबल्स

खालील पर्यावरणीय व्हेरिएबल्स समर्थित आहेत:

| व्हेरिएबल | डीफॉल्ट | वर्णन |
|-----------|---------|-------|
| `SHOW_USAGE` | `0` | टोकन वापर प्रिंट करण्यासाठी `1` सेट करा |
| `RETRY_ON_FAIL` | `1` | पुनः प्रयत्न लॉजिक सक्षम करा |
| `RETRY_BACKOFF` | `1.0` | प्रारंभिक पुनः प्रयत्न विलंब (सेकंद) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | सेवा एंडपॉइंट ओव्हरराइड करा |

### वापर उदाहरणे

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## जुन्या पद्धतीतून स्थलांतर

जर तुमच्याकडे थेट API कॉल्स वापरणारा विद्यमान कोड असेल, तर येथे स्थलांतर कसे करायचे:

### पूर्वी (थेट API)
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

### नंतर (SDK)
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

### स्थलांतराचे फायदे
- ✅ स्वयंचलित सेवा व्यवस्थापन
- ✅ मॉडेल उपनाम रिझोल्यूशन
- ✅ हार्डवेअर ऑप्टिमायझेशन निवड
- ✅ चांगली त्रुटी हाताळणी
- ✅ OpenAI SDK सुसंगतता
- ✅ स्ट्रीमिंग समर्थन

## संदर्भ

### अधिकृत दस्तऐवजीकरण
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK स्रोत**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI संदर्भ**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **समस्या निवारण**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop संसाधने
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **नमुना नोटबुक**: `Workshop/notebooks/session06_models_router.ipynb`

### समुदाय
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## पुढील पावले

1. **बदल पुनरावलोकन करा**: अद्यतनित फाइल्स वाचा  
2. **नोटबुक चाचणी करा**: session06_models_router.ipynb चालवा  
3. **SDK सत्यापित करा**: सुनिश्चित करा की foundry-local-sdk स्थापित आहे  
4. **सेवा तपासा**: Foundry Local चालू असल्याचे पुष्टी करा  
5. **दस्तऐवजीकरण एक्सप्लोर करा**: नवीन session06_README.md वाचा  

## सारांश

हे अद्यतन Workshop सामग्री **अधिकृत Foundry Local SDK पद्धतीं**शी अचूकपणे जुळवून घेतात, जसे GitHub रिपॉझिटरीमध्ये दस्तऐवजीकरण केले आहे. सर्व कोड उदाहरणे, दस्तऐवजीकरण आणि युटिलिटीज आता स्थानिक AI मॉडेल तैनातीसाठी Microsoft च्या शिफारस केलेल्या सर्वोत्तम पद्धतींशी संरेखित आहेत.

बदल सुधारित करतात:
- ✅ **योग्यता**: अधिकृत SDK पद्धतींचा वापर करते  
- ✅ **दस्तऐवजीकरण**: व्यापक स्पष्टीकरणे आणि उदाहरणे  
- ✅ **त्रुटी हाताळणी**: चांगले संदेश आणि समस्या निवारण मार्गदर्शन  
- ✅ **देखभालक्षमता**: अधिकृत परंपरा अनुसरण करते  
- ✅ **वापरकर्ता अनुभव**: स्पष्ट सूचना आणि डीबगिंग मदत  

---

**अद्यतनित:** 8 ऑक्टोबर, 2025  
**SDK आवृत्ती:** foundry-local-sdk (नवीनतम)  
**Workshop शाखा:** Reactor  

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.