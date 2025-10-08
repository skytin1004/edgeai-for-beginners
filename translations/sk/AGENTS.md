<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "135b2658979f1e494bb0ecc6e26d4752",
  "translation_date": "2025-10-08T15:04:19+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sk"
}
-->
# AGENTS.md

> **Príručka pre vývojárov prispievajúcich do EdgeAI pre začiatočníkov**
> 
> Tento dokument poskytuje komplexné informácie pre vývojárov, AI agentov a prispievateľov pracujúcich s týmto repozitárom. Zahŕňa nastavenie, pracovné postupy vývoja, testovanie a osvedčené postupy.
> 
> **Posledná aktualizácia**: október 2025 | **Verzia dokumentu**: 2.0

## Obsah

- [Prehľad projektu](../..)
- [Štruktúra repozitára](../..)
- [Predpoklady](../..)
- [Príkazy na nastavenie](../..)
- [Pracovný postup vývoja](../..)
- [Pokyny na testovanie](../..)
- [Štýlové pokyny pre kód](../..)
- [Pokyny pre pull requesty](../..)
- [Systém prekladu](../..)
- [Integrácia Foundry Local](../..)
- [Build a nasadenie](../..)
- [Bežné problémy a riešenie problémov](../..)
- [Dodatočné zdroje](../..)
- [Poznámky špecifické pre projekt](../..)
- [Získanie pomoci](../..)

## Prehľad projektu

EdgeAI pre začiatočníkov je komplexný vzdelávací repozitár, ktorý učí vývoj Edge AI pomocou malých jazykových modelov (SLM). Kurz pokrýva základy EdgeAI, nasadenie modelov, optimalizačné techniky a implementácie pripravené na produkciu pomocou Microsoft Foundry Local a rôznych AI rámcov.

**Kľúčové technológie:**
- Python 3.8+ (primárny jazyk pre AI/ML ukážky)
- .NET C# (AI/ML ukážky)
- JavaScript/Node.js s Electron (pre desktopové aplikácie)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI rámce: LangChain, Semantic Kernel, Chainlit
- Optimalizácia modelov: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Typ repozitára:** Vzdelávací obsahový repozitár s 8 modulmi a 10 komplexnými ukážkovými aplikáciami

**Architektúra:** Viacmodulová vzdelávacia cesta s praktickými ukážkami demonštrujúcimi vzory nasadenia Edge AI

## Štruktúra repozitára

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

## Predpoklady

### Požadované nástroje

- **Python 3.8+** - Pre AI/ML ukážky a notebooky
- **Node.js 16+** - Pre ukážkovú aplikáciu Electron
- **Git** - Pre správu verzií
- **Microsoft Foundry Local** - Pre lokálne spúšťanie AI modelov

### Odporúčané nástroje

- **Visual Studio Code** - S rozšíreniami Python, Jupyter a Pylance
- **Windows Terminal** - Pre lepší zážitok z príkazového riadku (používatelia Windows)
- **Docker** - Pre kontajnerový vývoj (voliteľné)

### Požiadavky na systém

- **RAM**: Minimálne 8GB, odporúča sa 16GB+ pre scenáre s viacerými modelmi
- **Úložisko**: 10GB+ voľného miesta pre modely a závislosti
- **OS**: Windows 10/11, macOS 11+, alebo Linux (Ubuntu 20.04+)
- **Hardvér**: CPU s podporou AVX2; GPU (CUDA, Qualcomm NPU) voliteľné, ale odporúčané

### Predpoklady znalostí

- Základné porozumenie programovaniu v Pythone
- Znalosť príkazového riadku
- Porozumenie konceptom AI/ML (pre vývoj ukážok)
- Git pracovné postupy a procesy pull requestov

## Príkazy na nastavenie

### Nastavenie repozitára

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Nastavenie Python ukážok (Modul08 a Python ukážky)

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

### Nastavenie Node.js ukážok (Ukážka 08 - Windows Chat App)

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

### Nastavenie Foundry Local

Foundry Local je potrebné na spustenie ukážok. Stiahnite a nainštalujte z oficiálneho repozitára:

**Inštalácia:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manuálne**: Stiahnite z [stránky vydaní](https://github.com/microsoft/Foundry-Local/releases)

**Rýchly štart:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-3.5-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Poznámka**: Foundry Local automaticky vyberie najlepšiu variantu modelu pre váš hardvér (CUDA GPU, Qualcomm NPU alebo CPU).

## Pracovný postup vývoja

### Vývoj obsahu

Tento repozitár obsahuje primárne **Markdown vzdelávací obsah**. Pri vykonávaní zmien:

1. Upravte `.md` súbory v príslušných adresároch modulov
2. Dodržiavajte existujúce formátovacie vzory
3. Uistite sa, že ukážky kódu sú presné a otestované
4. Aktualizujte zodpovedajúci preložený obsah, ak je to potrebné (alebo nechajte automatizáciu, aby to spravila)

### Vývoj ukážkových aplikácií

Pre Python ukážky (ukážky 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Pre ukážku Electron (ukážka 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testovanie ukážkových aplikácií

Python ukážky nemajú automatizované testy, ale môžu byť validované ich spustením:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Ukážka Electron má testovaciu infraštruktúru:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Pokyny na testovanie

### Validácia obsahu

Repozitár používa automatizované pracovné postupy pre preklady. Manuálne testovanie prekladov nie je potrebné.

**Manuálna validácia zmien obsahu:**
1. Skontrolujte vykreslenie Markdownu náhľadom `.md` súborov
2. Overte, že všetky odkazy smerujú na platné ciele
3. Otestujte akékoľvek ukážky kódu zahrnuté v dokumentácii
4. Skontrolujte, či sa obrázky načítavajú správne

### Testovanie ukážkových aplikácií

**Module08/samples/08 (Electron app) má komplexné testovanie:**
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

**Python ukážky by mali byť testované manuálne:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Štýlové pokyny pre kód

### Markdown obsah

- Používajte konzistentnú hierarchiu nadpisov (# pre názov, ## pre hlavné sekcie, ### pre podsekcie)
- Zahrňte bloky kódu so špecifikátormi jazyka: ```python, ```bash, ```javascript
- Dodržiavajte existujúce formátovanie pre tabuľky, zoznamy a zvýraznenie
- Udržujte riadky čitateľné (cieľom je ~80-100 znakov, ale nie striktne)
- Používajte relatívne odkazy pre interné referencie

### Štýl kódu v Pythone

- Dodržiavajte konvencie PEP 8
- Používajte typové anotácie, kde je to vhodné
- Zahrňte docstringy pre funkcie a triedy
- Používajte zmysluplné názvy premenných
- Udržujte funkcie zamerané a stručné

### Štýl kódu v JavaScripte/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Kľúčové konvencie:**
- Konfigurácia ESLint je poskytnutá v ukážke 08
- Prettier pre formátovanie kódu
- Používajte modernú syntax ES6+
- Dodržiavajte existujúce vzory v kóde

## Pokyny pre pull requesty

### Pracovný postup prispievania

1. **Forknite repozitár** a vytvorte novú vetvu z `main`
2. **Vykonajte svoje zmeny** podľa štýlových pokynov pre kód
3. **Dôkladne otestujte** pomocou pokynov na testovanie vyššie
4. **Commitujte s jasnými správami** podľa formátu konvenčných commitov
5. **Pushnite do svojho forku** a vytvorte pull request
6. **Reagujte na spätnú väzbu** od správcov počas revízie

### Konvencia pomenovania vetiev

- `feature/<modul>-<popis>` - Pre nové funkcie alebo obsah
- `fix/<modul>-<popis>` - Pre opravy chýb
- `docs/<popis>` - Pre vylepšenia dokumentácie
- `refactor/<popis>` - Pre refaktoring kódu

### Formát správy commitov

Dodržiavajte [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Príklady:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Formát názvu
```
[ModuleXX] Brief description of change
```
alebo
```
[Module08/samples/XX] Description for sample changes
```

### Kódex správania

Všetci prispievatelia musia dodržiavať [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Pred prispievaním si prosím preštudujte [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

### Pred odoslaním

**Pre zmeny obsahu:**
- Náhľad všetkých upravených Markdown súborov
- Overte odkazy a obrázky
- Skontrolujte pravopisné a gramatické chyby

**Pre zmeny ukážkového kódu (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Pre zmeny Python ukážok:**
- Otestujte, že ukážka sa úspešne spustí
- Overte, že spracovanie chýb funguje
- Skontrolujte kompatibilitu s Foundry Local

### Proces revízie

- Zmeny vzdelávacieho obsahu sú kontrolované na presnosť a jasnosť
- Ukážky kódu sú testované na funkčnosť
- Aktualizácie prekladov sú spracované automaticky pomocou GitHub Actions

## Systém prekladu

**DÔLEŽITÉ:** Tento repozitár používa automatizovaný preklad prostredníctvom GitHub Actions.

- Preklady sú v adresári `/translations/` (50+ jazykov)
- Automatizované prostredníctvom workflowu `co-op-translator.yml`
- **NEUPRAVUJTE manuálne prekladové súbory** - budú prepísané
- Upravujte iba anglické zdrojové súbory v koreňovom adresári a adresároch modulov
- Preklady sa automaticky generujú pri pushnutí do vetvy `main`

## Integrácia Foundry Local

Väčšina ukážok z Modulu08 vyžaduje, aby bol Microsoft Foundry Local spustený.

### Inštalácia a nastavenie

**Inštalácia Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Inštalácia Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Spustenie Foundry Local
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

### Použitie SDK (Python)
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

### Overenie Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Premenné prostredia pre ukážky

Väčšina ukážok používa tieto premenné prostredia:
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

**Poznámka**: Pri použití `FoundryLocalManager` SDK automaticky spracováva objavovanie služieb a načítanie modelov. Alias modelov (napr. `phi-3.5-mini`) zabezpečuje výber najlepšej varianty pre váš hardvér.

## Build a nasadenie

### Nasadenie obsahu

Tento repozitár je primárne dokumentácia - nie je potrebný žiadny proces buildovania pre obsah.

### Build ukážkových aplikácií

**Electron aplikácia (Module08/samples/08):**
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

**Python ukážky:**
Nie je potrebný proces buildovania - ukážky sa spúšťajú priamo pomocou Python interpretera.

## Bežné problémy a riešenie problémov

> **Tip**: Skontrolujte [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) pre známe problémy a riešenia.

### Kritické problémy (blokujúce)

#### Foundry Local nie je spustený
**Problém:** Ukážky zlyhávajú s chybami pripojenia

**Riešenie:**
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

### Bežné problémy (stredné)

#### Problémy s Python virtuálnym prostredím
**Problém:** Chyby pri importe modulov

**Riešenie:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Problémy s buildom Electron
**Problém:** npm install alebo build zlyháva

**Riešenie:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Problémy s pracovným postupom (menšie)

#### Konflikty pracovného postupu prekladu
**Problém:** Konflikty PR prekladu s vašimi zmenami

**Riešenie:**
- Upravujte iba anglické zdrojové súbory
- Nechajte automatizovaný pracovný postup prekladu spracovať preklady
- Ak nastanú konflikty, zlúčte `main` do svojej vetvy po zlúčení prekladov

#### Zlyhania pri sťahovaní modelov
**Problém:** Foundry Local zlyháva pri sťahovaní modelov

**Riešenie:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Dodatočné zdroje

### Vzdelávacie cesty
- **Cesta pre začiatočníkov:** Moduly 01-02 (7-9 hodín)
- **Cesta pre pokročilých:** Moduly 03-04 (9-11 hodín)
- **Cesta pre expertov:** Moduly 05-07 (12-15 hodín)
- **Cesta pre profesionálov:** Modul 08 (8-10 hodín)

### Kľúčový obsah modulov
- **Modul01:** Základy EdgeAI a prípadové štúdie z reálneho sveta
- **Modul02:** Rodiny a architektúry malých jazykových modelov (SLM)
- **Modul03:** Lokálne a cloudové stratégie nasadenia
- **Modul04:** Optimalizácia modelov s viacerými rámcami
- **Modul05:** SLMOps - operácie v produkcii
- **Modul06:** AI agenti a volanie funkcií
- **Modul07:** Implementácie špecifické pre platformu
- **Modul08:** Nástroj Foundry Local s 10 komplexnými ukážkami

### Externé závislosti
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Lokálny runtime AI modelov s OpenAI-kompatibilným API
  - [Dokumentácia](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimalizačný rámec
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Nástroj na optimalizáciu modelov
- [OpenVINO](https://docs.openvino.ai/) - Intelov nástroj na optimalizáciu

## Poznámky špecifické pre projekt

### Ukážkové aplikácie Modulu08

Repozitár obsahuje 10 komplexných ukážkových aplikácií:

1. **01-REST Chat Quickstart** - Základná integrácia OpenAI SDK
2. **02-OpenAI SDK Integration** - Pokročilé funkcie SDK
3. **03-Model Discovery & Benchmarking** - Nástroje na porovnávanie modelov
4. **04-Chainlit RAG Application** - Generácia s podporou vyhľadávania
5. **05-Multi-Agent Orchestration** - Základná koordinácia agentov
6. **06-Models-as-Tools Router** - Inteligentné smerovanie modelov
7. **07
- Lokálna inferencia poskytuje odozvu v rozmedzí 50-500 ms
- Kvantizačné techniky dosahujú 75% zníženie veľkosti pri zachovaní 85% výkonu
- Schopnosti pre konverzáciu v reálnom čase s lokálnymi modelmi

### Bezpečnosť a súkromie

- Všetko spracovanie prebieha lokálne - žiadne dáta sa neposielajú do cloudu
- Vhodné pre aplikácie citlivé na súkromie (zdravotníctvo, financie)
- Spĺňa požiadavky na suverenitu dát
- Foundry Local beží výhradne na lokálnom hardvéri

## Získanie pomoci

### Dokumentácia

- **Hlavný README**: [README.md](README.md) - Prehľad repozitára a učebné cesty
- **Študijný sprievodca**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Učebné zdroje a časový plán
- **Podpora**: [SUPPORT.md](SUPPORT.md) - Ako získať pomoc
- **Bezpečnosť**: [SECURITY.md](SECURITY.md) - Nahlasovanie bezpečnostných problémov

### Podpora komunity

- **GitHub Issues**: [Nahlásiť chyby alebo požiadať o funkcie](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Pýtať sa otázky a zdieľať nápady](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Technické problémy s Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Kontakt

- **Správcovia**: Pozrite si [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Bezpečnostné problémy**: Postupujte podľa zodpovedného nahlasovania v [SECURITY.md](SECURITY.md)
- **Podpora od Microsoftu**: Pre podnikové služby kontaktujte zákaznícky servis Microsoftu

### Ďalšie zdroje

- **Microsoft Learn**: [Učebné cesty pre AI a strojové učenie](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Dokumentácia**: [Oficiálna dokumentácia](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Ukážky komunity**: Pozrite si [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) pre príspevky od komunity

---

**Toto je vzdelávací repozitár zameraný na výučbu vývoja Edge AI. Hlavným príspevkovým vzorom je zlepšovanie vzdelávacieho obsahu a pridávanie/vylepšovanie ukážkových aplikácií, ktoré demonštrujú koncepty Edge AI.**

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.