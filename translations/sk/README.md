<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ff006cd813df4152f5036e7b2bc5ed32",
  "translation_date": "2025-09-25T01:26:16+00:00",
  "source_file": "README.md",
  "language_code": "sk"
}
-->
# EdgeAI pre začiatočníkov

![Obrázok kurzu](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.sk.png)

[![Prispievatelia na GitHube](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problémy na GitHube](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull requesty na GitHube](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Sledovatelia na GitHube](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Forky na GitHube](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Hviezdičky na GitHube](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Postupujte podľa týchto krokov, aby ste mohli začať používať tieto zdroje:

1. **Forknite repozitár**: Kliknite [![Forky na GitHube](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Naklonujte repozitár**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Pripojte sa na Azure AI Foundry Discord a stretnite sa s odborníkmi a ďalšími vývojármi**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Podpora viacerých jazykov

#### Podporované cez GitHub Action (automatizované a vždy aktuálne)

[Arabčina](../ar/README.md) | [Bengálčina](../bn/README.md) | [Bulharčina](../bg/README.md) | [Barmčina (Mjanmarsko)](../my/README.md) | [Čínština (zjednodušená)](../zh/README.md) | [Čínština (tradičná, Hongkong)](../hk/README.md) | [Čínština (tradičná, Macao)](../mo/README.md) | [Čínština (tradičná, Taiwan)](../tw/README.md) | [Chorvátčina](../hr/README.md) | [Čeština](../cs/README.md) | [Dánčina](../da/README.md) | [Holandčina](../nl/README.md) | [Fínčina](../fi/README.md) | [Francúzština](../fr/README.md) | [Nemčina](../de/README.md) | [Gréčtina](../el/README.md) | [Hebrejčina](../he/README.md) | [Hindčina](../hi/README.md) | [Maďarčina](../hu/README.md) | [Indonézština](../id/README.md) | [Taliančina](../it/README.md) | [Japončina](../ja/README.md) | [Kórejčina](../ko/README.md) | [Malajčina](../ms/README.md) | [Maráthčina](../mr/README.md) | [Nepálčina](../ne/README.md) | [Nórčina](../no/README.md) | [Perzština (Farsi)](../fa/README.md) | [Poľština](../pl/README.md) | [Portugalčina (Brazília)](../br/README.md) | [Portugalčina (Portugalsko)](../pt/README.md) | [Pandžábčina (Gurmukhi)](../pa/README.md) | [Rumunčina](../ro/README.md) | [Ruština](../ru/README.md) | [Srbčina (cyrilika)](../sr/README.md) | [Slovenčina](./README.md) | [Slovinčina](../sl/README.md) | [Španielčina](../es/README.md) | [Swahilčina](../sw/README.md) | [Švédčina](../sv/README.md) | [Tagalog (Filipínčina)](../tl/README.md) | [Thajčina](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinčina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamčina](../vi/README.md)

**Ak chcete podporiť ďalšie jazyky, zoznam podporovaných jazykov nájdete [tu](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Úvod

Vitajte v **EdgeAI pre začiatočníkov** – vašej komplexnej ceste do transformačného sveta Edge umelej inteligencie. Tento kurz spája silné schopnosti AI s praktickým nasadením v reálnom svete na edge zariadeniach, čo vám umožní využiť potenciál AI priamo tam, kde sa generujú dáta a kde je potrebné robiť rozhodnutia.

### Čo sa naučíte

Tento kurz vás prevedie od základných konceptov až po implementácie pripravené na produkciu, vrátane:
- **Malé jazykové modely (SLMs)** optimalizované pre nasadenie na edge zariadeniach
- **Optimalizácia zohľadňujúca hardvér** na rôznych platformách
- **Inferencia v reálnom čase** s ochranou súkromia
- **Stratégie nasadenia do produkcie** pre podnikové aplikácie

### Prečo je EdgeAI dôležitá

Edge AI predstavuje zmenu paradigmy, ktorá rieši kritické moderné výzvy:
- **Ochrana súkromia a bezpečnosť**: Spracovanie citlivých dát lokálne bez vystavenia cloudu
- **Výkon v reálnom čase**: Eliminácia latencie siete pre aplikácie citlivé na čas
- **Efektívnosť nákladov**: Zníženie nákladov na šírku pásma a cloudové výpočty
- **Odolnosť operácií**: Zachovanie funkčnosti počas výpadkov siete
- **Regulačné požiadavky**: Splnenie požiadaviek na suverenitu dát

### Edge AI

Edge AI označuje spúšťanie AI algoritmov a jazykových modelov lokálne na hardvéri, blízko miesta, kde sa generujú dáta, bez závislosti na cloudových zdrojoch pre inferenciu. Znižuje latenciu, zvyšuje ochranu súkromia a umožňuje rozhodovanie v reálnom čase.

### Základné princípy:
- **Inferencia na zariadení**: AI modely bežia na edge zariadeniach (telefóny, routery, mikrokontroléry, priemyselné PC)
- **Offline schopnosti**: Funguje bez neustáleho pripojenia na internet
- **Nízka latencia**: Okamžité reakcie vhodné pre systémy v reálnom čase
- **Suverenita dát**: Uchováva citlivé dáta lokálne, čím zlepšuje bezpečnosť a súlad s predpismi

### Malé jazykové modely (SLMs)

SLMs ako Phi-4, Mistral-7B a Gemma sú optimalizované verzie väčších LLMs – trénované alebo destilované pre:
- **Znížené pamäťové nároky**: Efektívne využitie obmedzenej pamäte edge zariadení
- **Nižšie výpočtové požiadavky**: Optimalizované pre výkon CPU a edge GPU
- **Rýchlejšie spúšťanie**: Rýchla inicializácia pre pohotové aplikácie

Odomykajú silné NLP schopnosti pri splnení obmedzení:
- **Vstavané systémy**: IoT zariadenia a priemyselné kontroléry
- **Mobilné zariadenia**: Smartfóny a tablety s offline schopnosťami
- **IoT zariadenia**: Senzory a inteligentné zariadenia s obmedzenými zdrojmi
- **Edge servery**: Lokálne spracovacie jednotky s obmedzenými GPU zdrojmi
- **Osobné počítače**: Scenáre nasadenia na desktopoch a notebookoch

## Moduly kurzu a navigácia

| Modul | Téma | Oblasť zamerania | Kľúčový obsah | Úroveň | Trvanie |
|-------|------|------------------|---------------|--------|---------|
| [📚 01](../../Module01) | [Základy EdgeAI](./Module01/README.md) | Porovnanie Cloud vs Edge AI | Základy EdgeAI • Prípadové štúdie z reálneho sveta • Príručka implementácie • Nasadenie na edge | Začiatočník | 3-4 hod |
| [🧠 02](../../Module02) | [Základy modelov SLM](./Module02/README.md) | Rodiny modelov a architektúra | Rodina Phi • Rodina Qwen • Rodina Gemma • BitNET • μModel • Phi-Silica | Začiatočník | 4-5 hod |
| [🚀 03](../../Module03) | [Praxe nasadenia SLM](./Module03/README.md) | Lokálne a cloudové nasadenie | Pokročilé učenie • Lokálne prostredie • Cloudové nasadenie | Stredne pokročilý | 4-5 hod |
| [⚙️ 04](../../Module04) | [Toolkit optimalizácie modelov](./Module04/README.md) | Optimalizácia naprieč platformami | Úvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Workflow Synthesis | Stredne pokročilý | 5-6 hod |
| [🔧 05](../../Module05) | [SLMOps v produkcii](./Module05/README.md) | Produkčné operácie | Úvod do SLMOps • Destilácia modelov • Jemné doladenie • Nasadenie do produkcie | Pokročilý | 5-6 hod |
| [🤖 06](../../Module06) | [AI agenti a volanie funkcií](./Module06/README.md) | Rámce agentov a MCP | Úvod do agentov • Volanie funkcií • Protokol kontextu modelu | Pokročilý | 4-5 hod |
| [💻 07](../../Module07) | [Implementácia na platforme](./Module07/README.md) | Ukážky naprieč platformami | AI Toolkit • Foundry Local • Vývoj na Windows | Pokročilý | 3-4 hod |
| [🏭 08](../../Module08) | [Toolkit Foundry Local](./Module08/README.md) | Ukážky pripravené na produkciu | Ukážkové aplikácie (pozri podrobnosti nižšie) | Expert | 8-10 hod |

### 🏭 **Modul 08: Ukážkové aplikácie**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: Integrácia OpenAI SDK](./Module08/samples/02/README.md)
- [03: Objavovanie modelov a benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikácia](./Module08/samples/04/README.md)
- [05: Orchestrácia viacerých agentov](./Module08/samples/05/README.md)
- [06: Router modelov ako nástrojov](./Module08/samples/06/README.md)
- [07: Priamy API klient](./Module08/samples/07/README.md)
- [08: Chat aplikácia pre Windows 11](./Module08/samples/08/README.md)
- [09: Pokročilý systém viacerých agentov](./Module08/samples/09/README.md)
- [10: Rámec nástrojov Foundry](./Module08/samples/10/README.md)

### 📊 **Zhrnutie učebnej cesty**
- **Celkové trvanie**: 36-45 hodín
- **Cesta pre začiatočníkov**: Moduly 01-02 (7-9 hodín)  
- **Cesta pre stredne pokročilých**: Moduly 03-04 (9-11 hodín)
- **Cesta pre pokročilých**: Moduly 05-07 (12-15 hodín)
- **Cesta pre expertov**: Modul 08 (8-10 hodín)

## Čo vytvoríte

### 🎯 Kľúčové kompetencie
- **Architektúra Edge AI**: Navrhovanie systémov AI s lokálnym zameraním a integráciou cloudu
- **Optimalizácia modelov**: Kvantizácia a kompresia modelov pre nasadenie na edge (85% zrýchlenie, 75% zmenšenie veľkosti)
- **Nasadenie na viacerých platformách**: Windows, mobilné zariadenia, vstavané systémy a hybridné systémy cloud-edge
- **Produkčné operácie**: Monitorovanie, škálovanie a údržba Edge AI v produkcii

### 🏗️ Praktické projekty
- **Chat aplikácie Foundry Local**: Natívna aplikácia pre Windows 11 s prepínaním modelov
- **Systémy viacerých agentov**: Koordinátor so špecializovanými agentmi pre komplexné pracovné postupy  
- **RAG aplikácie**: Lokálne spracovanie dokumentov s vyhľadávaním vo vektoroch
- **Routery modelov**: Inteligentný výber medzi modelmi na základe analýzy úloh
- **API rámce**: Klienti pripravení na produkciu so streamovaním a monitorovaním zdravia
- **Nástroje naprieč platformami**: Vzory integrácie LangChain/Semantic Kernel

### 🏢 Priemyselné aplikácie
**Výroba** • **Zdravotníctvo** • **Autonómne vozidlá** • **Inteligentné mestá** • **Mobilné aplikácie**

## Rýchly štart

**Odporúčaná učebná cesta** (celkovo 20-30 hodín):

1. **📚 Základy** (Moduly 01-02): Koncepty EdgeAI + rodiny modelov SLM
2. **⚙️ Optimalizácia** (Moduly 03-04): Nasadenie + rámce kvantizácie  
3. **🚀 Produkcia** (Moduly 05-06): SLMOps + AI agenti + volanie funkcií
4. **💻 Implementácia** (Moduly 07-08): Ukážky na platformách + toolkit Foundry Local

Každý modul obsahuje teóriu, praktické cvičenia a ukážky kódu pripravené na produkciu.

## Dopad na kariéru
**Technické role**: EdgeAI Solutions Architect • ML Engineer (Edge) • IoT AI Developer • Mobile AI Developer

**Priemyselné sektory**: Výroba 4.0 • Zdravotnícka technológia • Autonómne systémy • FinTech • Spotrebná elektronika

**Portfólio projektov**: Multi-agentné systémy • Produkčné RAG aplikácie • Nasadenie na viacerých platformách • Optimalizácia výkonu

## Štruktúra repozitára

```
edgeai-for-beginners/
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## Hlavné body kurzu

✅ **Progresívne učenie**: Teória → Prax → Produkčné nasadenie  
✅ **Reálne prípadové štúdie**: Microsoft, Japan Airlines, podnikové implementácie  
✅ **Praktické ukážky**: Viac ako 50 príkladov, 10 komplexných Foundry Local demo ukážok  
✅ **Zameranie na výkon**: Zlepšenie rýchlosti o 85 %, zmenšenie veľkosti o 75 %  
✅ **Viacero platforiem**: Windows, mobilné zariadenia, embedded systémy, cloud-edge hybrid  
✅ **Pripravené na produkciu**: Monitoring, škálovanie, bezpečnosť, rámce pre súlad

📖 **[Študijný sprievodca k dispozícii](STUDY_GUIDE.md)**: Štruktúrovaný 20-hodinový študijný plán s odporúčaním časového rozvrhu a nástrojmi na sebahodnotenie.

---

**EdgeAI predstavuje budúcnosť nasadenia AI**: lokálne zamerané, zachovávajúce súkromie a efektívne. Ovládnite tieto zručnosti a vytvorte ďalšiu generáciu inteligentných aplikácií.

## Ďalšie kurzy

Náš tím vytvára aj ďalšie kurzy! Pozrite si:

- [MCP pre začiatočníkov](https://github.com/microsoft/mcp-for-beginners)
- [AI agenti pre začiatočníkov](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Generatívna AI pre začiatočníkov s .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [Generatívna AI pre začiatočníkov s JavaScriptom](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [Generatívna AI pre začiatočníkov](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML pre začiatočníkov](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [Data Science pre začiatočníkov](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI pre začiatočníkov](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [Kybernetická bezpečnosť pre začiatočníkov](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Webový vývoj pre začiatočníkov](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT pre začiatočníkov](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR vývoj pre začiatočníkov](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Ovládnutie GitHub Copilot pre AI párové programovanie](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [Ovládnutie GitHub Copilot pre C#/.NET vývojárov](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [Vyberte si vlastné dobrodružstvo s Copilotom](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

