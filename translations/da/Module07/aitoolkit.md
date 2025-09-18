<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-18T10:52:44+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "da"
}
-->
# AI Toolkit til Visual Studio Code - Edge AI Udviklingsguide

## Introduktion

Velkommen til den omfattende guide til brug af AI Toolkit for Visual Studio Code i Edge AI-udvikling. Efterhånden som kunstig intelligens bevæger sig fra centraliseret cloud computing til distribuerede edge-enheder, har udviklere brug for kraftfulde, integrerede værktøjer, der kan håndtere de unikke udfordringer ved edge-implementering - fra ressourcebegrænsninger til krav om offline drift.

AI Toolkit for Visual Studio Code bygger bro over denne kløft ved at tilbyde et komplet udviklingsmiljø, der er specifikt designet til at bygge, teste og optimere AI-applikationer, der kører effektivt på edge-enheder. Uanset om du udvikler til IoT-sensorer, mobile enheder, indlejrede systemer eller edge-servere, strømliner dette værktøj hele din udviklingsarbejdsgang inden for det velkendte VS Code-miljø.

Denne guide vil føre dig gennem de essentielle begreber, værktøjer og bedste praksis for at udnytte AI Toolkit i dine Edge AI-projekter, fra den indledende modeludvælgelse til implementering i produktion.

## Oversigt

AI Toolkit tilbyder et integreret udviklingsmiljø til hele livscyklussen for Edge AI-applikationer inden for VS Code. Det giver problemfri integration med populære AI-modeller fra leverandører som OpenAI, Anthropic, Google og GitHub, samtidig med at det understøtter lokal modelimplementering via ONNX og Ollama - afgørende funktioner for Edge AI-applikationer, der kræver on-device inferens.

Det, der adskiller AI Toolkit for Edge AI-udvikling, er dets fokus på hele edge-implementeringspipeline. I modsætning til traditionelle AI-udviklingsværktøjer, der primært sigter mod cloud-implementering, inkluderer AI Toolkit specialiserede funktioner til modeloptimering, test under ressourcebegrænsninger og edge-specifik præstationsvurdering. Værktøjet forstår, at Edge AI-udvikling kræver andre overvejelser - mindre modelstørrelser, hurtigere inferenstider, offline kapacitet og hardware-specifikke optimeringer.

Platformen understøtter flere implementeringsscenarier, fra simpel on-device inferens til komplekse multi-model edge-arkitekturer. Den tilbyder værktøjer til modelkonvertering, kvantisering og optimering, som er essentielle for succesfuld edge-implementering, samtidig med at den opretholder den udviklerproduktivitet, som VS Code er kendt for.

## Læringsmål

Ved afslutningen af denne guide vil du være i stand til:

### Kernekompetencer
- **Installere og konfigurere** AI Toolkit for Visual Studio Code til Edge AI-udviklingsarbejdsgange
- **Navigere og anvende** AI Toolkit-grænsefladen, herunder Model Catalog, Playground og Agent Builder
- **Udvælge og evaluere** AI-modeller, der er egnede til edge-implementering baseret på præstation og ressourcebegrænsninger
- **Konvertere og optimere** modeller ved hjælp af ONNX-format og kvantiseringsteknikker til edge-enheder

### Edge AI Udviklingsfærdigheder
- **Designe og implementere** Edge AI-applikationer ved hjælp af det integrerede udviklingsmiljø
- **Udføre modeltest** under edge-lignende forhold ved hjælp af lokal inferens og ressourceovervågning
- **Oprette og tilpasse** AI-agenter optimeret til edge-implementeringsscenarier
- **Evaluere modelpræstation** ved hjælp af metrics, der er relevante for edge computing (latens, hukommelsesforbrug, nøjagtighed)

### Optimering og Implementering
- **Anvende kvantisering og beskæring** teknikker til at reducere modelstørrelse, mens acceptabel præstation opretholdes
- **Optimere modeller** til specifikke edge-hardwareplatforme, herunder CPU, GPU og NPU-acceleration
- **Implementere bedste praksis** for Edge AI-udvikling, herunder ressourcehåndtering og fallback-strategier
- **Forberede modeller og applikationer** til produktionsimplementering på edge-enheder

### Avancerede Edge AI Begreber
- **Integrere med edge AI-rammer** som ONNX Runtime, Windows ML og TensorFlow Lite
- **Implementere multi-model arkitekturer** og federerede læringsscenarier for edge-miljøer
- **Fejlsøge almindelige edge AI-problemer** som hukommelsesbegrænsninger, inferenshastighed og hardwarekompatibilitet
- **Designe overvågnings- og logningsstrategier** for Edge AI-applikationer i produktion

### Praktisk Anvendelse
- **Bygge end-to-end Edge AI-løsninger** fra modeludvælgelse til implementering
- **Demonstrere færdigheder** i edge-specifikke udviklingsarbejdsgange og optimeringsteknikker
- **Anvende lærte begreber** til virkelige Edge AI-brugsscenarier, herunder IoT, mobile og indlejrede applikationer
- **Evaluere og sammenligne** forskellige edge AI-implementeringsstrategier og deres kompromiser

## Nøglefunktioner til Edge AI Udvikling

### 1. Modelkatalog og Opdagelse
- **Lokal Modelunderstøttelse**: Opdag og få adgang til AI-modeller, der er specifikt optimeret til edge-implementering
- **ONNX Integration**: Få adgang til modeller i ONNX-format for effektiv edge-inferens
- **Ollama Understøttelse**: Udnyt lokalt kørende modeller via Ollama for privatliv og offline drift
- **Model Sammenligning**: Sammenlign modeller side om side for at finde den optimale balance mellem præstation og ressourceforbrug for edge-enheder

### 2. Interaktiv Playground
- **Lokal Testmiljø**: Test modeller lokalt før edge-implementering
- **Multi-modal Eksperimentering**: Test med billeder, tekst og andre input, der er typiske i edge-scenarier
- **Parameterjustering**: Eksperimenter med forskellige modelparametre for at optimere til edge-begrænsninger
- **Realtids Præstationsovervågning**: Observer inferenshastighed og ressourceforbrug under udvikling

### 3. Agent Builder til Edge Applikationer
- **Prompt Engineering**: Opret optimerede prompts, der fungerer effektivt med mindre edge-modeller
- **MCP Værktøjsintegration**: Integrer Model Context Protocol-værktøjer for forbedrede edge-agentkapaciteter
- **Kodegenerering**: Generer produktionsklar kode optimeret til edge-implementeringsscenarier
- **Strukturerede Outputs**: Design agenter, der leverer konsistente, strukturerede svar, der er egnede til edge-applikationer

### 4. Model Evaluering og Test
- **Præstationsmetrics**: Evaluer modeller ved hjælp af metrics, der er relevante for edge-implementering (latens, hukommelsesforbrug, nøjagtighed)
- **Batch Testning**: Test flere modelkonfigurationer samtidigt for at finde optimale edge-indstillinger
- **Tilpasset Evaluering**: Opret tilpassede evalueringskriterier specifikt til Edge AI-brugsscenarier
- **Ressourceprofilering**: Analyser hukommelses- og beregningskrav til edge-implementeringsplanlægning

### 5. Modelkonvertering og Optimering
- **ONNX Konvertering**: Konverter modeller fra forskellige formater til ONNX for edge-kompatibilitet
- **Kvantisering**: Reducer modelstørrelse og forbedr inferenshastighed gennem kvantiseringsteknikker
- **Hardwareoptimering**: Optimer modeller til specifik edge-hardware (CPU, GPU, NPU)
- **Formattransformation**: Transformér modeller fra Hugging Face og andre kilder til edge-implementering

### 6. Finjustering til Edge-scenarier
- **Domæne Tilpasning**: Tilpas modeller til specifikke edge-brugsscenarier og miljøer
- **Lokal Træning**: Træn modeller lokalt med GPU-understøttelse til edge-specifikke krav
- **Azure Integration**: Udnyt Azure Container Apps til cloud-baseret finjustering før edge-implementering
- **Transfer Learning**: Tilpas fortrænede modeller til edge-specifikke opgaver og begrænsninger

### 7. Præstationsovervågning og Sporing
- **Edge Præstationsanalyse**: Overvåg modelpræstation under edge-lignende forhold
- **Sporingsindsamling**: Indsamle detaljerede præstationsdata til optimering
- **Flaskehalsidentifikation**: Identificer præstationsproblemer før implementering på edge-enheder
- **Ressourceforbrugsovervågning**: Overvåg hukommelse, CPU og inferenstid for edge-optimering

## Edge AI Udviklingsarbejdsgang

### Fase 1: Modelopdagelse og Udvælgelse
1. **Udforsk Modelkatalog**: Brug modelkataloget til at finde modeller, der er egnede til edge-implementering
2. **Sammenlign Præstation**: Evaluer modeller baseret på størrelse, nøjagtighed og inferenshastighed
3. **Test Lokalt**: Brug Ollama eller ONNX-modeller til lokal test før edge-implementering
4. **Vurder Ressourcekrav**: Bestem hukommelses- og beregningsbehov for mål-edge-enheder

### Fase 2: Modeloptimering
1. **Konverter til ONNX**: Konverter udvalgte modeller til ONNX-format for edge-kompatibilitet
2. **Anvend Kvantisering**: Reducer modelstørrelse gennem INT8 eller INT4 kvantisering
3. **Hardwareoptimering**: Optimer til mål-edge-hardware (ARM, x86, specialiserede acceleratorer)
4. **Præstationsvalidering**: Valider, at optimerede modeller opretholder acceptabel nøjagtighed

### Fase 3: Applikationsudvikling
1. **Agentdesign**: Brug Agent Builder til at skabe edge-optimerede AI-agenter
2. **Prompt Engineering**: Udvikl prompts, der fungerer effektivt med mindre edge-modeller
3. **Integrationstest**: Test agenter under simulerede edge-forhold
4. **Kodegenerering**: Generer produktionskode optimeret til edge-implementering

### Fase 4: Evaluering og Test
1. **Batch Evaluering**: Test flere konfigurationer for at finde optimale edge-indstillinger
2. **Præstationsprofilering**: Analyser inferenshastighed, hukommelsesforbrug og nøjagtighed
3. **Edge Simulation**: Test under forhold, der ligner mål-edge-implementeringsmiljøet
4. **Stress Testning**: Evaluer præstation under forskellige belastningsforhold

### Fase 5: Implementeringsforberedelse
1. **Endelig Optimering**: Anvend endelige optimeringer baseret på testresultater
2. **Implementeringspakning**: Pak modeller og kode til edge-implementering
3. **Dokumentation**: Dokumenter implementeringskrav og konfiguration
4. **Overvågningsopsætning**: Forbered overvågning og logning til edge-implementering

## Målgruppe for Edge AI Udvikling

### Edge AI Udviklere
- Applikationsudviklere, der bygger AI-drevne edge-enheder og IoT-løsninger
- Udviklere af indlejrede systemer, der integrerer AI-funktioner i ressourcebegrænsede enheder
- Mobiludviklere, der skaber on-device AI-applikationer til smartphones og tablets

### Edge AI Ingeniører
- AI-ingeniører, der optimerer modeller til edge-implementering og administrerer inferens-pipelines
- DevOps-ingeniører, der implementerer og administrerer AI-modeller på distribueret edge-infrastruktur
- Præstationsingeniører, der optimerer AI-arbejdsbelastninger til edge-hardwarebegrænsninger

### Forskere og Undervisere
- AI-forskere, der udvikler effektive modeller og algoritmer til edge computing
- Undervisere, der underviser i Edge AI-koncepter og demonstrerer optimeringsteknikker
- Studerende, der lærer om udfordringer og løsninger i edge AI-implementering

## Edge AI Brugsscenarier

### Smarte IoT-enheder
- **Realtids Billedgenkendelse**: Implementer computer vision-modeller på IoT-kameraer og sensorer
- **Stemmekontrol**: Implementer talegenkendelse og naturlig sprogbehandling på smarte højttalere
- **Prædiktiv Vedligeholdelse**: Kør anomali-detekteringsmodeller på industrielle edge-enheder
- **Miljøovervågning**: Implementer sensor-dataanalysemodeller til miljøapplikationer

### Mobile og Indlejrede Applikationer
- **On-device Oversættelse**: Implementer sprogoversættelsesmodeller, der fungerer offline
- **Augmented Reality**: Implementer realtids objektgenkendelse og sporing til AR-applikationer
- **Sundhedsovervågning**: Kør sundhedsanalysemodeller på wearables og medicinsk udstyr
- **Autonome Systemer**: Implementer beslutningstagende modeller til droner, robotter og køretøjer

### Edge Computing Infrastruktur
- **Edge Datacentre**: Implementer AI-modeller i edge-datacentre til lav-latens applikationer
- **CDN Integration**: Integrer AI-behandlingskapaciteter i content delivery-netværk
- **5G Edge**: Udnyt 5G edge computing til AI-drevne applikationer
- **Fog Computing**: Implementer AI-behandling i fog computing-miljøer

## Installation og Opsætning

### Hurtig Installation
Installer AI Toolkit-udvidelsen direkte fra Visual Studio Code Marketplace:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Forudsætninger for Edge AI Udvikling
- **ONNX Runtime**: Installer ONNX Runtime til modelinference
- **Ollama** (Valgfrit): Installer Ollama til lokal modelservering
- **Python Miljø**: Opsæt Python med nødvendige AI-biblioteker
- **Edge Hardware Værktøjer**: Installer hardware-specifikke udviklingsværktøjer (CUDA, OpenVINO osv.)

### Indledende Konfiguration
1. Åbn VS Code og installer AI Toolkit-udvidelsen
2. Konfigurer modelkilder (ONNX, Ollama, cloud-leverandører)
3. Opsæt lokalt udviklingsmiljø til edge-testning
4. Konfigurer hardwareaccelerationsmuligheder til din udviklingsmaskine

## Kom godt i gang med Edge AI Udvikling

### Trin 1: Modeludvælgelse
1. Åbn AI Toolkit-visningen i Aktivitetslinjen
2. Gennemse Modelkataloget for edge-kompatible modeller
3. Filtrer efter modelstørrelse, format (ONNX) og præstationskarakteristika
4. Sammenlign modeller ved hjælp af de indbyggede sammenligningsværktøjer

### Trin 2: Lokal Testning
1. Brug Playground til at teste udvalgte modeller lokalt
2. Eksperimenter med forskellige prompts og parametre
3. Overvåg præstationsmetrics under testning
4. Evaluer modelrespons for edge-brugsscenariekrav

### Trin 3: Modeloptimering
1. Brug Modelkonverteringsværktøjer til at optimere til edge-implementering
2. Anvend kvantisering for at reducere modelstørrelse
3. Test optimerede modeller for at sikre acceptabel præstation
4. Dokumenter optimeringsindstillinger og præstationskompromiser

### Trin 4: Agentudvikling
1. Brug Agent Builder til at skabe edge-optimerede AI-agenter
2. Udvikl prompts, der fungerer effektivt med mindre modeller
3. Integrer nødvendige værktøjer og API'er til edge-scenarier
4. Test agenter under simulerede edge-forhold

### Trin 5: Evaluering og Implementering
1. Brug bulk-evaluering til at teste flere konfigurationer
2. Profilér præstation under forskellige forhold
3. Forbered implementeringspakker til mål-edge-enheder
4. Opsæt overvågning og logning til produktionsimplementering

## Bedste Praksis for Edge AI Udvikling

### Modeludvælgelse
- **Størrelsesbegrænsninger**: Vælg modeller, der passer inden for hukommelsesbegrænsningerne for mål-enheder
- **Inferenshastighed**: Prioriter modeller med hurtige inferenstider til realtidsapplikationer
- **Nøjagtighedskompromiser**: Balancer modelnøjagtighed med ressourcebegrænsninger
- **Formatkompatibilitet**: Foretræk ONNX eller hardware-optimerede formater til edge-implementering

### Optimeringsteknikker
- **Kvantisering**: Brug INT8 eller INT4 kvantisering til at reducere modelstørrelse og forbedre hastighed
- **Beskæring**: Fjern unødvendige modelparametre for at reducere beregningskrav
- **Knowledge Distillation**: Skab mindre modeller, der opretholder præstationen af større modeller
- **Hardwareacceleration**: Udnyt NPUs, GPUs eller specialiserede acceleratorer, når det er muligt

### Udviklingsarbejdsgang
- **Iterativ
- **Sikkerhed**: Implementer passende sikkerhedsforanstaltninger for Edge AI-applikationer

## Integration med Edge AI-rammer

### ONNX Runtime
- **Platformuafhængig Udrulning**: Udrul ONNX-modeller på tværs af forskellige edge-platforme
- **Hardwareoptimering**: Udnyt ONNX Runtimes hardware-specifikke optimeringer
- **Mobil Support**: Brug ONNX Runtime Mobile til smartphone- og tabletapplikationer
- **IoT Integration**: Udrul på IoT-enheder med ONNX Runtimes letvægtsdistributioner

### Windows ML
- **Windows-enheder**: Optimer til Windows-baserede edge-enheder og PC'er
- **NPU Acceleration**: Udnyt Neural Processing Units på Windows-enheder
- **DirectML**: Brug DirectML til GPU-acceleration på Windows-platforme
- **UWP Integration**: Integrer med Universal Windows Platform-applikationer

### TensorFlow Lite
- **Mobiloptimering**: Udrul TensorFlow Lite-modeller på mobile og indlejrede enheder
- **Hardwaredelegeringer**: Brug specialiserede hardwaredelegeringer til acceleration
- **Mikrocontrollere**: Udrul på mikrocontrollere med TensorFlow Lite Micro
- **Platformuafhængig Support**: Udrul på tværs af Android, iOS og indlejrede Linux-systemer

### Azure IoT Edge
- **Cloud-Edge Hybrid**: Kombiner cloud-træning med edge-inferens
- **Moduludrulning**: Udrul AI-modeller som IoT Edge-moduler
- **Enhedsstyring**: Administrer edge-enheder og modelopdateringer eksternt
- **Telemetri**: Indsaml ydelsesdata og modelmetrikker fra edge-udrulninger

## Avancerede Edge AI-scenarier

### Multi-Model Udrulning
- **Modelensembler**: Udrul flere modeller for forbedret nøjagtighed eller redundans
- **A/B Testning**: Test forskellige modeller samtidig på edge-enheder
- **Dynamisk Udvælgelse**: Vælg modeller baseret på aktuelle enhedsforhold
- **Ressourcedeling**: Optimer ressourceforbrug på tværs af flere udrullede modeller

### Federated Learning
- **Distribueret Træning**: Træn modeller på tværs af flere edge-enheder
- **Privatlivsbeskyttelse**: Behold træningsdata lokalt, mens modelforbedringer deles
- **Samarbejdende Læring**: Gør det muligt for enheder at lære af kollektive erfaringer
- **Edge-Cloud Koordination**: Koordiner læring mellem edge-enheder og cloud-infrastruktur

### Realtidsbehandling
- **Streambehandling**: Behandl kontinuerlige datastrømme på edge-enheder
- **Lav-latens Inferens**: Optimer for minimal inferenslatens
- **Batchbehandling**: Behandl effektivt datapartier på edge-enheder
- **Adaptiv Behandling**: Juster behandling baseret på aktuelle enhedskapaciteter

## Fejlfinding i Edge AI-udvikling

### Almindelige Problemer
- **Hukommelsesbegrænsninger**: Model for stor til mål-enhedens hukommelse
- **Inferenshastighed**: Modelinferens for langsom til realtidskrav
- **Nøjagtighedsforringelse**: Optimering reducerer modelnøjagtighed uacceptabelt
- **Hardwarekompatibilitet**: Model ikke kompatibel med mål-hardware

### Fejlfindingsstrategier
- **Ydelsesprofilering**: Brug AI Toolkits sporingsfunktioner til at identificere flaskehalse
- **Ressourceovervågning**: Overvåg hukommelse og CPU-forbrug under udvikling
- **Inkrementel Testning**: Test optimeringer trinvis for at isolere problemer
- **Hardwaresimulering**: Brug udviklingsværktøjer til at simulere mål-hardware

### Optimeringsløsninger
- **Mere Aggressiv Kvantisering**: Anvend mere aggressive kvantiseringsteknikker
- **Modelarkitektur**: Overvej forskellige modelarkitekturer optimeret til edge
- **Forbehandlingsoptimering**: Optimer databehandling for edge-begrænsninger
- **Inferensoptimering**: Brug hardware-specifikke inferensoptimeringer

## Ressourcer og Næste Skridt

### Dokumentation
- [AI Toolkit Models Guide](https://code.visualstudio.com/docs/intelligentapps/models)
- [Model Playground Documentation](https://code.visualstudio.com/docs/intelligentapps/playground)
- [ONNX Runtime Documentation](https://onnxruntime.ai/)
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)

### Fællesskab og Support
- [VS Code AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [ONNX Community](https://github.com/onnx/onnx)
- [Edge AI Developer Community](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Læringsressourcer
- [Edge AI Fundamentals Course](./Module01/README.md)
- [Small Language Models Guide](./Module02/README.md)
- [Edge Deployment Strategies](./Module03/README.md)
- [Windows Edge AI Development](./windowdeveloper.md)

## Konklusion

AI Toolkit for Visual Studio Code tilbyder en omfattende platform til Edge AI-udvikling, fra modelopdagelse og optimering til udrulning og overvågning. Ved at udnytte de integrerede værktøjer og arbejdsgange kan udviklere effektivt skabe, teste og udrulle AI-applikationer, der fungerer godt på ressourcebegrænsede edge-enheder.

Toolkitets support til ONNX, Ollama og forskellige cloud-leverandører, kombineret med dets optimerings- og evalueringsmuligheder, gør det til et ideelt valg for Edge AI-udvikling. Uanset om du bygger IoT-applikationer, mobile AI-funktioner eller indlejrede intelligenssystemer, giver AI Toolkit de nødvendige værktøjer og arbejdsgange til succesfuld Edge AI-udrulning.

Efterhånden som Edge AI fortsætter med at udvikle sig, forbliver AI Toolkit for VS Code i frontlinjen og tilbyder udviklere avancerede værktøjer og kapaciteter til at bygge næste generation af intelligente edge-applikationer.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.