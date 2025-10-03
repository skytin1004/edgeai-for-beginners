<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:41:38+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sw"
}
-->
# AGENTS.md

## Muhtasari wa Mradi

EdgeAI kwa Kompyuta ni hifadhi ya elimu inayofundisha maendeleo ya Edge AI kwa kutumia Small Language Models (SLMs). Kozi inashughulikia misingi ya EdgeAI, usambazaji wa modeli, mbinu za uboreshaji, na utekelezaji wa kiwango cha uzalishaji kwa kutumia Microsoft Foundry Local na mifumo mbalimbali ya AI.

**Teknolojia Muhimu:**
- Python 3.8+ (lugha kuu kwa sampuli za AI/ML)
- .NET C# (Sampuli za AI/ML)
- JavaScript/Node.js na Electron (kwa programu za desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Mifumo ya AI: LangChain, Semantic Kernel, Chainlit
- Uboreshaji wa Modeli: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Aina ya Hifadhi:** Hifadhi ya maudhui ya elimu yenye moduli 8 na programu 10 za sampuli za kina

**Muundo:** Njia ya kujifunza yenye moduli nyingi na sampuli za vitendo zinazoonyesha mifumo ya usambazaji wa Edge AI

## Muundo wa Hifadhi

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

## Amri za Usanidi

### Usanidi wa Hifadhi

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Usanidi wa Sampuli za Python (Moduli08 na sampuli za Python)

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

### Usanidi wa Sampuli za Node.js (Sampuli 08 - Windows Chat App)

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

### Usanidi wa Foundry Local

Foundry Local inahitajika kuendesha sampuli za Moduli08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Mtiririko wa Maendeleo

### Maendeleo ya Maudhui

Hifadhi hii ina maudhui ya elimu ya **Markdown**. Unapofanya mabadiliko:

1. Hariri faili za `.md` katika saraka za moduli husika
2. Fuata mifumo ya muundo iliyopo
3. Hakikisha mifano ya msimbo ni sahihi na imejaribiwa
4. Sasisha maudhui yaliyotafsiriwa yanayolingana ikiwa ni lazima (au acha otomatiki ishughulikie)

### Maendeleo ya Programu za Sampuli

Kwa sampuli za Python (sampuli 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Kwa sampuli za Electron (sampuli 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Upimaji wa Programu za Sampuli

Sampuli za Python hazina majaribio ya kiotomatiki lakini zinaweza kuthibitishwa kwa kuziendesha:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Sampuli za Electron zina miundombinu ya majaribio:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Maelekezo ya Upimaji

### Uthibitishaji wa Maudhui

Hifadhi hutumia mtiririko wa tafsiri otomatiki. Hakuna upimaji wa mikono unaohitajika kwa tafsiri.

**Uthibitishaji wa mikono kwa mabadiliko ya maudhui:**
1. Angalia uwasilishaji wa Markdown kwa kutazama faili za `.md`
2. Hakikisha viungo vyote vinaelekeza kwenye malengo sahihi
3. Jaribu vipande vyovyote vya msimbo vilivyojumuishwa katika nyaraka
4. Hakikisha picha zinapakia vizuri

### Upimaji wa Programu za Sampuli

**Moduli08/sampuli/08 (programu ya Electron) ina majaribio ya kina:**
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

**Sampuli za Python zinapaswa kujaribiwa kwa mikono:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Miongozo ya Mtindo wa Msimbo

### Maudhui ya Markdown

- Tumia uongozi thabiti wa vichwa (# kwa kichwa, ## kwa sehemu kuu, ### kwa sehemu ndogo)
- Jumuisha vizuizi vya msimbo na viainishi vya lugha: ```python, ```bash, ```javascript
- Fuata muundo uliopo kwa jedwali, orodha, na msisitizo
- Weka mistari isomeke (lenga ~80-100 herufi, lakini si lazima)
- Tumia viungo vya jamaa kwa marejeleo ya ndani

### Mtindo wa Msimbo wa Python

- Fuata kanuni za PEP 8
- Tumia vidokezo vya aina inapofaa
- Jumuisha maelezo ya kazi na madarasa
- Tumia majina ya kutofautisha yenye maana
- Weka kazi zikiwa zinalenga na fupi

### Mtindo wa Msimbo wa JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Kanuni Muhimu:**
- Usanidi wa ESLint umetolewa katika sampuli 08
- Prettier kwa muundo wa msimbo
- Tumia sintaksia ya kisasa ya ES6+
- Fuata mifumo iliyopo katika hifadhidata ya msimbo

## Miongozo ya Ombi la Kuvuta

### Muundo wa Kichwa
```
[ModuleXX] Brief description of change
```
au
```
[Module08/samples/XX] Description for sample changes
```

### Kabla ya Kuwasilisha

**Kwa mabadiliko ya maudhui:**
- Tazama faili zote za Markdown zilizobadilishwa
- Hakikisha viungo na picha zinafanya kazi
- Angalia makosa ya tahajia na sarufi

**Kwa mabadiliko ya msimbo wa sampuli (Moduli08/sampuli/08):**
```bash
npm run lint
npm test
```

**Kwa mabadiliko ya sampuli za Python:**
- Jaribu sampuli zinaendesha kwa mafanikio
- Hakikisha utunzaji wa makosa unafanya kazi
- Angalia utangamano na Foundry Local

### Mchakato wa Mapitio

- Mabadiliko ya maudhui ya elimu yanapitiwa kwa usahihi na uwazi
- Sampuli za msimbo zinajaribiwa kwa utendaji
- Sasisho za tafsiri zinashughulikiwa kiotomatiki na GitHub Actions

## Mfumo wa Tafsiri

**MUHIMU:** Hifadhi hii hutumia tafsiri otomatiki kupitia GitHub Actions.

- Tafsiri ziko katika saraka ya `/translations/` (lugha 50+)
- Zinafanywa kiotomatiki kupitia mtiririko wa `co-op-translator.yml`
- **USIHARIRI faili za tafsiri kwa mikono** - zitafutwa
- Hariri faili za chanzo za Kiingereza pekee katika saraka kuu na moduli
- Tafsiri zinazalishwa kiotomatiki unapoweka kwenye tawi la `main`

## Ujumuishaji wa Foundry Local

Sampuli nyingi za Moduli08 zinahitaji Microsoft Foundry Local kuendesha:

### Kuanza Foundry Local
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

### Kuthibitisha Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Vigezo vya Mazingira kwa Sampuli

Sampuli nyingi zinatumia vigezo hivi vya mazingira:
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

## Ujenzi na Usambazaji

### Usambazaji wa Maudhui

Hifadhi hii ni nyaraka hasa - hakuna mchakato wa ujenzi unaohitajika kwa maudhui.

### Ujenzi wa Programu za Sampuli

**Programu ya Electron (Moduli08/sampuli/08):**
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

**Sampuli za Python:**
Hakuna mchakato wa ujenzi - sampuli zinaendeshwa moja kwa moja na tafsiri ya Python.

## Masuala ya Kawaida na Utatuzi

### Foundry Local Haifanyi Kazi
**Tatizo:** Sampuli zinashindwa na makosa ya muunganisho

**Suluhisho:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Masuala ya Mazingira ya Virtual ya Python
**Tatizo:** Makosa ya uingizaji wa moduli

**Suluhisho:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Masuala ya Ujenzi wa Electron
**Tatizo:** npm install au kushindwa kwa ujenzi

**Suluhisho:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Migogoro ya Mtiririko wa Tafsiri
**Tatizo:** Tafsiri PR zinagongana na mabadiliko yako

**Suluhisho:**
- Hariri faili za chanzo za Kiingereza pekee
- Acha mtiririko wa tafsiri otomatiki ushughulikie tafsiri
- Ikiwa migogoro itatokea, unganisha `main` kwenye tawi lako baada ya tafsiri kuunganishwa

## Rasilimali za Ziada

### Njia za Kujifunza
- **Njia ya Kompyuta:** Moduli 01-02 (saa 7-9)
- **Njia ya Kati:** Moduli 03-04 (saa 9-11)
- **Njia ya Juu:** Moduli 05-07 (saa 12-15)
- **Njia ya Mtaalamu:** Moduli 08 (saa 8-10)

### Maudhui Muhimu ya Moduli
- **Moduli01:** Misingi ya EdgeAI na masomo ya hali halisi
- **Moduli02:** Familia za Small Language Model (SLM) na miundo
- **Moduli03:** Mikakati ya usambazaji wa ndani na wingu
- **Moduli04:** Uboreshaji wa modeli kwa mifumo mbalimbali
- **Moduli05:** SLMOps - operesheni za uzalishaji
- **Moduli06:** Mawakala wa AI na kupiga kazi
- **Moduli07:** Utekelezaji maalum wa jukwaa
- **Moduli08:** Zana za Foundry Local na sampuli 10 za kina

### Vitegemezi vya Nje
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Muda wa modeli ya AI ya ndani
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Mfumo wa uboreshaji
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Zana ya uboreshaji wa modeli
- [OpenVINO](https://docs.openvino.ai/) - Zana ya uboreshaji ya Intel

## Vidokezo Maalum vya Mradi

### Programu za Sampuli za Moduli08

Hifadhi inajumuisha programu 10 za sampuli za kina:

1. **01-REST Chat Quickstart** - Muunganisho wa msingi wa OpenAI SDK
2. **02-OpenAI SDK Integration** - Vipengele vya SDK vya hali ya juu
3. **03-Model Discovery & Benchmarking** - Zana za kulinganisha modeli
4. **04-Chainlit RAG Application** - Uzalishaji unaosaidiwa na urejeshaji
5. **05-Multi-Agent Orchestration** - Uratibu wa mawakala wa msingi
6. **06-Models-as-Tools Router** - Usambazaji wa modeli wenye akili
7. **07-Direct API Client** - Muunganisho wa API wa kiwango cha chini
8. **08-Windows 11 Chat App** - Programu ya desktop ya Electron ya asili
9. **09-Advanced Multi-Agent System** - Uratibu wa mawakala wa hali ya juu
10. **10-Foundry Tools Framework** - Muunganisho wa LangChain/Semantic Kernel

Kila sampuli inaonyesha vipengele tofauti vya maendeleo ya Edge AI kwa Foundry Local.

### Mazingatio ya Utendaji

- SLMs zimeboreshwa kwa usambazaji wa Edge (RAM 2-16GB)
- Utoaji wa ndani hutoa nyakati za majibu za 50-500ms
- Mbinu za upunguzaji hufanikisha kupunguzwa kwa ukubwa kwa 75% na uhifadhi wa utendaji wa 85%
- Uwezo wa mazungumzo ya wakati halisi na modeli za ndani

### Usalama na Faragha

- Usindikaji wote hufanyika ndani - hakuna data inayotumwa kwa wingu
- Inafaa kwa programu nyeti za faragha (huduma za afya, fedha)
- Inakidhi mahitaji ya uhuru wa data
- Foundry Local inaendeshwa kikamilifu kwenye vifaa vya ndani

---

**Hii ni hifadhi ya elimu inayolenga kufundisha maendeleo ya Edge AI. Muundo mkuu wa mchango ni kuboresha maudhui ya elimu na kuongeza/kuboresha programu za sampuli zinazoonyesha dhana za Edge AI.**

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.