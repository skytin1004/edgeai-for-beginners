<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:36:42+00:00",
  "source_file": "AGENTS.md",
  "language_code": "da"
}
-->
# AGENTS.md

## Projektoversigt

EdgeAI for Beginners er et omfattende uddannelsesmateriale, der lærer udvikling af Edge AI med små sproglige modeller (SLMs). Kurset dækker EdgeAI-grundprincipper, modelimplementering, optimeringsteknikker og produktionsklare løsninger ved brug af Microsoft Foundry Local og forskellige AI-rammer.

**Nøgleteknologier:**
- Python 3.8+ (primært sprog til AI/ML-eksempler)
- .NET C# (AI/ML-eksempler)
- JavaScript/Node.js med Electron (til desktop-applikationer)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-rammer: LangChain, Semantic Kernel, Chainlit
- Modeloptimering: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repositorytype:** Uddannelsesindhold med 8 moduler og 10 omfattende prøveapplikationer

**Arkitektur:** Multimodul læringssti med praktiske eksempler, der demonstrerer Edge AI-implementeringsmønstre

## Repositorystruktur

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

## Opsætningskommandoer

### Repositoryopsætning

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Opsætning af Python-eksempler (Modul08 og Python-eksempler)

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

### Opsætning af Node.js-eksempler (Eksempel 08 - Windows Chat App)

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

### Foundry Local Opsætning

Foundry Local er påkrævet for at køre eksemplerne i Modul08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Udviklingsworkflow

### Udvikling af indhold

Dette repository indeholder primært **Markdown-uddannelsesindhold**. Når du foretager ændringer:

1. Rediger `.md`-filer i de relevante modulmapper
2. Følg eksisterende formateringsmønstre
3. Sørg for, at kodeeksempler er nøjagtige og testede
4. Opdater tilsvarende oversat indhold, hvis nødvendigt (eller lad automatisering håndtere det)

### Udvikling af prøveapplikationer

For Python-eksempler (eksempler 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

For Electron-eksempel (eksempel 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Test af prøveapplikationer

Python-eksempler har ikke automatiserede tests, men kan valideres ved at køre dem:
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

## Testinstruktioner

### Validering af indhold

Repositoryet bruger automatiserede oversættelsesworkflows. Ingen manuel test er påkrævet for oversættelser.

**Manuel validering af indholdsændringer:**
1. Gennemse Markdown-rendering ved at forhåndsvise `.md`-filer
2. Bekræft, at alle links peger på gyldige mål
3. Test eventuelle kodeeksempler, der er inkluderet i dokumentationen
4. Kontroller, at billeder indlæses korrekt

### Test af prøveapplikationer

**Modul08/samples/08 (Electron-app) har omfattende tests:**
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

**Python-eksempler skal testes manuelt:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Kodestilretningslinjer

### Markdown-indhold

- Brug konsekvent overskriftshierarki (# til titel, ## til hovedsektioner, ### til undersektioner)
- Inkluder kodeblokke med sprogspecifikatorer: ```python, ```bash, ```javascript
- Følg eksisterende formatering for tabeller, lister og fremhævning
- Hold linjer læsbare (sigte mod ~80-100 tegn, men ikke strengt)
- Brug relative links til interne referencer

### Python-kodestil

- Følg PEP 8-konventioner
- Brug type hints, hvor det er relevant
- Inkluder docstrings for funktioner og klasser
- Brug meningsfulde variabelnavne
- Hold funktioner fokuserede og korte

### JavaScript/Node.js-kodestil

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Vigtige konventioner:**
- ESLint-konfiguration leveret i eksempel 08
- Prettier til kodeformatering
- Brug moderne ES6+ syntaks
- Følg eksisterende mønstre i kodebasen

## Retningslinjer for pull requests

### Titelformat
```
[ModuleXX] Brief description of change
```
eller
```
[Module08/samples/XX] Description for sample changes
```

### Før indsendelse

**For indholdsændringer:**
- Forhåndsvis alle ændrede Markdown-filer
- Bekræft, at links og billeder fungerer
- Kontroller for stavefejl og grammatiske fejl

**For ændringer i prøvekode (Modul08/samples/08):**
```bash
npm run lint
npm test
```

**For ændringer i Python-eksempler:**
- Test, at eksemplet kører korrekt
- Bekræft, at fejlhåndtering fungerer
- Kontroller kompatibilitet med Foundry Local

### Gennemgangsproces

- Ændringer i uddannelsesindhold gennemgås for nøjagtighed og klarhed
- Kodeeksempler testes for funktionalitet
- Oversættelsesopdateringer håndteres automatisk af GitHub Actions

## Oversættelsessystem

**VIGTIGT:** Dette repository bruger automatiseret oversættelse via GitHub Actions.

- Oversættelser findes i `/translations/`-mappen (50+ sprog)
- Automatiseret via `co-op-translator.yml` workflow
- **REDIGER IKKE oversættelsesfiler manuelt** - de vil blive overskrevet
- Rediger kun engelske kildefiler i rod- og modulmapper
- Oversættelser genereres automatisk ved push til `main`-branch

## Foundry Local Integration

De fleste eksempler i Modul08 kræver, at Microsoft Foundry Local kører:

### Start Foundry Local
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

### Verificer Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Miljøvariabler for eksempler

De fleste eksempler bruger disse miljøvariabler:
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

## Bygning og implementering

### Indholdsimplementering

Dette repository er primært dokumentation - ingen byggeproces krævet for indhold.

### Bygning af prøveapplikationer

**Electron-applikation (Modul08/samples/08):**
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
Ingen byggeproces - eksempler køres direkte med Python-fortolkeren.

## Almindelige problemer og fejlfinding

### Foundry Local kører ikke
**Problem:** Eksempler fejler med forbindelsesfejl

**Løsning:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Problemer med Python-virtuelt miljø
**Problem:** Fejl ved import af moduler

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

### Problemer med Electron-bygning
**Problem:** npm install eller byggefejl

**Løsning:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Konflikter i oversættelsesworkflow
**Problem:** Oversættelses-PR konflikter med dine ændringer

**Løsning:**
- Rediger kun engelske kildefiler
- Lad det automatiserede oversættelsesworkflow håndtere oversættelser
- Hvis konflikter opstår, flet `main` ind i din branch efter oversættelser er flettet

## Yderligere ressourcer

### Læringsstier
- **Begyndersti:** Moduler 01-02 (7-9 timer)
- **Mellemsti:** Moduler 03-04 (9-11 timer)
- **Avanceret sti:** Moduler 05-07 (12-15 timer)
- **Ekspertsti:** Modul 08 (8-10 timer)

### Nøgleindhold i moduler
- **Modul01:** EdgeAI-grundprincipper og virkelige eksempler
- **Modul02:** Små sproglige modeller (SLM) og arkitekturer
- **Modul03:** Lokale og cloud-implementeringsstrategier
- **Modul04:** Modeloptimering med flere rammer
- **Modul05:** SLMOps - produktionsdrift
- **Modul06:** AI-agenter og funktionskald
- **Modul07:** Platformsspecifikke implementeringer
- **Modul08:** Foundry Local toolkit med 10 omfattende eksempler

### Eksterne afhængigheder
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Lokal AI-model runtime
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimeringsramme
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Modeloptimeringsværktøj
- [OpenVINO](https://docs.openvino.ai/) - Intels optimeringsværktøj

## Projektspecifikke noter

### Modul08 prøveapplikationer

Repositoryet inkluderer 10 omfattende prøveapplikationer:

1. **01-REST Chat Quickstart** - Grundlæggende OpenAI SDK-integration
2. **02-OpenAI SDK Integration** - Avancerede SDK-funktioner
3. **03-Model Discovery & Benchmarking** - Værktøjer til model sammenligning
4. **04-Chainlit RAG Application** - Retrieval-augmented generation
5. **05-Multi-Agent Orchestration** - Grundlæggende agentkoordinering
6. **06-Models-as-Tools Router** - Intelligent modelrouting
7. **07-Direct API Client** - Lav-niveau API-integration
8. **08-Windows 11 Chat App** - Native Electron desktop-applikation
9. **09-Advanced Multi-Agent System** - Kompleks agentkoordinering
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel integration

Hvert eksempel demonstrerer forskellige aspekter af Edge AI-udvikling med Foundry Local.

### Ydelseshensyn

- SLM'er er optimeret til Edge-implementering (2-16GB RAM)
- Lokal inferens giver 50-500ms svartider
- Kvantiseringsteknikker opnår 75% størrelsesreduktion med 85% ydelsesbevarelse
- Realtidskonversationsmuligheder med lokale modeller

### Sikkerhed og privatliv

- Al behandling sker lokalt - ingen data sendes til cloud
- Velegnet til applikationer med følsomme data (sundhedsvæsen, finans)
- Opfylder krav til datasuverænitet
- Foundry Local kører udelukkende på lokal hardware

---

**Dette er et uddannelsesrepository fokuseret på at lære udvikling af Edge AI. Det primære bidragsmønster er forbedring af uddannelsesindhold og tilføjelse/forbedring af prøveapplikationer, der demonstrerer Edge AI-koncepter.**

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.