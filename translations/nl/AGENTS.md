<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:38:16+00:00",
  "source_file": "AGENTS.md",
  "language_code": "nl"
}
-->
# AGENTS.md

## Projectoverzicht

EdgeAI for Beginners is een uitgebreide educatieve repository die Edge AI-ontwikkeling met Small Language Models (SLMs) leert. De cursus behandelt de basisprincipes van EdgeAI, modelimplementatie, optimalisatietechnieken en productieklare implementaties met Microsoft Foundry Local en verschillende AI-frameworks.

**Belangrijke technologieën:**
- Python 3.8+ (primaire taal voor AI/ML-voorbeelden)
- .NET C# (AI/ML-voorbeelden)
- JavaScript/Node.js met Electron (voor desktopapplicaties)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-frameworks: LangChain, Semantic Kernel, Chainlit
- Modeloptimalisatie: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Type repository:** Educatieve contentrepository met 8 modules en 10 uitgebreide voorbeeldapplicaties

**Architectuur:** Leerpad met meerdere modules en praktische voorbeelden die Edge AI-implementatiepatronen demonstreren

## Repositorystructuur

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

## Setupcommando's

### Repositorysetup

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Pythonvoorbeeldsetup (Module08 en Pythonvoorbeelden)

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

### Node.js voorbeeldsetup (Voorbeeld 08 - Windows Chat App)

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

### Foundry Local setup

Foundry Local is vereist om de voorbeelden van Module08 uit te voeren:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Ontwikkelworkflow

### Contentontwikkeling

Deze repository bevat voornamelijk **Markdown educatieve content**. Bij het aanbrengen van wijzigingen:

1. Bewerk `.md`-bestanden in de juiste modulemappen
2. Volg bestaande opmaakpatronen
3. Zorg ervoor dat codevoorbeelden nauwkeurig en getest zijn
4. Werk de bijbehorende vertaalde content bij indien nodig (of laat automatisering dit afhandelen)

### Voorbeeldapplicatieontwikkeling

Voor Pythonvoorbeelden (voorbeelden 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Voor Electronvoorbeeld (voorbeeld 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testen van voorbeeldapplicaties

Pythonvoorbeelden hebben geen geautomatiseerde tests, maar kunnen worden gevalideerd door ze uit te voeren:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electronvoorbeeld heeft testinfrastructuur:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testinstructies

### Contentvalidatie

De repository gebruikt geautomatiseerde vertaalworkflows. Handmatig testen is niet vereist voor vertalingen.

**Handmatige validatie voor contentwijzigingen:**
1. Bekijk de Markdown-rendering door `.md`-bestanden te bekijken
2. Controleer of alle links naar geldige doelen verwijzen
3. Test eventuele codefragmenten die in de documentatie zijn opgenomen
4. Controleer of afbeeldingen correct worden geladen

### Testen van voorbeeldapplicaties

**Module08/samples/08 (Electron-app) heeft uitgebreide tests:**
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

**Pythonvoorbeelden moeten handmatig worden getest:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Code stijlgids

### Markdowncontent

- Gebruik een consistente koppenhiërarchie (# voor titel, ## voor hoofdsecties, ### voor subsecties)
- Voeg codeblokken toe met taalspecificaties: ```python, ```bash, ```javascript
- Volg bestaande opmaak voor tabellen, lijsten en nadruk
- Houd regels leesbaar (streef naar ~80-100 tekens, maar niet strikt)
- Gebruik relatieve links voor interne verwijzingen

### Pythoncode stijl

- Volg PEP 8-conventies
- Gebruik type hints waar nodig
- Voeg docstrings toe voor functies en klassen
- Gebruik betekenisvolle variabelnamen
- Houd functies gefocust en beknopt

### JavaScript/Node.js code stijl

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Belangrijke conventies:**
- ESLint-configuratie geleverd in voorbeeld 08
- Prettier voor codeopmaak
- Gebruik moderne ES6+ syntaxis
- Volg bestaande patronen in de codebase

## Richtlijnen voor pull requests

### Titelindeling
```
[ModuleXX] Brief description of change
```
of
```
[Module08/samples/XX] Description for sample changes
```

### Voor het indienen

**Voor contentwijzigingen:**
- Bekijk alle gewijzigde Markdown-bestanden
- Controleer of links en afbeeldingen werken
- Controleer op typfouten en grammaticale fouten

**Voor wijzigingen in voorbeeldcode (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Voor wijzigingen in Pythonvoorbeelden:**
- Test of het voorbeeld succesvol wordt uitgevoerd
- Controleer of foutafhandeling werkt
- Controleer compatibiliteit met Foundry Local

### Reviewproces

- Educatieve contentwijzigingen worden beoordeeld op nauwkeurigheid en duidelijkheid
- Codevoorbeelden worden getest op functionaliteit
- Vertaalupdates worden automatisch afgehandeld door GitHub Actions

## Vertaalingssysteem

**BELANGRIJK:** Deze repository gebruikt geautomatiseerde vertaling via GitHub Actions.

- Vertalingen staan in de map `/translations/` (50+ talen)
- Geautomatiseerd via de workflow `co-op-translator.yml`
- **BEWERK vertaalbestanden NIET handmatig** - ze worden overschreven
- Bewerk alleen Engelse bronbestanden in de root- en modulemappen
- Vertalingen worden automatisch gegenereerd bij een push naar de `main`-branch

## Foundry Local-integratie

De meeste voorbeelden van Module08 vereisen dat Microsoft Foundry Local actief is:

### Foundry Local starten
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

### Foundry Local verifiëren
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Omgevingsvariabelen voor voorbeelden

De meeste voorbeelden gebruiken deze omgevingsvariabelen:
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

## Build en implementatie

### Contentimplementatie

Deze repository is voornamelijk documentatie - geen buildproces vereist voor content.

### Voorbeeldapplicatie bouwen

**Electronapplicatie (Module08/samples/08):**
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

**Pythonvoorbeelden:**
Geen buildproces - voorbeelden worden direct uitgevoerd met de Python-interpreter.

## Veelvoorkomende problemen en oplossingen

### Foundry Local niet actief
**Probleem:** Voorbeelden falen met verbindingsfouten

**Oplossing:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Problemen met Python virtuele omgeving
**Probleem:** Module importfouten

**Oplossing:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron buildproblemen
**Probleem:** npm install of buildfouten

**Oplossing:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Vertaalworkflowconflicten
**Probleem:** Vertaal-PR conflicteert met uw wijzigingen

**Oplossing:**
- Bewerk alleen Engelse bronbestanden
- Laat de geautomatiseerde vertaalworkflow vertalingen afhandelen
- Als er conflicten optreden, merge `main` in uw branch nadat vertalingen zijn gemerged

## Aanvullende bronnen

### Leertrajecten
- **Beginnertraject:** Modules 01-02 (7-9 uur)
- **Intermediate traject:** Modules 03-04 (9-11 uur)
- **Advanced traject:** Modules 05-07 (12-15 uur)
- **Expert traject:** Module 08 (8-10 uur)

### Belangrijke modulecontent
- **Module01:** Basisprincipes van EdgeAI en praktijkvoorbeelden
- **Module02:** Small Language Model (SLM) families en architecturen
- **Module03:** Lokale en cloudimplementatiestrategieën
- **Module04:** Modeloptimalisatie met meerdere frameworks
- **Module05:** SLMOps - productieoperaties
- **Module06:** AI-agenten en functieaanroepen
- **Module07:** Platformspecifieke implementaties
- **Module08:** Foundry Local toolkit met 10 uitgebreide voorbeelden

### Externe afhankelijkheden
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Lokale AI-modelruntime
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimalisatieframework
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Modeloptimalisatietoolkit
- [OpenVINO](https://docs.openvino.ai/) - Intel's optimalisatietoolkit

## Projectspecifieke opmerkingen

### Module08 voorbeeldapplicaties

De repository bevat 10 uitgebreide voorbeeldapplicaties:

1. **01-REST Chat Quickstart** - Basisintegratie van OpenAI SDK
2. **02-OpenAI SDK Integratie** - Geavanceerde SDK-functies
3. **03-Modelontdekking & benchmarking** - Hulpmiddelen voor modelvergelijking
4. **04-Chainlit RAG Applicatie** - Retrieval-augmented generation
5. **05-Multi-Agent Orchestratie** - Basiscoördinatie van agenten
6. **06-Models-as-Tools Router** - Intelligente modelroutering
7. **07-Directe API Client** - Laag-niveau API-integratie
8. **08-Windows 11 Chat App** - Native Electron desktopapplicatie
9. **09-Geavanceerd Multi-Agent Systeem** - Complexe agentenorchestratie
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel integratie

Elk voorbeeld demonstreert verschillende aspecten van Edge AI-ontwikkeling met Foundry Local.

### Prestatieoverwegingen

- SLMs zijn geoptimaliseerd voor edge-implementatie (2-16GB RAM)
- Lokale inferentie biedt responstijden van 50-500ms
- Kwantiseringstechnieken bereiken 75% groottevermindering met 85% prestatiebehoud
- Real-time gespreksmogelijkheden met lokale modellen

### Veiligheid en privacy

- Alle verwerking gebeurt lokaal - geen gegevens worden naar de cloud verzonden
- Geschikt voor privacygevoelige toepassingen (gezondheidszorg, financiën)
- Voldoet aan eisen voor gegevenssoevereiniteit
- Foundry Local draait volledig op lokale hardware

---

**Dit is een educatieve repository gericht op het leren van Edge AI-ontwikkeling. Het primaire bijdragepatroon is het verbeteren van educatieve content en het toevoegen/verbeteren van voorbeeldapplicaties die Edge AI-concepten demonstreren.**

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.