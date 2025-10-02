<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77bb931ce93583c081cf7861f43d9662",
  "translation_date": "2025-10-02T14:19:56+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "sk"
}
-->
# Windows Edge AI Vývojárska Príručka

## Úvod

Vitajte vo svete vývoja Edge AI aplikácií na Windows – komplexnej príručke, ktorá vám pomôže vytvárať inteligentné aplikácie využívajúce silu AI priamo na zariadení prostredníctvom platformy Windows AI Foundry od Microsoftu. Táto príručka je určená pre vývojárov na Windows, ktorí chcú integrovať najmodernejšie Edge AI funkcie do svojich aplikácií a zároveň využiť plný potenciál hardvérovej akcelerácie na Windows.

### Výhody Windows AI

Windows AI Foundry predstavuje jednotnú, spoľahlivú a bezpečnú platformu, ktorá podporuje celý životný cyklus vývoja AI – od výberu a doladenia modelov až po optimalizáciu a nasadenie na CPU, GPU, NPU a hybridné cloudové architektúry. Táto platforma demokratizuje vývoj AI poskytovaním:

- **Hardvérovej abstrakcie**: Jednoduché nasadenie na AMD, Intel, NVIDIA a Qualcomm čipy
- **Inteligencie na zariadení**: AI zachovávajúca súkromie, ktorá beží výhradne na lokálnom hardvéri
- **Optimalizovaného výkonu**: Modely predoptimalizované pre konfigurácie hardvéru na Windows
- **Pripravenosti pre podniky**: Funkcie zabezpečenia a súladu na úrovni produkcie

### Prečo Windows pre Edge AI?

**Univerzálna podpora hardvéru**  
Windows ML automaticky optimalizuje hardvér v celom ekosystéme Windows, čím zabezpečuje, že vaše AI aplikácie budú fungovať optimálne bez ohľadu na architektúru čipu.

**Integrovaný AI Runtime**  
Vstavaný inference engine Windows ML eliminuje zložité požiadavky na nastavenie, čo umožňuje vývojárom sústrediť sa na logiku aplikácie namiesto infraštruktúry.

**Optimalizácia pre Copilot+ PC**  
API navrhnuté špeciálne pre zariadenia novej generácie Windows s dedikovanými Neural Processing Units (NPUs), ktoré poskytujú výnimočný výkon na watt.

**Vývojársky ekosystém**  
Bohaté nástroje vrátane integrácie Visual Studio, komplexnej dokumentácie a ukážkových aplikácií, ktoré urýchľujú vývojové cykly.

## Ciele učenia

Po dokončení tejto príručky pre vývoj Edge AI na Windows získate kľúčové zručnosti potrebné na vytváranie produkčne pripravených AI aplikácií na platforme Windows.

### Základné technické kompetencie

**Ovládanie Windows AI Foundry**  
- Porozumenie architektúre a komponentom platformy Windows AI Foundry  
- Navigácia celým životným cyklom vývoja AI v ekosystéme Windows  
- Implementácia najlepších bezpečnostných praktík pre AI aplikácie na zariadení  
- Optimalizácia aplikácií pre rôzne konfigurácie hardvéru na Windows  

**Expertíza v integrácii API**  
- Ovládanie Windows AI API pre textové, vizuálne a multimodálne aplikácie  
- Implementácia Phi Silica jazykového modelu pre generovanie textu a logické uvažovanie  
- Nasadenie schopností počítačového videnia pomocou vstavaných API na spracovanie obrazu  
- Prispôsobenie predtrénovaných modelov pomocou techník LoRA (Low-Rank Adaptation)  

**Implementácia Foundry Local**  
- Prehliadanie, hodnotenie a nasadenie open-source jazykových modelov pomocou Foundry Local CLI  
- Porozumenie optimalizácii modelov a kvantizácii pre lokálne nasadenie  
- Implementácia offline AI funkcií, ktoré fungujú bez internetového pripojenia  
- Správa životného cyklu modelov a ich aktualizácií v produkčnom prostredí  

**Nasadenie Windows ML**  
- Integrácia vlastných ONNX modelov do aplikácií na Windows pomocou Windows ML  
- Využitie automatickej hardvérovej akcelerácie na CPU, GPU a NPU architektúrach  
- Implementácia inferencie v reálnom čase s optimálnym využitím zdrojov  
- Návrh škálovateľných AI aplikácií pre rôzne kategórie zariadení na Windows  

### Zručnosti vývoja aplikácií

**Vývoj naprieč platformami na Windows**  
- Vytváranie AI aplikácií pomocou .NET MAUI pre univerzálne nasadenie na Windows  
- Integrácia AI funkcií do Win32, UWP a progresívnych webových aplikácií  
- Implementácia responzívnych UI dizajnov, ktoré sa prispôsobujú stavom AI spracovania  
- Spracovanie asynchrónnych AI operácií s vhodnými vzormi používateľskej skúsenosti  

**Optimalizácia výkonu**  
- Profilovanie a optimalizácia výkonu AI inferencie na rôznych konfiguráciách hardvéru  
- Implementácia efektívneho manažmentu pamäte pre veľké jazykové modely  
- Návrh aplikácií, ktoré sa elegantne prispôsobujú dostupným hardvérovým schopnostiam  
- Použitie stratégií cacheovania pre často používané AI operácie  

**Pripravenosť na produkciu**  
- Implementácia komplexného spracovania chýb a záložných mechanizmov  
- Návrh telemetrie a monitorovania výkonu AI aplikácií  
- Aplikácia najlepších bezpečnostných praktík pre lokálne uloženie a vykonávanie AI modelov  
- Plánovanie stratégií nasadenia pre podnikové a spotrebiteľské aplikácie  

### Obchodné a strategické porozumenie

**Architektúra AI aplikácií**  
- Návrh hybridných architektúr, ktoré optimalizujú medzi lokálnym a cloudovým AI spracovaním  
- Hodnotenie kompromisov medzi veľkosťou modelu, presnosťou a rýchlosťou inferencie  
- Plánovanie architektúr toku dát, ktoré zachovávajú súkromie a zároveň umožňujú inteligenciu  
- Implementácia nákladovo efektívnych AI riešení, ktoré sa škálujú podľa požiadaviek používateľov  

**Pozicionovanie na trhu**  
- Porozumenie konkurenčným výhodám Windows-native AI aplikácií  
- Identifikácia prípadov použitia, kde AI na zariadení poskytuje lepší používateľský zážitok  
- Vývoj stratégií uvedenia na trh pre AI aplikácie na Windows  
- Pozicionovanie aplikácií na využitie výhod ekosystému Windows  

## Ukážky AI aplikácií v Windows App SDK

Windows App SDK poskytuje komplexné ukážky, ktoré demonštrujú integráciu AI naprieč rôznymi rámcami a scenármi nasadenia. Tieto ukážky sú nevyhnutné referencie pre pochopenie vzorov vývoja AI na Windows.

### Ukážky Windows AI Foundry

| Ukážka | Rámec | Oblasť zamerania | Kľúčové funkcie |
|--------|-------|------------------|-----------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integrácia Windows AI API | Kompletná WinUI aplikácia demonštrujúca Windows AI API, optimalizáciu pre ARM64, balíčkové nasadenie |

**Kľúčové technológie:**  
- Windows AI API  
- Rámec WinUI 3  
- Optimalizácia pre platformu ARM64  
- Kompatibilita s Copilot+ PC  
- Balíčkové nasadenie aplikácií  

**Predpoklady:**  
- Windows 11 s odporúčaným Copilot+ PC  
- Visual Studio 2022  
- Konfigurácia buildu ARM64  
- Windows App SDK 1.8.1+  

### Ukážky Windows ML

#### Ukážky v C++

| Ukážka | Typ | Oblasť zamerania | Kľúčové funkcie |
|--------|-----|------------------|-----------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikácia | Základy Windows ML | Objavovanie EP, možnosti príkazového riadku, kompilácia modelu |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikácia | Nasadenie rámca | Zdieľaný runtime, menšia stopa nasadenia |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikácia | Samostatné nasadenie | Samostatné nasadenie, bez runtime závislostí |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Použitie knižnice | WindowsML v zdieľanej knižnici, správa pamäte |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet tutoriál | Konverzia modelu, kompilácia EP, Build 2025 tutoriál |

#### Ukážky v C#

**Konzolové aplikácie**

| Ukážka | Typ | Oblasť zamerania | Kľúčové funkcie |
|--------|-----|------------------|-----------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konzolová aplikácia | Základy integrácie C# | Použitie zdieľaných pomocníkov, rozhranie príkazového riadku |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet tutoriál | Konverzia modelu, kompilácia EP, Build 2025 tutoriál |

**GUI aplikácie**

| Ukážka | Rámec | Oblasť zamerania | Kľúčové funkcie |
|--------|-------|------------------|-----------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | Klasifikácia obrazu s rozhraním WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradičné GUI | Klasifikácia obrazu s Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderné GUI | Klasifikácia obrazu s rozhraním WinUI 3 |

#### Ukážky v Pythone

| Ukážka | Jazyk | Oblasť zamerania | Kľúčové funkcie |
|--------|-------|------------------|-----------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Klasifikácia obrazu | WinML Python väzby, dávkové spracovanie obrazu |

### Predpoklady pre ukážky

**Systémové požiadavky:**  
- Windows 11 PC s verziou 24H2 (build 26100) alebo vyššou  
- Visual Studio 2022 s pracovnými záťažami C++ a .NET  
- Windows App SDK 1.8.1 alebo novší  
- Python 3.10-3.13 pre Python ukážky na x64 a ARM64 zariadeniach  

**Špecifické pre Windows AI Foundry:**  
- Odporúčaný Copilot+ PC pre optimálny výkon  
- Konfigurácia buildu ARM64 pre ukážky Windows AI  
- Vyžaduje sa identita balíčka (nepodporujú sa nebalíčkové aplikácie)  

### Bežný pracovný postup ukážok

Väčšina ukážok Windows ML nasleduje tento štandardný vzor:

1. **Inicializácia prostredia** – Vytvorenie ONNX Runtime prostredia  
2. **Registrácia poskytovateľov vykonávania** – Objavenie a registrácia dostupných hardvérových akcelerátorov (CPU, GPU, NPU)  
3. **Načítanie modelu** – Načítanie ONNX modelu, voliteľne kompilácia pre cieľový hardvér  
4. **Predspracovanie vstupu** – Konverzia obrazov/dát na formát vstupu modelu  
5. **Spustenie inferencie** – Vykonanie modelu a získanie predikcií  
6. **Spracovanie výsledkov** – Aplikácia softmaxu a zobrazenie najlepších predikcií  

### Použité súbory modelov

| Model | Účel | Zahrnutý | Poznámky |
|-------|------|----------|----------|
| SqueezeNet | Ľahká klasifikácia obrazu | ✅ Zahrnutý | Predtrénovaný, pripravený na použitie |
| ResNet-50 | Klasifikácia obrazu s vysokou presnosťou | ❌ Vyžaduje konverziu | Použite [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) na konverziu |

### Podpora hardvéru

Všetky ukážky automaticky detegujú a využívajú dostupný hardvér:  
- **CPU** – Univerzálna podpora na všetkých zariadeniach Windows  
- **GPU** – Automatická detekcia a optimalizácia pre dostupný grafický hardvér  
- **NPU** – Využíva Neural Processing Units na podporovaných zariadeniach (Copilot+ PC)  

## Komponenty platformy Windows AI Foundry

### 1. Windows AI API

Windows AI API poskytujú pripravené AI funkcie poháňané modelmi na zariadení, optimalizované pre efektivitu a výkon na zariadeniach Copilot+ PC s minimálnymi požiadavkami na nastavenie.

#### Hlavné kategórie API

**Phi Silica jazykový model**  
- Malý, ale výkonný jazykový model pre generovanie textu a logické uvažovanie  
- Optimalizovaný pre inferenciu v reálnom čase s minimálnou spotrebou energie  
- Podpora vlastného doladenia pomocou techník LoRA  
- Integrácia s Windows semantickým vyhľadávaním a získavaním znalostí  

**API pre počítačové videnie**  
- **Rozpoznávanie textu (OCR)**: Extrakcia textu z obrazov s vysokou presnosťou  
- **Super rozlíšenie obrazu**: Zvýšenie rozlíšenia obrazov pomocou lokálnych AI modelov  
- **Segmentácia obrazu**: Identifikácia a izolácia konkrétnych objektov na obrazoch  
- **Popis obrazu**: Generovanie podrobných textových popisov vizuálneho obsahu  
- **Odstránenie objektov**: Odstránenie nežiaducich objektov z obrazov pomocou AI inpaintingu  

**Multimodálne schopnosti**  
- **Integrácia videnia a jazyka**: Kombinácia porozumenia textu a obrazu  
- **Semantické vyhľadávanie**: Umožnenie prirodzených jazykových dotazov naprieč multimediálnym obsahom  
- **Získavanie znalostí**: Vytváranie inteligentných vyhľadávacích zážitkov s lokálnymi dátami  

### 2. Foundry Local

Foundry Local poskytuje vývojárom rýchly prístup k pripraveným open-source jazykovým modelom na Windows Silicon, ponúkajúc možnosť prehliadať, testovať, interagovať a nasadzovať modely v lokálnych aplikáciách.

#### Ukážkové aplikácie Foundry Local

[Foundry Local repository](https://github.com/microsoft/Foundry-Local/tree/main/samples) poskytuje komplexné ukážky naprieč rôznymi programovacími jazykmi a rámcami, demonštrujúce rôzne vzory integrácie a prípady použitia.

| Ukážka | Jazyk/Rámec | Oblasť zamerania | Kľúčové funkcie |
|--------|-------------|------------------|-----------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementácia RAG | Integrácia Semantic Kernel, Qdrant vektorový úložisko, JINA embeddings, ingestia dokumentov, streamovanie chatu |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Desktopová chat aplikácia | Cross-platform chat, prepínanie lokálnych/cloud modelov, integrácia OpenAI SDK, streamovanie v reálnom čase |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Základná integrácia | Jednoduché použitie SDK, inicializácia modelu, základná funkcia chatu |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-
- **Funkcie**: Výber modelu, streamovanie odpovedí, spracovanie chýb, nasadenie na rôznych platformách  
- **Architektúra**: Hlavný proces Electron, IPC komunikácia, bezpečné preload skripty  

**Príklady integrácie SDK**  
- **JavaScript (Node.js)**: Základná interakcia s modelom a streamovanie odpovedí  
- **Python**: Použitie API kompatibilného s OpenAI s asynchrónnym streamovaním  
- **Rust**: Nízkoúrovňová integrácia s reqwest a tokio pre asynchrónne operácie  

#### Predpoklady pre lokálne vzorky Foundry  

**Systémové požiadavky:**  
- Windows 11 s nainštalovaným Foundry Local  
- Node.js v16+ pre vzorky JavaScript/Electron  
- .NET 8.0+ pre vzorky C#  
- Python 3.10+ pre vzorky Python  
- Rust 1.70+ pre vzorky Rust  

**Inštalácia:**  
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```
  

#### Nastavenie špecifické pre vzorky  

**dotNET RAG vzorka:**  
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```
  
**Electron Chat vzorka:**  
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```
  
**JavaScript/Python/Rust vzorky:**  
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```
  

#### Kľúčové funkcie  

**Katalóg modelov**  
- Komplexná zbierka predoptimalizovaných open-source modelov  
- Modely optimalizované pre CPU, GPU a NPU na okamžité nasadenie  
- Podpora populárnych rodín modelov vrátane Llama, Mistral, Phi a špecializovaných doménových modelov  

**Integrácia CLI**  
- Rozhranie príkazového riadku na správu a nasadenie modelov  
- Automatizované pracovné postupy optimalizácie a kvantizácie  
- Integrácia s populárnymi vývojovými prostrediami a CI/CD pipeline  

**Lokálne nasadenie**  
- Kompletná offline prevádzka bez závislosti na cloude  
- Podpora vlastných formátov a konfigurácií modelov  
- Efektívne poskytovanie modelov s automatickou optimalizáciou hardvéru  

### 3. Windows ML  

Windows ML slúži ako hlavná AI platforma a integrovaný runtime na inferenciu na Windows, umožňujúca vývojárom efektívne nasadiť vlastné modely naprieč širokým ekosystémom hardvéru Windows.  

#### Výhody architektúry  

**Univerzálna podpora hardvéru**  
- Automatická optimalizácia pre AMD, Intel, NVIDIA a Qualcomm čipy  
- Podpora CPU, GPU a NPU s transparentným prepínaním  
- Abstrakcia hardvéru, ktorá eliminuje prácu na optimalizácii špecifickej pre platformu  

**Flexibilita modelov**  
- Podpora formátu modelov ONNX s automatickou konverziou z populárnych frameworkov  
- Nasadenie vlastných modelov s výkonnosťou na úrovni produkcie  
- Integrácia s existujúcimi architektúrami aplikácií Windows  

**Integrácia pre podniky**  
- Kompatibilita s bezpečnostnými a súladovými rámcami Windows  
- Podpora nástrojov na nasadenie a správu pre podniky  
- Integrácia so systémami na správu a monitorovanie zariadení Windows  

## Pracovný postup vývoja  

### Fáza 1: Príprava prostredia a konfigurácia nástrojov  

**Príprava vývojového prostredia**  
1. Nainštalujte Visual Studio 2022 s pracovnými záťažami C++ a .NET  
2. Nainštalujte Windows App SDK 1.8.1 alebo novšiu verziu  
3. Konfigurujte nástroje CLI Windows AI Foundry  
4. Nastavte rozšírenie AI Toolkit pre Visual Studio Code  
5. Zabezpečte nástroje na profilovanie výkonu a monitorovanie  
6. Uistite sa, že je nastavená konfigurácia ARM64 pre optimalizáciu Copilot+ PC  

**Nastavenie vzorového repozitára**  
1. Naklonujte [repozitár vzoriek Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)  
2. Prejdite do `Samples/WindowsAIFoundry/cs-winui` pre príklady API Windows AI  
3. Prejdite do `Samples/WindowsML` pre komplexné príklady Windows ML  
4. Skontrolujte [požiadavky na zostavenie](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) pre vaše cieľové platformy  

**Preskúmanie galérie AI Dev**  
- Preskúmajte vzorové aplikácie a referenčné implementácie  
- Testujte API Windows AI s interaktívnymi ukážkami  
- Skontrolujte zdrojový kód pre osvedčené postupy a vzory  
- Identifikujte relevantné vzorky pre váš konkrétny prípad použitia  

### Fáza 2: Výber a integrácia modelu  

**Analýza požiadaviek**  
- Definujte funkčné požiadavky na AI schopnosti  
- Stanovte obmedzenia výkonu a ciele optimalizácie  
- Vyhodnoťte požiadavky na ochranu súkromia a bezpečnosť  
- Naplánujte architektúru nasadenia a stratégie škálovania  

**Hodnotenie modelu**  
- Použite Foundry Local na testovanie open-source modelov pre váš prípad použitia  
- Porovnajte API Windows AI s požiadavkami na vlastné modely  
- Vyhodnoťte kompromisy medzi veľkosťou modelu, presnosťou a rýchlosťou inferencie  
- Prototypujte integračné prístupy s vybranými modelmi  

### Fáza 3: Vývoj aplikácie  

**Základná integrácia**  
- Implementujte integráciu API Windows AI s riadnym spracovaním chýb  
- Navrhnite používateľské rozhrania, ktoré zohľadňujú pracovné postupy AI spracovania  
- Implementujte stratégie ukladania do vyrovnávacej pamäte a optimalizácie pre inferenciu modelov  
- Pridajte telemetriu a monitorovanie výkonu AI operácií  

**Testovanie a validácia**  
- Testujte aplikácie na rôznych hardvérových konfiguráciách Windows  
- Validujte metriky výkonu pri rôznych podmienkach zaťaženia  
- Implementujte automatizované testovanie pre spoľahlivosť AI funkcií  
- Vykonajte testovanie používateľskej skúsenosti s funkciami vylepšenými AI  

### Fáza 4: Optimalizácia a nasadenie  

**Optimalizácia výkonu**  
- Profilujte výkon aplikácie na cieľových hardvérových konfiguráciách  
- Optimalizujte využitie pamäte a stratégie načítania modelov  
- Implementujte adaptívne správanie na základe dostupných hardvérových schopností  
- Doladte používateľskú skúsenosť pre rôzne scenáre výkonu  

**Nasadenie do produkcie**  
- Zabaľte aplikácie s riadnymi závislosťami AI modelov  
- Implementujte mechanizmy aktualizácie modelov a logiky aplikácie  
- Konfigurujte monitorovanie a analytiku pre produkčné prostredia  
- Naplánujte stratégie nasadenia pre podnikové a spotrebiteľské aplikácie  

## Praktické príklady implementácie  

### Príklad 1: Inteligentná aplikácia na spracovanie dokumentov  

Vytvorte aplikáciu Windows, ktorá spracováva dokumenty pomocou viacerých AI schopností:  

**Použité technológie:**  
- Phi Silica na sumarizáciu dokumentov a odpovedanie na otázky  
- OCR API na extrakciu textu zo skenovaných dokumentov  
- API na popis obrázkov pre analýzu grafov a diagramov  
- Vlastné ONNX modely na klasifikáciu dokumentov  

**Prístup k implementácii:**  
- Navrhnite modulárnu architektúru s pripojiteľnými AI komponentmi  
- Implementujte asynchrónne spracovanie pre veľké dávky dokumentov  
- Pridajte indikátory pokroku a podporu zrušenia pre dlhodobé operácie  
- Zahrňte offline schopnosti pre spracovanie citlivých dokumentov  

### Príklad 2: Systém na správu maloobchodných zásob  

Vytvorte AI-poháňaný systém na správu zásob pre maloobchodné aplikácie:  

**Použité technológie:**  
- Segmentácia obrázkov na identifikáciu produktov  
- Vlastné vizuálne modely na klasifikáciu značiek a kategórií  
- Lokálne nasadenie špecializovaných jazykových modelov pre maloobchod  
- Integrácia s existujúcimi POS a systémami zásob  

**Prístup k implementácii:**  
- Vytvorte integráciu kamery na skenovanie produktov v reálnom čase  
- Implementujte rozpoznávanie čiarových kódov a vizuálnych produktov  
- Pridajte dotazy na zásoby v prirodzenom jazyku pomocou lokálnych jazykových modelov  
- Navrhnite škálovateľnú architektúru pre nasadenie vo viacerých predajniach  

### Príklad 3: Asistent na dokumentáciu v zdravotníctve  

Vyvinúť nástroj na dokumentáciu v zdravotníctve, ktorý zachováva súkromie:  

**Použité technológie:**  
- Phi Silica na generovanie lekárskych poznámok a podporu klinického rozhodovania  
- OCR na digitalizáciu ručne písaných lekárskych záznamov  
- Vlastné lekárske jazykové modely nasadené cez Windows ML  
- Lokálne vektorové úložisko na vyhľadávanie lekárskych znalostí  

**Prístup k implementácii:**  
- Zabezpečte úplnú offline prevádzku pre ochranu súkromia pacientov  
- Implementujte validáciu a návrhy lekárskej terminológie  
- Pridajte protokolovanie auditu pre súlad s reguláciami  
- Navrhnite integráciu s existujúcimi systémami elektronických zdravotných záznamov  

## Stratégie optimalizácie výkonu  

### Vývoj zohľadňujúci hardvér  

**Optimalizácia pre NPU**  
- Navrhnite aplikácie na využitie schopností NPU na Copilot+ PC  
- Implementujte plynulý prechod na GPU/CPU na zariadeniach bez NPU  
- Optimalizujte formáty modelov pre akceleráciu špecifickú pre NPU  
- Monitorujte využitie NPU a tepelné charakteristiky  

**Správa pamäte**  
- Implementujte efektívne stratégie načítania a ukladania modelov do vyrovnávacej pamäte  
- Použite mapovanie pamäte pre veľké modely na zníženie času spustenia  
- Navrhnite aplikácie šetrné k pamäti pre zariadenia s obmedzenými zdrojmi  
- Implementujte kvantizáciu modelov na optimalizáciu pamäte  

**Efektivita batérie**  
- Optimalizujte AI operácie na minimálnu spotrebu energie  
- Implementujte adaptívne spracovanie na základe stavu batérie  
- Navrhnite efektívne spracovanie na pozadí pre kontinuálne AI operácie  
- Použite nástroje na profilovanie energie na optimalizáciu spotreby  

### Úvahy o škálovateľnosti  

**Multithreading**  
- Navrhnite bezpečné AI operácie pre súbežné spracovanie  
- Implementujte efektívne rozdelenie práce medzi dostupné jadrá  
- Použite vzory async/await na neblokujúce AI operácie  
- Naplánujte optimalizáciu thread poolu pre rôzne hardvérové konfigurácie  

**Stratégie ukladania do vyrovnávacej pamäte**  
- Implementujte inteligentné ukladanie do vyrovnávacej pamäte pre často používané AI operácie  
- Navrhnite stratégie invalidácie vyrovnávacej pamäte pre aktualizácie modelov  
- Použite trvalé ukladanie do vyrovnávacej pamäte pre nákladné operácie predspracovania  
- Implementujte distribuované ukladanie do vyrovnávacej pamäte pre scenáre s viacerými používateľmi  

## Najlepšie postupy pre bezpečnosť a ochranu súkromia  

### Ochrana údajov  

**Lokálne spracovanie**  
- Zabezpečte, aby citlivé údaje nikdy neopustili lokálne zariadenie  
- Implementujte bezpečné úložisko pre AI modely a dočasné údaje  
- Použite bezpečnostné funkcie Windows na sandboxing aplikácií  
- Aplikujte šifrovanie na uložené modely a výsledky medzistupňového spracovania  

**Bezpečnosť modelov**  
- Validujte integritu modelov pred ich načítaním a vykonaním  
- Implementujte bezpečné mechanizmy aktualizácie modelov  
- Použite podpísané modely na zabránenie manipulácii  
- Aplikujte kontrolu prístupu na súbory modelov a konfigurácie  

### Úvahy o súlade  

**Regulačné požiadavky**  
- Navrhnite aplikácie tak, aby spĺňali GDPR, HIPAA a ďalšie regulačné požiadavky  
- Implementujte protokolovanie auditu pre procesy rozhodovania AI  
- Poskytnite funkcie transparentnosti pre výsledky generované AI  
- Umožnite používateľom kontrolu nad spracovaním údajov AI  

**Bezpečnosť pre podniky**  
- Integrujte s bezpečnostnými politikami Windows pre podniky  
- Podporte spravované nasadenie prostredníctvom nástrojov na správu podnikov  
- Implementujte kontrolu prístupu na základe rolí pre funkcie AI  
- Poskytnite administratívne ovládacie prvky pre funkčnosť AI  

## Riešenie problémov a ladenie  

### Bežné vývojové výzvy  

**Problémy s konfiguráciou zostavenia**  
- Uistite sa, že je nastavená konfigurácia platformy ARM64 pre vzorky API Windows AI  
- Overte kompatibilitu verzie Windows App SDK (vyžaduje sa 1.8.1+)  
- Skontrolujte, či je správne nakonfigurovaná identita balíka (vyžaduje sa pre API Windows AI)  
- Validujte, že nástroje na zostavenie podporujú cieľovú verziu frameworku  

**Problémy s načítaním modelov**  
- Validujte kompatibilitu modelov ONNX s Windows ML  
- Skontrolujte integritu súborov modelov a požiadavky na formát  
- Overte požiadavky na schopnosti hardvéru pre konkrétne modely  
- Ladiť problémy s alokáciou pamäte počas načítania modelov  
- Uistite sa, že je zaregistrovaný poskytovateľ vykonávania pre hardvérovú akceleráciu  

**Úvahy o režime nasadenia**  
- **Režim samostatného balíka**: Plne podporovaný s väčšou veľkosťou nasadenia  
- **Režim závislý na frameworku**: Menšia stopa, ale vyžaduje zdieľaný runtime  
- **Neprebalené aplikácie**: Už nie sú podporované pre API Windows AI  
- Použite `dotnet run -p:Platform=ARM64 -p:SelfContained=true` pre samostatné nasadenie ARM64  

**Problémy s výkonom**  
- Profilujte výkon aplikácie na rôznych hardvérových konfiguráciách  
- Identifikujte úzke miesta v pipeline spracovania AI  
- Optimalizujte operácie predspracovania a postspracovania údajov  
- Implementujte monitorovanie výkonu a upozornenia  

**Problémy s integráciou**  
- Ladiť problémy s integráciou API s riadnym spracovaním chýb  
- Validujte formáty vstupných údajov a požiadavky na predspracovanie  
- Dôkladne testujte hraničné prípady a podmienky chýb  
- Implementujte komplexné protokolovanie na ladenie problémov v produkcii  

### Nástroje a techniky ladenia  

**Integrácia Visual Studio**  
- Použite debugger AI Toolkit na analýzu vykonávania modelov  
- Implementujte profilovanie výkonu pre AI operácie  
- Ladiť asynchrónne AI operácie s riadnym spracovaním výnimiek  
- Použite nástroje na profilovanie pamäte na optimalizáciu  

**Nástroje Windows AI Foundry**  
- Využite CLI Foundry Local na testovanie a validáciu modelov  
- Použite nástroje na testovanie API Windows AI na overenie integrácie  
- Implementujte vlastné protokolovanie na monitorovanie AI operácií  
- Vytvorte automatizované testovanie pre spoľahlivosť AI funkcií  

## Budúce zabezpečenie vašich aplikácií  

### Nové technológie  

**Hardvér novej generácie**  
- Navrhnite aplikácie na využitie budúcich schopností NPU  
- Plánujte pre zvýšené veľkosti modelov a zložitosť  
- Implementujte adaptívne architekt
- [Windows App SDK Samples Repository](https://github.com/microsoft/WindowsAppSDK-Samples)

### Vývojárske nástroje
- [AI Toolkit pre Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Ukážky](https://learn.microsoft.com/windows/ai/samples/)
- [Nástroje na konverziu modelov](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Technická podpora
- [Windows ML Dokumentácia](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Dokumentácia](https://onnxruntime.ai/docs/)
- [Windows App SDK Dokumentácia](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Nahlásiť problémy - Windows App SDK Samples](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Komunita a podpora
- [Windows Developer Community](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Tréning](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Tento sprievodca je navrhnutý tak, aby sa vyvíjal spolu s rýchlo napredujúcim ekosystémom Windows AI. Pravidelné aktualizácie zabezpečujú súlad s najnovšími schopnosťami platformy a najlepšími postupmi vývoja.*

[08. Praktické cvičenie s Microsoft Foundry Local - Kompletná sada nástrojov pre vývojárov](../Module08/README.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.