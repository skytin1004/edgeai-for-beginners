<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9c2dacb560380677a2c923171d3e423d",
  "translation_date": "2025-09-22T23:40:19+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "sk"
}
-->
# Windows Edge AI Vývojová Príručka

## Úvod

Vitajte vo svete Windows Edge AI Development - komplexnej príručke na vytváranie inteligentných aplikácií, ktoré využívajú silu AI priamo na zariadení pomocou platformy Windows AI Foundry od Microsoftu. Táto príručka je určená pre vývojárov na Windows, ktorí chcú integrovať najmodernejšie schopnosti Edge AI do svojich aplikácií a zároveň využiť plný potenciál hardvérovej akcelerácie Windows.

### Výhody Windows AI

Windows AI Foundry predstavuje jednotnú, spoľahlivú a bezpečnú platformu, ktorá podporuje celý životný cyklus vývoja AI - od výberu a doladenia modelov až po optimalizáciu a nasadenie na CPU, GPU, NPU a hybridné cloudové architektúry. Táto platforma demokratizuje vývoj AI poskytovaním:

- **Hardvérová abstrakcia**: Bezproblémové nasadenie na AMD, Intel, NVIDIA a Qualcomm čipoch
- **Inteligencia na zariadení**: AI, ktorá zachováva súkromie a beží výhradne na lokálnom hardvéri
- **Optimalizovaný výkon**: Modely predoptimalizované pre konfigurácie hardvéru Windows
- **Pripravené pre podniky**: Bezpečnostné a súladové funkcie na úrovni produkcie

### Prečo Windows pre Edge AI?

**Univerzálna podpora hardvéru**  
Windows ML poskytuje automatickú optimalizáciu hardvéru naprieč celým ekosystémom Windows, čím zabezpečuje, že vaše AI aplikácie budú fungovať optimálne bez ohľadu na architektúru čipu.

**Integrovaný AI Runtime**  
Vstavaný inference engine Windows ML eliminuje zložité požiadavky na nastavenie, čo umožňuje vývojárom sústrediť sa na logiku aplikácie namiesto infraštruktúry.

**Optimalizácia Copilot+ PC**  
API navrhnuté špeciálne pre zariadenia novej generácie Windows s dedikovanými neurónovými procesorovými jednotkami (NPU), ktoré poskytujú výnimočný výkon na watt.

**Ekosystém pre vývojárov**  
Bohaté nástroje vrátane integrácie Visual Studio, komplexnej dokumentácie a ukážkových aplikácií, ktoré urýchľujú vývojové cykly.

## Ciele učenia

Po dokončení tejto príručky pre vývoj Windows Edge AI získate základné zručnosti na vytváranie produkčne pripravených AI aplikácií na platforme Windows.

### Základné technické kompetencie

**Ovládanie Windows AI Foundry**  
- Pochopenie architektúry a komponentov platformy Windows AI Foundry  
- Navigácia v celom životnom cykle vývoja AI v ekosystéme Windows  
- Implementácia bezpečnostných najlepších praktík pre AI aplikácie na zariadení  
- Optimalizácia aplikácií pre rôzne konfigurácie hardvéru Windows  

**Expertíza v integrácii API**  
- Ovládanie Windows AI API pre textové, vizuálne a multimodálne aplikácie  
- Implementácia integrácie jazykového modelu Phi Silica pre generovanie textu a uvažovanie  
- Nasadenie schopností počítačového videnia pomocou vstavaných API na spracovanie obrazu  
- Prispôsobenie predtrénovaných modelov pomocou techník LoRA (Low-Rank Adaptation)  

**Implementácia Foundry Local**  
- Prehliadanie, hodnotenie a nasadenie open-source jazykových modelov pomocou Foundry Local CLI  
- Pochopenie optimalizácie modelov a kvantizácie pre lokálne nasadenie  
- Implementácia offline AI schopností, ktoré fungujú bez internetového pripojenia  
- Správa životného cyklu modelov a aktualizácií v produkčnom prostredí  

**Nasadenie Windows ML**  
- Integrácia vlastných ONNX modelov do aplikácií Windows pomocou Windows ML  
- Využitie automatickej hardvérovej akcelerácie na CPU, GPU a NPU architektúrach  
- Implementácia inferencie v reálnom čase s optimálnym využitím zdrojov  
- Návrh škálovateľných AI aplikácií pre rôzne kategórie zariadení Windows  

### Zručnosti vývoja aplikácií

**Vývoj naprieč platformami Windows**  
- Vytváranie AI aplikácií pomocou .NET MAUI pre univerzálne nasadenie na Windows  
- Integrácia AI schopností do Win32, UWP a progresívnych webových aplikácií  
- Implementácia responzívnych UI dizajnov, ktoré sa prispôsobujú stavom spracovania AI  
- Riešenie asynchrónnych AI operácií s vhodnými vzormi používateľskej skúsenosti  

**Optimalizácia výkonu**  
- Profilovanie a optimalizácia výkonu inferencie AI na rôznych konfiguráciách hardvéru  
- Implementácia efektívneho spravovania pamäte pre veľké jazykové modely  
- Návrh aplikácií, ktoré sa elegantne degradujú na základe dostupných hardvérových schopností  
- Aplikácia stratégií ukladania do vyrovnávacej pamäte pre často používané AI operácie  

**Pripravenosť na produkciu**  
- Implementácia komplexného spracovania chýb a záložných mechanizmov  
- Návrh telemetrie a monitorovania výkonu AI aplikácií  
- Aplikácia bezpečnostných najlepších praktík pre lokálne ukladanie a vykonávanie AI modelov  
- Plánovanie stratégií nasadenia pre podnikové a spotrebiteľské aplikácie  

### Obchodné a strategické porozumenie

**Architektúra AI aplikácií**  
- Návrh hybridných architektúr, ktoré optimalizujú medzi lokálnym a cloudovým spracovaním AI  
- Hodnotenie kompromisov medzi veľkosťou modelu, presnosťou a rýchlosťou inferencie  
- Plánovanie architektúr toku dát, ktoré zachovávajú súkromie a zároveň umožňujú inteligenciu  
- Implementácia nákladovo efektívnych AI riešení, ktoré sa škálujú podľa požiadaviek používateľov  

**Pozicionovanie na trhu**  
- Pochopenie konkurenčných výhod Windows-native AI aplikácií  
- Identifikácia prípadov použitia, kde AI na zariadení poskytuje lepšie používateľské skúsenosti  
- Vývoj stratégií uvedenia na trh pre AI vylepšené aplikácie na Windows  
- Pozicionovanie aplikácií na využitie výhod ekosystému Windows  

## Komponenty platformy Windows AI Foundry

### 1. Windows AI API

Windows AI API poskytujú pripravené AI schopnosti poháňané modelmi na zariadení, optimalizované pre efektivitu a výkon na zariadeniach Copilot+ PC s minimálnymi požiadavkami na nastavenie.

#### Hlavné kategórie API

**Jazykový model Phi Silica**  
- Malý, ale výkonný jazykový model pre generovanie textu a uvažovanie  
- Optimalizovaný pre inferenciu v reálnom čase s minimálnou spotrebou energie  
- Podpora vlastného doladenia pomocou techník LoRA  
- Integrácia s Windows semantickým vyhľadávaním a získavaním znalostí  

**API počítačového videnia**  
- **Rozpoznávanie textu (OCR)**: Extrakcia textu z obrázkov s vysokou presnosťou  
- **Super rozlíšenie obrazu**: Zvýšenie kvality obrázkov pomocou lokálnych AI modelov  
- **Segmentácia obrazu**: Identifikácia a izolácia konkrétnych objektov na obrázkoch  
- **Popis obrázkov**: Generovanie podrobných textových popisov vizuálneho obsahu  
- **Odstránenie objektov**: Odstránenie nežiaducich objektov z obrázkov pomocou AI  

**Multimodálne schopnosti**  
- **Integrácia videnia a jazyka**: Kombinácia porozumenia textu a obrazu  
- **Semantické vyhľadávanie**: Umožnenie prirodzených jazykových dotazov naprieč multimediálnym obsahom  
- **Získavanie znalostí**: Vytváranie inteligentných vyhľadávacích skúseností s lokálnymi dátami  

### 2. Foundry Local

Foundry Local poskytuje vývojárom rýchly prístup k pripraveným open-source jazykovým modelom na Windows Silicon, ponúkajúc možnosť prehliadať, testovať, interagovať a nasadzovať modely v lokálnych aplikáciách.

#### Kľúčové funkcie

**Katalóg modelov**  
- Komplexná zbierka predoptimalizovaných open-source modelov  
- Modely optimalizované na CPU, GPU a NPU pre okamžité nasadenie  
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

Windows ML slúži ako hlavná AI platforma a integrovaný runtime inferencie na Windows, umožňujúc vývojárom efektívne nasadzovať vlastné modely naprieč širokým ekosystémom hardvéru Windows.

#### Výhody architektúry

**Univerzálna podpora hardvéru**  
- Automatická optimalizácia pre AMD, Intel, NVIDIA a Qualcomm čipy  
- Podpora CPU, GPU a NPU vykonávania s transparentným prepínaním  
- Hardvérová abstrakcia, ktorá eliminuje prácu na optimalizácii špecifickej pre platformu  

**Flexibilita modelov**  
- Podpora formátu ONNX modelov s automatickou konverziou z populárnych frameworkov  
- Nasadenie vlastných modelov s výkonom na úrovni produkcie  
- Integrácia s existujúcimi architektúrami aplikácií Windows  

**Integrácia pre podniky**  
- Kompatibilita s bezpečnostnými a súladovými rámcami Windows  
- Podpora podnikových nástrojov na nasadenie a správu  
- Integrácia s monitorovacími systémami a správou zariadení Windows  

## Pracovný postup vývoja

### Fáza 1: Nastavenie prostredia a konfigurácia nástrojov

**Príprava vývojového prostredia**  
1. Nainštalujte Visual Studio s rozšírením AI Toolkit  
2. Konfigurujte nástroje Windows AI Foundry CLI  
3. Nastavte lokálne testovacie prostredie modelov  
4. Zabezpečte nástroje na profilovanie výkonu a monitorovanie  

**Preskúmanie AI Dev Gallery**  
- Preskúmajte ukážkové aplikácie a referenčné implementácie  
- Testujte Windows AI API pomocou interaktívnych ukážok  
- Preštudujte zdrojový kód pre najlepšie praktiky a vzory  
- Identifikujte relevantné ukážky pre váš konkrétny prípad použitia  

### Fáza 2: Výber a integrácia modelov

**Analýza požiadaviek**  
- Definujte funkčné požiadavky na schopnosti AI  
- Stanovte výkonové obmedzenia a ciele optimalizácie  
- Vyhodnoťte požiadavky na súkromie a bezpečnosť  
- Plánujte architektúru nasadenia a stratégie škálovania  

**Hodnotenie modelov**  
- Použite Foundry Local na testovanie open-source modelov pre váš prípad použitia  
- Porovnajte Windows AI API s požiadavkami na vlastné modely  
- Vyhodnoťte kompromisy medzi veľkosťou modelu, presnosťou a rýchlosťou inferencie  
- Prototypujte prístupy integrácie s vybranými modelmi  

### Fáza 3: Vývoj aplikácií

**Základná integrácia**  
- Implementujte integráciu Windows AI API s vhodným spracovaním chýb  
- Navrhnite používateľské rozhrania, ktoré zohľadňujú pracovné postupy spracovania AI  
- Implementujte stratégie ukladania do vyrovnávacej pamäte a optimalizácie pre inferenciu modelov  
- Pridajte telemetriu a monitorovanie výkonu AI operácií  

**Testovanie a validácia**  
- Testujte aplikácie na rôznych konfiguráciách hardvéru Windows  
- Validujte výkonové metriky pri rôznych podmienkach zaťaženia  
- Implementujte automatizované testovanie spoľahlivosti funkcií AI  
- Vykonajte testovanie používateľskej skúsenosti s funkciami vylepšenými AI  

### Fáza 4: Optimalizácia a nasadenie

**Optimalizácia výkonu**  
- Profilujte výkon aplikácie na cieľových konfiguráciách hardvéru  
- Optimalizujte využitie pamäte a stratégie načítania modelov  
- Implementujte adaptívne správanie na základe dostupných schopností hardvéru  
- Doladte používateľskú skúsenosť pre rôzne scenáre výkonu  

**Nasadenie do produkcie**  
- Zabalte aplikácie s vhodnými závislosťami AI modelov  
- Implementujte mechanizmy aktualizácie modelov a logiky aplikácií  
- Konfigurujte monitorovanie a analytiku pre produkčné prostredia  
- Plánujte stratégie nasadenia pre podnikové a spotrebiteľské aplikácie  

## Praktické príklady implementácie

### Príklad 1: Inteligentná aplikácia na spracovanie dokumentov

Vytvorte aplikáciu Windows, ktorá spracováva dokumenty pomocou viacerých AI schopností:

**Použité technológie:**  
- Phi Silica na sumarizáciu dokumentov a odpovedanie na otázky  
- OCR API na extrakciu textu zo skenovaných dokumentov  
- API na popis obrázkov na analýzu grafov a diagramov  
- Vlastné ONNX modely na klasifikáciu dokumentov  

**Prístup k implementácii:**  
- Navrhnite modulárnu architektúru s pripojiteľnými AI komponentmi  
- Implementujte asynchrónne spracovanie pre veľké dávky dokumentov  
- Pridajte indikátory pokroku a podporu zrušenia pre dlhodobé operácie  
- Zahrňte offline schopnosti pre spracovanie citlivých dokumentov  

### Príklad 2: Systém správy inventára pre maloobchod

Vytvorte AI-poháňaný systém inventára pre maloobchodné aplikácie:

**Použité technológie:**  
- Segmentácia obrazu na identifikáciu produktov  
- Vlastné modely videnia na klasifikáciu značiek a kategórií  
- Nasadenie špecializovaných jazykových modelov pre maloobchod pomocou Foundry Local  
- Integrácia s existujúcimi POS a inventárnymi systémami  

**Prístup k implementácii:**  
- Vytvorte integráciu kamery na skenovanie produktov v reálnom čase  
- Implementujte rozpoznávanie čiarových kódov a vizuálnych produktov  
- Pridajte prirodzené jazykové dotazy inventára pomocou lokálnych jazykových modelov  
- Navrhnite škálovateľnú architektúru pre nasadenie vo viacerých obchodoch  

### Príklad 3: Asistent dokumentácie v zdravotníctve

Vyvinúť nástroj na dokumentáciu v zdravotníctve, ktorý zachováva súkromie:

**Použité technológie:**  
- Phi Silica na generovanie lekárskych poznámok a podporu klinického rozhodovania  
- OCR na digitalizáciu ručne písaných lekárskych záznamov  
- Vlastné lekárske jazykové modely nasadené cez Windows ML  
- Lokálne vektorové úložisko na získavanie lekárskych znalostí  

**Prístup k implementácii:**  
- Zabezpečte úplnú offline prevádzku pre ochranu súkromia pacientov  
- Implementujte validáciu a návrhy lekárskej terminológie  
- Pridajte auditné logovanie pre regulačnú súlad  
- Navrhnite integráciu s existujúcimi systémami elektronických zdravotných záznamov  

## Stratégie optimalizácie výkonu

### Vývoj orientovaný na hardvér

**Optimalizácia NPU**  
- Navrhnite aplikácie na využitie schopností NPU na Copilot+ PC  
- Implementujte elegantné záložné riešenia na GPU/CPU na zariadeniach bez NPU  
- Optimalizujte formáty modelov pre akceleráciu špecifickú pre NPU  
- Monitorujte využitie NPU a tepelné charakteristiky  

**Správa pamäte**  
- Implementujte efektívne stratégie načítania a ukladania
- Využite Foundry Local CLI na testovanie a validáciu modelov
- Použite nástroje Windows AI API na overenie integrácie
- Implementujte vlastné logovanie na monitorovanie operácií AI
- Vytvorte automatizované testovanie pre spoľahlivosť funkčnosti AI

## Príprava vašich aplikácií na budúcnosť

### Nové technológie

**Hardvér novej generácie**
- Navrhujte aplikácie tak, aby využívali budúce schopnosti NPU
- Plánujte pre väčšie modely a vyššiu komplexnosť
- Implementujte adaptívne architektúry pre vyvíjajúci sa hardvér
- Zvážte algoritmy pripravené na kvantové výpočty pre budúcu kompatibilitu

**Pokročilé schopnosti AI**
- Pripravte sa na integráciu multimodálnej AI naprieč rôznymi typmi dát
- Plánujte pre real-time spoluprácu AI medzi viacerými zariadeniami
- Navrhujte pre schopnosti federatívneho učenia
- Zvážte hybridné architektúry inteligencie medzi edge a cloudom

### Neustále učenie a adaptácia

**Aktualizácie modelov**
- Implementujte bezproblémové mechanizmy aktualizácie modelov
- Navrhujte aplikácie tak, aby sa prispôsobili zlepšeným schopnostiam modelov
- Plánujte spätnú kompatibilitu s existujúcimi modelmi
- Implementujte A/B testovanie na hodnotenie výkonu modelov

**Evolúcia funkcií**
- Navrhujte modulárne architektúry, ktoré umožňujú integráciu nových schopností AI
- Plánujte integráciu nových Windows AI API
- Implementujte funkčné vlajky pre postupné zavádzanie schopností
- Navrhujte používateľské rozhrania, ktoré sa prispôsobujú vylepšeným funkciám AI

## Záver

Vývoj Windows Edge AI predstavuje spojenie výkonných schopností AI s robustnou, bezpečnou a škálovateľnou platformou Windows. Ovládnutím ekosystému Windows AI Foundry môžu vývojári vytvárať inteligentné aplikácie, ktoré poskytujú výnimočné používateľské zážitky pri zachovaní najvyšších štandardov ochrany súkromia, bezpečnosti a výkonu.

Kombinácia Windows AI API, Foundry Local a Windows ML poskytuje bezkonkurenčný základ pre budovanie novej generácie inteligentných aplikácií pre Windows. Ako sa AI neustále vyvíja, platforma Windows zabezpečuje, že vaše aplikácie budú rásť s novými technológiami, pričom si zachovajú kompatibilitu a výkon naprieč rôznorodým hardvérovým ekosystémom Windows.

Či už vytvárate spotrebiteľské aplikácie, podnikové riešenia alebo špecializované nástroje pre priemysel, vývoj Windows Edge AI vám umožňuje vytvárať inteligentné, responzívne a hlboko integrované zážitky, ktoré využívajú plný potenciál moderných zariadení Windows.

## Ďalšie zdroje

Pre podrobný Windows návod na Foundry Local (inštalácia, CLI, dynamický endpoint, používanie SDK) si pozrite sprievodcu repo: [foundrylocal.md](./foundrylocal.md).

### Dokumentácia a vzdelávanie
- [Windows AI Foundry Dokumentácia](https://learn.microsoft.com/windows/ai/)
- [Windows AI API Referencia](https://learn.microsoft.com/windows/ai/apis/)
- [Foundry Local Začíname](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML Prehľad](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)

### Vývojárske nástroje
- [AI Toolkit pre Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Galéria](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Ukážky](https://learn.microsoft.com/windows/ai/samples/)

### Komunita a podpora
- [Windows Vývojárska komunita](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Tréning](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Tento sprievodca je navrhnutý tak, aby sa vyvíjal spolu s rýchlo napredujúcim ekosystémom Windows AI. Pravidelné aktualizácie zabezpečujú súlad s najnovšími schopnosťami platformy a najlepšími postupmi vývoja.*

---

