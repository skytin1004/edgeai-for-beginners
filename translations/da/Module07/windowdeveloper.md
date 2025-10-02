<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77bb931ce93583c081cf7861f43d9662",
  "translation_date": "2025-10-02T13:12:58+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "da"
}
-->
# Windows Edge AI Udviklingsguide

## Introduktion

Velkommen til Windows Edge AI Udvikling - din omfattende guide til at bygge intelligente applikationer, der udnytter kraften af AI direkte på enheden ved hjælp af Microsofts Windows AI Foundry-platform. Denne guide er specielt designet til Windows-udviklere, der ønsker at integrere avancerede Edge AI-funktioner i deres applikationer og samtidig udnytte Windows' hardwareacceleration fuldt ud.

### Fordelene ved Windows AI

Windows AI Foundry repræsenterer en samlet, pålidelig og sikker platform, der understøtter hele AI-udviklerens livscyklus - fra modelvalg og finjustering til optimering og implementering på tværs af CPU, GPU, NPU og hybrid cloud-arkitekturer. Platformen demokratiserer AI-udvikling ved at tilbyde:

- **Hardwareabstraktion**: Problemfri implementering på AMD-, Intel-, NVIDIA- og Qualcomm-chips
- **Intelligens på enheden**: AI, der bevarer privatliv og kører udelukkende på lokal hardware
- **Optimeret ydeevne**: Modeller, der er forudoptimeret til Windows-hardwarekonfigurationer
- **Klar til erhvervslivet**: Produktionsklare sikkerheds- og compliance-funktioner

### Hvorfor vælge Windows til Edge AI?

**Universel hardwareunderstøttelse**  
Windows ML tilbyder automatisk hardwareoptimering på tværs af hele Windows-økosystemet, hvilket sikrer, at dine AI-applikationer fungerer optimalt uanset den underliggende chiparkitektur.

**Integreret AI-runtime**  
Den indbyggede Windows ML-inferensmotor eliminerer komplekse opsætningskrav, så udviklere kan fokusere på applikationslogik frem for infrastruktur.

**Copilot+ PC Optimering**  
Specialdesignede API'er til næste generations Windows-enheder med dedikerede Neural Processing Units (NPUs), der leverer enestående ydeevne pr. watt.

**Udviklerøkosystem**  
Omfattende værktøjer, herunder Visual Studio-integration, detaljeret dokumentation og eksempelsapplikationer, der fremskynder udviklingsprocessen.

## Læringsmål

Ved at gennemføre denne Windows Edge AI-udviklingsguide vil du mestre de essentielle færdigheder til at bygge produktionsklare AI-applikationer på Windows-platformen.

### Kernekompetencer

**Windows AI Foundry Ekspertise**  
- Forstå arkitekturen og komponenterne i Windows AI Foundry-platformen  
- Naviger gennem hele AI-udviklingslivscyklussen inden for Windows-økosystemet  
- Implementer sikkerhedsbedste praksis for AI-applikationer på enheden  
- Optimer applikationer til forskellige Windows-hardwarekonfigurationer  

**API Integration**  
- Mestre Windows AI API'er til tekst-, vision- og multimodale applikationer  
- Implementer Phi Silica sprogmodelintegration til tekstgenerering og ræsonnement  
- Udrul computer vision-funktioner ved hjælp af indbyggede billedbehandlings-API'er  
- Tilpas fortrænede modeller ved hjælp af LoRA (Low-Rank Adaptation) teknikker  

**Foundry Local Implementering**  
- Gennemse, evaluere og implementere open source-sprogmodeller ved hjælp af Foundry Local CLI  
- Forstå modeloptimering og kvantisering til lokal implementering  
- Implementer offline AI-funktioner, der fungerer uden internetforbindelse  
- Administrer modellivscyklusser og opdateringer i produktionsmiljøer  

**Windows ML Implementering**  
- Integrer brugerdefinerede ONNX-modeller i Windows-applikationer ved hjælp af Windows ML  
- Udnyt automatisk hardwareacceleration på tværs af CPU-, GPU- og NPU-arkitekturer  
- Implementer realtidsinferens med optimal ressourceudnyttelse  
- Design skalerbare AI-applikationer til forskellige Windows-enhedskategorier  

### Applikationsudviklingsfærdigheder

**Cross-Platform Windows Udvikling**  
- Byg AI-drevne applikationer ved hjælp af .NET MAUI til universel Windows-implementering  
- Integrer AI-funktioner i Win32-, UWP- og Progressive Web Applications  
- Implementer responsive UI-designs, der tilpasser sig AI-processeringsstatus  
- Håndter asynkrone AI-operationer med passende brugeroplevelsesmønstre  

**Ydeevneoptimering**  
- Profilér og optimer AI-inferensydelse på tværs af forskellige hardwarekonfigurationer  
- Implementer effektiv hukommelsesstyring for store sprogmodeller  
- Design applikationer, der nedskalerer yndefuldt baseret på tilgængelige hardwarekapaciteter  
- Anvend caching-strategier for ofte brugte AI-operationer  

**Produktionsklarhed**  
- Implementer omfattende fejlhåndtering og fallback-mekanismer  
- Design telemetri og overvågning for AI-applikationers ydeevne  
- Anvend sikkerhedsbedste praksis for lokal AI-modelopbevaring og eksekvering  
- Planlæg implementeringsstrategier for erhvervs- og forbrugerapplikationer  

### Forretnings- og strategisk forståelse

**AI Applikationsarkitektur**  
- Design hybride arkitekturer, der optimerer mellem lokal og cloud AI-processering  
- Evaluer afvejninger mellem modelstørrelse, nøjagtighed og inferenshastighed  
- Planlæg dataflowarkitekturer, der bevarer privatliv og samtidig muliggør intelligens  
- Implementer omkostningseffektive AI-løsninger, der skalerer med brugerbehov  

**Markedspositionering**  
- Forstå konkurrencefordele ved Windows-native AI-applikationer  
- Identificer brugsscenarier, hvor AI på enheden giver overlegne brugeroplevelser  
- Udvikl go-to-market strategier for AI-forbedrede Windows-applikationer  
- Positionér applikationer til at udnytte Windows-økosystemets fordele  

## Windows App SDK AI Eksempler

Windows App SDK tilbyder omfattende eksempler, der demonstrerer AI-integration på tværs af flere frameworks og implementeringsscenarier. Disse eksempler er essentielle referencer til forståelse af Windows AI-udviklingsmønstre.

### Windows AI Foundry Eksempler

| Eksempel | Framework | Fokusområde | Nøglefunktioner |
|----------|-----------|-------------|-----------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API Integration | Komplet WinUI-app, der demonstrerer Windows AI API'er, ARM64-optimering, pakket implementering |

**Nøgleteknologier:**  
- Windows AI API'er  
- WinUI 3 framework  
- ARM64 platformoptimering  
- Copilot+ PC-kompatibilitet  
- Pakket app-implementering  

**Forudsætninger:**  
- Windows 11 med Copilot+ PC anbefales  
- Visual Studio 2022  
- ARM64 build-konfiguration  
- Windows App SDK 1.8.1+  

### Windows ML Eksempler

#### C++ Eksempler

| Eksempel | Type | Fokusområde | Nøglefunktioner |
|----------|------|-------------|-----------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Console App | Grundlæggende Windows ML | EP-opdagelse, kommandolinjemuligheder, modelkompilering |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Console App | Framework Implementering | Delt runtime, mindre implementeringsfodaftryk |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Console App | Selvstændig Implementering | Standalone implementering, ingen runtime-afhængigheder |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Biblioteksbrug | WindowsML i delt bibliotek, hukommelsesstyring |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet Tutorial | Modelkonvertering, EP-kompilering, Build 2025 tutorial |

#### C# Eksempler

**Console Applikationer**

| Eksempel | Type | Fokusområde | Nøglefunktioner |
|----------|------|-------------|-----------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Console App | Grundlæggende C# Integration | Delt hjælperbrug, kommandolinjegrænseflade |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet Tutorial | Modelkonvertering, EP-kompilering, Build 2025 tutorial |

**GUI Applikationer**

| Eksempel | Framework | Fokusområde | Nøglefunktioner |
|----------|-----------|-------------|-----------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | Billedklassifikation med WPF-grænseflade |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Traditionel GUI | Billedklassifikation med Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderne GUI | Billedklassifikation med WinUI 3-grænseflade |

#### Python Eksempler

| Eksempel | Sprog | Fokusområde | Nøglefunktioner |
|----------|-------|-------------|-----------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Billedklassifikation | WinML Python bindings, batch billedbehandling |

### Eksempel Forudsætninger

**Systemkrav:**  
- Windows 11 PC med version 24H2 (build 26100) eller nyere  
- Visual Studio 2022 med C++ og .NET workloads  
- Windows App SDK 1.8.1 eller senere  
- Python 3.10-3.13 til Python-eksempler på x64 og ARM64-enheder  

**Windows AI Foundry Specifik:**  
- Copilot+ PC anbefales for optimal ydeevne  
- ARM64 build-konfiguration til Windows AI-eksempler  
- Pakkeidentitet krævet (upakkede apps understøttes ikke længere)  

### Almindelig Eksempelarbejdsgang

De fleste Windows ML-eksempler følger dette standardmønster:

1. **Initialiser Miljø** - Opret ONNX Runtime-miljø  
2. **Registrer Execution Providers** - Opdag og registrer tilgængelige hardwareacceleratorer (CPU, GPU, NPU)  
3. **Indlæs Model** - Indlæs ONNX-model, eventuelt kompileret til målhardware  
4. **Forbehandl Input** - Konverter billeder/data til modelinputformat  
5. **Kør Inferens** - Udfør model og få forudsigelser  
6. **Behandl Resultater** - Anvend softmax og vis topforudsigelser  

### Brugte Modelfiler

| Model | Formål | Inkluderet | Noter |
|-------|--------|------------|-------|
| SqueezeNet | Letvægts billedklassifikation | ✅ Inkluderet | Fortrænet, klar til brug |
| ResNet-50 | Højpræcision billedklassifikation | ❌ Kræver konvertering | Brug [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) til konvertering |

### Hardwareunderstøttelse

Alle eksempler registrerer og udnytter automatisk tilgængelig hardware:  
- **CPU** - Universel understøttelse på alle Windows-enheder  
- **GPU** - Automatisk registrering og optimering til tilgængelig grafikhardware  
- **NPU** - Udnytter Neural Processing Units på understøttede enheder (Copilot+ PC'er)  

## Windows AI Foundry Platformkomponenter

### 1. Windows AI API'er

Windows AI API'er tilbyder færdige AI-funktioner drevet af modeller på enheden, optimeret til effektivitet og ydeevne på Copilot+ PC-enheder med minimal opsætning.

#### Kerne API-kategorier

**Phi Silica Sprogmodel**  
- Lille, men kraftfuld sprogmodel til tekstgenerering og ræsonnement  
- Optimeret til realtidsinferens med minimal strømforbrug  
- Understøttelse af brugerdefineret finjustering ved hjælp af LoRA-teknikker  
- Integration med Windows semantisk søgning og videnshentning  

**Computer Vision API'er**  
- **Tekstgenkendelse (OCR)**: Uddrag tekst fra billeder med høj nøjagtighed  
- **Billedsuperopløsning**: Opskalér billeder ved hjælp af lokale AI-modeller  
- **Billedsegmentering**: Identificér og isolér specifikke objekter i billeder  
- **Billedbeskrivelse**: Generér detaljerede tekstbeskrivelser for visuelt indhold  
- **Objektfjernelse**: Fjern uønskede objekter fra billeder med AI-drevet inpainting  

**Multimodale Funktioner**  
- **Vision-Sprog Integration**: Kombinér tekst- og billedforståelse  
- **Semantisk Søgning**: Muliggør naturlige sprogforespørgsler på tværs af multimedieindhold  
- **Videnshentning**: Byg intelligente søgeoplevelser med lokale data  

### 2. Foundry Local

Foundry Local giver udviklere hurtig adgang til færdige open source-sprogmodeller på Windows Silicon, med mulighed for at gennemse, teste, interagere og implementere modeller i lokale applikationer.

#### Foundry Local Eksempelsapplikationer

[Foundry Local repository](https://github.com/microsoft/Foundry-Local/tree/main/samples) tilbyder omfattende eksempler på tværs af flere programmeringssprog og frameworks, der demonstrerer forskellige integrationsmønstre og brugsscenarier.

| Eksempel | Sprog/Framework | Fokusområde | Nøglefunktioner |
|----------|-----------------|-------------|-----------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG Implementering | Semantisk Kernel integration, Qdrant vektorlagring, JINA embeddings, dokumentindtagelse, streaming chat |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Desktop Chat App | Cross-platform chat, lokal/cloud modelskift, OpenAI SDK integration, realtidsstreaming |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Grundlæggende Integration | Enkel SDK-brug, modelinitialisering, grundlæggende chatfunktionalitet |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Grundlæggende Integration | Python SDK-brug, streaming svar, OpenAI-kompatibel API |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Systemintegration | Lav-niveau SDK-brug, asynkrone operationer, reqwest HTTP-klient |

#### Eksempelkategorier efter Brugsscenarie

**RAG (Retrieval-Augmented Generation)**  
- **dotNET/rag**: Komplet RAG-implementering ved hjælp af Semantisk Kernel, Qdrant vektordatabase og JINA embeddings  
- **Arkitektur**: Dokumentindtagelse → Tekstopdeling → Vektorembeddings → Lighedssøgning → Kontekstbevidste svar  
- **Teknologier**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddings, streaming chat-komplettering  

**Desktop Applikationer**  
- **electron/foundry-chat**: Produktionsklar chatapplikation med lokal/cloud modelskift  
- **Funktioner**: Modelvælger, streaming-svar, fejlhåndtering, tværplatformsudrulning  
- **Arkitektur**: Electron hovedproces, IPC-kommunikation, sikre preload-scripts  

**Eksempler på SDK-integration**  
- **JavaScript (Node.js)**: Grundlæggende modelinteraktion og streaming-svar  
- **Python**: OpenAI-kompatibel API-brug med asynkron streaming  
- **Rust**: Lav-niveau integration med reqwest og tokio til asynkrone operationer  

#### Forudsætninger for Foundry Local eksempler  

**Systemkrav:**  
- Windows 11 med Foundry Local installeret  
- Node.js v16+ til JavaScript/Electron eksempler  
- .NET 8.0+ til C# eksempler  
- Python 3.10+ til Python eksempler  
- Rust 1.70+ til Rust eksempler  

**Installation:**  
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```
  

#### Specifik opsætning for eksempler  

**dotNET RAG eksempel:**  
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```
  
**Electron Chat eksempel:**  
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```
  
**JavaScript/Python/Rust eksempler:**  
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```
  

#### Nøglefunktioner  

**Modelkatalog**  
- Omfattende samling af præoptimerede open source-modeller  
- Modeller optimeret til CPU'er, GPU'er og NPU'er for øjeblikkelig udrulning  
- Understøttelse af populære modelfamilier som Llama, Mistral, Phi og specialiserede domænemodeller  

**CLI-integration**  
- Kommandolinjegrænseflade til modelstyring og udrulning  
- Automatiserede optimerings- og kvantiseringsarbejdsgange  
- Integration med populære udviklingsmiljøer og CI/CD-pipelines  

**Lokal udrulning**  
- Fuld offline drift uden cloud-afhængigheder  
- Understøttelse af brugerdefinerede modelformater og konfigurationer  
- Effektiv modelservering med automatisk hardwareoptimering  

### 3. Windows ML  

Windows ML fungerer som den centrale AI-platform og integrerede inferens-runtime på Windows, hvilket gør det muligt for udviklere at udrulle brugerdefinerede modeller effektivt på tværs af det brede Windows-hardwareøkosystem.  

#### Arkitekturmæssige fordele  

**Universel hardwareunderstøttelse**  
- Automatisk optimering til AMD-, Intel-, NVIDIA- og Qualcomm-silicium  
- Understøttelse af CPU-, GPU- og NPU-eksekvering med transparent skift  
- Hardwareabstraktion, der eliminerer platformsspecifik optimeringsarbejde  

**Modelfleksibilitet**  
- Understøttelse af ONNX-modelformat med automatisk konvertering fra populære frameworks  
- Brugerdefineret modeludrulning med produktionsklar ydeevne  
- Integration med eksisterende Windows-applikationsarkitekturer  

**Enterprise-integration**  
- Kompatibel med Windows sikkerheds- og overholdelsesrammer  
- Understøttelse af enterprise-udrulning og styringsværktøjer  
- Integration med Windows enhedsstyring og overvågningssystemer  

## Udviklingsworkflow  

### Fase 1: Opsætning af miljø og værktøjskonfiguration  

**Forberedelse af udviklingsmiljø**  
1. Installer Visual Studio 2022 med C++ og .NET workloads  
2. Installer Windows App SDK 1.8.1 eller nyere  
3. Konfigurer Windows AI Foundry CLI-værktøjer  
4. Opsæt AI Toolkit-udvidelsen til Visual Studio Code  
5. Etabler værktøjer til performanceprofilering og overvågning  
6. Sørg for ARM64 build-konfiguration til Copilot+ PC-optimering  

**Opsætning af eksempelrepository**  
1. Klon [Windows App SDK Samples repository](https://github.com/microsoft/WindowsAppSDK-Samples)  
2. Naviger til `Samples/WindowsAIFoundry/cs-winui` for Windows AI API-eksempler  
3. Naviger til `Samples/WindowsML` for omfattende Windows ML-eksempler  
4. Gennemgå [build-krav](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) for dine målplatforme  

**Udforskning af AI Dev Gallery**  
- Udforsk eksempelapplikationer og referenceimplementeringer  
- Test Windows AI API'er med interaktive demonstrationer  
- Gennemgå kildekode for bedste praksis og mønstre  
- Identificer relevante eksempler til din specifikke brugssag  

### Fase 2: Modelvalg og integration  

**Kravsanalyse**  
- Definer funktionelle krav til AI-funktioner  
- Etabler performancebegrænsninger og optimeringsmål  
- Evaluer privatlivs- og sikkerhedskrav  
- Planlæg udrulningsarkitektur og skaleringsstrategier  

**Modelevaluering**  
- Brug Foundry Local til at teste open source-modeller til din brugssag  
- Benchmark Windows AI API'er mod brugerdefinerede modelkrav  
- Evaluer afvejninger mellem modelstørrelse, nøjagtighed og inferenshastighed  
- Prototype integrationsmetoder med udvalgte modeller  

### Fase 3: Applikationsudvikling  

**Kerneintegration**  
- Implementer Windows AI API-integration med korrekt fejlhåndtering  
- Design brugergrænseflader, der understøtter AI-processeringsarbejdsgange  
- Implementer caching og optimeringsstrategier for modelinferens  
- Tilføj telemetri og overvågning for AI-driftens ydeevne  

**Test og validering**  
- Test applikationer på tværs af forskellige Windows-hardwarekonfigurationer  
- Valider performance-metrics under forskellige belastningsforhold  
- Implementer automatiserede tests for AI-funktioners pålidelighed  
- Udfør brugeroplevelsestest med AI-forbedrede funktioner  

### Fase 4: Optimering og udrulning  

**Performanceoptimering**  
- Profilér applikationsydelse på tværs af målhardwarekonfigurationer  
- Optimer hukommelsesbrug og modelladningsstrategier  
- Implementer adaptiv adfærd baseret på tilgængelige hardwarekapaciteter  
- Finjuster brugeroplevelsen for forskellige performance-scenarier  

**Produktionsudrulning**  
- Pak applikationer med korrekte AI-modelafhængigheder  
- Implementer opdateringsmekanismer for modeller og applikationslogik  
- Konfigurer overvågning og analyse for produktionsmiljøer  
- Planlæg udrulningsstrategier for enterprise- og forbrugerudrulninger  

## Praktiske implementeringseksempler  

### Eksempel 1: Intelligent dokumentbehandlingsapplikation  

Byg en Windows-applikation, der behandler dokumenter ved hjælp af flere AI-funktioner:  

**Anvendte teknologier:**  
- Phi Silica til dokumentopsummering og spørgsmål/svar  
- OCR API'er til tekstudtrækning fra scannede dokumenter  
- Image Description API'er til analyse af diagrammer og grafer  
- Brugerdefinerede ONNX-modeller til dokumentklassificering  

**Implementeringsmetode:**  
- Design modulær arkitektur med udskiftelige AI-komponenter  
- Implementer asynkron behandling for store dokumentbatches  
- Tilføj statusindikatorer og annulleringsmuligheder for langvarige operationer  
- Inkluder offline kapacitet til behandling af følsomme dokumenter  

### Eksempel 2: Detailhandels lagerstyringssystem  

Skab et AI-drevet lagerstyringssystem til detailhandelsapplikationer:  

**Anvendte teknologier:**  
- Image Segmentation til produktidentifikation  
- Brugerdefinerede visionsmodeller til mærke- og kategoriklassificering  
- Foundry Local udrulning af specialiserede detailhandels sprogmodeller  
- Integration med eksisterende POS- og lagerstyringssystemer  

**Implementeringsmetode:**  
- Byg kamera-integration til realtids produktscanning  
- Implementer stregkode- og visuel produktgenkendelse  
- Tilføj naturlige sprogforespørgsler til lagerstyring med lokale sprogmodeller  
- Design skalerbar arkitektur til udrulning på tværs af flere butikker  

### Eksempel 3: Sundhedsdokumentationsassistent  

Udvikl et privatlivsbevarende værktøj til sundhedsdokumentation:  

**Anvendte teknologier:**  
- Phi Silica til generering af medicinske noter og klinisk beslutningsstøtte  
- OCR til digitalisering af håndskrevne medicinske journaler  
- Brugerdefinerede medicinske sprogmodeller udrullet via Windows ML  
- Lokal vektorlagring til medicinsk videnssøgning  

**Implementeringsmetode:**  
- Sørg for fuld offline drift for patientprivatliv  
- Implementer validering og forslag til medicinsk terminologi  
- Tilføj revisionslogning for overholdelse af lovgivning  
- Design integration med eksisterende elektroniske patientjournal-systemer  

## Performanceoptimeringsstrategier  

### Hardwarebevidst udvikling  

**NPU-optimering**  
- Design applikationer til at udnytte NPU-kapaciteter på Copilot+ PC'er  
- Implementer elegant fallback til GPU/CPU på enheder uden NPU  
- Optimer modelformater til NPU-specifik acceleration  
- Overvåg NPU-udnyttelse og termiske egenskaber  

**Hukommelsesstyring**  
- Implementer effektive modelladnings- og cachingstrategier  
- Brug hukommelseskortlægning til store modeller for at reducere opstartstid  
- Design hukommelsesbevidste applikationer til ressourcebegrænsede enheder  
- Implementer modelkvantisering for hukommelsesoptimering  

**Batterieffektivitet**  
- Optimer AI-operationer for minimal strømforbrug  
- Implementer adaptiv behandling baseret på batteristatus  
- Design effektiv baggrundsbehandling til kontinuerlige AI-operationer  
- Brug værktøjer til strømprofilering for at optimere energiforbrug  

### Skalerbarhedsovervejelser  

**Multitrådning**  
- Design trådsikre AI-operationer til samtidig behandling  
- Implementer effektiv arbejdsfordeling på tværs af tilgængelige kerner  
- Brug async/await mønstre til ikke-blokerende AI-operationer  
- Planlæg optimering af trådpool til forskellige hardwarekonfigurationer  

**Cachingstrategier**  
- Implementer intelligent caching til ofte anvendte AI-operationer  
- Design cache-invalideringsstrategier til modelopdateringer  
- Brug vedvarende caching til dyre forbehandlingsoperationer  
- Implementer distribueret caching til scenarier med flere brugere  

## Sikkerheds- og privatlivsbedste praksis  

### Databeskyttelse  

**Lokal behandling**  
- Sørg for, at følsomme data aldrig forlader den lokale enhed  
- Implementer sikker lagring til AI-modeller og midlertidige data  
- Brug Windows sikkerhedsfunktioner til applikationssandboxing  
- Anvend kryptering til lagrede modeller og mellemresultater  

**Modelsikkerhed**  
- Valider modelintegritet før indlæsning og eksekvering  
- Implementer sikre modelopdateringsmekanismer  
- Brug signerede modeller for at forhindre manipulation  
- Anvend adgangskontrol til modelfiler og konfiguration  

### Overholdelsesovervejelser  

**Regulatorisk tilpasning**  
- Design applikationer til at opfylde GDPR, HIPAA og andre lovkrav  
- Implementer revisionslogning for AI-beslutningsprocesser  
- Tilbyd gennemsigtighedsfunktioner for AI-genererede resultater  
- Giv brugere kontrol over AI-databehandling  

**Enterprise-sikkerhed**  
- Integrer med Windows enterprise-sikkerhedspolitikker  
- Understøt administreret udrulning via enterprise-styringsværktøjer  
- Implementer rollebaseret adgangskontrol til AI-funktioner  
- Tilbyd administrative kontroller for AI-funktionalitet  

## Fejlfinding og debugging  

### Almindelige udviklingsudfordringer  

**Build-konfigurationsproblemer**  
- Sørg for ARM64 platformskonfiguration til Windows AI API-eksempler  
- Verificer kompatibilitet med Windows App SDK-version (1.8.1+ krævet)  
- Kontroller, at pakkeidentitet er korrekt konfigureret (krævet til Windows AI API'er)  
- Valider, at build-værktøjer understøtter målframework-versionen  

**Modelindlæsningsproblemer**  
- Valider ONNX-modelkompatibilitet med Windows ML  
- Kontroller modelintegritet og formatkrav  
- Verificer hardwarekapabilitetskrav til specifikke modeller  
- Debug hukommelsestildelingsproblemer under modelladning  
- Sørg for registrering af eksekveringsudbyder til hardwareacceleration  

**Udrulningstilstandsovervejelser**  
- **Self-Contained Mode**: Fuldt understøttet med større udrulningsstørrelse  
- **Framework-Dependent Mode**: Mindre footprint, men kræver delt runtime  
- **Unpackaged Applications**: Ikke længere understøttet til Windows AI API'er  
- Brug `dotnet run -p:Platform=ARM64 -p:SelfContained=true` til selvstændig ARM64-udrulning  

**Performanceproblemer**  
- Profilér applikationsydelse på tværs af forskellige hardwarekonfigurationer  
- Identificer flaskehalse i AI-processeringspipelines  
- Optimer dataforbehandling og efterbehandlingsoperationer  
- Implementer performanceovervågning og alarmering  

**Integrationsvanskeligheder**  
- Debug API-integrationsproblemer med korrekt fejlhåndtering  
- Valider inputdataformater og forbehandlingskrav  
- Test edge cases og fejlbetingelser grundigt  
- Implementer omfattende logning til debugging af produktionsproblemer  

### Debugging-værktøjer og teknikker  

**Visual Studio-integration**  
- Brug AI Toolkit debugger til analyse af modeludførelse  
- Implementer performanceprofilering for AI-operationer  
- Debug asynkrone AI-operationer med korrekt undtagelseshåndtering  
- Brug hukommelsesprofilering til optimering  

**Windows AI Foundry-værktøjer**  
- Udnyt Foundry Local CLI til modeltest og validering  
- Brug Windows AI API-testværktøjer til integrationsverifikation  
- Implementer brugerdefineret logning til overvågning af AI-operationer  
- Opret automatiserede tests for AI-funktioners pålidelighed  

## Fremtidssikring af dine applikationer  

### Fremvoksende teknologier  

**Næste generations hardware**  
- Design applikationer til at udnytte fremtidige NPU-kapaciteter  
- Planlæg for øgede modelstørrelser og kompleksitet  
- Implementer adaptive arkitekturer til udviklende hardware  
- Overvej kvanteklare algoritmer for fremtidig kompatibilitet  

**Avancerede AI-funktioner**  
- Forbered dig på multimodal AI-integration på tværs af flere datatyper  
- Planlæg for realtids samarbejdende AI mellem flere enheder  
- Design til federeret læringskapacitet  
- Overvej edge-cloud hybrid intelligensarkitekturer  

### Kontinuerlig læring og tilpasning  

**Modelopdateringer**  
- Implementer problemfri modelopdateringsmekanismer  
- Design applikationer til at tilpasse sig forbedrede modelkapaciteter  
- Planlæg for bagudkompatibilitet med eksisterende modeller  
- Implementer A/B-test for evaluering af modelydelse  

**Funktionsudvikling**  
- Design modulære arkitekturer, der kan rumme nye AI-funktioner  
- Planlæg for integration af fremvoksende Windows AI API'er  
- Implementer funktionsflag til gradvis udrulning af kapaciteter  
- Design brugergrænseflader, der tilpasser sig forbedrede AI-funktioner  

## Konklusion  

Windows Edge AI-udvikling repræsenterer konvergensen af kraftfulde AI-funktioner med den robuste, sikre og skalerbare Windows-platform. Ved at mestre Windows AI Foundry-økosystemet kan udviklere skabe intelligente applikationer, der leverer enestående brugeroplevelser, samtidig med at de opretholder de højeste standarder for privatliv, sikkerhed og ydeevne.  

Kombinationen af Windows AI API'er, Foundry Local og Windows ML giver et enestående fundament for at bygge næste generation af intelligente Windows-applikationer. Efterhånden som AI fortsætter med at udvikle sig, sikrer Windows-platformen, at dine applikationer vil skalere med fremvoksende teknologier, samtidig med at de opretholder kompatibilitet og ydeevne på tværs af det mangfoldige Windows-hardwareøkosystem.  

Uanset om du bygger forbrugerapplikationer, enterprise-løsninger eller specialiserede industriværktøjer, giver Windows Edge AI-udvikling dig mulighed for at skabe intelligente, responsive og dybt integrerede oplevelser, der udnytter det fulde potentiale af moderne Windows-enheder.  

## Yderligere ressourcer  

### Dokumentation og læring  
- [Windows AI Foundry Dokumentation](https://learn.microsoft.com/windows/ai/)  
- [Windows AI API'er Reference](https://learn.microsoft.com/windows/ai/apis/)  
- [Kom godt i gang med at bygge en app med Windows AI API'er](https://learn.microsoft.com/windows/ai/apis/model-setup)  
- [Foundry Local Kom godt i gang](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)  

- [Windows App SDK Samples Repository](https://github.com/microsoft/WindowsAppSDK-Samples)

### Udviklingsværktøjer
- [AI Toolkit til Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Eksempler](https://learn.microsoft.com/windows/ai/samples/)
- [Modelkonverteringsværktøjer](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Teknisk Support
- [Windows ML Dokumentation](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Dokumentation](https://onnxruntime.ai/docs/)
- [Windows App SDK Dokumentation](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Rapportér Problemer - Windows App SDK Eksempler](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Fællesskab og Support
- [Windows Udviklerfællesskab](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Træning](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Denne guide er designet til at udvikle sig i takt med det hurtigt fremskridende Windows AI-økosystem. Regelmæssige opdateringer sikrer overensstemmelse med de nyeste platformfunktioner og bedste udviklingspraksis.*

[08. Hands on With Microsoft Foundry Local - Complete Developer Toolkit](../Module08/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.