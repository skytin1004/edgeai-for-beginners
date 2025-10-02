<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T13:25:28+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "nl"
}
-->
# AI Toolkit voor Visual Studio Code - Handleiding voor Edge AI-ontwikkeling

## Introductie

Welkom bij de uitgebreide handleiding voor het gebruik van AI Toolkit voor Visual Studio Code in Edge AI-ontwikkeling. Nu kunstmatige intelligentie verschuift van gecentraliseerde cloudcomputing naar gedistribueerde edge-apparaten, hebben ontwikkelaars krachtige, geïntegreerde tools nodig die de unieke uitdagingen van edge-implementatie aankunnen - van beperkte middelen tot vereisten voor offline werking.

AI Toolkit voor Visual Studio Code overbrugt deze kloof door een complete ontwikkelomgeving te bieden die specifiek is ontworpen voor het bouwen, testen en optimaliseren van AI-toepassingen die efficiënt draaien op edge-apparaten. Of je nu ontwikkelt voor IoT-sensoren, mobiele apparaten, embedded systemen of edge-servers, deze toolkit stroomlijnt je hele ontwikkelworkflow binnen de vertrouwde VS Code-omgeving.

Deze handleiding neemt je mee door de essentiële concepten, tools en best practices om AI Toolkit te benutten in je Edge AI-projecten, van de initiële modelselectie tot productie-implementatie.

## Overzicht

AI Toolkit voor Visual Studio Code is een krachtige extensie die agentontwikkeling en het creëren van AI-toepassingen vereenvoudigt. De toolkit biedt uitgebreide mogelijkheden voor het verkennen, evalueren en implementeren van AI-modellen van een breed scala aan providers—waaronder Anthropic, OpenAI, GitHub, Google—en ondersteunt lokale modeluitvoering met ONNX en Ollama.

Wat AI Toolkit onderscheidt, is de uitgebreide aanpak van de hele AI-ontwikkelingscyclus. In tegenstelling tot traditionele AI-ontwikkeltools die zich richten op afzonderlijke aspecten, biedt AI Toolkit een geïntegreerde omgeving die modelontdekking, experimentatie, agentontwikkeling, evaluatie en implementatie omvat—alles binnen de vertrouwde VS Code-omgeving.

Het platform is specifiek ontworpen voor snelle prototyping en productie-implementatie, met functies zoals promptgeneratie, snelle starters, naadloze MCP (Model Context Protocol) toolintegraties en uitgebreide evaluatiemogelijkheden. Voor Edge AI-ontwikkeling betekent dit dat je efficiënt AI-toepassingen kunt ontwikkelen, testen en optimaliseren voor edge-implementatiescenario's, terwijl je de volledige ontwikkelworkflow binnen VS Code behoudt.

## Leerdoelen

Aan het einde van deze handleiding kun je:

### Kerncompetenties
- **Installeren en configureren** van AI Toolkit voor Visual Studio Code voor Edge AI-ontwikkelingsworkflows
- **Navigeren en gebruiken** van de AI Toolkit-interface, inclusief Model Catalog, Playground en Agent Builder
- **Selecteren en evalueren** van AI-modellen die geschikt zijn voor edge-implementatie op basis van prestaties en resourcebeperkingen
- **Converteren en optimaliseren** van modellen met behulp van ONNX-formaat en kwantiseringstechnieken voor edge-apparaten

### Vaardigheden in Edge AI-ontwikkeling
- **Ontwerpen en implementeren** van Edge AI-toepassingen met behulp van de geïntegreerde ontwikkelomgeving
- **Modeltesten uitvoeren** in edge-achtige omstandigheden met lokale inferentie en resourcebewaking
- **AI-agents creëren en aanpassen** die geoptimaliseerd zijn voor edge-implementatiescenario's
- **Modelprestaties evalueren** met behulp van relevante metrics voor edge computing (latentie, geheugengebruik, nauwkeurigheid)

### Optimalisatie en implementatie
- **Kwantisering en pruning toepassen** om de modelgrootte te verkleinen terwijl de prestaties acceptabel blijven
- **Modellen optimaliseren** voor specifieke edge-hardwareplatforms, inclusief CPU-, GPU- en NPU-versnelling
- **Best practices implementeren** voor Edge AI-ontwikkeling, inclusief resourcebeheer en fallback-strategieën
- **Modellen en toepassingen voorbereiden** voor productie-implementatie op edge-apparaten

### Geavanceerde Edge AI-concepten
- **Integreren met edge AI-frameworks** zoals ONNX Runtime, Windows ML en TensorFlow Lite
- **Multi-modelarchitecturen en federated learning** implementeren voor edge-omgevingen
- **Veelvoorkomende Edge AI-problemen oplossen** zoals geheugenbeperkingen, inferentiesnelheid en hardwarecompatibiliteit
- **Monitoring- en logstrategieën ontwerpen** voor Edge AI-toepassingen in productie

### Praktische toepassing
- **End-to-end Edge AI-oplossingen bouwen** van modelselectie tot implementatie
- **Bekwaamheid demonstreren** in edge-specifieke ontwikkelworkflows en optimalisatietechnieken
- **Geleerde concepten toepassen** op real-world Edge AI-use cases, waaronder IoT, mobiel en embedded toepassingen
- **Verschillende Edge AI-implementatiestrategieën evalueren en vergelijken** en hun afwegingen begrijpen

## Belangrijke functies voor Edge AI-ontwikkeling

### 1. Modelcatalogus en ontdekking
- **Ondersteuning voor meerdere providers**: Blader door en krijg toegang tot AI-modellen van Anthropic, OpenAI, GitHub, Google en andere providers
- **Lokale modelintegratie**: Vereenvoudigde ontdekking van ONNX- en Ollama-modellen voor edge-implementatie
- **GitHub-modellen**: Directe integratie met GitHub's modelhosting voor gestroomlijnde toegang
- **Modelvergelijking**: Vergelijk modellen naast elkaar om de optimale balans te vinden voor edge-apparaatbeperkingen

### 2. Interactieve Playground
- **Interactieve testomgeving**: Snel experimenteren met modelmogelijkheden in een gecontroleerde omgeving
- **Ondersteuning voor multimodale input**: Testen met afbeeldingen, tekst en andere inputs die typisch zijn in edge-scenario's
- **Realtime experimentatie**: Directe feedback op modelreacties en prestaties
- **Parameteroptimalisatie**: Fijn afstemmen van modelparameters voor edge-implementatievereisten

### 3. Prompt (Agent) Builder
- **Generatie van natuurlijke taal**: Starterprompts genereren met behulp van natuurlijke taalbeschrijvingen
- **Iteratieve verfijning**: Prompts verbeteren op basis van modelreacties en prestaties
- **Taakdecompositie**: Complexe taken opsplitsen met prompt chaining en gestructureerde outputs
- **Ondersteuning voor variabelen**: Variabelen gebruiken in prompts voor dynamisch agentgedrag
- **Productiecodegeneratie**: Productieklaar code genereren voor snelle app-ontwikkeling

### 4. Bulkuitvoering en evaluatie
- **Multi-modeltesten**: Meerdere prompts tegelijkertijd uitvoeren op geselecteerde modellen
- **Efficiënt testen op schaal**: Verschillende inputs en configuraties efficiënt testen
- **Aangepaste testcases**: Agents uitvoeren met testcases om functionaliteit te valideren
- **Prestatievergelijking**: Resultaten vergelijken tussen verschillende modellen en configuraties

### 5. Modelevaluatie met datasets
- **Standaardmetrics**: AI-modellen testen met ingebouwde evaluatoren (F1-score, relevantie, gelijkenis, samenhang)
- **Aangepaste evaluatoren**: Eigen evaluatiemetrics creëren voor specifieke use cases
- **Datasetintegratie**: Modellen testen tegen uitgebreide datasets
- **Prestatiemeting**: Modelprestaties kwantificeren voor edge-implementatiebeslissingen

### 6. Fine-tuning mogelijkheden
- **Modelaanpassing**: Modellen aanpassen voor specifieke use cases en domeinen
- **Gespecialiseerde adaptatie**: Modellen aanpassen aan gespecialiseerde domeinen en vereisten
- **Edge-optimalisatie**: Modellen specifiek fine-tunen voor edge-implementatiebeperkingen
- **Domeinspecifieke training**: Modellen creëren die zijn afgestemd op specifieke edge-use cases

### 7. MCP-toolintegratie
- **Connectiviteit met externe tools**: Agents verbinden met externe tools via Model Context Protocol-servers
- **Acties in de echte wereld**: Agents in staat stellen databases te raadplegen, API's te benaderen of aangepaste logica uit te voeren
- **Bestaande MCP-servers**: Tools gebruiken via command (stdio) of HTTP (server-sent event) protocollen
- **Aangepaste MCP-ontwikkeling**: Nieuwe MCP-servers bouwen en testen in Agent Builder

### 8. Agentontwikkeling en testen
- **Ondersteuning voor functieaanroepen**: Agents in staat stellen externe functies dynamisch aan te roepen
- **Realtime integratietesten**: Integraties testen met realtime runs en toolgebruik
- **Agentversiebeheer**: Versiebeheer voor agents met vergelijkingsmogelijkheden voor evaluatieresultaten
- **Debugging en tracing**: Lokale tracing- en debuggingmogelijkheden voor agentontwikkeling

## Workflow voor Edge AI-ontwikkeling

### Fase 1: Modelontdekking en selectie
1. **Modelcatalogus verkennen**: Gebruik de modelcatalogus om modellen te vinden die geschikt zijn voor edge-implementatie
2. **Prestaties vergelijken**: Modellen evalueren op basis van grootte, nauwkeurigheid en inferentiesnelheid
3. **Lokaal testen**: Ollama- of ONNX-modellen lokaal testen voordat ze op edge worden geïmplementeerd
4. **Resourcevereisten beoordelen**: Geheugen- en computatiebehoeften bepalen voor doel-edge-apparaten

### Fase 2: Modeloptimalisatie
1. **Converteren naar ONNX**: Geselecteerde modellen converteren naar ONNX-formaat voor edge-compatibiliteit
2. **Kwantisering toepassen**: Modelgrootte verkleinen via INT8- of INT4-kwantisering
3. **Hardwareoptimalisatie**: Optimaliseren voor doel-edge-hardware (ARM, x86, gespecialiseerde accelerators)
4. **Prestatievalidatie**: Geoptimaliseerde modellen valideren om acceptabele nauwkeurigheid te behouden

### Fase 3: Applicatieontwikkeling
1. **Agentontwerp**: Gebruik Agent Builder om edge-geoptimaliseerde AI-agents te creëren
2. **Promptengineering**: Prompts ontwikkelen die effectief werken met kleinere edge-modellen
3. **Integratietesten**: Agents testen in gesimuleerde edge-omstandigheden
4. **Codegeneratie**: Productieklaar code genereren die geoptimaliseerd is voor edge-implementatie

### Fase 4: Evaluatie en testen
1. **Batch-evaluatie**: Meerdere configuraties testen om optimale edge-instellingen te vinden
2. **Prestatieprofilering**: Inferentiesnelheid, geheugengebruik en nauwkeurigheid analyseren
3. **Edge-simulatie**: Testen in omstandigheden die vergelijkbaar zijn met de doel-edge-implementatieomgeving
4. **Stress-testen**: Prestaties evalueren onder verschillende belastingomstandigheden

### Fase 5: Voorbereiding op implementatie
1. **Eindoptimalisatie**: Laatste optimalisaties toepassen op basis van testresultaten
2. **Implementatieverpakking**: Modellen en code verpakken voor edge-implementatie
3. **Documentatie**: Implementatievereisten en configuratie documenteren
4. **Monitoring instellen**: Monitoring en logging voorbereiden voor edge-implementatie

## Doelgroep voor Edge AI-ontwikkeling

### Edge AI-ontwikkelaars
- Applicatieontwikkelaars die AI-aangedreven edge-apparaten en IoT-oplossingen bouwen
- Embedded systems-ontwikkelaars die AI-functionaliteiten integreren in apparaten met beperkte middelen
- Mobiele ontwikkelaars die on-device AI-toepassingen maken voor smartphones en tablets

### Edge AI-ingenieurs
- AI-ingenieurs die modellen optimaliseren voor edge-implementatie en inferentie-pipelines beheren
- DevOps-ingenieurs die AI-modellen implementeren en beheren in gedistribueerde edge-infrastructuur
- Prestatie-ingenieurs die AI-workloads optimaliseren voor edge-hardwarebeperkingen

### Onderzoekers en docenten
- AI-onderzoekers die efficiënte modellen en algoritmen ontwikkelen voor edge computing
- Docenten die Edge AI-concepten onderwijzen en optimalisatietechnieken demonstreren
- Studenten die leren over de uitdagingen en oplossingen in edge AI-implementatie

## Edge AI-use cases

### Slimme IoT-apparaten
- **Realtime beeldherkenning**: Computervisiemodellen implementeren op IoT-camera's en sensoren
- **Stemverwerking**: Spraakherkenning en natuurlijke taalverwerking implementeren op slimme luidsprekers
- **Voorspellend onderhoud**: Anomaliedetectiemodellen uitvoeren op industriële edge-apparaten
- **Milieubewaking**: Sensorgegevensanalysemodellen implementeren voor milieutoepassingen

### Mobiele en embedded toepassingen
- **On-device vertaling**: Taalvertalingsmodellen implementeren die offline werken
- **Augmented reality**: Realtime objectherkenning en tracking implementeren voor AR-toepassingen
- **Gezondheidsmonitoring**: Gezondheidsanalysemiddelen uitvoeren op draagbare apparaten en medische apparatuur
- **Autonome systemen**: Besluitvormingsmodellen implementeren voor drones, robots en voertuigen

### Edge computing-infrastructuur
- **Edge-datacenters**: AI-modellen implementeren in edge-datacenters voor toepassingen met lage latentie
- **CDN-integratie**: AI-verwerkingsmogelijkheden integreren in content delivery-netwerken
- **5G Edge**: 5G-edge computing benutten voor AI-aangedreven toepassingen
- **Fog computing**: AI-verwerking implementeren in fog computing-omgevingen

## Installatie en configuratie

### Extensie-installatie
Installeer de AI Toolkit-extensie rechtstreeks vanuit de Visual Studio Code Marketplace:

**Extensie-ID**: `ms-windows-ai-studio.windows-ai-studio`

**Installatiemethoden**:
1. **VS Code Marketplace**: Zoek naar "AI Toolkit" in de Extensies-weergave
2. **Command Line**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Directe installatie**: Download van [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Vereisten voor Edge AI-ontwikkeling
- **Visual Studio Code**: Laatste versie aanbevolen
- **Python-omgeving**: Python 3.8+ met vereiste AI-bibliotheken
- **ONNX Runtime** (optioneel): Voor ONNX-modelinferentie
- **Ollama** (optioneel): Voor lokale modelservering
- **Hardwareversnellingstools**: CUDA, OpenVINO of platformspecifieke versnellers

### Initiële configuratie
1. **Extensie activeren**: Open VS Code en controleer of AI Toolkit verschijnt in de Activiteitenbalk
2. **Modelproviderinstelling**: Toegang configureren tot GitHub, OpenAI, Anthropic of andere modelproviders
3. **Lokale omgeving**: Python-omgeving instellen en vereiste pakketten installeren
4. **Hardwareversnelling**: GPU/NPU-versnelling configureren indien beschikbaar
5. **MCP-integratie**: Model Context Protocol-servers instellen indien nodig

### Checklist voor eerste installatie
- [ ] AI Toolkit-extensie geïnstalleerd en geactiveerd
- [ ] Modelcatalogus toegankelijk en modellen vindbaar
- [ ] Playground functioneel voor modeltesten
- [ ] Agent Builder toegankelijk voor promptontwikkeling
- [ ] Lokale ontwikkelomgeving geconfigureerd
- [ ] Hardwareversnelling (indien beschikbaar) correct geconfigureerd

## Aan de slag met AI Toolkit

### Snelle startgids

We raden aan te beginnen met modellen die door GitHub worden gehost voor de meest gestroomlijnde ervaring:

1. **Installatie**: Volg de [installatiehandleiding](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) om AI Toolkit op je apparaat in te stellen
2. **Modelontdekking**: Selecteer **CATALOG > Models** in de extensieboomweergave om beschikbare modellen te verkennen
3. **GitHub-modellen**: Begin met modellen die door GitHub worden gehost voor optimale integratie
4. **Playground-testen**: Selecteer **Try in Playground** vanuit een modelkaart om te beginnen met experimenteren met modelmogelijkheden

### Stapsgewijze Edge AI-ontwikkeling

#### Stap 1: Modelverkenning en selectie
1. Open de AI Toolkit-weergave in de Activiteitenbalk van VS Code
2. Blader door de Model Catalog voor modellen die geschikt zijn voor edge-implementatie
3. Filter op provider (GitHub, ONNX, Ollama) op basis van je edge-vereisten
4. Gebruik **Try in Playground** om modelmogelijkheden direct te testen

#### Stap 2: Agentontwikkeling
1. Gebruik de **Prompt (Agent) Builder** om edge-geoptimaliseerde AI-agents te creëren
2. Genereer startprompts met behulp van natuurlijke taalbeschrijvingen  
3. Itereer en verfijn prompts op basis van modelreacties  
4. Integreer MCP-tools voor verbeterde agentmogelijkheden  

#### Stap 3: Testen en Evaluatie  
1. Gebruik **Bulk Run** om meerdere prompts te testen op geselecteerde modellen  
2. Voer agents uit met testcases om functionaliteit te valideren  
3. Evalueer nauwkeurigheid en prestaties met ingebouwde of aangepaste metrics  
4. Vergelijk verschillende modellen en configuraties  

#### Stap 4: Fijnafstemming en Optimalisatie  
1. Pas modellen aan voor specifieke edge-use cases  
2. Voer domeinspecifieke fijnafstemming uit  
3. Optimaliseer voor beperkingen bij edge-implementatie  
4. Versieer en vergelijk verschillende agentconfiguraties  

#### Stap 5: Voorbereiding op Implementatie  
1. Genereer productieklare code met de Agent Builder  
2. Stel MCP-serververbindingen in voor productiegebruik  
3. Bereid implementatiepakketten voor edge-apparaten voor  
4. Configureer monitoring- en evaluatiemetrics  

## Best Practices voor Edge AI-ontwikkeling  

### Modelselectie  
- **Beperkingen qua grootte**: Kies modellen die passen binnen de geheugencapaciteit van de doelapparaten  
- **Inference-snelheid**: Geef prioriteit aan modellen met snelle inference-tijden voor realtime toepassingen  
- **Nauwkeurigheid versus middelen**: Vind een balans tussen modelnauwkeurigheid en resourcebeperkingen  
- **Compatibiliteit van formaten**: Geef de voorkeur aan ONNX of hardware-geoptimaliseerde formaten voor edge-implementatie  

### Optimalisatietechnieken  
- **Quantisatie**: Gebruik INT8- of INT4-quantisatie om de modelgrootte te verkleinen en de snelheid te verbeteren  
- **Pruning**: Verwijder onnodige modelparameters om de rekenvereisten te verminderen  
- **Knowledge Distillation**: Maak kleinere modellen die de prestaties van grotere modellen behouden  
- **Hardwareversnelling**: Maak gebruik van NPUs, GPUs of gespecialiseerde versnellers indien beschikbaar  

### Ontwikkelworkflow  
- **Iteratief testen**: Test regelmatig in edge-achtige omstandigheden tijdens ontwikkeling  
- **Prestatiemonitoring**: Houd resourcegebruik en inference-snelheid continu in de gaten  
- **Versiebeheer**: Houd modelversies en optimalisatie-instellingen bij  
- **Documentatie**: Documenteer alle optimalisatiebeslissingen en afwegingen in prestaties  

### Overwegingen bij implementatie  
- **Resource monitoring**: Houd geheugen-, CPU- en energiegebruik in productie in de gaten  
- **Fallback-strategieën**: Implementeer fallback-mechanismen voor modelstoringen  
- **Update-mechanismen**: Plan modelupdates en versiebeheer  
- **Beveiliging**: Implementeer passende beveiligingsmaatregelen voor edge AI-toepassingen  

## Integratie met Edge AI-frameworks  

### ONNX Runtime  
- **Cross-platform implementatie**: Implementeer ONNX-modellen op verschillende edge-platforms  
- **Hardwareoptimalisatie**: Maak gebruik van hardware-specifieke optimalisaties van ONNX Runtime  
- **Mobiele ondersteuning**: Gebruik ONNX Runtime Mobile voor smartphones en tablets  
- **IoT-integratie**: Implementeer op IoT-apparaten met behulp van lichte distributies van ONNX Runtime  

### Windows ML  
- **Windows-apparaten**: Optimaliseer voor Windows-gebaseerde edge-apparaten en pc's  
- **NPU-versnelling**: Maak gebruik van Neural Processing Units op Windows-apparaten  
- **DirectML**: Gebruik DirectML voor GPU-versnelling op Windows-platforms  
- **UWP-integratie**: Integreer met Universal Windows Platform-toepassingen  

### TensorFlow Lite  
- **Mobiele optimalisatie**: Implementeer TensorFlow Lite-modellen op mobiele en embedded apparaten  
- **Hardwaredelegates**: Gebruik gespecialiseerde hardwaredelegates voor versnelling  
- **Microcontrollers**: Implementeer op microcontrollers met TensorFlow Lite Micro  
- **Cross-platform ondersteuning**: Implementeer op Android, iOS en embedded Linux-systemen  

### Azure IoT Edge  
- **Cloud-Edge hybride**: Combineer cloudtraining met edge-inference  
- **Module-implementatie**: Implementeer AI-modellen als IoT Edge-modules  
- **Apparaatbeheer**: Beheer edge-apparaten en modelupdates op afstand  
- **Telemetrie**: Verzamel prestatiegegevens en modelmetrics van edge-implementaties  

## Geavanceerde Edge AI-scenario's  

### Multi-model implementatie  
- **Modelensembles**: Implementeer meerdere modellen voor verbeterde nauwkeurigheid of redundantie  
- **A/B-testen**: Test verschillende modellen tegelijkertijd op edge-apparaten  
- **Dynamische selectie**: Kies modellen op basis van de huidige apparaatcondities  
- **Resource sharing**: Optimaliseer resourcegebruik over meerdere geïmplementeerde modellen  

### Federated Learning  
- **Gedistribueerde training**: Train modellen op meerdere edge-apparaten  
- **Privacybescherming**: Houd trainingsdata lokaal terwijl modelverbeteringen worden gedeeld  
- **Collaboratief leren**: Laat apparaten leren van collectieve ervaringen  
- **Edge-Cloud coördinatie**: Coördineer leren tussen edge-apparaten en cloudinfrastructuur  

### Realtime verwerking  
- **Streamverwerking**: Verwerk continue datastromen op edge-apparaten  
- **Inference met lage latentie**: Optimaliseer voor minimale inference-latentie  
- **Batchverwerking**: Verwerk batches van data efficiënt op edge-apparaten  
- **Adaptieve verwerking**: Pas verwerking aan op basis van de huidige apparaatcapaciteiten  

## Problemen oplossen bij Edge AI-ontwikkeling  

### Veelvoorkomende problemen  
- **Geheugenbeperkingen**: Model te groot voor het geheugen van het doelapparaat  
- **Inference-snelheid**: Modelinference te traag voor realtimevereisten  
- **Nauwkeurigheidsverlies**: Optimalisatie vermindert modelnauwkeurigheid onaanvaardbaar  
- **Hardwarecompatibiliteit**: Model niet compatibel met doelhardware  

### Debugging-strategieën  
- **Prestatieprofilering**: Gebruik tracingfuncties van AI Toolkit om knelpunten te identificeren  
- **Resource monitoring**: Houd geheugen- en CPU-gebruik tijdens ontwikkeling in de gaten  
- **Incrementeel testen**: Test optimalisaties stapsgewijs om problemen te isoleren  
- **Hardware simulatie**: Gebruik ontwikkeltools om doelhardware te simuleren  

### Optimalisatieoplossingen  
- **Verdergaande quantisatie**: Pas agressievere quantisatietechnieken toe  
- **Modelarchitectuur**: Overweeg andere modelarchitecturen die geoptimaliseerd zijn voor edge  
- **Preprocessing-optimalisatie**: Optimaliseer datavoorverwerking voor edge-beperkingen  
- **Inference-optimalisatie**: Gebruik hardware-specifieke inference-optimalisaties  

## Bronnen en volgende stappen  

### Officiële documentatie  
- [AI Toolkit Developer Documentatie](https://aka.ms/AIToolkit/doc)  
- [Installatie- en Setupgids](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps Documentatie](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) Documentatie](https://modelcontextprotocol.io/)  

### Community en ondersteuning  
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub Issues en Functieaanvragen](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord Community](https://aka.ms/azureaifoundry/discord)  
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Technische bronnen  
- [ONNX Runtime Documentatie](https://onnxruntime.ai/)  
- [Ollama Documentatie](https://ollama.ai/)  
- [Windows ML Documentatie](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry Documentatie](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Leertrajecten  
- [Edge AI Fundamentals Cursus](../Module01/README.md)  
- [Small Language Models Gids](../Module02/README.md)  
- [Edge Implementatiestrategieën](../Module03/README.md)  
- [Windows Edge AI Ontwikkeling](./windowdeveloper.md)  

### Aanvullende bronnen  
- **Repository Statistieken**: 1.8k+ sterren, 150+ forks, 18+ bijdragers  
- **Licentie**: MIT-licentie  
- **Beveiliging**: Microsoft-beveiligingsbeleid van toepassing  
- **Telemetrie**: Respecteert VS Code-telemetrie-instellingen  

## Conclusie  

AI Toolkit voor Visual Studio Code biedt een uitgebreid platform voor moderne AI-ontwikkeling, met gestroomlijnde mogelijkheden voor agentontwikkeling die bijzonder waardevol zijn voor Edge AI-toepassingen. Met een uitgebreide modelcatalogus die providers zoals Anthropic, OpenAI, GitHub en Google ondersteunt, gecombineerd met lokale uitvoering via ONNX en Ollama, biedt de toolkit de flexibiliteit die nodig is voor diverse edge-implementatiescenario's.  

De kracht van de toolkit ligt in de geïntegreerde aanpak—van modelontdekking en experimentatie in de Playground tot geavanceerde agentontwikkeling met de Prompt Builder, uitgebreide evaluatiemogelijkheden en naadloze MCP-toolintegratie. Voor Edge AI-ontwikkelaars betekent dit snelle prototyping en testen van AI-agents vóór edge-implementatie, met de mogelijkheid om snel te itereren en te optimaliseren voor omgevingen met beperkte middelen.  

Belangrijke voordelen voor Edge AI-ontwikkeling zijn:  
- **Snelle experimentatie**: Test modellen en agents snel voordat ze worden geïmplementeerd op edge  
- **Multi-provider flexibiliteit**: Toegang tot modellen van verschillende bronnen om optimale edge-oplossingen te vinden  
- **Lokale ontwikkeling**: Test met ONNX en Ollama voor offline en privacyvriendelijke ontwikkeling  
- **Productieklaar**: Genereer productieklare code en integreer met externe tools via MCP  
- **Uitgebreide evaluatie**: Gebruik ingebouwde en aangepaste metrics om edge AI-prestaties te valideren  

Naarmate AI zich steeds meer richt op edge-implementatiescenario's, biedt AI Toolkit voor VS Code de ontwikkelomgeving en workflow die nodig zijn om intelligente toepassingen te bouwen, testen en optimaliseren voor omgevingen met beperkte middelen. Of je nu IoT-oplossingen, mobiele AI-toepassingen of embedded intelligentiesystemen ontwikkelt, de uitgebreide functieset en geïntegreerde workflow van de toolkit ondersteunen de volledige edge AI-ontwikkelingscyclus.  

Met voortdurende ontwikkeling en een actieve community (1.8k+ GitHub-sterren) blijft AI Toolkit aan de top van AI-ontwikkeltools, en evolueert het voortdurend om te voldoen aan de behoeften van moderne AI-ontwikkelaars die bouwen voor edge-implementatiescenario's.  

[Next Foundry Local](./foundrylocal.md)  

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.