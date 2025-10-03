<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:43:26+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sk"
}
-->
# AGENTS.md

## Prehľad projektu

EdgeAI for Beginners je komplexné vzdelávacie úložisko, ktoré učí vývoj Edge AI pomocou malých jazykových modelov (SLM). Kurz pokrýva základy EdgeAI, nasadenie modelov, optimalizačné techniky a implementácie pripravené na produkciu pomocou Microsoft Foundry Local a rôznych AI rámcov.

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

**Typ úložiska:** Vzdelávacie úložisko s 8 modulmi a 10 komplexnými ukážkovými aplikáciami

**Architektúra:** Viacmodulová vzdelávacia cesta s praktickými ukážkami nasadenia Edge AI

## Štruktúra úložiska

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

## Príkazy na nastavenie

### Nastavenie úložiska

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

# Install dependencies for Module08 samples
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

Foundry Local je potrebné na spustenie ukážok Modulu08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Pracovný postup vývoja

### Vývoj obsahu

Toto úložisko obsahuje primárne **Markdown vzdelávací obsah**. Pri vykonávaní zmien:

1. Upravte súbory `.md` v príslušných adresároch modulov
2. Dodržiavajte existujúce formátovacie vzory
3. Uistite sa, že ukážky kódu sú presné a otestované
4. Aktualizujte zodpovedajúci preložený obsah, ak je to potrebné (alebo nechajte automatizáciu, aby to spravila)

### Vývoj ukážkových aplikácií

Pre Python ukážky (ukážky 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Pre Electron ukážku (ukážka 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testovanie ukážkových aplikácií

Python ukážky nemajú automatizované testy, ale môžu byť overené ich spustením:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron ukážka má testovaciu infraštruktúru:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Pokyny na testovanie

### Validácia obsahu

Úložisko používa automatizované prekladové pracovné postupy. Manuálne testovanie prekladov nie je potrebné.

**Manuálna validácia zmien obsahu:**
1. Skontrolujte vykreslenie Markdownu náhľadom súborov `.md`
2. Overte, že všetky odkazy smerujú na platné ciele
3. Otestujte akékoľvek ukážky kódu zahrnuté v dokumentácii
4. Skontrolujte, či sa obrázky načítavajú správne

### Testovanie ukážkových aplikácií

**Modul08/ukážky/08 (Electron aplikácia) má komplexné testovanie:**
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

## Pokyny pre štýl kódu

### Markdown obsah

- Používajte konzistentnú hierarchiu nadpisov (# pre názov, ## pre hlavné sekcie, ### pre podsekcie)
- Zahrňte bloky kódu so špecifikátormi jazyka: ```python, ```bash, ```javascript
- Dodržiavajte existujúce formátovanie pre tabuľky, zoznamy a zvýraznenie
- Udržujte riadky čitateľné (cieľom je ~80-100 znakov, ale nie striktne)
- Používajte relatívne odkazy pre interné referencie

### Štýl Python kódu

- Dodržiavajte konvencie PEP 8
- Používajte typové náznaky, kde je to vhodné
- Zahrňte docstringy pre funkcie a triedy
- Používajte zmysluplné názvy premenných
- Udržujte funkcie zamerané a stručné

### Štýl JavaScript/Node.js kódu

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Kľúčové konvencie:**
- ESLint konfigurácia je poskytnutá v ukážke 08
- Prettier na formátovanie kódu
- Používajte modernú syntax ES6+
- Dodržiavajte existujúce vzory v kóde

## Pokyny pre Pull Requesty

### Formát názvu
```
[ModuleXX] Brief description of change
```
alebo
```
[Module08/samples/XX] Description for sample changes
```

### Pred odoslaním

**Pre zmeny obsahu:**
- Náhľad všetkých upravených Markdown súborov
- Overte funkčnosť odkazov a obrázkov
- Skontrolujte pravopisné a gramatické chyby

**Pre zmeny ukážkového kódu (Modul08/ukážky/08):**
```bash
npm run lint
npm test
```

**Pre zmeny Python ukážok:**
- Otestujte, či ukážka funguje úspešne
- Overte funkčnosť spracovania chýb
- Skontrolujte kompatibilitu s Foundry Local

### Proces kontroly

- Zmeny vzdelávacieho obsahu sú kontrolované na presnosť a jasnosť
- Ukážky kódu sú testované na funkčnosť
- Aktualizácie prekladov sú spracované automaticky pomocou GitHub Actions

## Systém prekladov

**DÔLEŽITÉ:** Toto úložisko používa automatizovaný preklad cez GitHub Actions.

- Preklady sú v adresári `/translations/` (50+ jazykov)
- Automatizované cez pracovný postup `co-op-translator.yml`
- **NEUPRAVUJTE manuálne prekladové súbory** - budú prepísané
- Upravujte iba anglické zdrojové súbory v koreňovom adresári a adresároch modulov
- Preklady sú automaticky generované pri pushnutí do vetvy `main`

## Integrácia Foundry Local

Väčšina ukážok Modulu08 vyžaduje, aby bol Microsoft Foundry Local spustený:

### Spustenie Foundry Local
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

### Overenie Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Premenné prostredia pre ukážky

Väčšina ukážok používa tieto premenné prostredia:
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

## Build a nasadenie

### Nasadenie obsahu

Toto úložisko je primárne dokumentácia - nie je potrebný žiadny proces buildovania pre obsah.

### Build ukážkových aplikácií

**Electron aplikácia (Modul08/ukážky/08):**
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
Nie je potrebný proces buildovania - ukážky sa spúšťajú priamo pomocou Python interpreteru.

## Bežné problémy a riešenie

### Foundry Local nie je spustený
**Problém:** Ukážky zlyhávajú s chybami pripojenia

**Riešenie:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Problémy s Python virtuálnym prostredím
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

### Problémy s buildom Electron aplikácie
**Problém:** npm install alebo chyby buildovania

**Riešenie:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Konflikty pracovného postupu prekladov
**Problém:** PR pre preklad je v konflikte s vašimi zmenami

**Riešenie:**
- Upravujte iba anglické zdrojové súbory
- Nechajte automatizovaný pracovný postup prekladov spracovať preklady
- Ak nastanú konflikty, zlúčte `main` do svojej vetvy po zlúčení prekladov

## Dodatočné zdroje

### Vzdelávacie cesty
- **Začiatočnícka cesta:** Moduly 01-02 (7-9 hodín)
- **Stredne pokročilá cesta:** Moduly 03-04 (9-11 hodín)
- **Pokročilá cesta:** Moduly 05-07 (12-15 hodín)
- **Expertná cesta:** Modul 08 (8-10 hodín)

### Kľúčový obsah modulov
- **Modul01:** Základy EdgeAI a prípadové štúdie z reálneho sveta
- **Modul02:** Rodiny a architektúry malých jazykových modelov (SLM)
- **Modul03:** Lokálne a cloudové stratégie nasadenia
- **Modul04:** Optimalizácia modelov s viacerými rámcami
- **Modul05:** SLMOps - operácie v produkcii
- **Modul06:** AI agenti a volanie funkcií
- **Modul07:** Implementácie špecifické pre platformu
- **Modul08:** Nástrojová sada Foundry Local s 10 komplexnými ukážkami

### Externé závislosti
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Lokálny runtime AI modelov
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimalizačný rámec
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Nástroj na optimalizáciu modelov
- [OpenVINO](https://docs.openvino.ai/) - Optimalizačný nástroj od Intelu

## Poznámky špecifické pre projekt

### Ukážkové aplikácie Modulu08

Úložisko obsahuje 10 komplexných ukážkových aplikácií:

1. **01-REST Chat Quickstart** - Základná integrácia OpenAI SDK
2. **02-OpenAI SDK Integration** - Pokročilé funkcie SDK
3. **03-Model Discovery & Benchmarking** - Nástroje na porovnanie modelov
4. **04-Chainlit RAG Application** - Generácia s podporou vyhľadávania
5. **05-Multi-Agent Orchestration** - Základná koordinácia agentov
6. **06-Models-as-Tools Router** - Inteligentné smerovanie modelov
7. **07-Direct API Client** - Nízkoúrovňová integrácia API
8. **08-Windows 11 Chat App** - Natívna Electron desktopová aplikácia
9. **09-Advanced Multi-Agent System** - Komplexná orchestrácia agentov
10. **10-Foundry Tools Framework** - Integrácia LangChain/Semantic Kernel

Každá ukážka demonštruje rôzne aspekty vývoja Edge AI s Foundry Local.

### Výkonnostné úvahy

- SLM sú optimalizované pre nasadenie na okraji (2-16GB RAM)
- Lokálne inferencie poskytujú odozvy 50-500ms
- Kvantizačné techniky dosahujú 75% zmenšenie veľkosti pri 85% zachovaní výkonu
- Schopnosti reálneho času pre konverzácie s lokálnymi modelmi

### Bezpečnosť a súkromie

- Všetko spracovanie prebieha lokálne - žiadne dáta sa neposielajú do cloudu
- Vhodné pre aplikácie citlivé na súkromie (zdravotníctvo, financie)
- Spĺňa požiadavky na suverenitu dát
- Foundry Local beží výhradne na lokálnom hardvéri

---

**Toto je vzdelávacie úložisko zamerané na výučbu vývoja Edge AI. Primárny vzor príspevkov je zlepšovanie vzdelávacieho obsahu a pridávanie/zlepšovanie ukážkových aplikácií, ktoré demonštrujú koncepty Edge AI.**

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.