<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T21:47:28+00:00",
  "source_file": "Module08/README.md",
  "language_code": "nl"
}
-->
# Module 08: Praktisch aan de slag met Microsoft Foundry Local - Complete ontwikkeltoolkit

## Overzicht

Microsoft Foundry Local vertegenwoordigt de volgende generatie van edge AI-ontwikkeling en biedt ontwikkelaars krachtige tools om AI-toepassingen lokaal te bouwen, implementeren en schalen, terwijl naadloze integratie met Azure AI Foundry behouden blijft. Deze module biedt een uitgebreide dekking van Foundry Local, van installatie tot geavanceerde agentontwikkeling.

**Belangrijke technologieën:**
- Microsoft Foundry Local CLI en SDK
- Integratie met Azure AI Foundry
- Modelinferentie op apparaat
- Lokale modelcaching en optimalisatie
- Agent-gebaseerde architecturen

## Leerdoelen van de module

Na het voltooien van deze module kun je:

- **Foundry Local Setup beheersen**: Foundry Local installeren, configureren en optimaliseren voor Windows 11-ontwikkeling
- **Diverse modellen implementeren**: Phi-, Qwen-, Deepseek- en GPT-OSS-20B-modellen lokaal uitvoeren met CLI-commando's
- **Productieoplossingen bouwen**: AI-toepassingen maken met geavanceerde prompt-engineering en gegevensintegratie
- **Open-source ecosysteem benutten**: Hugging Face-modellen en communitygedreven toevoegingen integreren
- **AI-architecturen vergelijken**: Trade-offs en implementatiestrategieën van LLM's versus SLM's begrijpen
- **AI-agents ontwikkelen**: Intelligente agents bouwen met Foundry Local's architectuur en groundingmogelijkheden
- **Modellen als tools implementeren**: Modulaire, aanpasbare AI-oplossingen creëren voor zakelijke toepassingen

## Sessiestructuur

### [1: Aan de slag met Foundry Local](./01.FoundryLocalSetup.md)
**Focus**: Installatie, CLI-setup, modelcaching en hardwareversnelling

**Wat je leert:**
- Volledige installatie van Foundry Local op Windows 11
- CLI-configuratie en commando-structuur
- Modelcachingstrategieën voor optimale prestaties
- Hardwareversnelling instellen en optimaliseren
- Praktische implementatie van Phi-, Qwen-, Deepseek- en GPT-OSS-20B-modellen

**Duur**: 2-3 uur  
**Vereisten**: Windows 11, basiskennis van de command line

---

### [2: AI-oplossingen bouwen met Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Focus**: Geavanceerde prompt-engineering, gegevensintegratie en uitvoerbare taken

**Wat je leert:**
- Geavanceerde technieken voor prompt-engineering
- Patronen en best practices voor gegevensintegratie
- Uitvoerbare AI-taken bouwen met Foundry Local
- Naadloze workflows voor integratie met Azure AI Foundry
- Prestatieoptimalisatie en monitoring

**Duur**: 2-3 uur  
**Vereisten**: Voltooiing van sessie 1, Azure-account (optioneel)

---

### [3: Open-source modellen Foundry Local](./03.OpenSourceModels.md)
**Focus**: Hugging Face-integratie, strategieën voor modelselectie en communitygedreven toevoegingen

**Wat je leert:**
- Hugging Face-modellen integreren met Foundry Local
- Bring-your-own-model (BYOM)-strategieën en implementatie
- Inzichten uit de Model Mondays-serie en bijdragen van de community
- Aangepaste modelimplementatie en optimalisatie
- Evaluatiecriteria en selectie van communitymodellen

**Duur**: 2-3 uur  
**Vereisten**: Voltooiing van sessie 1-2, Hugging Face-account

---

### [4: Verken geavanceerde modellen - LLM's, SLM's en inferentie op apparaat](./04.CuttingEdgeModels.md)
**Focus**: Modelvergelijking, EdgeAI met Phi en ONNX Runtime, geavanceerde demo's

**Wat je leert:**
- Uitgebreide vergelijking van LLM's versus SLM's en toepassingscases
- Trade-offs en beslissingskaders voor lokale versus cloud-inferentie
- EdgeAI-implementatie met Phi en ONNX Runtime
- Ontwikkeling en implementatie van Chainlit RAG Chat App
- Optimalisatietechnieken voor WebGPU-inferentie
- Integratie en mogelijkheden van AI PC SDK

**Duur**: 3-4 uur  
**Vereisten**: Voltooiing van sessie 1-3, begrip van inferentieconcepten

---

### [5: Snel AI-aangedreven agents bouwen met Foundry Local](./05.AIPoweredAgents.md)
**Focus**: Snelle ontwikkeling van GenAI-apps, systeemprompts, grounding en agentarchitecturen

**Wat je leert:**
- Architectuur en ontwerpprincipes van Foundry Local-agents
- Systeemprompt-engineering voor agentgedrag
- Groundingtechnieken voor betrouwbare agentreacties
- Snelle workflows voor ontwikkeling van GenAI-toepassingen
- Orchestratie van agents en multi-agent systemen
- Productiestrategieën voor implementatie van AI-agents

**Duur**: 3-4 uur  
**Vereisten**: Voltooiing van sessie 1-4, basisbegrip van AI-agents

---

### [6: Foundry Local - Modellen als tools](./06.ModelsAsTools.md)
**Focus**: Modulaire AI-oplossingen, implementatie op apparaat en schaalbaarheid voor ondernemingen

**Wat je leert:**
- AI-modellen behandelen als modulaire, aanpasbare tools
- Implementatie op apparaat zonder afhankelijkheid van de cloud
- Inferentie met lage latentie, kostenefficiëntie en privacybescherming
- SDK-, API- en CLI-integratiepatronen
- Modelaanpassing voor specifieke use cases
- Schaalstrategieën van lokaal naar Azure AI Foundry
- AI-applicatiearchitecturen die klaar zijn voor ondernemingen

**Duur**: 3-4 uur  
**Vereisten**: Alle voorgaande sessies, ervaring met zakelijke ontwikkeling is nuttig

## Vereisten

### Systeemvereisten
- **Besturingssysteem**: Windows 11 (22H2 of later)
- **Geheugen**: 16GB RAM (32GB aanbevolen voor grotere modellen)
- **Opslag**: 50GB vrije ruimte voor modelcaching
- **Hardware**: NPU-apparaat aanbevolen (Copilot+ PC), GPU optioneel
- **Netwerk**: Snelle internetverbinding voor initiële modeldownloads

### Ontwikkelomgeving
- Visual Studio Code met AI Toolkit-extensie
- Python 3.10+ en pip
- Git voor versiebeheer
- PowerShell of Command Prompt
- Azure CLI (optioneel voor cloudintegratie)

### Kennisvereisten
- Basisbegrip van AI/ML-concepten
- Vertrouwdheid met de command line
- Basiskennis van Python-programmering
- REST API-concepten
- Basiskennis van prompting en modelinferentie

## Module Tijdlijn

**Totale geschatte tijd**: 15-20 uur

| Sessie | Focusgebied | Tijd | Complexiteit |
|--------|-------------|------|-------------|
|  1 | Setup & Basis | 2-3 uur | Beginner |
|  2 | AI-oplossingen | 2-3 uur | Gemiddeld |
|  3 | Open Source | 2-3 uur | Gemiddeld |
|  4 | Geavanceerde Modellen | 3-4 uur | Geavanceerd |
|  5 | AI-agents | 3-4 uur | Geavanceerd |
|  6 | Tools voor ondernemingen | 3-4 uur | Expert |

## Belangrijke bronnen

### Primaire documentatie
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Documentatie](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays Serie](https://aka.ms/model-mondays)

### Communitybronnen
- [Foundry Local Community Discussies](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry Voorbeelden](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence)

## Leerresultaten

Na het voltooien van deze module ben je in staat om:

### Technische beheersing
- **Implementeren en beheren**: Foundry Local-installaties in ontwikkel- en productieomgevingen
- **Modellen integreren**: Naadloos werken met diverse modelfamilies van Microsoft, Hugging Face en communitybronnen
- **Toepassingen bouwen**: Productieklare AI-toepassingen maken met geavanceerde functies en optimalisaties
- **Agents ontwikkelen**: Geavanceerde AI-agents implementeren met grounding, redenering en toolintegratie

### Strategisch inzicht
- **Architectuurkeuzes**: Informatiegestuurde beslissingen nemen tussen lokale en cloudimplementatie
- **Prestatieoptimalisatie**: Inferentieprestaties optimaliseren voor verschillende hardwareconfiguraties
- **Schaalbaarheid voor ondernemingen**: Applicaties ontwerpen die schaalbaar zijn van lokale prototypes tot bedrijfsimplementaties
- **Privacy en beveiliging**: Privacybeschermende AI-oplossingen implementeren met lokale inferentie

### Innovatievermogen
- **Snelle prototyping**: Snel AI-toepassingsconcepten bouwen en testen
- **Communityintegratie**: Open-source modellen benutten en bijdragen aan het ecosysteem
- **Geavanceerde patronen**: Cutting-edge AI-patronen implementeren, zoals RAG, agents en toolintegratie
- **Toekomstbestendige ontwikkeling**: Applicaties bouwen die klaar zijn voor opkomende AI-technologieën en -patronen

## Aan de slag

1. **Bereid je omgeving voor**: Zorg voor Windows 11 met aanbevolen hardwarevereisten
2. **Installeer vereisten**: Stel ontwikkeltools en afhankelijkheden in
3. **Begin met sessie 1**: Start met de installatie en basisconfiguratie van Foundry Local
4. **Volg de sessies op volgorde**: Voltooi de sessies in volgorde voor optimale leerprogressie
5. **Oefen continu**: Pas concepten toe via praktische oefeningen en projecten

## Succescriteria

Volg je voortgang door de module:

- [ ] Foundry Local succesvol installeren en configureren
- [ ] Minstens 4 verschillende modelfamilies implementeren en uitvoeren
- [ ] Een complete AI-oplossing bouwen met gegevensintegratie
- [ ] Minstens 2 open-source modellen integreren
- [ ] Een functionele RAG-chatapplicatie creëren
- [ ] Een AI-agent ontwikkelen en implementeren
- [ ] Een modellen-als-tools architectuur implementeren

## Snelle start voor voorbeelden

### 1) Omgevingsinstelling (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Start een lokaal model (nieuw terminalvenster)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Voer de Chainlit-demo uit (Sessie 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Voer de multi-agent coördinator uit (Sessie 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Als je verbindingsfouten ziet, valideer Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Routerconfiguratie (Sessie 6)
De router voert een snelle gezondheidscontrole uit en ondersteunt configuratie op basis van omgevingsvariabelen:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Deze module vertegenwoordigt de nieuwste ontwikkelingen in edge AI-ontwikkeling, waarbij de enterprise-grade tools van Microsoft worden gecombineerd met de flexibiliteit en innovatie van het open-source ecosysteem. Door Foundry Local te beheersen, sta je aan de voorhoede van AI-toepassingsontwikkeling.

Voor Azure OpenAI (Sessie 2), zie de voorbeeld README voor vereiste omgevingsvariabelen en API-versie-instellingen.

## Overzicht van voorbeelden

- `samples/01`: Snelle REST-chat naar Foundry Local (`chat_quickstart.py`).
- `samples/02`: OpenAI SDK-integratie (`sdk_quickstart.py`).
- `samples/03`: Modelontdekking + snelle benchmark (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG-demo (`app.py`).
- `samples/05`: Multi-agent orkestratie (`python -m samples.05.agents.coordinator`).
- `samples/06`: Modellen-als-tools router (`python samples\06\router.py`).

---

