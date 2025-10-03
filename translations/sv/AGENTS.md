<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:36:13+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sv"
}
-->
# AGENTS.md

## Projektöversikt

EdgeAI för nybörjare är ett omfattande utbildningsmaterial som lär ut Edge AI-utveckling med små språkmodeller (SLMs). Kursen täcker EdgeAI-grunder, modellimplementering, optimeringstekniker och produktionsklara lösningar med Microsoft Foundry Local och olika AI-ramverk.

**Nyckelteknologier:**
- Python 3.8+ (huvudspråk för AI/ML-exempel)
- .NET C# (AI/ML-exempel)
- JavaScript/Node.js med Electron (för skrivbordsapplikationer)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-ramverk: LangChain, Semantic Kernel, Chainlit
- Modelloptimering: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repositorytyp:** Utbildningsinnehåll med 8 moduler och 10 omfattande exempelapplikationer

**Arkitektur:** Flermoduls lärväg med praktiska exempel som demonstrerar Edge AI-implementeringsmönster

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

## Installationskommandon

### Repositoryinstallation

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python-exempelinstallation (Modul08 och Python-exempel)

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

### Node.js-exempelinstallation (Exempel 08 - Windows Chat App)

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

### Foundry Local-installation

Foundry Local krävs för att köra Modul08-exemplen:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Utvecklingsarbetsflöde

### Innehållsutveckling

Detta repository innehåller främst **Markdown-utbildningsinnehåll**. Vid ändringar:

1. Redigera `.md`-filer i motsvarande modulkataloger
2. Följ befintliga formateringsmönster
3. Säkerställ att kodexempel är korrekta och testade
4. Uppdatera motsvarande översatt innehåll om nödvändigt (eller låt automatisering hantera det)

### Utveckling av exempelapplikationer

För Python-exempel (exempel 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

För Electron-exempel (exempel 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testning av exempelapplikationer

Python-exempel har inga automatiserade tester men kan valideras genom att köra dem:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron-exempel har testinfrastruktur:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testinstruktioner

### Validering av innehåll

Repository använder automatiserade översättningsarbetsflöden. Ingen manuell testning krävs för översättningar.

**Manuell validering för innehållsändringar:**
1. Granska Markdown-rendering genom att förhandsgranska `.md`-filer
2. Kontrollera att alla länkar pekar på giltiga mål
3. Testa eventuella kodsnuttar som ingår i dokumentationen
4. Kontrollera att bilder laddas korrekt

### Testning av exempelapplikationer

**Modul08/exempel/08 (Electron-app) har omfattande tester:**
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

**Python-exempel bör testas manuellt:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Kodstilsguider

### Markdown-innehåll

- Använd konsekvent rubrikhierarki (# för titel, ## för huvudsektioner, ### för undersektioner)
- Inkludera kodblock med språkspecifikationer: ```python, ```bash, ```javascript
- Följ befintlig formatering för tabeller, listor och betoning
- Håll rader läsbara (sikta på ~80-100 tecken, men inte strikt)
- Använd relativa länkar för interna referenser

### Python-kodstil

- Följ PEP 8-konventioner
- Använd typanvisningar där det är lämpligt
- Inkludera docstrings för funktioner och klasser
- Använd meningsfulla variabelnamn
- Håll funktioner fokuserade och koncisa

### JavaScript/Node.js-kodstil

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Viktiga konventioner:**
- ESLint-konfiguration tillhandahålls i exempel 08
- Prettier för kodformatering
- Använd modern ES6+ syntax
- Följ befintliga mönster i kodbasen

## Riktlinjer för pull requests

### Titelformat
```
[ModuleXX] Brief description of change
```
eller
```
[Module08/samples/XX] Description for sample changes
```

### Innan inlämning

**För innehållsändringar:**
- Förhandsgranska alla ändrade Markdown-filer
- Kontrollera att länkar och bilder fungerar
- Kontrollera stavfel och grammatiska fel

**För kodändringar i exempel (Modul08/exempel/08):**
```bash
npm run lint
npm test
```

**För Python-exempeländringar:**
- Testa att exemplet körs framgångsrikt
- Kontrollera att felhantering fungerar
- Kontrollera kompatibilitet med Foundry Local

### Granskningsprocess

- Ändringar i utbildningsinnehåll granskas för noggrannhet och tydlighet
- Kodexempel testas för funktionalitet
- Översättningsuppdateringar hanteras automatiskt av GitHub Actions

## Översättningssystem

**VIKTIGT:** Detta repository använder automatiserad översättning via GitHub Actions.

- Översättningar finns i katalogen `/translations/` (50+ språk)
- Automatiserat via arbetsflödet `co-op-translator.yml`
- **REDIGERA INTE översättningsfiler manuellt** - de kommer att skrivas över
- Redigera endast engelska källfiler i root- och modulkataloger
- Översättningar genereras automatiskt vid push till `main`-grenen

## Foundry Local-integration

De flesta Modul08-exempel kräver att Microsoft Foundry Local körs:

### Starta Foundry Local
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

### Verifiera Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Miljövariabler för exempel

De flesta exempel använder dessa miljövariabler:
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

## Bygg och implementering

### Implementering av innehåll

Detta repository är främst dokumentation - ingen byggprocess krävs för innehåll.

### Byggprocess för exempelapplikationer

**Electron-applikation (Modul08/exempel/08):**
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

**Python-exempel:**
Ingen byggprocess - exempel körs direkt med Python-tolk.

## Vanliga problem och felsökning

### Foundry Local körs inte
**Problem:** Exempel misslyckas med anslutningsfel

**Lösning:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Problem med Python-virtuella miljöer
**Problem:** Modulimportfel

**Lösning:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Problem med Electron-bygge
**Problem:** npm install eller byggfel

**Lösning:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Konflikter i översättningsarbetsflöde
**Problem:** Översättnings-PR konflikter med dina ändringar

**Lösning:**
- Redigera endast engelska källfiler
- Låt det automatiserade översättningsarbetsflödet hantera översättningar
- Om konflikter uppstår, slå samman `main` till din gren efter att översättningar har slagits samman

## Ytterligare resurser

### Lärvägar
- **Nybörjarväg:** Moduler 01-02 (7-9 timmar)
- **Mellannivåväg:** Moduler 03-04 (9-11 timmar)
- **Avancerad väg:** Moduler 05-07 (12-15 timmar)
- **Expertväg:** Modul 08 (8-10 timmar)

### Viktigt modulinnehåll
- **Modul01:** EdgeAI-grunder och verkliga fallstudier
- **Modul02:** Familjer och arkitekturer för små språkmodeller (SLM)
- **Modul03:** Strategier för lokal och molnbaserad implementering
- **Modul04:** Modelloptimering med flera ramverk
- **Modul05:** SLMOps - produktionsdrift
- **Modul06:** AI-agenter och funktionsanrop
- **Modul07:** Plattformsspecifika implementeringar
- **Modul08:** Foundry Local-verktyg med 10 omfattande exempel

### Externa beroenden
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Lokal AI-modellruntime
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimeringsramverk
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Verktyg för modelloptimering
- [OpenVINO](https://docs.openvino.ai/) - Intels optimeringsverktyg

## Projektspecifika anteckningar

### Modul08-exempelapplikationer

Repository innehåller 10 omfattande exempelapplikationer:

1. **01-REST Chat Quickstart** - Grundläggande OpenAI SDK-integration
2. **02-OpenAI SDK Integration** - Avancerade SDK-funktioner
3. **03-Model Discovery & Benchmarking** - Verktyg för modelljämförelse
4. **04-Chainlit RAG Application** - Generering med förbättrad hämtning
5. **05-Multi-Agent Orchestration** - Grundläggande agentkoordinering
6. **06-Models-as-Tools Router** - Intelligent modellroutning
7. **07-Direct API Client** - Låg nivå API-integration
8. **08-Windows 11 Chat App** - Native Electron-skrivbordsapplikation
9. **09-Advanced Multi-Agent System** - Komplex agentkoordinering
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel-integration

Varje exempel demonstrerar olika aspekter av Edge AI-utveckling med Foundry Local.

### Prestandaöverväganden

- SLMs är optimerade för Edge-implementering (2-16GB RAM)
- Lokal inferens ger svarstider på 50-500ms
- Kvantiseringstekniker uppnår 75% storleksreduktion med 85% prestandabehållning
- Realtidskonversationsmöjligheter med lokala modeller

### Säkerhet och integritet

- All bearbetning sker lokalt - ingen data skickas till molnet
- Lämplig för integritetskänsliga applikationer (sjukvård, finans)
- Uppfyller krav på datasuveränitet
- Foundry Local körs helt på lokal hårdvara

---

**Detta är ett utbildningsrepository som fokuserar på att lära ut Edge AI-utveckling. Det primära bidragsmönstret är att förbättra utbildningsinnehåll och lägga till/förbättra exempelapplikationer som demonstrerar Edge AI-koncept.**

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.