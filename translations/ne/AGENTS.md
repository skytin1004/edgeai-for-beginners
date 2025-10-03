<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:29:35+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ne"
}
-->
# AGENTS.md

## परियोजना अवलोकन

EdgeAI for Beginners एउटा व्यापक शैक्षिक भण्डार हो जसले साना भाषा मोडेलहरू (SLMs) प्रयोग गरेर Edge AI विकास सिकाउँछ। यो पाठ्यक्रमले EdgeAI को आधारभूत कुराहरू, मोडेल परिनियोजन, अनुकूलन प्रविधिहरू, र उत्पादन-तयार कार्यान्वयनहरू Microsoft Foundry Local र विभिन्न AI फ्रेमवर्कहरू प्रयोग गरेर समेट्छ।

**मुख्य प्रविधिहरू:**
- Python 3.8+ (AI/ML नमूनाहरूको प्राथमिक भाषा)
- .NET C# (AI/ML नमूनाहरू)
- JavaScript/Node.js Electron सँग (डेस्कटप अनुप्रयोगहरूको लागि)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI फ्रेमवर्कहरू: LangChain, Semantic Kernel, Chainlit
- मोडेल अनुकूलन: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**भण्डार प्रकार:** ८ मोड्युलहरू र १० व्यापक नमूना अनुप्रयोगहरू सहितको शैक्षिक सामग्री भण्डार

**आर्किटेक्चर:** व्यावहारिक नमूनाहरूले Edge AI परिनियोजन ढाँचाहरू प्रदर्शन गर्ने बहु-मोड्युल सिकाइ मार्ग

## भण्डार संरचना

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

## सेटअप आदेशहरू

### भण्डार सेटअप

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python नमूना सेटअप (Module08 र Python नमूनाहरू)

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

### Node.js नमूना सेटअप (नमूना 08 - Windows Chat App)

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

Module08 नमूनाहरू चलाउन Foundry Local आवश्यक छ:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## विकास कार्यप्रवाह

### सामग्री विकास

यो भण्डारमा मुख्य रूपमा **Markdown शैक्षिक सामग्री** समावेश छ। परिवर्तन गर्दा:

1. उपयुक्त मोड्युल निर्देशिकाहरूमा `.md` फाइलहरू सम्पादन गर्नुहोस्
2. विद्यमान ढाँचाहरू अनुसरण गर्नुहोस्
3. कोड उदाहरणहरू सटीक र परीक्षण गरिएको सुनिश्चित गर्नुहोस्
4. आवश्यक परेमा सम्बन्धित अनुवादित सामग्री अद्यावधिक गर्नुहोस् (वा स्वचालनलाई यसलाई ह्यान्डल गर्न दिनुहोस्)

### नमूना अनुप्रयोग विकास

Python नमूनाहरूको लागि (नमूनाहरू 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron नमूनाको लागि (नमूना 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### नमूना अनुप्रयोग परीक्षण

Python नमूनाहरूमा स्वचालित परीक्षण छैन तर तिनीहरू चलाएर प्रमाणित गर्न सकिन्छ:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron नमूनामा परीक्षण पूर्वाधार छ:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## परीक्षण निर्देशनहरू

### सामग्री प्रमाणीकरण

भण्डारले स्वचालित अनुवाद कार्यप्रवाहहरू प्रयोग गर्दछ। अनुवादहरूको लागि कुनै म्यानुअल परीक्षण आवश्यक छैन।

**सामग्री परिवर्तनहरूको लागि म्यानुअल प्रमाणीकरण:**
1. `.md` फाइलहरू पूर्वावलोकन गरेर Markdown रेंडरिङ समीक्षा गर्नुहोस्
2. सबै लिंकहरू मान्य लक्ष्यहरूमा संकेत गर्छन् भनी प्रमाणित गर्नुहोस्
3. दस्तावेजमा समावेश गरिएको कुनै पनि कोड स्निपेट परीक्षण गर्नुहोस्
4. छविहरू सही रूपमा लोड हुन्छन् भनी जाँच गर्नुहोस्

### नमूना अनुप्रयोग परीक्षण

**Module08/samples/08 (Electron अनुप्रयोग) मा व्यापक परीक्षण छ:**
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

**Python नमूनाहरू म्यानुअल रूपमा परीक्षण गर्नुपर्छ:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## कोड शैली दिशानिर्देशहरू

### Markdown सामग्री

- लगातार शीर्षक पदानुक्रम प्रयोग गर्नुहोस् (# शीर्षकको लागि, ## मुख्य खण्डहरूको लागि, ### उपखण्डहरूको लागि)
- भाषा निर्दिष्टकर्ताहरू सहित कोड ब्लकहरू समावेश गर्नुहोस्: ```python, ```bash, ```javascript
- तालिका, सूची, र जोडको लागि विद्यमान ढाँचाहरू अनुसरण गर्नुहोस्
- लाइनहरू पढ्न योग्य राख्नुहोस् (~80-100 अक्षरहरूको लक्ष्य राख्नुहोस्, तर कडा छैन)
- आन्तरिक सन्दर्भहरूको लागि सापेक्ष लिंकहरू प्रयोग गर्नुहोस्

### Python कोड शैली

- PEP 8 सम्मेलनहरू अनुसरण गर्नुहोस्
- उपयुक्त ठाउँमा प्रकार संकेतहरू प्रयोग गर्नुहोस्
- कार्यहरू र कक्षाहरूको लागि डकस्ट्रिङहरू समावेश गर्नुहोस्
- अर्थपूर्ण भेरिएबल नामहरू प्रयोग गर्नुहोस्
- कार्यहरू केन्द्रित र संक्षिप्त राख्नुहोस्

### JavaScript/Node.js कोड शैली

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**मुख्य सम्मेलनहरू:**
- नमूना 08 मा प्रदान गरिएको ESLint कन्फिगरेसन
- कोड ढाँचाका लागि Prettier
- आधुनिक ES6+ सिन्ट्याक्स प्रयोग गर्नुहोस्
- कोडबेसमा विद्यमान ढाँचाहरू अनुसरण गर्नुहोस्

## पुल अनुरोध दिशानिर्देशहरू

### शीर्षक ढाँचा
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### पेश गर्नु अघि

**सामग्री परिवर्तनहरूको लागि:**
- सबै संशोधित Markdown फाइलहरू पूर्वावलोकन गर्नुहोस्
- लिंकहरू र छविहरू काम गर्छन् भनी प्रमाणित गर्नुहोस्
- टाइपो र व्याकरण त्रुटिहरू जाँच गर्नुहोस्

**नमूना कोड परिवर्तनहरूको लागि (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python नमूना परिवर्तनहरूको लागि:**
- नमूना सफलतापूर्वक चल्छ भनी परीक्षण गर्नुहोस्
- त्रुटि ह्यान्डलिङ काम गर्छ भनी प्रमाणित गर्नुहोस्
- Foundry Local सँग अनुकूलता जाँच गर्नुहोस्

### समीक्षा प्रक्रिया

- शैक्षिक सामग्री परिवर्तनहरू सटीकता र स्पष्टताको लागि समीक्षा गरिन्छ
- कोड नमूनाहरू कार्यक्षमताको लागि परीक्षण गरिन्छ
- अनुवाद अद्यावधिकहरू स्वचालित रूपमा GitHub Actions द्वारा ह्यान्डल गरिन्छ

## अनुवाद प्रणाली

**महत्वपूर्ण:** यो भण्डारले GitHub Actions मार्फत स्वचालित अनुवाद प्रयोग गर्दछ।

- अनुवादहरू `/translations/` निर्देशिकामा छन् (५०+ भाषाहरू)
- `co-op-translator.yml` कार्यप्रवाह मार्फत स्वचालित
- **अनुवाद फाइलहरू म्यानुअल रूपमा सम्पादन नगर्नुहोस्** - तिनीहरू अधिलेखित हुनेछन्
- मूल अंग्रेजी स्रोत फाइलहरू मात्र सम्पादन गर्नुहोस् र मोड्युल निर्देशिकाहरूमा
- `main` शाखामा पुश गर्दा अनुवादहरू स्वचालित रूपमा उत्पन्न हुन्छन्

## Foundry Local एकीकरण

अधिकांश Module08 नमूनाहरू चलाउन Microsoft Foundry Local आवश्यक छ:

### Foundry Local सुरु गर्दै
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

### Foundry Local प्रमाणित गर्दै
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### नमूनाहरूको लागि वातावरण चरहरू

अधिकांश नमूनाहरूले यी वातावरण चरहरू प्रयोग गर्छन्:
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

## निर्माण र परिनियोजन

### सामग्री परिनियोजन

यो भण्डार मुख्य रूपमा दस्तावेजीकरण हो - सामग्रीको लागि कुनै निर्माण प्रक्रिया आवश्यक छैन।

### नमूना अनुप्रयोग निर्माण

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

**Python नमूनाहरू:**
कुनै निर्माण प्रक्रिया छैन - नमूनाहरू Python व्याख्याता सँग सिधै चलाइन्छ।

## सामान्य समस्याहरू र समस्या समाधान

### Foundry Local चलिरहेको छैन
**समस्या:** नमूनाहरू जडान त्रुटिहरूको साथ असफल हुन्छन्

**समाधान:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python भर्चुअल वातावरण समस्याहरू
**समस्या:** मोड्युल आयात त्रुटिहरू

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

### Electron निर्माण समस्याहरू
**समस्या:** npm install वा निर्माण असफलता

**समाधान:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### अनुवाद कार्यप्रवाह द्वन्द्वहरू
**समस्या:** अनुवाद PR तपाईंको परिवर्तनहरूसँग द्वन्द्वमा छ

**समाधान:**
- केवल अंग्रेजी स्रोत फाइलहरू सम्पादन गर्नुहोस्
- स्वचालित अनुवाद कार्यप्रवाहलाई अनुवादहरू ह्यान्डल गर्न दिनुहोस्
- यदि द्वन्द्वहरू उत्पन्न हुन्छन् भने, अनुवादहरू मर्ज भएपछि `main` लाई तपाईंको शाखामा मर्ज गर्नुहोस्

## अतिरिक्त स्रोतहरू

### सिकाइ मार्गहरू
- **सुरुआती मार्ग:** मोड्युलहरू 01-02 (7-9 घण्टा)
- **मध्यम मार्ग:** मोड्युलहरू 03-04 (9-11 घण्टा)
- **उन्नत मार्ग:** मोड्युलहरू 05-07 (12-15 घण्टा)
- **विशेषज्ञ मार्ग:** मोड्युल 08 (8-10 घण्टा)

### प्रमुख मोड्युल सामग्री
- **Module01:** EdgeAI को आधारभूत कुराहरू र वास्तविक-विश्व केस अध्ययनहरू
- **Module02:** साना भाषा मोडेल (SLM) परिवारहरू र आर्किटेक्चरहरू
- **Module03:** स्थानीय र क्लाउड परिनियोजन रणनीतिहरू
- **Module04:** बहु फ्रेमवर्कहरूसँग मोडेल अनुकूलन
- **Module05:** SLMOps - उत्पादन सञ्चालनहरू
- **Module06:** AI एजेन्टहरू र कार्य कलिङ
- **Module07:** प्लेटफर्म-विशिष्ट कार्यान्वयनहरू
- **Module08:** Foundry Local टूलकिट १० व्यापक नमूनाहरू सहित

### बाह्य निर्भरताहरू
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - स्थानीय AI मोडेल रनटाइम
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - अनुकूलन फ्रेमवर्क
- [Microsoft Olive](https://microsoft.github.io/Olive/) - मोडेल अनुकूलन टूलकिट
- [OpenVINO](https://docs.openvino.ai/) - Intel को अनुकूलन टूलकिट

## परियोजना-विशिष्ट नोटहरू

### Module08 नमूना अनुप्रयोगहरू

भण्डारमा १० व्यापक नमूना अनुप्रयोगहरू समावेश छन्:

1. **01-REST Chat Quickstart** - आधारभूत OpenAI SDK एकीकरण
2. **02-OpenAI SDK Integration** - उन्नत SDK सुविधाहरू
3. **03-Model Discovery & Benchmarking** - मोडेल तुलना उपकरणहरू
4. **04-Chainlit RAG Application** - पुनःप्राप्ति-संवर्धित उत्पादन
5. **05-Multi-Agent Orchestration** - आधारभूत एजेन्ट समन्वय
6. **06-Models-as-Tools Router** - बुद्धिमान मोडेल राउटिङ
7. **07-Direct API Client** - निम्न-स्तर API एकीकरण
8. **08-Windows 11 Chat App** - देशी Electron डेस्कटप अनुप्रयोग
9. **09-Advanced Multi-Agent System** - जटिल एजेन्ट समन्वय
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel एकीकरण

प्रत्येक नमूनाले Foundry Local सँग Edge AI विकासका विभिन्न पक्षहरू प्रदर्शन गर्दछ।

### प्रदर्शन विचारहरू

- SLMs Edge परिनियोजनको लागि अनुकूलित छन् (2-16GB RAM)
- स्थानीय अनुमानले 50-500ms प्रतिक्रिया समय प्रदान गर्दछ
- क्वान्टाइजेसन प्रविधिहरूले 75% आकार घटाउने र 85% प्रदर्शन कायम राख्ने उपलब्धि हासिल गर्छन्
- स्थानीय मोडेलहरूसँग वास्तविक-समय वार्तालाप क्षमता

### सुरक्षा र गोपनीयता

- सबै प्रशोधन स्थानीय रूपमा हुन्छ - कुनै पनि डाटा क्लाउडमा पठाइँदैन
- गोपनीयता-संवेदनशील अनुप्रयोगहरूको लागि उपयुक्त (स्वास्थ्य सेवा, वित्त)
- डाटा सार्वभौमिकता आवश्यकताहरू पूरा गर्दछ
- Foundry Local पूर्ण रूपमा स्थानीय हार्डवेयरमा चल्छ

---

**यो शैक्षिक भण्डार Edge AI विकास सिकाउन केन्द्रित छ। मुख्य योगदान ढाँचा शैक्षिक सामग्री सुधार गर्ने र Edge AI अवधारणाहरू प्रदर्शन गर्ने नमूना अनुप्रयोगहरू थप्ने/विस्तार गर्ने हो।**

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथासम्भव शुद्धता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।