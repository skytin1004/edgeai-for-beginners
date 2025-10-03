<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:29:00+00:00",
  "source_file": "AGENTS.md",
  "language_code": "mr"
}
-->
# AGENTS.md

## प्रकल्पाचा आढावा

EdgeAI for Beginners हा Edge AI विकास Small Language Models (SLMs) सह शिकवणारा एक व्यापक शैक्षणिक संग्रह आहे. हा कोर्स EdgeAI मूलभूत गोष्टी, मॉडेल तैनाती, ऑप्टिमायझेशन तंत्र आणि Microsoft Foundry Local आणि विविध AI फ्रेमवर्क्स वापरून उत्पादन-तयार अंमलबजावणी कव्हर करतो.

**मुख्य तंत्रज्ञान:**
- Python 3.8+ (AI/ML नमुन्यांसाठी प्राथमिक भाषा)
- .NET C# (AI/ML नमुने)
- JavaScript/Node.js सह Electron (डेस्कटॉप अनुप्रयोगांसाठी)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI फ्रेमवर्क्स: LangChain, Semantic Kernel, Chainlit
- मॉडेल ऑप्टिमायझेशन: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**संग्रह प्रकार:** 8 मॉड्यूल्स आणि 10 व्यापक नमुना अनुप्रयोगांसह शैक्षणिक सामग्री संग्रह

**आर्किटेक्चर:** Edge AI तैनाती नमुन्यांचे प्रदर्शन करणारे व्यावहारिक नमुने असलेल्या बहु-मॉड्यूल शिक्षण मार्ग

## संग्रह रचना

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

### संग्रह सेटअप

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python नमुना सेटअप (Module08 आणि Python नमुने)

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

### Node.js नमुना सेटअप (नमुना 08 - Windows Chat App)

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

Module08 नमुने चालवण्यासाठी Foundry Local आवश्यक आहे:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## विकास कार्यप्रवाह

### सामग्री विकास

या संग्रहात प्रामुख्याने **Markdown शैक्षणिक सामग्री** आहे. बदल करताना:

1. योग्य मॉड्यूल निर्देशिकांमध्ये `.md` फाइल्स संपादित करा
2. विद्यमान स्वरूपन नमुन्यांचे अनुसरण करा
3. कोड उदाहरणे अचूक आणि चाचणी केलेली असल्याची खात्री करा
4. आवश्यक असल्यास संबंधित अनुवादित सामग्री अद्यतनित करा (किंवा ऑटोमेशनला ते हाताळू द्या)

### नमुना अनुप्रयोग विकास

Python नमुन्यांसाठी (नमुने 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron नमुन्यासाठी (नमुना 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### नमुना अनुप्रयोगांची चाचणी

Python नमुन्यांमध्ये स्वयंचलित चाचण्या नाहीत परंतु त्यांना चालवून सत्यापित करता येते:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron नमुन्याला चाचणी पायाभूत सुविधा आहे:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## चाचणी सूचना

### सामग्री सत्यापन

संग्रह स्वयंचलित अनुवाद कार्यप्रवाह वापरतो. अनुवादांसाठी कोणतीही मॅन्युअल चाचणी आवश्यक नाही.

**सामग्री बदलांसाठी मॅन्युअल सत्यापन:**
1. `.md` फाइल्स प्रीव्ह्यू करून Markdown रेंडरिंग पुनरावलोकन करा
2. सर्व दुवे वैध लक्ष्यांकडे निर्देशित करतात याची खात्री करा
3. दस्तऐवजीकरणात समाविष्ट केलेल्या कोड स्निपेट्सची चाचणी करा
4. प्रतिमा योग्य प्रकारे लोड होतात याची खात्री करा

### नमुना अनुप्रयोग चाचणी

**Module08/samples/08 (Electron app) मध्ये व्यापक चाचणी आहे:**
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

**Python नमुने मॅन्युअली चाचणी करणे आवश्यक आहे:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## कोड शैली मार्गदर्शक तत्त्वे

### Markdown सामग्री

- सुसंगत शीर्षक श्रेणीक्रम वापरा (# शीर्षकासाठी, ## मुख्य विभागांसाठी, ### उपविभागांसाठी)
- भाषा निर्दिष्ट करणाऱ्या कोड ब्लॉक्स समाविष्ट करा: ```python, ```bash, ```javascript
- टेबल्स, यादी आणि जोरासाठी विद्यमान स्वरूपनाचे अनुसरण करा
- ओळी वाचनीय ठेवा (~80-100 वर्णांचे लक्ष्य ठेवा, परंतु कठोर नाही)
- अंतर्गत संदर्भांसाठी सापेक्ष दुवे वापरा

### Python कोड शैली

- PEP 8 नियमांचे अनुसरण करा
- योग्य ठिकाणी प्रकार संकेत वापरा
- फंक्शन्स आणि वर्गांसाठी docstrings समाविष्ट करा
- अर्थपूर्ण व्हेरिएबल नावे वापरा
- फंक्शन्स लक्ष केंद्रित आणि संक्षिप्त ठेवा

### JavaScript/Node.js कोड शैली

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**मुख्य नियम:**
- नमुना 08 मध्ये ESLint कॉन्फिगरेशन प्रदान केले आहे
- कोड स्वरूपनासाठी Prettier वापरा
- आधुनिक ES6+ सिंटॅक्स वापरा
- कोडबेसमधील विद्यमान नमुन्यांचे अनुसरण करा

## पुल विनंती मार्गदर्शक तत्त्वे

### शीर्षक स्वरूप
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### सबमिट करण्यापूर्वी

**सामग्री बदलांसाठी:**
- सर्व सुधारित Markdown फाइल्स प्रीव्ह्यू करा
- दुवे आणि प्रतिमा कार्यरत आहेत याची खात्री करा
- टायपो आणि व्याकरणाच्या चुका तपासा

**नमुना कोड बदलांसाठी (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python नमुना बदलांसाठी:**
- नमुना यशस्वीरित्या चालतो याची चाचणी करा
- त्रुटी हाताळणी कार्यरत आहे याची खात्री करा
- Foundry Local सह सुसंगतता तपासा

### पुनरावलोकन प्रक्रिया

- शैक्षणिक सामग्री बदल अचूकता आणि स्पष्टतेसाठी पुनरावलोकन केले जातात
- कोड नमुने कार्यक्षमतेसाठी चाचणी केले जातात
- GitHub Actions द्वारे अनुवाद अद्यतन स्वयंचलितपणे हाताळले जातात

## अनुवाद प्रणाली

**महत्त्वाचे:** हा संग्रह GitHub Actions द्वारे स्वयंचलित अनुवाद वापरतो.

- अनुवाद `/translations/` निर्देशिकेत आहेत (50+ भाषा)
- `co-op-translator.yml` कार्यप्रवाहाद्वारे स्वयंचलित
- **अनुवाद फाइल्स मॅन्युअली संपादित करू नका** - त्या अधिलिखित केल्या जातील
- मूळ आणि मॉड्यूल निर्देशिकांमधील इंग्रजी स्रोत फाइल्स संपादित करा
- `main` शाखेत पुश केल्यावर अनुवाद स्वयंचलितपणे तयार होतात

## Foundry Local एकत्रीकरण

Module08 नमुन्यांपैकी बहुतेक नमुने Microsoft Foundry Local चालू असणे आवश्यक आहे:

### Foundry Local सुरू करणे
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

### Foundry Local सत्यापित करणे
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### नमुन्यांसाठी पर्यावरणीय व्हेरिएबल्स

बहुतेक नमुने या पर्यावरणीय व्हेरिएबल्स वापरतात:
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

## बांधणी आणि तैनाती

### सामग्री तैनाती

हा संग्रह प्रामुख्याने दस्तऐवजीकरण आहे - सामग्रीसाठी कोणतीही बांधणी प्रक्रिया आवश्यक नाही.

### नमुना अनुप्रयोग बांधणी

**Electron अनुप्रयोग (Module08/samples/08):**
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

**Python नमुने:**
कोणतीही बांधणी प्रक्रिया नाही - नमुने थेट Python interpreter सह चालवले जातात.

## सामान्य समस्या आणि समस्या निवारण

### Foundry Local चालू नाही
**समस्या:** नमुने कनेक्शन त्रुटींसह अयशस्वी होतात

**उपाय:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python व्हर्च्युअल वातावरण समस्या
**समस्या:** मॉड्यूल आयात त्रुटी

**उपाय:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron बांधणी समस्या
**समस्या:** npm install किंवा बांधणी अयशस्वी

**उपाय:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### अनुवाद कार्यप्रवाह संघर्ष
**समस्या:** अनुवाद PR तुमच्या बदलांशी संघर्ष करतो

**उपाय:**
- फक्त इंग्रजी स्रोत फाइल्स संपादित करा
- स्वयंचलित अनुवाद कार्यप्रवाह अनुवाद हाताळू द्या
- जर संघर्ष झाला तर, अनुवाद विलीन झाल्यानंतर `main` तुमच्या शाखेत विलीन करा

## अतिरिक्त संसाधने

### शिक्षण मार्ग
- **Beginner Path:** मॉड्यूल्स 01-02 (7-9 तास)
- **Intermediate Path:** मॉड्यूल्स 03-04 (9-11 तास)
- **Advanced Path:** मॉड्यूल्स 05-07 (12-15 तास)
- **Expert Path:** मॉड्यूल 08 (8-10 तास)

### मुख्य मॉड्यूल सामग्री
- **Module01:** EdgeAI मूलभूत गोष्टी आणि वास्तविक-जगातील केस स्टडीज
- **Module02:** Small Language Model (SLM) कुटुंबे आणि आर्किटेक्चर
- **Module03:** स्थानिक आणि क्लाउड तैनाती धोरणे
- **Module04:** अनेक फ्रेमवर्कसह मॉडेल ऑप्टिमायझेशन
- **Module05:** SLMOps - उत्पादन ऑपरेशन्स
- **Module06:** AI एजंट्स आणि फंक्शन कॉलिंग
- **Module07:** प्लॅटफॉर्म-विशिष्ट अंमलबजावणी
- **Module08:** Foundry Local टूलकिटसह 10 व्यापक नमुने

### बाह्य अवलंबित्वे
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - स्थानिक AI मॉडेल रनटाइम
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - ऑप्टिमायझेशन फ्रेमवर्क
- [Microsoft Olive](https://microsoft.github.io/Olive/) - मॉडेल ऑप्टिमायझेशन टूलकिट
- [OpenVINO](https://docs.openvino.ai/) - Intel चे ऑप्टिमायझेशन टूलकिट

## प्रकल्प-विशिष्ट टीप

### Module08 नमुना अनुप्रयोग

संग्रहात 10 व्यापक नमुना अनुप्रयोग समाविष्ट आहेत:

1. **01-REST Chat Quickstart** - मूलभूत OpenAI SDK एकत्रीकरण
2. **02-OpenAI SDK Integration** - प्रगत SDK वैशिष्ट्ये
3. **03-Model Discovery & Benchmarking** - मॉडेल तुलना साधने
4. **04-Chainlit RAG Application** - Retrieval-augmented generation
5. **05-Multi-Agent Orchestration** - मूलभूत एजंट समन्वय
6. **06-Models-as-Tools Router** - बुद्धिमान मॉडेल रूटिंग
7. **07-Direct API Client** - लो-लेव्हल API एकत्रीकरण
8. **08-Windows 11 Chat App** - मूळ Electron डेस्कटॉप अनुप्रयोग
9. **09-Advanced Multi-Agent System** - जटिल एजंट समन्वय
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel एकत्रीकरण

प्रत्येक नमुना Foundry Local सह Edge AI विकासाचे विविध पैलू प्रदर्शित करतो.

### कार्यक्षमता विचार

- SLMs Edge तैनातीसाठी ऑप्टिमाइझ केले आहेत (2-16GB RAM)
- स्थानिक अनुमान 50-500ms प्रतिसाद वेळ प्रदान करतो
- क्वांटायझेशन तंत्र 75% आकार कमी करून 85% कार्यक्षमता टिकवून ठेवते
- स्थानिक मॉडेल्ससह रिअल-टाइम संभाषण क्षमता

### सुरक्षा आणि गोपनीयता

- सर्व प्रक्रिया स्थानिक पातळीवर होते - कोणतेही डेटा क्लाउडला पाठवले जात नाही
- गोपनीयता-संवेदनशील अनुप्रयोगांसाठी योग्य (आरोग्यसेवा, वित्त)
- डेटा सार्वभौमत्व आवश्यकता पूर्ण करते
- Foundry Local पूर्णपणे स्थानिक हार्डवेअरवर चालतो

---

**हा Edge AI विकास शिकवणारा शैक्षणिक संग्रह आहे. प्राथमिक योगदान नमुना Edge AI संकल्पना प्रदर्शित करणारे शैक्षणिक सामग्री सुधारणे आणि नमुना अनुप्रयोग जोडणे/वाढवणे आहे.**

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.