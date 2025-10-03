<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:27:52+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hi"
}
-->
# AGENTS.md

## परियोजना का अवलोकन

EdgeAI for Beginners एक व्यापक शैक्षिक रिपॉजिटरी है जो छोटे भाषा मॉडल (SLMs) के साथ Edge AI विकास सिखाती है। यह कोर्स EdgeAI की मूल बातें, मॉडल डिप्लॉयमेंट, ऑप्टिमाइज़ेशन तकनीकें, और Microsoft Foundry Local और विभिन्न AI फ्रेमवर्क्स का उपयोग करके प्रोडक्शन-रेडी इम्प्लीमेंटेशन को कवर करता है।

**मुख्य तकनीकें:**
- Python 3.8+ (AI/ML नमूनों के लिए प्राथमिक भाषा)
- .NET C# (AI/ML नमूने)
- JavaScript/Node.js और Electron (डेस्कटॉप एप्लिकेशन के लिए)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI फ्रेमवर्क्स: LangChain, Semantic Kernel, Chainlit
- मॉडल ऑप्टिमाइज़ेशन: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**रिपॉजिटरी प्रकार:** 8 मॉड्यूल और 10 व्यापक नमूना एप्लिकेशन के साथ शैक्षिक सामग्री रिपॉजिटरी

**आर्किटेक्चर:** मल्टी-मॉड्यूल लर्निंग पाथ जिसमें Edge AI डिप्लॉयमेंट पैटर्न को प्रदर्शित करने वाले व्यावहारिक नमूने शामिल हैं

## रिपॉजिटरी संरचना

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## सेटअप कमांड्स

### रिपॉजिटरी सेटअप

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python नमूना सेटअप (Module08 और Python नमूने)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Node.js नमूना सेटअप (नमूना 08 - Windows चैट ऐप)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local सेटअप

Module08 नमूनों को चलाने के लिए Foundry Local आवश्यक है:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## विकास वर्कफ़्लो

### सामग्री विकास

यह रिपॉजिटरी मुख्य रूप से **Markdown शैक्षिक सामग्री** शामिल करती है। जब बदलाव करें:

1. उपयुक्त मॉड्यूल डायरेक्टरी में `.md` फाइलें संपादित करें
2. मौजूदा फॉर्मेटिंग पैटर्न का पालन करें
3. सुनिश्चित करें कि कोड उदाहरण सटीक और परीक्षण किए गए हैं
4. यदि आवश्यक हो तो संबंधित अनुवादित सामग्री को अपडेट करें (या स्वचालन को इसे संभालने दें)

### नमूना एप्लिकेशन विकास

Python नमूनों के लिए (नमूने 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron नमूने के लिए (नमूना 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### नमूना एप्लिकेशन का परीक्षण

Python नमूनों में स्वचालित परीक्षण नहीं हैं लेकिन इन्हें चलाकर सत्यापित किया जा सकता है:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron नमूने में परीक्षण इंफ्रास्ट्रक्चर है:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## परीक्षण निर्देश

### सामग्री सत्यापन

रिपॉजिटरी स्वचालित अनुवाद वर्कफ़्लो का उपयोग करती है। अनुवादों के लिए कोई मैनुअल परीक्षण आवश्यक नहीं है।

**सामग्री परिवर्तनों के लिए मैनुअल सत्यापन:**
1. `.md` फाइलों को प्रीव्यू करके Markdown रेंडरिंग की समीक्षा करें
2. सुनिश्चित करें कि सभी लिंक वैध लक्ष्यों की ओर इशारा करते हैं
3. दस्तावेज़ में शामिल कोड स्निपेट्स का परीक्षण करें
4. जांचें कि छवियां सही तरीके से लोड हो रही हैं

### नमूना एप्लिकेशन परीक्षण

**Module08/samples/08 (Electron ऐप) में व्यापक परीक्षण है:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python नमूनों को मैनुअल रूप से परीक्षण किया जाना चाहिए:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## कोड शैली दिशानिर्देश

### Markdown सामग्री

- सुसंगत शीर्षक पदानुक्रम का उपयोग करें (# शीर्षक के लिए, ## मुख्य अनुभागों के लिए, ### उप-अनुभागों के लिए)
- भाषा निर्दिष्ट करने वाले कोड ब्लॉक शामिल करें: ```python, ```bash, ```javascript
- तालिकाओं, सूचियों, और जोर देने के लिए मौजूदा फॉर्मेटिंग का पालन करें
- पंक्तियों को पठनीय रखें (लगभग ~80-100 वर्णों का लक्ष्य रखें, लेकिन सख्त नहीं)
- आंतरिक संदर्भों के लिए सापेक्ष लिंक का उपयोग करें

### Python कोड शैली

- PEP 8 कन्वेंशन का पालन करें
- जहां उपयुक्त हो, टाइप हिंट्स का उपयोग करें
- फ़ंक्शन्स और क्लासेस के लिए डॉकस्ट्रिंग्स शामिल करें
- सार्थक वेरिएबल नामों का उपयोग करें
- फ़ंक्शन्स को केंद्रित और संक्षिप्त रखें

### JavaScript/Node.js कोड शैली

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**मुख्य कन्वेंशन:**
- नमूना 08 में प्रदान की गई ESLint कॉन्फ़िगरेशन
- कोड फॉर्मेटिंग के लिए Prettier का उपयोग करें
- आधुनिक ES6+ सिंटैक्स का उपयोग करें
- कोडबेस में मौजूदा पैटर्न का पालन करें

## पुल अनुरोध दिशानिर्देश

### शीर्षक प्रारूप
```
[ModuleXX] Brief description of change
```
या
```
[Module08/samples/XX] Description for sample changes
```

### सबमिट करने से पहले

**सामग्री परिवर्तनों के लिए:**
- सभी संशोधित Markdown फाइलों का प्रीव्यू करें
- सुनिश्चित करें कि लिंक और छवियां काम कर रही हैं
- टाइपो और व्याकरण संबंधी त्रुटियों की जांच करें

**नमूना कोड परिवर्तनों के लिए (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python नमूना परिवर्तनों के लिए:**
- सुनिश्चित करें कि नमूना सफलतापूर्वक चलता है
- त्रुटि हैंडलिंग की जांच करें
- Foundry Local के साथ संगतता की जांच करें

### समीक्षा प्रक्रिया

- शैक्षिक सामग्री परिवर्तनों की सटीकता और स्पष्टता के लिए समीक्षा की जाती है
- कोड नमूनों की कार्यक्षमता के लिए परीक्षण किया जाता है
- अनुवाद अपडेट स्वचालित रूप से GitHub Actions द्वारा संभाले जाते हैं

## अनुवाद प्रणाली

**महत्वपूर्ण:** यह रिपॉजिटरी GitHub Actions के माध्यम से स्वचालित अनुवाद का उपयोग करती है।

- अनुवाद `/translations/` डायरेक्टरी में हैं (50+ भाषाएं)
- `co-op-translator.yml` वर्कफ़्लो के माध्यम से स्वचालित
- **अनुवाद फाइलों को मैनुअल रूप से संपादित न करें** - वे अधिलेखित हो जाएंगी
- केवल रूट और मॉड्यूल डायरेक्टरी में अंग्रेजी स्रोत फाइलों को संपादित करें
- `main` ब्रांच पर पुश करने पर अनुवाद स्वचालित रूप से उत्पन्न होते हैं

## Foundry Local इंटीग्रेशन

अधिकांश Module08 नमूनों को Microsoft Foundry Local चलाने की आवश्यकता होती है:

### Foundry Local शुरू करना
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Foundry Local सत्यापन
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### नमूनों के लिए पर्यावरण वेरिएबल्स

अधिकांश नमूने इन पर्यावरण वेरिएबल्स का उपयोग करते हैं:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## निर्माण और डिप्लॉयमेंट

### सामग्री डिप्लॉयमेंट

यह रिपॉजिटरी मुख्य रूप से दस्तावेज़ीकरण है - सामग्री के लिए कोई निर्माण प्रक्रिया आवश्यक नहीं है।

### नमूना एप्लिकेशन निर्माण

**Electron एप्लिकेशन (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python नमूने:**
कोई निर्माण प्रक्रिया नहीं - नमूने सीधे Python इंटरप्रेटर के साथ चलाए जाते हैं।

## सामान्य समस्याएं और समाधान

### Foundry Local नहीं चल रहा
**समस्या:** नमूने कनेक्शन त्रुटियों के साथ विफल हो जाते हैं

**समाधान:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python वर्चुअल एनवायरनमेंट समस्याएं
**समस्या:** मॉड्यूल आयात त्रुटियां

**समाधान:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron निर्माण समस्याएं
**समस्या:** npm इंस्टॉल या निर्माण विफलताएं

**समाधान:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### अनुवाद वर्कफ़्लो संघर्ष
**समस्या:** अनुवाद PR आपके परिवर्तनों के साथ संघर्ष करता है

**समाधान:**
- केवल अंग्रेजी स्रोत फाइलों को संपादित करें
- स्वचालित अनुवाद वर्कफ़्लो को अनुवाद संभालने दें
- यदि संघर्ष होता है, तो अनुवादों के विलय के बाद `main` को अपनी ब्रांच में मर्ज करें

## अतिरिक्त संसाधन

### लर्निंग पाथ्स
- **शुरुआती पथ:** मॉड्यूल 01-02 (7-9 घंटे)
- **मध्यम पथ:** मॉड्यूल 03-04 (9-11 घंटे)
- **उन्नत पथ:** मॉड्यूल 05-07 (12-15 घंटे)
- **विशेषज्ञ पथ:** मॉड्यूल 08 (8-10 घंटे)

### प्रमुख मॉड्यूल सामग्री
- **Module01:** EdgeAI की मूल बातें और वास्तविक दुनिया के केस स्टडीज
- **Module02:** छोटे भाषा मॉडल (SLM) परिवार और आर्किटेक्चर
- **Module03:** स्थानीय और क्लाउड डिप्लॉयमेंट रणनीतियां
- **Module04:** कई फ्रेमवर्क्स के साथ मॉडल ऑप्टिमाइज़ेशन
- **Module05:** SLMOps - प्रोडक्शन ऑपरेशन्स
- **Module06:** AI एजेंट्स और फंक्शन कॉलिंग
- **Module07:** प्लेटफ़ॉर्म-विशिष्ट इम्प्लीमेंटेशन
- **Module08:** Foundry Local टूलकिट के साथ 10 व्यापक नमूने

### बाहरी निर्भरताएं
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - स्थानीय AI मॉडल रनटाइम
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - ऑप्टिमाइज़ेशन फ्रेमवर्क
- [Microsoft Olive](https://microsoft.github.io/Olive/) - मॉडल ऑप्टिमाइज़ेशन टूलकिट
- [OpenVINO](https://docs.openvino.ai/) - Intel का ऑप्टिमाइज़ेशन टूलकिट

## परियोजना-विशिष्ट नोट्स

### Module08 नमूना एप्लिकेशन

रिपॉजिटरी में 10 व्यापक नमूना एप्लिकेशन शामिल हैं:

1. **01-REST चैट क्विकस्टार्ट** - बेसिक OpenAI SDK इंटीग्रेशन
2. **02-OpenAI SDK इंटीग्रेशन** - उन्नत SDK फीचर्स
3. **03-मॉडल डिस्कवरी और बेंचमार्किंग** - मॉडल तुलना उपकरण
4. **04-Chainlit RAG एप्लिकेशन** - रिट्रीवल-ऑगमेंटेड जनरेशन
5. **05-मल्टी-एजेंट ऑर्केस्ट्रेशन** - बेसिक एजेंट समन्वय
6. **06-मॉडल्स-एज़-टूल्स राउटर** - इंटेलिजेंट मॉडल रूटिंग
7. **07-डायरेक्ट API क्लाइंट** - लो-लेवल API इंटीग्रेशन
8. **08-Windows 11 चैट ऐप** - नेटिव Electron डेस्कटॉप एप्लिकेशन
9. **09-उन्नत मल्टी-एजेंट सिस्टम** - जटिल एजेंट समन्वय
10. **10-Foundry टूल्स फ्रेमवर्क** - LangChain/Semantic Kernel इंटीग्रेशन

प्रत्येक नमूना Foundry Local के साथ Edge AI विकास के विभिन्न पहलुओं को प्रदर्शित करता है।

### प्रदर्शन विचार

- SLMs को Edge डिप्लॉयमेंट के लिए ऑप्टिमाइज़ किया गया है (2-16GB RAM)
- स्थानीय इनफेरेंस 50-500ms प्रतिक्रिया समय प्रदान करता है
- क्वांटाइज़ेशन तकनीकें 75% आकार में कमी और 85% प्रदर्शन प्रतिधारण प्राप्त करती हैं
- स्थानीय मॉडलों के साथ रीयल-टाइम बातचीत की क्षमताएं

### सुरक्षा और गोपनीयता

- सभी प्रोसेसिंग स्थानीय रूप से होती है - कोई डेटा क्लाउड में नहीं भेजा जाता
- गोपनीयता-संवेदनशील एप्लिकेशन (स्वास्थ्य सेवा, वित्त) के लिए उपयुक्त
- डेटा संप्रभुता आवश्यकताओं को पूरा करता है
- Foundry Local पूरी तरह से स्थानीय हार्डवेयर पर चलता है

---

**यह एक शैक्षिक रिपॉजिटरी है जो Edge AI विकास सिखाने पर केंद्रित है। प्राथमिक योगदान पैटर्न शैक्षिक सामग्री को बेहतर बनाना और Edge AI अवधारणाओं को प्रदर्शित करने वाले नमूना एप्लिकेशन जोड़ना/सुधारना है।**

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।