<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T19:16:14+00:00",
  "source_file": "Module08/README.md",
  "language_code": "sv"
}
-->
# Modul 08: Praktisk erfarenhet med Microsoft Foundry Local - Komplett utvecklarverktyg

## Översikt

Microsoft Foundry Local representerar nästa generation av edge AI-utveckling och ger utvecklare kraftfulla verktyg för att bygga, distribuera och skala AI-applikationer lokalt, samtidigt som det erbjuder sömlös integration med Azure AI Foundry. Denna modul täcker Foundry Local från installation till avancerad agentutveckling.

**Nyckelteknologier:**
- Microsoft Foundry Local CLI och SDK
- Integration med Azure AI Foundry
- Modellinferens på enheten
- Lokal modellcaching och optimering
- Agentbaserade arkitekturer

## Modulens lärandemål

Genom att slutföra denna modul kommer du att:

- **Behärska Foundry Local-setup**: Installera, konfigurera och optimera Foundry Local för utveckling på Windows 11
- **Distribuera olika modeller**: Köra phi, qwen, deepseek och GPT-OSS-20B-modeller lokalt med CLI-kommandon
- **Bygga produktionslösningar**: Skapa AI-applikationer med avancerad promptteknik och dataintegration
- **Utnyttja open source-ekosystemet**: Integrera Hugging Face-modeller och community-drivna tillägg
- **Jämföra AI-arkitekturer**: Förstå för- och nackdelar med LLMs kontra SLMs och strategier för distribution
- **Utveckla AI-agenter**: Bygga intelligenta agenter med Foundry Locals arkitektur och grundningsfunktioner
- **Implementera modeller som verktyg**: Skapa modulära, anpassningsbara AI-lösningar för företagsapplikationer

## Sessionsstruktur

### [1: Kom igång med Foundry Local](./01.FoundryLocalSetup.md)
**Fokus**: Installation, CLI-setup, modellcaching och hårdvaruacceleration

**Vad du kommer att lära dig:**
- Komplett installation av Foundry Local på Windows 11
- CLI-konfiguration och kommandostruktur
- Strategier för modellcaching för optimal prestanda
- Setup och optimering av hårdvaruacceleration
- Praktisk distribution av phi, qwen, deepseek och GPT-OSS-20B-modeller

**Varaktighet**: 2-3 timmar  
**Förkunskaper**: Windows 11, grundläggande kunskaper om kommandoraden

---

### [2: Bygg AI-lösningar med Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Fokus**: Avancerad promptteknik, dataintegration och handlingsbara uppgifter

**Vad du kommer att lära dig:**
- Avancerade tekniker för promptteknik
- Mönster och bästa praxis för dataintegration
- Bygga handlingsbara AI-uppgifter med Foundry Local
- Sömlösa arbetsflöden för integration med Azure AI Foundry
- Optimering och övervakning av prestanda

**Varaktighet**: 2-3 timmar  
**Förkunskaper**: Slutförande av session 1, Azure-konto (valfritt)

---

### [3: Open Source-modeller i Foundry Local](./03.OpenSourceModels.md)
**Fokus**: Hugging Face-integration, strategier för modellval och community-drivna tillägg

**Vad du kommer att lära dig:**
- Integration av Hugging Face-modeller med Foundry Local
- Strategier och implementering för "Bring-your-own-model" (BYOM)
- Insikter från Model Mondays-serien och community-bidrag
- Anpassad modelldistribution och optimering
- Utvärderingskriterier för community-modeller

**Varaktighet**: 2-3 timmar  
**Förkunskaper**: Slutförande av session 1-2, Hugging Face-konto

---

### [4: Utforska banbrytande modeller - LLMs, SLMs och inferens på enheten](./04.CuttingEdgeModels.md)
**Fokus**: Modelljämförelse, EdgeAI med Phi och ONNX Runtime, avancerade demos

**Vad du kommer att lära dig:**
- Omfattande jämförelse mellan LLMs och SLMs samt användningsfall
- Trade-offs mellan lokal och molnbaserad inferens och beslutsramverk
- EdgeAI-implementering med Phi och ONNX Runtime
- Utveckling och distribution av Chainlit RAG Chat App
- Optimeringstekniker för WebGPU-inferens
- Integration och kapabiliteter för AI PC SDK

**Varaktighet**: 3-4 timmar  
**Förkunskaper**: Slutförande av session 1-3, förståelse för inferenskoncept

---

### [5: Bygg AI-drivna agenter snabbt med Foundry Local](./05.AIPoweredAgents.md)
**Fokus**: Snabb utveckling av GenAI-appar, systemprompter, grundning och agentarkitekturer

**Vad du kommer att lära dig:**
- Foundry Locals agentarkitektur och designmönster
- Tekniker för systemprompter för agentbeteende
- Grundningstekniker för tillförlitliga agentresponser
- Snabba arbetsflöden för utveckling av GenAI-applikationer
- Orkestrering av agenter och system med flera agenter
- Strategier för produktionsdistribution av AI-agenter

**Varaktighet**: 3-4 timmar  
**Förkunskaper**: Slutförande av session 1-4, grundläggande förståelse för AI-agenter

---

### [6: Foundry Local - Modeller som verktyg](./06.ModelsAsTools.md)
**Fokus**: Modulära AI-lösningar, distribution på enheten och företagsmässig skalning

**Vad du kommer att lära dig:**
- Behandla AI-modeller som modulära, anpassningsbara verktyg
- Distribution på enheten utan molnberoende
- Inferens med låg latens, kostnadseffektivitet och integritetsskydd
- Mönster för integration av SDK, API och CLI
- Anpassning av modeller för specifika användningsfall
- Skalningsstrategier från lokal till Azure AI Foundry
- Företagsklara AI-applikationsarkitekturer

**Varaktighet**: 3-4 timmar  
**Förkunskaper**: Alla tidigare sessioner, erfarenhet av företagsutveckling är användbart

## Förkunskaper

### Systemkrav
- **Operativsystem**: Windows 11 (22H2 eller senare)
- **Minne**: 16GB RAM (32GB rekommenderas för större modeller)
- **Lagring**: 50GB ledigt utrymme för modellcaching
- **Hårdvara**: Enhet med NPU rekommenderas (Copilot+ PC), GPU valfritt
- **Nätverk**: Snabb internetanslutning för initiala modellnedladdningar

### Utvecklingsmiljö
- Visual Studio Code med AI Toolkit-tillägg
- Python 3.10+ och pip
- Git för versionskontroll
- PowerShell eller Kommandotolken
- Azure CLI (valfritt för molnintegration)

### Kunskapsförkunskaper
- Grundläggande förståelse för AI/ML-koncept
- Bekantskap med kommandoraden
- Grundläggande Python-programmering
- REST API-koncept
- Grundläggande kunskaper om promptteknik och modellinferens

## Modulens tidslinje

**Total uppskattad tid**: 15-20 timmar

| Session | Fokusområde | Tid | Svårighetsgrad |
|---------|-------------|-----|----------------|
|  1 | Setup & Grunder | 2-3 timmar | Nybörjare |
|  2 | AI-lösningar | 2-3 timmar | Mellanliggande |
|  3 | Open Source | 2-3 timmar | Mellanliggande |
|  4 | Avancerade modeller | 3-4 timmar | Avancerad |
|  5 | AI-agenter | 3-4 timmar | Avancerad |
|  6 | Företagsverktyg | 3-4 timmar | Expert |

## Viktiga resurser

### Primär dokumentation
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays Series](https://aka.ms/model-mondays)

### Community-resurser
- [Foundry Local Community Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry Samples](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence)

## Lärandemål

Efter att ha slutfört denna modul kommer du att vara utrustad för att:

### Teknisk kompetens
- **Distribuera och hantera**: Foundry Local-installationer i utvecklings- och produktionsmiljöer
- **Integrera modeller**: Arbeta sömlöst med olika modelfamiljer från Microsoft, Hugging Face och community-källor
- **Bygga applikationer**: Skapa produktionsklara AI-applikationer med avancerade funktioner och optimeringar
- **Utveckla agenter**: Implementera sofistikerade AI-agenter med grundning, resonemang och verktygsintegration

### Strategisk förståelse
- **Arkitekturval**: Göra informerade val mellan lokal och molnbaserad distribution
- **Prestandaoptimering**: Optimera inferensprestanda över olika hårdvarukonfigurationer
- **Företagsskalning**: Designa applikationer som skalar från lokala prototyper till företagsdistributioner
- **Integritet och säkerhet**: Implementera integritetsskyddande AI-lösningar med lokal inferens

### Innovationsförmåga
- **Snabb prototypframtagning**: Bygga och testa AI-applikationskoncept snabbt
- **Community-integration**: Utnyttja open source-modeller och bidra till ekosystemet
- **Avancerade mönster**: Implementera banbrytande AI-mönster inklusive RAG, agenter och verktygsintegration
- **Framtidsredo utveckling**: Bygga applikationer redo för framväxande AI-teknologier och mönster

## Kom igång

1. **Förbered din miljö**: Säkerställ Windows 11 med rekommenderade hårdvaruspecifikationer
2. **Installera förutsättningar**: Ställ in utvecklingsverktyg och beroenden
3. **Börja med session 1**: Starta med installation och grundläggande setup av Foundry Local
4. **Fortsätt sekventiellt**: Slutför sessionerna i ordning för optimal inlärningsprogression
5. **Öva kontinuerligt**: Tillämpa koncept genom praktiska övningar och projekt

## Framgångsmått

Följ din framgång genom modulen:

- [ ] Installera och konfigurera Foundry Local framgångsrikt
- [ ] Distribuera och köra minst 4 olika modelfamiljer
- [ ] Bygga en komplett AI-lösning med dataintegration
- [ ] Integrera minst 2 open source-modeller
- [ ] Skapa en fungerande RAG-chatapplikation
- [ ] Utveckla och distribuera en AI-agent
- [ ] Implementera en arkitektur för modeller-som-verktyg

## Snabbstart för exempel

### 1) Miljösetup (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Starta en lokal modell (ny terminal)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Kör Chainlit-demo (Session 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Kör multi-agent-koordinatorn (Session 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Om du ser anslutningsfel, validera Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Routerkonfiguration (Session 6)
Routern utför en snabb hälsokontroll och stödjer konfiguration baserad på miljövariabler:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Denna modul representerar det senaste inom edge AI-utveckling och kombinerar Microsofts företagsklassade verktyg med flexibiliteten och innovationen från open source-ekosystemet. Genom att behärska Foundry Local kommer du att vara i framkant av AI-applikationsutveckling.

För Azure OpenAI (Session 2), se README för exempel på nödvändiga miljövariabler och API-versionsinställningar.

## Översikt över exempel

- `samples/01`: Snabb REST-chat till Foundry Local (`chat_quickstart.py`).
- `samples/02`: OpenAI SDK-integration (`sdk_quickstart.py`).
- `samples/03`: Modellupptäckt + snabb benchmark (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG-demo (`app.py`).
- `samples/05`: Multi-agent-orkestrering (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router för modeller-som-verktyg (`python samples\06\router.py`).

---

