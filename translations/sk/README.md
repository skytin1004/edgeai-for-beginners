<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a189d7d9d47816a518ca119d79dc19b",
  "translation_date": "2025-09-22T23:33:59+00:00",
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
2. **Klonujte repozitár**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Pripojte sa na Azure AI Foundry Discord a stretnite sa s odborníkmi a ďalšími vývojármi**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Podpora viacerých jazykov

#### Podporované cez GitHub Action (automatizované a vždy aktuálne)

[Arabčina](../ar/README.md) | [Bengálčina](../bn/README.md) | [Bulharčina](../bg/README.md) | [Barmčina (Mjanmarsko)](../my/README.md) | [Čínština (zjednodušená)](../zh/README.md) | [Čínština (tradičná, Hongkong)](../hk/README.md) | [Čínština (tradičná, Macao)](../mo/README.md) | [Čínština (tradičná, Taiwan)](../tw/README.md) | [Chorvátčina](../hr/README.md) | [Čeština](../cs/README.md) | [Dánčina](../da/README.md) | [Holandčina](../nl/README.md) | [Fínčina](../fi/README.md) | [Francúzština](../fr/README.md) | [Nemčina](../de/README.md) | [Gréčtina](../el/README.md) | [Hebrejčina](../he/README.md) | [Hindčina](../hi/README.md) | [Maďarčina](../hu/README.md) | [Indonézština](../id/README.md) | [Taliančina](../it/README.md) | [Japončina](../ja/README.md) | [Kórejčina](../ko/README.md) | [Malajčina](../ms/README.md) | [Maráthčina](../mr/README.md) | [Nepálčina](../ne/README.md) | [Nórčina](../no/README.md) | [Perzština (Farsi)](../fa/README.md) | [Poľština](../pl/README.md) | [Portugalčina (Brazília)](../br/README.md) | [Portugalčina (Portugalsko)](../pt/README.md) | [Pandžábčina (Gurmukhi)](../pa/README.md) | [Rumunčina](../ro/README.md) | [Ruština](../ru/README.md) | [Srbčina (cyrilika)](../sr/README.md) | [Slovenčina](./README.md) | [Slovinčina](../sl/README.md) | [Španielčina](../es/README.md) | [Swahilčina](../sw/README.md) | [Švédčina](../sv/README.md) | [Tagalog (Filipínčina)](../tl/README.md) | [Thajčina](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinčina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamčina](../vi/README.md)

**Ak chcete podporu ďalších jazykov, zoznam podporovaných jazykov nájdete [tu](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Úvod

Vitajte v **EdgeAI pre začiatočníkov** – vašej komplexnej ceste do transformačného sveta Edge umelej inteligencie. Tento kurz spája silné schopnosti AI s praktickým nasadením v reálnom svete na edge zariadeniach, čo vám umožní využiť potenciál AI priamo tam, kde sa generujú dáta a kde je potrebné robiť rozhodnutia.

### Čo sa naučíte

Tento kurz vás prevedie od základných konceptov až po implementácie pripravené na produkciu, vrátane:
- **Malé jazykové modely (SLMs)** optimalizované pre nasadenie na edge
- **Optimalizácia zohľadňujúca hardvér** na rôznych platformách
- **Inferencia v reálnom čase** s ochranou súkromia
- **Stratégie nasadenia do produkcie** pre podnikové aplikácie

### Prečo je EdgeAI dôležitá

Edge AI predstavuje posun paradigmy, ktorý rieši kľúčové moderné výzvy:
- **Súkromie a bezpečnosť**: Spracovanie citlivých dát lokálne bez vystavenia cloudu
- **Výkon v reálnom čase**: Eliminácia latencie siete pre aplikácie kritické na čas
- **Efektívnosť nákladov**: Zníženie nákladov na šírku pásma a cloudové výpočty
- **Odolné operácie**: Zachovanie funkčnosti počas výpadkov siete
- **Regulačné požiadavky**: Splnenie požiadaviek na suverenitu dát

### Edge AI

Edge AI sa týka spúšťania AI algoritmov a jazykových modelov lokálne na hardvéri – blízko miesta, kde sa generujú dáta – bez spoliehania sa na cloudové zdroje pre inferenciu. Znižuje latenciu, zlepšuje súkromie a umožňuje rozhodovanie v reálnom čase.

### Základné princípy:
- **Inferencia na zariadení**: AI modely bežia na edge zariadeniach (telefóny, routery, mikrokontroléry, priemyselné PC)
- **Offline schopnosti**: Funguje bez trvalého pripojenia na internet
- **Nízka latencia**: Okamžité reakcie vhodné pre systémy v reálnom čase
- **Suverenita dát**: Uchováva citlivé dáta lokálne, čím zlepšuje bezpečnosť a súlad s predpismi

### Malé jazykové modely (SLMs)

SLMs ako Phi-4, Mistral-7B a Gemma sú optimalizované verzie väčších LLMs – trénované alebo destilované pre:
- **Zníženú pamäťovú náročnosť**: Efektívne využitie obmedzenej pamäte edge zariadení
- **Nižšie výpočtové požiadavky**: Optimalizované pre výkon CPU a edge GPU
- **Rýchlejšie spúšťanie**: Rýchla inicializácia pre pohotové aplikácie

Umožňujú silné NLP schopnosti pri splnení obmedzení:
- **Vstavané systémy**: IoT zariadenia a priemyselné kontroléry
- **Mobilné zariadenia**: Smartfóny a tablety s offline schopnosťami
- **IoT zariadenia**: Senzory a inteligentné zariadenia s obmedzenými zdrojmi
- **Edge servery**: Lokálne spracovacie jednotky s obmedzenými GPU zdrojmi
- **Osobné počítače**: Scenáre nasadenia na desktopoch a notebookoch

## Architektúra kurzu

### [Modul 01: Základy EdgeAI a transformácia](./Module01/README.md)
**Téma**: Transformujúci posun nasadenia Edge AI

#### Štruktúra kapitol:
- [**Sekcia 1: Základy EdgeAI**](./Module01/01.EdgeAIFundamentals.md)
  - Porovnanie tradičnej cloud AI a Edge AI
  - Výzvy a obmedzenia edge computingu
  - Kľúčové technológie: kvantizácia modelov, optimalizácia kompresie, malé jazykové modely (SLMs)
  - Hardvérová akcelerácia: NPUs, optimalizácia GPU, optimalizácia CPU
  - Výhody: bezpečnosť súkromia, nízka latencia, offline schopnosti, efektívnosť nákladov

- [**Sekcia 2: Prípadové štúdie z reálneho sveta**](./Module01/02.RealWorldCaseStudies.md)
  - Ekosystém modelov Microsoft Phi & Mu
  - Prípadová štúdia AI reportovacieho systému Japan Airlines
  - Dopad na trh a budúce smerovanie
  - Úvahy o nasadení a najlepšie postupy

- [**Sekcia 3: Praktický sprievodca implementáciou**](./Module01/03.PracticalImplementationGuide.md)
  - Nastavenie vývojového prostredia (Python 3.10+, .NET 8+)
  - Hardvérové požiadavky a odporúčané konfigurácie
  - Zdroje rodiny základných modelov
  - Nástroje na kvantizáciu a optimalizáciu (Llama.cpp, Microsoft Olive, Apple MLX)
  - Kontrolný zoznam hodnotenia a overovania

- [**Sekcia 4: Hardvérové platformy na nasadenie Edge AI**](./Module01/04.EdgeDeployment.md)
  - Úvahy a požiadavky na nasadenie Edge AI
  - Hardvér Intel pre Edge AI a optimalizačné techniky
  - Qualcomm AI riešenia pre mobilné a vstavané systémy
  - NVIDIA Jetson a platformy pre edge computing
  - Windows AI PC platformy s akceleráciou NPU
  - Hardvérovo špecifické optimalizačné stratégie

---

### [Modul 02: Základy malých jazykových modelov](./Module02/README.md)
**Téma**: Teoretické princípy SLM, stratégie implementácie a nasadenie do produkcie

#### Štruktúra kapitol:
- [**Sekcia 1: Základy rodiny modelov Microsoft Phi**](./Module02/01.PhiFamily.md)
  - Vývoj filozofie dizajnu (Phi-1 až Phi-4)
  - Dizajn architektúry s dôrazom na efektívnosť
  - Špecializované schopnosti (uvažovanie, multimodálne, nasadenie na edge)

- [**Sekcia 2: Základy rodiny Qwen**](./Module02/02.QwenFamily.md)
  - Excelentnosť open source (Qwen 1.0 až Qwen3) – dostupné cez Hugging Face
  - Pokročilá architektúra uvažovania s režimom myslenia
  - Možnosti škálovateľného nasadenia (0.5B-235B parametrov)

- [**Sekcia 3: Základy rodiny Gemma**](./Module02/03.GemmaFamily.md)
  - Inovácie poháňané výskumom (Gemma 3 & 3n)
  - Multimodálna excelentnosť
  - Architektúra orientovaná na mobilné zariadenia

- [**Sekcia 4: Základy rodiny BitNET**](./Module02/04.BitNETFamily.md)
  - Revolučná kvantizačná technológia (1.58-bit)
  - Špecializovaný inferenčný rámec z https://github.com/microsoft/BitNet
  - Udržateľné AI vedenie prostredníctvom extrémnej efektívnosti

- [**Sekcia 5: Základy modelu Microsoft Mu**](./Module02/05.mumodel.md)
  - Architektúra orientovaná na zariadenia zabudovaná do Windows 11
  - Systémová integrácia s nastaveniami Windows 11
  - Offline operácia s ochranou súkromia

- [**Sekcia 6: Základy Phi-Silica**](./Module02/06.phisilica.md)
  - Architektúra optimalizovaná pre NPU zabudovaná do Windows 11 Copilot+ PC
  - Výnimočná efektívnosť (650 tokenov/sekundu pri 1.5W)
  - Integrácia pre vývojárov s Windows App SDK

---

### [Modul 03: Nasadenie malých jazykových modelov](./Module03/README.md)
**Téma**: Kompletný životný cyklus nasadenia SLM, od teórie po produkčné prostredie

#### Štruktúra kapitol:
- [**Sekcia 1: Pokročilé učenie SLM**](./Module03/01.SLMAdvancedLearning.md)
  - Rámec klasifikácie parametrov (Micro SLM 100M-1.4B, Medium SLM 14B-30B)
  - Pokročilé optimalizačné techniky (metódy kvantizácie, BitNET 1-bit kvantizácia)
  - Stratégie získavania modelov (Azure AI Foundry pre Phi modely, Hugging Face pre vybrané modely)

- [**Sekcia 2: Nasadenie v lokálnom prostredí**](./Module03/02.DeployingSLMinLocalEnv.md)
  - Univerzálne nasadenie platformy Ollama
  - Lokálne podnikové riešenia Microsoft Foundry
  - Porovnávacia analýza rámcov

- [**Sekcia 3: Kontajnerizované nasadenie v cloude**](./Module03/03.DeployingSLMinCloud.md)
  - vLLM nasadenie inferencie s vysokým výkonom
  - Orchestrace kontajnerov Ollama
  - Implementácia optimalizovaná pre ONNX Runtime

---

### [Modul 04: Konverzia formátu modelu a kvantizácia](./Module04/README.md)
**Téma**: Kompletná sada nástrojov na optimalizáciu modelov pre nasadenie na edge naprieč platformami

#### Štruktúra kapitol:
- [**Sekcia 1: Základy konverzie formátu modelu a kvantizácie**](./Module04/01.Introduce.md)
  - Rámec klasifikácie presnosti (ultra-nízka, nízka, stredná presnosť)
  - Výhody a použitie formátov GGUF a ONNX
  - Výhody kvantizácie pre operačnú efektívnosť
  - Porovnania výkonu a pamäťovej náročnosti
- [**Sekcia 2: Llama.cpp Implementačný sprievodca**](./Module04/02.Llamacpp.md)
  - Inštalácia na rôznych platformách (Windows, macOS, Linux)
  - Konverzia do formátu GGUF a úrovne kvantizácie (Q2_K až Q8_0)
  - Hardvérová akcelerácia (CUDA, Metal, OpenCL, Vulkan)
  - Integrácia s Pythonom a nasadenie REST API

- [**Sekcia 3: Microsoft Olive Optimalizačný balík**](./Module04/03.MicrosoftOlive.md)
  - Optimalizácia modelov prispôsobená hardvéru s viac ako 40 zabudovanými komponentmi
  - Automatická optimalizácia s dynamickou a statickou kvantizáciou
  - Integrácia do podnikových procesov s Azure ML
  - Podpora populárnych modelov (Llama, Phi, vybrané modely Qwen, Gemma)

- [**Sekcia 4: OpenVINO Toolkit Optimalizačný balík**](./Module04/04.openvino.md)
  - Open-source nástroj od Intelu pre nasadenie AI na rôznych platformách
  - Neural Network Compression Framework (NNCF) pre pokročilú optimalizáciu
  - OpenVINO GenAI pre nasadenie veľkých jazykových modelov
  - Hardvérová akcelerácia na CPU, GPU, VPU a AI akcelerátoroch

- [**Sekcia 5: Apple MLX Framework - Detailný pohľad**](./Module04/05.AppleMLX.md)
  - Jednotná pamäťová architektúra pre Apple Silicon
  - Podpora modelov LLaMA, Mistral, Phi, vybrané modely Qwen
  - LoRA jemné doladenie a prispôsobenie modelov
  - Integrácia s Hugging Face s kvantizáciou na 4-bit/8-bit

- [**Sekcia 6: Syntéza pracovného postupu pre Edge AI vývoj**](./Module04/06.workflow-synthesis.md)
  - Jednotná architektúra pracovného postupu integrujúca rôzne optimalizačné rámce
  - Rozhodovacie stromy pre výber rámca a analýza kompromisov výkonu
  - Validácia pripravenosti na produkciu a komplexné stratégie nasadenia
  - Stratégie pre budúce hardvérové a modelové architektúry

---

### [Modul 05: SLMOps - Operácie malých jazykových modelov](./Module05/README.md)
**Téma**: Kompletné operácie životného cyklu SLM od destilácie po produkčné nasadenie

#### Štruktúra kapitol:
- [**Sekcia 1: Úvod do SLMOps**](./Module05/01.IntroduceSLMOps.md)
  - Paradigma SLMOps v AI operáciách
  - Nákladová efektívnosť a architektúra zameraná na ochranu súkromia
  - Strategický obchodný dopad a konkurenčné výhody
  - Výzvy a riešenia pri reálnom nasadení

- [**Sekcia 2: Destilácia modelov - Od teórie k praxi**](./Module05/02.SLMOps-Distillation.md)
  - Prenos znalostí z učiteľských na študentské modely
  - Implementácia dvojstupňového procesu destilácie
  - Pracovné postupy destilácie v Azure ML s praktickými príkladmi
  - 85% zníženie času inferencie pri zachovaní 92% presnosti

- [**Sekcia 3: Jemné doladenie - Prispôsobenie modelov pre špecifické úlohy**](./Module05/03.SLMOps-Finetuing.md)
  - Techniky jemného doladenia s efektívnym využitím parametrov (PEFT)
  - Pokročilé metódy LoRA a QLoRA
  - Implementácia jemného doladenia pomocou Microsoft Olive
  - Tréning s viacerými adaptérmi a optimalizácia hyperparametrov

- [**Sekcia 4: Nasadenie - Implementácia pripravená na produkciu**](./Module05/04.SLMOps.Deployment.md)
  - Konverzia modelov a kvantizácia pre produkciu
  - Konfigurácia nasadenia Foundry Local
  - Benchmarking výkonu a validácia kvality
  - 75% zníženie veľkosti s monitorovaním produkcie

---

### [Modul 06: SLM Agentické systémy - AI agenti a volanie funkcií](./Module06/README.md)
**Téma**: Implementácia SLM agentických systémov od základov po pokročilé volanie funkcií a integráciu Model Context Protocol

#### Štruktúra kapitol:
- [**Sekcia 1: AI agenti a základy malých jazykových modelov**](./Module06/01.IntroduceAgent.md)
  - Rámec klasifikácie agentov (reflexní, modelovo orientovaní, cieľovo orientovaní, učiaci sa agenti)
  - Základy SLM a optimalizačné stratégie (GGUF, kvantizácia, edge rámce)
  - Analýza kompromisov medzi SLM a LLM (10-30× zníženie nákladov, 70-80% efektívnosť úloh)
  - Praktické nasadenie s Ollama, VLLM a Microsoft edge riešeniami

- [**Sekcia 2: Volanie funkcií v malých jazykových modeloch**](./Module06/02.FunctionCalling.md)
  - Systematická implementácia pracovného postupu (detekcia zámeru, výstup JSON, externé vykonanie)
  - Implementácie špecifické pre platformu (Phi-4-mini, vybrané modely Qwen, Microsoft Foundry Local)
  - Pokročilé príklady (spolupráca viacerých agentov, dynamický výber nástrojov)
  - Produkčné aspekty (obmedzenie rýchlosti, auditovanie, bezpečnostné opatrenia)

- [**Sekcia 3: Integrácia Model Context Protocol (MCP)**](./Module06/03.IntroduceMCP.md)
  - Architektúra protokolu a vrstvený systémový dizajn
  - Podpora viacerých backendov (Ollama pre vývoj, vLLM pre produkciu)
  - Protokoly pripojenia (režimy STDIO a SSE)
  - Reálne aplikácie (webová automatizácia, spracovanie dát, integrácia API)

---

### [Modul 07: Ukážky implementácie EdgeAI](./Module07/README.md)
**Téma**: Komplexné implementácie EdgeAI na rôznych platformách a rámcoch

#### Štruktúra kapitol:
- [**AI Toolkit pre Visual Studio Code**](./Module07/aitoolkit.md)
  - Komplexné prostredie pre vývoj Edge AI vo VS Code
  - Katalóg modelov a ich objavovanie pre nasadenie na edge
  - Lokálne testovanie, optimalizácia a vývoj agentov
  - Monitorovanie výkonu a hodnotenie pre edge scenáre

- [**Windows EdgeAI Vývojársky sprievodca**](./Module07/windowdeveloper.md)
  - Komplexný prehľad platformy Windows AI Foundry
  - Phi Silica API pre efektívnu inferenciu na NPU
  - API pre počítačové videnie na spracovanie obrazu a OCR
  - Foundry Local CLI pre lokálny vývoj a testovanie

- [**EdgeAI na NVIDIA Jetson Orin Nano**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 67 TOPS AI výkon v rozmere kreditnej karty
  - Podpora generatívnych AI modelov (vision transformers, LLMs, vision-language models)
  - Aplikácie v robotike, dronoch, inteligentných kamerách, autonómnych zariadeniach
  - Cenovo dostupná platforma za $249 pre demokratizovaný vývoj AI

- [**EdgeAI v mobilných aplikáciách s .NET MAUI a ONNX Runtime GenAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - Cross-platform mobilná AI s jednotným C# kódom
  - Podpora hardvérovej akcelerácie (CPU, GPU, mobilné AI procesory)
  - Optimalizácie špecifické pre platformu (CoreML pre iOS, NNAPI pre Android)
  - Kompletná implementácia generatívneho AI cyklu

- [**EdgeAI v Azure s Small Language Models Engine**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - Hybridná architektúra nasadenia cloud-edge
  - Integrácia Azure AI služieb s ONNX Runtime
  - Nasadenie v podnikovej škále a kontinuálne riadenie modelov
  - Hybridné AI pracovné postupy pre inteligentné spracovanie dokumentov

- [**EdgeAI s Windows ML**](./Module07/README.md#4-edgeai-with-windows-ml)
  - Základy Windows AI Foundry pre výkonnú inferenciu na zariadení
  - Univerzálna podpora hardvéru (AMD, Intel, NVIDIA, Qualcomm silicon)
  - Automatická abstrakcia a optimalizácia hardvéru
  - Jednotný rámec pre rôznorodý ekosystém Windows hardvéru

- [**EdgeAI s Foundry Local aplikáciami**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - Implementácia RAG zameraná na ochranu súkromia s lokálnymi zdrojmi
  - Integrácia jazykového modelu Phi-4 s semantickým vyhľadávaním (iba Phi modely)
  - Podpora lokálnych vektorových databáz (SQLite, Qdrant)
  - Schopnosti pre suverenitu dát a offline operácie

### [Modul 08: Microsoft Foundry Local – Kompletný vývojársky balík](./Module08/README.md)
**Téma**: Vytvárajte, spúšťajte a integrujte AI lokálne s Foundry Local; škálujte a hybridizujte s Azure AI Foundry

#### Štruktúra kapitol:
- [**1: Začíname s Foundry Local**](./Module08/01.FoundryLocalSetup.md)
- [**2: Vytváranie AI riešení s Azure AI Foundry**](./Module08/02.AzureAIFoundryIntegration.md)
- [**3: Open-source modely Foundry Local**](./Module08/03.OpenSourceModels.md)
- [**4: Najmodernejšie modely a inferencia na zariadení**](./Module08/04.CuttingEdgeModels.md)
- [**5: AI agenti s Foundry Local**](./Module08/05.AIPoweredAgents.md)
- [**6: Modely ako nástroje**](./Module08/06.ModelsAsTools.md)

## Ciele kurzu

Po absolvovaní tohto komplexného kurzu EdgeAI získate odborné znalosti na navrhovanie, implementáciu a nasadenie produkčne pripravených EdgeAI riešení. Naša štruktúrovaná metodika vám zabezpečí zvládnutie teoretických základov aj praktických zručností.

### Technické kompetencie

**Základné znalosti**
- Pochopenie základných rozdielov medzi cloudovými a edge AI architektúrami
- Ovládanie princípov kvantizácie, kompresie a optimalizácie modelov pre prostredia s obmedzenými zdrojmi
- Porozumenie možnostiam hardvérovej akcelerácie (NPU, GPU, CPU) a ich dopadom na nasadenie

**Implementačné zručnosti**
- Nasadenie malých jazykových modelov na rôznych edge platformách (mobilné, embedded, IoT, edge servery)
- Aplikácia optimalizačných rámcov vrátane Llama.cpp, Microsoft Olive, ONNX Runtime a Apple MLX
- Implementácia systémov inferencie v reálnom čase s požiadavkami na sub-sekundovú odozvu

**Produkčné znalosti**
- Návrh škálovateľných EdgeAI architektúr pre podnikové aplikácie
- Implementácia monitorovacích, údržbových a aktualizačných stratégií pre nasadené systémy
- Aplikácia bezpečnostných najlepších praktík pre ochranu súkromia v EdgeAI implementáciách

### Strategické schopnosti

**Rámec rozhodovania**
- Hodnotenie príležitostí EdgeAI a identifikácia vhodných prípadov použitia pre obchodné aplikácie
- Posúdenie kompromisov medzi presnosťou modelu, rýchlosťou inferencie, spotrebou energie a nákladmi na hardvér
- Výber vhodných rodín SLM a konfigurácií na základe špecifických obmedzení nasadenia

**Systémová architektúra**
- Návrh end-to-end EdgeAI riešení, ktoré sa integrujú do existujúcej infraštruktúry
- Plánovanie hybridných edge-cloud architektúr pre optimálny výkon a nákladovú efektívnosť
- Implementácia dátových tokov a spracovateľských pipeline pre AI aplikácie v reálnom čase

### Priemyselné aplikácie

**Praktické scenáre nasadenia**
- **Výroba**: Systémy kontroly kvality, prediktívna údržba a optimalizácia procesov
- **Zdravotníctvo**: Diagnostické nástroje s ochranou súkromia a systémy monitorovania pacientov
- **Doprava**: Rozhodovanie autonómnych vozidiel a riadenie dopravy
- **Inteligentné mestá**: Inteligentná infraštruktúra a systémy riadenia zdrojov
- **Spotrebná elektronika**: Mobilné aplikácie poháňané AI a inteligentné domáce zariadenia

## Prehľad očakávaných výsledkov kurzu

### Výsledky učenia Modulu 01:
- Pochopenie základných rozdielov medzi cloudovými a edge AI architektúrami
- Ovládanie základných optimalizačných techník pre edge nasadenie
- Rozpoznanie reálnych aplikácií a úspešných prípadov
- Získanie praktických zručností pre implementáciu EdgeAI riešení

### Výsledky učenia Modulu 02:
- Hlboké pochopenie rôznych filozofií návrhu SLM a ich dopadov na nasadenie
- Ovládanie strategických rozhodovacích schopností na základe výpočtových obmedzení a požiadaviek na výkon
- Pochopenie kompromisov flexibility nasadenia
- Získanie poznatkov pripravených na budúcnosť o efektívnej AI architektúre

### Výsledky učenia Modulu 03:
- Schopnosti strategického výberu modelov
- Ovládanie techník optimalizácie
- Ovládanie flexibility nasadenia
- Schopnosti konfigurácie pripravené na produkciu

### Výsledky učenia Modulu 04:
- Hlboké pochopenie hraníc kvantizácie a praktických aplikácií
- Praktické skúsenosti s viacerými optimalizačnými rámcami (Llama.cpp, Olive, OpenVINO, MLX)
- Ovládanie optimalizácie hardvéru Intel pomocou OpenVINO a NNCF
- Schopnosti výberu optimalizácie prispôsobenej hardvéru na rôznych platformách
- Zručnosti nasadenia pre cross-platform edge výpočtové prostredia
- Strategický výber rámca a syntéza pracovného postupu pre optimálne Edge AI riešenia

### Výsledky učenia Modulu 05:
- Ovládanie paradigmy SLMOps a operačných princípov
- Implementácia destilácie modelov pre prenos znalostí a optimalizáciu efektívnosti
- Aplikácia techník jemného doladenia pre prispôsobenie modelov konkrétnym doménam
- Nasadenie produkčne pripravených SLM riešení s monitorovacími a údržbovými stratégiami

### Výsledky učenia Modulu 06:
- Pochopenie základných konceptov AI agentov a architektúry malých jazykových modelov
- Ovládanie implementácie volania funkcií na rôznych platformách a rámcoch
- Integrácia Model Context Protocol (MCP) pre štandardizovanú interakciu s externými nástrojmi
- Vytváranie sofistikovaných agentických systémov s minimálnymi požiadavkami na ľudskú intervenciu

### Výsledky učenia Modulu 07:
- Ovládanie AI Toolkit pre Visual Studio Code pre komplexné pracovné postupy vývoja Edge AI
- Získanie odborných znalostí o platforme Windows AI Foundry a optimalizačných stratégiách NPU
- Získanie praktických skúseností s rôznymi EdgeAI platformami a implementačnými stratégiami
- Ovládanie techník optimalizácie špecifických pre hardvér na platformách NVIDIA, mobilných zariadeniach, Azure a Windows
- Pochopenie kompromisov nasadenia medzi výkonom, nákladmi a požiadavkami na ochranu súkromia
- Rozvoj praktických zručností pre budovanie reálnych EdgeAI aplikácií v rôznych ekosystémoch

## Očakávané výsledky kur
- **Riadenie rizík**: Identifikácia a zmiernenie technických a prevádzkových rizík pri nasadení EdgeAI
- **Optimalizácia ROI**: Preukázanie merateľnej obchodnej hodnoty z implementácií EdgeAI

### Príležitosti na kariérny rozvoj

**Profesionálne pozície**
- Architekt riešení EdgeAI
- Inžinier strojového učenia (špecializácia na Edge)
- Vývojár IoT AI
- Vývojár mobilných AI aplikácií
- Konzultant pre podnikové AI

**Priemyselné sektory**
- Inteligentná výroba a Priemysel 4.0
- Autonómne vozidlá a doprava
- Zdravotnícka technológia a medicínske zariadenia
- Finančné technológie a bezpečnosť
- Spotrebná elektronika a mobilné aplikácie

### Certifikácia a validácia

**Rozvoj portfólia**
- Dokončenie komplexných EdgeAI projektov preukazujúcich praktické zručnosti
- Nasadenie produkčne pripravených riešení na rôznych hardvérových platformách
- Dokumentácia optimalizačných stratégií a dosiahnutých zlepšení výkonu

**Cesta neustáleho vzdelávania**
- Základ pre pokročilé špecializácie v oblasti AI
- Príprava na hybridné architektúry cloud-edge
- Brána k novým technológiám a rámcom AI

Tento kurz vás umiestni na čelo nasadzovania AI technológií, kde inteligentné schopnosti sú bezproblémovo integrované do zariadení a systémov, ktoré poháňajú moderný život.

## Diagram štruktúry súborov

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
├── Module08/ (Hands on with Foundry Local)
│   ├── 01.FoundryLocalSetup.md
│   ├── 02.AzureAIFoundryIntegration.md
│   ├── 03.OpenSourceModels.md
│   ├── 04.CuttingEdgeModels.md
│   ├── 05.AIPoweredAgents.md
│   ├── 06.ModelsAsTools.md
│   └── README.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md (This file)
├── SECURITY.md
├── STUDY_GUIDE.md
└── SUPPORT.md
```

## Vlastnosti kurzu

- **Progresívne učenie**: Postupný prechod od základných konceptov k pokročilému nasadeniu
- **Integrácia teórie a praxe**: Každý modul obsahuje teoretické základy aj praktické operácie
- **Reálne prípadové štúdie**: Na základe skutočných prípadov od Microsoftu, Alibaba, Google a ďalších
- **Praktické cvičenia**: Kompletné konfiguračné súbory, postupy testovania API a skripty na nasadenie
- **Výkonnostné benchmarky**: Podrobné porovnania rýchlosti inferencie, využitia pamäte a požiadaviek na zdroje
- **Podnikové aspekty**: Praktiky bezpečnosti, rámce súladu a stratégie ochrany údajov

## Začíname

Odporúčaný študijný plán:
1. Začnite s **Module01**, aby ste si vybudovali základné porozumenie EdgeAI
2. Pokračujte s **Module02**, aby ste hlbšie pochopili rôzne rodiny modelov SLM
3. Naučte sa **Module03**, aby ste zvládli praktické zručnosti nasadenia
4. Pokračujte s **Module04** pre pokročilú optimalizáciu modelov, konverziu formátov a syntézu rámcov
5. Dokončite **Module05**, aby ste zvládli SLMOps pre produkčne pripravené implementácie
6. Preskúmajte **Module06**, aby ste pochopili agentické systémy SLM a schopnosti volania funkcií
7. Ukončite s **Module07**, aby ste získali praktické skúsenosti s AI Toolkit a rôznymi príkladmi implementácie EdgeAI
8. Preskúmajte **Module08** pre kompletnú sadu nástrojov Foundry Local pre vývojárov (lokálne zameraný vývoj s hybridnou integráciou Azure)

Každý modul je navrhnutý tak, aby bol samostatne kompletný, ale postupné učenie poskytne najlepšie výsledky.

## Študijný sprievodca

Komplexný [Študijný sprievodca](STUDY_GUIDE.md) je k dispozícii, aby vám pomohol maximalizovať váš študijný zážitok. Študijný sprievodca poskytuje:

- **Štruktúrované študijné plány**: Optimalizované rozvrhy na dokončenie kurzu za 20 hodín
- **Odporúčania na rozdelenie času**: Konkrétne návrhy na vyváženie čítania, cvičení a projektov
- **Zameranie na kľúčové koncepty**: Prioritné učebné ciele pre každý modul
- **Nástroje na sebahodnotenie**: Otázky a cvičenia na testovanie vášho porozumenia
- **Nápady na mini-projekty**: Praktické aplikácie na posilnenie vášho učenia

Študijný sprievodca je navrhnutý tak, aby vyhovoval intenzívnemu učeniu (1 týždeň) aj štúdiu na čiastočný úväzok (3 týždne), s jasnými pokynmi, ako efektívne rozložiť čas, aj keď môžete kurzu venovať len 10 hodín.

---

**Budúcnosť EdgeAI spočíva v neustálom zlepšovaní architektúr modelov, techník kvantizácie a stratégií nasadenia, ktoré uprednostňujú efektivitu a špecializáciu pred všeobecnými schopnosťami. Organizácie, ktoré prijmú tento posun paradigmy, budú dobre pripravené využiť transformačný potenciál AI a zároveň si zachovať kontrolu nad svojimi údajmi a operáciami.**

## Ďalšie kurzy

Náš tím vytvára aj ďalšie kurzy! Pozrite si:

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

