<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77bb931ce93583c081cf7861f43d9662",
  "translation_date": "2025-10-02T14:12:03+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "cs"
}
-->
# Windows Edge AI Vývojářský Průvodce

## Úvod

Vítejte ve světě vývoje Edge AI na Windows – komplexním průvodci pro tvorbu inteligentních aplikací využívajících sílu AI přímo na zařízení pomocí platformy Windows AI Foundry od Microsoftu. Tento průvodce je určen vývojářům na Windows, kteří chtějí integrovat nejmodernější funkce Edge AI do svých aplikací a zároveň využít plný potenciál hardwarové akcelerace na Windows.

### Výhody Windows AI

Windows AI Foundry představuje jednotnou, spolehlivou a bezpečnou platformu podporující celý životní cyklus vývoje AI – od výběru a doladění modelu až po optimalizaci a nasazení na CPU, GPU, NPU a hybridní cloudové architektury. Tato platforma demokratizuje vývoj AI díky:

- **Abstrakci hardwaru**: Bezproblémové nasazení na AMD, Intel, NVIDIA a Qualcomm čipech
- **Inteligenci na zařízení**: AI zachovávající soukromí, která běží výhradně na lokálním hardwaru
- **Optimalizovanému výkonu**: Modely předem optimalizované pro konfigurace hardwaru Windows
- **Připravenosti pro podniky**: Funkce zabezpečení a shody na úrovni produkce

### Proč Windows pro Edge AI?

**Univerzální podpora hardwaru**  
Windows ML automaticky optimalizuje hardware v celém ekosystému Windows, což zajišťuje, že vaše AI aplikace budou fungovat optimálně bez ohledu na architekturu čipu.

**Integrovaný AI Runtime**  
Vestavěný inference engine Windows ML eliminuje složité požadavky na nastavení, což umožňuje vývojářům soustředit se na logiku aplikace místo infrastruktury.

**Optimalizace pro Copilot+ PC**  
API navržené speciálně pro zařízení nové generace Windows s dedikovanými Neural Processing Units (NPUs) poskytují výjimečný výkon na watt.

**Ekosystém pro vývojáře**  
Bohaté nástroje včetně integrace Visual Studio, komplexní dokumentace a ukázkových aplikací urychlují vývojové cykly.

## Cíle učení

Po dokončení tohoto průvodce vývojem Edge AI na Windows získáte klíčové dovednosti pro tvorbu produkčně připravených AI aplikací na platformě Windows.

### Klíčové technické kompetence

**Ovládnutí Windows AI Foundry**  
- Porozumění architektuře a komponentám platformy Windows AI Foundry  
- Navigace celým životním cyklem vývoje AI v ekosystému Windows  
- Implementace bezpečnostních osvědčených postupů pro AI aplikace na zařízení  
- Optimalizace aplikací pro různé konfigurace hardwaru Windows  

**Expertíza v integraci API**  
- Ovládnutí Windows AI API pro text, obraz a multimodální aplikace  
- Implementace integrace jazykového modelu Phi Silica pro generování textu a logické úvahy  
- Nasazení funkcí počítačového vidění pomocí vestavěných API pro zpracování obrazu  
- Přizpůsobení předtrénovaných modelů pomocí technik LoRA (Low-Rank Adaptation)  

**Implementace Foundry Local**  
- Procházení, hodnocení a nasazení open-source jazykových modelů pomocí Foundry Local CLI  
- Porozumění optimalizaci modelů a kvantizaci pro lokální nasazení  
- Implementace offline AI funkcí, které fungují bez připojení k internetu  
- Správa životního cyklu modelů a aktualizací v produkčním prostředí  

**Nasazení Windows ML**  
- Integrace vlastních ONNX modelů do aplikací Windows pomocí Windows ML  
- Využití automatické hardwarové akcelerace na CPU, GPU a NPU architekturách  
- Implementace inference v reálném čase s optimálním využitím zdrojů  
- Návrh škálovatelných AI aplikací pro různé kategorie zařízení Windows  

### Dovednosti vývoje aplikací

**Vývoj napříč platformami na Windows**  
- Tvorba AI aplikací pomocí .NET MAUI pro univerzální nasazení na Windows  
- Integrace AI funkcí do Win32, UWP a progresivních webových aplikací  
- Implementace responzivních UI designů, které se přizpůsobují stavům zpracování AI  
- Správa asynchronních AI operací s ohledem na uživatelskou zkušenost  

**Optimalizace výkonu**  
- Profilování a optimalizace výkonu inference AI na různých konfiguracích hardwaru  
- Implementace efektivní správy paměti pro velké jazykové modely  
- Návrh aplikací, které se přizpůsobují dostupným hardwarovým schopnostem  
- Použití strategií ukládání do mezipaměti pro často používané AI operace  

**Připravenost na produkci**  
- Implementace komplexního zpracování chyb a záložních mechanismů  
- Návrh telemetrie a monitorování výkonu AI aplikací  
- Aplikace bezpečnostních osvědčených postupů pro lokální úložiště a spuštění AI modelů  
- Plánování strategií nasazení pro podnikové i spotřebitelské aplikace  

### Obchodní a strategické porozumění

**Architektura AI aplikací**  
- Návrh hybridních architektur optimalizujících mezi lokálním a cloudovým zpracováním AI  
- Hodnocení kompromisů mezi velikostí modelu, přesností a rychlostí inference  
- Plánování architektur toku dat, které zachovávají soukromí a zároveň umožňují inteligenci  
- Implementace nákladově efektivních AI řešení, která se škálují podle požadavků uživatelů  

**Pozice na trhu**  
- Porozumění konkurenčním výhodám AI aplikací nativních pro Windows  
- Identifikace případů použití, kde AI na zařízení poskytuje lepší uživatelskou zkušenost  
- Vývoj strategií uvedení na trh pro AI aplikace na Windows  
- Pozicování aplikací tak, aby využívaly výhody ekosystému Windows  

## Ukázky AI ve Windows App SDK

Windows App SDK poskytuje komplexní ukázky demonstrující integraci AI napříč různými frameworky a scénáři nasazení. Tyto ukázky jsou klíčovými referencemi pro pochopení vzorů vývoje AI na Windows.

### Ukázky Windows AI Foundry

| Ukázka | Framework | Oblast zaměření | Klíčové funkce |
|--------|-----------|-----------------|----------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integrace Windows AI API | Kompletní aplikace WinUI demonstrující Windows AI API, optimalizaci pro ARM64, balíčkové nasazení |

**Klíčové technologie:**  
- Windows AI API  
- Framework WinUI 3  
- Optimalizace pro platformu ARM64  
- Kompatibilita s Copilot+ PC  
- Balíčkové nasazení aplikace  

**Předpoklady:**  
- Windows 11 s doporučeným Copilot+ PC  
- Visual Studio 2022  
- Konfigurace sestavení ARM64  
- Windows App SDK 1.8.1+  

### Ukázky Windows ML

#### Ukázky v C++

| Ukázka | Typ | Oblast zaměření | Klíčové funkce |
|--------|------|-----------------|----------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikace | Základy Windows ML | Objevování EP, možnosti příkazové řádky, kompilace modelu |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikace | Nasazení frameworku | Sdílený runtime, menší stopa nasazení |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikace | Samostatné nasazení | Samostatné nasazení, žádné runtime závislosti |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Použití knihovny | WindowsML v sdílené knihovně, správa paměti |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet tutoriál | Konverze modelu, kompilace EP, tutoriál Build 2025 |

#### Ukázky v C#

**Konzolové aplikace**

| Ukázka | Typ | Oblast zaměření | Klíčové funkce |
|--------|------|-----------------|----------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konzolová aplikace | Základy integrace C# | Použití sdílených pomocníků, rozhraní příkazové řádky |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet tutoriál | Konverze modelu, kompilace EP, tutoriál Build 2025 |

**GUI aplikace**

| Ukázka | Framework | Oblast zaměření | Klíčové funkce |
|--------|-----------|-----------------|----------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | Klasifikace obrazu s rozhraním WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradiční GUI | Klasifikace obrazu s Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderní GUI | Klasifikace obrazu s rozhraním WinUI 3 |

#### Ukázky v Pythonu

| Ukázka | Jazyk | Oblast zaměření | Klíčové funkce |
|--------|-------|-----------------|----------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Klasifikace obrazu | WinML Python bindings, dávkové zpracování obrazu |

### Předpoklady pro ukázky

**Systémové požadavky:**  
- PC s Windows 11 verze 24H2 (build 26100) nebo vyšší  
- Visual Studio 2022 s pracovními zátěžemi C++ a .NET  
- Windows App SDK 1.8.1 nebo novější  
- Python 3.10–3.13 pro ukázky v Pythonu na zařízeních x64 a ARM64  

**Specifické pro Windows AI Foundry:**  
- Doporučený Copilot+ PC pro optimální výkon  
- Konfigurace sestavení ARM64 pro ukázky Windows AI  
- Vyžadována identita balíčku (nepodporovány aplikace bez balíčku)  

### Společný pracovní postup ukázek

Většina ukázek Windows ML následuje tento standardní vzor:

1. **Inicializace prostředí** – Vytvoření prostředí ONNX Runtime  
2. **Registrace poskytovatelů výkonu** – Objevování a registrace dostupných hardwarových akcelerátorů (CPU, GPU, NPU)  
3. **Načtení modelu** – Načtení ONNX modelu, volitelně kompilace pro cílový hardware  
4. **Předzpracování vstupu** – Konverze obrazů/dat do formátu vstupu modelu  
5. **Spuštění inference** – Spuštění modelu a získání predikcí  
6. **Zpracování výsledků** – Použití softmaxu a zobrazení nejlepších predikcí  

### Použité soubory modelů

| Model | Účel | Zahrnuto | Poznámky |
|-------|------|----------|----------|
| SqueezeNet | Lehká klasifikace obrazu | ✅ Zahrnuto | Předtrénováno, připraveno k použití |
| ResNet-50 | Klasifikace obrazu s vysokou přesností | ❌ Vyžaduje konverzi | Použijte [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) pro konverzi |

### Podpora hardwaru

Všechny ukázky automaticky detekují a využívají dostupný hardware:  
- **CPU** – Univerzální podpora na všech zařízeních Windows  
- **GPU** – Automatická detekce a optimalizace pro dostupný grafický hardware  
- **NPU** – Využití Neural Processing Units na podporovaných zařízeních (Copilot+ PC)  

## Komponenty platformy Windows AI Foundry

### 1. Windows AI API

Windows AI API poskytují připravené AI funkce poháněné modely na zařízení, optimalizované pro efektivitu a výkon na zařízeních Copilot+ PC s minimálními požadavky na nastavení.

#### Klíčové kategorie API

**Jazykový model Phi Silica**  
- Malý, ale výkonný jazykový model pro generování textu a logické úvahy  
- Optimalizováno pro inference v reálném čase s minimální spotřebou energie  
- Podpora vlastního doladění pomocí technik LoRA  
- Integrace s vyhledáváním a získáváním znalostí na Windows  

**API pro počítačové vidění**  
- **Rozpoznávání textu (OCR)**: Extrakce textu z obrazů s vysokou přesností  
- **Super rozlišení obrazu**: Zvýšení rozlišení obrazů pomocí lokálních AI modelů  
- **Segmentace obrazu**: Identifikace a izolace specifických objektů na obrazech  
- **Popis obrazu**: Generování podrobných textových popisů vizuálního obsahu  
- **Odstranění objektů**: Odstranění nežádoucích objektů z obrazů pomocí AI-powered inpaintingu  

**Multimodální schopnosti**  
- **Integrace vidění a jazyka**: Kombinace porozumění textu a obrazu  
- **Semantické vyhledávání**: Umožnění přirozených jazykových dotazů napříč multimediálním obsahem  
- **Získávání znalostí**: Tvorba inteligentních vyhledávacích zkušeností s lokálními daty  

### 2. Foundry Local

Foundry Local poskytuje vývojářům rychlý přístup k připraveným open-source jazykovým modelům na Windows Silicon, umožňující procházení, testování, interakci a nasazení modelů v lokálních aplikacích.

#### Ukázkové aplikace Foundry Local

[Repozitář Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) poskytuje komplexní ukázky napříč různými programovacími jazyky a frameworky, demonstrující různé vzory integrace a případy použití.

| Ukázka | Jazyk/Framework | Oblast zaměření | Klíčové funkce |
|--------|-----------------|-----------------|----------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementace RAG | Integrace Semantic Kernel, Qdrant vektorový úložiště, JINA embeddings, ingestace dokumentů, streamování chatu |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Desktopová chatovací aplikace | Cross-platform chat, přepínání mezi lokálním/cloudovým modelem, integrace OpenAI SDK, streamování v reálném čase |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Základní integrace | Jednoduché použití SDK, inicializace modelu, základní funkce chatu |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Základní integrace | Použití Python SDK, streamování odpovědí, OpenAI-kompatibilní API |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Systémová integrace | Nízkoúrovňové použití SDK, asynchronní operace, reqwest HTTP klient |

#### Kategorie ukázek podle případu použití

**RAG (Retrieval-Augmented Generation)**  
- **dotNET/rag**: Kompletní implementace RAG pomocí Semantic Kernel, Qdrant vektorové databáze a JINA embeddings  
- **Architektura**: Ingestace dokumentů → Rozdělení textu →
- **Funkce**: Výběr modelu, streamování odpovědí, zpracování chyb, nasazení napříč platformami  
- **Architektura**: Hlavní proces Electron, komunikace IPC, bezpečné preload skripty  

**Příklady integrace SDK**  
- **JavaScript (Node.js)**: Základní interakce s modelem a streamování odpovědí  
- **Python**: Použití API kompatibilního s OpenAI s asynchronním streamováním  
- **Rust**: Nízká úroveň integrace s reqwest a tokio pro asynchronní operace  

#### Požadavky pro lokální vzorky Foundry  

**Systémové požadavky:**  
- Windows 11 s nainstalovaným Foundry Local  
- Node.js v16+ pro vzorky v JavaScriptu/Electronu  
- .NET 8.0+ pro vzorky v C#  
- Python 3.10+ pro vzorky v Pythonu  
- Rust 1.70+ pro vzorky v Rustu  

**Instalace:**  
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```
  

#### Nastavení specifické pro vzorky  

**dotNET RAG vzorek:**  
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
  
**Electron Chat vzorek:**  
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
  

#### Klíčové funkce  

**Katalog modelů**  
- Komplexní sbírka předem optimalizovaných open-source modelů  
- Modely optimalizované pro CPU, GPU a NPU pro okamžité nasazení  
- Podpora populárních rodin modelů, včetně Llama, Mistral, Phi a specializovaných doménových modelů  

**Integrace CLI**  
- Rozhraní příkazového řádku pro správu a nasazení modelů  
- Automatizované pracovní postupy optimalizace a kvantizace  
- Integrace s populárními vývojovými prostředími a CI/CD pipeline  

**Lokální nasazení**  
- Kompletní offline provoz bez závislosti na cloudu  
- Podpora vlastních formátů a konfigurací modelů  
- Efektivní obsluha modelů s automatickou optimalizací hardwaru  

### 3. Windows ML  

Windows ML slouží jako hlavní AI platforma a integrované runtime prostředí pro inferenci na Windows, umožňující vývojářům efektivně nasazovat vlastní modely napříč širokým ekosystémem hardwaru Windows.  

#### Výhody architektury  

**Univerzální podpora hardwaru**  
- Automatická optimalizace pro AMD, Intel, NVIDIA a Qualcomm čipy  
- Podpora CPU, GPU a NPU s transparentním přepínáním  
- Abstrakce hardwaru, která eliminuje práci na optimalizaci specifické pro platformu  

**Flexibilita modelů**  
- Podpora formátu modelů ONNX s automatickou konverzí z populárních frameworků  
- Nasazení vlastních modelů s výkonem na úrovni produkce  
- Integrace s existujícími architekturami aplikací Windows  

**Podniková integrace**  
- Kompatibilita s bezpečnostními a compliance frameworky Windows  
- Podpora podnikových nástrojů pro nasazení a správu  
- Integrace s nástroji pro správu a monitorování zařízení Windows  

## Pracovní postup vývoje  

### Fáze 1: Nastavení prostředí a konfigurace nástrojů  

**Příprava vývojového prostředí**  
1. Nainstalujte Visual Studio 2022 s pracovními zátěžemi C++ a .NET  
2. Nainstalujte Windows App SDK 1.8.1 nebo novější  
3. Nakonfigurujte nástroje CLI Windows AI Foundry  
4. Nastavte rozšíření AI Toolkit pro Visual Studio Code  
5. Zajistěte nástroje pro profilování výkonu a monitorování  
6. Zajistěte konfiguraci ARM64 build pro optimalizaci Copilot+ PC  

**Nastavení repozitáře vzorků**  
1. Naklonujte [repozitář vzorků Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)  
2. Přejděte do `Samples/WindowsAIFoundry/cs-winui` pro příklady API Windows AI  
3. Přejděte do `Samples/WindowsML` pro komplexní příklady Windows ML  
4. Projděte si [požadavky na sestavení](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) pro cílové platformy  

**Prozkoumání AI Dev Gallery**  
- Prozkoumejte ukázkové aplikace a referenční implementace  
- Testujte API Windows AI s interaktivními demonstracemi  
- Projděte si zdrojový kód pro osvědčené postupy a vzory  
- Identifikujte relevantní vzorky pro váš konkrétní případ použití  

### Fáze 2: Výběr modelu a integrace  

**Analýza požadavků**  
- Definujte funkční požadavky na AI schopnosti  
- Stanovte výkonové limity a cíle optimalizace  
- Vyhodnoťte požadavky na soukromí a bezpečnost  
- Naplánujte architekturu nasazení a strategie škálování  

**Hodnocení modelu**  
- Použijte Foundry Local k testování open-source modelů pro váš případ použití  
- Proveďte benchmark API Windows AI vůči požadavkům na vlastní modely  
- Vyhodnoťte kompromisy mezi velikostí modelu, přesností a rychlostí inferencí  
- Prototypujte přístupy integrace s vybranými modely  

### Fáze 3: Vývoj aplikace  

**Základní integrace**  
- Implementujte integraci API Windows AI s řádným zpracováním chyb  
- Navrhněte uživatelská rozhraní, která zohledňují pracovní postupy AI  
- Implementujte strategie ukládání do mezipaměti a optimalizace pro inferenci modelů  
- Přidejte telemetrii a monitorování výkonu operací AI  

**Testování a validace**  
- Testujte aplikace na různých konfiguracích hardwaru Windows  
- Validujte výkonové metriky za různých podmínek zatížení  
- Implementujte automatizované testování pro spolehlivost funkcí AI  
- Proveďte testování uživatelského zážitku s funkcemi vylepšenými AI  

### Fáze 4: Optimalizace a nasazení  

**Optimalizace výkonu**  
- Profilujte výkon aplikace na cílových konfiguracích hardwaru  
- Optimalizujte využití paměti a strategie načítání modelů  
- Implementujte adaptivní chování na základě dostupných hardwarových schopností  
- Doladěte uživatelský zážitek pro různé scénáře výkonu  

**Nasazení do produkce**  
- Zabalte aplikace s řádnými závislostmi na modelech AI  
- Implementujte mechanismy aktualizace modelů a logiky aplikace  
- Nakonfigurujte monitorování a analytiku pro produkční prostředí  
- Naplánujte strategie nasazení pro podnikové i spotřebitelské aplikace  

## Praktické příklady implementace  

### Příklad 1: Aplikace pro inteligentní zpracování dokumentů  

Vytvořte aplikaci Windows, která zpracovává dokumenty pomocí více AI schopností:  

**Použité technologie:**  
- Phi Silica pro sumarizaci dokumentů a odpovídání na otázky  
- OCR API pro extrakci textu ze skenovaných dokumentů  
- API pro popis obrázků pro analýzu grafů a diagramů  
- Vlastní ONNX modely pro klasifikaci dokumentů  

**Přístup k implementaci:**  
- Navrhněte modulární architekturu s připojitelnými AI komponentami  
- Implementujte asynchronní zpracování pro velké dávky dokumentů  
- Přidejte indikátory průběhu a podporu zrušení pro dlouhotrvající operace  
- Zahrňte offline schopnosti pro zpracování citlivých dokumentů  

### Příklad 2: Systém správy maloobchodních zásob  

Vytvořte AI-poháněný systém správy zásob pro maloobchodní aplikace:  

**Použité technologie:**  
- Segmentace obrazu pro identifikaci produktů  
- Vlastní modely vidění pro klasifikaci značek a kategorií  
- Nasazení specializovaných jazykových modelů pro maloobchod pomocí Foundry Local  
- Integrace s existujícími POS a systémy správy zásob  

**Přístup k implementaci:**  
- Vytvořte integraci kamer pro skenování produktů v reálném čase  
- Implementujte rozpoznávání čárových kódů a vizuálních produktů  
- Přidejte dotazy na zásoby v přirozeném jazyce pomocí lokálních jazykových modelů  
- Navrhněte škálovatelnou architekturu pro nasazení v několika obchodech  

### Příklad 3: Asistent pro dokumentaci ve zdravotnictví  

Vyviněte nástroj pro dokumentaci ve zdravotnictví s ochranou soukromí:  

**Použité technologie:**  
- Phi Silica pro generování lékařských poznámek a podporu klinického rozhodování  
- OCR pro digitalizaci ručně psaných lékařských záznamů  
- Vlastní lékařské jazykové modely nasazené prostřednictvím Windows ML  
- Lokální vektorové úložiště pro vyhledávání lékařských znalostí  

**Přístup k implementaci:**  
- Zajistěte kompletní offline provoz pro ochranu soukromí pacientů  
- Implementujte validaci a návrhy lékařské terminologie  
- Přidejte auditní logování pro regulační shodu  
- Navrhněte integraci s existujícími systémy elektronických zdravotních záznamů  

## Strategie optimalizace výkonu  

### Vývoj s ohledem na hardware  

**Optimalizace pro NPU**  
- Navrhněte aplikace tak, aby využívaly schopnosti NPU na Copilot+ PC  
- Implementujte plynulý přechod na GPU/CPU na zařízeních bez NPU  
- Optimalizujte formáty modelů pro akceleraci specifickou pro NPU  
- Monitorujte využití NPU a tepelné charakteristiky  

**Správa paměti**  
- Implementujte efektivní strategie načítání a ukládání modelů do mezipaměti  
- Používejte mapování paměti pro velké modely ke snížení doby spuštění  
- Navrhněte aplikace šetrné k paměti pro zařízení s omezenými zdroji  
- Implementujte kvantizaci modelů pro optimalizaci paměti  

**Efektivita baterie**  
- Optimalizujte AI operace pro minimální spotřebu energie  
- Implementujte adaptivní zpracování na základě stavu baterie  
- Navrhněte efektivní zpracování na pozadí pro kontinuální AI operace  
- Používejte nástroje pro profilování energie k optimalizaci spotřeby  

### Úvahy o škálovatelnosti  

**Vícevláknové zpracování**  
- Navrhněte operace AI bezpečné pro vlákna pro současné zpracování  
- Implementujte efektivní rozdělení práce mezi dostupná jádra  
- Používejte vzory async/await pro neblokující operace AI  
- Naplánujte optimalizaci vláken pro různé konfigurace hardwaru  

**Strategie ukládání do mezipaměti**  
- Implementujte inteligentní ukládání do mezipaměti pro často používané operace AI  
- Navrhněte strategie invalidace mezipaměti pro aktualizace modelů  
- Používejte trvalé ukládání do mezipaměti pro nákladné operace předzpracování  
- Implementujte distribuované ukládání do mezipaměti pro scénáře s více uživateli  

## Nejlepší postupy pro bezpečnost a ochranu soukromí  

### Ochrana dat  

**Lokální zpracování**  
- Zajistěte, aby citlivá data nikdy neopustila místní zařízení  
- Implementujte bezpečné úložiště pro modely AI a dočasná data  
- Používejte bezpečnostní funkce Windows pro sandboxing aplikací  
- Aplikujte šifrování na uložené modely a výsledky mezizpracování  

**Bezpečnost modelů**  
- Validujte integritu modelů před jejich načtením a spuštěním  
- Implementujte bezpečné mechanismy aktualizace modelů  
- Používejte podepsané modely k prevenci manipulace  
- Aplikujte kontrolu přístupu na soubory modelů a konfigurace  

### Úvahy o shodě  

**Regulační soulad**  
- Navrhněte aplikace tak, aby splňovaly požadavky GDPR, HIPAA a dalších předpisů  
- Implementujte auditní logování pro procesy rozhodování AI  
- Poskytněte funkce transparentnosti pro výsledky generované AI  
- Umožněte uživatelům kontrolu nad zpracováním dat AI  

**Podniková bezpečnost**  
- Integrujte s bezpečnostními politikami Windows pro podniky  
- Podporujte spravované nasazení prostřednictvím nástrojů pro správu podniků  
- Implementujte řízení přístupu na základě rolí pro funkce AI  
- Poskytněte administrativní kontrolu nad funkcemi AI  

## Řešení problémů a ladění  

### Běžné vývojové problémy  

**Problémy s konfigurací sestavení**  
- Zajistěte konfiguraci platformy ARM64 pro vzorky API Windows AI  
- Ověřte kompatibilitu verze Windows App SDK (vyžadována verze 1.8.1+)  
- Zkontrolujte, zda je správně nakonfigurována identita balíčku (vyžadováno pro API Windows AI)  
- Validujte, že nástroje pro sestavení podporují cílovou verzi frameworku  

**Problémy s načítáním modelů**  
- Validujte kompatibilitu modelů ONNX s Windows ML  
- Zkontrolujte integritu souborů modelů a požadavky na formát  
- Ověřte požadavky na schopnosti hardwaru pro konkrétní modely  
- Laděte problémy s alokací paměti během načítání modelů  
- Zajistěte registraci poskytovatele exekuce pro akceleraci hardwaru  

**Úvahy o režimu nasazení**  
- **Režim Self-Contained**: Plně podporován s větší velikostí nasazení  
- **Režim Framework-Dependent**: Menší velikost, ale vyžaduje sdílený runtime  
- **Nepaketované aplikace**: Již nejsou podporovány pro API Windows AI  
- Použijte `dotnet run -p:Platform=ARM64 -p:SelfContained=true` pro samostatné nasazení ARM64  

**Problémy s výkonem**  
- Profilujte výkon aplikace na různých konfiguracích hardwaru  
- Identifikujte úzká místa v pipeline zpracování AI  
- Optimalizujte operace předzpracování a postzpracování dat  
- Implementujte monitorování výkonu a upozornění  

**Problémy s integrací**  
- Laděte problémy s integrací API s řádným zpracováním chyb  
- Validujte formáty vstupních dat a požadavky na předzpracování  
- Důkladně testujte hraniční případy a podmínky chyb  
- Implementujte komplexní logování pro ladění problémů v produkci  

### Nástroje a techniky ladění  

**Integrace Visual Studio**  
- Používejte debugger AI Toolkit pro analýzu exekuce modelů  
- Implementujte profilování výkonu pro operace AI  
- Laděte asynchronní operace AI s řádným zpracováním výjimek  
- Používejte nástroje pro profilování paměti k optimalizaci  

**Nástroje Windows AI Foundry**  
- Využijte CLI Foundry Local pro testování a validaci modelů  
- Používejte nástroje pro testování API Windows AI k ověření integrace  
- Implementujte vlastní logování pro monitorování operací AI  
- Vytvořte automatizované testování pro spolehlivost funkcí AI  

## Budoucí zajištění vašich aplikací  

### Nové technologie  

**Hardware nové generace**  
- Navrhněte aplikace tak, aby využívaly budoucí schopnosti NPU  
- Plánujte pro zvýšené velikosti modelů a složitost  
- Implementujte adaptivní architektury pro vyvíjející se hardware  
- Zvažte algoritmy připravené na kvantové technologie pro budoucí kompatibilitu  

**Pokročilé schopnosti AI**  
- Připravte se na multimodální integraci AI napříč více typy dat  
- Plánujte pro real-time spolupráci AI mezi více zařízeními  
- Navrhněte pro schopnosti federovaného učení  
- Zvažte hybridní architektury edge-cloud inteligence  

### Kontinuální učení a adaptace  

**Aktualizace modelů**  
- Implementujte bezproblémové mechanismy aktualizace modelů
- [Windows App SDK Samples Repository](https://github.com/microsoft/WindowsAppSDK-Samples)

### Vývojářské nástroje
- [AI Toolkit pro Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Ukázky](https://learn.microsoft.com/windows/ai/samples/)
- [Nástroje pro konverzi modelů](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Technická podpora
- [Dokumentace Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Dokumentace ONNX Runtime](https://onnxruntime.ai/docs/)
- [Dokumentace Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Nahlásit problémy - Windows App SDK Samples](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Komunita a podpora
- [Komunita vývojářů Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI školení](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Tento průvodce je navržen tak, aby se vyvíjel spolu s rychle se rozvíjejícím ekosystémem Windows AI. Pravidelné aktualizace zajišťují sladění s nejnovějšími schopnostmi platformy a osvědčenými postupy vývoje.*

[08. Praktické zkušenosti s Microsoft Foundry Local - Kompletní sada nástrojů pro vývojáře](../Module08/README.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.