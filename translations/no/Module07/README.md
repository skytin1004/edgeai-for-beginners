<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-18T10:47:10+00:00",
  "source_file": "Module07/README.md",
  "language_code": "no"
}
-->
# Kapittel 07: EdgeAI Eksempler

Edge AI representerer sammensmeltingen av kunstig intelligens med edge computing, som muliggjør intelligent prosessering direkte på enheter uten behov for skytilkobling. Dette kapittelet utforsker fem ulike EdgeAI-implementeringer på forskjellige plattformer og rammeverk, og viser frem allsidigheten og kraften ved å kjøre AI-modeller på kanten.

## 1. EdgeAI på NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano representerer et gjennombrudd innen tilgjengelig edge AI-computing, med opptil 67 TOPS AI-ytelse i et kompakt format på størrelse med et kredittkort. Denne kraftige edge AI-plattformen demokratiserer utviklingen av generativ AI for hobbyister, studenter og profesjonelle utviklere.

### Hovedfunksjoner
- Leverer opptil 67 TOPS AI-ytelse—en 1,7X forbedring sammenlignet med forgjengeren
- 1024 CUDA-kjerner og opptil 32 Tensor-kjerner for AI-prosessering
- 6-kjerners Arm Cortex-A78AE v8.2 64-bit CPU med maksimal frekvens på 1,5 GHz
- Priset til kun $249, og gir utviklere, studenter og skapere den mest tilgjengelige plattformen

### Bruksområder
Jetson Orin Nano utmerker seg ved å kjøre moderne generative AI-modeller, inkludert vision transformers, store språkmodeller og vision-language-modeller. Den er spesielt designet for GenAI-brukstilfeller, og nå kan du kjøre flere LLM-er på en håndholdt enhet. Populære bruksområder inkluderer AI-drevne roboter, smarte droner, intelligente kameraer og autonome edge-enheter.

**Les mer**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI i mobilapplikasjoner med .NET MAUI og ONNX Runtime GenAI

Denne løsningen viser hvordan man kan integrere Generativ AI og Store Språkmodeller (LLMs) i plattformuavhengige mobilapplikasjoner ved hjelp av .NET MAUI (Multi-platform App UI) og ONNX Runtime GenAI. Denne tilnærmingen gjør det mulig for .NET-utviklere å bygge avanserte AI-drevne mobilapplikasjoner som kjører lokalt på Android- og iOS-enheter.

### Hovedfunksjoner
- Bygget på .NET MAUI-rammeverket, som gir én kodebase for både Android- og iOS-applikasjoner
- ONNX Runtime GenAI-integrasjon muliggjør kjøring av generative AI-modeller direkte på mobile enheter
- Støtter ulike maskinvareakseleratorer tilpasset mobile enheter, inkludert CPU, GPU og spesialiserte mobile AI-prosessorer
- Plattformspesifikke optimaliseringer som CoreML for iOS og NNAPI for Android via ONNX Runtime
- Implementerer hele generativ AI-syklusen, inkludert pre- og postprosessering, inferens, logits-prosessering, søk og sampling, og KV-cache-håndtering

### Fordeler for utvikling
.NET MAUI-tilnærmingen lar utviklere utnytte sine eksisterende C#- og .NET-ferdigheter mens de bygger plattformuavhengige AI-applikasjoner. ONNX Runtime GenAI-rammeverket støtter flere modellarkitekturer, inkludert Llama, Mistral, Phi, Gemma og mange andre. Optimaliserte ARM64-kjerner akselererer INT4-kvantisert matriksmultiplikasjon, og sikrer effektiv ytelse på mobil maskinvare samtidig som den velkjente .NET-utviklingsopplevelsen opprettholdes.

### Bruksområder
Denne løsningen er ideell for utviklere som ønsker å bygge AI-drevne mobilapplikasjoner ved hjelp av .NET-teknologier, inkludert intelligente chatbots, bildegjenkjenningsapper, språköversettelsesverktøy og personlige anbefalingssystemer som kjører helt lokalt for forbedret personvern og offline-funksjonalitet.

**Les mer**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI i Azure med Small Language Models Engine

Microsofts Azure-baserte EdgeAI-løsning fokuserer på effektiv distribusjon av Small Language Models (SLMs) i sky-edge hybride miljøer. Denne tilnærmingen bygger bro mellom AI-tjenester i skyen og kravene til edge-distribusjon.

### Arkitekturegenskaper
- Sømløs integrasjon med Azure AI-tjenester
- Kjører SLMs/LLMs og multimodale modeller på enheter og i skyen med ONNX Runtime
- Optimalisert for distribusjon i stor skala for bedrifter
- Støtte for kontinuerlige modelloppdateringer og administrasjon

### Bruksområder
Azure EdgeAI-implementeringen utmerker seg i scenarier som krever AI-distribusjon i bedriftsklasse med skyadministrasjonsmuligheter. Dette inkluderer intelligent dokumentbehandling, sanntidsanalyse og hybride AI-arbeidsflyter som utnytter både sky- og edge computing-ressurser.

**Les mer**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI med Windows ML

Windows ML representerer Microsofts avanserte runtime, optimalisert for effektiv modellinferens på enheter og forenklet distribusjon, og fungerer som grunnlaget for Windows AI Foundry. Denne plattformen gjør det mulig for utviklere å lage AI-drevne Windows-applikasjoner som utnytter hele spekteret av PC-maskinvare.

### Plattformfunksjoner
- Fungerer på alle Windows 11-PC-er som kjører versjon 24H2 (build 26100) eller nyere
- Fungerer på all x64- og ARM64-PC-maskinvare, selv PC-er uten NPUs eller GPUs
- Lar utviklere ta med sine egne modeller og distribuere dem effektivt på tvers av silisiumpartnerøkosystemet, inkludert AMD, Intel, NVIDIA og Qualcomm, som spenner over CPU, GPU, NPU
- Ved å bruke infrastruktur-API-er trenger utviklere ikke lenger å lage flere versjoner av appen for å målrette mot forskjellige silisiumtyper

### Fordeler for utviklere
Windows ML abstraherer maskinvaren og utførelsesleverandørene, slik at du kan fokusere på å skrive koden din. I tillegg oppdateres Windows ML automatisk for å støtte de nyeste NPUs, GPUs og CPUs etter hvert som de lanseres. Plattformen gir et enhetlig rammeverk for AI-utvikling på tvers av det mangfoldige Windows-maskinvareøkosystemet.

**Les mer**: 
- [Windows ML Oversikt](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Utviklingsguide](../windowdeveloper.md) - Omfattende guide for Windows Edge AI-utvikling

## 5. EdgeAI med Foundry Local Applikasjoner

Foundry Local gjør det mulig for utviklere å bygge Retrieval Augmented Generation (RAG)-applikasjoner ved hjelp av lokale ressurser i .NET, og kombinerer lokale språkmodeller med semantiske søkefunksjoner. Denne tilnærmingen gir personvernfokuserte AI-løsninger som opererer helt på lokal infrastruktur.

### Teknisk arkitektur
- Kombinerer Phi-3 språkmodell, lokale embeddings og Semantic Kernel for å skape et RAG-scenario
- Bruker embeddings som vektorer (arrays) av flyttallsverdier som representerer innhold og dets semantiske betydning
- Semantic Kernel fungerer som hovedorkestrator, og integrerer Phi-3 og smarte komponenter for å skape en sømløs RAG-pipeline
- Støtte for lokale vektordatabaser, inkludert SQLite og Qdrant

### Implementeringsfordeler
RAG, eller Retrieval Augmented Generation, er bare en fancy måte å si "slå opp noe og legg det inn i prompten". Denne lokale implementeringen sikrer dataprivacy samtidig som den gir intelligente svar basert på tilpassede kunnskapsbaser. Tilnærmingen er spesielt verdifull for bedriftsmiljøer som krever datasuverenitet og offline-funksjonalitet.

**Les mer**: [Foundry Local RAG Eksempler](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Windows EdgeAI Utviklingsressurser

For utviklere som spesifikt retter seg mot Windows-plattformen, har vi laget en omfattende guide som dekker hele Windows EdgeAI-økosystemet. Denne ressursen gir detaljert informasjon om Windows AI Foundry, inkludert API-er, verktøy og beste praksis for EdgeAI-utvikling på Windows.

### Windows AI Foundry Plattform
Windows AI Foundry-plattformen gir et omfattende sett med verktøy og API-er spesielt designet for Edge AI-utvikling på Windows-enheter. Dette inkluderer spesialisert støtte for NPU-akselerert maskinvare, Windows ML-integrasjon og plattformspesifikke optimaliseringsteknikker.

**Omfattende guide**: [Windows EdgeAI Utviklingsguide](../windowdeveloper.md)

Denne guiden dekker:
- Oversikt over Windows AI Foundry-plattformen og komponenter
- Phi Silica API for effektiv inferens på NPU-maskinvare
- Computer Vision API-er for bildebehandling og OCR
- Windows ML runtime-integrasjon og optimalisering
- Foundry Local CLI for lokal utvikling og testing
- Maskinvareoptimaliseringsstrategier for Windows-enheter
- Praktiske implementeringseksempler og beste praksis

### AI Toolkit for Edge AI Utvikling
For utviklere som bruker Visual Studio Code, gir AI Toolkit-utvidelsen et omfattende utviklingsmiljø spesielt designet for å bygge, teste og distribuere Edge AI-applikasjoner. Dette verktøyet strømlinjeformer hele Edge AI-utviklingsarbeidsflyten innenfor VS Code.

**Utviklingsguide**: [AI Toolkit for Edge AI Utvikling](../aitoolkit.md)

AI Toolkit-guiden dekker:
- Modelloppdagelse og valg for edge-distribusjon
- Lokale test- og optimaliseringsarbeidsflyter
- ONNX og Ollama-integrasjon for edge-modeller
- Modellkonvertering og kvantiseringsteknikker
- Agentutvikling for edge-scenarier
- Ytelsesevaluering og overvåking
- Distribusjonsforberedelse og beste praksis

## Konklusjon

Disse fem EdgeAI-implementeringene viser modenheten og mangfoldet av edge AI-løsninger som er tilgjengelige i dag. Fra maskinvareakselererte edge-enheter som Jetson Orin Nano til programvarerammer som ONNX Runtime GenAI og Windows ML, har utviklere enestående muligheter for å distribuere intelligente applikasjoner på kanten.

Den røde tråden på tvers av alle disse plattformene er demokratiseringen av AI-funksjoner, som gjør avansert maskinlæring tilgjengelig for utviklere på tvers av ulike ferdighetsnivåer og bruksområder. Enten du bygger mobilapplikasjoner, skrivebordsprogramvare eller innebygde systemer, gir disse EdgeAI-løsningene grunnlaget for neste generasjons intelligente applikasjoner som opererer effektivt og privat på kanten.

Hver plattform tilbyr unike fordeler: Jetson Orin Nano for maskinvareakselerert edge computing, ONNX Runtime GenAI for plattformuavhengig mobilutvikling, Azure EdgeAI for bedriftsintegrasjon mellom sky og edge, Windows ML for Windows-native applikasjoner, og Foundry Local for personvernfokuserte RAG-implementeringer. Sammen representerer de et omfattende økosystem for EdgeAI-utvikling.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.