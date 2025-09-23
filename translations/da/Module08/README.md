<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T20:19:13+00:00",
  "source_file": "Module08/README.md",
  "language_code": "da"
}
-->
# Modul 08: Hands-on med Microsoft Foundry Local - Komplet udviklerværktøjssæt

## Oversigt

Microsoft Foundry Local repræsenterer den næste generation af edge AI-udvikling og giver udviklere kraftfulde værktøjer til at bygge, implementere og skalere AI-applikationer lokalt, samtidig med at der opretholdes problemfri integration med Azure AI Foundry. Dette modul dækker Foundry Local fra installation til avanceret agentudvikling.

**Nøgleteknologier:**
- Microsoft Foundry Local CLI og SDK
- Azure AI Foundry integration
- Modelinference på enheden
- Lokal modelcaching og optimering
- Agentbaserede arkitekturer

## Modul læringsmål

Ved at gennemføre dette modul vil du:

- **Beherske Foundry Local opsætning**: Installere, konfigurere og optimere Foundry Local til udvikling på Windows 11
- **Implementere forskellige modeller**: Køre phi-, qwen-, deepseek- og GPT-OSS-20B-modeller lokalt med CLI-kommandoer
- **Bygge produktionsløsninger**: Skabe AI-applikationer med avanceret prompt engineering og dataintegration
- **Udnytte open source-økosystemet**: Integrere Hugging Face-modeller og bidrag fra fællesskabet
- **Sammenligne AI-arkitekturer**: Forstå fordele og ulemper ved LLMs vs SLMs og implementeringsstrategier
- **Udvikle AI-agenter**: Bygge intelligente agenter ved hjælp af Foundry Locals arkitektur og grounding-funktioner
- **Implementere modeller som værktøjer**: Skabe modulære, tilpasselige AI-løsninger til virksomhedsapplikationer

## Sessionstruktur

### [1: Kom godt i gang med Foundry Local](./01.FoundryLocalSetup.md)
**Fokus**: Installation, CLI-opsætning, modelcaching og hardwareacceleration

**Hvad du lærer:**
- Fuldføre Foundry Local installation på Windows 11
- CLI-konfiguration og kommandostruktur
- Strategier for modelcaching for optimal ydeevne
- Opsætning og optimering af hardwareacceleration
- Praktisk implementering af phi-, qwen-, deepseek- og GPT-OSS-20B-modeller

**Varighed**: 2-3 timer  
**Forudsætninger**: Windows 11, grundlæggende kendskab til kommandolinjen

---

### [2: Byg AI-løsninger med Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Fokus**: Avanceret prompt engineering, dataintegration og handlingsorienterede opgaver

**Hvad du lærer:**
- Avancerede teknikker inden for prompt engineering
- Mønstre og bedste praksis for dataintegration
- Bygge handlingsorienterede AI-opgaver med Foundry Local
- Problemfri workflows for integration med Azure AI Foundry
- Optimering af ydeevne og overvågning

**Varighed**: 2-3 timer  
**Forudsætninger**: Session 1 fuldført, Azure-konto (valgfrit)

---

### [3: Open Source-modeller i Foundry Local](./03.OpenSourceModels.md)
**Fokus**: Hugging Face-integration, strategier for modelvalg og bidrag fra fællesskabet

**Hvad du lærer:**
- Hugging Face-modelintegration med Foundry Local
- Strategier og implementering af "Bring-your-own-model" (BYOM)
- Indsigt fra Model Mondays-serien og bidrag fra fællesskabet
- Tilpasset modelimplementering og optimering
- Evaluering og udvælgelseskriterier for fællesskabsmodeller

**Varighed**: 2-3 timer  
**Forudsætninger**: Session 1-2 fuldført, Hugging Face-konto

---

### [4: Udforsk avancerede modeller - LLMs, SLMs og inference på enheden](./04.CuttingEdgeModels.md)
**Fokus**: Model-sammenligning, EdgeAI med Phi og ONNX Runtime, avancerede demoer

**Hvad du lærer:**
- Omfattende sammenligning af LLMs vs SLMs og anvendelsesscenarier
- Afvejninger mellem lokal og cloud-inference og beslutningsrammer
- EdgeAI-implementering med Phi og ONNX Runtime
- Udvikling og implementering af Chainlit RAG Chat App
- Optimeringsteknikker for WebGPU-inference
- Integration og funktioner i AI PC SDK

**Varighed**: 3-4 timer  
**Forudsætninger**: Session 1-3 fuldført, forståelse af inference-konceptet

---

### [5: Byg AI-drevne agenter hurtigt med Foundry Local](./05.AIPoweredAgents.md)
**Fokus**: Hurtig udvikling af GenAI-apps, systemprompter, grounding og agentarkitekturer

**Hvad du lærer:**
- Foundry Locals agentarkitektur og designmønstre
- Systemprompt engineering for agentadfærd
- Grounding-teknikker for pålidelige agentrespons
- Arbejdsflows for hurtig udvikling af GenAI-applikationer
- Orkestrering af agenter og systemer med flere agenter
- Produktionsimplementeringsstrategier for AI-agenter

**Varighed**: 3-4 timer  
**Forudsætninger**: Session 1-4 fuldført, grundlæggende forståelse af AI-agenter

---

### [6: Foundry Local - Modeller som værktøjer](./06.ModelsAsTools.md)
**Fokus**: Modulære AI-løsninger, implementering på enheden og skalering til virksomheder

**Hvad du lærer:**
- Behandle AI-modeller som modulære, tilpasselige værktøjer
- Implementering på enheden uden afhængighed af cloud
- Lav-latens, omkostningseffektiv og privatlivsbevarende inference
- Mønstre for integration af SDK, API og CLI
- Tilpasning af modeller til specifikke anvendelsesscenarier
- Skalering fra lokale prototyper til Azure AI Foundry
- Virksomhedsklare AI-applikationsarkitekturer

**Varighed**: 3-4 timer  
**Forudsætninger**: Alle tidligere sessioner, erfaring med virksomhedsudvikling er nyttig

## Forudsætninger

### Systemkrav
- **Operativsystem**: Windows 11 (22H2 eller nyere)
- **Hukommelse**: 16GB RAM (32GB anbefales til større modeller)
- **Lagring**: 50GB ledig plads til modelcaching
- **Hardware**: Enhed med NPU anbefales (Copilot+ PC), GPU valgfrit
- **Netværk**: Højhastighedsinternet til initial modeldownload

### Udviklingsmiljø
- Visual Studio Code med AI Toolkit-udvidelse
- Python 3.10+ og pip
- Git til versionskontrol
- PowerShell eller Kommandoprompt
- Azure CLI (valgfrit til cloud-integration)

### Videnforudsætninger
- Grundlæggende forståelse af AI/ML-konceptet
- Fortrolighed med kommandolinjen
- Grundlæggende Python-programmering
- REST API-konceptet
- Grundlæggende kendskab til prompting og modelinference

## Modul tidslinje

**Samlet estimeret tid**: 15-20 timer

| Session | Fokusområde | Tid | Kompleksitet |
|---------|-------------|-----|--------------|
|  1 | Opsætning & Grundlæggende | 2-3 timer | Begynder |
|  2 | AI-løsninger | 2-3 timer | Mellem |
|  3 | Open Source | 2-3 timer | Mellem |
|  4 | Avancerede modeller | 3-4 timer | Avanceret |
|  5 | AI-agenter | 3-4 timer | Avanceret |
|  6 | Virksomhedsværktøjer | 3-4 timer | Ekspert |

## Nøgleressourcer

### Primær dokumentation
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays Series](https://aka.ms/model-mondays)

### Fællesskabsressourcer
- [Foundry Local Community Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry Samples](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence)

## Læringsresultater

Når du har gennemført dette modul, vil du være i stand til:

### Teknisk ekspertise
- **Implementere og administrere**: Foundry Local installationer på tværs af udviklings- og produktionsmiljøer
- **Integrere modeller**: Arbejde problemfrit med forskellige modelfamilier fra Microsoft, Hugging Face og fællesskabet
- **Bygge applikationer**: Skabe produktionsklare AI-applikationer med avancerede funktioner og optimeringer
- **Udvikle agenter**: Implementere sofistikerede AI-agenter med grounding, ræsonnement og værktøjsintegration

### Strategisk forståelse
- **Arkitekturvalg**: Træffe informerede beslutninger mellem lokal og cloud-implementering
- **Ydeevneoptimering**: Optimere inference-ydeevne på tværs af forskellige hardwarekonfigurationer
- **Skalering til virksomheder**: Designe applikationer, der kan skaleres fra lokale prototyper til virksomhedsimplementeringer
- **Privatliv og sikkerhed**: Implementere AI-løsninger, der bevarer privatliv med lokal inference

### Innovationskapacitet
- **Hurtig prototyping**: Hurtigt bygge og teste AI-applikationskoncepter
- **Fællesskabsintegration**: Udnytte open source-modeller og bidrage til økosystemet
- **Avancerede mønstre**: Implementere banebrydende AI-mønstre, herunder RAG, agenter og værktøjsintegration
- **Fremtidsklar udvikling**: Bygge applikationer klar til fremtidens AI-teknologier og mønstre

## Kom godt i gang

1. **Forbered dit miljø**: Sørg for Windows 11 med anbefalede hardware-specifikationer
2. **Installer forudsætninger**: Opsæt udviklingsværktøjer og afhængigheder
3. **Start med session 1**: Begynd med Foundry Local installation og grundlæggende opsætning
4. **Fortsæt sekventielt**: Fuldfør sessionerne i rækkefølge for optimal læringsprogression
5. **Øv dig løbende**: Anvend koncepter gennem praktiske øvelser og projekter

## Succeskriterier

Følg din fremgang gennem modulet:

- [ ] Installere og konfigurere Foundry Local med succes
- [ ] Implementere og køre mindst 4 forskellige modelfamilier
- [ ] Bygge en komplet AI-løsning med dataintegration
- [ ] Integrere mindst 2 open source-modeller
- [ ] Skabe en funktionel RAG-chatapplikation
- [ ] Udvikle og implementere en AI-agent
- [ ] Implementere en arkitektur med modeller som værktøjer

## Hurtig start for eksempler

### 1) Opsætning af miljø (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Start en lokal model (nyt terminalvindue)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Kør Chainlit-demoen (Session 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Kør multi-agent koordinatoren (Session 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Hvis du ser forbindelsesfejl, valider Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Routerkonfiguration (Session 6)
Routeren udfører en hurtig sundhedstjek og understøtter miljøbaseret konfiguration:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Dette modul repræsenterer det nyeste inden for edge AI-udvikling og kombinerer Microsofts værktøjer i virksomhedsklasse med fleksibiliteten og innovationen fra open source-økosystemet. Ved at mestre Foundry Local vil du være i front inden for AI-applikationsudvikling.

For Azure OpenAI (Session 2), se README for nødvendige miljøvariabler og API-versionindstillinger.

## Oversigt over eksempler

- `samples/01`: Hurtig REST-chat til Foundry Local (`chat_quickstart.py`).
- `samples/02`: OpenAI SDK-integration (`sdk_quickstart.py`).
- `samples/03`: Modelopdagelse + hurtig benchmark (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG-demo (`app.py`).
- `samples/05`: Multi-agent orkestrering (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router til modeller som værktøjer (`python samples\06\router.py`).

---

