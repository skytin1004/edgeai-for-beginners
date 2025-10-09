<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "135b2658979f1e494bb0ecc6e26d4752",
  "translation_date": "2025-10-09T09:09:59+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ne"
}
-->
# AGENTS.md

> **डेभलपर गाइड: EdgeAI को शुरुवातकर्ताहरूका लागि योगदान**
> 
> यो दस्तावेजले यस रिपोजिटरीसँग काम गर्ने डेभलपरहरू, AI एजेन्टहरू, र योगदानकर्ताहरूका लागि विस्तृत जानकारी प्रदान गर्दछ। यसमा सेटअप, विकास कार्यप्रवाह, परीक्षण, र उत्कृष्ट अभ्यासहरू समेटिएको छ।
> 
> **अन्तिम अपडेट**: अक्टोबर २०२५ | **दस्तावेज संस्करण**: २.०

## सामग्री तालिका

- [परियोजना अवलोकन](../..)
- [रिपोजिटरी संरचना](../..)
- [पूर्वापेक्षाहरू](../..)
- [सेटअप कमाण्डहरू](../..)
- [विकास कार्यप्रवाह](../..)
- [परीक्षण निर्देशनहरू](../..)
- [कोड शैली दिशानिर्देशहरू](../..)
- [पुल अनुरोध दिशानिर्देशहरू](../..)
- [अनुवाद प्रणाली](../..)
- [Foundry Local एकीकरण](../..)
- [निर्माण र परिनियोजन](../..)
- [सामान्य समस्याहरू र समाधान](../..)
- [अतिरिक्त स्रोतहरू](../..)
- [परियोजना-विशेष नोटहरू](../..)
- [मद्दत प्राप्त गर्ने तरिका](../..)

## परियोजना अवलोकन

EdgeAI for Beginners एक व्यापक शैक्षिक रिपोजिटरी हो जसले साना भाषा मोडेल (SLMs) प्रयोग गरेर Edge AI विकास सिकाउँछ। यो पाठ्यक्रमले EdgeAI को आधारभूत कुरा, मोडेल परिनियोजन, अनुकूलन प्रविधिहरू, र उत्पादन-तयार कार्यान्वयनहरू Microsoft Foundry Local र विभिन्न AI फ्रेमवर्कहरू प्रयोग गरेर समेट्छ।

**मुख्य प्रविधिहरू:**
- Python 3.8+ (AI/ML नमूनाहरूको लागि प्राथमिक भाषा)
- .NET C# (AI/ML नमूनाहरू)
- JavaScript/Node.js with Electron (डेस्कटप अनुप्रयोगहरूको लागि)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI फ्रेमवर्कहरू: LangChain, Semantic Kernel, Chainlit
- मोडेल अनुकूलन: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**रिपोजिटरी प्रकार:** ८ मोड्युल र १० व्यापक नमूना अनुप्रयोगहरू सहितको शैक्षिक सामग्री रिपोजिटरी

**आर्किटेक्चर:** व्यावहारिक नमूनाहरू मार्फत Edge AI परिनियोजन ढाँचाहरू प्रदर्शन गर्ने बहु-मोड्युल शिक्षण पथ

## रिपोजिटरी संरचना

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

## पूर्वापेक्षाहरू

### आवश्यक उपकरणहरू

- **Python 3.8+** - AI/ML नमूनाहरू र नोटबुकहरूको लागि
- **Node.js 16+** - Electron नमूना अनुप्रयोगको लागि
- **Git** - संस्करण नियन्त्रणको लागि
- **Microsoft Foundry Local** - AI मोडेलहरू स्थानीय रूपमा चलाउनको लागि

### सिफारिस गरिएका उपकरणहरू

- **Visual Studio Code** - Python, Jupyter, र Pylance एक्सटेन्सनहरूसहित
- **Windows Terminal** - राम्रो कमाण्ड-लाइन अनुभवको लागि (Windows प्रयोगकर्ताहरू)
- **Docker** - कन्टेनराइज्ड विकासको लागि (वैकल्पिक)

### प्रणाली आवश्यकताहरू

- **RAM**: न्यूनतम ८GB, बहु-मोडेल परिदृश्यहरूको लागि १६GB+ सिफारिस
- **स्टोरेज**: मोडेलहरू र निर्भरताहरूको लागि १०GB+ खाली ठाउँ
- **OS**: Windows 10/11, macOS 11+, वा Linux (Ubuntu 20.04+)
- **हार्डवेयर**: AVX2 समर्थन भएको CPU; GPU (CUDA, Qualcomm NPU) वैकल्पिक तर सिफारिस गरिएको

### ज्ञान पूर्वापेक्षाहरू

- Python प्रोग्रामिङको आधारभूत समझ
- कमाण्ड-लाइन इन्टरफेसहरूसँग परिचितता
- AI/ML अवधारणाहरूको समझ (नमूना विकासको लागि)
- Git कार्यप्रवाहहरू र पुल अनुरोध प्रक्रियाहरू

## सेटअप कमाण्डहरू

### रिपोजिटरी सेटअप

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

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Node.js नमूना सेटअप (नमूना ०८ - Windows Chat App)

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

Foundry Local नमूनाहरू चलाउन आवश्यक छ। आधिकारिक रिपोजिटरीबाट डाउनलोड र स्थापना गर्नुहोस्:

**स्थापना:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **म्यानुअल**: [रिलिज पृष्ठ](https://github.com/microsoft/Foundry-Local/releases) बाट डाउनलोड गर्नुहोस्

**द्रुत सुरुवात:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-3.5-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**नोट**: Foundry Local ले तपाईंको हार्डवेयरको लागि उत्तम मोडेल भेरियन्ट स्वतः चयन गर्दछ (CUDA GPU, Qualcomm NPU, वा CPU)।

## विकास कार्यप्रवाह

### सामग्री विकास

यो रिपोजिटरी मुख्य रूपमा **Markdown शैक्षिक सामग्री** समावेश गर्दछ। परिवर्तन गर्दा:

1. उपयुक्त मोड्युल निर्देशिकाहरूमा `.md` फाइलहरू सम्पादन गर्नुहोस्
2. विद्यमान ढाँचाहरू अनुसरण गर्नुहोस्
3. कोड उदाहरणहरू सटीक र परीक्षण गरिएको सुनिश्चित गर्नुहोस्
4. आवश्यक परेमा सम्बन्धित अनुवादित सामग्री अद्यावधिक गर्नुहोस् (वा स्वचालनलाई यसलाई ह्यान्डल गर्न दिनुहोस्)

### नमूना अनुप्रयोग विकास

Python नमूनाहरूको लागि (नमूना ०१-०७, ०९-१०):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron नमूनाको लागि (नमूना ०८):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### नमूना अनुप्रयोग परीक्षण

Python नमूनाहरूमा स्वचालित परीक्षण छैन तर तिनीहरू चलाएर मान्य गर्न सकिन्छ:
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

### सामग्री मान्यता

रिपोजिटरीले स्वचालित अनुवाद कार्यप्रवाहहरू प्रयोग गर्दछ। अनुवादहरूको लागि कुनै म्यानुअल परीक्षण आवश्यक छैन।

**सामग्री परिवर्तनहरूको लागि म्यानुअल मान्यता:**
1. `.md` फाइलहरू पूर्वावलोकन गरेर Markdown रेंडरिङ समीक्षा गर्नुहोस्
2. सबै लिंकहरू मान्य लक्ष्यहरूमा संकेत गर्छन् भनी सुनिश्चित गर्नुहोस्
3. दस्तावेजमा समावेश गरिएका कुनै पनि कोड स्निपेटहरू परीक्षण गर्नुहोस्
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
- लाइनहरू पढ्न मिल्ने बनाउनुहोस् (~८०-१०० अक्षरहरूको लक्ष्य राख्नुहोस्, तर कडा नियम होइन)
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
- नमूना ०८ मा प्रदान गरिएको ESLint कन्फिगरेसन
- कोड ढाँचाका लागि Prettier
- आधुनिक ES6+ सिन्ट्याक्स प्रयोग गर्नुहोस्
- कोडबेसमा विद्यमान ढाँचाहरू अनुसरण गर्नुहोस्

## पुल अनुरोध दिशानिर्देशहरू

### योगदान कार्यप्रवाह

1. **रिपोजिटरी फोर्क गर्नुहोस्** र `main` बाट नयाँ शाखा सिर्जना गर्नुहोस्
2. **तपाईंको परिवर्तनहरू गर्नुहोस्** कोड शैली दिशानिर्देशहरू अनुसरण गर्दै
3. **परीक्षण गर्नुहोस्** माथि दिइएको परीक्षण निर्देशनहरू प्रयोग गरेर
4. **स्पष्ट सन्देशहरूसहित कमिट गर्नुहोस्** परम्परागत कमिट ढाँचाको अनुसरण गर्दै
5. **तपाईंको फोर्कमा पुश गर्नुहोस्** र पुल अनुरोध सिर्जना गर्नुहोस्
6. **समीक्षा क्रममा मर्मतकर्ताहरूको प्रतिक्रिया दिनुहोस्**

### शाखा नामकरण सम्मेलन

- `feature/<module>-<description>` - नयाँ सुविधाहरू वा सामग्रीको लागि
- `fix/<module>-<description>` - बग सुधारको लागि
- `docs/<description>` - दस्तावेज सुधारको लागि
- `refactor/<description>` - कोड पुनर्संरचना

### कमिट सन्देश ढाँचा

[Conventional Commits](https://www.conventionalcommits.org/) अनुसरण गर्नुहोस्:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**उदाहरणहरू:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### शीर्षक ढाँचा
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### आचार संहिता

सबै योगदानकर्ताहरूले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) अनुसरण गर्नुपर्छ। योगदान गर्नु अघि कृपया [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) समीक्षा गर्नुहोस्।

### पेश गर्नु अघि

**सामग्री परिवर्तनहरूको लागि:**
- सबै संशोधित Markdown फाइलहरू पूर्वावलोकन गर्नुहोस्
- लिंकहरू र छविहरू काम गर्छन् भनी सुनिश्चित गर्नुहोस्
- टाइपो र व्याकरण त्रुटिहरूको लागि जाँच गर्नुहोस्

**नमूना कोड परिवर्तनहरूको लागि (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python नमूना परिवर्तनहरूको लागि:**
- नमूना सफलतापूर्वक चल्छ भनी परीक्षण गर्नुहोस्
- त्रुटि ह्यान्डलिङ काम गर्छ भनी सुनिश्चित गर्नुहोस्
- Foundry Local सँग अनुकूलता जाँच गर्नुहोस्

### समीक्षा प्रक्रिया

- शैक्षिक सामग्री परिवर्तनहरू सटीकता र स्पष्टताको लागि समीक्षा गरिन्छ
- कोड नमूनाहरू कार्यक्षमताको लागि परीक्षण गरिन्छ
- अनुवाद अपडेटहरू GitHub Actions द्वारा स्वचालित रूपमा ह्यान्डल गरिन्छ

## अनुवाद प्रणाली

**महत्वपूर्ण:** यो रिपोजिटरीले GitHub Actions मार्फत स्वचालित अनुवाद प्रयोग गर्दछ।

- अनुवादहरू `/translations/` निर्देशिकामा छन् (५०+ भाषाहरू)
- `co-op-translator.yml` कार्यप्रवाह मार्फत स्वचालित
- **अनुवाद फाइलहरू म्यानुअल रूपमा सम्पादन नगर्नुहोस्** - तिनीहरू ओभरराइट गरिनेछन्
- मूल अंग्रेजी स्रोत फाइलहरू मात्र सम्पादन गर्नुहोस् रूट र मोड्युल निर्देशिकाहरूमा
- `main` शाखामा पुश गर्दा अनुवादहरू स्वचालित रूपमा उत्पन्न हुन्छन्

## Foundry Local एकीकरण

Module08 का अधिकांश नमूनाहरू Microsoft Foundry Local चलिरहेको आवश्यक छ।

### स्थापना र सेटअप

**Foundry Local स्थापना गर्नुहोस्:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK स्थापना गर्नुहोस्:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local सुरु गर्दै
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### SDK प्रयोग (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-3.5-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Foundry Local प्रमाणित गर्दै
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### नमूनाहरूको लागि वातावरण चरहरू

अधिकांश नमूनाहरूले यी वातावरण चरहरू प्रयोग गर्छन्:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-3.5-mini  # or phi-4-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**नोट**: `FoundryLocalManager` प्रयोग गर्दा, SDK ले सेवा खोजी र मोडेल लोडिङ स्वचालित रूपमा ह्यान्डल गर्छ। मोडेल उपनामहरू (जस्तै `phi-3.5-mini`) ले तपाईंको हार्डवेयरको लागि उत्तम भेरियन्ट सुनिश्चित गर्छ।

## निर्माण र परिनियोजन

### सामग्री परिनियोजन

यो रिपोजिटरी मुख्य रूपमा दस्तावेज हो - सामग्रीको लागि कुनै निर्माण प्रक्रिया आवश्यक छैन।

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
कुनै निर्माण प्रक्रिया छैन - नमूनाहरू Python इन्टरप्रिटरसँग सिधै चलाइन्छन्।

## सामान्य समस्याहरू र समाधान

> **टिप**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) मा ज्ञात समस्याहरू र समाधानहरू जाँच गर्नुहोस्।

### महत्वपूर्ण समस्याहरू (ब्लकिङ)

#### Foundry Local चलिरहेको छैन
**समस्या:** नमूनाहरू जडान त्रुटिहरूसँग असफल हुन्छन्

**समाधान:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-3.5-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### सामान्य समस्याहरू (मध्यम)

#### Python भर्चुअल वातावरण समस्याहरू
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

#### Electron निर्माण समस्याहरू
**समस्या:** npm स्थापना वा निर्माण असफलता

**समाधान:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### कार्यप्रवाह समस्याहरू (सामान्य)

#### अनुवाद कार्यप्रवाह द्वन्द्व
**समस्या:** अनुवाद PR तपाईंको परिवर्तनहरूसँग द्वन्द्वमा छ

**समाधान:**
- अंग्रेजी स्रोत फाइलहरू मात्र सम्पादन गर्नुहोस्
- स्वचालित अनुवाद कार्यप्रवाहलाई अनुवादहरू ह्यान्डल गर्न दिनुहोस्
- यदि द्वन्द्वहरू उत्पन्न हुन्छन् भने, अनुवादहरू मर्ज भएपछि `main` लाई तपाईंको शाखामा मर्ज गर्नुहोस्

#### मोडेल डाउनलोड असफलता
**समस्या:** Foundry Local मोडेलहरू डाउनलोड गर्न असफल हुन्छ

**समाधान:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## अतिरिक्त स्रोतहरू

### शिक्षण पथहरू
- **शुरुवात पथ:** मोड्युल ०१-०२ (७-९ घण्टा)
- **मध्यम पथ:** मोड्युल ०३-०४ (९-११ घण्टा)
- **उन्नत पथ:** मोड्युल ०५-०७ (१२-१५ घण्टा)
- **विशेषज्ञ पथ:** मोड्युल ०८ (८-१० घण्टा)

### प्रमुख मोड्युल सामग्री
- **मोड्युल०१:** EdgeAI को आधारभूत कुरा र वास्तविक-विश्व केस अध्ययनहरू
- **मोड्युल०२:** साना भाषा मोडेल (SLM) परिवारहरू र आर्किटेक्चरहरू
- **मोड्युल०३:** स्थानीय र क्लाउड परिनियोजन रणनीतिहरू
- **मोड्युल०४:** बहु-फ्रेमवर्कहरूसँग मोडेल अनुकूलन
- **मोड्युल०५:** SLMOps - उत्पादन सञ्चालनहरू
- **मोड्युल०६:** AI एजेन्टहरू र कार्य कलिङ
- **मोड्युल०७:** प्लेटफर्म-विशेष कार्यान्वयनहरू
- **मोड्युल०८:** Foundry Local टूलकिट १० व्यापक नमूनाहरू सहित

### बाह्य निर्भरताहरू
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI-संगत API सहितको स्थानीय AI मोडेल रनटाइम
  - [दस्तावेज](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - अनुकूलन फ्रेमवर्क
- [Microsoft Olive](https://microsoft.github.io/Olive/) - मोडेल अनुकूलन टूलकिट
- [OpenVINO](https://docs.openvino.ai/) - Intel को अनुकूलन टूलकिट

## परियोजना-विशेष नोटहरू

### Module08 नमूना अनुप्रयोगहरू

रिपोजिटरीमा १० व्यापक नमूना अनुप्रयोगहरू समावेश छन्:

1. **01-REST Chat Quickstart** - आधारभूत OpenAI SDK एकीकरण
2. **02-OpenAI SDK Integration** - उन्नत SDK सुविधाहरू
3. **03-Model Discovery & Benchmarking** - मोडेल तुलना उपकरणहरू
4. **04-Chainlit RAG Application** - पुनःप्राप्ति-संवर्धित उत्पादन
5. **05-Multi-Agent Orchestration** - आधारभूत एजेन्ट समन्वय
6. **06-Models-as-Tools Router** - बौद्धिक मोडेल राउटिङ
7. **07-Direct API Client** - कम-स्तर API एकीकरण
8. **08-Windows 11 Chat App** - देशी Electron डेस्कटप अनुप्रयोग
9. **09-Advanced Multi-Agent System** - जटिल एजेन्ट समन्वय
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel एकीकरण

प्रत्य
- स्थानीय इनफरेन्सले ५०-५०० मिलिसेकेन्डको प्रतिक्रिया समय प्रदान गर्दछ
- क्वान्टाइजेसन प्रविधिले ७५% आकार घटाउने र ८५% प्रदर्शन कायम राख्ने क्षमता हासिल गर्दछ
- स्थानीय मोडेलहरूसँग वास्तविक समय संवादको क्षमता

### सुरक्षा र गोपनीयता

- सबै प्रक्रिया स्थानीय रूपमा हुन्छ - कुनै पनि डेटा क्लाउडमा पठाइँदैन
- गोपनीयता-संवेदनशील एप्लिकेसनहरू (जस्तै स्वास्थ्य सेवा, वित्त) का लागि उपयुक्त
- डेटा सार्वभौमिकता आवश्यकताहरू पूरा गर्दछ
- Foundry Local पूर्ण रूपमा स्थानीय हार्डवेयरमा चल्छ

## सहयोग प्राप्त गर्ने तरिका

### दस्तावेज

- **मुख्य README**: [README.md](README.md) - रिपोजिटरीको अवलोकन र सिकाइका मार्गहरू
- **अध्ययन मार्गदर्शक**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - सिकाइका स्रोतहरू र समयरेखा
- **सहयोग**: [SUPPORT.md](SUPPORT.md) - सहयोग प्राप्त गर्ने तरिका
- **सुरक्षा**: [SECURITY.md](SECURITY.md) - सुरक्षा समस्याहरू रिपोर्ट गर्ने तरिका

### समुदाय सहयोग

- **GitHub Issues**: [बग रिपोर्ट गर्नुहोस् वा फिचर अनुरोध गर्नुहोस्](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [प्रश्न सोध्नुहोस् र विचारहरू साझा गर्नुहोस्](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Foundry Local सम्बन्धी प्राविधिक समस्याहरू](https://github.com/microsoft/Foundry-Local/issues)

### सम्पर्क

- **रखवाला**: [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS) हेर्नुहोस्
- **सुरक्षा समस्याहरू**: [SECURITY.md](SECURITY.md) मा जिम्मेवार प्रकटीकरणको पालना गर्नुहोस्
- **Microsoft सहयोग**: उद्यम सहयोगका लागि Microsoft ग्राहक सेवासँग सम्पर्क गर्नुहोस्

### थप स्रोतहरू

- **Microsoft Learn**: [AI र मेसिन लर्निङ सिकाइका मार्गहरू](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local दस्तावेज**: [औपचारिक दस्तावेज](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **समुदाय नमूनाहरू**: समुदाय योगदानका लागि [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) हेर्नुहोस्

---

**यो शैक्षिक रिपोजिटरी Edge AI विकास सिकाउनेमा केन्द्रित छ। मुख्य योगदान ढाँचा शैक्षिक सामग्री सुधार गर्ने र Edge AI अवधारणाहरू प्रदर्शन गर्ने नमूना एप्लिकेसनहरू थप्ने/सुधार गर्ने हो।**

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।