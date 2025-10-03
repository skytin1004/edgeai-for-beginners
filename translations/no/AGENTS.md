<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:37:11+00:00",
  "source_file": "AGENTS.md",
  "language_code": "no"
}
-->
# AGENTS.md

## Prosjektoversikt

EdgeAI for Beginners er et omfattende opplæringsmateriale som lærer bort utvikling av Edge AI med små språkmodeller (SLMs). Kurset dekker grunnleggende EdgeAI, modellutplassering, optimaliseringsteknikker og produksjonsklare implementeringer ved bruk av Microsoft Foundry Local og ulike AI-rammeverk.

**Nøkkelteknologier:**
- Python 3.8+ (primærspråk for AI/ML-eksempler)
- .NET C# (AI/ML-eksempler)
- JavaScript/Node.js med Electron (for skrivebordsapplikasjoner)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-rammeverk: LangChain, Semantic Kernel, Chainlit
- Modelloptimalisering: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repository-type:** Opplæringsinnhold med 8 moduler og 10 omfattende eksempelapplikasjoner

**Arkitektur:** Læringssti med flere moduler og praktiske eksempler som demonstrerer mønstre for Edge AI-utplassering

## Repository-struktur

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

## Oppsettskommandoer

### Repository-oppsett

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Oppsett for Python-eksempler (Modul08 og Python-eksempler)

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

### Oppsett for Node.js-eksempler (Eksempel 08 - Windows Chat App)

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

### Foundry Local-oppsett

Foundry Local er nødvendig for å kjøre eksemplene i Modul08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Utviklingsarbeidsflyt

### Utvikling av innhold

Dette repositoryet inneholder primært **Markdown-opplæringsinnhold**. Når du gjør endringer:

1. Rediger `.md`-filer i de relevante modulmappene
2. Følg eksisterende formateringsmønstre
3. Sørg for at kodeeksempler er nøyaktige og testet
4. Oppdater tilsvarende oversatt innhold hvis nødvendig (eller la automatisering håndtere det)

### Utvikling av eksempelapplikasjoner

For Python-eksempler (eksempler 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

For Electron-eksemplet (eksempel 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testing av eksempelapplikasjoner

Python-eksempler har ikke automatiserte tester, men kan valideres ved å kjøre dem:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron-eksemplet har testinfrastruktur:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testinstruksjoner

### Validering av innhold

Repositoryet bruker automatiserte oversettelsesarbeidsflyter. Ingen manuell testing kreves for oversettelser.

**Manuell validering for innholdsendringer:**
1. Forhåndsvis Markdown-filer for å sjekke gjengivelse
2. Verifiser at alle lenker peker til gyldige mål
3. Test eventuelle kodeeksempler som er inkludert i dokumentasjonen
4. Sjekk at bilder lastes korrekt

### Testing av eksempelapplikasjoner

**Modul08/eksempler/08 (Electron-app) har omfattende testing:**
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

**Python-eksempler bør testes manuelt:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Retningslinjer for kodestil

### Markdown-innhold

- Bruk konsistent overskrifthierarki (# for tittel, ## for hovedseksjoner, ### for underseksjoner)
- Inkluder kodeblokker med språkspesifikasjoner: ```python, ```bash, ```javascript
- Følg eksisterende formatering for tabeller, lister og utheving
- Hold linjene lesbare (mål for ~80-100 tegn, men ikke strengt)
- Bruk relative lenker for interne referanser

### Python-kodestil

- Følg PEP 8-konvensjoner
- Bruk typehint der det er hensiktsmessig
- Inkluder docstrings for funksjoner og klasser
- Bruk meningsfulle variabelnavn
- Hold funksjoner fokuserte og konsise

### JavaScript/Node.js-kodestil

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Viktige konvensjoner:**
- ESLint-konfigurasjon inkludert i eksempel 08
- Prettier for kodeformatering
- Bruk moderne ES6+ syntaks
- Følg eksisterende mønstre i kodebasen

## Retningslinjer for pull requests

### Tittelformat
```
[ModuleXX] Brief description of change
```
eller
```
[Module08/samples/XX] Description for sample changes
```

### Før innsending

**For innholdsendringer:**
- Forhåndsvis alle endrede Markdown-filer
- Verifiser at lenker og bilder fungerer
- Sjekk for skrivefeil og grammatiske feil

**For endringer i eksempelkode (Modul08/eksempler/08):**
```bash
npm run lint
npm test
```

**For endringer i Python-eksempler:**
- Test at eksemplet kjører som forventet
- Verifiser at feilhåndtering fungerer
- Sjekk kompatibilitet med Foundry Local

### Gjennomgangsprosess

- Endringer i opplæringsinnhold vurderes for nøyaktighet og klarhet
- Eksempelkode testes for funksjonalitet
- Oppdateringer av oversettelser håndteres automatisk av GitHub Actions

## Oversettelsessystem

**VIKTIG:** Dette repositoryet bruker automatisert oversettelse via GitHub Actions.

- Oversettelser finnes i `/translations/`-mappen (50+ språk)
- Automatisert via `co-op-translator.yml`-arbeidsflyt
- **IKKE rediger oversettelsesfiler manuelt** - de vil bli overskrevet
- Rediger kun engelske kildefiler i rot- og modulmapper
- Oversettelser genereres automatisk ved push til `main`-grenen

## Foundry Local-integrasjon

De fleste eksemplene i Modul08 krever at Microsoft Foundry Local kjører:

### Starte Foundry Local
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

### Verifisere Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Miljøvariabler for eksempler

De fleste eksempler bruker disse miljøvariablene:
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

## Bygging og utplassering

### Utplassering av innhold

Dette repositoryet er primært dokumentasjon - ingen byggeprosess kreves for innhold.

### Bygging av eksempelapplikasjoner

**Electron-applikasjon (Modul08/eksempler/08):**
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

**Python-eksempler:**
Ingen byggeprosess - eksempler kjøres direkte med Python-tolk.

## Vanlige problemer og feilsøking

### Foundry Local ikke kjører
**Problem:** Eksempler feiler med tilkoblingsfeil

**Løsning:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Problemer med Python-virtuelt miljø
**Problem:** Feil ved import av moduler

**Løsning:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Problemer med Electron-bygging
**Problem:** npm install eller byggefeil

**Løsning:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Konflikter i oversettelsesarbeidsflyt
**Problem:** Oversettelses-PR konflikter med dine endringer

**Løsning:**
- Rediger kun engelske kildefiler
- La den automatiserte oversettelsesarbeidsflyten håndtere oversettelser
- Hvis konflikter oppstår, slå sammen `main` inn i din gren etter at oversettelser er slått sammen

## Tilleggsressurser

### Læringsstier
- **Nybegynnersti:** Moduler 01-02 (7-9 timer)
- **Mellomnivåsti:** Moduler 03-04 (9-11 timer)
- **Avansert sti:** Moduler 05-07 (12-15 timer)
- **Ekspertsti:** Modul 08 (8-10 timer)

### Viktig modulinnhold
- **Modul01:** Grunnleggende EdgeAI og virkelige casestudier
- **Modul02:** Familier og arkitekturer for små språkmodeller (SLM)
- **Modul03:** Strategier for lokal og skybasert utplassering
- **Modul04:** Modelloptimalisering med flere rammeverk
- **Modul05:** SLMOps - produksjonsoperasjoner
- **Modul06:** AI-agenter og funksjonskall
- **Modul07:** Plattformspesifikke implementeringer
- **Modul08:** Foundry Local-verktøysett med 10 omfattende eksempler

### Eksterne avhengigheter
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Lokal AI-modellkjøring
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimaliseringsrammeverk
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Verktøy for modelloptimalisering
- [OpenVINO](https://docs.openvino.ai/) - Intels optimaliseringsverktøy

## Prosjektspesifikke notater

### Modul08-eksempelapplikasjoner

Repositoryet inkluderer 10 omfattende eksempelapplikasjoner:

1. **01-REST Chat Quickstart** - Grunnleggende OpenAI SDK-integrasjon
2. **02-OpenAI SDK Integration** - Avanserte SDK-funksjoner
3. **03-Model Discovery & Benchmarking** - Verktøy for modell sammenligning
4. **04-Chainlit RAG Application** - Generering med informasjonsinnhenting
5. **05-Multi-Agent Orchestration** - Grunnleggende agentkoordinering
6. **06-Models-as-Tools Router** - Intelligent modellruting
7. **07-Direct API Client** - Lavnivå API-integrasjon
8. **08-Windows 11 Chat App** - Native Electron skrivebordsapplikasjon
9. **09-Advanced Multi-Agent System** - Kompleks agentkoordinering
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel-integrasjon

Hvert eksempel demonstrerer ulike aspekter av Edge AI-utvikling med Foundry Local.

### Ytelseshensyn

- SLM-er er optimalisert for Edge-utplassering (2-16GB RAM)
- Lokal inferens gir responstider på 50-500ms
- Kvantiseringsteknikker oppnår 75% størrelsesreduksjon med 85% ytelsesbevaring
- Sanntids samtalefunksjoner med lokale modeller

### Sikkerhet og personvern

- All behandling skjer lokalt - ingen data sendes til skyen
- Egnet for applikasjoner med høye krav til personvern (helse, finans)
- Oppfyller krav til datasuverenitet
- Foundry Local kjører helt på lokal maskinvare

---

**Dette er et opplæringsrepository som fokuserer på å lære bort Edge AI-utvikling. Hovedbidragsmønsteret er å forbedre opplæringsinnhold og legge til/forbedre eksempelapplikasjoner som demonstrerer Edge AI-konsepter.**

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.