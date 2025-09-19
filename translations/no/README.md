<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c817161ba08864340737d623f761b9ae",
  "translation_date": "2025-09-18T08:51:18+00:00",
  "source_file": "README.md",
  "language_code": "no"
}
-->
# EdgeAI for Nybegynnere

![Kurs forsidebilde](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.no.png)

Følg disse trinnene for å komme i gang med ressursene:

1. **Fork Repository**: Klikk [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klon Repository**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Bli med på Azure AI Foundry Discord og møt eksperter og andre utviklere**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Støtte for flere språk

#### Støttet via GitHub Action (Automatisk og alltid oppdatert)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](./README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

**Hvis du ønsker støtte for flere språk, finner du en liste over tilgjengelige språk [her](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Introduksjon

Velkommen til **EdgeAI for Nybegynnere** – din omfattende reise inn i den transformative verdenen av Edge Artificial Intelligence. Dette kurset bygger bro mellom kraftige AI-funksjoner og praktisk, virkelighetsnær implementering på edge-enheter, slik at du kan utnytte AI direkte der data genereres og beslutninger må tas.

### Hva du vil lære

Dette kurset tar deg fra grunnleggende konsepter til produksjonsklare implementeringer, og dekker:
- **Små språkmodeller (SLMs)** optimalisert for edge-implementering
- **Maskinvarebevisst optimalisering** på tvers av ulike plattformer
- **Sanntidsinferens** med personvernbevarende funksjoner
- **Produksjonsstrategier** for bedriftsapplikasjoner

### Hvorfor EdgeAI er viktig

Edge AI representerer et paradigmeskifte som adresserer kritiske moderne utfordringer:
- **Personvern og sikkerhet**: Behandle sensitive data lokalt uten eksponering til skyen
- **Sanntidsytelse**: Fjern nettverksforsinkelser for tidskritiske applikasjoner
- **Kostnadseffektivitet**: Reduser båndbredde og skyutgifter
- **Robuste operasjoner**: Oppretthold funksjonalitet under nettverksavbrudd
- **Regulatorisk samsvar**: Oppfyll krav til datasuverenitet

### Edge AI

Edge AI refererer til å kjøre AI-algoritmer og språkmodeller lokalt på maskinvare – nær der data genereres – uten å være avhengig av skyressurser for inferens. Det reduserer forsinkelser, forbedrer personvern og muliggjør sanntidsbeslutninger.

### Kjerneprinsipper:
- **På-enhet inferens**: AI-modeller kjører på edge-enheter (telefoner, rutere, mikrokontrollere, industrielle PC-er)
- **Offline-funksjonalitet**: Fungerer uten vedvarende internettforbindelse
- **Lav forsinkelse**: Umiddelbare responser egnet for sanntidssystemer
- **Datasuverenitet**: Holder sensitive data lokalt, forbedrer sikkerhet og samsvar

### Små språkmodeller (SLMs)

SLMs som Phi-4, Mistral-7B og Gemma er optimaliserte versjoner av større LLMs – trent eller destillert for:
- **Redusert minnebruk**: Effektiv bruk av begrenset minne på edge-enheter
- **Lavere beregningskrav**: Optimalisert for CPU og edge GPU-ytelse
- **Raskere oppstartstider**: Rask initialisering for responsive applikasjoner

De låser opp kraftige NLP-funksjoner samtidig som de møter begrensningene til:
- **Innebygde systemer**: IoT-enheter og industrielle kontrollere
- **Mobile enheter**: Smarttelefoner og nettbrett med offline-funksjonalitet
- **IoT-enheter**: Sensorer og smarte enheter med begrensede ressurser
- **Edge-servere**: Lokale behandlingsenheter med begrensede GPU-ressurser
- **Personlige datamaskiner**: Desktop- og laptop-implementeringsscenarier

## Kursarkitektur

### [Modul 01: EdgeAI Grunnleggende og Transformasjon](./Module01/README.md)
**Tema**: Den transformative endringen ved edge AI-implementering

#### Kapittelstruktur:
- [**Seksjon 1: EdgeAI Grunnleggende**](./Module01/01.EdgeAIFundamentals.md)
  - Sammenligning av tradisjonell sky-AI og edge-AI
  - Utfordringer og begrensninger ved edge computing
  - Nøkkelteknologier: modellkvantisering, kompresjonsoptimalisering, små språkmodeller (SLMs)
  - Maskinvareakselerasjon: NPUs, GPU-optimalisering, CPU-optimalisering
  - Fordeler: personvern, sikkerhet, lav forsinkelse, offline-funksjonalitet, kostnadseffektivitet

- [**Seksjon 2: Virkelige eksempler**](./Module01/02.RealWorldCaseStudies.md)
  - Microsoft Phi & Mu modelløkosystem
  - Japan Airlines AI-rapporteringssystem case study
  - Markedspåvirkning og fremtidige retninger
  - Implementeringshensyn og beste praksis

- [**Seksjon 3: Praktisk Implementeringsveiledning**](./Module01/03.PracticalImplementationGuide.md)
  - Oppsett av utviklingsmiljø (Python 3.10+, .NET 8+)
  - Maskinvarekrav og anbefalte konfigurasjoner
  - Ressurser for kjernefamilie-modeller
  - Kvantisering og optimaliseringsverktøy (Llama.cpp, Microsoft Olive, Apple MLX)
  - Sjekkliste for vurdering og verifisering

- [**Seksjon 4: Edge AI Implementeringsplattformer**](./Module01/04.EdgeDeployment.md)
  - Hensyn og krav for edge AI-implementering
  - Intel edge AI-maskinvare og optimaliseringsteknikker
  - Qualcomm AI-løsninger for mobile og innebygde systemer
  - NVIDIA Jetson og edge computing-plattformer
  - Windows AI PC-plattformer med NPU-akselerasjon
  - Maskinvare-spesifikke optimaliseringsstrategier

---

### [Modul 02: Grunnleggende for Små Språkmodeller](./Module02/README.md)
**Tema**: Teoretiske prinsipper, implementeringsstrategier og produksjonsimplementering for SLMs

#### Kapittelstruktur:
- [**Seksjon 1: Grunnleggende for Microsoft Phi Modellfamilie**](./Module02/01.PhiFamily.md)
  - Designfilosofiutvikling (Phi-1 til Phi-4)
  - Effektivitet-først arkitekturdesign
  - Spesialiserte funksjoner (resonnering, multimodalitet, edge-implementering)

- [**Seksjon 2: Grunnleggende for Qwen Modellfamilie**](./Module02/02.QwenFamily.md)
  - Åpen kildekode (Qwen 1.0 til Qwen3) - tilgjengelig via Hugging Face
  - Avansert resonneringsarkitektur med tenkemodus-funksjoner
  - Skalerbare implementeringsalternativer (0.5B-235B parametere)

- [**Seksjon 3: Grunnleggende for Gemma Modellfamilie**](./Module02/03.GemmaFamily.md)
  - Forskningsdrevet innovasjon (Gemma 3 & 3n)
  - Multimodalitet i verdensklasse
  - Mobil-først arkitektur

- [**Seksjon 4: Grunnleggende for BitNET Modellfamilie**](./Module02/04.BitNETFamily.md)
  - Revolusjonerende kvantiseringsteknologi (1.58-bit)
  - Spesialisert inferensrammeverk fra https://github.com/microsoft/BitNet
  - Bærekraftig AI-lederskap gjennom ekstrem effektivitet

- [**Seksjon 5: Grunnleggende for Microsoft Mu Modell**](./Module02/05.mumodel.md)
  - Enhets-først arkitektur innebygd i Windows 11
  - Systemintegrasjon med Windows 11-innstillinger
  - Personvernbevarende offline-funksjonalitet

- [**Seksjon 6: Grunnleggende for Phi-Silica**](./Module02/06.phisilica.md)
  - NPU-optimalisert arkitektur innebygd i Windows 11 Copilot+ PC-er
  - Eksepsjonell effektivitet (650 tokens/sekund ved 1.5W)
  - Utviklerintegrasjon med Windows App SDK

---

### [Modul 03: Implementering av Små Språkmodeller](./Module03/README.md)
**Tema**: Fullstendig livssyklus for SLM-implementering, fra teori til produksjonsmiljø

#### Kapittelstruktur:
- [**Seksjon 1: Avansert Læring for SLMs**](./Module03/01.SLMAdvancedLearning.md)
  - Parameterklassifiseringsrammeverk (Micro SLM 100M-1.4B, Medium SLM 14B-30B)
  - Avanserte optimaliseringsteknikker (kvantiseringsmetoder, BitNET 1-bit kvantisering)
  - Strategier for modellanskaffelse (Azure AI Foundry for Phi-modeller, Hugging Face for utvalgte modeller)

- [**Seksjon 2: Lokal Miljøimplementering**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Ollama universell plattformimplementering
  - Microsoft Foundry lokale bedriftsløsninger
  - Sammenligning av rammeverk

- [**Seksjon 3: Containerisert Skyimplementering**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM høyytelses inferensimplementering
  - Ollama containerorkestrering
  - ONNX Runtime edge-optimalisert implementering

---

### [Modul 04: Modellformatkonvertering og Kvantisering](./Module04/README.md)
**Tema**: Komplett verktøysett for modelloptimalisering for edge-implementering på tvers av plattformer

#### Kapittelstruktur:
- [**Seksjon 1: Grunnleggende for Modellformatkonvertering og Kvantisering**](./Module04/01.Introduce.md)
  - Presisjonsklassifiseringsrammeverk (ultra-lav, lav, medium presisjon)
  - GGUF og ONNX formatfordeler og bruksområder
  - Fordeler med kvantisering for operasjonell effektivitet
  - Ytelsesbenchmarker og sammenligninger av minnebruk
- [**Seksjon 2: Llama.cpp Implementeringsguide**](./Module04/02.Llamacpp.md)
  - Plattformuavhengig installasjon (Windows, macOS, Linux)
  - GGUF-formatkonvertering og kvantiseringsnivåer (Q2_K til Q8_0)
  - Maskinvareakselerasjon (CUDA, Metal, OpenCL, Vulkan)
  - Python-integrasjon og REST API-utplassering

- [**Seksjon 3: Microsoft Olive Optimaliseringssuite**](./Module04/03.MicrosoftOlive.md)
  - Maskinvarebevisst modelloptimalisering med over 40 innebygde komponenter
  - Auto-optimalisering med dynamisk og statisk kvantisering
  - Bedriftsintegrasjon med Azure ML-arbeidsflyter
  - Støtte for populære modeller (Llama, Phi, utvalgte Qwen-modeller, Gemma)

- [**Seksjon 4: OpenVINO Toolkit Optimaliseringssuite**](./Module04/04.openvino.md)
  - Intels åpen kildekode-verktøy for plattformuavhengig AI-utplassering
  - Neural Network Compression Framework (NNCF) for avansert optimalisering
  - OpenVINO GenAI for utplassering av store språkmodeller
  - Maskinvareakselerasjon på tvers av CPU, GPU, VPU og AI-akseleratorer

- [**Seksjon 5: Apple MLX Framework Dypdykk**](./Module04/05.AppleMLX.md)
  - Enhetlig minnearkitektur for Apple Silicon
  - Støtte for LLaMA, Mistral, Phi-3, utvalgte Qwen-modeller
  - LoRA finjustering og modelltilpasning
  - Hugging Face-integrasjon med 4-bit/8-bit kvantisering

- [**Seksjon 6: Edge AI Utviklingsarbeidsflyt-syntese**](./Module04/06.workflow-synthesis.md)
  - Enhetlig arbeidsflytarkitektur som integrerer flere optimaliseringsrammeverk
  - Beslutningstrær for rammeverksvalg og analyse av ytelseskonsekvenser
  - Validering av produksjonsklarhet og omfattende utplasseringsstrategier
  - Fremtidssikring for nye maskinvare- og modellarkitekturer

---

### [Modul 05: SLMOps - Operasjoner for små språkmodeller](./Module05/README.md)
**Tema**: Fullstendig livssyklus for små språkmodeller fra destillasjon til produksjonsutplassering

#### Kapittelstruktur:
- [**Seksjon 1: Introduksjon til SLMOps**](./Module05/01.IntroduceSLMOps.md)
  - SLMOps-paradigmeskifte innen AI-operasjoner
  - Kostnadseffektivitet og personvernfokusert arkitektur
  - Strategisk forretningspåvirkning og konkurransefordeler
  - Utfordringer og løsninger fra virkelige implementeringer

- [**Seksjon 2: Modelldestillasjon - Fra teori til praksis**](./Module05/02.SLMOps-Distillation.md)
  - Kunnskapsoverføring fra lærer- til studentmodeller
  - Implementering av totrinns destillasjonsprosess
  - Azure ML-destillasjonsarbeidsflyter med praktiske eksempler
  - 85 % reduksjon i inferenstid med 92 % nøyaktighetsbevaring

- [**Seksjon 3: Finjustering - Tilpasning av modeller for spesifikke oppgaver**](./Module05/03.SLMOps-Finetuing.md)
  - Parameter-effektive finjusteringsteknikker (PEFT)
  - Avanserte metoder som LoRA og QLoRA
  - Microsoft Olive-implementering for finjustering
  - Multi-adapter trening og hyperparameteroptimalisering

- [**Seksjon 4: Utplassering - Produksjonsklar implementering**](./Module05/04.SLMOps.Deployment.md)
  - Modellkonvertering og kvantisering for produksjon
  - Foundry Local-konfigurasjon for utplassering
  - Ytelsesbenchmarking og kvalitetsvalidering
  - 75 % størrelsesreduksjon med produksjonsovervåking

---

### [Modul 06: SLM Agentiske Systemer - AI-agenter og funksjonskalling](./Module06/README.md)
**Tema**: Implementering av SLM-agentiske systemer fra grunnleggende funksjonskalling til avansert Model Context Protocol-integrasjon

#### Kapittelstruktur:
- [**Seksjon 1: AI-agenter og små språkmodellers grunnlag**](./Module06/01.IntroduceAgent.md)
  - Rammeverk for agentklassifisering (refleks, modellbasert, målbasert, læringsagenter)
  - SLM-grunnleggende og optimaliseringsstrategier (GGUF, kvantisering, edge-rammeverk)
  - Analyse av SLM vs LLM (10-30× kostnadsreduksjon, 70-80 % oppgaveeffektivitet)
  - Praktisk utplassering med Ollama, VLLM og Microsoft edge-løsninger

- [**Seksjon 2: Funksjonskalling i små språkmodeller**](./Module06/02.FunctionCalling.md)
  - Systematisk arbeidsflytimplementering (intensjonsdeteksjon, JSON-utdata, ekstern utførelse)
  - Plattformspesifikke implementeringer (Phi-4-mini, utvalgte Qwen-modeller, Microsoft Foundry Local)
  - Avanserte eksempler (samarbeid mellom flere agenter, dynamisk verktøyvalg)
  - Produksjonsbetraktninger (ratebegrensning, revisjonslogging, sikkerhetstiltak)

- [**Seksjon 3: Model Context Protocol (MCP) Integrasjon**](./Module06/03.IntroduceMCP.md)
  - Protokollarkitektur og lagdelt systemdesign
  - Støtte for flere backend-løsninger (Ollama for utvikling, vLLM for produksjon)
  - Tilkoblingsprotokoller (STDIO og SSE-modus)
  - Virkelige applikasjoner (webautomatisering, databehandling, API-integrasjon)

---

### [Modul 07: EdgeAI Implementeringsprøver](./Module07/README.md)
**Tema**: Omfattende EdgeAI-implementeringer på tvers av ulike plattformer og rammeverk

#### Kapittelstruktur:
- [**AI-verktøysett for Visual Studio Code**](./Module07/aitoolkit.md)
  - Omfattende Edge AI-utviklingsmiljø i VS Code
  - Modellkatalog og oppdagelse for edge-utplassering
  - Lokal testing, optimalisering og agentutviklingsarbeidsflyter
  - Ytelsesovervåking og evaluering for edge-scenarier

- [**Windows EdgeAI Utviklingsguide**](./Module07/windowdeveloper.md)
  - Omfattende oversikt over Windows AI Foundry-plattformen
  - Phi Silica API for effektiv NPU-inferens
  - Computer Vision API-er for bildebehandling og OCR
  - Foundry Local CLI for lokal utvikling og testing

- [**EdgeAI i NVIDIA Jetson Orin Nano**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 67 TOPS AI-ytelse i kredittkortstørrelse
  - Støtte for generative AI-modeller (visuelle transformatorer, LLM-er, visuell-språkmodeller)
  - Applikasjoner innen robotikk, droner, intelligente kameraer, autonome enheter
  - Rimelig plattform til $249 for demokratisert AI-utvikling

- [**EdgeAI i mobilapplikasjoner med .NET MAUI og ONNX Runtime GenAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - Plattformuavhengig mobil AI med én C#-kodebase
  - Støtte for maskinvareakselerasjon (CPU, GPU, mobile AI-prosessorer)
  - Plattformspesifikke optimaliseringer (CoreML for iOS, NNAPI for Android)
  - Fullstendig generativ AI-loop-implementering

- [**EdgeAI i Azure med Small Language Models Engine**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - Hybrid utplasseringsarkitektur for sky-edge
  - Integrasjon av Azure AI-tjenester med ONNX Runtime
  - Bedriftsomfattende utplassering og kontinuerlig modelladministrasjon
  - Hybrid AI-arbeidsflyter for intelligent dokumentbehandling

- [**EdgeAI med Windows ML**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Windows AI Foundry-grunnlag for effektiv inferens på enheten
  - Universell maskinvarestøtte (AMD, Intel, NVIDIA, Qualcomm-silikon)
  - Automatisk maskinvareabstraksjon og optimalisering
  - Enhetlig rammeverk for mangfoldig Windows-maskinvareøkosystem

- [**EdgeAI med Foundry Local-applikasjoner**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - Personvernfokusert RAG-implementering med lokale ressurser
  - Phi-3 språkmodellintegrasjon med semantisk søk (kun Phi-modeller)
  - Støtte for lokale vektordatabaser (SQLite, Qdrant)
  - Datasuverenitet og offline operasjonsmuligheter

## Kursmål

Ved å fullføre dette omfattende EdgeAI-kurset, vil du utvikle ekspertise i å designe, implementere og utplassere produksjonsklare EdgeAI-løsninger. Vår strukturerte tilnærming sikrer at du mestrer både teoretiske grunnlag og praktiske implementeringsferdigheter.

### Tekniske ferdigheter

**Grunnleggende kunnskap**
- Forstå de grunnleggende forskjellene mellom skybaserte og edge-baserte AI-arkitekturer
- Mestre prinsippene for modellkvantisering, komprimering og optimalisering for ressursbegrensede miljøer
- Forstå alternativer for maskinvareakselerasjon (NPUs, GPUs, CPUs) og deres utplasseringsimplikasjoner

**Implementeringsferdigheter**
- Utplassere små språkmodeller på tvers av ulike edge-plattformer (mobil, innebygd, IoT, edge-servere)
- Bruke optimaliseringsrammeverk som Llama.cpp, Microsoft Olive, ONNX Runtime og Apple MLX
- Implementere sanntids inferenssystemer med krav om sub-sekund respons

**Produksjonsekspertise**
- Designe skalerbare EdgeAI-arkitekturer for bedriftsapplikasjoner
- Implementere overvåking, vedlikehold og oppdateringsstrategier for utplasserte systemer
- Bruke sikkerhetspraksis for personvernbevarende EdgeAI-implementeringer

### Strategiske evner

**Beslutningsrammeverk**
- Evaluere EdgeAI-muligheter og identifisere passende bruksområder for forretningsapplikasjoner
- Vurdere avveininger mellom modellnøyaktighet, inferenshastighet, strømforbruk og maskinvarekostnader
- Velge passende SLM-familier og konfigurasjoner basert på spesifikke utplasseringsbegrensninger

**Systemarkitektur**
- Designe ende-til-ende EdgeAI-løsninger som integreres med eksisterende infrastruktur
- Planlegge hybrid edge-sky-arkitekturer for optimal ytelse og kostnadseffektivitet
- Implementere dataflyt og behandlingspipelines for sanntids AI-applikasjoner

### Bransjeapplikasjoner

**Praktiske utplasseringsscenarier**
- **Produksjon**: Kvalitetskontrollsystemer, prediktivt vedlikehold og prosessoptimalisering
- **Helsevesen**: Personvernbevarende diagnostiske verktøy og pasientovervåkingssystemer
- **Transport**: Beslutningstaking for autonome kjøretøy og trafikkstyring
- **Smarte byer**: Intelligente infrastrukturer og ressursstyringssystemer
- **Forbrukerelektronikk**: AI-drevne mobilapplikasjoner og smarthusenheter

## Oversikt over læringsutbytte

### Modul 01 Læringsutbytte:
- Forstå de grunnleggende forskjellene mellom sky- og edge AI-arkitekturer
- Mestre kjerneoptimaliseringsteknikker for edge-utplassering
- Gjenkjenne virkelige applikasjoner og suksesshistorier
- Tilegne seg praktiske ferdigheter for implementering av EdgeAI-løsninger

### Modul 02 Læringsutbytte:
- Dyp forståelse av ulike SLM-designfilosofier og deres utplasseringsimplikasjoner
- Mestre strategiske beslutningsevner basert på beregningsbegrensninger og ytelseskrav
- Forstå fleksibilitetsavveininger ved utplassering
- Besitte fremtidsrettede innsikter i effektiv AI-arkitektur

### Modul 03 Læringsutbytte:
- Strategiske evner for modellvalg
- Mestre optimaliseringsteknikker
- Mestre fleksibilitet ved utplassering
- Produksjonsklare konfigurasjonsevner

### Modul 04 Læringsutbytte:
- Dyp forståelse av kvantiseringsgrenser og praktiske applikasjoner
- Praktisk erfaring med flere optimaliseringsrammeverk (Llama.cpp, Olive, OpenVINO, MLX)
- Mestre Intel-maskinvareoptimalisering med OpenVINO og NNCF
- Evner til maskinvarebevisst optimalisering på tvers av ulike plattformer
- Produksjonsutplasseringsferdigheter for plattformuavhengige edge computing-miljøer
- Strategisk rammeverksvalg og arbeidsflytsyntese for optimale EdgeAI-løsninger

### Modul 05 Læringsutbytte:
- Mestre SLMOps-paradigmet og operasjonsprinsipper
- Implementere modelldestillasjon for kunnskapsoverføring og effektivitetsoptimalisering
- Bruke finjusteringsteknikker for domenespesifikk modelltilpasning
- Utplassere produksjonsklare SLM-løsninger med overvåkings- og vedlikeholdsstrategier

### Modul 06 Læringsutbytte:
- Forstå grunnleggende konsepter for AI-agenter og små språkmodellers arkitektur
- Mestre funksjonskallimplementering på tvers av flere plattformer og rammeverk
- Integrere Model Context Protocol (MCP) for standardisert ekstern verktøysinteraksjon
- Bygge sofistikerte agentiske systemer med minimal menneskelig intervensjon

### Modul 07 Læringsutbytte:
- Mestre AI-verktøysett for Visual Studio Code for omfattende EdgeAI-utviklingsarbeidsflyter
- Tilegne seg ekspertise i Windows AI Foundry-plattformen og NPU-optimaliseringsstrategier
- Få praktisk erfaring med ulike EdgeAI-plattformer og implementeringsstrategier
- Mestre maskinvare-spesifikke optimaliseringsteknikker på tvers av NVIDIA, mobil, Azure og Windows-plattformer
- Forstå utplasseringsavveininger mellom ytelse, kostnad og personvernkrav
- Utvikle praktiske ferdigheter for å bygge virkelige EdgeAI-applikasjoner på tvers av ulike økosystemer

## Forventede kursresultater

Ved vellykket fullføring av dette kurset vil du være utstyrt med kunnskap, ferdigheter og selvtillit til å lede EdgeAI-initiativer i profesjonelle miljøer.

### Profesjonell beredskap

**Teknisk lederskap**
- **Løsningsarkitektur**: Designe omfattende EdgeAI-systemer som oppfyller bedriftskrav
- **Ytelsesoptimalisering**: Oppnå optimal balanse mellom nøyaktighet, hastighet og ressursforbruk
- **Plattformuavhengig utplassering**: Implementere løsninger på tvers av Windows, Linux, mobil og innebygde plattformer
- **Produksjonsoperasjoner**: Vedlikeholde og skalere EdgeAI-systemer med bedriftsgrad pålitelighet

**Bransjeekspertise**
- **Teknologivurdering**: Vurdere og anbefale EdgeAI-løsninger for spesifikke forretningsutfordringer
- **Implementeringsplanlegging**: Utvikle realistiske tidslinjer og ressurskrav for EdgeAI-prosjekter
- **Risikostyring**: Identifisere og redusere tekniske og operasjonelle risikoer i EdgeAI-utplasseringer
- **ROI-optimalisering**: Demonstrere målbar forretningsverdi fra EdgeAI-implementeringer

### Karriereutviklingsmuligheter

**Profesjonelle roller**
- EdgeAI-løsningsarkitekt
- Maskinlæringsingeniør (Edge-spesialisering)
- IoT AI-utvikler
- Mobil AI-applikasjonsutvikler
- Bedrifts AI-konsulent

**Bransjesektorer**
- Smart produksjon og Industri 4.0
- Autonome kjøretøy og transport
- Helsevesenteknologi og medisinske enheter
- Finansteknologi og sikkerhet
- Forbrukerelektronikk og mobilapplikasjoner

### Sertifisering og validering

**Porteføljeutvikling**
- Fullføre ende-til-ende EdgeAI-prosjekter som demonstrerer praktisk kompetanse
- Utplassere produksjonsklare løsninger på tvers av flere maskinvareplattformer
- Dokumentere optimaliseringsstrategier og ytelsesforbedringer oppnådd

**Kontinuerlig læringsvei**
- Grunnlag for avan
Denne kursen plasserer deg i frontlinjen av AI-teknologiutvikling, der intelligente funksjoner sømløst integreres i enhetene og systemene som driver det moderne livet.

## Filstruktur Tre-diagram

```
edgeai-for-beginners/
├── imgs/
│   └── cover.png
├── Module01/ (EdgeAI Fundamentals and Transformation)
│   ├── 01.EdgeAIFundamentals.md
│   ├── 02.RealWorldCaseStudies.md
│   ├── 03.PracticalImplementationGuide.md
│   ├── 04.EdgeDeployment.md
│   └── README.md
├── Module02/ (Small Language Model Foundations)
│   ├── 01.PhiFamily.md
│   ├── 02.QwenFamily.md
│   ├── 03.GemmaFamily.md
│   ├── 04.BitNETFamily.md
│   ├── 05.mumodel.md
│   ├── 06.phisilica.md
│   └── README.md
├── Module03/ (SLM Deployment Practice)
│   ├── 01.SLMAdvancedLearning.md
│   ├── 02.DeployingSLMinLocalEnv.md
│   ├── 03.DeployingSLMinCloud.md
│   └── README.md
├── Module04/ (Model Format Conversion and Quantization)
│   ├── 01.Introduce.md
│   ├── 02.Llamacpp.md
│   ├── 03.MicrosoftOlive.md
│   ├── 04.openvino.md
│   ├── 05.AppleMLX.md
│   ├── 06.workflow-synthesis.md
│   └── README.md
├── Module05/ (SLMOps - Small Language Model Operations)
│   ├── 01.IntroduceSLMOps.md
│   ├── 02.SLMOps-Distillation.md
│   ├── 03.SLMOps-Finetuing.md
│   ├── 04.SLMOps.Deployment.md
│   └── README.md
├── Module06/ (SLM Agentic Systems)
│   ├── 01.IntroduceAgent.md
│   ├── 02.FunctionCalling.md
│   ├── 03.IntroduceMCP.md
│   └── README.md
├── Module07/ (EdgeAI Implementation Samples)
│   ├── aitoolkit.md
│   ├── windowdeveloper.md
│   └── README.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md (This file)
├── SECURITY.md
├── STUDY_GUIDE.md
└── SUPPORT.md
```

## Kursfunksjoner

- **Progressiv læring**: Gradvis utvikling fra grunnleggende konsepter til avansert implementering
- **Integrasjon av teori og praksis**: Hvert modul inneholder både teoretiske grunnlag og praktiske operasjoner
- **Reelle casestudier**: Basert på faktiske eksempler fra Microsoft, Alibaba, Google og andre
- **Praktisk erfaring**: Fullfør konfigurasjonsfiler, API-testprosedyrer og implementeringsskript
- **Ytelsesbenchmarking**: Detaljerte sammenligninger av inferenshastighet, minnebruk og ressurskrav
- **Bedriftsnivå hensyn**: Sikkerhetspraksis, samsvarsrammeverk og strategier for databeskyttelse

## Komme i gang

Anbefalt læringssti:
1. Start med **Module01** for å bygge en grunnleggende forståelse av EdgeAI
2. Fortsett til **Module02** for å få dyp innsikt i ulike SLM-modellfamilier
3. Lær **Module03** for å mestre praktiske implementeringsferdigheter
4. Fortsett med **Module04** for avansert modelloptimalisering, formatkonvertering og rammeverkssyntese
5. Fullfør **Module05** for å mestre SLMOps for produksjonsklare implementeringer
6. Utforsk **Module06** for å forstå SLM-agentiske systemer og funksjonskallmuligheter
7. Avslutt med **Module07** for å få praktisk erfaring med AI Toolkit og ulike EdgeAI-implementeringseksempler

Hver modul er designet for å være selvstendig komplett, men sekvensiell læring vil gi de beste resultatene.

## Studieveiledning

En omfattende [Studieveiledning](STUDY_GUIDE.md) er tilgjengelig for å hjelpe deg med å maksimere din læringsopplevelse. Studieveiledningen gir:

- **Strukturerte læringsstier**: Optimaliserte tidsplaner for å fullføre kurset på 20 timer
- **Veiledning for tidsfordeling**: Spesifikke anbefalinger for å balansere lesing, øvelser og prosjekter
- **Fokus på nøkkelkonsepter**: Prioriterte læringsmål for hver modul
- **Selvvurderingsverktøy**: Spørsmål og øvelser for å teste din forståelse
- **Ideer til miniprosjekter**: Praktiske applikasjoner for å styrke læringen din

Studieveiledningen er designet for å imøtekomme både intensiv læring (1 uke) og deltidsstudier (3 uker), med klare retningslinjer for hvordan du effektivt kan fordele tiden din, selv om du bare kan dedikere 10 timer til kurset.

---

**Fremtiden for EdgeAI ligger i kontinuerlig forbedring av modellarkitekturer, kvantiseringsteknikker og implementeringsstrategier som prioriterer effektivitet og spesialisering fremfor generelle funksjoner. Organisasjoner som omfavner dette paradigmeskiftet vil være godt posisjonert til å utnytte AI's transformative potensial samtidig som de opprettholder kontroll over sine data og operasjoner.**

## Andre kurs

Vårt team produserer andre kurs! Sjekk ut:

- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents For Beginners](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [Generative AI for Beginners using JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML for Beginners](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [Data Science for Beginners](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI for Beginners](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT for Beginners](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR Development for Beginners](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Mastering GitHub Copilot for AI Paired Programming](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [Mastering GitHub Copilot for C#/.NET Developers](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [Choose Your Own Copilot Adventure](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.