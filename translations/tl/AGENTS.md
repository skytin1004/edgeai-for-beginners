<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "135b2658979f1e494bb0ecc6e26d4752",
  "translation_date": "2025-10-09T19:07:33+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tl"
}
-->
# AGENTS.md

> **Gabay para sa mga Developer sa Pagsali sa EdgeAI para sa mga Baguhan**
> 
> Ang dokumentong ito ay nagbibigay ng komprehensibong impormasyon para sa mga developer, AI agents, at mga kontribyutor na nagtatrabaho sa repositoryong ito. Sinasaklaw nito ang setup, mga workflow sa pag-develop, testing, at mga pinakamahusay na kasanayan.
> 
> **Huling Na-update**: Oktubre 2025 | **Bersyon ng Dokumento**: 2.0

## Talaan ng Nilalaman

- [Pangkalahatang-ideya ng Proyekto](../..)
- [Istruktura ng Repositoryo](../..)
- [Mga Kinakailangan](../..)
- [Mga Utos sa Setup](../..)
- [Workflow sa Pag-develop](../..)
- [Mga Tagubilin sa Pagsusuri](../..)
- [Mga Alituntunin sa Estilo ng Code](../..)
- [Mga Alituntunin sa Pull Request](../..)
- [Sistema ng Pagsasalin](../..)
- [Integrasyon ng Foundry Local](../..)
- [Pagbuo at Pag-deploy](../..)
- [Mga Karaniwang Isyu at Pag-troubleshoot](../..)
- [Karagdagang Mga Mapagkukunan](../..)
- [Mga Tala na Tiyak sa Proyekto](../..)
- [Pagkuha ng Tulong](../..)

## Pangkalahatang-ideya ng Proyekto

Ang EdgeAI para sa mga Baguhan ay isang komprehensibong repositoryo ng edukasyon na nagtuturo ng pag-develop ng Edge AI gamit ang Small Language Models (SLMs). Sinasaklaw ng kurso ang mga pangunahing kaalaman sa EdgeAI, pag-deploy ng modelo, mga teknik sa pag-optimize, at mga implementasyong handa sa produksyon gamit ang Microsoft Foundry Local at iba't ibang AI frameworks.

**Pangunahing Teknolohiya:**
- Python 3.8+ (pangunahing wika para sa mga halimbawa ng AI/ML)
- .NET C# (mga halimbawa ng AI/ML)
- JavaScript/Node.js gamit ang Electron (para sa mga desktop application)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI Frameworks: LangChain, Semantic Kernel, Chainlit
- Pag-optimize ng Modelo: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Uri ng Repositoryo:** Repositoryo ng nilalamang pang-edukasyon na may 8 modules at 10 komprehensibong sample na aplikasyon

**Arkitektura:** Multi-module na landas ng pag-aaral na may mga praktikal na halimbawa na nagpapakita ng mga pattern ng pag-deploy ng edge AI

## Istruktura ng Repositoryo

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

## Mga Kinakailangan

### Mga Kinakailangang Tool

- **Python 3.8+** - Para sa mga halimbawa ng AI/ML at notebooks
- **Node.js 16+** - Para sa Electron sample application
- **Git** - Para sa version control
- **Microsoft Foundry Local** - Para sa pagpapatakbo ng mga AI model nang lokal

### Inirerekomendang Mga Tool

- **Visual Studio Code** - Gamit ang Python, Jupyter, at Pylance extensions
- **Windows Terminal** - Para sa mas magandang karanasan sa command-line (Windows users)
- **Docker** - Para sa containerized development (opsyonal)

### Mga Kinakailangan sa Sistema

- **RAM**: Minimum na 8GB, inirerekomenda ang 16GB+ para sa multi-model scenarios
- **Storage**: 10GB+ libreng espasyo para sa mga modelo at dependencies
- **OS**: Windows 10/11, macOS 11+, o Linux (Ubuntu 20.04+)
- **Hardware**: CPU na may AVX2 support; GPU (CUDA, Qualcomm NPU) opsyonal ngunit inirerekomenda

### Mga Kinakailangang Kaalaman

- Pangunahing kaalaman sa Python programming
- Pamilyar sa mga command-line interface
- Pag-unawa sa mga konsepto ng AI/ML (para sa pag-develop ng mga halimbawa)
- Mga workflow ng Git at proseso ng pull request

## Mga Utos sa Setup

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

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
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

Kinakailangan ang Foundry Local upang patakbuhin ang mga halimbawa. I-download at i-install mula sa opisyal na repositoryo:

**Pag-install:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manwal**: I-download mula sa [releases page](https://github.com/microsoft/Foundry-Local/releases)

**Mabilis na Simula:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-3.5-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Tandaan**: Awtomatikong pinipili ng Foundry Local ang pinakamahusay na variant ng modelo para sa iyong hardware (CUDA GPU, Qualcomm NPU, o CPU).

## Workflow sa Pag-develop

### Pag-develop ng Nilalaman

Ang repositoryong ito ay pangunahing naglalaman ng **Markdown educational content**. Kapag gumagawa ng mga pagbabago:

1. I-edit ang mga `.md` file sa tamang module directories
2. Sundin ang umiiral na mga pattern ng pag-format
3. Siguraduhing tama at nasubukan ang mga halimbawa ng code
4. I-update ang kaukulang isinaling nilalaman kung kinakailangan (o hayaan ang automation na gawin ito)

### Pag-develop ng Sample Application

Para sa mga Python samples (samples 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Para sa Electron sample (sample 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Pagsusuri ng Sample Applications

Walang automated tests ang Python samples ngunit maaaring ma-validate sa pamamagitan ng pagpapatakbo ng mga ito:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

May test infrastructure ang Electron sample:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Mga Tagubilin sa Pagsusuri

### Pag-validate ng Nilalaman

Gumagamit ang repositoryo ng automated translation workflows. Walang kinakailangang manwal na pagsusuri para sa mga pagsasalin.

**Manwal na pag-validate para sa mga pagbabago sa nilalaman:**
1. Suriin ang Markdown rendering sa pamamagitan ng pag-preview ng `.md` files
2. Siguraduhing lahat ng link ay tumutukoy sa tamang destinasyon
3. Subukan ang anumang code snippets na kasama sa dokumentasyon
4. Tiyaking tama ang pag-load ng mga imahe

### Pagsusuri ng Sample Application

**Ang Module08/samples/08 (Electron app) ay may komprehensibong pagsusuri:**
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

**Ang Python samples ay dapat manwal na masuri:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Mga Alituntunin sa Estilo ng Code

### Markdown Content

- Gumamit ng pare-parehong hierarchy ng heading (# para sa pamagat, ## para sa pangunahing seksyon, ### para sa subseksyon)
- Isama ang mga code block na may language specifiers: ```python, ```bash, ```javascript
- Sundin ang umiiral na pag-format para sa mga talahanayan, listahan, at pag-emphasize
- Panatilihing nababasa ang mga linya (layunin ang ~80-100 characters, ngunit hindi mahigpit)
- Gumamit ng relative links para sa mga internal na reference

### Estilo ng Python Code

- Sundin ang PEP 8 conventions
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

**Pangunahing conventions:**
- May ESLint configuration sa sample 08
- Prettier para sa pag-format ng code
- Gumamit ng modernong ES6+ syntax
- Sundin ang umiiral na mga pattern sa codebase

## Mga Alituntunin sa Pull Request

### Workflow ng Kontribusyon

1. **I-fork ang repositoryo** at gumawa ng bagong branch mula sa `main`
2. **Gawin ang iyong mga pagbabago** ayon sa mga alituntunin sa estilo ng code
3. **Subukang mabuti** gamit ang mga tagubilin sa pagsusuri sa itaas
4. **Mag-commit na may malinaw na mensahe** ayon sa conventional commits format
5. **I-push sa iyong fork** at gumawa ng pull request
6. **Tumugon sa feedback** mula sa mga maintainer sa panahon ng review

### Convention sa Pangalan ng Branch

- `feature/<module>-<description>` - Para sa mga bagong feature o nilalaman
- `fix/<module>-<description>` - Para sa mga bug fix
- `docs/<description>` - Para sa mga pagpapabuti sa dokumentasyon
- `refactor/<description>` - Para sa refactoring ng code

### Format ng Mensahe ng Commit

Sundin ang [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Mga Halimbawa:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Format ng Pamagat
```
[ModuleXX] Brief description of change
```
o
```
[Module08/samples/XX] Description for sample changes
```

### Code of Conduct

Lahat ng kontribyutor ay dapat sumunod sa [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Mangyaring suriin ang [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) bago mag-ambag.

### Bago Mag-sumite

**Para sa mga pagbabago sa nilalaman:**
- I-preview ang lahat ng binagong Markdown files
- Siguraduhing gumagana ang mga link at imahe
- Suriin ang mga typo at gramatikal na error

**Para sa mga pagbabago sa sample code (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Para sa mga pagbabago sa Python sample:**
- Subukang matagumpay na tumakbo ang sample
- Siguraduhing gumagana ang error handling
- Suriin ang compatibility sa Foundry Local

### Proseso ng Review

- Ang mga pagbabago sa nilalamang pang-edukasyon ay sinusuri para sa katumpakan at kalinawan
- Ang mga halimbawa ng code ay sinusuri para sa functionality
- Ang mga update sa pagsasalin ay awtomatikong pinangangasiwaan ng GitHub Actions

## Sistema ng Pagsasalin

**MAHALAGA:** Ang repositoryong ito ay gumagamit ng automated translation sa pamamagitan ng GitHub Actions.

- Ang mga pagsasalin ay nasa `/translations/` directory (50+ wika)
- Awtomatikong pinangangasiwaan sa pamamagitan ng `co-op-translator.yml` workflow
- **HUWAG manwal na i-edit ang mga file ng pagsasalin** - awtomatiko itong mapapalitan
- I-edit lamang ang mga English source files sa root at module directories
- Awtomatikong nalilikha ang mga pagsasalin kapag nag-push sa `main` branch

## Integrasyon ng Foundry Local

Karamihan sa mga Module08 samples ay nangangailangan ng Microsoft Foundry Local na tumatakbo.

### Pag-install at Setup

**I-install ang Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**I-install ang Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Pagsisimula ng Foundry Local
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

### Paggamit ng SDK (Python)
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

### Pag-verify ng Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Mga Environment Variable para sa Mga Halimbawa

Karamihan sa mga halimbawa ay gumagamit ng mga environment variable na ito:
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

**Tandaan**: Kapag gumagamit ng `FoundryLocalManager`, awtomatikong pinangangasiwaan ng SDK ang service discovery at pag-load ng modelo. Ang mga alias ng modelo (tulad ng `phi-3.5-mini`) ay tinitiyak na ang pinakamahusay na variant ay napipili para sa iyong hardware.

## Pagbuo at Pag-deploy

### Pag-deploy ng Nilalaman

Ang repositoryong ito ay pangunahing dokumentasyon - walang kinakailangang proseso ng pagbuo para sa nilalaman.

### Pagbuo ng Sample Application

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
Walang proseso ng pagbuo - direktang pinapatakbo ang mga sample gamit ang Python interpreter.

## Mga Karaniwang Isyu at Pag-troubleshoot

> **Tip**: Suriin ang [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) para sa mga kilalang problema at solusyon.

### Kritikal na Isyu (Blocking)

#### Hindi Tumatakbo ang Foundry Local
**Isyu:** Nabibigo ang mga halimbawa na may mga error sa koneksyon

**Solusyon:**
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

### Karaniwang Isyu (Moderate)

#### Mga Isyu sa Python Virtual Environment
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

#### Mga Isyu sa Electron Build
**Isyu:** Mga pagkabigo sa npm install o build

**Solusyon:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Mga Isyu sa Workflow (Minor)

#### Mga Konflikto sa Workflow ng Pagsasalin
**Isyu:** Ang Translation PR ay sumasalungat sa iyong mga pagbabago

**Solusyon:**
- I-edit lamang ang mga English source files
- Hayaan ang automated translation workflow na pangasiwaan ang mga pagsasalin
- Kung may mga conflict, i-merge ang `main` sa iyong branch pagkatapos ma-merge ang mga pagsasalin

#### Mga Pagkabigo sa Pag-download ng Modelo
**Isyu:** Nabibigo ang Foundry Local na mag-download ng mga modelo

**Solusyon:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Karagdagang Mga Mapagkukunan

### Mga Landas sa Pag-aaral
- **Landas ng Baguhan:** Modules 01-02 (7-9 oras)
- **Landas ng Intermediate:** Modules 03-04 (9-11 oras)
- **Landas ng Advanced:** Modules 05-07 (12-15 oras)
- **Landas ng Eksperto:** Module 08 (8-10 oras)

### Pangunahing Nilalaman ng Module
- **Module01:** Mga pangunahing kaalaman sa EdgeAI at mga case study sa totoong mundo
- **Module02:** Mga pamilya at arkitektura ng Small Language Model (SLM)
- **Module03:** Mga estratehiya sa lokal at cloud deployment
- **Module04:** Pag-optimize ng modelo gamit ang maraming framework
- **Module05:** SLMOps - mga operasyon sa produksyon
- **Module06:** Mga AI agents at function calling
- **Module07:** Mga implementasyon na tiyak sa platform
- **Module08:** Foundry Local toolkit na may 10 komprehensibong halimbawa

### Mga Panlabas na Dependency
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Lokal na runtime ng AI model na may OpenAI-compatible API
  - [Dokumentasyon](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Framework para sa pag-optimize
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Toolkit para sa pag-optimize ng modelo
- [OpenVINO](https://docs.openvino.ai/) - Toolkit ng Intel para sa pag-optimize

## Mga Tala na Tiyak sa Proyekto

### Mga Sample Application ng Module08

Ang repositoryo ay naglalaman ng 10 komprehensibong sample na aplikasyon:

1. **01-REST Chat Quickstart** - Pangunahing integrasyon ng OpenAI SDK
2. **02-OpenAI SDK Integration** - Mga advanced na feature ng SDK
3. **03-Model Discovery & Benchmarking** - Mga tool sa paghahambing ng modelo
4. **04-Chainlit RAG Application** - Retrieval-augmented generation
5. **05-Multi-Agent Orchestration** - Pangunahing koordinasyon ng agent
6. **06-Models-as-Tools Router** - Matalinong pag-route ng modelo
7. **07-Direct API Client** - Mababang antas ng integrasyon ng API
8. **08-Windows 11 Chat App** - Native na Electron desktop application
9. **09-Advanced Multi-Agent System** - Komplikadong koordinasyon ng agent
10. **10-Foundry Tools Framework** - Integrasyon ng LangChain/Semantic Kernel

Ang bawat halimbawa ay nagpapakita ng iba't ibang aspeto ng pag-develop ng edge AI gamit ang Foundry Local.

### Mga Pagsasaalang-alang sa Pagganap

- Ang mga SLM ay na-optimize para sa edge deployment (2-16GB RAM)
- Ang lokal na inference ay nagbibigay ng 50-500ms na oras ng tugon
- Ang mga teknik ng quantization ay nakakamit ng 75% na pagbawas sa laki na may 85% na pagpapanatili ng performance
- Kakayahan sa real-time na pag-uusap gamit ang mga lokal na modelo

### Seguridad at Privacy

- Lahat ng pagproseso ay nangyayari nang lokal - walang data na ipinapadala sa cloud
- Angkop para sa mga aplikasyon na sensitibo sa privacy (healthcare, finance)
- Tumutugon sa mga kinakailangan sa data sovereignty
- Ang Foundry Local ay ganap na tumatakbo sa lokal na hardware

## Pagkuha ng Tulong

### Dokumentasyon

- **Pangunahing README**: [README.md](README.md) - Pangkalahatang-ideya ng repository at mga landas sa pag-aaral
- **Study Guide**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Mga mapagkukunan sa pag-aaral at timeline
- **Support**: [SUPPORT.md](SUPPORT.md) - Paano makakuha ng tulong
- **Seguridad**: [SECURITY.md](SECURITY.md) - Pag-uulat ng mga isyu sa seguridad

### Suporta ng Komunidad

- **GitHub Issues**: [Mag-ulat ng mga bug o humiling ng mga tampok](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Magtanong at magbahagi ng mga ideya](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Mga teknikal na isyu sa Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Kontak

- **Mga Tagapangalaga**: Tingnan ang [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Mga Isyu sa Seguridad**: Sundin ang responsableng pag-uulat sa [SECURITY.md](SECURITY.md)
- **Suporta ng Microsoft**: Para sa suporta sa enterprise, makipag-ugnayan sa customer service ng Microsoft

### Karagdagang Mga Mapagkukunan

- **Microsoft Learn**: [Mga Landas sa Pag-aaral ng AI at Machine Learning](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Dokumentasyon ng Foundry Local**: [Opisyal na Dokumento](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Mga Sample ng Komunidad**: Tingnan ang [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) para sa mga kontribusyon ng komunidad

---

**Ito ay isang pang-edukasyong repository na nakatuon sa pagtuturo ng pag-develop ng Edge AI. Ang pangunahing pattern ng kontribusyon ay ang pagpapabuti ng nilalaman pang-edukasyon at ang pagdaragdag/pagpapahusay ng mga sample na aplikasyon na nagpapakita ng mga konsepto ng Edge AI.**

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.