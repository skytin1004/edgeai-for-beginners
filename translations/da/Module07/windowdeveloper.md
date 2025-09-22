<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9c2dacb560380677a2c923171d3e423d",
  "translation_date": "2025-09-22T20:02:10+00:00",
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
- **Klar til erhvervslivet**: Sikkerhed og overholdelsesfunktioner i produktionskvalitet

### Hvorfor vælge Windows til Edge AI?

**Universel hardwareunderstøttelse**  
Windows ML tilbyder automatisk hardwareoptimering på tværs af hele Windows-økosystemet, hvilket sikrer, at dine AI-applikationer fungerer optimalt uanset den underliggende chiparkitektur.

**Integreret AI-runtime**  
Den indbyggede Windows ML-inferensmotor eliminerer komplekse opsætningskrav, så udviklere kan fokusere på applikationslogik frem for infrastrukturproblemer.

**Copilot+ PC-optimering**  
API'er, der er specielt designet til næste generations Windows-enheder med dedikerede neurale processorenheder (NPUs), leverer enestående ydeevne pr. watt.

**Udviklerøkosystem**  
Omfattende værktøjer, herunder integration med Visual Studio, detaljeret dokumentation og eksempler på applikationer, der fremskynder udviklingscyklusser.

## Læringsmål

Ved at gennemføre denne Windows Edge AI-udviklingsguide vil du mestre de essentielle færdigheder til at bygge produktionsklare AI-applikationer på Windows-platformen.

### Kernekompetencer inden for teknologi

**Windows AI Foundry-ekspertise**  
- Forstå arkitekturen og komponenterne i Windows AI Foundry-platformen  
- Naviger gennem hele AI-udviklingslivscyklussen inden for Windows-økosystemet  
- Implementer sikkerhedsbedste praksis for AI-applikationer på enheden  
- Optimer applikationer til forskellige Windows-hardwarekonfigurationer  

**API-integrationsekspertise**  
- Mestre Windows AI API'er til tekst-, vision- og multimodale applikationer  
- Implementer Phi Silica-sprogsmodelintegration til tekstgenerering og ræsonnement  
- Udrul computer vision-funktioner ved hjælp af indbyggede billedbehandlings-API'er  
- Tilpas forudtrænede modeller ved hjælp af LoRA (Low-Rank Adaptation)-teknikker  

**Foundry Local-implementering**  
- Gennemse, evaluér og implementer open source-sprogsmodeller ved hjælp af Foundry Local CLI  
- Forstå modeloptimering og kvantisering til lokal implementering  
- Implementer offline AI-funktioner, der fungerer uden internetforbindelse  
- Administrer modellivscyklusser og opdateringer i produktionsmiljøer  

**Windows ML-implementering**  
- Integrer brugerdefinerede ONNX-modeller i Windows-applikationer ved hjælp af Windows ML  
- Udnyt automatisk hardwareacceleration på tværs af CPU-, GPU- og NPU-arkitekturer  
- Implementer realtidsinferens med optimal ressourceudnyttelse  
- Design skalerbare AI-applikationer til forskellige Windows-enhedskategorier  

### Applikationsudviklingsfærdigheder

**Windows-udvikling på tværs af platforme**  
- Byg AI-drevne applikationer ved hjælp af .NET MAUI til universel Windows-implementering  
- Integrer AI-funktioner i Win32-, UWP- og Progressive Web Applications  
- Implementer responsive UI-designs, der tilpasser sig AI-behandlingsstatus  
- Håndter asynkrone AI-operationer med korrekte brugeroplevelsesmønstre  

**Ydelsesoptimering**  
- Profilér og optimer AI-inferensydelse på tværs af forskellige hardwarekonfigurationer  
- Implementer effektiv hukommelsesstyring til store sprogsmodeller  
- Design applikationer, der nedskalerer yndefuldt baseret på tilgængelige hardwarekapaciteter  
- Anvend caching-strategier til ofte brugte AI-operationer  

**Produktionsklarhed**  
- Implementer omfattende fejlhåndtering og fallback-mekanismer  
- Design telemetri og overvågning af AI-applikationers ydeevne  
- Anvend sikkerhedsbedste praksis til lokal AI-modelopbevaring og udførelse  
- Planlæg implementeringsstrategier til erhvervs- og forbrugerapplikationer  

### Forretnings- og strategisk forståelse

**AI-applikationsarkitektur**  
- Design hybride arkitekturer, der optimerer mellem lokal og cloud AI-behandling  
- Evaluér afvejninger mellem modelstørrelse, nøjagtighed og inferenshastighed  
- Planlæg dataflowarkitekturer, der bevarer privatliv og samtidig muliggør intelligens  
- Implementer omkostningseffektive AI-løsninger, der skalerer med brugerbehov  

**Markedspositionering**  
- Forstå konkurrencemæssige fordele ved Windows-native AI-applikationer  
- Identificer brugsscenarier, hvor AI på enheden giver overlegne brugeroplevelser  
- Udvikl go-to-market-strategier for AI-forbedrede Windows-applikationer  
- Positionér applikationer til at udnytte Windows-økosystemets fordele  

## Windows AI Foundry-platformkomponenter

### 1. Windows AI API'er

Windows AI API'er tilbyder færdige AI-funktioner drevet af modeller på enheden, optimeret til effektivitet og ydeevne på Copilot+ PC-enheder med minimal opsætning.

#### Kerne-API-kategorier

**Phi Silica-sprogsmodel**  
- Lille, men kraftfuld sprogsmodel til tekstgenerering og ræsonnement  
- Optimeret til realtidsinferens med minimal strømforbrug  
- Understøttelse af brugerdefineret finjustering ved hjælp af LoRA-teknikker  
- Integration med Windows semantisk søgning og videnshentning  

**Computer Vision API'er**  
- **Tekstgenkendelse (OCR)**: Uddrag tekst fra billeder med høj nøjagtighed  
- **Billedsuperopløsning**: Opskalér billeder ved hjælp af lokale AI-modeller  
- **Billedsegmentering**: Identificér og isolér specifikke objekter i billeder  
- **Billedbeskrivelse**: Generér detaljerede tekstbeskrivelser for visuelt indhold  
- **Objektfjernelse**: Fjern uønskede objekter fra billeder med AI-drevet inpainting  

**Multimodale funktioner**  
- **Integration af vision og sprog**: Kombinér tekst- og billedforståelse  
- **Semantisk søgning**: Muliggør naturlige sprogforespørgsler på tværs af multimedieindhold  
- **Videnshentning**: Byg intelligente søgeoplevelser med lokale data  

### 2. Foundry Local

Foundry Local giver udviklere hurtig adgang til færdige open source-sprogsmodeller på Windows Silicon, med mulighed for at gennemse, teste, interagere og implementere modeller i lokale applikationer.

#### Nøglefunktioner

**Modelkatalog**  
- Omfattende samling af forudoptimerede open source-modeller  
- Modeller optimeret på tværs af CPU'er, GPU'er og NPU'er til øjeblikkelig implementering  
- Understøttelse af populære modelfamilier, herunder Llama, Mistral, Phi og specialiserede domænemodeller  

**CLI-integration**  
- Kommandolinjegrænseflade til modelstyring og implementering  
- Automatiserede optimerings- og kvantiseringsarbejdsgange  
- Integration med populære udviklingsmiljøer og CI/CD-pipelines  

**Lokal implementering**  
- Fuld offline drift uden cloud-afhængigheder  
- Understøttelse af brugerdefinerede modelformater og konfigurationer  
- Effektiv modelservering med automatisk hardwareoptimering  

### 3. Windows ML

Windows ML fungerer som den centrale AI-platform og integrerede inferensruntime på Windows, der giver udviklere mulighed for effektivt at implementere brugerdefinerede modeller på tværs af det brede Windows-hardwareøkosystem.

#### Arkitekturmæssige fordele

**Universel hardwareunderstøttelse**  
- Automatisk optimering til AMD-, Intel-, NVIDIA- og Qualcomm-chips  
- Understøttelse af CPU-, GPU- og NPU-udførelse med gennemsigtig skift  
- Hardwareabstraktion, der eliminerer platformsspecifik optimeringsarbejde  

**Modelfleksibilitet**  
- Understøttelse af ONNX-modelformat med automatisk konvertering fra populære frameworks  
- Brugerdefineret modelimplementering med ydeevne i produktionskvalitet  
- Integration med eksisterende Windows-applikationsarkitekturer  

**Erhvervsintegration**  
- Kompatibel med Windows sikkerheds- og overholdelsesrammer  
- Understøttelse af erhvervsimplementering og styringsværktøjer  
- Integration med Windows enhedsstyring og overvågningssystemer  

## Udviklingsarbejdsgang

### Fase 1: Miljøopsætning og værktøjskonfiguration

**Forberedelse af udviklingsmiljø**  
1. Installer Visual Studio med AI Toolkit-udvidelse  
2. Konfigurer Windows AI Foundry CLI-værktøjer  
3. Opsæt lokalt testmiljø for modeller  
4. Etabler værktøjer til ydeevneprofilering og overvågning  

**Udforskning af AI Dev Gallery**  
- Udforsk eksempler på applikationer og referenceimplementeringer  
- Test Windows AI API'er med interaktive demonstrationer  
- Gennemgå kildekode for bedste praksis og mønstre  
- Identificér relevante eksempler til din specifikke brugssag  

### Fase 2: Modelvalg og integration

**Kravsanalyse**  
- Definér funktionelle krav til AI-funktioner  
- Etabler ydeevnebegrænsninger og optimeringsmål  
- Evaluér privatlivs- og sikkerhedskrav  
- Planlæg implementeringsarkitektur og skaleringsstrategier  

**Modelevaluering**  
- Brug Foundry Local til at teste open source-modeller til din brugssag  
- Benchmark Windows AI API'er mod brugerdefinerede modelkrav  
- Evaluér afvejninger mellem modelstørrelse, nøjagtighed og inferenshastighed  
- Prototype integrationsmetoder med valgte modeller  

### Fase 3: Applikationsudvikling

**Kerneintegration**  
- Implementer Windows AI API-integration med korrekt fejlhåndtering  
- Design brugergrænseflader, der tilpasser sig AI-behandlingsarbejdsgange  
- Implementer caching- og optimeringsstrategier for modelinferens  
- Tilføj telemetri og overvågning af AI-driftens ydeevne  

**Test og validering**  
- Test applikationer på tværs af forskellige Windows-hardwarekonfigurationer  
- Valider ydeevnemetrikker under forskellige belastningsforhold  
- Implementer automatiseret test for AI-funktioners pålidelighed  
- Udfør brugeroplevelsestest med AI-forbedrede funktioner  

### Fase 4: Optimering og implementering

**Ydelsesoptimering**  
- Profilér applikationsydelse på tværs af målhardwarekonfigurationer  
- Optimer hukommelsesbrug og modelladningsstrategier  
- Implementer adaptiv adfærd baseret på tilgængelige hardwarekapaciteter  
- Finjustér brugeroplevelsen for forskellige ydeevnescenarier  

**Produktionsimplementering**  
- Pak applikationer med korrekte AI-modelafhængigheder  
- Implementer opdateringsmekanismer for modeller og applikationslogik  
- Konfigurer overvågning og analyse for produktionsmiljøer  
- Planlæg udrulningsstrategier for erhvervs- og forbrugerimplementeringer  

## Praktiske implementeringseksempler

### Eksempel 1: Intelligent dokumentbehandlingsapplikation

Byg en Windows-applikation, der behandler dokumenter ved hjælp af flere AI-funktioner:

**Anvendte teknologier:**  
- Phi Silica til dokumentopsummering og spørgsmål/svar  
- OCR-API'er til tekstudtrækning fra scannede dokumenter  
- Billedbeskrivelses-API'er til analyse af diagrammer og grafer  
- Brugerdefinerede ONNX-modeller til dokumentklassificering  

**Implementeringsmetode:**  
- Design modulær arkitektur med udskiftelige AI-komponenter  
- Implementer asynkron behandling for store dokumentmængder  
- Tilføj statusindikatorer og annulleringsmuligheder for langvarige operationer  
- Inkluder offline-funktionalitet til behandling af følsomme dokumenter  

### Eksempel 2: Detailhandels lagerstyringssystem

Skab et AI-drevet lagerstyringssystem til detailhandelsapplikationer:

**Anvendte teknologier:**  
- Billedsegmentering til produktidentifikation  
- Brugerdefinerede visionmodeller til mærke- og kategoriklassificering  
- Foundry Local-implementering af specialiserede sprogsmodeller til detailhandel  
- Integration med eksisterende POS- og lagerstyringssystemer  

**Implementeringsmetode:**  
- Byg kameraintegration til realtidsproduktscanning  
- Implementer stregkode- og visuel produktgenkendelse  
- Tilføj naturlige sprogforespørgsler til lagerstyring ved hjælp af lokale sprogsmodeller  
- Design skalerbar arkitektur til implementering i flere butikker  

### Eksempel 3: Sundhedsdokumentationsassistent

Udvikl et privatlivsbevarende værktøj til sundhedsdokumentation:

**Anvendte teknologier:**  
- Phi Silica til generering af medicinske noter og klinisk beslutningsstøtte  
- OCR til digitalisering af håndskrevne medicinske journaler  
- Brugerdefinerede medicinske sprogsmodeller implementeret via Windows ML  
- Lokal vektorlagring til medicinsk videnshentning  

**Implementeringsmetode:**  
- Sikr fuld offline-drift for patientprivatliv  
- Implementer validering og forslag til medicinsk terminologi  
- Tilføj revisionslogning for overholdelse af lovgivning  
- Design integration med eksisterende elektroniske patientjournal-systemer  

## Ydelsesoptimeringsstrategier

### Hardwarebevidst udvikling

**NPU-optimering**  
- Design applikationer til at udnytte NPU-funktioner på Copilot+ PC'er  
- Implementer yndefuld fallback til GPU/CPU på enheder uden NPU  
- Optimer modelformater til NPU-specifik acceleration  
- Overvåg NPU-udnyttelse og termiske egenskaber  

**Hukommelsesstyring**  
- Implementer effektive strategier for modelladning og caching  
- Brug hukommelseskortlægning til store modeller for at reducere opstartstid  
- Design hukommelsesbevidste applikationer til enheder med begrænsede ressourcer  
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
- Brug async/await-mønstre til ikke-blokerende AI-operationer  
- Planlæg optimering af trådpool til forskellige hardwarekonfigurationer  

**Caching-strategier**  
- Implementer intelligent caching til ofte brugte AI-operationer  
- Design strategier for cache-invalidering ved modelopdateringer  
- Brug vedvarende caching til dyre forbehandlingsoperationer  
- Implementer distribueret caching til scenarier med flere brugere  

## Sikkerheds- og privatlivsbedste praksis

### Databeskyttelse

**Lokal behandling**  
- Sikr, at følsomme data aldrig forlader den lokale enhed  
- Implementer sikker opbevaring af AI-modeller og midlertidige data  
- Brug Windows sikkerhedsfunktioner til applikationssandboxing  
- Anvend kryptering til lagrede modeller og mellemliggende behandlingsresultater  

**Modelsikkerhed**  
- Valider modelintegritet før indlæsning og udførelse  
- Implementer sikre mekanismer til modelopdatering  
- Brug signerede modeller for at forhindre manipulation  
- Anvend adgangskontrol til modelfiler og konfiguration  

### Overholdelsesovervejelser

**Regulatorisk tilpasning**  
-
- Udnyt Foundry Local CLI til modeltest og validering
- Brug Windows AI API-testværktøjer til integrationsverifikation
- Implementér brugerdefineret logning til overvågning af AI-operationer
- Opret automatiserede tests for pålidelighed af AI-funktionalitet

## Fremtidssikring af dine applikationer

### Fremspirende teknologier

**Næste generations hardware**
- Design applikationer til at udnytte fremtidige NPU-muligheder
- Planlæg for større modelstørrelser og øget kompleksitet
- Implementér adaptive arkitekturer til udviklende hardware
- Overvej kvanteklare algoritmer for fremtidig kompatibilitet

**Avancerede AI-funktioner**
- Forbered dig på multimodal AI-integration på tværs af flere datatyper
- Planlæg for realtids samarbejdende AI mellem flere enheder
- Design til federeret læringskapacitet
- Overvej edge-cloud hybrid intelligensarkitekturer

### Kontinuerlig læring og tilpasning

**Modelopdateringer**
- Implementér problemfri mekanismer til modelopdateringer
- Design applikationer til at tilpasse sig forbedrede modelkapaciteter
- Planlæg for bagudkompatibilitet med eksisterende modeller
- Implementér A/B-test for evaluering af modelpræstation

**Featureudvikling**
- Design modulære arkitekturer, der kan rumme nye AI-funktioner
- Planlæg for integration af fremspirende Windows AI APIs
- Implementér feature flags for gradvis udrulning af funktioner
- Design brugergrænseflader, der tilpasser sig forbedrede AI-funktioner

## Konklusion

Windows Edge AI-udvikling repræsenterer sammenfletningen af kraftfulde AI-funktioner med den robuste, sikre og skalerbare Windows-platform. Ved at mestre Windows AI Foundry-økosystemet kan udviklere skabe intelligente applikationer, der leverer enestående brugeroplevelser, samtidig med at de opretholder de højeste standarder for privatliv, sikkerhed og ydeevne.

Kombinationen af Windows AI APIs, Foundry Local og Windows ML giver et enestående fundament for at bygge næste generation af intelligente Windows-applikationer. Efterhånden som AI fortsætter med at udvikle sig, sikrer Windows-platformen, at dine applikationer vil skalere med fremspirende teknologier, samtidig med at de opretholder kompatibilitet og ydeevne på tværs af det mangfoldige Windows-hardwareøkosystem.

Uanset om du bygger forbrugerapplikationer, virksomhedsløsninger eller specialiserede industriværktøjer, giver Windows Edge AI-udvikling dig mulighed for at skabe intelligente, responsive og dybt integrerede oplevelser, der udnytter det fulde potentiale af moderne Windows-enheder.

## Yderligere ressourcer

For en trin-for-trin Windows-gennemgang af Foundry Local (installation, CLI, dynamisk endpoint, SDK-brug), se repo-guiden: [foundrylocal.md](./foundrylocal.md).

### Dokumentation og læring
- [Windows AI Foundry Dokumentation](https://learn.microsoft.com/windows/ai/)
- [Windows AI APIs Reference](https://learn.microsoft.com/windows/ai/apis/)
- [Foundry Local Kom godt i gang](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML Oversigt](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)

### Udviklingsværktøjer
- [AI Toolkit til Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Eksempler](https://learn.microsoft.com/windows/ai/samples/)

### Fællesskab og support
- [Windows Udviklerfællesskab](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Træning](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Denne guide er designet til at udvikle sig i takt med det hurtigt fremskridende Windows AI-økosystem. Regelmæssige opdateringer sikrer tilpasning til de nyeste platformfunktioner og bedste udviklingspraksis.*

---

