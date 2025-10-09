<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "135b2658979f1e494bb0ecc6e26d4752",
  "translation_date": "2025-10-09T20:58:09+00:00",
  "source_file": "AGENTS.md",
  "language_code": "lt"
}
-->
# AGENTS.md

> **Kūrėjų vadovas pradedantiesiems EdgeAI**
> 
> Šiame dokumente pateikiama išsami informacija kūrėjams, AI agentams ir prisidedantiems prie šio saugyklos darbo. Jame aptariamas nustatymas, kūrimo procesai, testavimas ir geriausios praktikos.
> 
> **Paskutinį kartą atnaujinta**: 2025 m. spalio mėn. | **Dokumento versija**: 2.0

## Turinys

- [Projekto apžvalga](../..)
- [Saugyklos struktūra](../..)
- [Reikalavimai](../..)
- [Nustatymo komandos](../..)
- [Kūrimo procesas](../..)
- [Testavimo instrukcijos](../..)
- [Kodo stiliaus gairės](../..)
- [Prašymų sujungti gaires](../..)
- [Vertimo sistema](../..)
- [Foundry Local integracija](../..)
- [Kūrimas ir diegimas](../..)
- [Dažnos problemos ir trikčių šalinimas](../..)
- [Papildomi ištekliai](../..)
- [Pastabos apie projektą](../..)
- [Pagalbos gavimas](../..)

## Projekto apžvalga

EdgeAI pradedantiesiems yra išsamus edukacinis saugyklos projektas, mokantis Edge AI kūrimo su mažais kalbos modeliais (SLM). Kursas apima EdgeAI pagrindus, modelių diegimą, optimizavimo technikas ir paruoštus gamybai sprendimus naudojant Microsoft Foundry Local ir įvairias AI sistemas.

**Pagrindinės technologijos:**
- Python 3.8+ (pagrindinė kalba AI/ML pavyzdžiams)
- .NET C# (AI/ML pavyzdžiai)
- JavaScript/Node.js su Electron (darbalaukio programoms)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI sistemos: LangChain, Semantic Kernel, Chainlit
- Modelių optimizavimas: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Saugyklos tipas:** Edukacinis turinys su 8 moduliais ir 10 išsamiais pavyzdžiais

**Architektūra:** Daugiamodulinis mokymosi kelias su praktiniais pavyzdžiais, demonstruojančiais Edge AI diegimo modelius

## Saugyklos struktūra

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

## Reikalavimai

### Reikalingi įrankiai

- **Python 3.8+** - AI/ML pavyzdžiams ir užrašų knygelėms
- **Node.js 16+** - Electron pavyzdinei programai
- **Git** - Versijų kontrolės sistema
- **Microsoft Foundry Local** - AI modelių paleidimui vietoje

### Rekomenduojami įrankiai

- **Visual Studio Code** - Su Python, Jupyter ir Pylance plėtiniais
- **Windows Terminal** - Geresnei komandų eilutės patirčiai (Windows vartotojams)
- **Docker** - Konteinerizuotam kūrimui (neprivaloma)

### Sistemos reikalavimai

- **RAM**: Mažiausiai 8GB, rekomenduojama 16GB+ daugiamodeliams scenarijams
- **Saugykla**: 10GB+ laisvos vietos modeliams ir priklausomybėms
- **OS**: Windows 10/11, macOS 11+ arba Linux (Ubuntu 20.04+)
- **Aparatūra**: CPU su AVX2 palaikymu; GPU (CUDA, Qualcomm NPU) neprivaloma, bet rekomenduojama

### Žinių reikalavimai

- Pagrindinės Python programavimo žinios
- Susipažinimas su komandų eilutės sąsajomis
- AI/ML koncepcijų supratimas (pavyzdžių kūrimui)
- Git darbo procesai ir prašymų sujungti procesai

## Nustatymo komandos

### Saugyklos nustatymas

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python pavyzdžių nustatymas (08 modulis ir Python pavyzdžiai)

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

### Node.js pavyzdžių nustatymas (08 pavyzdys - Windows pokalbių programa)

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

### Foundry Local nustatymas

Foundry Local reikalingas pavyzdžiams paleisti. Atsisiųskite ir įdiekite iš oficialios saugyklos:

**Diegimas:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Rankiniu būdu**: Atsisiųskite iš [leidimų puslapio](https://github.com/microsoft/Foundry-Local/releases)

**Greitas startas:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-3.5-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Pastaba**: Foundry Local automatiškai parenka geriausią modelio variantą jūsų aparatūrai (CUDA GPU, Qualcomm NPU arba CPU).

## Kūrimo procesas

### Turinio kūrimas

Ši saugykla daugiausia apima **Markdown edukacinį turinį**. Atliekant pakeitimus:

1. Redaguokite `.md` failus atitinkamuose modulio kataloguose
2. Laikykitės esamų formatavimo šablonų
3. Užtikrinkite, kad kodo pavyzdžiai būtų tikslūs ir išbandyti
4. Atnaujinkite atitinkamą išverstą turinį, jei reikia (arba leiskite automatizacijai tai atlikti)

### Pavyzdinių programų kūrimas

Python pavyzdžiams (pavyzdžiai 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron pavyzdžiui (pavyzdys 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Pavyzdinių programų testavimas

Python pavyzdžiai neturi automatizuotų testų, bet gali būti patikrinti paleidžiant juos:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron pavyzdys turi testavimo infrastruktūrą:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testavimo instrukcijos

### Turinio patikrinimas

Saugykla naudoja automatizuotus vertimo procesus. Rankinis testavimas vertimams nereikalingas.

**Rankinis turinio pakeitimų patikrinimas:**
1. Peržiūrėkite Markdown failų atvaizdavimą
2. Patikrinkite, ar visi nuorodos nukreipia į galiojančius taikinius
3. Išbandykite dokumentacijoje pateiktus kodo fragmentus
4. Įsitikinkite, kad vaizdai tinkamai įkeliami

### Pavyzdinių programų testavimas

**08 modulis/pavyzdžiai/08 (Electron programa) turi išsamų testavimą:**
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

**Python pavyzdžiai turėtų būti testuojami rankiniu būdu:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Kodo stiliaus gairės

### Markdown turinys

- Naudokite nuoseklią antraščių hierarchiją (# pavadinimui, ## pagrindinėms sekcijoms, ### poskyriams)
- Įtraukite kodo blokus su kalbos specifikatoriais: ```python, ```bash, ```javascript
- Laikykitės esamo formatavimo lentelėms, sąrašams ir akcentams
- Išlaikykite skaitomus eilutes (~80-100 simbolių, bet ne griežtai)
- Naudokite santykines nuorodas vidiniams šaltiniams

### Python kodo stilius

- Laikykitės PEP 8 konvencijų
- Naudokite tipų užuominas, kur tai tinkama
- Įtraukite docstring'us funkcijoms ir klasėms
- Naudokite prasmingus kintamųjų pavadinimus
- Laikykitės funkcijų fokusavimo ir glaustumo

### JavaScript/Node.js kodo stilius

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Pagrindinės konvencijos:**
- ESLint konfigūracija pateikta 08 pavyzdyje
- Prettier kodo formatavimui
- Naudokite modernią ES6+ sintaksę
- Laikykitės esamų šablonų kode

## Prašymų sujungti gairės

### Prisidėjimo procesas

1. **Fork saugyklą** ir sukurkite naują šaką iš `main`
2. **Atlikite pakeitimus**, laikydamiesi kodo stiliaus gairių
3. **Išbandykite kruopščiai**, naudodamiesi aukščiau pateiktomis testavimo instrukcijomis
4. **Įsipareigokite su aiškiais pranešimais**, laikydamiesi įprastų įsipareigojimų formato
5. **Įkelkite į savo fork** ir sukurkite prašymą sujungti
6. **Atsakykite į palaikytojų atsiliepimus** peržiūros metu

### Šakų pavadinimų konvencija

- `feature/<modulis>-<aprašymas>` - Naujiems funkcionalumams ar turiniui
- `fix/<modulis>-<aprašymas>` - Klaidų taisymui
- `docs/<aprašymas>` - Dokumentacijos patobulinimams
- `refactor/<aprašymas>` - Kodo refaktorizavimui

### Įsipareigojimų pranešimų formatas

Laikykitės [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Pavyzdžiai:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Pavadinimo formatas
```
[ModuleXX] Brief description of change
```
arba
```
[Module08/samples/XX] Description for sample changes
```

### Elgesio kodeksas

Visi prisidedantys privalo laikytis [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Prašome peržiūrėti [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) prieš prisidedant.

### Prieš pateikimą

**Turinio pakeitimams:**
- Peržiūrėkite visus modifikuotus Markdown failus
- Patikrinkite nuorodas ir vaizdus
- Patikrinkite rašybos ir gramatikos klaidas

**Pavyzdinio kodo pakeitimams (08 modulis/pavyzdžiai/08):**
```bash
npm run lint
npm test
```

**Python pavyzdžių pakeitimams:**
- Patikrinkite, ar pavyzdys sėkmingai veikia
- Patikrinkite klaidų tvarkymą
- Patikrinkite suderinamumą su Foundry Local

### Peržiūros procesas

- Edukacinio turinio pakeitimai peržiūrimi dėl tikslumo ir aiškumo
- Kodo pavyzdžiai testuojami dėl funkcionalumo
- Vertimo atnaujinimai automatiškai tvarkomi GitHub Actions

## Vertimo sistema

**SVARBU:** Ši saugykla naudoja automatizuotą vertimą per GitHub Actions.

- Vertimai yra `/translations/` kataloge (50+ kalbų)
- Automatizuota per `co-op-translator.yml` darbo eigą
- **NEKEISKITE vertimo failų rankiniu būdu** - jie bus perrašyti
- Redaguokite tik angliškus šaltinio failus šakniniame ir modulio kataloguose
- Vertimai automatiškai generuojami, kai įkeliate į `main` šaką

## Foundry Local integracija

Dauguma 08 modulio pavyzdžių reikalauja, kad Microsoft Foundry Local būtų paleistas.

### Diegimas ir nustatymas

**Diegti Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Diegti Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local paleidimas
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

### SDK naudojimas (Python)
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

### Foundry Local patikrinimas
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Aplinkos kintamieji pavyzdžiams

Dauguma pavyzdžių naudoja šiuos aplinkos kintamuosius:
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

**Pastaba**: Naudojant `FoundryLocalManager`, SDK automatiškai tvarko paslaugų atradimą ir modelių įkrovimą. Modelių pseudonimai (pvz., `phi-3.5-mini`) užtikrina, kad jūsų aparatūrai bus pasirinktas geriausias variantas.

## Kūrimas ir diegimas

### Turinio diegimas

Ši saugykla daugiausia dokumentacija - turiniui nereikalingas kūrimo procesas.

### Pavyzdinių programų kūrimas

**Electron programa (08 modulis/pavyzdžiai/08):**
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

**Python pavyzdžiai:**
Nereikalingas kūrimo procesas - pavyzdžiai paleidžiami tiesiogiai su Python interpretatoriumi.

## Dažnos problemos ir trikčių šalinimas

> **Patarimas**: Patikrinkite [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) dėl žinomų problemų ir sprendimų.

### Kritinės problemos (blokuojančios)

#### Foundry Local neveikia
**Problema:** Pavyzdžiai nepavyksta sujungti dėl ryšio klaidų

**Sprendimas:**
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

### Dažnos problemos (vidutinės)

#### Python virtualios aplinkos problemos
**Problema:** Modulių importavimo klaidos

**Sprendimas:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron kūrimo problemos
**Problema:** npm diegimo arba kūrimo klaidos

**Sprendimas:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Darbo eigos problemos (nedidelės)

#### Vertimo darbo eigos konfliktai
**Problema:** Vertimo PR konfliktuoja su jūsų pakeitimais

**Sprendimas:**
- Redaguokite tik angliškus šaltinio failus
- Leiskite automatizuotam vertimo procesui tvarkyti vertimus
- Jei kyla konfliktų, sujunkite `main` į savo šaką po vertimų sujungimo

#### Modelio atsisiuntimo klaidos
**Problema:** Foundry Local nepavyksta atsisiųsti modelių

**Sprendimas:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Papildomi ištekliai

### Mokymosi keliai
- **Pradedančiųjų kelias:** Moduliai 01-02 (7-9 valandos)
- **Vidutinis kelias:** Moduliai 03-04 (9-11 valandos)
- **Pažengusiųjų kelias:** Moduliai 05-07 (12-15 valandos)
- **Ekspertų kelias:** Modulis 08 (8-10 valandų)

### Pagrindinis modulio turinys
- **Modulis01:** EdgeAI pagrindai ir realaus pasaulio atvejų analizės
- **Modulis02:** Mažų kalbos modelių (SLM) šeimos ir architektūros
- **Modulis03:** Vietinio ir debesų diegimo strategijos
- **Modulis04:** Modelių optimizavimas su įvairiomis sistemomis
- **Modulis05:** SLMOps - gamybos operacijos
- **Modulis06:** AI agentai ir funkcijų kvietimas
- **Modulis07:** Platformai specifiniai įgyvendinimai
- **Modulis08:** Foundry Local įrankių rinkinys su 10 išsamiais pavyzdžiais

### Išorinės priklausomybės
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Vietinis AI modelių paleidimo įrankis su OpenAI suderinama API
  - [Dokumentacija](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimizavimo sistema
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Modelių optimizavimo įrankių rinkinys
- [OpenVINO](https://docs.openvino.ai/) - Intel optimizavimo įrankių rinkinys

## Pastabos apie projektą

### 08 modulio pavyzdinės programos

Saugykla apima 10 išsamių pavyzdinių programų:

1. **01-REST pokalbių greitas startas** - Pagrindinė OpenAI SDK integracija
2. **02-OpenAI SDK integracija** - Išplė
- Vietinis apdorojimas užtikrina 50-500 ms atsako laiką  
- Kvantavimo technikos sumažina dydį 75%, išlaikant 85% našumo  
- Realaus laiko pokalbių galimybės su vietiniais modeliais  

### Saugumas ir privatumas  

- Visi apdorojimai vykdomi vietoje – duomenys nėra siunčiami į debesiją  
- Tinka privatumui jautrioms programoms (sveikatos apsauga, finansai)  
- Atitinka duomenų suvereniteto reikalavimus  
- Foundry Local veikia tik vietinėje aparatinėje įrangoje  

## Pagalbos gavimas  

### Dokumentacija  

- **Pagrindinis README**: [README.md](README.md) – Saugyklos apžvalga ir mokymosi keliai  
- **Mokymosi vadovas**: [STUDY_GUIDE.md](STUDY_GUIDE.md) – Mokymosi ištekliai ir tvarkaraštis  
- **Pagalba**: [SUPPORT.md](SUPPORT.md) – Kaip gauti pagalbą  
- **Saugumas**: [SECURITY.md](SECURITY.md) – Kaip pranešti apie saugumo problemas  

### Bendruomenės pagalba  

- **GitHub problemos**: [Pranešti apie klaidas ar siūlyti funkcijas](https://github.com/microsoft/edgeai-for-beginners/issues)  
- **GitHub diskusijos**: [Užduoti klausimus ir dalintis idėjomis](https://github.com/microsoft/edgeai-for-beginners/discussions)  
- **Foundry Local problemos**: [Techninės problemos su Foundry Local](https://github.com/microsoft/Foundry-Local/issues)  

### Kontaktai  

- **Prižiūrėtojai**: Žr. [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)  
- **Saugumo problemos**: Vadovaukitės atsakingo atskleidimo gairėmis [SECURITY.md](SECURITY.md)  
- **Microsoft pagalba**: Dėl įmonių pagalbos kreipkitės į Microsoft klientų aptarnavimą  

### Papildomi ištekliai  

- **Microsoft Learn**: [Dirbtinio intelekto ir mašininio mokymosi mokymosi keliai](https://learn.microsoft.com/training/browse/?products=ai-services)  
- **Foundry Local dokumentacija**: [Oficiali dokumentacija](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)  
- **Bendruomenės pavyzdžiai**: Peržiūrėkite [GitHub diskusijas](https://github.com/microsoft/edgeai-for-beginners/discussions) dėl bendruomenės indėlių  

---

**Tai yra edukacinė saugykla, skirta mokyti Edge AI kūrimo. Pagrindinis indėlio modelis – tobulinti edukacinį turinį ir pridėti/pagerinti pavyzdines programas, kurios demonstruoja Edge AI koncepcijas.**

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.