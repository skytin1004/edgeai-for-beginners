<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "135b2658979f1e494bb0ecc6e26d4752",
  "translation_date": "2025-10-11T10:58:14+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ta"
}
-->
# AGENTS.md

> **EdgeAI ஆரம்பக்கட்ட பயிற்சிக்கான டெவலப்பர் வழிகாட்டி**
> 
> இந்த ஆவணம் இந்த repository-யுடன் பணியாற்றும் டெவலப்பர்கள், AI ஏஜென்ட்கள் மற்றும் பங்களிப்பாளர்களுக்கு விரிவான தகவல்களை வழங்குகிறது. இது அமைப்பு, மேம்பாட்டு வேலைகள், சோதனை மற்றும் சிறந்த நடைமுறைகளை உள்ளடக்கியது.
> 
> **கடைசியாக புதுப்பிக்கப்பட்டது**: அக்டோபர் 2025 | **ஆவண பதிப்பு**: 2.0

## உள்ளடக்க அட்டவணை

- [திட்டத்தின் மேற்பார்வை](../..)
- [Repository அமைப்பு](../..)
- [முன்னோட்டங்கள்](../..)
- [அமைப்பு கட்டளைகள்](../..)
- [மேம்பாட்டு வேலைகள்](../..)
- [சோதனை வழிகாட்டுதல்கள்](../..)
- [கோடு பாணி வழிகாட்டுதல்கள்](../..)
- [Pull Request வழிகாட்டுதல்கள்](../..)
- [மொழிபெயர்ப்பு அமைப்பு](../..)
- [Foundry Local ஒருங்கிணைப்பு](../..)
- [Build மற்றும் Deployment](../..)
- [பொதுவான சிக்கல்கள் மற்றும் தீர்வுகள்](../..)
- [கூடுதல் வளங்கள்](../..)
- [திட்டத்திற்கு குறிப்பிட்ட குறிப்புகள்](../..)
- [உதவி பெறுதல்](../..)

## திட்டத்தின் மேற்பார்வை

EdgeAI for Beginners என்பது Small Language Models (SLMs) உடன் Edge AI மேம்பாட்டை கற்பதற்கான விரிவான கல்வி repository ஆகும். இந்த பாடநெறி EdgeAI அடிப்படைகள், மாடல் deployment, optimization தொழில்நுட்பங்கள் மற்றும் Microsoft Foundry Local மற்றும் பல AI frameworks-களைப் பயன்படுத்தி தயாரிப்பு-தயார் செயல்பாடுகளை உள்ளடக்கியது.

**முக்கிய தொழில்நுட்பங்கள்:**
- Python 3.8+ (AI/ML மாதிரிகளுக்கான முதன்மை மொழி)
- .NET C# (AI/ML மாதிரிகள்)
- JavaScript/Node.js மற்றும் Electron (டெஸ்க்டாப் பயன்பாடுகளுக்காக)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI Frameworks: LangChain, Semantic Kernel, Chainlit
- Model Optimization: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repository வகை:** 8 modules மற்றும் 10 விரிவான மாதிரி பயன்பாடுகளுடன் கல்வி உள்ளடக்க repository

**Architecture:** Edge AI deployment patterns-ஐ விளக்கும் நடைமுறை மாதிரிகளுடன் பல module கற்றல் பாதை

## Repository அமைப்பு

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

## முன்னோட்டங்கள்

### தேவையான கருவிகள்

- **Python 3.8+** - AI/ML மாதிரிகள் மற்றும் நோட்புக்குகளுக்காக
- **Node.js 16+** - Electron மாதிரி பயன்பாட்டுக்காக
- **Git** - பதிப்பு கட்டுப்பாட்டுக்காக
- **Microsoft Foundry Local** - AI மாதிரிகளை உள்ளூர் இயக்குவதற்காக

### பரிந்துரைக்கப்பட்ட கருவிகள்

- **Visual Studio Code** - Python, Jupyter மற்றும் Pylance extensions உடன்
- **Windows Terminal** - Windows பயனர்களுக்கு சிறந்த கட்டளை வரி அனுபவத்திற்காக
- **Docker** - Containerized மேம்பாட்டிற்காக (விருப்பம்)

### கணினி தேவைகள்

- **RAM**: குறைந்தபட்சம் 8GB, பல மாடல் சூழல்களுக்கு 16GB+ பரிந்துரைக்கப்படுகிறது
- **Storage**: மாடல்கள் மற்றும் dependencies க்காக 10GB+ இலவச இடம்
- **OS**: Windows 10/11, macOS 11+, அல்லது Linux (Ubuntu 20.04+)
- **Hardware**: AVX2 ஆதரவு கொண்ட CPU; GPU (CUDA, Qualcomm NPU) விருப்பமானது ஆனால் பரிந்துரைக்கப்படுகிறது

### அறிவு முன்னோட்டங்கள்

- Python நிரலாக்கத்தின் அடிப்படை புரிதல்
- Command-line interfaces பற்றிய பரிச்சயம்
- AI/ML கருத்துக்கள் (மாதிரி மேம்பாட்டிற்காக) பற்றிய புரிதல்
- Git workflows மற்றும் pull request செயல்முறைகள்

## அமைப்பு கட்டளைகள்

### Repository அமைப்பு

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python மாதிரி அமைப்பு (Module08 மற்றும் Python மாதிரிகள்)

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

### Node.js மாதிரி அமைப்பு (மாதிரி 08 - Windows Chat App)

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

### Foundry Local அமைப்பு

Foundry Local மாதிரிகளை இயக்க தேவையானது. அதிகாரப்பூர்வ repository-யில் இருந்து பதிவிறக்கி நிறுவவும்:

**நிறுவல்:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manual**: [releases page](https://github.com/microsoft/Foundry-Local/releases) இல் இருந்து பதிவிறக்கவும்

**விரைவான தொடக்கம்:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-3.5-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**குறிப்பு**: Foundry Local உங்கள் hardware-க்கு சிறந்த மாடல் மாறுபாட்டை தானாக தேர்ந்தெடுக்கிறது (CUDA GPU, Qualcomm NPU, அல்லது CPU).

## மேம்பாட்டு வேலைகள்

### உள்ளடக்க மேம்பாடு

இந்த repository முக்கியமாக **Markdown கல்வி உள்ளடக்கத்தை** கொண்டுள்ளது. மாற்றங்களைச் செய்யும்போது:

1. சரியான module கோப்பகங்களில் `.md` கோப்புகளைத் திருத்தவும்
2. ஏற்கனவே உள்ள வடிவமைப்பு முறைகளை பின்பற்றவும்
3. கோடு உதாரணங்கள் சரியாகவும் சோதிக்கப்பட்டதாகவும் இருக்க வேண்டும்
4. தேவையானால் தொடர்புடைய மொழிபெயர்ப்பு உள்ளடக்கத்தை புதுப்பிக்கவும் (அல்லது automation அதைச் செய்ய அனுமதிக்கவும்)

### மாதிரி பயன்பாட்டு மேம்பாடு

Python மாதிரிகளுக்காக (மாதிரிகள் 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron மாதிரிக்காக (மாதிரி 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### மாதிரி பயன்பாடுகளை சோதனை செய்தல்

Python மாதிரிகளுக்கு automated tests இல்லை, ஆனால் அவற்றை இயக்குவதன் மூலம் சரிபார்க்கலாம்:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron மாதிரிக்கு சோதனை அமைப்பு உள்ளது:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## சோதனை வழிகாட்டுதல்கள்

### உள்ளடக்க சரிபார்ப்பு

இந்த repository automated translation workflows-ஐ பயன்படுத்துகிறது. மொழிபெயர்ப்புகளுக்கு கையேடு சோதனை தேவையில்லை.

**கையேடு சரிபார்ப்பு உள்ளடக்க மாற்றங்களுக்கு:**
1. `.md` கோப்புகளை முன்னோட்டமாகக் காண்பதன் மூலம் Markdown rendering-ஐ மதிப்பீடு செய்யவும்
2. அனைத்து இணைப்புகளும் செல்லுபடியாகும் இலக்குகளைச் சுட்டிக்காட்டுவதை உறுதிப்படுத்தவும்
3. ஆவணத்தில் உள்ள கோடு துணுக்குகளை சோதிக்கவும்
4. படங்கள் சரியாக ஏற்றப்படுவதைச் சரிபார்க்கவும்

### மாதிரி பயன்பாட்டு சோதனை

**Module08/samples/08 (Electron app) முழுமையான சோதனைகள் கொண்டுள்ளது:**
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

**Python மாதிரிகள் கையேடு சோதனை செய்யப்பட வேண்டும்:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## கோடு பாணி வழிகாட்டுதல்கள்

### Markdown உள்ளடக்கம்

- ஒரே மாதிரியான தலைப்பு வரிசையைப் பயன்படுத்தவும் (# தலைப்பு, ## முக்கிய பிரிவுகள், ### துணைப் பிரிவுகள்)
- மொழி குறிப்புகளுடன் கோடு துணுக்குகளைச் சேர்க்கவும்: ```python, ```bash, ```javascript
- அட்டவணைகள், பட்டியல்கள் மற்றும் வலியுறுத்தலுக்கான ஏற்கனவே உள்ள வடிவமைப்பைப் பின்பற்றவும்
- வரிகளை வாசிக்கக்கூடியதாக வைத்திருங்கள் (~80-100 எழுத்துகள், ஆனால் கடுமையானது அல்ல)
- உள்நாட்டு குறிப்புகளுக்கு சார்பு இணைப்புகளைப் பயன்படுத்தவும்

### Python கோடு பாணி

- PEP 8 விதிகளைப் பின்பற்றவும்
- தேவையான இடங்களில் வகை குறிப்புகளைப் பயன்படுத்தவும்
- செயல்பாடுகள் மற்றும் வகுப்புகளுக்கு docstrings சேர்க்கவும்
- பொருத்தமான மாறி பெயர்களைப் பயன்படுத்தவும்
- செயல்பாடுகளை கவனம் செலுத்திய மற்றும் சுருக்கமாக வைத்திருங்கள்

### JavaScript/Node.js கோடு பாணி

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**முக்கிய விதிகள்:**
- மாதிரி 08 இல் வழங்கப்பட்ட ESLint கட்டமைப்பு
- கோடு வடிவமைக்க Prettier
- ES6+ நவீன syntax-ஐப் பயன்படுத்தவும்
- கோட்பகுதியில் ஏற்கனவே உள்ள வடிவமைப்புகளைப் பின்பற்றவும்

## Pull Request வழிகாட்டுதல்கள்

### பங்களிப்பு வேலைகள்

1. **Repository-யை fork செய்யவும்** மற்றும் `main`-இல் இருந்து புதிய branch உருவாக்கவும்
2. **உங்கள் மாற்றங்களைச் செய்யவும்** கோடு பாணி வழிகாட்டுதல்களைப் பின்பற்றவும்
3. **மேலுமாக சோதிக்கவும்** மேலே உள்ள சோதனை வழிகாட்டுதல்களைப் பயன்படுத்தி
4. **தெளிவான செய்திகளுடன் commit செய்யவும்** வழக்கமான commit வடிவத்தைப் பின்பற்றவும்
5. **உங்கள் fork-க்கு push செய்யவும்** மற்றும் pull request உருவாக்கவும்
6. **Maintainers-இன் கருத்துக்களுக்கு பதிலளிக்கவும்** மதிப்பீட்டின் போது

### Branch பெயரிடும் விதிகள்

- `feature/<module>-<description>` - புதிய அம்சங்கள் அல்லது உள்ளடக்கம்
- `fix/<module>-<description>` - பிழை திருத்தங்கள்
- `docs/<description>` - ஆவண மேம்பாடுகள்
- `refactor/<description>` - கோடு மறுசீரமைப்பு

### Commit Message வடிவம்

[Conventional Commits](https://www.conventionalcommits.org/) ஐப் பின்பற்றவும்:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**உதாரணங்கள்:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### தலைப்பு வடிவம்
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### நடத்தை விதிகள்

அனைத்து பங்களிப்பாளர்களும் [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ஐப் பின்பற்ற வேண்டும். பங்களிப்பதற்கு முன் [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) ஐ மதிப்பீடு செய்யவும்.

### சமர்ப்பிப்பதற்கு முன்

**உள்ளடக்க மாற்றங்களுக்கு:**
- மாற்றியுள்ள அனைத்து Markdown கோப்புகளையும் முன்னோட்டமாகக் காண்பிக்கவும்
- இணைப்புகள் மற்றும் படங்கள் வேலை செய்கின்றன என்பதை உறுதிப்படுத்தவும்
- தட்டச்சு பிழைகள் மற்றும் இலக்கண பிழைகளைச் சரிபார்க்கவும்

**மாதிரி கோடு மாற்றங்களுக்கு (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python மாதிரி மாற்றங்களுக்கு:**
- மாதிரி வெற்றிகரமாக இயங்குகிறது என்பதைச் சோதிக்கவும்
- பிழை கையாளுதல் வேலை செய்கிறது என்பதை உறுதிப்படுத்தவும்
- Foundry Local உடன் இணக்கத்தன்மையைச் சரிபார்க்கவும்

### மதிப்பீட்டு செயல்முறை

- கல்வி உள்ளடக்க மாற்றங்கள் துல்லியத்திற்கும் தெளிவிற்கும் மதிப்பீடு செய்யப்படும்
- கோடு மாதிரிகள் செயல்பாட்டிற்காக சோதிக்கப்படும்
- மொழிபெயர்ப்பு புதுப்பிப்புகள் GitHub Actions மூலம் தானாகவே கையாளப்படும்

## மொழிபெயர்ப்பு அமைப்பு

**முக்கியம்:** இந்த repository GitHub Actions மூலம் automated translation ஐப் பயன்படுத்துகிறது.

- மொழிபெயர்ப்புகள் `/translations/` கோப்பகத்தில் உள்ளன (50+ மொழிகள்)
- `co-op-translator.yml` workflow மூலம் தானாகவே
- **மொழிபெயர்ப்பு கோப்புகளை கையேடு திருத்த வேண்டாம்** - அவை மீண்டும் எழுதப்படும்
- Root மற்றும் module கோப்பகங்களில் உள்ள ஆங்கில மூல கோப்புகளை மட்டுமே திருத்தவும்
- `main` branch-க்கு push செய்யும் போது மொழிபெயர்ப்புகள் தானாகவே உருவாக்கப்படும்

## Foundry Local ஒருங்கிணைப்பு

Module08 மாதிரிகள் பெரும்பாலும் Microsoft Foundry Local இயங்க வேண்டும்.

### நிறுவல் & அமைப்பு

**Foundry Local-ஐ நிறுவவும்:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK-ஐ நிறுவவும்:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local தொடங்குதல்
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

### SDK பயன்பாடு (Python)
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

### Foundry Local-ஐ சரிபார்த்தல்
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### மாதிரிகளுக்கான சூழல் மாறிகள்

பெரும்பாலான மாதிரிகள் இந்த சூழல் மாறிகளைப் பயன்படுத்துகின்றன:
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

**குறிப்பு**: `FoundryLocalManager` ஐப் பயன்படுத்தும்போது, SDK தானாகவே சேவை கண்டறிதல் மற்றும் மாடல் ஏற்றுதலை கையாளுகிறது. மாடல் alias-கள் (உதாரணமாக `phi-3.5-mini`) உங்கள் hardware-க்கு சிறந்த மாறுபாட்டை உறுதிப்படுத்துகின்றன.

## Build மற்றும் Deployment

### உள்ளடக்க Deployment

இந்த repository முக்கியமாக ஆவணமாகும் - உள்ளடக்கத்திற்கான build செயல்முறை தேவையில்லை.

### மாதிரி பயன்பாட்டு Build

**Electron பயன்பாடு (Module08/samples/08):**
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

**Python மாதிரிகள்:**
Build செயல்முறை இல்லை - மாதிரிகள் Python interpreter உடன் நேரடியாக இயக்கப்படுகின்றன.

## பொதுவான சிக்கல்கள் மற்றும் தீர்வுகள்

> **Tip**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) ஐச் சரிபார்க்கவும், அறியப்பட்ட பிரச்சினைகள் மற்றும் தீர்வுகளுக்காக.

### முக்கிய சிக்கல்கள் (தடைசெய்யும்)

#### Foundry Local இயங்கவில்லை
**சிக்கல்:** மாதிரிகள் இணைப்பு பிழைகளுடன் தோல்வியடைகின்றன

**தீர்வு:**
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

### பொதுவான சிக்கல்கள் (மிதமான)

#### Python Virtual Environment சிக்கல்கள்
**சிக்கல்:** Module import பிழைகள்

**தீர்வு:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron Build சிக்கல்கள்
**சிக்கல்:** npm install அல்லது build தோல்விகள்

**தீர்வு:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### வேலைகள் சிக்கல்கள் (சிறிய)

#### மொழிபெயர்ப்பு வேலைகள் முரண்பாடுகள்
**சிக்கல்:** மொழிபெயர்ப்பு PR உங்கள் மாற்றங்களுடன் முரண்படுகிறது

**தீர்வு:**
- ஆங்கில மூல கோப்புகளை மட்டுமே திருத்தவும்
- Automated translation workflow மொழிபெயர்ப்புகளை கையாள அனுமதிக்கவும்
- முரண்பாடுகள் ஏற்பட்டால், மொழிபெயர்ப்புகள் merge செய்யப்பட்ட பிறகு `main`-ஐ உங்கள் branch-க்கு merge செய்யவும்

#### மாடல் பதிவிறக்க தோல்விகள்
**சிக்கல்:** Foundry Local மாடல்களை பதிவிறக்க தோல்வியடைகிறது

**தீர்வு:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## கூடுதல் வளங்கள்

### கற்றல் பாதைகள்
- **ஆரம்ப பாதை:** Modules 01-02 (7-9 மணி நேரம்)
- **இடைநிலை பாதை:** Modules 03-04 (9-11 மணி நேரம்)
- **மேம்பட்ட பாதை:** Modules 05-07 (12-15 மணி நேரம்)
- **வல்லுநர் பாதை:** Module 08 (8-10 மணி நேரம்)

### முக்கிய Module உள்ளடக்கம்
- **Module01:** EdgeAI அடிப்படைகள் மற்றும் உண்மையான உலகக் கேஸ் ஸ்டடிகள்
- **Module02:** Small Language Model (SLM) குடும்பங்கள் மற்றும் கட்டமைப்புகள்
- **Module03:** உள்ளூர் மற்றும் cloud deployment உத்திகள்
- **Module04:** பல frameworks உடன் மாடல் optimization
- **Module05:** SLMOps - தயாரிப்பு செயல்பாடுகள்
- **Module06:** AI ஏஜென்ட்கள் மற்றும் செயல்பாடு அழைப்புகள்
- **Module07:** தளத்திற்கு குறிப்பிட்ட செயல்பாடுகள்
- **Module08:** Foundry Local toolkit மற்றும் 10 விரிவான மாதிரிகள்

### வெளிப்புற சார்புகள்
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI-இன் இணக்கமான API உடன் உள்ளூர் AI மாடல் runtime
  - [ஆவணம்](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimization framework
- [Microsoft Olive](https://microsoft.github.io/Olive/) - மாடல் optimization toolkit
- [OpenVINO](https://docs.openvino.ai/) - Intel-இன் optimization toolkit

## திட்டத்திற்கு குறிப்பிட்ட குறிப்புகள்

### Module08 மாதிரி பயன்பாடுகள்

இந்த repository 10 விரிவான மாதிரி பயன்பாடுகளை உள்ளடக்கியது:

1. **01-REST Chat Quickstart** - அடிப்படை OpenAI SDK ஒருங்கிணைப்பு
2. **02-OpenAI SDK Integration** - மேம்பட்ட SDK அம்சங்கள்
3. **03-Model Discovery & Benchmarking** - மாடல் ஒப்பீட்டு கருவிகள்
4. **04-Chainlit RAG Application** - Retrieval-augmented generation
5. **05-Multi-Agent Orchestration** - அடிப்படை ஏஜென்ட் ஒருங்கிணைப்பு
6. **06-Models-as-Tools Router** - புத்திசாலி மாடல் வழிமாற்று
7. **07-Direct API Client** - குறைந்த நில API ஒருங்கிணைப்பு
- உள்ளூர் முன்னறிவிப்பு 50-500ms பதில் நேரங்களை வழங்குகிறது  
- அளவீட்டு நுட்பங்கள் 75% அளவு குறைப்பை 85% செயல்திறன் தக்கவைத்தல் மூலம் அடைகின்றன  
- உள்ளூர் மாதிரிகளுடன் நேரடி உரையாடல் திறன்கள்  

### பாதுகாப்பு மற்றும் தனியுரிமை  

- அனைத்து செயலாக்கமும் உள்ளூரில் நடக்கிறது - தரவுகள் மேகத்துக்கு அனுப்பப்படுவதில்லை  
- தனியுரிமைக்கு முக்கியமான பயன்பாடுகளுக்கு பொருத்தமானது (மருத்துவம், நிதி)  
- தரவுச் சுயாதீனத்திற்கான தேவைகளை பூர்த்தி செய்கிறது  
- Foundry Local முழுவதும் உள்ளூர் ஹார்ட்வேரில் இயங்குகிறது  

## உதவி பெறுதல்  

### ஆவணங்கள்  

- **முக்கிய README**: [README.md](README.md) - களஞ்சியத்தின் மேற்பார்வை மற்றும் கற்றல் பாதைகள்  
- **ஆய்வு வழிகாட்டி**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - கற்றல் வளங்கள் மற்றும் காலக்கெடுகள்  
- **ஆதரவு**: [SUPPORT.md](SUPPORT.md) - உதவி பெறுவது எப்படி  
- **பாதுகாப்பு**: [SECURITY.md](SECURITY.md) - பாதுகாப்பு பிரச்சினைகளை அறிவிக்க  

### சமூக ஆதரவு  

- **GitHub Issues**: [பிழைகளை அறிவிக்க அல்லது அம்சங்களை கோருங்கள்](https://github.com/microsoft/edgeai-for-beginners/issues)  
- **GitHub Discussions**: [கேள்விகளை கேளுங்கள் மற்றும் யோசனைகளை பகிருங்கள்](https://github.com/microsoft/edgeai-for-beginners/discussions)  
- **Foundry Local Issues**: [Foundry Local தொடர்பான தொழில்நுட்ப பிரச்சினைகள்](https://github.com/microsoft/Foundry-Local/issues)  

### தொடர்பு  

- **பராமரிப்பாளர்கள்**: [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS) ஐப் பார்க்கவும்  
- **பாதுகாப்பு பிரச்சினைகள்**: [SECURITY.md](SECURITY.md) இல் பொறுப்பான வெளிப்பாட்டை பின்பற்றவும்  
- **Microsoft ஆதரவு**: நிறுவன ஆதரவுக்கு, Microsoft வாடிக்கையாளர் சேவையை தொடர்பு கொள்ளவும்  

### கூடுதல் வளங்கள்  

- **Microsoft Learn**: [AI மற்றும் இயந்திர கற்றல் கற்றல் பாதைகள்](https://learn.microsoft.com/training/browse/?products=ai-services)  
- **Foundry Local ஆவணங்கள்**: [அதிகாரப்பூர்வ ஆவணங்கள்](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)  
- **சமூக மாதிரிகள்**: சமூக பங்களிப்புகளுக்கான [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) ஐச் சரிபார்க்கவும்  

---

**இது Edge AI மேம்பாட்டத்தை கற்பதற்கான கல்வி களஞ்சியம் ஆகும். முக்கிய பங்களிப்பு முறை கல்வி உள்ளடக்கத்தை மேம்படுத்துதல் மற்றும் Edge AI கருத்துக்களை விளக்கும் மாதிரிப் பயன்பாடுகளை சேர்த்தல்/மேம்படுத்தல் ஆகும்.**  

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.