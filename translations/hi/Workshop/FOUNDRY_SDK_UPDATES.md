<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T21:37:41+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "hi"
}
-->
# Foundry Local SDK अपडेट्स

## अवलोकन

**आधिकारिक Foundry Local Python SDK** का उपयोग करने के लिए Workshop नोटबुक्स और यूटिलिटीज को अपडेट किया गया है, निम्नलिखित पैटर्न्स के अनुसार:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## संशोधित फाइलें

### 1. `Workshop/samples/workshop_utils.py`

**परिवर्तन:**
- ✅ `foundry-local-sdk` पैकेज के लिए इम्पोर्ट एरर हैंडलिंग जोड़ा गया
- ✅ आधिकारिक SDK पैटर्न्स के साथ डॉक्यूमेंटेशन को बेहतर बनाया गया
- ✅ Unicode प्रतीकों (✓, ✗, ⚠) के साथ लॉगिंग में सुधार किया गया
- ✅ उदाहरणों के साथ व्यापक डॉकस्ट्रिंग्स जोड़ी गईं
- ✅ CLI कमांड्स का संदर्भ देते हुए बेहतर एरर संदेश जोड़े गए
- ✅ आधिकारिक SDK डॉक्यूमेंटेशन से मेल खाते हुए टिप्पणियों को अपडेट किया गया

**मुख्य सुधार:**

#### इम्पोर्ट एरर हैंडलिंग
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### बेहतर `get_client()` फ़ंक्शन
- SDK इनिशियलाइज़ेशन पैटर्न के बारे में विस्तृत डॉक्यूमेंटेशन जोड़ा गया
- स्पष्ट किया गया कि `FoundryLocalManager` सेवा को स्वचालित रूप से शुरू करता है
- हार्डवेयर-ऑप्टिमाइज़्ड वेरिएंट्स के लिए मॉडल एलियास रेज़ोल्यूशन समझाया गया
- एंडपॉइंट जानकारी के साथ लॉगिंग में सुधार किया गया
- समस्या निवारण चरणों का सुझाव देते हुए बेहतर एरर संदेश जोड़े गए

#### बेहतर `chat_once()` फ़ंक्शन
- उपयोग के उदाहरणों के साथ व्यापक डॉकस्ट्रिंग जोड़ी गई
- OpenAI SDK संगतता स्पष्ट की गई
- स्ट्रीमिंग सपोर्ट (kwargs के माध्यम से) डॉक्यूमेंट किया गया
- CLI कमांड सुझावों के साथ बेहतर एरर संदेश जोड़े गए
- मॉडल उपलब्धता जांचने के नोट्स जोड़े गए

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**परिवर्तन:**
- ✅ सभी मार्कडाउन सेल्स को SDK संदर्भों के साथ अपडेट किया गया
- ✅ SDK पैटर्न व्याख्याओं के साथ कोड टिप्पणियों को बेहतर बनाया गया
- ✅ सेल डॉक्यूमेंटेशन और व्याख्याओं में सुधार किया गया
- ✅ समस्या निवारण मार्गदर्शन जोड़ा गया
- ✅ मॉडल कैटलॉग अपडेट किया गया (गैर-मानक 'gpt-oss-20b' को 'phi-3.5-mini' से बदल दिया गया)
- ✅ विज़ुअल इंडिकेटर्स के साथ आउटपुट फॉर्मेटिंग में सुधार किया गया
- ✅ पूरे नोटबुक में SDK लिंक और संदर्भ जोड़े गए

**सेल-बाय-सेल अपडेट्स:**

#### सेल 1 (शीर्षक)
- SDK डॉक्यूमेंटेशन लिंक जोड़े गए
- आधिकारिक GitHub रिपॉजिटरीज़ का संदर्भ दिया गया

#### सेल 2 (परिदृश्य)
- क्रमांकित चरणों के साथ पुनः स्वरूपित किया गया
- इरादा-आधारित रूटिंग पैटर्न स्पष्ट किया गया
- स्थानीय निष्पादन लाभों पर जोर दिया गया

#### सेल 3 (डिपेंडेंसी इंस्टॉलेशन)
- प्रत्येक पैकेज क्या प्रदान करता है, इसका स्पष्टीकरण जोड़ा गया
- SDK क्षमताओं (एलियास रेज़ोल्यूशन, हार्डवेयर ऑप्टिमाइज़ेशन) को डॉक्यूमेंट किया गया

#### सेल 4 (पर्यावरण सेटअप)
- फ़ंक्शन डॉकस्ट्रिंग्स में सुधार किया गया
- SDK पैटर्न्स को समझाने वाली इनलाइन टिप्पणियां जोड़ी गईं
- मॉडल कैटलॉग संरचना डॉक्यूमेंट की गई
- प्राथमिकता/क्षमता मिलान स्पष्ट किया गया

#### सेल 5 (कैटलॉग जांच)
- विज़ुअल चेकमार्क्स (✓) जोड़े गए
- बेहतर फॉर्मेटेड आउटपुट

#### सेल 6 (इरादा पहचान परीक्षण)
- आउटपुट को टेबल-स्टाइल में पुनः स्वरूपित किया गया
- इरादा और चयनित मॉडल दोनों दिखाए गए

#### सेल 7 (रूटिंग फ़ंक्शन)
- व्यापक SDK पैटर्न व्याख्या
- इनिशियलाइज़ेशन फ्लो डॉक्यूमेंट किया गया
- सभी फीचर्स (रीट्राई, ट्रैकिंग, एरर) सूचीबद्ध किए गए
- SDK संदर्भ लिंक जोड़ा गया

#### सेल 8 (बैच डेमो)
- अपेक्षित परिणामों की व्याख्या में सुधार किया गया
- समस्या निवारण अनुभाग जोड़ा गया
- डीबगिंग के लिए CLI कमांड्स शामिल किए गए
- बेहतर फॉर्मेटेड आउटपुट डिस्प्ले

### 3. `Workshop/notebooks/session06_README.md` (नई फाइल)

**व्यापक डॉक्यूमेंटेशन बनाया गया जिसमें शामिल हैं:**

1. **अवलोकन**: आर्किटेक्चर डायग्राम और घटक व्याख्या
2. **SDK इंटीग्रेशन**: आधिकारिक पैटर्न्स का पालन करते हुए कोड उदाहरण
3. **पूर्वापेक्षाएँ**: चरण-दर-चरण सेटअप निर्देश
4. **उपयोग**: नोटबुक को चलाने और अनुकूलित करने का तरीका
5. **मॉडल एलियास**: हार्डवेयर-ऑप्टिमाइज़्ड वेरिएंट्स की व्याख्या
6. **समस्या निवारण**: सामान्य समस्याएं और समाधान
7. **विस्तार**: इरादे, मॉडल और कस्टम लॉजिक कैसे जोड़ें
8. **प्रदर्शन सुझाव**: उत्पादन उपयोग के लिए सर्वोत्तम प्रथाएं
9. **संसाधन**: आधिकारिक डॉक्यूमेंटेशन और समुदाय के लिंक

## SDK पैटर्न कार्यान्वयन

### आधिकारिक पैटर्न (Foundry Local डॉक्यूमेंट्स से)

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

### हमारा कार्यान्वयन (workshop_utils में)

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

**हमारे दृष्टिकोण के लाभ:**
- ✅ आधिकारिक SDK पैटर्न का सटीक पालन करता है
- ✅ बार-बार इनिशियलाइज़ेशन से बचने के लिए कैशिंग जोड़ता है
- ✅ उत्पादन मजबूती के लिए रीट्राई लॉजिक शामिल करता है
- ✅ टोकन उपयोग ट्रैकिंग का समर्थन करता है
- ✅ बेहतर एरर संदेश प्रदान करता है
- ✅ आधिकारिक उदाहरणों के साथ संगत रहता है

## मॉडल कैटलॉग परिवर्तन

### पहले
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### बाद में
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**कारण:** 'gpt-oss-20b' (गैर-मानक एलियास) को 'phi-3.5-mini' (आधिकारिक Foundry Local एलियास) से बदल दिया गया।

## डिपेंडेंसीज़

### अपडेटेड requirements.txt

Workshop requirements.txt पहले से ही शामिल करता है:
```
foundry-local-sdk
openai>=1.30.0
```

Foundry Local इंटीग्रेशन के लिए केवल यही पैकेज आवश्यक हैं।

## अपडेट्स का परीक्षण

### 1. सुनिश्चित करें कि Foundry Local चल रहा है

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. उपलब्ध मॉडल्स की जांच करें

```bash
foundry model ls
```

सुनिश्चित करें कि ये मॉडल उपलब्ध हैं या स्वचालित रूप से डाउनलोड हो जाएंगे:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. नोटबुक चलाएं

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

या VS Code में खोलें और सभी सेल्स चलाएं।

### 4. अपेक्षित व्यवहार

**सेल 1 (इंस्टॉल):** पैकेज सफलतापूर्वक इंस्टॉल करता है  
**सेल 2 (सेटअप):** कोई एरर नहीं, इम्पोर्ट्स काम करते हैं  
**सेल 3 (जांच):** मॉडल सूची के साथ ✓ दिखाता है  
**सेल 4 (इरादा परीक्षण):** इरादा पहचान परिणाम दिखाता है  
**सेल 5 (राउटर):** ✓ रूट फ़ंक्शन तैयार दिखाता है  
**सेल 6 (निष्पादन):** प्रॉम्प्ट्स को मॉडल्स पर रूट करता है, परिणाम दिखाता है  

### 5. कनेक्शन एरर समस्या निवारण

यदि आपको `APIConnectionError: Connection error` दिखाई देता है:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## पर्यावरण वेरिएबल्स

निम्नलिखित पर्यावरण वेरिएबल्स समर्थित हैं:

| वेरिएबल | डिफ़ॉल्ट | विवरण |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | टोकन उपयोग प्रिंट करने के लिए `1` पर सेट करें |
| `RETRY_ON_FAIL` | `1` | रीट्राई लॉजिक सक्षम करें |
| `RETRY_BACKOFF` | `1.0` | प्रारंभिक रीट्राई देरी (सेकंड) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | सेवा एंडपॉइंट ओवरराइड करें |

### उपयोग के उदाहरण

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## पुराने पैटर्न से माइग्रेशन

यदि आपके पास मौजूदा कोड है जो सीधे API कॉल्स का उपयोग करता है, तो इसे माइग्रेट करने का तरीका यहां है:

### पहले (डायरेक्ट API)
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

### बाद में (SDK)
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

### माइग्रेशन के लाभ
- ✅ स्वचालित सेवा प्रबंधन
- ✅ मॉडल एलियास रेज़ोल्यूशन
- ✅ हार्डवेयर ऑप्टिमाइज़ेशन चयन
- ✅ बेहतर एरर हैंडलिंग
- ✅ OpenAI SDK संगतता
- ✅ स्ट्रीमिंग सपोर्ट

## संदर्भ

### आधिकारिक डॉक्यूमेंटेशन
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK स्रोत**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI संदर्भ**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **समस्या निवारण**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop संसाधन
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **नमूना नोटबुक**: `Workshop/notebooks/session06_models_router.ipynb`

### समुदाय
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## अगले कदम

1. **परिवर्तनों की समीक्षा करें**: अपडेटेड फाइल्स को पढ़ें  
2. **नोटबुक का परीक्षण करें**: session06_models_router.ipynb चलाएं  
3. **SDK सत्यापित करें**: सुनिश्चित करें कि foundry-local-sdk इंस्टॉल है  
4. **सेवा जांचें**: पुष्टि करें कि Foundry Local चल रहा है  
5. **डॉक्यूमेंट्स एक्सप्लोर करें**: नया session06_README.md पढ़ें  

## सारांश

ये अपडेट्स सुनिश्चित करते हैं कि Workshop सामग्री **आधिकारिक Foundry Local SDK पैटर्न्स** का पालन करती है, जैसा कि GitHub रिपॉजिटरी में डॉक्यूमेंट किया गया है। सभी कोड उदाहरण, डॉक्यूमेंटेशन, और यूटिलिटीज अब Microsoft के अनुशंसित सर्वोत्तम प्रथाओं के साथ संरेखित हैं।

परिवर्तनों में सुधार किया गया है:
- ✅ **सटीकता**: आधिकारिक SDK पैटर्न्स का उपयोग करता है  
- ✅ **डॉक्यूमेंटेशन**: व्यापक व्याख्याएं और उदाहरण  
- ✅ **एरर हैंडलिंग**: बेहतर संदेश और समस्या निवारण मार्गदर्शन  
- ✅ **रखरखाव**: आधिकारिक कन्वेंशन्स का पालन करता है  
- ✅ **उपयोगकर्ता अनुभव**: स्पष्ट निर्देश और डीबगिंग सहायता  

---

**अपडेटेड:** 8 अक्टूबर, 2025  
**SDK संस्करण:** foundry-local-sdk (नवीनतम)  
**Workshop शाखा:** Reactor  

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।