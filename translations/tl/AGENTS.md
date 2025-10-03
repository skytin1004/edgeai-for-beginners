<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:41:07+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tl"
}
-->
# AGENTS.md

## Pangkalahatang-ideya ng Proyekto

Ang EdgeAI for Beginners ay isang komprehensibong repositoryo pang-edukasyon na nagtuturo ng pag-develop ng Edge AI gamit ang Small Language Models (SLMs). Saklaw ng kurso ang mga pangunahing kaalaman sa EdgeAI, pag-deploy ng modelo, mga teknik sa pag-optimize, at mga implementasyong handa para sa produksyon gamit ang Microsoft Foundry Local at iba't ibang AI frameworks.

**Pangunahing Teknolohiya:**
- Python 3.8+ (pangunahing wika para sa mga AI/ML sample)
- .NET C# (AI/ML Samples)
- JavaScript/Node.js gamit ang Electron (para sa mga desktop application)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI Frameworks: LangChain, Semantic Kernel, Chainlit
- Pag-optimize ng Modelo: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Uri ng Repositoryo:** Repositoryo ng nilalamang pang-edukasyon na may 8 modules at 10 komprehensibong sample na aplikasyon

**Arkitektura:** Multi-module na landas sa pag-aaral na may mga praktikal na sample na nagpapakita ng mga pattern sa pag-deploy ng edge AI

## Estruktura ng Repositoryo

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

## Mga Command sa Setup

### Setup ng Repositoryo

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Setup ng Python Sample (Module08 at Python samples)

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

### Setup ng Node.js Sample (Sample 08 - Windows Chat App)

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

### Setup ng Foundry Local

Kinakailangan ang Foundry Local upang patakbuhin ang mga sample ng Module08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Workflow ng Pag-develop

### Pag-develop ng Nilalaman

Ang repositoryong ito ay pangunahing naglalaman ng **Markdown na nilalamang pang-edukasyon**. Kapag gumagawa ng mga pagbabago:

1. I-edit ang mga `.md` file sa tamang direktoryo ng module
2. Sundin ang umiiral na mga pattern ng format
3. Siguraduhing tama at nasubukan ang mga halimbawa ng code
4. I-update ang kaukulang nilalamang isinalin kung kinakailangan (o hayaan ang automation na gawin ito)

### Pag-develop ng Sample na Aplikasyon

Para sa mga Python sample (samples 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Para sa Electron sample (sample 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Pagsubok ng Sample na Aplikasyon

Ang mga Python sample ay walang automated na pagsubok ngunit maaaring ma-validate sa pamamagitan ng pagpapatakbo ng mga ito:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Ang Electron sample ay may test infrastructure:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Mga Tagubilin sa Pagsubok

### Pag-validate ng Nilalaman

Ang repositoryo ay gumagamit ng automated na workflows para sa pagsasalin. Walang kinakailangang manual na pagsubok para sa mga pagsasalin.

**Manual na pag-validate para sa mga pagbabago sa nilalaman:**
1. I-preview ang rendering ng Markdown sa pamamagitan ng pagtingin sa mga `.md` file
2. Siguraduhing lahat ng link ay tumuturo sa tamang target
3. Subukan ang anumang code snippets na kasama sa dokumentasyon
4. Siguraduhing tama ang pag-load ng mga imahe

### Pagsubok ng Sample na Aplikasyon

**Module08/samples/08 (Electron app) ay may komprehensibong pagsubok:**
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

**Ang mga Python sample ay dapat manual na subukan:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Mga Alituntunin sa Estilo ng Code

### Nilalaman ng Markdown

- Gumamit ng pare-parehong hierarchy ng heading (# para sa pamagat, ## para sa mga pangunahing seksyon, ### para sa mga subseksyon)
- Isama ang mga code block na may language specifiers: ```python, ```bash, ```javascript
- Sundin ang umiiral na format para sa mga talahanayan, listahan, at emphasis
- Panatilihing nababasa ang mga linya (hanggang ~80-100 characters, ngunit hindi mahigpit)
- Gumamit ng relative links para sa mga internal na reference

### Estilo ng Python Code

- Sundin ang mga convention ng PEP 8
- Gumamit ng type hints kung naaangkop
- Isama ang mga docstring para sa mga function at klase
- Gumamit ng makabuluhang pangalan ng variable
- Panatilihing nakatuon at maikli ang mga function

### Estilo ng JavaScript/Node.js Code

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Pangunahing mga convention:**
- ESLint configuration na ibinigay sa sample 08
- Prettier para sa pag-format ng code
- Gumamit ng modernong ES6+ syntax
- Sundin ang umiiral na mga pattern sa codebase

## Mga Alituntunin sa Pull Request

### Format ng Pamagat
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### Bago Mag-submit

**Para sa mga pagbabago sa nilalaman:**
- I-preview ang lahat ng binagong Markdown files
- Siguraduhing gumagana ang mga link at imahe
- Suriin ang mga typo at grammatical errors

**Para sa mga pagbabago sa sample na code (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Para sa mga pagbabago sa Python sample:**
- Subukan ang sample na matagumpay na tumatakbo
- Siguraduhing gumagana ang error handling
- Suriin ang compatibility sa Foundry Local

### Proseso ng Review

- Ang mga pagbabago sa nilalamang pang-edukasyon ay sinusuri para sa katumpakan at kalinawan
- Ang mga sample na code ay sinusubukan para sa functionality
- Ang mga update sa pagsasalin ay awtomatikong hinahawakan ng GitHub Actions

## Sistema ng Pagsasalin

**MAHALAGA:** Ang repositoryong ito ay gumagamit ng automated na pagsasalin sa pamamagitan ng GitHub Actions.

- Ang mga pagsasalin ay nasa direktoryo ng `/translations/` (50+ na wika)
- Awtomatikong ginagawa sa `co-op-translator.yml` workflow
- **HUWAG manual na i-edit ang mga file ng pagsasalin** - sila ay awtomatikong maa-overwrite
- I-edit lamang ang mga English source files sa root at module directories
- Ang mga pagsasalin ay awtomatikong nabubuo kapag nag-push sa `main` branch

## Integrasyon ng Foundry Local

Karamihan sa mga sample ng Module08 ay nangangailangan ng Microsoft Foundry Local na tumatakbo:

### Pagsisimula ng Foundry Local
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

### Pag-verify ng Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Mga Environment Variable para sa Mga Sample

Karamihan sa mga sample ay gumagamit ng mga environment variable na ito:
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

## Pagbuo at Pag-deploy

### Pag-deploy ng Nilalaman

Ang repositoryong ito ay pangunahing dokumentasyon - walang kinakailangang proseso ng pagbuo para sa nilalaman.

### Pagbuo ng Sample na Aplikasyon

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

**Python Samples:**
Walang proseso ng pagbuo - ang mga sample ay direktang pinapatakbo gamit ang Python interpreter.

## Karaniwang Isyu at Pag-troubleshoot

### Foundry Local Hindi Tumatakbo
**Isyu:** Nabigo ang mga sample na may mga error sa koneksyon

**Solusyon:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Mga Isyu sa Python Virtual Environment
**Isyu:** Mga error sa pag-import ng module

**Solusyon:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Mga Isyu sa Electron Build
**Isyu:** npm install o mga pagkabigo sa pagbuo

**Solusyon:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Mga Konflikto sa Workflow ng Pagsasalin
**Isyu:** Ang Translation PR ay nagkakaroon ng conflict sa iyong mga pagbabago

**Solusyon:**
- I-edit lamang ang mga English source files
- Hayaan ang automated na workflow ng pagsasalin na hawakan ang mga pagsasalin
- Kung may mga conflict, i-merge ang `main` sa iyong branch pagkatapos ma-merge ang mga pagsasalin

## Karagdagang Mga Mapagkukunan

### Mga Landas sa Pag-aaral
- **Beginner Path:** Modules 01-02 (7-9 oras)
- **Intermediate Path:** Modules 03-04 (9-11 oras)
- **Advanced Path:** Modules 05-07 (12-15 oras)
- **Expert Path:** Module 08 (8-10 oras)

### Pangunahing Nilalaman ng Module
- **Module01:** Mga pangunahing kaalaman sa EdgeAI at mga case study sa totoong mundo
- **Module02:** Mga pamilya at arkitektura ng Small Language Model (SLM)
- **Module03:** Mga estratehiya sa pag-deploy sa lokal at cloud
- **Module04:** Pag-optimize ng modelo gamit ang maraming frameworks
- **Module05:** SLMOps - mga operasyon sa produksyon
- **Module06:** Mga AI agents at function calling
- **Module07:** Mga implementasyon na partikular sa platform
- **Module08:** Foundry Local toolkit na may 10 komprehensibong sample

### Mga Panlabas na Dependency
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Lokal na runtime ng AI model
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Framework para sa pag-optimize
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Toolkit para sa pag-optimize ng modelo
- [OpenVINO](https://docs.openvino.ai/) - Toolkit ng Intel para sa pag-optimize

## Mga Tala na Partikular sa Proyekto

### Mga Sample na Aplikasyon ng Module08

Ang repositoryo ay naglalaman ng 10 komprehensibong sample na aplikasyon:

1. **01-REST Chat Quickstart** - Pangunahing integrasyon ng OpenAI SDK
2. **02-OpenAI SDK Integration** - Mga advanced na feature ng SDK
3. **03-Model Discovery & Benchmarking** - Mga tool sa paghahambing ng modelo
4. **04-Chainlit RAG Application** - Retrieval-augmented generation
5. **05-Multi-Agent Orchestration** - Pangunahing koordinasyon ng agent
6. **06-Models-as-Tools Router** - Matalinong pag-route ng modelo
7. **07-Direct API Client** - Low-level na integrasyon ng API
8. **08-Windows 11 Chat App** - Native Electron desktop application
9. **09-Advanced Multi-Agent System** - Kumplikadong koordinasyon ng agent
10. **10-Foundry Tools Framework** - Integrasyon ng LangChain/Semantic Kernel

Ang bawat sample ay nagpapakita ng iba't ibang aspeto ng pag-develop ng edge AI gamit ang Foundry Local.

### Mga Pagsasaalang-alang sa Performance

- Ang mga SLM ay na-optimize para sa edge deployment (2-16GB RAM)
- Ang lokal na inference ay nagbibigay ng 50-500ms na response times
- Ang mga teknik sa quantization ay nakakamit ng 75% na pagbawas sa laki na may 85% na retention ng performance
- Mga kakayahan sa real-time na pag-uusap gamit ang mga lokal na modelo

### Seguridad at Privacy

- Lahat ng pagproseso ay nangyayari nang lokal - walang data na ipinapadala sa cloud
- Angkop para sa mga aplikasyon na sensitibo sa privacy (healthcare, finance)
- Tumutugon sa mga kinakailangan sa data sovereignty
- Ang Foundry Local ay ganap na tumatakbo sa lokal na hardware

---

**Ito ay isang repositoryong pang-edukasyon na nakatuon sa pagtuturo ng pag-develop ng Edge AI. Ang pangunahing pattern ng kontribusyon ay ang pagpapabuti ng nilalamang pang-edukasyon at ang pagdaragdag/pagpapahusay ng mga sample na aplikasyon na nagpapakita ng mga konsepto ng Edge AI.**

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.