<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:46:00+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hr"
}
-->
# AGENTS.md

## Pregled projekta

EdgeAI za početnike je sveobuhvatan edukacijski repozitorij koji podučava razvoj Edge AI-a koristeći male jezične modele (SLM-ove). Tečaj pokriva osnove EdgeAI-a, implementaciju modela, tehnike optimizacije i proizvodno spremne implementacije koristeći Microsoft Foundry Local i razne AI okvire.

**Ključne tehnologije:**
- Python 3.8+ (primarni jezik za AI/ML primjere)
- .NET C# (AI/ML primjeri)
- JavaScript/Node.js s Electronom (za desktop aplikacije)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI okviri: LangChain, Semantic Kernel, Chainlit
- Optimizacija modela: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Vrsta repozitorija:** Edukacijski sadržaj s 8 modula i 10 sveobuhvatnih uzoraka aplikacija

**Arhitektura:** Višemodulski put učenja s praktičnim primjerima koji demonstriraju obrasce implementacije Edge AI-a

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

## Postavljanje naredbi

### Postavljanje repozitorija

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Postavljanje Python primjera (Modul08 i Python primjeri)

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

### Postavljanje Node.js primjera (Primjer 08 - Windows Chat App)

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

### Postavljanje Foundry Local

Foundry Local je potreban za pokretanje primjera iz Modula08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Radni tijek razvoja

### Razvoj sadržaja

Ovaj repozitorij primarno sadrži **edukacijski sadržaj u Markdownu**. Prilikom izmjena:

1. Uredite `.md` datoteke u odgovarajućim direktorijima modula
2. Slijedite postojeće obrasce formatiranja
3. Osigurajte da su primjeri koda točni i testirani
4. Ažurirajte odgovarajući prevedeni sadržaj ako je potrebno (ili prepustite automatizaciji)

### Razvoj uzoraka aplikacija

Za Python primjere (primjeri 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Za Electron primjer (primjer 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testiranje uzoraka aplikacija

Python primjeri nemaju automatizirane testove, ali se mogu provjeriti pokretanjem:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron primjer ima infrastrukturu za testiranje:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Upute za testiranje

### Validacija sadržaja

Repozitorij koristi automatizirane radne tijekove za prijevod. Nije potrebno ručno testiranje prijevoda.

**Ručno testiranje izmjena sadržaja:**
1. Pregledajte prikaz Markdown datoteka
2. Provjerite da svi linkovi vode na valjane ciljeve
3. Testirajte sve uključene isječke koda
4. Provjerite da se slike ispravno učitavaju

### Testiranje uzoraka aplikacija

**Modul08/primjeri/08 (Electron aplikacija) ima sveobuhvatno testiranje:**
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

**Python primjeri trebaju se ručno testirati:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Smjernice za stil koda

### Markdown sadržaj

- Koristite dosljednu hijerarhiju naslova (# za naslov, ## za glavne sekcije, ### za podsekcije)
- Uključite blokove koda s oznakama jezika: ```python, ```bash, ```javascript
- Slijedite postojeće formatiranje za tablice, liste i naglašavanje
- Održavajte čitljivost linija (~80-100 znakova, ali nije strogo)
- Koristite relativne linkove za interne reference

### Python stil koda

- Slijedite PEP 8 konvencije
- Koristite tipne oznake gdje je prikladno
- Uključite docstringove za funkcije i klase
- Koristite smislena imena varijabli
- Održavajte funkcije fokusiranim i sažetim

### JavaScript/Node.js stil koda

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Ključne konvencije:**
- ESLint konfiguracija uključena u primjer 08
- Prettier za formatiranje koda
- Koristite modernu ES6+ sintaksu
- Slijedite postojeće obrasce u kodnoj bazi

## Smjernice za Pull Requestove

### Format naslova
```
[ModuleXX] Brief description of change
```
ili
```
[Module08/samples/XX] Description for sample changes
```

### Prije slanja

**Za izmjene sadržaja:**
- Pregledajte sve izmijenjene Markdown datoteke
- Provjerite da linkovi i slike rade
- Provjerite pravopisne i gramatičke pogreške

**Za izmjene uzoraka koda (Modul08/primjeri/08):**
```bash
npm run lint
npm test
```

**Za izmjene Python primjera:**
- Testirajte da se primjer uspješno pokreće
- Provjerite da rukovanje greškama radi
- Provjerite kompatibilnost s Foundry Local

### Proces pregleda

- Izmjene edukacijskog sadržaja pregledavaju se radi točnosti i jasnoće
- Uzorci koda testiraju se radi funkcionalnosti
- Ažuriranja prijevoda automatski obrađuje GitHub Actions

## Sustav za prijevod

**VAŽNO:** Ovaj repozitorij koristi automatizirani prijevod putem GitHub Actions.

- Prijevodi se nalaze u direktoriju `/translations/` (50+ jezika)
- Automatizirano putem `co-op-translator.yml` radnog tijeka
- **NE uređujte ručno datoteke prijevoda** - bit će prepisane
- Uređujte samo izvorne datoteke na engleskom u rootu i direktorijima modula
- Prijevodi se automatski generiraju prilikom pushanja na `main` granu

## Integracija Foundry Local

Većina primjera iz Modula08 zahtijeva pokretanje Microsoft Foundry Local:

### Pokretanje Foundry Local
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

### Provjera Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Varijable okruženja za primjere

Većina primjera koristi ove varijable okruženja:
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

## Izgradnja i implementacija

### Implementacija sadržaja

Ovaj repozitorij primarno sadrži dokumentaciju - nije potreban proces izgradnje za sadržaj.

### Izgradnja uzoraka aplikacija

**Electron aplikacija (Modul08/primjeri/08):**
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

**Python primjeri:**
Nema procesa izgradnje - primjeri se pokreću izravno s Python interpreterom.

## Uobičajeni problemi i rješavanje

### Foundry Local nije pokrenut
**Problem:** Primjeri ne rade zbog grešaka u povezivanju

**Rješenje:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Problemi s Python virtualnim okruženjem
**Problem:** Greške pri uvozu modula

**Rješenje:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Problemi s izgradnjom Electron aplikacije
**Problem:** Greške pri npm install ili izgradnji

**Rješenje:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Sukobi u radnom tijeku prijevoda
**Problem:** Prijevodni PR u sukobu s vašim izmjenama

**Rješenje:**
- Uređujte samo izvorne datoteke na engleskom
- Prepustite automatiziranom radnom tijeku da obradi prijevode
- Ako dođe do sukoba, spojite `main` u svoju granu nakon što se prijevodi spoje

## Dodatni resursi

### Putovi učenja
- **Put za početnike:** Moduli 01-02 (7-9 sati)
- **Put za srednji nivo:** Moduli 03-04 (9-11 sati)
- **Put za napredni nivo:** Moduli 05-07 (12-15 sati)
- **Put za stručnjake:** Modul 08 (8-10 sati)

### Ključni sadržaj modula
- **Modul01:** Osnove EdgeAI-a i studije slučaja iz stvarnog svijeta
- **Modul02:** Obitelji i arhitekture malih jezičnih modela (SLM)
- **Modul03:** Strategije lokalne i cloud implementacije
- **Modul04:** Optimizacija modela s više okvira
- **Modul05:** SLMOps - operacije u produkciji
- **Modul06:** AI agenti i pozivanje funkcija
- **Modul07:** Implementacije specifične za platformu
- **Modul08:** Foundry Local alatni set s 10 sveobuhvatnih primjera

### Vanjske ovisnosti
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Lokalni runtime za AI modele
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Okvir za optimizaciju
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Alat za optimizaciju modela
- [OpenVINO](https://docs.openvino.ai/) - Intelov alat za optimizaciju

## Napomene specifične za projekt

### Primjeri aplikacija iz Modula08

Repozitorij uključuje 10 sveobuhvatnih primjera aplikacija:

1. **01-REST Chat Quickstart** - Osnovna integracija OpenAI SDK-a
2. **02-OpenAI SDK Integration** - Napredne značajke SDK-a
3. **03-Model Discovery & Benchmarking** - Alati za usporedbu modela
4. **04-Chainlit RAG Application** - Generacija uz pomoć pretraživanja
5. **05-Multi-Agent Orchestration** - Osnovna koordinacija agenata
6. **06-Models-as-Tools Router** - Inteligentno usmjeravanje modela
7. **07-Direct API Client** - Niskorazinska integracija API-ja
8. **08-Windows 11 Chat App** - Nativna Electron desktop aplikacija
9. **09-Advanced Multi-Agent System** - Složena orkestracija agenata
10. **10-Foundry Tools Framework** - Integracija LangChain/Semantic Kernel

Svaki primjer demonstrira različite aspekte razvoja Edge AI-a s Foundry Local.

### Razmatranja performansi

- SLM-ovi su optimizirani za implementaciju na rubu (2-16GB RAM-a)
- Lokalna inferencija pruža vrijeme odziva od 50-500ms
- Tehnike kvantizacije postižu smanjenje veličine od 75% uz zadržavanje 85% performansi
- Mogućnosti razgovora u stvarnom vremenu s lokalnim modelima

### Sigurnost i privatnost

- Sva obrada odvija se lokalno - nema slanja podataka u cloud
- Pogodno za aplikacije osjetljive na privatnost (zdravstvo, financije)
- Zadovoljava zahtjeve za suverenitetom podataka
- Foundry Local radi isključivo na lokalnom hardveru

---

**Ovo je edukacijski repozitorij usmjeren na podučavanje razvoja Edge AI-a. Primarni obrazac doprinosa je poboljšanje edukacijskog sadržaja i dodavanje/poboljšanje uzoraka aplikacija koje demonstriraju koncepte Edge AI-a.**

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.