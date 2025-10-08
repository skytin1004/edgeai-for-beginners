<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "135b2658979f1e494bb0ecc6e26d4752",
  "translation_date": "2025-10-08T13:54:21+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hr"
}
-->
# AGENTS.md

> **Vodič za razvoj za doprinos EdgeAI za početnike**
> 
> Ovaj dokument pruža sveobuhvatne informacije za programere, AI agente i suradnike koji rade s ovim repozitorijem. Pokriva postavljanje, razvojne tijekove rada, testiranje i najbolje prakse.
> 
> **Zadnje ažuriranje**: listopad 2025 | **Verzija dokumenta**: 2.0

## Sadržaj

- [Pregled projekta](../..)
- [Struktura repozitorija](../..)
- [Preduvjeti](../..)
- [Naredbe za postavljanje](../..)
- [Razvojni tijek rada](../..)
- [Upute za testiranje](../..)
- [Smjernice za stil kodiranja](../..)
- [Smjernice za zahtjeve za povlačenje](../..)
- [Sustav za prijevod](../..)
- [Integracija s Foundry Local](../..)
- [Izrada i implementacija](../..)
- [Uobičajeni problemi i rješavanje problema](../..)
- [Dodatni resursi](../..)
- [Napomene specifične za projekt](../..)
- [Dobivanje pomoći](../..)

## Pregled projekta

EdgeAI za početnike je sveobuhvatan edukacijski repozitorij koji podučava razvoj Edge AI-a s malim jezičnim modelima (SLM). Tečaj pokriva osnove EdgeAI-a, implementaciju modela, tehnike optimizacije i implementacije spremne za produkciju koristeći Microsoft Foundry Local i razne AI okvire.

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

**Arhitektura:** Višemodularni obrazovni put s praktičnim primjerima koji demonstriraju obrasce implementacije Edge AI-a

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

## Preduvjeti

### Potrebni alati

- **Python 3.8+** - Za AI/ML primjere i bilježnice
- **Node.js 16+** - Za uzorak aplikacije Electron
- **Git** - Za kontrolu verzija
- **Microsoft Foundry Local** - Za lokalno pokretanje AI modela

### Preporučeni alati

- **Visual Studio Code** - S ekstenzijama za Python, Jupyter i Pylance
- **Windows Terminal** - Za bolji rad u naredbenom retku (korisnici Windowsa)
- **Docker** - Za razvoj u kontejnerima (opcionalno)

### Sistemski zahtjevi

- **RAM**: Minimalno 8GB, preporučeno 16GB+ za scenarije s više modela
- **Prostor za pohranu**: 10GB+ slobodnog prostora za modele i ovisnosti
- **OS**: Windows 10/11, macOS 11+ ili Linux (Ubuntu 20.04+)
- **Hardver**: CPU s podrškom za AVX2; GPU (CUDA, Qualcomm NPU) opcionalno, ali preporučeno

### Preduvjeti znanja

- Osnovno razumijevanje programiranja u Pythonu
- Poznavanje rada s naredbenim retkom
- Razumijevanje AI/ML koncepata (za razvoj primjera)
- Git tijekovi rada i procesi zahtjeva za povlačenje

## Naredbe za postavljanje

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

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Postavljanje Node.js primjera (Uzorak 08 - Windows Chat aplikacija)

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

Foundry Local je potreban za pokretanje primjera. Preuzmite i instalirajte s službenog repozitorija:

**Instalacija:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Ručno**: Preuzmite s [stranice za izdanja](https://github.com/microsoft/Foundry-Local/releases)

**Brzi početak:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-3.5-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Napomena**: Foundry Local automatski odabire najbolju varijantu modela za vaš hardver (CUDA GPU, Qualcomm NPU ili CPU).

## Razvojni tijek rada

### Razvoj sadržaja

Ovaj repozitorij primarno sadrži **edukacijski sadržaj u Markdownu**. Prilikom izmjena:

1. Uredite `.md` datoteke u odgovarajućim direktorijima modula
2. Slijedite postojeće obrasce formatiranja
3. Osigurajte da su primjeri koda točni i testirani
4. Ažurirajte odgovarajući prevedeni sadržaj ako je potrebno (ili neka automatizacija to obavi)

### Razvoj uzoraka aplikacija

Za Python primjere (uzorci 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Za Electron uzorak (uzorak 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testiranje uzoraka aplikacija

Python primjeri nemaju automatizirane testove, ali se mogu validirati pokretanjem:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron uzorak ima infrastrukturu za testiranje:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Upute za testiranje

### Validacija sadržaja

Repozitorij koristi automatizirane tijekove rada za prijevod. Nije potrebno ručno testiranje prijevoda.

**Ručno testiranje promjena sadržaja:**
1. Pregledajte prikaz Markdown datoteka
2. Provjerite da svi linkovi vode na valjane ciljeve
3. Testirajte sve primjere koda uključene u dokumentaciju
4. Provjerite da se slike pravilno učitavaju

### Testiranje uzoraka aplikacija

**Module08/samples/08 (Electron aplikacija) ima sveobuhvatno testiranje:**
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

## Smjernice za stil kodiranja

### Markdown sadržaj

- Koristite dosljednu hijerarhiju naslova (# za naslov, ## za glavne sekcije, ### za podsekcije)
- Uključite blokove koda s oznakama jezika: ```python, ```bash, ```javascript
- Slijedite postojeće formatiranje za tablice, popise i naglaske
- Održavajte čitljivost redaka (~80-100 znakova, ali nije strogo)
- Koristite relativne linkove za interne reference

### Stil kodiranja u Pythonu

- Slijedite PEP 8 konvencije
- Koristite tipne oznake gdje je to prikladno
- Uključite docstrings za funkcije i klase
- Koristite smislena imena varijabli
- Održavajte funkcije fokusirane i sažete

### Stil kodiranja u JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Ključne konvencije:**
- Konfiguracija ESLint-a dostupna u uzorku 08
- Prettier za formatiranje koda
- Koristite modernu ES6+ sintaksu
- Slijedite postojeće obrasce u kodnoj bazi

## Smjernice za zahtjeve za povlačenje

### Tijek doprinosa

1. **Forkajte repozitorij** i kreirajte novu granu iz `main`
2. **Napravite promjene** slijedeći smjernice za stil kodiranja
3. **Temeljito testirajte** koristeći gore navedene upute za testiranje
4. **Commitajte s jasnim porukama** slijedeći format konvencionalnih commitova
5. **Pushajte na svoj fork** i kreirajte zahtjev za povlačenje
6. **Odgovarajte na povratne informacije** od održavatelja tijekom pregleda

### Konvencija za imenovanje grana

- `feature/<modul>-<opis>` - Za nove značajke ili sadržaj
- `fix/<modul>-<opis>` - Za ispravke grešaka
- `docs/<opis>` - Za poboljšanja dokumentacije
- `refactor/<opis>` - Za refaktoriranje koda

### Format poruke commita

Slijedite [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Primjeri:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Format naslova
```
[ModuleXX] Brief description of change
```
ili
```
[Module08/samples/XX] Description for sample changes
```

### Kodeks ponašanja

Svi suradnici moraju slijediti [Kodeks ponašanja za otvoreni kod Microsofta](https://opensource.microsoft.com/codeofconduct/). Molimo pregledajte [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) prije doprinosa.

### Prije slanja

**Za promjene sadržaja:**
- Pregledajte sve izmijenjene Markdown datoteke
- Provjerite da linkovi i slike rade
- Provjerite pravopisne i gramatičke pogreške

**Za promjene uzoraka koda (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Za promjene Python primjera:**
- Testirajte da se uzorak uspješno pokreće
- Provjerite da rukovanje greškama funkcionira
- Provjerite kompatibilnost s Foundry Local

### Proces pregleda

- Promjene edukacijskog sadržaja pregledavaju se radi točnosti i jasnoće
- Uzorci koda testiraju se na funkcionalnost
- Ažuriranja prijevoda automatski obrađuje GitHub Actions

## Sustav za prijevod

**VAŽNO:** Ovaj repozitorij koristi automatizirani prijevod putem GitHub Actions.

- Prijevodi se nalaze u direktoriju `/translations/` (50+ jezika)
- Automatizirano putem tijeka rada `co-op-translator.yml`
- **NE uređujte ručno datoteke prijevoda** - bit će prebrisane
- Uređujte samo izvorne datoteke na engleskom jeziku u korijenskim i modulskim direktorijima
- Prijevodi se automatski generiraju prilikom slanja na `main` granu

## Integracija s Foundry Local

Većina uzoraka iz Modula08 zahtijeva pokretanje Microsoft Foundry Local.

### Instalacija i postavljanje

**Instalirajte Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Instalirajte Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Pokretanje Foundry Local
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

### Korištenje SDK-a (Python)
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

### Provjera Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Varijable okruženja za uzorke

Većina uzoraka koristi ove varijable okruženja:
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

**Napomena**: Kada koristite `FoundryLocalManager`, SDK automatski upravlja otkrivanjem usluga i učitavanjem modela. Alias modela (poput `phi-3.5-mini`) osigurava odabir najbolje varijante za vaš hardver.

## Izrada i implementacija

### Implementacija sadržaja

Ovaj repozitorij primarno sadrži dokumentaciju - nije potreban proces izrade za sadržaj.

### Izrada uzoraka aplikacija

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

**Python primjeri:**
Nema procesa izrade - primjeri se izravno pokreću s Python interpreterom.

## Uobičajeni problemi i rješavanje problema

> **Savjet**: Provjerite [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) za poznate probleme i rješenja.

### Kritični problemi (blokirajući)

#### Foundry Local ne radi
**Problem:** Uzorci ne rade zbog grešaka u povezivanju

**Rješenje:**
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

### Uobičajeni problemi (umjereni)

#### Problemi s Python virtualnim okruženjem
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

#### Problemi s izradom Electron aplikacije
**Problem:** Greške pri npm install ili izradi

**Rješenje:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Problemi s tijekovima rada (manji)

#### Sukobi u tijeku rada za prijevod
**Problem:** Sukobi u PR-u za prijevod s vašim promjenama

**Rješenje:**
- Uređujte samo izvorne datoteke na engleskom jeziku
- Neka automatizirani tijek rada za prijevod obavi prijevode
- Ako dođe do sukoba, spojite `main` u svoju granu nakon što se prijevodi spoje

#### Problemi s preuzimanjem modela
**Problem:** Foundry Local ne uspijeva preuzeti modele

**Rješenje:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Dodatni resursi

### Obrazovni putovi
- **Put za početnike:** Moduli 01-02 (7-9 sati)
- **Put za srednje napredne:** Moduli 03-04 (9-11 sati)
- **Put za napredne:** Moduli 05-07 (12-15 sati)
- **Put za stručnjake:** Modul 08 (8-10 sati)

### Ključni sadržaj modula
- **Modul01:** Osnove EdgeAI-a i studije slučaja iz stvarnog svijeta
- **Modul02:** Obitelji i arhitekture malih jezičnih modela (SLM)
- **Modul03:** Strategije lokalne i cloud implementacije
- **Modul04:** Optimizacija modela s više okvira
- **Modul05:** SLMOps - operacije u produkciji
- **Modul06:** AI agenti i pozivanje funkcija
- **Modul07:** Implementacije specifične za platformu
- **Modul08:** Foundry Local alatni set s 10 sveobuhvatnih uzoraka

### Vanjske ovisnosti
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Lokalno okruženje za AI modele s OpenAI-kompatibilnim API-jem
  - [Dokumentacija](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Okvir za optimizaciju
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Alat za optimizaciju modela
- [OpenVINO](https://docs.openvino.ai/) - Intelov alat za optimizaciju

## Napomene specifične za projekt

### Uzorci aplikacija iz Modula08

Repozitorij uključuje 10 sveobuhvatnih uzoraka aplikacija:

1. **01-REST Chat Quickstart** - Osnovna integracija OpenAI SDK-a
2. **02-OpenAI SDK Integration** - Napredne značajke SDK-a
3. **03-Model Discovery & Benchmarking** - Alati za usporedbu modela
4. **04-Chainlit RAG Application** - Generacija uz pomoć pretraživanja
5. **05-Multi-Agent Orchestration** - Osnovna koordinacija agenata
6. **06-Models-as-Tools Router** - Inteligentno usmjeravanje modela
7. **07-Direct API Client** - Niskorazinska integracija API-ja
8. **08-Windows 11 Chat App** - Nativna Electron desktop aplikacija
9. **09-Advanced Multi-Agent System** - Kompleksna koordinacija agenata
10. **10-Foundry Tools Framework** - Integracija LangChain/Semantic Kernel

Svaki uzorak demonstrira različite aspekte razvoja Edge AI-a s Foundry Local.

### Razmatranja performansi

- SLM-ovi su optimizirani za implementaciju na rubu (2-16GB RAM)
- Lokalna inferencija omogućuje vrijeme odziva od 50-500 ms  
- Tehnike kvantizacije postižu smanjenje veličine za 75% uz zadržavanje 85% performansi  
- Mogućnosti za razgovore u stvarnom vremenu s lokalnim modelima  

### Sigurnost i privatnost  

- Sva obrada odvija se lokalno - podaci se ne šalju u oblak  
- Prikladno za aplikacije osjetljive na privatnost (zdravstvo, financije)  
- Zadovoljava zahtjeve za suverenitet podataka  
- Foundry Local radi isključivo na lokalnom hardveru  

## Dobivanje pomoći  

### Dokumentacija  

- **Glavni README**: [README.md](README.md) - Pregled repozitorija i putovi za učenje  
- **Vodič za učenje**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Resursi za učenje i vremenski okvir  
- **Podrška**: [SUPPORT.md](SUPPORT.md) - Kako dobiti pomoć  
- **Sigurnost**: [SECURITY.md](SECURITY.md) - Prijava sigurnosnih problema  

### Podrška zajednice  

- **GitHub Issues**: [Prijavite greške ili zatražite značajke](https://github.com/microsoft/edgeai-for-beginners/issues)  
- **GitHub Discussions**: [Postavite pitanja i podijelite ideje](https://github.com/microsoft/edgeai-for-beginners/discussions)  
- **Foundry Local Issues**: [Tehnički problemi s Foundry Local](https://github.com/microsoft/Foundry-Local/issues)  

### Kontakt  

- **Održavatelji**: Pogledajte [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)  
- **Sigurnosni problemi**: Slijedite odgovorno prijavljivanje u [SECURITY.md](SECURITY.md)  
- **Microsoft podrška**: Za podršku za poduzeća, kontaktirajte Microsoft korisničku službu  

### Dodatni resursi  

- **Microsoft Learn**: [Putovi za učenje o AI i strojnom učenju](https://learn.microsoft.com/training/browse/?products=ai-services)  
- **Foundry Local Dokumentacija**: [Službena dokumentacija](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)  
- **Primjeri zajednice**: Pogledajte [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) za doprinose zajednice  

---

**Ovo je edukacijski repozitorij usmjeren na podučavanje razvoja Edge AI-a. Primarni obrazac doprinosa uključuje poboljšanje edukacijskog sadržaja i dodavanje/poboljšanje uzoraka aplikacija koje demonstriraju Edge AI koncepte.**  

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.