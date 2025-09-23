<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T20:19:45+00:00",
  "source_file": "Module08/README.md",
  "language_code": "no"
}
-->
# Modul 08: Praktisk arbeid med Microsoft Foundry Local - Komplett utviklerverktøy

## Oversikt

Microsoft Foundry Local representerer neste generasjon av edge AI-utvikling, og gir utviklere kraftige verktøy for å bygge, distribuere og skalere AI-applikasjoner lokalt, samtidig som det opprettholder sømløs integrasjon med Azure AI Foundry. Denne modulen gir en omfattende dekning av Foundry Local, fra installasjon til avansert agentutvikling.

**Nøkkelteknologier:**
- Microsoft Foundry Local CLI og SDK
- Azure AI Foundry-integrasjon
- Modellinferens på enheten
- Lokal modellbuffer og optimalisering
- Agentbaserte arkitekturer

## Modulens læringsmål

Ved å fullføre denne modulen vil du:

- **Beherske Foundry Local-oppsett**: Installere, konfigurere og optimalisere Foundry Local for utvikling på Windows 11
- **Distribuere ulike modeller**: Kjøre phi, qwen, deepseek og GPT-OSS-20B-modeller lokalt med CLI-kommandoer
- **Bygge produksjonsløsninger**: Lage AI-applikasjoner med avansert prompt engineering og dataintegrasjon
- **Utnytte det åpne økosystemet**: Integrere Hugging Face-modeller og bidrag fra fellesskapet
- **Sammenligne AI-arkitekturer**: Forstå fordeler og ulemper med LLMs vs SLMs og distribusjonsstrategier
- **Utvikle AI-agenter**: Bygge intelligente agenter ved hjelp av Foundry Locals arkitektur og grounding-funksjoner
- **Implementere modeller som verktøy**: Lage modulære, tilpassbare AI-løsninger for bedriftsapplikasjoner

## Sesjonsstruktur

### [1: Kom i gang med Foundry Local](./01.FoundryLocalSetup.md)
**Fokus**: Installasjon, CLI-oppsett, modellbuffer og maskinvareakselerasjon

**Hva du vil lære:**
- Fullstendig installasjon av Foundry Local på Windows 11
- CLI-konfigurasjon og kommandooppsett
- Strategier for modellbuffer for optimal ytelse
- Oppsett og optimalisering av maskinvareakselerasjon
- Praktisk distribusjon av phi, qwen, deepseek og GPT-OSS-20B-modeller

**Varighet**: 2-3 timer  
**Forutsetninger**: Windows 11, grunnleggende kunnskap om kommandolinjen

---

### [2: Bygg AI-løsninger med Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Fokus**: Avansert prompt engineering, dataintegrasjon og handlingsorienterte oppgaver

**Hva du vil lære:**
- Avanserte teknikker for prompt engineering
- Mønstre og beste praksis for dataintegrasjon
- Bygge handlingsorienterte AI-oppgaver med Foundry Local
- Sømløse arbeidsflyter for Azure AI Foundry-integrasjon
- Ytelsesoptimalisering og overvåking

**Varighet**: 2-3 timer  
**Forutsetninger**: Fullført sesjon 1, Azure-konto (valgfritt)

---

### [3: Åpen kildekode-modeller med Foundry Local](./03.OpenSourceModels.md)
**Fokus**: Hugging Face-integrasjon, modellvalgstrategier og bidrag fra fellesskapet

**Hva du vil lære:**
- Integrasjon av Hugging Face-modeller med Foundry Local
- Strategier og implementering for "Bring-your-own-model" (BYOM)
- Innsikt fra Model Mondays-serien og bidrag fra fellesskapet
- Tilpasset modelldistribusjon og optimalisering
- Evaluering og utvalgskriterier for fellesskapsmodeller

**Varighet**: 2-3 timer  
**Forutsetninger**: Fullført sesjon 1-2, Hugging Face-konto

---

### [4: Utforsk banebrytende modeller - LLMs, SLMs og inferens på enheten](./04.CuttingEdgeModels.md)
**Fokus**: Modellsammenligning, EdgeAI med Phi og ONNX Runtime, avanserte demoer

**Hva du vil lære:**
- Omfattende sammenligning av LLMs vs SLMs og bruksområder
- Fordeler og ulemper med lokal vs skybasert inferens
- EdgeAI-implementering med Phi og ONNX Runtime
- Utvikling og distribusjon av Chainlit RAG Chat App
- Optimaliseringsteknikker for WebGPU-inferens
- Integrasjon og funksjoner i AI PC SDK

**Varighet**: 3-4 timer  
**Forutsetninger**: Fullført sesjon 1-3, forståelse av inferenskonsepter

---

### [5: Bygg AI-drevne agenter raskt med Foundry Local](./05.AIPoweredAgents.md)
**Fokus**: Rask utvikling av GenAI-apper, systemprompter, grounding og agentarkitekturer

**Hva du vil lære:**
- Foundry Locals agentarkitektur og designmønstre
- Systemprompt engineering for agentadferd
- Grounding-teknikker for pålitelige agentresponser
- Arbeidsflyter for rask utvikling av GenAI-applikasjoner
- Orkestrering av agenter og systemer med flere agenter
- Strategier for produksjonsdistribusjon av AI-agenter

**Varighet**: 3-4 timer  
**Forutsetninger**: Fullført sesjon 1-4, grunnleggende forståelse av AI-agenter

---

### [6: Foundry Local - Modeller som verktøy](./06.ModelsAsTools.md)
**Fokus**: Modulære AI-løsninger, distribusjon på enheten og skalering for bedrifter

**Hva du vil lære:**
- Behandle AI-modeller som modulære, tilpassbare verktøy
- Distribusjon på enheten uten avhengighet av skyen
- Lav latens, kostnadseffektiv og personvernvennlig inferens
- Mønstre for integrasjon med SDK, API og CLI
- Tilpasning av modeller for spesifikke bruksområder
- Skalering fra lokal til Azure AI Foundry
- Bedriftsklare AI-applikasjonsarkitekturer

**Varighet**: 3-4 timer  
**Forutsetninger**: Alle tidligere sesjoner, erfaring med bedriftsutvikling er nyttig

## Forutsetninger

### Systemkrav
- **Operativsystem**: Windows 11 (22H2 eller nyere)
- **Minne**: 16GB RAM (32GB anbefales for større modeller)
- **Lagring**: 50GB ledig plass for modellbuffer
- **Maskinvare**: Enhet med NPU anbefales (Copilot+ PC), GPU valgfritt
- **Nettverk**: Høyhastighetsinternett for nedlasting av modeller

### Utviklingsmiljø
- Visual Studio Code med AI Toolkit-utvidelse
- Python 3.10+ og pip
- Git for versjonskontroll
- PowerShell eller kommandolinje
- Azure CLI (valgfritt for skyintegrasjon)

### Kunnskapsforutsetninger
- Grunnleggende forståelse av AI/ML-konsepter
- Kjennskap til kommandolinjen
- Grunnleggende Python-programmering
- REST API-konsepter
- Grunnleggende kunnskap om prompting og modellinferens

## Modulens tidslinje

**Total estimert tid**: 15-20 timer

| Sesjon | Fokusområde | Tid | Kompleksitet |
|--------|-------------|-----|--------------|
|  1 | Oppsett og grunnleggende | 2-3 timer | Nybegynner |
|  2 | AI-løsninger | 2-3 timer | Middels |
|  3 | Åpen kildekode | 2-3 timer | Middels |
|  4 | Avanserte modeller | 3-4 timer | Avansert |
|  5 | AI-agenter | 3-4 timer | Avansert |
|  6 | Bedriftsverktøy | 3-4 timer | Ekspert |

## Nøkkelressurser

### Primær dokumentasjon
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Dokumentasjon](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays Series](https://aka.ms/model-mondays)

### Fellesskapsressurser
- [Foundry Local Community Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry Eksempler](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence)

## Læringsutbytte

Ved fullføring av denne modulen vil du være i stand til å:

### Teknisk mestring
- **Distribuere og administrere**: Foundry Local-installasjoner i utviklings- og produksjonsmiljøer
- **Integrere modeller**: Arbeide sømløst med ulike modelfamilier fra Microsoft, Hugging Face og fellesskapskilder
- **Bygge applikasjoner**: Lage produksjonsklare AI-applikasjoner med avanserte funksjoner og optimaliseringer
- **Utvikle agenter**: Implementere sofistikerte AI-agenter med grounding, resonnering og verktøyintegrasjon

### Strategisk forståelse
- **Arkitekturvalg**: Ta informerte beslutninger mellom lokal vs skybasert distribusjon
- **Ytelsesoptimalisering**: Optimalisere inferensytelse på ulike maskinvarekonfigurasjoner
- **Skalering for bedrifter**: Designe applikasjoner som skalerer fra lokale prototyper til bedriftsdistribusjoner
- **Personvern og sikkerhet**: Implementere personvernvennlige AI-løsninger med lokal inferens

### Innovasjonskapasitet
- **Rask prototyping**: Bygge og teste AI-applikasjonskonsepter raskt
- **Fellesskapsintegrasjon**: Utnytte åpne kildekode-modeller og bidra til økosystemet
- **Avanserte mønstre**: Implementere banebrytende AI-mønstre, inkludert RAG, agenter og verktøyintegrasjon
- **Fremtidsrettet utvikling**: Lage applikasjoner klare for fremvoksende AI-teknologier og mønstre

## Kom i gang

1. **Forbered miljøet ditt**: Sørg for Windows 11 med anbefalte maskinspesifikasjoner
2. **Installer forutsetninger**: Sett opp utviklingsverktøy og avhengigheter
3. **Start med sesjon 1**: Begynn med installasjon og grunnleggende oppsett av Foundry Local
4. **Følg progresjonen**: Fullfør sesjonene i rekkefølge for optimal læring
5. **Øv kontinuerlig**: Bruk konseptene gjennom praktiske øvelser og prosjekter

## Suksessmål

Følg fremgangen din gjennom modulen:

- [ ] Installere og konfigurere Foundry Local med suksess
- [ ] Distribuere og kjøre minst 4 forskjellige modelfamilier
- [ ] Bygge en komplett AI-løsning med dataintegrasjon
- [ ] Integrere minst 2 åpne kildekode-modeller
- [ ] Lage en funksjonell RAG-chatapplikasjon
- [ ] Utvikle og distribuere en AI-agent
- [ ] Implementere en arkitektur for modeller som verktøy

## Hurtigstart for eksempler

### 1) Miljøoppsett (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Start en lokal modell (ny terminal)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Kjør Chainlit-demoen (Sesjon 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Kjør koordinator for flere agenter (Sesjon 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Hvis du ser tilkoblingsfeil, valider Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Router-konfigurasjon (Sesjon 6)
Routeren utfører en rask helsesjekk og støtter miljøbasert konfigurasjon:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Denne modulen representerer det nyeste innen edge AI-utvikling, og kombinerer Microsofts verktøy i bedriftsklasse med fleksibiliteten og innovasjonen fra det åpne kilde-økosystemet. Ved å mestre Foundry Local vil du være i frontlinjen av AI-applikasjonsutvikling.

For Azure OpenAI (Sesjon 2), se README for nødvendige miljøvariabler og API-versjonsinnstillinger.

## Oversikt over eksempler

- `samples/01`: Rask REST-chat til Foundry Local (`chat_quickstart.py`).
- `samples/02`: OpenAI SDK-integrasjon (`sdk_quickstart.py`).
- `samples/03`: Modelloppdagelse + rask benchmark (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG-demo (`app.py`).
- `samples/05`: Orkestrering av flere agenter (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router for modeller som verktøy (`python samples\06\router.py`).

---

