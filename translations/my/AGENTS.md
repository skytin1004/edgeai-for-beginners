<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:47:09+00:00",
  "source_file": "AGENTS.md",
  "language_code": "my"
}
-->
# AGENTS.md

## ပရောဂျက်အကျဉ်းချုပ်

EdgeAI for Beginners သည် Small Language Models (SLMs) ကို အသုံးပြု၍ Edge AI ဖွံ့ဖြိုးတိုးတက်မှုကို သင်ကြားပေးသည့် ပညာရေးဆိုင်ရာ repository တစ်ခုဖြစ်သည်။ ဒီသင်တန်းတွင် EdgeAI အခြေခံအကြောင်းအရာများ၊ မော်ဒယ်များကို အသုံးချခြင်း၊ အထူးပြုနည်းလမ်းများနှင့် Microsoft Foundry Local နှင့် အမျိုးမျိုးသော AI frameworks များကို အသုံးပြု၍ ထုတ်လုပ်မှုအဆင်သင့် အကောင်အထည်ဖော်မှုများကို လေ့လာနိုင်ပါသည်။

**အဓိကနည်းပညာများ:**
- Python 3.8+ (AI/ML နမူနာများအတွက် အဓိက programming language)
- .NET C# (AI/ML နမူနာများ)
- JavaScript/Node.js နှင့် Electron (desktop applications အတွက်)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI Frameworks: LangChain, Semantic Kernel, Chainlit
- Model Optimization: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repository အမျိုးအစား:** ပညာရေးဆိုင်ရာ အကြောင်းအရာများပါဝင်သော repository (8 modules နှင့် 10 နမူနာ applications)

**Architecture:** Edge AI deployment patterns ကို လက်တွေ့နမူနာများဖြင့် ပြသထားသော multi-module learning path

## Repository ဖွဲ့စည်းပုံ

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

## Setup Commands

### Repository Setup

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python Sample Setup (Module08 နှင့် Python နမူနာများ)

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

### Node.js Sample Setup (Sample 08 - Windows Chat App)

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

### Foundry Local Setup

Module08 နမူနာများကို run လုပ်ရန် Foundry Local လိုအပ်ပါသည်။

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## ဖွံ့ဖြိုးတိုးတက်မှုလုပ်ငန်းစဉ်

### အကြောင်းအရာ ဖွံ့ဖြိုးတိုးတက်မှု

ဒီ repository တွင် အဓိကအားဖြင့် **Markdown ပညာရေးဆိုင်ရာ အကြောင်းအရာများ** ပါဝင်သည်။ ပြင်ဆင်မှုများလုပ်ဆောင်သောအခါ:

1. `.md` ဖိုင်များကို သင့် module directories မှာ ပြင်ဆင်ပါ
2. ရှိပြီးသား formatting ပုံစံများကို လိုက်နာပါ
3. Code နမူနာများကို မှန်ကန်မှုနှင့် စမ်းသပ်ပြီးကြောင်း သေချာပါ
4. လိုအပ်ပါက ဘာသာပြန်ထားသော အကြောင်းအရာများကို update လုပ်ပါ (သို့မဟုတ် automation ကို အားထားပါ)

### နမူနာ Application ဖွံ့ဖြိုးတိုးတက်မှု

Python နမူနာများအတွက် (samples 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron နမူနာအတွက် (sample 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### နမူနာ Applications စမ်းသပ်ခြင်း

Python နမူနာများတွင် automated tests မပါဝင်ပါ၊ သို့သော် run လုပ်ခြင်းဖြင့် စစ်ဆေးနိုင်ပါသည်။
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron နမူနာတွင် စမ်းသပ်မှု infrastructure ပါဝင်သည်။
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## စမ်းသပ်မှုညွှန်ကြားချက်များ

### အကြောင်းအရာ အတည်ပြုခြင်း

Repository တွင် automated translation workflows ကို အသုံးပြုထားသည်။ ဘာသာပြန်မှုများအတွက် လက်တွေ့စမ်းသပ်မှုမလိုအပ်ပါ။

**Manual validation အတွက်:**
1. `.md` ဖိုင်များကို preview လုပ်၍ Markdown rendering ကို စစ်ဆေးပါ
2. Links များမှန်ကန်သော target များကို ရောက်ရှိကြောင်း သေချာပါ
3. Documentation တွင်ပါဝင်သော code snippets များကို စမ်းသပ်ပါ
4. ပုံများမှန်ကန်စွာ load ဖြစ်ကြောင်း စစ်ဆေးပါ

### နမူနာ Application စမ်းသပ်ခြင်း

**Module08/samples/08 (Electron app) တွင် စုံလင်သော စမ်းသပ်မှုများပါဝင်သည်။**
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

**Python နမူနာများကို လက်တွေ့စမ်းသပ်ရမည်။**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Code Style Guidelines

### Markdown အကြောင်းအရာ

- Heading hierarchy ကို တိကျစွာ အသုံးပြုပါ (# for title, ## for main sections, ### for subsections)
- Code blocks တွင် language specifiers ပါဝင်စေရန်: ```python, ```bash, ```javascript
- Tables, lists, နှင့် emphasis အတွက် ရှိပြီးသား formatting ကို လိုက်နာပါ
- လိုင်းများကို ဖတ်ရှုရလွယ်ကူစေရန် (~80-100 characters) ထိန်းသိမ်းပါ
- Internal references အတွက် relative links ကို အသုံးပြုပါ

### Python Code Style

- PEP 8 conventions ကို လိုက်နာပါ
- လိုအပ်သောနေရာများတွင် type hints ကို အသုံးပြုပါ
- Functions နှင့် classes အတွက် docstrings ထည့်ပါ
- အဓိကအကြောင်းအရာကို ဖော်ပြသော variable names ကို အသုံးပြုပါ
- Functions များကို အကျဉ်းချုပ်ထားပြီး အဓိကအကြောင်းအရာကို အာရုံစိုက်ပါ

### JavaScript/Node.js Code Style

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**အဓိကအချက်များ:**
- ESLint configuration ကို sample 08 တွင် ပေးထားသည်
- Prettier ကို code formatting အတွက် အသုံးပြုပါ
- ES6+ syntax ကို အသုံးပြုပါ
- Codebase တွင် ရှိပြီးသား patterns များကို လိုက်နာပါ

## Pull Request Guidelines

### Title Format
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### Submit မလုပ်မီ

**အကြောင်းအရာ ပြင်ဆင်မှုများအတွက်:**
- Markdown ဖိုင်များကို preview လုပ်ပါ
- Links နှင့် images မှန်ကန်ကြောင်း စစ်ဆေးပါ
- စာလုံးပေါင်းနှင့် သဒ္ဒါအမှားများကို စစ်ဆေးပါ

**နမူနာ code ပြင်ဆင်မှုများအတွက် (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python နမူနာများအတွက်:**
- နမူနာကို run လုပ်၍ အောင်မြင်ကြောင်း စစ်ဆေးပါ
- Error handling မှန်ကန်ကြောင်း စစ်ဆေးပါ
- Foundry Local နှင့် အညီဖြစ်ကြောင်း စစ်ဆေးပါ

### Review လုပ်ငန်းစဉ်

- ပညာရေးဆိုင်ရာ အကြောင်းအရာ ပြင်ဆင်မှုများကို မှန်ကန်မှုနှင့် ရှင်းလင်းမှုအတွက် စစ်ဆေးပါ
- Code နမူနာများကို လုပ်ဆောင်မှုအတွက် စမ်းသပ်ပါ
- Translation updates များကို GitHub Actions မှ automatic handle လုပ်ပါ

## Translation System

**အရေးကြီး:** ဒီ repository တွင် GitHub Actions မှ automated translation ကို အသုံးပြုထားသည်။

- Translations များကို `/translations/` directory တွင် သိမ်းဆည်းထားသည် (50+ ဘာသာစကား)
- `co-op-translator.yml` workflow မှ automated ဖြစ်သည်
- **ဘာသာပြန်ဖိုင်များကို လက်တွေ့ပြင်ဆင်မလုပ်ပါနှင့်** - အလိုအလျောက် overwrite ဖြစ်မည်
- Root နှင့် module directories တွင် English source files ကိုသာ ပြင်ဆင်ပါ
- `main` branch သို့ push လုပ်သောအခါ ဘာသာပြန်မှုများကို အလိုအလျောက် ဖန်တီးမည်

## Foundry Local Integration

Module08 နမူနာများအများစုတွင် Microsoft Foundry Local ကို run လုပ်ရန် လိုအပ်ပါသည်။

### Foundry Local စတင်ခြင်း
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

### Foundry Local အတည်ပြုခြင်း
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### နမူနာများအတွက် Environment Variables

နမူနာများအများစုတွင် အောက်ပါ environment variables များကို အသုံးပြုသည်။
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

## Build နှင့် Deployment

### အကြောင်းအရာ Deployment

ဒီ repository သည် documentation အဓိကဖြစ်သောကြောင့် အကြောင်းအရာအတွက် build လုပ်စရာမလိုအပ်ပါ။

### နမူနာ Application Build လုပ်ခြင်း

**Electron Application (Module08/samples/08):**
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

**Python နမူနာများ:**
Build လုပ်စရာမလိုအပ်ပါ - Python interpreter ဖြင့် တိုက်ရိုက် run လုပ်နိုင်သည်။

## အများဆုံးတွေ့ရသော ပြဿနာများနှင့် ဖြေရှင်းနည်းများ

### Foundry Local မ run လုပ်ခြင်း
**ပြဿနာ:** Connection errors ဖြင့် နမူနာများ fail ဖြစ်သည်

**ဖြေရှင်းနည်း:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python Virtual Environment ပြဿနာများ
**ပြဿနာ:** Module import errors

**ဖြေရှင်းနည်း:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron Build ပြဿနာများ
**ပြဿနာ:** npm install သို့မဟုတ် build fail ဖြစ်သည်

**ဖြေရှင်းနည်း:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Translation Workflow Conflicts
**ပြဿနာ:** Translation PR သင့်ပြင်ဆင်မှုများနှင့် conflict ဖြစ်သည်

**ဖြေရှင်းနည်း:**
- English source files ကိုသာ ပြင်ဆင်ပါ
- Automated translation workflow ကို အားထားပါ
- Conflict ဖြစ်ပါက translation merge ပြီးနောက် `main` ကို သင့် branch ထဲ merge လုပ်ပါ

## အပိုဆောင်း အရင်းအမြစ်များ

### Learning Paths
- **Beginner Path:** Modules 01-02 (7-9 နာရီ)
- **Intermediate Path:** Modules 03-04 (9-11 နာရီ)
- **Advanced Path:** Modules 05-07 (12-15 နာရီ)
- **Expert Path:** Module 08 (8-10 နာရီ)

### အဓိက Module အကြောင်းအရာ
- **Module01:** EdgeAI အခြေခံနှင့် အမှန်တကယ် case studies
- **Module02:** Small Language Model (SLM) များ၏ မျိုးစဉ်နှင့် architecture
- **Module03:** Local နှင့် cloud deployment strategies
- **Module04:** Framework များစွာဖြင့် Model optimization
- **Module05:** SLMOps - production operations
- **Module06:** AI agents နှင့် function calling
- **Module07:** Platform-specific implementations
- **Module08:** Foundry Local toolkit နှင့် 10 comprehensive samples

### အပြင်ပေါ် Dependencies
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Local AI model runtime
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimization framework
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Model optimization toolkit
- [OpenVINO](https://docs.openvino.ai/) - Intel's optimization toolkit

## Project-Specific Notes

### Module08 နမူနာ Applications

Repository တွင် 10 comprehensive နမူနာ applications ပါဝင်သည်။

1. **01-REST Chat Quickstart** - OpenAI SDK integration အခြေခံ
2. **02-OpenAI SDK Integration** - အဆင့်မြင့် SDK features
3. **03-Model Discovery & Benchmarking** - Model comparison tools
4. **04-Chainlit RAG Application** - Retrieval-augmented generation
5. **05-Multi-Agent Orchestration** - Agent coordination အခြေခံ
6. **06-Models-as-Tools Router** - Intelligent model routing
7. **07-Direct API Client** - Low-level API integration
8. **08-Windows 11 Chat App** - Native Electron desktop application
9. **09-Advanced Multi-Agent System** - Agent orchestration အဆင့်မြင့်
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel integration

နမူနာတစ်ခုစီသည် Foundry Local ဖြင့် Edge AI ဖွံ့ဖြိုးတိုးတက်မှု၏ အမျိုးမျိုးသော အချက်များကို ပြသထားသည်။

### Performance အချက်များ

- SLMs များကို edge deployment အတွက် optimize လုပ်ထားသည် (2-16GB RAM)
- Local inference မှာ 50-500ms response times ရရှိသည်
- Quantization နည်းလမ်းများသည် 75% size reduction နှင့် 85% performance retention ရရှိစေသည်
- Local models ဖြင့် အချိန်နှင့်တပြေးညီ စကားဝိုင်း capabilities ရရှိနိုင်သည်

### လုံခြုံရေးနှင့် ကိုယ်ရေးအချက်အလက်

- အားလုံးကို locally process လုပ်သည် - cloud သို့ data မပို့ပါ
- Privacy-sensitive applications (healthcare, finance) အတွက် သင့်လျော်သည်
- Data sovereignty လိုအပ်ချက်များကို ဖြည့်ဆည်းပေးသည်
- Foundry Local သည် အပြည့်အဝ local hardware ပေါ်တွင် run လုပ်သည်

---

**ဒီ repository သည် Edge AI ဖွံ့ဖြိုးတိုးတက်မှုကို သင်ကြားပေးရန် အဓိကထားသော ပညာရေးဆိုင်ရာ repository ဖြစ်သည်။ အဓိကအထောက်အပံ့ပုံစံမှာ ပညာရေးဆိုင်ရာ အကြောင်းအရာများကို တိုးတက်အောင် ပြင်ဆင်ခြင်းနှင့် Edge AI အကြောင်းအရာများကို ပြသထားသော နမူနာ applications များကို ထည့်သွင်းခြင်းဖြစ်သည်။**

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။