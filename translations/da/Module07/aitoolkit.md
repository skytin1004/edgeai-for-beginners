<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T13:11:04+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "da"
}
-->
# AI Toolkit til Visual Studio Code - Guide til Edge AI-udvikling

## Introduktion

Velkommen til den omfattende guide til brug af AI Toolkit til Visual Studio Code i Edge AI-udvikling. Efterhånden som kunstig intelligens bevæger sig fra centraliseret cloud computing til distribuerede edge-enheder, har udviklere brug for kraftfulde, integrerede værktøjer, der kan håndtere de unikke udfordringer ved edge-implementering - fra begrænsede ressourcer til krav om offline drift.

AI Toolkit til Visual Studio Code bygger bro mellem disse behov ved at tilbyde et komplet udviklingsmiljø, der er specifikt designet til at bygge, teste og optimere AI-applikationer, der kører effektivt på edge-enheder. Uanset om du udvikler til IoT-sensorer, mobile enheder, indlejrede systemer eller edge-servere, forenkler dette værktøj hele din udviklingsproces inden for det velkendte VS Code-miljø.

Denne guide vil føre dig gennem de essentielle begreber, værktøjer og bedste praksis for at udnytte AI Toolkit i dine Edge AI-projekter, fra den indledende modeludvælgelse til implementering i produktion.

## Oversigt

AI Toolkit til Visual Studio Code er en kraftfuld udvidelse, der forenkler udviklingen af agenter og skabelsen af AI-applikationer. Værktøjet tilbyder omfattende funktioner til at udforske, evaluere og implementere AI-modeller fra en bred vifte af udbydere—herunder Anthropic, OpenAI, GitHub, Google—samt understøttelse af lokal modelkørsel ved brug af ONNX og Ollama.

Det, der adskiller AI Toolkit, er dets omfattende tilgang til hele AI-udviklingslivscyklussen. I modsætning til traditionelle AI-udviklingsværktøjer, der fokuserer på enkelte aspekter, tilbyder AI Toolkit et integreret miljø, der dækker modelopdagelse, eksperimentering, agentudvikling, evaluering og implementering—alt sammen inden for det velkendte VS Code-miljø.

Platformen er specifikt designet til hurtig prototyping og implementering i produktion med funktioner som promptgenerering, hurtige startskabeloner, problemfri MCP (Model Context Protocol)-værktøjsintegrationer og omfattende evalueringsmuligheder. For Edge AI-udvikling betyder det, at du effektivt kan udvikle, teste og optimere AI-applikationer til edge-implementeringsscenarier, mens du opretholder hele udviklingsprocessen inden for VS Code.

## Læringsmål

Ved afslutningen af denne guide vil du være i stand til:

### Kernekompetencer
- **Installere og konfigurere** AI Toolkit til Visual Studio Code til Edge AI-udviklingsarbejdsgange
- **Navigere og anvende** AI Toolkit-grænsefladen, herunder Model Catalog, Playground og Agent Builder
- **Udvælge og evaluere** AI-modeller, der er egnede til edge-implementering baseret på ydeevne og ressourcebegrænsninger
- **Konvertere og optimere** modeller ved brug af ONNX-format og kvantiseringsteknikker til edge-enheder

### Edge AI-udviklingsfærdigheder
- **Designe og implementere** Edge AI-applikationer ved brug af det integrerede udviklingsmiljø
- **Udføre modeltest** under edge-lignende forhold ved brug af lokal inferens og ressourceovervågning
- **Oprette og tilpasse** AI-agenter optimeret til edge-implementeringsscenarier
- **Evaluere modelpræstation** ved brug af metrics, der er relevante for edge computing (latens, hukommelsesforbrug, nøjagtighed)

### Optimering og implementering
- **Anvende kvantisering og beskæring** teknikker til at reducere modelstørrelse, mens acceptabel ydeevne opretholdes
- **Optimere modeller** til specifikke edge-hardwareplatforme, herunder CPU-, GPU- og NPU-acceleration
- **Implementere bedste praksis** for Edge AI-udvikling, herunder ressourcehåndtering og fallback-strategier
- **Forberede modeller og applikationer** til implementering i produktion på edge-enheder

### Avancerede Edge AI-koncepter
- **Integrere med edge AI-rammer** herunder ONNX Runtime, Windows ML og TensorFlow Lite
- **Implementere multi-model arkitekturer** og federerede læringsscenarier til edge-miljøer
- **Fejlsøge almindelige Edge AI-problemer** herunder hukommelsesbegrænsninger, inferenshastighed og hardwarekompatibilitet
- **Designe overvågnings- og logningsstrategier** til Edge AI-applikationer i produktion

### Praktisk anvendelse
- **Bygge end-to-end Edge AI-løsninger** fra modeludvælgelse til implementering
- **Demonstrere færdigheder** i edge-specifikke udviklingsarbejdsgange og optimeringsteknikker
- **Anvende lærte koncepter** til virkelige Edge AI-brugsscenarier, herunder IoT, mobile og indlejrede applikationer
- **Evaluere og sammenligne** forskellige Edge AI-implementeringsstrategier og deres kompromiser

## Nøglefunktioner til Edge AI-udvikling

### 1. Modelkatalog og opdagelse
- **Understøttelse af flere udbydere**: Gennemse og få adgang til AI-modeller fra Anthropic, OpenAI, GitHub, Google og andre udbydere
- **Lokal modelintegration**: Forenklet opdagelse af ONNX- og Ollama-modeller til edge-implementering
- **GitHub-modeller**: Direkte integration med GitHubs modelhosting for problemfri adgang
- **Model sammenligning**: Sammenlign modeller side om side for at finde den optimale balance for edge-enhedens begrænsninger

### 2. Interaktiv Playground
- **Interaktivt testmiljø**: Hurtig eksperimentering med modelkapaciteter i et kontrolleret miljø
- **Multimodal understøttelse**: Test med billeder, tekst og andre input, der er typiske i edge-scenarier
- **Realtids eksperimentering**: Øjeblikkelig feedback på modelrespons og ydeevne
- **Parameteroptimering**: Finjuster modelparametre til edge-implementeringskrav

### 3. Prompt (Agent) Builder
- **Naturlig sprog generation**: Generer startprompter ved brug af naturlige sprog beskrivelser
- **Iterativ forbedring**: Forbedr prompter baseret på modelrespons og ydeevne
- **Opgaveopdeling**: Opdel komplekse opgaver med promptkæder og strukturerede output
- **Variabel understøttelse**: Brug variabler i prompter for dynamisk agentadfærd
- **Produktionskodegenerering**: Generer produktionsklar kode til hurtig app-udvikling

### 4. Massekørsel og evaluering
- **Multi-model testning**: Udfør flere prompter på tværs af udvalgte modeller samtidigt
- **Effektiv testning i stor skala**: Test forskellige input og konfigurationer effektivt
- **Brugerdefinerede testcases**: Kør agenter med testcases for at validere funktionalitet
- **Præstationssammenligning**: Sammenlign resultater på tværs af forskellige modeller og konfigurationer

### 5. Model evaluering med datasæt
- **Standard metrics**: Test AI-modeller ved brug af indbyggede evaluatorer (F1-score, relevans, lighed, sammenhæng)
- **Brugerdefinerede evaluatorer**: Opret dine egne evalueringsmetrics til specifikke brugsscenarier
- **Datasæt integration**: Test modeller mod omfattende datasæt
- **Præstationsmåling**: Kvantificer modelpræstation for edge-implementeringsbeslutninger

### 6. Finjusteringsmuligheder
- **Modeltilpasning**: Tilpas modeller til specifikke brugsscenarier og domæner
- **Specialiseret tilpasning**: Tilpas modeller til specialiserede domæner og krav
- **Edge-optimering**: Finjuster modeller specifikt til edge-implementeringsbegrænsninger
- **Domænespecifik træning**: Opret modeller skræddersyet til specifikke edge-brugsscenarier

### 7. MCP-værktøjsintegration
- **Ekstern værktøjsforbindelse**: Forbind agenter til eksterne værktøjer via Model Context Protocol-servere
- **Reelle handlinger**: Gør det muligt for agenter at forespørge databaser, få adgang til API'er eller udføre brugerdefineret logik
- **Eksisterende MCP-servere**: Brug værktøjer fra kommando (stdio) eller HTTP (server-sent event) protokoller
- **Brugerdefineret MCP-udvikling**: Byg og opret nye MCP-servere med test i Agent Builder

### 8. Agentudvikling og testning
- **Understøttelse af funktionskald**: Gør det muligt for agenter at kalde eksterne funktioner dynamisk
- **Realtids integrationstest**: Test integrationer med realtidskørsler og værktøjsbrug
- **Agent versionering**: Versionskontrol for agenter med sammenligningsmuligheder for evalueringsresultater
- **Fejlfinding og sporing**: Lokal sporing og fejlfinding til agentudvikling

## Edge AI-udviklingsarbejdsgang

### Fase 1: Modelopdagelse og udvælgelse
1. **Udforsk Model Catalog**: Brug modelkataloget til at finde modeller, der er egnede til edge-implementering
2. **Sammenlign ydeevne**: Evaluer modeller baseret på størrelse, nøjagtighed og inferenshastighed
3. **Test lokalt**: Brug Ollama eller ONNX-modeller til lokal test før edge-implementering
4. **Vurder ressourcekrav**: Bestem hukommelses- og beregningsbehov for mål-edge-enheder

### Fase 2: Modeloptimering
1. **Konverter til ONNX**: Konverter udvalgte modeller til ONNX-format for edge-kompatibilitet
2. **Anvend kvantisering**: Reducer modelstørrelse gennem INT8- eller INT4-kvantisering
3. **Hardwareoptimering**: Optimer til mål-edge-hardware (ARM, x86, specialiserede acceleratorer)
4. **Præstationsvalidering**: Valider, at optimerede modeller opretholder acceptabel nøjagtighed

### Fase 3: Applikationsudvikling
1. **Agentdesign**: Brug Agent Builder til at oprette edge-optimerede AI-agenter
2. **Prompt Engineering**: Udvikl prompter, der fungerer effektivt med mindre edge-modeller
3. **Integrationstest**: Test agenter under simulerede edge-forhold
4. **Kodegenerering**: Generer produktionskode optimeret til edge-implementering

### Fase 4: Evaluering og testning
1. **Batch-evaluering**: Test flere konfigurationer for at finde optimale edge-indstillinger
2. **Præstationsprofilering**: Analyser inferenshastighed, hukommelsesforbrug og nøjagtighed
3. **Edge-simulering**: Test under forhold, der ligner mål-edge-implementeringsmiljøet
4. **Stress-testning**: Evaluer ydeevne under forskellige belastningsforhold

### Fase 5: Implementeringsforberedelse
1. **Endelig optimering**: Anvend endelige optimeringer baseret på testresultater
2. **Implementeringspakning**: Pak modeller og kode til edge-implementering
3. **Dokumentation**: Dokumenter implementeringskrav og konfiguration
4. **Overvågningsopsætning**: Forbered overvågning og logning til edge-implementering

## Målgruppe for Edge AI-udvikling

### Edge AI-udviklere
- Applikationsudviklere, der bygger AI-drevne edge-enheder og IoT-løsninger
- Udviklere af indlejrede systemer, der integrerer AI-funktioner i ressourcebegrænsede enheder
- Mobiludviklere, der skaber AI-applikationer på enheder som smartphones og tablets

### Edge AI-ingeniører
- AI-ingeniører, der optimerer modeller til edge-implementering og administrerer inferens-pipelines
- DevOps-ingeniører, der implementerer og administrerer AI-modeller på tværs af distribueret edge-infrastruktur
- Præstationsingeniører, der optimerer AI-arbejdsgange til edge-hardwarebegrænsninger

### Forskere og undervisere
- AI-forskere, der udvikler effektive modeller og algoritmer til edge computing
- Undervisere, der underviser i Edge AI-koncepter og demonstrerer optimeringsteknikker
- Studerende, der lærer om udfordringer og løsninger i Edge AI-implementering

## Edge AI-brugsscenarier

### Smarte IoT-enheder
- **Realtids billedgenkendelse**: Implementer computer vision-modeller på IoT-kameraer og sensorer
- **Stemmekontrol**: Implementer talegenkendelse og naturlig sprogbehandling på smarte højttalere
- **Forudsigende vedligeholdelse**: Kør anomali-detekteringsmodeller på industrielle edge-enheder
- **Miljøovervågning**: Implementer sensordataanalysemodeller til miljøapplikationer

### Mobile og indlejrede applikationer
- **Oversættelse på enheden**: Implementer sprogoversættelsesmodeller, der fungerer offline
- **Augmented Reality**: Implementer realtids objektgenkendelse og sporing til AR-applikationer
- **Sundhedsovervågning**: Kør sundhedsanalysemodeller på wearables og medicinsk udstyr
- **Autonome systemer**: Implementer beslutningstagende modeller til droner, robotter og køretøjer

### Edge computing-infrastruktur
- **Edge-datacentre**: Implementer AI-modeller i edge-datacentre til applikationer med lav latens
- **CDN-integration**: Integrer AI-behandlingsfunktioner i content delivery-netværk
- **5G Edge**: Udnyt 5G edge computing til AI-drevne applikationer
- **Fog computing**: Implementer AI-behandling i fog computing-miljøer

## Installation og opsætning

### Installation af udvidelse
Installer AI Toolkit-udvidelsen direkte fra Visual Studio Code Marketplace:

**Udvidelses-ID**: `ms-windows-ai-studio.windows-ai-studio`

**Installationsmetoder**:
1. **VS Code Marketplace**: Søg efter "AI Toolkit" i Extensions-visningen
2. **Kommandolinje**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Direkte installation**: Download fra [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Forudsætninger for Edge AI-udvikling
- **Visual Studio Code**: Seneste version anbefales
- **Python-miljø**: Python 3.8+ med nødvendige AI-biblioteker
- **ONNX Runtime** (valgfrit): Til ONNX-modelinferens
- **Ollama** (valgfrit): Til lokal modelservering
- **Hardwareaccelerationsværktøjer**: CUDA, OpenVINO eller platform-specifikke acceleratorer

### Indledende konfiguration
1. **Aktivering af udvidelse**: Åbn VS Code og verificer, at AI Toolkit vises i Activity Bar
2. **Opsætning af modeludbyder**: Konfigurer adgang til GitHub, OpenAI, Anthropic eller andre modeludbydere
3. **Lokalt miljø**: Opsæt Python-miljø og installer nødvendige pakker
4. **Hardwareacceleration**: Konfigurer GPU/NPU-acceleration, hvis tilgængelig
5. **MCP-integration**: Opsæt Model Context Protocol-servere, hvis nødvendigt

### Førstegangsopsætningscheckliste
- [ ] AI Toolkit-udvidelse installeret og aktiveret
- [ ] Modelkatalog tilgængeligt og modeller opdagelige
- [ ] Playground funktionel til modeltestning
- [ ] Agent Builder tilgængelig til promptudvikling
- [ ] Lokalt udviklingsmiljø konfigureret
- [ ] Hardwareacceleration (hvis tilgængelig) korrekt konfigureret

## Kom godt i gang med AI Toolkit

### Hurtig startguide

Vi anbefaler at starte med modeller hostet af GitHub for den mest problemfri oplevelse:

1. **Installation**: Følg [installationsguiden](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) for at opsætte AI Toolkit på din enhed
2. **Modelopdagelse**: Fra udvidelsens trævisning, vælg **CATALOG > Models** for at udforske tilgængelige modeller
3. **GitHub-modeller**: Start med modeller hostet af GitHub for optimal integration
4. **Playground-testning**: Fra enhver modelkort, vælg **Try in Playground** for at begynde at eksperimentere med modelkapaciteter

### Trin-for-trin Edge AI-udvikling

#### Trin 1: Modelopdagelse og udvælgelse
1. Åbn AI Toolkit-visningen i VS Code Activity Bar
2. Gennemse Model
2. Generer startprompter ved hjælp af naturlige sprog beskrivelser  
3. Iterér og forfin prompter baseret på modellens svar  
4. Integrer MCP-værktøjer for at forbedre agentens funktioner  

#### Trin 3: Test og Evaluering  
1. Brug **Bulk Run** til at teste flere prompter på tværs af udvalgte modeller  
2. Kør agenter med testcases for at validere funktionalitet  
3. Evaluer nøjagtighed og ydeevne ved hjælp af indbyggede eller brugerdefinerede metrikker  
4. Sammenlign forskellige modeller og konfigurationer  

#### Trin 4: Finjustering og Optimering  
1. Tilpas modeller til specifikke edge-brugsscenarier  
2. Anvend domænespecifik finjustering  
3. Optimer til begrænsninger ved edge-udrulning  
4. Versionsstyr og sammenlign forskellige agentkonfigurationer  

#### Trin 5: Forberedelse til Udrulning  
1. Generer produktionsklar kode ved hjælp af Agent Builder  
2. Opsæt MCP-serverforbindelser til produktionsbrug  
3. Forbered udrulningspakker til edge-enheder  
4. Konfigurer overvågnings- og evalueringsmetrikker  

## Bedste Praksis for Edge AI Udvikling  

### Modelvalg  
- **Størrelsesbegrænsninger**: Vælg modeller, der passer inden for hukommelsesbegrænsningerne på målenheder  
- **Inferenshastighed**: Prioritér modeller med hurtige inferenstider til realtidsapplikationer  
- **Nøjagtighedsafvejninger**: Balancér modelnøjagtighed med ressourcebegrænsninger  
- **Formatkompatibilitet**: Foretræk ONNX eller hardwareoptimerede formater til edge-udrulning  

### Optimeringsteknikker  
- **Kvantisering**: Brug INT8 eller INT4 kvantisering for at reducere modelstørrelse og forbedre hastighed  
- **Pruning**: Fjern unødvendige modelparametre for at reducere beregningskrav  
- **Knowledge Distillation**: Skab mindre modeller, der bevarer ydeevnen fra større modeller  
- **Hardwareacceleration**: Udnyt NPUs, GPUs eller specialiserede acceleratorer, når det er muligt  

### Udviklingsworkflow  
- **Iterativ Testning**: Test ofte under edge-lignende forhold under udvikling  
- **Ydelsesovervågning**: Overvåg løbende ressourceforbrug og inferenshastighed  
- **Versionsstyring**: Spor modelversioner og optimeringsindstillinger  
- **Dokumentation**: Dokumentér alle optimeringsbeslutninger og afvejninger  

### Overvejelser ved Udrulning  
- **Ressourceovervågning**: Overvåg hukommelse, CPU og strømforbrug i produktion  
- **Fallback-strategier**: Implementér fallback-mekanismer ved modelfejl  
- **Opdateringsmekanismer**: Planlæg for modelopdateringer og versionsstyring  
- **Sikkerhed**: Implementér passende sikkerhedsforanstaltninger for edge AI-applikationer  

## Integration med Edge AI Frameworks  

### ONNX Runtime  
- **Platformuafhængig Udrulning**: Udrul ONNX-modeller på tværs af forskellige edge-platforme  
- **Hardwareoptimering**: Udnyt ONNX Runtimes hardware-specifikke optimeringer  
- **Mobilsupport**: Brug ONNX Runtime Mobile til smartphones og tablets  
- **IoT-integration**: Udrul på IoT-enheder ved hjælp af ONNX Runtimes letvægtsdistributioner  

### Windows ML  
- **Windows-enheder**: Optimer til Windows-baserede edge-enheder og pc'er  
- **NPU-acceleration**: Udnyt Neural Processing Units på Windows-enheder  
- **DirectML**: Brug DirectML til GPU-acceleration på Windows-platforme  
- **UWP-integration**: Integrer med Universal Windows Platform-applikationer  

### TensorFlow Lite  
- **Mobiloptimering**: Udrul TensorFlow Lite-modeller på mobile og indlejrede enheder  
- **Hardwaredelegering**: Brug specialiserede hardwaredelegeringer til acceleration  
- **Mikrocontrollere**: Udrul på mikrocontrollere ved hjælp af TensorFlow Lite Micro  
- **Platformuafhængig Support**: Udrul på tværs af Android, iOS og indlejrede Linux-systemer  

### Azure IoT Edge  
- **Cloud-Edge Hybrid**: Kombinér cloud-træning med edge-inferens  
- **Moduludrulning**: Udrul AI-modeller som IoT Edge-moduler  
- **Enhedsstyring**: Administrer edge-enheder og modelopdateringer eksternt  
- **Telemetri**: Indsaml ydelsesdata og modelmetrikker fra edge-udrulninger  

## Avancerede Edge AI Scenarier  

### Multi-Model Udrulning  
- **Modelensembler**: Udrul flere modeller for forbedret nøjagtighed eller redundans  
- **A/B Testning**: Test forskellige modeller samtidig på edge-enheder  
- **Dynamisk Valg**: Vælg modeller baseret på aktuelle enhedsforhold  
- **Ressourcedeling**: Optimer ressourceforbrug på tværs af flere udrullede modeller  

### Federated Learning  
- **Distribueret Træning**: Træn modeller på tværs af flere edge-enheder  
- **Privatlivsbeskyttelse**: Behold træningsdata lokalt, mens modelforbedringer deles  
- **Samarbejdende Læring**: Gør det muligt for enheder at lære af kollektive erfaringer  
- **Edge-Cloud Koordination**: Koordiner læring mellem edge-enheder og cloud-infrastruktur  

### Realtidsbehandling  
- **Streambehandling**: Behandl kontinuerlige datastrømme på edge-enheder  
- **Lav-latens Inferens**: Optimer for minimal inferenslatens  
- **Batchbehandling**: Effektivt behandle batches af data på edge-enheder  
- **Adaptiv Behandling**: Juster behandling baseret på aktuelle enhedskapaciteter  

## Fejlfinding i Edge AI Udvikling  

### Almindelige Problemer  
- **Hukommelsesbegrænsninger**: Model for stor til målenhedens hukommelse  
- **Inferenshastighed**: Modelinference for langsom til realtidskrav  
- **Nøjagtighedsforringelse**: Optimering reducerer modelnøjagtighed uacceptabelt  
- **Hardwarekompatibilitet**: Model ikke kompatibel med målhardware  

### Fejlfindingsstrategier  
- **Ydelsesprofilering**: Brug AI Toolkits sporingsfunktioner til at identificere flaskehalse  
- **Ressourceovervågning**: Overvåg hukommelse og CPU-forbrug under udvikling  
- **Inkrementel Testning**: Test optimeringer trinvis for at isolere problemer  
- **Hardwaresimulering**: Brug udviklingsværktøjer til at simulere målhardware  

### Optimeringsløsninger  
- **Yderligere Kvantisering**: Anvend mere aggressive kvantiseringsteknikker  
- **Modelarkitektur**: Overvej forskellige modelarkitekturer optimeret til edge  
- **Forbehandlingsoptimering**: Optimer databehandling til edge-begrænsninger  
- **Inferensoptimering**: Brug hardware-specifikke inferensoptimeringer  

## Ressourcer og Næste Skridt  

### Officiel Dokumentation  
- [AI Toolkit Udviklerdokumentation](https://aka.ms/AIToolkit/doc)  
- [Installations- og Opsætningsguide](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps Dokumentation](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) Dokumentation](https://modelcontextprotocol.io/)  

### Fællesskab og Support  
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub Issues og Funktionsanmodninger](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord Community](https://aka.ms/azureaifoundry/discord)  
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Tekniske Ressourcer  
- [ONNX Runtime Dokumentation](https://onnxruntime.ai/)  
- [Ollama Dokumentation](https://ollama.ai/)  
- [Windows ML Dokumentation](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Læringsforløb  
- [Edge AI Grundkursus](../Module01/README.md)  
- [Guide til Små Sproglige Modeller](../Module02/README.md)  
- [Strategier for Edge-udrulning](../Module03/README.md)  
- [Windows Edge AI Udvikling](./windowdeveloper.md)  

### Yderligere Ressourcer  
- **Repository Statistikker**: 1.8k+ stjerner, 150+ forks, 18+ bidragydere  
- **Licens**: MIT-licens  
- **Sikkerhed**: Microsofts sikkerhedspolitikker gælder  
- **Telemetri**: Respekterer VS Codes telemetriindstillinger  

## Konklusion  

AI Toolkit til Visual Studio Code repræsenterer en omfattende platform til moderne AI-udvikling, der tilbyder strømlinede agentudviklingsmuligheder, som er særligt værdifulde for Edge AI-applikationer. Med sin omfattende modelkatalog, der understøtter udbydere som Anthropic, OpenAI, GitHub og Google, kombineret med lokal eksekvering via ONNX og Ollama, tilbyder værktøjet den fleksibilitet, der er nødvendig for forskellige edge-udrulningsscenarier.  

Værktøjets styrke ligger i dets integrerede tilgang—fra modelopdagelse og eksperimentering i Playground til sofistikeret agentudvikling med Prompt Builder, omfattende evalueringsmuligheder og problemfri MCP-værktøjsintegration. For Edge AI-udviklere betyder dette hurtig prototyping og test af AI-agenter før edge-udrulning, med mulighed for hurtigt at iterere og optimere til ressourcebegrænsede miljøer.  

Nøglefordele for Edge AI-udvikling inkluderer:  
- **Hurtig Eksperimentering**: Test modeller og agenter hurtigt før edge-udrulning  
- **Fleksibilitet med Flere Udbydere**: Adgang til modeller fra forskellige kilder for at finde optimale edge-løsninger  
- **Lokal Udvikling**: Test med ONNX og Ollama for offline og privatlivsbevarende udvikling  
- **Produktionsklarhed**: Generer produktionsklar kode og integrer med eksterne værktøjer via MCP  
- **Omfattende Evaluering**: Brug indbyggede og brugerdefinerede metrikker til at validere edge AI-ydeevne  

Efterhånden som AI fortsætter med at bevæge sig mod edge-udrulningsscenarier, giver AI Toolkit til VS Code det udviklingsmiljø og workflow, der er nødvendigt for at bygge, teste og optimere intelligente applikationer til ressourcebegrænsede miljøer. Uanset om du udvikler IoT-løsninger, mobile AI-applikationer eller indlejrede intelligenssystemer, understøtter værktøjets omfattende funktionssæt og integrerede workflow hele edge AI-udviklingslivscyklussen.  

Med løbende udvikling og et aktivt fællesskab (1.8k+ GitHub-stjerner) forbliver AI Toolkit i frontlinjen af AI-udviklingsværktøjer og udvikler sig konstant for at imødekomme behovene hos moderne AI-udviklere, der bygger til edge-udrulningsscenarier.  

[Next Foundry Local](./foundrylocal.md)  

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.