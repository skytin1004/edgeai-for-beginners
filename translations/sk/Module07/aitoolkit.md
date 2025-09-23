<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-18T19:15:09+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "sk"
}
-->
# AI Toolkit pre Visual Studio Code - Príručka pre vývoj Edge AI

## Úvod

Vitajte v komplexnej príručke na používanie AI Toolkit pre Visual Studio Code vo vývoji Edge AI. Ako sa umelá inteligencia presúva z centralizovaného cloudového výpočtu na distribuované edge zariadenia, vývojári potrebujú výkonné, integrované nástroje, ktoré zvládnu jedinečné výzvy nasadenia na edge - od obmedzených zdrojov až po požiadavky na offline prevádzku.

AI Toolkit pre Visual Studio Code prekonáva túto medzeru tým, že poskytuje kompletné vývojové prostredie špeciálne navrhnuté na vytváranie, testovanie a optimalizáciu AI aplikácií, ktoré efektívne fungujú na edge zariadeniach. Či už vyvíjate pre IoT senzory, mobilné zariadenia, zabudované systémy alebo edge servery, tento nástroj zjednodušuje celý váš vývojový proces v známom prostredí VS Code.

Táto príručka vás prevedie základnými konceptmi, nástrojmi a osvedčenými postupmi na využitie AI Toolkit vo vašich Edge AI projektoch, od výberu modelu až po nasadenie do produkcie.

## Prehľad

AI Toolkit poskytuje integrované vývojové prostredie pre celý životný cyklus Edge AI aplikácií v rámci VS Code. Ponúka bezproblémovú integráciu s populárnymi AI modelmi od poskytovateľov ako OpenAI, Anthropic, Google a GitHub, pričom podporuje lokálne nasadenie modelov prostredníctvom ONNX a Ollama - kľúčové funkcie pre Edge AI aplikácie, ktoré vyžadujú inferenciu priamo na zariadení.

Čo odlišuje AI Toolkit pre vývoj Edge AI, je jeho zameranie na celý pipeline nasadenia na edge. Na rozdiel od tradičných AI vývojových nástrojov, ktoré sa primárne zameriavajú na nasadenie v cloude, AI Toolkit obsahuje špecializované funkcie na optimalizáciu modelov, testovanie v podmienkach s obmedzenými zdrojmi a hodnotenie výkonu špecifického pre edge. Nástroj chápe, že vývoj Edge AI vyžaduje odlišné úvahy - menšie veľkosti modelov, rýchlejšie časy inferencie, schopnosť offline prevádzky a optimalizácie špecifické pre hardvér.

Platforma podporuje rôzne scenáre nasadenia, od jednoduchej inferencie na zariadení až po komplexné multi-modelové edge architektúry. Poskytuje nástroje na konverziu modelov, kvantizáciu a optimalizáciu, ktoré sú nevyhnutné pre úspešné nasadenie na edge, pričom zachováva produktivitu vývojára, ktorou je VS Code známy.

## Ciele učenia

Na konci tejto príručky budete schopní:

### Základné kompetencie
- **Nainštalovať a nakonfigurovať** AI Toolkit pre Visual Studio Code pre vývojové workflowy Edge AI
- **Navigovať a používať** rozhranie AI Toolkit, vrátane Model Catalog, Playground a Agent Builder
- **Vybrať a hodnotiť** AI modely vhodné pre nasadenie na edge na základe výkonu a obmedzení zdrojov
- **Konvertovať a optimalizovať** modely pomocou formátu ONNX a techník kvantizácie pre edge zariadenia

### Zručnosti vo vývoji Edge AI
- **Navrhnúť a implementovať** Edge AI aplikácie pomocou integrovaného vývojového prostredia
- **Testovať modely** v podmienkach podobných edge pomocou lokálnej inferencie a monitorovania zdrojov
- **Vytvoriť a prispôsobiť** AI agentov optimalizovaných pre scenáre nasadenia na edge
- **Hodnotiť výkon modelov** pomocou metrík relevantných pre edge výpočty (latencia, využitie pamäte, presnosť)

### Optimalizácia a nasadenie
- **Použiť kvantizáciu a prerezávanie** na zmenšenie veľkosti modelu pri zachovaní prijateľného výkonu
- **Optimalizovať modely** pre konkrétne hardvérové platformy na edge vrátane CPU, GPU a NPU akcelerácie
- **Implementovať osvedčené postupy** pre vývoj Edge AI vrátane správy zdrojov a záložných stratégií
- **Pripraviť modely a aplikácie** na nasadenie do produkcie na edge zariadeniach

### Pokročilé koncepty Edge AI
- **Integrovať s frameworkmi Edge AI** vrátane ONNX Runtime, Windows ML a TensorFlow Lite
- **Implementovať multi-modelové architektúry** a scenáre federovaného učenia pre edge prostredia
- **Riešiť bežné problémy Edge AI** vrátane obmedzení pamäte, rýchlosti inferencie a kompatibility hardvéru
- **Navrhnúť stratégie monitorovania a logovania** pre Edge AI aplikácie v produkcii

### Praktická aplikácia
- **Vytvoriť kompletné Edge AI riešenia** od výberu modelu až po nasadenie
- **Preukázať zručnosti** v edge-špecifických vývojových workflowoch a optimalizačných technikách
- **Aplikovať naučené koncepty** na reálne prípady použitia Edge AI vrátane IoT, mobilných a zabudovaných aplikácií
- **Hodnotiť a porovnávať** rôzne stratégie nasadenia Edge AI a ich kompromisy

## Kľúčové funkcie pre vývoj Edge AI

### 1. Katalóg modelov a objavovanie
- **Podpora lokálnych modelov**: Objavujte a pristupujte k AI modelom špeciálne optimalizovaným pre nasadenie na edge
- **Integrácia ONNX**: Prístup k modelom vo formáte ONNX pre efektívnu inferenciu na edge
- **Podpora Ollama**: Využívajte modely bežiace lokálne prostredníctvom Ollama pre ochranu súkromia a offline prevádzku
- **Porovnanie modelov**: Porovnávajte modely vedľa seba, aby ste našli optimálnu rovnováhu medzi výkonom a spotrebou zdrojov pre edge zariadenia

### 2. Interaktívne ihrisko (Playground)
- **Lokálne testovacie prostredie**: Testujte modely lokálne pred nasadením na edge
- **Multi-modálne experimentovanie**: Testujte s obrázkami, textom a ďalšími vstupmi typickými pre edge scenáre
- **Ladenie parametrov**: Experimentujte s rôznymi parametrami modelu na optimalizáciu pre obmedzenia edge
- **Monitorovanie výkonu v reálnom čase**: Sledujte rýchlosť inferencie a využitie zdrojov počas vývoja

### 3. Tvorca agentov pre Edge aplikácie
- **Inžinierstvo promptov**: Vytvárajte optimalizované prompty, ktoré efektívne fungujú s menšími edge modelmi
- **Integrácia MCP nástrojov**: Integrujte nástroje Model Context Protocol pre rozšírené schopnosti edge agentov
- **Generovanie kódu**: Generujte kód pripravený na produkciu optimalizovaný pre scenáre nasadenia na edge
- **Štruktúrované výstupy**: Navrhujte agentov, ktorí poskytujú konzistentné, štruktúrované odpovede vhodné pre edge aplikácie

### 4. Hodnotenie a testovanie modelov
- **Metriky výkonu**: Hodnoťte modely pomocou metrík relevantných pre nasadenie na edge (latencia, využitie pamäte, presnosť)
- **Batch testovanie**: Testujte viacero konfigurácií modelov súčasne, aby ste našli optimálne nastavenia pre edge
- **Vlastné hodnotenie**: Vytvárajte vlastné kritériá hodnotenia špecifické pre prípady použitia Edge AI
- **Profilovanie zdrojov**: Analyzujte požiadavky na pamäť a výpočtový výkon pre plánovanie nasadenia na edge

### 5. Konverzia a optimalizácia modelov
- **Konverzia na ONNX**: Konvertujte modely z rôznych formátov na ONNX pre kompatibilitu s edge
- **Kvantizácia**: Zmenšite veľkosť modelu a zlepšite rýchlosť inferencie pomocou techník kvantizácie
- **Optimalizácia hardvéru**: Optimalizujte modely pre konkrétny edge hardvér (CPU, GPU, NPU)
- **Transformácia formátov**: Transformujte modely z Hugging Face a iných zdrojov pre nasadenie na edge

### 6. Jemné doladenie pre scenáre Edge
- **Adaptácia na doménu**: Prispôsobte modely pre konkrétne prípady použitia a prostredia na edge
- **Lokálne trénovanie**: Trénujte modely lokálne s podporou GPU pre špecifické požiadavky na edge
- **Integrácia Azure**: Využívajte Azure Container Apps na jemné doladenie v cloude pred nasadením na edge
- **Transferové učenie**: Prispôsobte predtrénované modely pre úlohy a obmedzenia špecifické pre edge

### 7. Monitorovanie výkonu a sledovanie
- **Analýza výkonu na edge**: Monitorujte výkon modelu v podmienkach podobných edge
- **Zber sledovacích údajov**: Zbierajte podrobné údaje o výkone na optimalizáciu
- **Identifikácia úzkych miest**: Identifikujte problémy s výkonom pred nasadením na edge zariadenia
- **Sledovanie využitia zdrojov**: Monitorujte pamäť, CPU a čas inferencie pre optimalizáciu na edge

## Workflow vývoja Edge AI

### Fáza 1: Objavovanie a výber modelu
1. **Preskúmajte katalóg modelov**: Použite katalóg modelov na vyhľadanie modelov vhodných pre nasadenie na edge
2. **Porovnajte výkon**: Hodnoťte modely na základe veľkosti, presnosti a rýchlosti inferencie
3. **Testujte lokálne**: Použite modely Ollama alebo ONNX na lokálne testovanie pred nasadením na edge
4. **Posúďte požiadavky na zdroje**: Určte potreby pamäte a výpočtového výkonu pre cieľové edge zariadenia

### Fáza 2: Optimalizácia modelu
1. **Konvertujte na ONNX**: Konvertujte vybrané modely na formát ONNX pre kompatibilitu s edge
2. **Použite kvantizáciu**: Zmenšite veľkosť modelu pomocou kvantizácie INT8 alebo INT4
3. **Optimalizácia hardvéru**: Optimalizujte pre cieľový edge hardvér (ARM, x86, špecializované akcelerátory)
4. **Validácia výkonu**: Overte, že optimalizované modely si zachovávajú prijateľnú presnosť

### Fáza 3: Vývoj aplikácie
1. **Návrh agenta**: Použite Agent Builder na vytvorenie AI agentov optimalizovaných pre edge
2. **Inžinierstvo promptov**: Vyvíjajte prompty, ktoré efektívne fungujú s menšími edge modelmi
3. **Testovanie integrácie**: Testujte agentov v simulovaných podmienkach edge
4. **Generovanie kódu**: Generujte produkčný kód optimalizovaný pre nasadenie na edge

### Fáza 4: Hodnotenie a testovanie
1. **Batch hodnotenie**: Testujte viacero konfigurácií na nájdenie optimálnych nastavení pre edge
2. **Profilovanie výkonu**: Analyzujte rýchlosť inferencie, využitie pamäte a presnosť
3. **Simulácia edge**: Testujte v podmienkach podobných cieľovému prostrediu nasadenia na edge
4. **Záťažové testovanie**: Hodnoťte výkon pri rôznych podmienkach zaťaženia

### Fáza 5: Príprava na nasadenie
1. **Finálna optimalizácia**: Použite finálne optimalizácie na základe výsledkov testovania
2. **Balenie na nasadenie**: Zabaľte modely a kód na nasadenie na edge
3. **Dokumentácia**: Dokumentujte požiadavky na nasadenie a konfiguráciu
4. **Nastavenie monitorovania**: Pripravte monitorovanie a logovanie pre nasadenie do produkcie

## Cieľová skupina pre vývoj Edge AI

### Vývojári Edge AI
- Vývojári aplikácií, ktorí vytvárajú edge zariadenia a IoT riešenia poháňané AI
- Vývojári zabudovaných systémov, ktorí integrujú AI schopnosti do zariadení s obmedzenými zdrojmi
- Mobilní vývojári, ktorí vytvárajú AI aplikácie priamo na zariadeniach, ako sú smartfóny a tablety

### Inžinieri Edge AI
- AI inžinieri optimalizujúci modely pre nasadenie na edge a spravujúci inferenčné pipeline
- DevOps inžinieri nasadzujúci a spravujúci AI modely na distribuovanej edge infraštruktúre
- Inžinieri výkonu optimalizujúci AI pracovné zaťaženie pre obmedzenia edge hardvéru

### Výskumníci a pedagógovia
- AI výskumníci vyvíjajúci efektívne modely a algoritmy pre edge výpočty
- Pedagógovia vyučujúci koncepty Edge AI a demonštrujúci optimalizačné techniky
- Študenti, ktorí sa učia o výzvach a riešeniach pri nasadení Edge AI

## Prípady použitia Edge AI

### Inteligentné IoT zariadenia
- **Rozpoznávanie obrazu v reálnom čase**: Nasadenie modelov počítačového videnia na IoT kamerách a senzoroch
- **Spracovanie hlasu**: Implementácia rozpoznávania reči a spracovania prirodzeného jazyka na inteligentných reproduktoroch
- **Prediktívna údržba**: Spustenie modelov detekcie anomálií na priemyselných edge zariadeniach
- **Monitorovanie prostredia**: Nasadenie modelov analýzy senzorových dát pre environmentálne aplikácie

### Mobilné a zabudované aplikácie
- **Preklad na zariadení**: Implementácia modelov prekladu jazyka, ktoré fungujú offline
- **Rozšírená realita**: Nasadenie modelov rozpoznávania a sledovania objektov v reálnom čase pre AR aplikácie
- **Monitorovanie zdravia**: Spustenie modelov analýzy zdravia na nositeľných zariadeniach a zdravotníckom vybavení
- **Autonómne systémy**: Implementácia modelov rozhodovania pre drony, roboty a vozidlá

### Edge výpočtová infraštruktúra
- **Edge dátové centrá**: Nasadenie AI modelov v edge dátových centrách pre aplikácie s nízkou latenciou
- **Integrácia CDN**: Integrácia schopností AI spracovania do sietí na doručovanie obsahu
- **5G Edge**: Využitie edge výpočtov na 5G pre aplikácie poháňané AI
- **Fog Computing**: Implementácia AI spracovania v prostrediach fog computingu

## Inštalácia a nastavenie

### Rýchla inštalácia
Nainštalujte rozšírenie AI Toolkit priamo z Visual Studio Code Marketplace:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Predpoklady pre vývoj Edge AI
- **ONNX Runtime**: Nainštalujte ONNX Runtime pre inferenciu modelov
- **Ollama** (voliteľné): Nainštalujte Ollama pre lokálne poskytovanie modelov
- **Python prostredie**: Nastavte Python s požadovanými AI knižnicami
- **Nástroje pre edge hardvér**: Nainštalujte nástroje na vývoj špecifické pre hardvér (CUDA, OpenVINO, atď.)

### Počiatočná konfigurácia
1. Otvorte VS Code a nainštalujte rozšírenie AI Toolkit
2. Nakonfigurujte zdroje modelov (ONNX, Ollama, poskytovatelia cloudu)
3. Nastavte lokálne vývojové prostredie pre testovanie na edge
4. Nakonfigurujte možnosti hardvérovej akcelerácie pre váš vývojový stroj

## Začíname s vývojom Edge AI

### Krok 1: Výber modelu
1. Otvorte zobrazenie AI Toolkit v Activity Bar
2. Prehliadajte katalóg modelov pre modely kompatibilné s edge
3. Filtrujte podľa veľkosti modelu, formátu (ONNX) a charakteristík výkonu
4. Porovnávajte modely pomocou zabudovaných nást
- **Bezpečnosť**: Implementujte vhodné bezpečnostné opatrenia pre aplikácie Edge AI

## Integrácia s Edge AI rámcami

### ONNX Runtime
- **Nasadenie na rôznych platformách**: Nasadzujte ONNX modely na rôzne edge platformy
- **Optimalizácia hardvéru**: Využívajte hardvérové špecifické optimalizácie ONNX Runtime
- **Podpora mobilných zariadení**: Používajte ONNX Runtime Mobile pre aplikácie na smartfónoch a tabletoch
- **Integrácia s IoT**: Nasadzujte na IoT zariadenia pomocou ľahkých distribúcií ONNX Runtime

### Windows ML
- **Windows zariadenia**: Optimalizujte pre edge zariadenia a PC založené na Windows
- **Akcelerácia NPU**: Využívajte Neural Processing Units na Windows zariadeniach
- **DirectML**: Používajte DirectML na akceleráciu GPU na Windows platformách
- **Integrácia UWP**: Integrujte s aplikáciami Universal Windows Platform

### TensorFlow Lite
- **Optimalizácia pre mobilné zariadenia**: Nasadzujte TensorFlow Lite modely na mobilné a zabudované zariadenia
- **Hardvérové delegáty**: Používajte špecializované hardvérové delegáty na akceleráciu
- **Mikrokontroléry**: Nasadzujte na mikrokontroléry pomocou TensorFlow Lite Micro
- **Podpora viacerých platforiem**: Nasadzujte na Android, iOS a zabudované Linux systémy

### Azure IoT Edge
- **Hybrid cloud-edge**: Kombinujte tréning v cloude s inferenciou na edge zariadeniach
- **Nasadenie modulov**: Nasadzujte AI modely ako IoT Edge moduly
- **Správa zariadení**: Spravujte edge zariadenia a aktualizácie modelov na diaľku
- **Telemetria**: Zbierajte údaje o výkone a metriky modelov z edge nasadení

## Pokročilé scenáre Edge AI

### Nasadenie viacerých modelov
- **Modelové súbory**: Nasadzujte viacero modelov pre zlepšenie presnosti alebo redundanciu
- **A/B testovanie**: Testujte rôzne modely súčasne na edge zariadeniach
- **Dynamický výber**: Vyberajte modely na základe aktuálnych podmienok zariadenia
- **Zdieľanie zdrojov**: Optimalizujte využitie zdrojov medzi viacerými nasadenými modelmi

### Federované učenie
- **Distribuovaný tréning**: Trénujte modely na viacerých edge zariadeniach
- **Zachovanie súkromia**: Uchovávajte tréningové dáta lokálne a zdieľajte len vylepšenia modelov
- **Kolaboratívne učenie**: Umožnite zariadeniam učiť sa zo spoločných skúseností
- **Koordinácia edge-cloud**: Koordinujte učenie medzi edge zariadeniami a cloudovou infraštruktúrou

### Spracovanie v reálnom čase
- **Spracovanie streamov**: Spracovávajte kontinuálne dátové toky na edge zariadeniach
- **Inferencia s nízkou latenciou**: Optimalizujte pre minimálnu latenciu inferencie
- **Spracovanie dávok**: Efektívne spracovávajte dávky dát na edge zariadeniach
- **Adaptívne spracovanie**: Prispôsobujte spracovanie na základe aktuálnych schopností zariadenia

## Riešenie problémov pri vývoji Edge AI

### Bežné problémy
- **Obmedzenia pamäte**: Model je príliš veľký pre pamäť cieľového zariadenia
- **Rýchlosť inferencie**: Inferencia modelu je príliš pomalá pre požiadavky reálneho času
- **Zhoršenie presnosti**: Optimalizácia neprijateľne znižuje presnosť modelu
- **Kompatibilita hardvéru**: Model nie je kompatibilný s cieľovým hardvérom

### Stratégie ladenia
- **Profilovanie výkonu**: Používajte funkcie sledovania AI Toolkit na identifikáciu úzkych miest
- **Monitorovanie zdrojov**: Monitorujte využitie pamäte a CPU počas vývoja
- **Postupné testovanie**: Testujte optimalizácie postupne na izolovanie problémov
- **Simulácia hardvéru**: Používajte vývojové nástroje na simuláciu cieľového hardvéru

### Riešenia optimalizácie
- **Ďalšia kvantizácia**: Aplikujte agresívnejšie techniky kvantizácie
- **Architektúra modelu**: Zvážte rôzne architektúry modelov optimalizované pre edge
- **Optimalizácia predspracovania**: Optimalizujte predspracovanie dát pre obmedzenia edge
- **Optimalizácia inferencie**: Používajte hardvérové špecifické optimalizácie inferencie

## Zdroje a ďalšie kroky

### Dokumentácia
- [AI Toolkit Models Guide](https://code.visualstudio.com/docs/intelligentapps/models)
- [Model Playground Documentation](https://code.visualstudio.com/docs/intelligentapps/playground)
- [ONNX Runtime Documentation](https://onnxruntime.ai/)
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)

### Komunita a podpora
- [VS Code AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [ONNX Community](https://github.com/onnx/onnx)
- [Edge AI Developer Community](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Vzdelávacie zdroje
- [Kurz základov Edge AI](./Module01/README.md)
- [Sprievodca malými jazykovými modelmi](./Module02/README.md)
- [Stratégie nasadenia na edge](./Module03/README.md)
- [Vývoj Edge AI na Windows](./windowdeveloper.md)

## Záver

AI Toolkit pre Visual Studio Code poskytuje komplexnú platformu pre vývoj Edge AI, od objavovania a optimalizácie modelov až po ich nasadenie a monitorovanie. Vďaka integrovaným nástrojom a pracovným postupom môžu vývojári efektívne vytvárať, testovať a nasadzovať AI aplikácie, ktoré fungujú efektívne na zariadeniach s obmedzenými zdrojmi.

Podpora ONNX, Ollama a rôznych cloudových poskytovateľov, spolu s optimalizačnými a hodnotiacimi schopnosťami, robí z AI Toolkit ideálnu voľbu pre vývoj Edge AI. Či už vytvárate IoT aplikácie, mobilné AI funkcie alebo zabudované inteligentné systémy, AI Toolkit poskytuje nástroje a pracovné postupy potrebné na úspešné nasadenie Edge AI.

Ako sa Edge AI neustále vyvíja, AI Toolkit pre VS Code zostáva na čele, poskytujúc vývojárom špičkové nástroje a schopnosti na budovanie novej generácie inteligentných edge aplikácií.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.