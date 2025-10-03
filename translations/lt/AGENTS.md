<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:48:35+00:00",
  "source_file": "AGENTS.md",
  "language_code": "lt"
}
-->
# AGENTS.md

## Projekto apžvalga

EdgeAI pradedantiesiems yra išsamus edukacinis šaltinis, mokantis Edge AI kūrimo su mažais kalbos modeliais (SLM). Kursas apima EdgeAI pagrindus, modelių diegimą, optimizavimo technikas ir paruoštus gamybai sprendimus, naudojant Microsoft Foundry Local ir įvairias AI sistemas.

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

**Saugyklos tipas:** Edukacinis turinys su 8 moduliais ir 10 išsamių pavyzdinių programų

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

# Install dependencies for Module08 samples
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

Foundry Local reikalingas 08 modulio pavyzdžiams vykdyti:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Kūrimo procesas

### Turinio kūrimas

Ši saugykla daugiausia sudaryta iš **Markdown edukacinio turinio**. Atliekant pakeitimus:

1. Redaguokite `.md` failus atitinkamuose modulio kataloguose
2. Laikykitės esamų formatavimo šablonų
3. Užtikrinkite, kad kodo pavyzdžiai būtų tikslūs ir išbandyti
4. Atnaujinkite atitinkamą išverstą turinį, jei reikia (arba leiskite tai atlikti automatizacijai)

### Pavyzdinių programų kūrimas

Python pavyzdžiams (pavyzdžiai 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron pavyzdžiui (08 pavyzdys):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Pavyzdinių programų testavimas

Python pavyzdžiai neturi automatizuotų testų, tačiau juos galima patikrinti vykdant:
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

Saugykla naudoja automatizuotus vertimo procesus. Vertimams nereikia rankinio testavimo.

**Rankinis turinio pakeitimų patikrinimas:**
1. Peržiūrėkite Markdown failų atvaizdavimą
2. Patikrinkite, ar visi nuorodos nukreipia į galiojančius tikslus
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
- Išlaikykite skaitomus eilutes (apie 80-100 simbolių, bet ne griežtai)
- Naudokite santykines nuorodas vidiniams šaltiniams

### Python kodo stilius

- Laikykitės PEP 8 konvencijų
- Naudokite tipų užuominas, kur tai tinkama
- Įtraukite docstrings funkcijoms ir klasėms
- Naudokite prasmingus kintamųjų pavadinimus
- Išlaikykite funkcijas koncentruotas ir glaustas

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

## Pull Request gairės

### Pavadinimo formatas
```
[ModuleXX] Brief description of change
```
arba
```
[Module08/samples/XX] Description for sample changes
```

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
- Vertimo atnaujinimai tvarkomi automatiškai per GitHub Actions

## Vertimo sistema

**SVARBU:** Ši saugykla naudoja automatizuotą vertimą per GitHub Actions.

- Vertimai yra `/translations/` kataloge (50+ kalbų)
- Automatizuota per `co-op-translator.yml` darbo eigą
- **NEKEISKITE vertimo failų rankiniu būdu** - jie bus perrašyti
- Redaguokite tik anglų kalbos šaltinio failus pagrindiniame ir modulio kataloguose
- Vertimai automatiškai generuojami po įkėlimo į `main` šaką

## Foundry Local integracija

Dauguma 08 modulio pavyzdžių reikalauja, kad Microsoft Foundry Local būtų paleistas:

### Foundry Local paleidimas
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

### Foundry Local patikrinimas
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Aplinkos kintamieji pavyzdžiams

Dauguma pavyzdžių naudoja šiuos aplinkos kintamuosius:
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

## Kūrimas ir diegimas

### Turinio diegimas

Ši saugykla daugiausia yra dokumentacija - turiniui nereikia kūrimo proceso.

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
Nėra kūrimo proceso - pavyzdžiai vykdomi tiesiogiai su Python interpreteriu.

## Dažnos problemos ir trikčių šalinimas

### Foundry Local neveikia
**Problema:** Pavyzdžiai nepavyksta dėl ryšio klaidų

**Sprendimas:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python virtualios aplinkos problemos
**Problema:** Modulio importavimo klaidos

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

### Electron kūrimo problemos
**Problema:** npm install arba kūrimo klaidos

**Sprendimas:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Vertimo darbo eigos konfliktai
**Problema:** Vertimo PR konfliktuoja su jūsų pakeitimais

**Sprendimas:**
- Redaguokite tik anglų kalbos šaltinio failus
- Leiskite automatizuotai vertimo darbo eigai tvarkyti vertimus
- Jei kyla konfliktų, sujunkite `main` su savo šaka po vertimų sujungimo

## Papildomi ištekliai

### Mokymosi keliai
- **Pradedančiųjų kelias:** Moduliai 01-02 (7-9 valandos)
- **Vidutinis kelias:** Moduliai 03-04 (9-11 valandos)
- **Pažengusiųjų kelias:** Moduliai 05-07 (12-15 valandos)
- **Ekspertų kelias:** Modulis 08 (8-10 valandos)

### Pagrindinis modulio turinys
- **Modulis01:** EdgeAI pagrindai ir realaus pasaulio atvejų analizės
- **Modulis02:** Mažų kalbos modelių (SLM) šeimos ir architektūros
- **Modulis03:** Vietinio ir debesų diegimo strategijos
- **Modulis04:** Modelių optimizavimas su įvairiomis sistemomis
- **Modulis05:** SLMOps - gamybos operacijos
- **Modulis06:** AI agentai ir funkcijų kvietimas
- **Modulis07:** Platformai specifiniai įgyvendinimai
- **Modulis08:** Foundry Local įrankių rinkinys su 10 išsamių pavyzdžių

### Išorinės priklausomybės
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Vietinis AI modelių vykdymo aplinka
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimizavimo sistema
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Modelių optimizavimo įrankių rinkinys
- [OpenVINO](https://docs.openvino.ai/) - Intel optimizavimo įrankių rinkinys

## Projekto specifinės pastabos

### 08 modulio pavyzdinės programos

Saugykla apima 10 išsamių pavyzdinių programų:

1. **01-REST pokalbių greitas startas** - Pagrindinė OpenAI SDK integracija
2. **02-OpenAI SDK integracija** - Išplėstinės SDK funkcijos
3. **03-Modelių atradimas ir palyginimas** - Modelių palyginimo įrankiai
4. **04-Chainlit RAG programa** - Generavimas su informacijos paieška
5. **05-Daugiagentė koordinacija** - Pagrindinė agentų koordinacija
6. **06-Modeliai kaip įrankiai** - Išmanus modelių maršrutizavimas
7. **07-Tiesioginis API klientas** - Žemo lygio API integracija
8. **08-Windows 11 pokalbių programa** - Vietinė Electron darbalaukio programa
9. **09-Išplėstinė daugiagentė sistema** - Sudėtinga agentų koordinacija
10. **10-Foundry įrankių sistema** - LangChain/Semantic Kernel integracija

Kiekvienas pavyzdys demonstruoja skirtingus Edge AI kūrimo aspektus su Foundry Local.

### Našumo aspektai

- SLM optimizuoti Edge diegimui (2-16GB RAM)
- Vietinis apdorojimas užtikrina 50-500ms atsako laiką
- Kvantizavimo technikos pasiekia 75% dydžio sumažinimą su 85% našumo išlaikymu
- Realaus laiko pokalbių galimybės su vietiniais modeliais

### Saugumas ir privatumas

- Visi apdorojimai vyksta vietoje - duomenys nėra siunčiami į debesį
- Tinka privatumui jautrioms programoms (sveikatos apsauga, finansai)
- Atitinka duomenų suvereniteto reikalavimus
- Foundry Local veikia tik vietinėje aparatinėje įrangoje

---

**Tai edukacinė saugykla, skirta mokyti Edge AI kūrimo. Pagrindinis indėlis yra edukacinio turinio tobulinimas ir pavyzdinių programų, demonstruojančių Edge AI koncepcijas, pridėjimas/pagerinimas.**

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.