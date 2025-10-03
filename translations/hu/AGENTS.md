<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:42:14+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hu"
}
-->
# AGENTS.md

## Projekt áttekintése

Az EdgeAI for Beginners egy átfogó oktatási gyűjtemény, amely az Edge AI fejlesztését tanítja Kis Nyelvi Modellekkel (SLM-ek). A kurzus az EdgeAI alapjait, modell telepítést, optimalizálási technikákat és gyártásra kész megvalósításokat tárgyalja a Microsoft Foundry Local és különböző AI keretrendszerek használatával.

**Kulcstechnológiák:**
- Python 3.8+ (AI/ML minták elsődleges nyelve)
- .NET C# (AI/ML minták)
- JavaScript/Node.js Electronnal (asztali alkalmazásokhoz)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI keretrendszerek: LangChain, Semantic Kernel, Chainlit
- Modell optimalizálás: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Gyűjtemény típusa:** Oktatási tartalom gyűjtemény 8 modul és 10 átfogó mintaprogrammal

**Architektúra:** Több modulból álló tanulási útvonal gyakorlati mintákkal, amelyek bemutatják az Edge AI telepítési mintákat

## Gyűjtemény felépítése

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

## Telepítési parancsok

### Gyűjtemény telepítése

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python minták telepítése (08. modul és Python minták)

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

### Node.js minták telepítése (08. minta - Windows Chat App)

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

### Foundry Local telepítése

A Foundry Local szükséges a 08. modul mintáinak futtatásához:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Fejlesztési munkafolyamat

### Tartalom fejlesztése

Ez a gyűjtemény elsősorban **Markdown oktatási tartalmat** tartalmaz. Változtatások esetén:

1. Szerkessze a `.md` fájlokat a megfelelő modul könyvtárakban
2. Kövesse a meglévő formázási mintákat
3. Biztosítsa, hogy a kódpéldák pontosak és teszteltek legyenek
4. Frissítse a megfelelő fordított tartalmat, ha szükséges (vagy hagyja, hogy az automatizálás kezelje)

### Mintaprogram fejlesztése

Python mintákhoz (01-07, 09-10 minták):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron mintához (08. minta):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Mintaprogramok tesztelése

A Python minták nem rendelkeznek automatizált tesztekkel, de futtatással ellenőrizhetők:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Az Electron mintának van teszt infrastruktúrája:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Tesztelési utasítások

### Tartalom ellenőrzése

A gyűjtemény automatizált fordítási munkafolyamatokat használ. A fordítások manuális tesztelése nem szükséges.

**Manuális ellenőrzés tartalomváltozások esetén:**
1. Ellenőrizze a Markdown megjelenítést `.md` fájlok előnézetével
2. Győződjön meg arról, hogy minden hivatkozás érvényes célra mutat
3. Tesztelje a dokumentációban szereplő kódrészleteket
4. Ellenőrizze, hogy a képek helyesen töltődnek be

### Mintaprogramok tesztelése

**08. modul/minták/08 (Electron alkalmazás) átfogó tesztelést tartalmaz:**
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

**Python mintákat manuálisan kell tesztelni:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Kódstílus irányelvek

### Markdown tartalom

- Használjon következetes címsor hierarchiát (# a címhez, ## a fő szakaszokhoz, ### az alfejezetekhez)
- Tartalmazzon kódrészleteket nyelvi megjelöléssel: ```python, ```bash, ```javascript
- Kövesse a meglévő formázást táblázatok, listák és kiemelések esetén
- Tartsa olvasható sorokat (~80-100 karakter, de nem szigorú)
- Használjon relatív hivatkozásokat belső referenciákhoz

### Python kódstílus

- Kövesse a PEP 8 konvenciókat
- Használjon típusjelöléseket, ahol megfelelő
- Tartalmazzon docstringeket a függvényekhez és osztályokhoz
- Használjon értelmes változóneveket
- Tartsa a függvényeket fókuszáltan és tömören

### JavaScript/Node.js kódstílus

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Kulcskonvenciók:**
- ESLint konfiguráció biztosított a 08. mintában
- Prettier a kódformázáshoz
- Használjon modern ES6+ szintaxist
- Kövesse a meglévő mintákat a kódbázisban

## Pull Request irányelvek

### Cím formátuma
```
[ModuleXX] Brief description of change
```
vagy
```
[Module08/samples/XX] Description for sample changes
```

### Beküldés előtt

**Tartalomváltozások esetén:**
- Tekintse meg az összes módosított Markdown fájlt
- Ellenőrizze a hivatkozások és képek működését
- Ellenőrizze a helyesírási és nyelvtani hibákat

**Mintakód változások esetén (08. modul/minták/08):**
```bash
npm run lint
npm test
```

**Python minták változásai esetén:**
- Tesztelje, hogy a minta sikeresen fut
- Ellenőrizze a hibakezelés működését
- Ellenőrizze a kompatibilitást a Foundry Local-lal

### Áttekintési folyamat

- Oktatási tartalom változásait pontosság és érthetőség szempontjából vizsgálják
- Mintakódokat funkcionalitás szempontjából tesztelik
- Fordítási frissítéseket automatikusan a GitHub Actions kezeli

## Fordítási rendszer

**FONTOS:** Ez a gyűjtemény automatizált fordítást használ a GitHub Actions segítségével.

- A fordítások a `/translations/` könyvtárban találhatók (50+ nyelv)
- Automatizált a `co-op-translator.yml` munkafolyamat által
- **NE szerkessze manuálisan a fordítási fájlokat** - felülíródnak
- Csak az angol forrásfájlokat szerkessze a gyökérben és a modul könyvtárakban
- A fordítások automatikusan generálódnak a `main` ágra történő push esetén

## Foundry Local integráció

A legtöbb 08. modul minta futtatásához szükséges a Microsoft Foundry Local:

### Foundry Local indítása
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

### Foundry Local ellenőrzése
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Környezeti változók mintákhoz

A legtöbb minta ezeket a környezeti változókat használja:
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

## Építés és telepítés

### Tartalom telepítése

Ez a gyűjtemény elsősorban dokumentáció - nincs szükség építési folyamatra a tartalomhoz.

### Mintaprogram építése

**Electron alkalmazás (08. modul/minták/08):**
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

**Python minták:**
Nincs építési folyamat - a minták közvetlenül a Python interpreterrel futtathatók.

## Gyakori problémák és hibaelhárítás

### Foundry Local nem fut
**Probléma:** Minták csatlakozási hibákkal meghiúsulnak

**Megoldás:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python virtuális környezet problémák
**Probléma:** Modul importálási hibák

**Megoldás:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron építési problémák
**Probléma:** npm install vagy építési hibák

**Megoldás:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Fordítási munkafolyamat konfliktusok
**Probléma:** A fordítási PR ütközik az Ön változásaival

**Megoldás:**
- Csak az angol forrásfájlokat szerkessze
- Hagyja, hogy az automatizált fordítási munkafolyamat kezelje a fordításokat
- Ha konfliktusok lépnek fel, egyesítse a `main` ágat az ágába, miután a fordítások egyesítve lettek

## További források

### Tanulási útvonalak
- **Kezdő útvonal:** 01-02 modulok (7-9 óra)
- **Középhaladó útvonal:** 03-04 modulok (9-11 óra)
- **Haladó útvonal:** 05-07 modulok (12-15 óra)
- **Szakértői útvonal:** 08. modul (8-10 óra)

### Kulcsmodul tartalom
- **01. modul:** EdgeAI alapok és valós esettanulmányok
- **02. modul:** Kis Nyelvi Modellek (SLM-ek) családjai és architektúrái
- **03. modul:** Helyi és felhő telepítési stratégiák
- **04. modul:** Modell optimalizálás több keretrendszerrel
- **05. modul:** SLMOps - gyártási műveletek
- **06. modul:** AI ügynökök és funkcióhívások
- **07. modul:** Platform-specifikus megvalósítások
- **08. modul:** Foundry Local eszközkészlet 10 átfogó mintával

### Külső függőségek
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Helyi AI modell futtatókörnyezet
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimalizációs keretrendszer
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Modell optimalizálási eszközkészlet
- [OpenVINO](https://docs.openvino.ai/) - Intel optimalizációs eszközkészlet

## Projekt-specifikus megjegyzések

### 08. modul mintaprogramok

A gyűjtemény 10 átfogó mintaprogramot tartalmaz:

1. **01-REST Chat Quickstart** - Alapvető OpenAI SDK integráció
2. **02-OpenAI SDK Integration** - Fejlett SDK funkciók
3. **03-Model Discovery & Benchmarking** - Modell összehasonlító eszközök
4. **04-Chainlit RAG Application** - Visszakeresés-alapú generáció
5. **05-Multi-Agent Orchestration** - Alapvető ügynök koordináció
6. **06-Models-as-Tools Router** - Intelligens modellirányítás
7. **07-Direct API Client** - Alacsony szintű API integráció
8. **08-Windows 11 Chat App** - Natív Electron asztali alkalmazás
9. **09-Advanced Multi-Agent System** - Komplex ügynök koordináció
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel integráció

Minden minta az Edge AI fejlesztés különböző aspektusait mutatja be Foundry Local használatával.

### Teljesítmény szempontok

- Az SLM-ek optimalizálva vannak Edge telepítésre (2-16GB RAM)
- Helyi következtetés 50-500ms válaszidőt biztosít
- Kvantálási technikák 75%-os méretcsökkentést érnek el 85%-os teljesítménymegtartással
- Valós idejű beszélgetési képességek helyi modellekkel

### Biztonság és adatvédelem

- Minden feldolgozás helyben történik - nincs adatküldés a felhőbe
- Alkalmas adatvédelmi szempontból érzékeny alkalmazásokhoz (egészségügy, pénzügy)
- Megfelel az adat szuverenitási követelményeknek
- A Foundry Local teljes mértékben helyi hardveren fut

---

**Ez egy oktatási gyűjtemény, amely az Edge AI fejlesztés tanítására fókuszál. Az elsődleges hozzájárulási minta az oktatási tartalom javítása és olyan mintaprogramok hozzáadása/fejlesztése, amelyek bemutatják az Edge AI koncepciókat.**

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.