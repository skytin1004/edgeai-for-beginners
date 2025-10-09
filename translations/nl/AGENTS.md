<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "135b2658979f1e494bb0ecc6e26d4752",
  "translation_date": "2025-10-09T16:22:47+00:00",
  "source_file": "AGENTS.md",
  "language_code": "nl"
}
-->
# AGENTS.md

> **Ontwikkelaarsgids voor bijdragen aan EdgeAI voor beginners**
> 
> Dit document biedt uitgebreide informatie voor ontwikkelaars, AI-agenten en bijdragers die met deze repository werken. Het behandelt installatie, ontwikkelworkflows, testen en best practices.
> 
> **Laatst bijgewerkt**: oktober 2025 | **Documentversie**: 2.0

## Inhoudsopgave

- [Projectoverzicht](../..)
- [Repositorystructuur](../..)
- [Vereisten](../..)
- [Installatiecommando's](../..)
- [Ontwikkelworkflow](../..)
- [Testinstructies](../..)
- [Code-stijlrichtlijnen](../..)
- [Richtlijnen voor pull requests](../..)
- [Vertalingssysteem](../..)
- [Foundry Local-integratie](../..)
- [Build en implementatie](../..)
- [Veelvoorkomende problemen en oplossingen](../..)
- [Aanvullende bronnen](../..)
- [Projectspecifieke opmerkingen](../..)
- [Hulp krijgen](../..)

## Projectoverzicht

EdgeAI voor beginners is een uitgebreide educatieve repository die Edge AI-ontwikkeling met Small Language Models (SLM's) leert. De cursus behandelt EdgeAI-grondbeginselen, modelimplementatie, optimalisatietechnieken en productieklare implementaties met Microsoft Foundry Local en verschillende AI-frameworks.

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

**Architectuur:** Multi-module leerpad met praktische voorbeelden die Edge AI-implementatiepatronen demonstreren

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

## Vereisten

### Benodigde tools

- **Python 3.8+** - Voor AI/ML-voorbeelden en notebooks
- **Node.js 16+** - Voor Electron-voorbeeldapplicatie
- **Git** - Voor versiebeheer
- **Microsoft Foundry Local** - Voor het lokaal uitvoeren van AI-modellen

### Aanbevolen tools

- **Visual Studio Code** - Met Python-, Jupyter- en Pylance-extensies
- **Windows Terminal** - Voor een betere command-line ervaring (Windows-gebruikers)
- **Docker** - Voor containergebaseerde ontwikkeling (optioneel)

### Systeemvereisten

- **RAM**: Minimaal 8GB, aanbevolen 16GB+ voor multi-modelscenario's
- **Opslag**: Minimaal 10GB vrije ruimte voor modellen en afhankelijkheden
- **OS**: Windows 10/11, macOS 11+ of Linux (Ubuntu 20.04+)
- **Hardware**: CPU met AVX2-ondersteuning; GPU (CUDA, Qualcomm NPU) optioneel maar aanbevolen

### Kennisvereisten

- Basiskennis van Python-programmering
- Vertrouwdheid met command-line interfaces
- Begrip van AI/ML-concepten (voor voorbeeldontwikkeling)
- Git-workflows en pull request-processen

## Installatiecommando's

### Repository-installatie

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python-voorbeeldinstallatie (Module08 en Python-voorbeelden)

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

### Node.js-voorbeeldinstallatie (Voorbeeld 08 - Windows Chat App)

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

### Foundry Local-installatie

Foundry Local is vereist om de voorbeelden uit te voeren. Download en installeer vanuit de officiële repository:

**Installatie:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Handmatig**: Download van [releases-pagina](https://github.com/microsoft/Foundry-Local/releases)

**Snelle start:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-3.5-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Opmerking**: Foundry Local selecteert automatisch de beste modelvariant voor jouw hardware (CUDA GPU, Qualcomm NPU of CPU).

## Ontwikkelworkflow

### Contentontwikkeling

Deze repository bevat voornamelijk **Markdown educatieve content**. Bij het aanbrengen van wijzigingen:

1. Bewerk `.md`-bestanden in de juiste modulemappen
2. Volg bestaande opmaakpatronen
3. Zorg ervoor dat codevoorbeelden nauwkeurig en getest zijn
4. Werk bijbehorende vertaalde content bij indien nodig (of laat automatisering dit afhandelen)

### Voorbeeldapplicatieontwikkeling

Voor Python-voorbeelden (voorbeelden 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Voor Electron-voorbeeld (voorbeeld 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testen van voorbeeldapplicaties

Python-voorbeelden hebben geen geautomatiseerde tests, maar kunnen worden gevalideerd door ze uit te voeren:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron-voorbeeld heeft testinfrastructuur:
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
1. Bekijk Markdown-rendering door `.md`-bestanden te previewen
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

**Python-voorbeelden moeten handmatig worden getest:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Code-stijlrichtlijnen

### Markdown-content

- Gebruik een consistente koppenhiërarchie (# voor titel, ## voor hoofdsecties, ### voor subsecties)
- Voeg codeblokken toe met taalspecificaties: ```python, ```bash, ```javascript
- Volg bestaande opmaak voor tabellen, lijsten en nadruk
- Houd regels leesbaar (streef naar ~80-100 tekens, maar niet strikt)
- Gebruik relatieve links voor interne verwijzingen

### Python-code stijl

- Volg PEP 8-conventies
- Gebruik type hints waar nodig
- Voeg docstrings toe voor functies en klassen
- Gebruik betekenisvolle variabelnamen
- Houd functies gefocust en beknopt

### JavaScript/Node.js-code stijl

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Belangrijke conventies:**
- ESLint-configuratie beschikbaar in voorbeeld 08
- Prettier voor codeopmaak
- Gebruik moderne ES6+ syntaxis
- Volg bestaande patronen in de codebase

## Richtlijnen voor pull requests

### Bijdrageworkflow

1. **Fork de repository** en maak een nieuwe branch van `main`
2. **Breng je wijzigingen aan** volgens de code-stijlrichtlijnen
3. **Test grondig** met behulp van de bovenstaande testinstructies
4. **Commit met duidelijke berichten** volgens het format van conventionele commits
5. **Push naar je fork** en maak een pull request
6. **Reageer op feedback** van maintainers tijdens de review

### Branchnaamconventie

- `feature/<module>-<beschrijving>` - Voor nieuwe functies of content
- `fix/<module>-<beschrijving>` - Voor bugfixes
- `docs/<beschrijving>` - Voor documentatieverbeteringen
- `refactor/<beschrijving>` - Voor codeherstructurering

### Commitberichtformat

Volg [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Voorbeelden:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Titelformat
```
[ModuleXX] Brief description of change
```
of
```
[Module08/samples/XX] Description for sample changes
```

### Gedragscode

Alle bijdragers moeten de [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) volgen. Bekijk [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) voordat je bijdraagt.

### Voordat je indient

**Voor contentwijzigingen:**
- Preview alle gewijzigde Markdown-bestanden
- Controleer of links en afbeeldingen werken
- Controleer op typfouten en grammaticale fouten

**Voor wijzigingen in voorbeeldcode (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Voor wijzigingen in Python-voorbeelden:**
- Test of het voorbeeld succesvol wordt uitgevoerd
- Controleer of foutafhandeling werkt
- Controleer compatibiliteit met Foundry Local

### Reviewproces

- Wijzigingen in educatieve content worden beoordeeld op nauwkeurigheid en duidelijkheid
- Codevoorbeelden worden getest op functionaliteit
- Vertalingsupdates worden automatisch afgehandeld door GitHub Actions

## Vertalingssysteem

**BELANGRIJK:** Deze repository gebruikt geautomatiseerde vertaling via GitHub Actions.

- Vertalingen staan in de map `/translations/` (50+ talen)
- Geautomatiseerd via de workflow `co-op-translator.yml`
- **WIJZIG vertaalbestanden NIET handmatig** - ze worden overschreven
- Bewerk alleen Engelse bronbestanden in de root- en modulemappen
- Vertalingen worden automatisch gegenereerd bij een push naar de `main` branch

## Foundry Local-integratie

De meeste Module08-voorbeelden vereisen dat Microsoft Foundry Local actief is.

### Installatie & Setup

**Installeer Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Installeer Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local starten
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

### SDK-gebruik (Python)
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

### Foundry Local verifiëren
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Omgevingsvariabelen voor voorbeelden

De meeste voorbeelden gebruiken deze omgevingsvariabelen:
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

**Opmerking**: Bij gebruik van `FoundryLocalManager` handelt de SDK automatisch serviceontdekking en modellading af. Modelaliassen (zoals `phi-3.5-mini`) zorgen ervoor dat de beste variant wordt geselecteerd voor jouw hardware.

## Build en implementatie

### Contentimplementatie

Deze repository is voornamelijk documentatie - geen buildproces vereist voor content.

### Buildproces voor voorbeeldapplicaties

**Electron-applicatie (Module08/samples/08):**
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

**Python-voorbeelden:**
Geen buildproces - voorbeelden worden direct uitgevoerd met de Python-interpreter.

## Veelvoorkomende problemen en oplossingen

> **Tip**: Bekijk [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) voor bekende problemen en oplossingen.

### Kritieke problemen (blokkerend)

#### Foundry Local niet actief
**Probleem:** Voorbeelden falen met verbindingsfouten

**Oplossing:**
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

### Veelvoorkomende problemen (matig)

#### Problemen met Python-virtuele omgeving
**Probleem:** Module-importfouten

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

#### Electron-buildproblemen
**Probleem:** npm install of buildfouten

**Oplossing:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Workflowproblemen (klein)

#### Vertaalworkflowconflicten
**Probleem:** Vertaal-PR conflicteert met jouw wijzigingen

**Oplossing:**
- Bewerk alleen Engelse bronbestanden
- Laat de geautomatiseerde vertaalworkflow vertalingen afhandelen
- Als er conflicten optreden, merge `main` in jouw branch nadat vertalingen zijn samengevoegd

#### Problemen met modeldownloads
**Probleem:** Foundry Local kan modellen niet downloaden

**Oplossing:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Aanvullende bronnen

### Leertrajecten
- **Beginnerstraject:** Modules 01-02 (7-9 uur)
- **Intermediate traject:** Modules 03-04 (9-11 uur)
- **Advanced traject:** Modules 05-07 (12-15 uur)
- **Expert traject:** Module 08 (8-10 uur)

### Belangrijke modulecontent
- **Module01:** EdgeAI-grondbeginselen en praktijkvoorbeelden
- **Module02:** Small Language Model (SLM)-families en architecturen
- **Module03:** Lokale en cloudimplementatiestrategieën
- **Module04:** Modeloptimalisatie met meerdere frameworks
- **Module05:** SLMOps - productieoperaties
- **Module06:** AI-agenten en functieaanroepen
- **Module07:** Platformspecifieke implementaties
- **Module08:** Foundry Local-toolkit met 10 uitgebreide voorbeelden

### Externe afhankelijkheden
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Lokale AI-modelruntime met OpenAI-compatibele API
  - [Documentatie](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimalisatieframework
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Modeloptimalisatietoolkit
- [OpenVINO](https://docs.openvino.ai/) - Intel's optimalisatietoolkit

## Projectspecifieke opmerkingen

### Module08-voorbeeldapplicaties

De repository bevat 10 uitgebreide voorbeeldapplicaties:

1. **01-REST Chat Quickstart** - Basisintegratie OpenAI SDK
2. **02-OpenAI SDK-integratie** - Geavanceerde SDK-functies
3. **03-Modelontdekking & benchmarking** - Modelvergelijkingstools
4. **04-Chainlit RAG-applicatie** - Retrieval-augmented generation
5. **05-Multi-agent orkestratie** - Basiscoördinatie van agenten
6. **06-Models-as-Tools Router** - Intelligente modelroutering
7. **07-Direct API Client** - Laag-niveau API-integratie
8. **08-Windows 11 Chat App** - Native Electron-desktopapplicatie
9. **09-Geavanceerd multi-agentsysteem** - Complexe agentenorkestratie
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel-integratie

Elk voorbeeld demonstreert verschillende aspecten van Edge AI-ontwikkeling met Foundry Local.

### Prestatieoverwegingen

- SLM's zijn geoptimaliseerd voor edge-implementatie (2-16GB RAM)
- Lokale inferentie biedt responstijden van 50-500ms
- Kwantiseringstechnieken bereiken een groottevermindering van 75% met behoud van 85% prestaties
- Mogelijkheden voor realtime gesprekken met lokale modellen

### Beveiliging en Privacy

- Alle verwerking gebeurt lokaal - geen gegevens worden naar de cloud verzonden
- Geschikt voor privacygevoelige toepassingen (gezondheidszorg, financiën)
- Voldoet aan eisen voor gegevenssoevereiniteit
- Foundry Local draait volledig op lokale hardware

## Hulp krijgen

### Documentatie

- **Hoofd README**: [README.md](README.md) - Overzicht van de repository en leerpaden
- **Studiegids**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Leermiddelen en tijdlijn
- **Ondersteuning**: [SUPPORT.md](SUPPORT.md) - Hoe hulp te krijgen
- **Beveiliging**: [SECURITY.md](SECURITY.md) - Beveiligingsproblemen melden

### Communityondersteuning

- **GitHub Issues**: [Meld bugs of vraag functies aan](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Stel vragen en deel ideeën](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Technische problemen met Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Contact

- **Beheerders**: Zie [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Beveiligingsproblemen**: Volg verantwoordelijke openbaarmaking in [SECURITY.md](SECURITY.md)
- **Microsoft Ondersteuning**: Voor ondersteuning op bedrijfsniveau, neem contact op met de klantenservice van Microsoft

### Aanvullende bronnen

- **Microsoft Learn**: [AI en Machine Learning Leertrajecten](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Documentatie**: [Officiële Documentatie](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Communityvoorbeelden**: Bekijk [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) voor bijdragen van de community

---

**Dit is een educatieve repository gericht op het onderwijzen van Edge AI-ontwikkeling. Het belangrijkste bijdragepatroon is het verbeteren van educatieve inhoud en het toevoegen/verbeteren van voorbeeldtoepassingen die Edge AI-concepten demonstreren.**

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.