<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-18T08:30:22+00:00",
  "source_file": "Module07/README.md",
  "language_code": "sv"
}
-->
# Kapitel 07: EdgeAI-exempel

Edge AI representerar sammansmältningen av artificiell intelligens och edge computing, vilket möjliggör intelligent bearbetning direkt på enheter utan att förlita sig på molnanslutning. Detta kapitel utforskar fem olika EdgeAI-implementationer på olika plattformar och ramverk, och visar mångsidigheten och kraften i att köra AI-modeller vid kanten.

## 1. EdgeAI i NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano representerar ett genombrott inom tillgänglig edge AI-datoranvändning och levererar upp till 67 TOPS av AI-prestanda i ett kompakt format i storlek med ett kreditkort. Denna kraftfulla edge AI-plattform demokratiserar utvecklingen av generativ AI för hobbyister, studenter och professionella utvecklare.

### Viktiga funktioner
- Levererar upp till 67 TOPS av AI-prestanda—en 1,7X förbättring jämfört med föregångaren
- 1024 CUDA-kärnor och upp till 32 Tensor-kärnor för AI-bearbetning
- 6-kärnig Arm Cortex-A78AE v8.2 64-bitars CPU med en maximal frekvens på 1,5 GHz
- Prissatt till endast $249, vilket gör den till den mest prisvärda och tillgängliga plattformen för utvecklare, studenter och skapare

### Användningsområden
Jetson Orin Nano utmärker sig i att köra moderna generativa AI-modeller, inklusive vision transformers, stora språkmodeller och vision-språkmodeller. Den är specifikt designad för GenAI-användningsfall och gör det nu möjligt att köra flera LLM:er på en handhållen enhet. Populära användningsområden inkluderar AI-drivna robotar, smarta drönare, intelligenta kameror och autonoma edge-enheter.

**Läs mer**: [NVIDIA:s Jetson Orin Nano SuperComputer: Nästa stora grej inom EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI i mobila applikationer med .NET MAUI och ONNX Runtime GenAI

Denna lösning visar hur man integrerar Generativ AI och Stora Språkmodeller (LLMs) i plattformsoberoende mobila applikationer med hjälp av .NET MAUI (Multi-platform App UI) och ONNX Runtime GenAI. Detta tillvägagångssätt gör det möjligt för .NET-utvecklare att bygga sofistikerade AI-drivna mobila applikationer som körs inbyggt på Android- och iOS-enheter.

### Viktiga funktioner
- Byggd på .NET MAUI-ramverket, vilket ger en enda kodbas för både Android- och iOS-applikationer
- ONNX Runtime GenAI-integration möjliggör körning av generativa AI-modeller direkt på mobila enheter
- Stödjer olika hårdvaruacceleratorer anpassade för mobila enheter, inklusive CPU, GPU och specialiserade mobila AI-processorer
- Plattformsspecifika optimeringar som CoreML för iOS och NNAPI för Android via ONNX Runtime
- Implementerar hela den generativa AI-loopen inklusive för- och efterbearbetning, inferens, logitsbearbetning, sökning och sampling samt KV-cachehantering

### Fördelar med utveckling
Med .NET MAUI kan utvecklare dra nytta av sina befintliga C#- och .NET-kunskaper samtidigt som de bygger plattformsoberoende AI-applikationer. ONNX Runtime GenAI-ramverket stödjer flera modellarkitekturer, inklusive Llama, Mistral, Phi, Gemma och många fler. Optimerade ARM64-kärnor accelererar INT4-kvantiserad matrisberäkning, vilket säkerställer effektiv prestanda på mobil hårdvara samtidigt som den bekanta .NET-utvecklingsupplevelsen bibehålls.

### Användningsområden
Denna lösning är idealisk för utvecklare som vill bygga AI-drivna mobila applikationer med .NET-teknologier, inklusive intelligenta chatbotar, bildigenkänningsappar, språköversättningsverktyg och personliga rekommendationssystem som körs helt på enheten för förbättrad integritet och offlinekapacitet.

**Läs mer**: [.NET MAUI ONNX Runtime GenAI Exempel](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI i Azure med Small Language Models Engine

Microsofts Azure-baserade EdgeAI-lösning fokuserar på att effektivt distribuera Small Language Models (SLMs) i hybridmiljöer mellan moln och edge. Detta tillvägagångssätt överbryggar klyftan mellan AI-tjänster i molnskala och krav på edge-distribution.

### Arkitekturella fördelar
- Sömlös integration med Azure AI-tjänster
- Kör SLM:er/LLM:er och multimodala modeller på enheten och i molnet med ONNX Runtime
- Optimerad för företagsdistribution i stor skala
- Stöd för kontinuerliga modelluppdateringar och hantering

### Användningsområden
Azure EdgeAI-implementationen utmärker sig i scenarier som kräver AI-distribution på företagsnivå med molnhanteringsmöjligheter. Detta inkluderar intelligent dokumentbearbetning, realtidsanalys och hybrida AI-arbetsflöden som utnyttjar både moln- och edge-beräkningsresurser.

**Läs mer**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI med Windows ML

Windows ML representerar Microsofts toppmoderna runtime, optimerad för prestanda vid modellinferens på enheten och förenklad distribution, och fungerar som grunden för Windows AI Foundry. Denna plattform gör det möjligt för utvecklare att skapa AI-drivna Windows-applikationer som utnyttjar hela spektrumet av PC-hårdvara.

### Plattformskapacitet
- Fungerar på alla Windows 11-datorer som kör version 24H2 (build 26100) eller senare
- Fungerar på all x64- och ARM64-PC-hårdvara, även datorer utan NPU:er eller GPU:er
- Gör det möjligt för utvecklare att använda sina egna modeller och distribuera dem effektivt över ekosystemet av kiselpartners, inklusive AMD, Intel, NVIDIA och Qualcomm, som spänner över CPU, GPU och NPU
- Genom att använda infrastruktur-API:er behöver utvecklare inte längre skapa flera versioner av sin app för att rikta in sig på olika kisel

### Fördelar för utvecklare
Windows ML abstraherar hårdvaran och exekveringsleverantörerna, så att du kan fokusera på att skriva din kod. Dessutom uppdateras Windows ML automatiskt för att stödja de senaste NPU:erna, GPU:erna och CPU:erna när de släpps. Plattformen tillhandahåller ett enhetligt ramverk för AI-utveckling över det mångsidiga Windows-hårdvaruekosystemet.

**Läs mer**: 
- [Windows ML Översikt](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Utvecklingsguide](../windowdeveloper.md) - Omfattande guide för Windows Edge AI-utveckling

## 5. EdgeAI med Foundry Local-applikationer

Foundry Local gör det möjligt för utvecklare att bygga Retrieval Augmented Generation (RAG)-applikationer med lokala resurser i .NET, genom att kombinera lokala språkmodeller med semantiska sökfunktioner. Detta tillvägagångssätt erbjuder integritetsfokuserade AI-lösningar som fungerar helt på lokal infrastruktur.

### Teknisk arkitektur
- Kombinerar Phi-3 språkmodell, lokala inbäddningar och Semantic Kernel för att skapa ett RAG-scenario
- Använder inbäddningar som vektorer (arrayer) av flyttal som representerar innehåll och dess semantiska betydelse
- Semantic Kernel fungerar som huvudorkestrator och integrerar Phi-3 och Smart Components för att skapa en sömlös RAG-pipeline
- Stöd för lokala vektordatabaser inklusive SQLite och Qdrant

### Implementeringsfördelar
RAG, eller Retrieval Augmented Generation, är bara ett finare sätt att säga "sök upp något och lägg till det i prompten". Denna lokala implementation säkerställer dataintegritet samtidigt som den ger intelligenta svar baserade på anpassade kunskapsbaser. Tillvägagångssättet är särskilt värdefullt för företagsmiljöer som kräver datasuveränitet och offlinekapacitet.

**Läs mer**: [Foundry Local RAG Exempel](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Windows EdgeAI Utvecklingsresurser

För utvecklare som specifikt riktar sig mot Windows-plattformen har vi skapat en omfattande guide som täcker hela Windows EdgeAI-ekosystemet. Denna resurs ger detaljerad information om Windows AI Foundry, inklusive API:er, verktyg och bästa praxis för EdgeAI-utveckling på Windows.

### Windows AI Foundry-plattform
Windows AI Foundry-plattformen erbjuder en omfattande uppsättning verktyg och API:er som är specifikt designade för Edge AI-utveckling på Windows-enheter. Detta inkluderar specialiserat stöd för NPU-accelererad hårdvara, Windows ML-integration och plattformsspecifika optimeringstekniker.

**Omfattande guide**: [Windows EdgeAI Utvecklingsguide](../windowdeveloper.md)

Denna guide täcker:
- Översikt och komponenter i Windows AI Foundry-plattformen
- Phi Silica API för effektiv inferens på NPU-hårdvara
- Datorvisions-API:er för bildbehandling och OCR
- Windows ML-runtime-integration och optimering
- Foundry Local CLI för lokal utveckling och testning
- Strategier för hårdvaruoptimering för Windows-enheter
- Praktiska implementeringsexempel och bästa praxis

### AI Toolkit för Edge AI-utveckling
För utvecklare som använder Visual Studio Code erbjuder AI Toolkit-tillägget en omfattande utvecklingsmiljö som är specifikt designad för att bygga, testa och distribuera Edge AI-applikationer. Detta verktyg förenklar hela Edge AI-utvecklingsarbetsflödet inom VS Code.

**Utvecklingsguide**: [AI Toolkit för Edge AI-utveckling](../aitoolkit.md)

AI Toolkit-guiden täcker:
- Modellupptäckt och urval för edge-distribution
- Lokala test- och optimeringsarbetsflöden
- ONNX- och Ollama-integration för edge-modeller
- Modellkonvertering och kvantiseringstekniker
- Agentutveckling för edge-scenarier
- Prestandautvärdering och övervakning
- Distributionsförberedelser och bästa praxis

## Slutsats

Dessa fem EdgeAI-implementationer visar mognaden och mångfalden av edge AI-lösningar som finns tillgängliga idag. Från hårdvaruaccelererade edge-enheter som Jetson Orin Nano till mjukvaruramverk som ONNX Runtime GenAI och Windows ML, har utvecklare oöverträffade möjligheter att distribuera intelligenta applikationer vid kanten.

Den gemensamma nämnaren för alla dessa plattformar är demokratiseringen av AI-kapaciteter, vilket gör sofistikerad maskininlärning tillgänglig för utvecklare med olika färdighetsnivåer och användningsfall. Oavsett om det handlar om att bygga mobila applikationer, skrivbordsprogram eller inbyggda system, erbjuder dessa EdgeAI-lösningar grunden för nästa generation av intelligenta applikationer som fungerar effektivt och privat vid kanten.

Varje plattform erbjuder unika fördelar: Jetson Orin Nano för hårdvaruaccelererad edge computing, ONNX Runtime GenAI för plattformsoberoende mobilutveckling, Azure EdgeAI för företagsintegration mellan moln och edge, Windows ML för Windows-inbyggda applikationer och Foundry Local för integritetsfokuserade RAG-implementationer. Tillsammans representerar de ett omfattande ekosystem för EdgeAI-utveckling.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.