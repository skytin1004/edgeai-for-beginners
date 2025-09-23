<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-23T00:48:51+00:00",
  "source_file": "Module08/README.md",
  "language_code": "sk"
}
-->
# Modul 08: Praktické skúsenosti s Microsoft Foundry Local - Kompletná sada nástrojov pre vývojárov

## Prehľad

Microsoft Foundry Local predstavuje novú generáciu vývoja edge AI, poskytujúc vývojárom výkonné nástroje na vytváranie, nasadzovanie a škálovanie AI aplikácií lokálne, pričom zachováva bezproblémovú integráciu s Azure AI Foundry. Tento modul ponúka komplexný prehľad Foundry Local od inštalácie až po pokročilý vývoj agentov.

**Kľúčové technológie:**
- Microsoft Foundry Local CLI a SDK
- Integrácia s Azure AI Foundry
- Lokálna inferencia modelov
- Lokálne ukladanie a optimalizácia modelov
- Architektúry založené na agentoch

## Ciele modulu

Po absolvovaní tohto modulu budete schopní:

- **Ovládnuť nastavenie Foundry Local**: Inštalovať, konfigurovať a optimalizovať Foundry Local pre vývoj na Windows 11
- **Nasadzovať rôzne modely**: Spúšťať modely phi, qwen, deepseek a GPT-OSS-20B lokálne pomocou CLI príkazov
- **Vytvárať produkčné riešenia**: Navrhovať AI aplikácie s pokročilým prompt engineeringom a integráciou dát
- **Využívať open-source ekosystém**: Integrovať modely Hugging Face a príspevky komunity
- **Porovnávať AI architektúry**: Pochopiť kompromisy medzi LLMs a SLMs a stratégie nasadzovania
- **Vyvíjať AI agentov**: Vytvárať inteligentných agentov pomocou architektúry Foundry Local a techník uzemnenia
- **Implementovať modely ako nástroje**: Navrhovať modulárne, prispôsobiteľné AI riešenia pre podnikové aplikácie

## Štruktúra modulu

### [1: Začíname s Foundry Local](./01.FoundryLocalSetup.md)
**Zameranie**: Inštalácia, nastavenie CLI, ukladanie modelov a hardvérová akcelerácia

**Čo sa naučíte:**
- Kompletná inštalácia Foundry Local na Windows 11
- Konfigurácia CLI a štruktúra príkazov
- Stratégie ukladania modelov pre optimálny výkon
- Nastavenie a optimalizácia hardvérovej akcelerácie
- Praktické nasadenie modelov phi, qwen, deepseek a GPT-OSS-20B

**Trvanie**: 2-3 hodiny  
**Predpoklady**: Windows 11, základné znalosti príkazového riadku

---

### [2: Vytváranie AI riešení s Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Zameranie**: Pokročilý prompt engineering, integrácia dát a akčné úlohy

**Čo sa naučíte:**
- Pokročilé techniky prompt engineeringu
- Vzory integrácie dát a osvedčené postupy
- Vytváranie akčných AI úloh s Foundry Local
- Bezproblémové pracovné postupy integrácie Azure AI Foundry
- Optimalizácia výkonu a monitorovanie

**Trvanie**: 2-3 hodiny  
**Predpoklady**: Dokončenie relácie 1, Azure účet (voliteľné)

---

### [3: Open-Source modely vo Foundry Local](./03.OpenSourceModels.md)
**Zameranie**: Integrácia Hugging Face, stratégie výberu modelov a príspevky komunity

**Čo sa naučíte:**
- Integrácia modelov Hugging Face s Foundry Local
- Stratégie „Bring-your-own-model“ (BYOM) a ich implementácia
- Prehľad série Model Mondays a príspevky komunity
- Nasadzovanie a optimalizácia vlastných modelov
- Kritériá hodnotenia a výberu modelov komunity

**Trvanie**: 2-3 hodiny  
**Predpoklady**: Dokončenie relácií 1-2, účet Hugging Face

---

### [4: Preskúmajte špičkové modely - LLMs, SLMs a lokálna inferencia](./04.CuttingEdgeModels.md)
**Zameranie**: Porovnanie modelov, EdgeAI s Phi a ONNX Runtime, pokročilé ukážky

**Čo sa naučíte:**
- Komplexné porovnanie LLMs vs SLMs a ich použitia
- Kompromisy medzi lokálnou a cloudovou inferenciou a rozhodovacie rámce
- Implementácia EdgeAI s Phi a ONNX Runtime
- Vývoj a nasadenie Chainlit RAG Chat App
- Optimalizačné techniky inferencie pomocou WebGPU
- Integrácia a schopnosti AI PC SDK

**Trvanie**: 3-4 hodiny  
**Predpoklady**: Dokončenie relácií 1-3, pochopenie konceptov inferencie

---

### [5: Rýchly vývoj AI agentov s Foundry Local](./05.AIPoweredAgents.md)
**Zameranie**: Rýchly vývoj GenAI aplikácií, systémové prompty, uzemnenie a architektúry agentov

**Čo sa naučíte:**
- Architektúra agentov Foundry Local a návrhové vzory
- Systémový prompt engineering pre správanie agentov
- Techniky uzemnenia pre spoľahlivé odpovede agentov
- Pracovné postupy rýchleho vývoja GenAI aplikácií
- Orchestrácia agentov a systémy s viacerými agentmi
- Stratégie produkčného nasadenia AI agentov

**Trvanie**: 3-4 hodiny  
**Predpoklady**: Dokončenie relácií 1-4, základné pochopenie AI agentov

---

### [6: Foundry Local - Modely ako nástroje](./06.ModelsAsTools.md)
**Zameranie**: Modulárne AI riešenia, lokálne nasadenie a podnikové škálovanie

**Čo sa naučíte:**
- Používanie AI modelov ako modulárnych, prispôsobiteľných nástrojov
- Lokálne nasadenie bez závislosti na cloude
- Inferencia s nízkou latenciou, nákladovou efektívnosťou a ochranou súkromia
- Vzory integrácie SDK, API a CLI
- Prispôsobenie modelov pre konkrétne použitia
- Stratégie škálovania od lokálneho nasadenia po Azure AI Foundry
- Architektúry AI aplikácií pripravené pre podnikové prostredie

**Trvanie**: 3-4 hodiny  
**Predpoklady**: Všetky predchádzajúce relácie, skúsenosti s podnikovým vývojom sú výhodou

## Predpoklady

### Požiadavky na systém
- **Operačný systém**: Windows 11 (22H2 alebo novší)
- **Pamäť**: 16GB RAM (32GB odporúčaných pre väčšie modely)
- **Úložisko**: 50GB voľného miesta na ukladanie modelov
- **Hardvér**: Odporúčaný NPU-enabled zariadenie (Copilot+ PC), GPU voliteľné
- **Sieť**: Rýchly internet na počiatočné stiahnutie modelov

### Vývojové prostredie
- Visual Studio Code s rozšírením AI Toolkit
- Python 3.10+ a pip
- Git na správu verzií
- PowerShell alebo Command Prompt
- Azure CLI (voliteľné pre integráciu s cloudom)

### Znalostné predpoklady
- Základné pochopenie AI/ML konceptov
- Znalosť príkazového riadku
- Základy programovania v Pythone
- Koncepty REST API
- Základné znalosti promptovania a inferencie modelov

## Časový harmonogram modulu

**Celkový odhadovaný čas**: 15-20 hodín

| Relácia | Oblasť zamerania | Čas | Náročnosť |
|---------|------------------|------|-----------|
|  1 | Nastavenie a základy | 2-3 hodiny | Začiatočník |
|  2 | AI riešenia | 2-3 hodiny | Stredne pokročilý |
|  3 | Open Source | 2-3 hodiny | Stredne pokročilý |
|  4 | Pokročilé modely | 3-4 hodiny | Pokročilý |
|  5 | AI agenti | 3-4 hodiny | Pokročilý |
|  6 | Podnikové nástroje | 3-4 hodiny | Expert |

## Kľúčové zdroje

### Primárna dokumentácia
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Dokumentácia](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Séria Model Mondays](https://aka.ms/model-mondays)

### Zdroje komunity
- [Diskusie komunity Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Ukážky Azure AI Foundry](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence)

## Výsledky učenia

Po absolvovaní tohto modulu budete schopní:

### Technická zručnosť
- **Nasadzovať a spravovať**: Inštalácie Foundry Local v prostredí vývoja a produkcie
- **Integrovať modely**: Bezproblémovo pracovať s rôznymi rodinami modelov od Microsoftu, Hugging Face a komunity
- **Vytvárať aplikácie**: Navrhovať produkčne pripravené AI aplikácie s pokročilými funkciami a optimalizáciami
- **Vyvíjať agentov**: Implementovať sofistikovaných AI agentov s uzemnením, logikou a integráciou nástrojov

### Strategické pochopenie
- **Rozhodnutia o architektúre**: Robiť informované rozhodnutia medzi lokálnym a cloudovým nasadením
- **Optimalizácia výkonu**: Optimalizovať výkon inferencie na rôznych hardvérových konfiguráciách
- **Podnikové škálovanie**: Navrhovať aplikácie, ktoré škálujú od lokálnych prototypov po podnikové nasadenia
- **Ochrana súkromia a bezpečnosť**: Implementovať AI riešenia s ochranou súkromia pomocou lokálnej inferencie

### Inovačné schopnosti
- **Rýchle prototypovanie**: Rýchlo vytvárať a testovať koncepty AI aplikácií
- **Integrácia komunity**: Využívať open-source modely a prispievať do ekosystému
- **Pokročilé vzory**: Implementovať špičkové AI vzory vrátane RAG, agentov a integrácie nástrojov
- **Vývoj pripravený na budúcnosť**: Navrhovať aplikácie pripravené na nové AI technológie a vzory

## Začíname

1. **Pripravte si prostredie**: Uistite sa, že máte Windows 11 s odporúčanými hardvérovými špecifikáciami
2. **Nainštalujte predpoklady**: Nastavte vývojové nástroje a závislosti
3. **Začnite s reláciou 1**: Začnite inštaláciou a základným nastavením Foundry Local
4. **Postupujte postupne**: Dokončite relácie v poradí pre optimálny postup učenia
5. **Praktizujte neustále**: Aplikujte koncepty prostredníctvom praktických cvičení a projektov

## Metriky úspechu

Sledujte svoj pokrok v module:

- [ ] Úspešne nainštalovať a konfigurovať Foundry Local
- [ ] Nasadiť a spustiť aspoň 4 rôzne rodiny modelov
- [ ] Vytvoriť kompletné AI riešenie s integráciou dát
- [ ] Integrovať aspoň 2 open-source modely
- [ ] Vytvoriť funkčnú RAG chat aplikáciu
- [ ] Vyvinúť a nasadiť AI agenta
- [ ] Implementovať architektúru modelov ako nástrojov

## Rýchly štart pre ukážky

### 1) Nastavenie prostredia (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Spustenie lokálneho modelu (nový terminál)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Spustenie Chainlit demo (Relácia 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Spustenie koordinátora viacerých agentov (Relácia 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Ak vidíte chyby pripojenia, overte Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Konfigurácia routera (Relácia 6)
Router vykonáva rýchlu kontrolu stavu a podporuje konfiguráciu na základe prostredia:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Tento modul predstavuje špičku vývoja edge AI, kombinujúc podnikové nástroje Microsoftu s flexibilitou a inováciou open-source ekosystému. Ovládnutím Foundry Local budete na čele vývoja AI aplikácií.

Pre Azure OpenAI (Relácia 2) si pozrite README ukážky pre požadované premenné prostredia a nastavenia verzie API.

## Prehľad ukážok

- `samples/01`: Rýchly REST chat s Foundry Local (`chat_quickstart.py`).
- `samples/02`: Integrácia OpenAI SDK (`sdk_quickstart.py`).
- `samples/03`: Objavovanie modelov + rýchly benchmark (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG demo (`app.py`).
- `samples/05`: Orchestrácia viacerých agentov (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router modelov ako nástrojov (`python samples\06\router.py`).

---

