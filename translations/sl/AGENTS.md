<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:46:35+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sl"
}
-->
# AGENTS.md

## Pregled projekta

EdgeAI za začetnike je obsežen izobraževalni repozitorij, ki poučuje razvoj Edge AI z majhnimi jezikovnimi modeli (SLM). Tečaj pokriva osnove EdgeAI, uvajanje modelov, tehnike optimizacije in implementacije, pripravljene za produkcijo, z uporabo Microsoft Foundry Local in različnih AI ogrodij.

**Ključne tehnologije:**
- Python 3.8+ (glavni jezik za vzorce AI/ML)
- .NET C# (vzorce AI/ML)
- JavaScript/Node.js z Electron (za namizne aplikacije)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI ogrodja: LangChain, Semantic Kernel, Chainlit
- Optimizacija modelov: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Tip repozitorija:** Izobraževalni repozitorij z 8 moduli in 10 obsežnimi vzorčnimi aplikacijami

**Arhitektura:** Učno potovanje z več moduli, ki vključuje praktične vzorce za prikaz vzorcev uvajanja Edge AI

## Struktura repozitorija

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

## Ukazi za nastavitev

### Nastavitev repozitorija

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Nastavitev Python vzorcev (Modul08 in Python vzorci)

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

### Nastavitev Node.js vzorcev (Vzorec 08 - Windows Chat App)

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

### Nastavitev Foundry Local

Foundry Local je potreben za zagon vzorcev Modula08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Potek razvoja

### Razvoj vsebine

Ta repozitorij vsebuje predvsem **Markdown izobraževalno vsebino**. Pri spreminjanju:

1. Uredite `.md` datoteke v ustreznih direktorijih modulov
2. Upoštevajte obstoječe vzorce oblikovanja
3. Poskrbite, da so primeri kode točni in preizkušeni
4. Posodobite ustrezno prevedeno vsebino, če je potrebno (ali naj to opravi avtomatizacija)

### Razvoj vzorčnih aplikacij

Za Python vzorce (vzorce 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Za Electron vzorec (vzorec 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testiranje vzorčnih aplikacij

Python vzorci nimajo avtomatiziranih testov, vendar jih je mogoče preveriti z zagonom:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron vzorec ima infrastrukturo za testiranje:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Navodila za testiranje

### Validacija vsebine

Repozitorij uporablja avtomatizirane prevajalske delovne tokove. Ročno testiranje prevodov ni potrebno.

**Ročna validacija sprememb vsebine:**
1. Preglejte prikaz Markdown datotek
2. Preverite, ali vse povezave vodijo na veljavne cilje
3. Testirajte vse kode, vključene v dokumentacijo
4. Preverite, ali se slike pravilno nalagajo

### Testiranje vzorčnih aplikacij

**Module08/samples/08 (Electron aplikacija) ima obsežno testiranje:**
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

**Python vzorce je treba ročno testirati:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Smernice za slog kode

### Markdown vsebina

- Uporabljajte dosledno hierarhijo naslovov (# za naslov, ## za glavne razdelke, ### za podrazdelke)
- Vključite kode z določenimi jezikovnimi oznakami: ```python, ```bash, ```javascript
- Upoštevajte obstoječe oblikovanje za tabele, sezname in poudarke
- Naj bodo vrstice berljive (cilj ~80-100 znakov, vendar ne strogo)
- Uporabljajte relativne povezave za notranje reference

### Slog Python kode

- Upoštevajte konvencije PEP 8
- Uporabljajte tipe, kjer je primerno
- Vključite docstrings za funkcije in razrede
- Uporabljajte smiselna imena spremenljivk
- Naj bodo funkcije osredotočene in jedrnate

### Slog JavaScript/Node.js kode

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Ključne konvencije:**
- ESLint konfiguracija je vključena v vzorec 08
- Prettier za oblikovanje kode
- Uporabljajte sodobno sintakso ES6+
- Upoštevajte obstoječe vzorce v kodi

## Smernice za zahteve za združitev (Pull Request)

### Format naslova
```
[ModuleXX] Brief description of change
```
ali
```
[Module08/samples/XX] Description for sample changes
```

### Pred oddajo

**Za spremembe vsebine:**
- Predogled vseh spremenjenih Markdown datotek
- Preverite, ali povezave in slike delujejo
- Preverite tipkarske napake in slovnične napake

**Za spremembe vzorčne kode (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Za spremembe Python vzorcev:**
- Preverite, ali vzorec uspešno deluje
- Preverite delovanje obravnave napak
- Preverite združljivost z Foundry Local

### Postopek pregleda

- Spremembe izobraževalne vsebine se pregledajo glede točnosti in jasnosti
- Vzorčne kode se testirajo glede funkcionalnosti
- Posodobitve prevodov se obravnavajo samodejno prek GitHub Actions

## Sistem prevajanja

**POMEMBNO:** Ta repozitorij uporablja avtomatizirano prevajanje prek GitHub Actions.

- Prevedene datoteke so v direktoriju `/translations/` (50+ jezikov)
- Avtomatizirano prek delovnega toka `co-op-translator.yml`
- **NE urejajte ročno prevedenih datotek** - te bodo prepisane
- Urejajte samo izvorne datoteke v angleščini v korenskem in modulskih direktorijih
- Prevajanja se samodejno ustvarijo ob potisku v vejo `main`

## Integracija Foundry Local

Večina vzorcev Modula08 zahteva, da je Microsoft Foundry Local zagnan:

### Zagon Foundry Local
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

### Preverjanje Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Spremenljivke okolja za vzorce

Večina vzorcev uporablja te spremenljivke okolja:
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

## Gradnja in uvajanje

### Uvajanje vsebine

Ta repozitorij je predvsem dokumentacija - proces gradnje za vsebino ni potreben.

### Gradnja vzorčnih aplikacij

**Electron aplikacija (Module08/samples/08):**
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

**Python vzorci:**
Proces gradnje ni potreben - vzorci se izvajajo neposredno z interpreterjem Python.

## Pogoste težave in odpravljanje napak

### Foundry Local ni zagnan
**Težava:** Vzorci ne uspejo zaradi napak povezave

**Rešitev:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Težave z virtualnim okoljem Python
**Težava:** Napake pri uvozu modulov

**Rešitev:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Težave pri gradnji Electron
**Težava:** Napake pri `npm install` ali gradnji

**Rešitev:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Konflikti pri prevajalskem delovnem toku
**Težava:** Konflikti prevajalskih PR-jev z vašimi spremembami

**Rešitev:**
- Urejajte samo izvorne datoteke v angleščini
- Naj avtomatizirani prevajalski delovni tok obravnava prevode
- Če pride do konfliktov, združite `main` v svojo vejo po združitvi prevodov

## Dodatni viri

### Učne poti
- **Pot za začetnike:** Moduli 01-02 (7-9 ur)
- **Pot za srednje izkušene:** Moduli 03-04 (9-11 ur)
- **Pot za napredne:** Moduli 05-07 (12-15 ur)
- **Pot za strokovnjake:** Modul 08 (8-10 ur)

### Ključna vsebina modulov
- **Modul01:** Osnove EdgeAI in študije primerov iz resničnega sveta
- **Modul02:** Družine in arhitekture majhnih jezikovnih modelov (SLM)
- **Modul03:** Strategije uvajanja lokalno in v oblaku
- **Modul04:** Optimizacija modelov z več ogrodji
- **Modul05:** SLMOps - operacije v produkciji
- **Modul06:** AI agenti in klicanje funkcij
- **Modul07:** Implementacije specifične za platformo
- **Modul08:** Orodja Foundry Local z 10 obsežnimi vzorci

### Zunanje odvisnosti
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Lokalni runtime za AI modele
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Ogrodje za optimizacijo
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Orodje za optimizacijo modelov
- [OpenVINO](https://docs.openvino.ai/) - Intelovo orodje za optimizacijo

## Opombe specifične za projekt

### Vzorčne aplikacije Modula08

Repozitorij vključuje 10 obsežnih vzorčnih aplikacij:

1. **01-REST Chat Quickstart** - Osnovna integracija OpenAI SDK
2. **02-OpenAI SDK Integration** - Napredne funkcije SDK
3. **03-Model Discovery & Benchmarking** - Orodja za primerjavo modelov
4. **04-Chainlit RAG Application** - Generacija, podprta z iskanjem
5. **05-Multi-Agent Orchestration** - Osnovna koordinacija agentov
6. **06-Models-as-Tools Router** - Inteligentno usmerjanje modelov
7. **07-Direct API Client** - Nizkoročnostna integracija API-ja
8. **08-Windows 11 Chat App** - Namizna aplikacija Electron
9. **09-Advanced Multi-Agent System** - Kompleksna orkestracija agentov
10. **10-Foundry Tools Framework** - Integracija LangChain/Semantic Kernel

Vsak vzorec prikazuje različne vidike razvoja Edge AI z Foundry Local.

### Premisleki o zmogljivosti

- SLM-ji so optimizirani za uvajanje na robu (2-16GB RAM)
- Lokalno sklepanje omogoča odzivne čase 50-500ms
- Tehnike kvantizacije dosežejo 75% zmanjšanje velikosti z 85% ohranitvijo zmogljivosti
- Zmožnosti pogovora v realnem času z lokalnimi modeli

### Varnost in zasebnost

- Vsa obdelava poteka lokalno - podatki se ne pošiljajo v oblak
- Primerno za aplikacije, občutljive na zasebnost (zdravstvo, finance)
- Izpolnjuje zahteve glede suverenosti podatkov
- Foundry Local deluje popolnoma na lokalni strojni opremi

---

**To je izobraževalni repozitorij, osredotočen na poučevanje razvoja Edge AI. Glavni vzorec prispevkov je izboljšanje izobraževalne vsebine in dodajanje/izboljšanje vzorčnih aplikacij, ki prikazujejo koncepte Edge AI.**

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.