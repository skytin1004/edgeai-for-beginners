<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-18T17:38:58+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "cs"
}
-->
# AI Toolkit pro Visual Studio Code - Průvodce vývojem Edge AI

## Úvod

Vítejte v komplexním průvodci používáním AI Toolkit pro Visual Studio Code při vývoji Edge AI. Jak se umělá inteligence přesouvá z centralizovaného cloudového výpočtu na distribuovaná edge zařízení, vývojáři potřebují výkonné, integrované nástroje, které zvládnou jedinečné výzvy nasazení na edge - od omezených zdrojů po požadavky na offline provoz.

AI Toolkit pro Visual Studio Code překonává tuto mezeru tím, že poskytuje kompletní vývojové prostředí speciálně navržené pro vytváření, testování a optimalizaci AI aplikací, které efektivně běží na edge zařízeních. Ať už vyvíjíte pro IoT senzory, mobilní zařízení, vestavěné systémy nebo edge servery, tento nástroj zjednodušuje celý váš vývojový proces v prostředí, které znáte z VS Code.

Tento průvodce vás provede základními koncepty, nástroji a osvědčenými postupy pro využití AI Toolkit ve vašich Edge AI projektech, od výběru modelu až po nasazení do produkce.

## Přehled

AI Toolkit poskytuje integrované vývojové prostředí pro celý životní cyklus Edge AI aplikací v rámci VS Code. Nabízí bezproblémovou integraci s populárními AI modely od poskytovatelů jako OpenAI, Anthropic, Google a GitHub, a zároveň podporuje lokální nasazení modelů prostřednictvím ONNX a Ollama - klíčové funkce pro Edge AI aplikace, které vyžadují inference přímo na zařízení.

Co odlišuje AI Toolkit pro vývoj Edge AI, je jeho zaměření na celý proces nasazení na edge. Na rozdíl od tradičních AI vývojových nástrojů, které se primárně zaměřují na nasazení v cloudu, AI Toolkit zahrnuje specializované funkce pro optimalizaci modelů, testování v podmínkách omezených zdrojů a hodnocení výkonu specifického pro edge. Nástroj chápe, že vývoj Edge AI vyžaduje jiné přístupy - menší velikosti modelů, rychlejší časy inference, schopnost offline provozu a optimalizace specifické pro hardware.

Platforma podporuje různé scénáře nasazení, od jednoduché inference na zařízení po komplexní architektury s více modely na edge. Poskytuje nástroje pro konverzi modelů, kvantizaci a optimalizaci, které jsou nezbytné pro úspěšné nasazení na edge, a zároveň zachovává produktivitu vývojáře, kterou je VS Code známý.

## Cíle učení

Na konci tohoto průvodce budete schopni:

### Základní dovednosti
- **Nainstalovat a nakonfigurovat** AI Toolkit pro Visual Studio Code pro pracovní postupy vývoje Edge AI
- **Orientovat se a využívat** rozhraní AI Toolkit, včetně Model Catalog, Playground a Agent Builder
- **Vybrat a hodnotit** AI modely vhodné pro nasazení na edge na základě výkonu a omezení zdrojů
- **Konvertovat a optimalizovat** modely pomocí formátu ONNX a technik kvantizace pro edge zařízení

### Dovednosti vývoje Edge AI
- **Navrhnout a implementovat** Edge AI aplikace pomocí integrovaného vývojového prostředí
- **Provádět testování modelů** v podmínkách podobných edge pomocí lokální inference a monitorování zdrojů
- **Vytvářet a přizpůsobovat** AI agenty optimalizované pro scénáře nasazení na edge
- **Hodnotit výkon modelů** pomocí metrik relevantních pro edge computing (latence, využití paměti, přesnost)

### Optimalizace a nasazení
- **Použít kvantizaci a prořezávání** k redukci velikosti modelu při zachování přijatelného výkonu
- **Optimalizovat modely** pro specifické edge hardwarové platformy včetně akcelerace CPU, GPU a NPU
- **Implementovat osvědčené postupy** pro vývoj Edge AI včetně správy zdrojů a záložních strategií
- **Připravit modely a aplikace** pro nasazení do produkce na edge zařízeních

### Pokročilé koncepty Edge AI
- **Integrovat s frameworky Edge AI** včetně ONNX Runtime, Windows ML a TensorFlow Lite
- **Implementovat architektury s více modely** a scénáře federovaného učení pro edge prostředí
- **Řešit běžné problémy Edge AI** včetně omezení paměti, rychlosti inference a kompatibility hardwaru
- **Navrhnout strategie monitorování a logování** pro Edge AI aplikace v produkci

### Praktické využití
- **Vytvořit kompletní Edge AI řešení** od výběru modelu po nasazení
- **Prokázat znalost** vývojových postupů specifických pro edge a optimalizačních technik
- **Aplikovat naučené koncepty** na reálné případy použití Edge AI včetně IoT, mobilních a vestavěných aplikací
- **Hodnotit a porovnávat** různé strategie nasazení Edge AI a jejich kompromisy

## Klíčové funkce pro vývoj Edge AI

### 1. Katalog modelů a jejich objevování
- **Podpora lokálních modelů**: Objevujte a přistupujte k AI modelům speciálně optimalizovaným pro nasazení na edge
- **Integrace ONNX**: Přístup k modelům ve formátu ONNX pro efektivní inference na edge
- **Podpora Ollama**: Využívejte modely běžící lokálně prostřednictvím Ollama pro ochranu soukromí a offline provoz
- **Porovnání modelů**: Porovnávejte modely vedle sebe a najděte optimální rovnováhu mezi výkonem a spotřebou zdrojů pro edge zařízení

### 2. Interaktivní Playground
- **Lokální testovací prostředí**: Testujte modely lokálně před nasazením na edge
- **Experimentování s multimodálními vstupy**: Testujte s obrázky, textem a dalšími vstupy typickými pro edge scénáře
- **Ladění parametrů**: Experimentujte s různými parametry modelu pro optimalizaci omezení na edge
- **Monitorování výkonu v reálném čase**: Sledujte rychlost inference a využití zdrojů během vývoje

### 3. Agent Builder pro Edge aplikace
- **Návrh promptů**: Vytvářejte optimalizované prompty, které efektivně fungují s menšími edge modely
- **Integrace MCP nástrojů**: Integrujte nástroje Model Context Protocol pro rozšířené schopnosti edge agentů
- **Generování kódu**: Generujte kód připravený pro produkci optimalizovaný pro scénáře nasazení na edge
- **Strukturované výstupy**: Navrhujte agenty, kteří poskytují konzistentní, strukturované odpovědi vhodné pro edge aplikace

### 4. Hodnocení a testování modelů
- **Metriky výkonu**: Hodnoťte modely pomocí metrik relevantních pro nasazení na edge (latence, využití paměti, přesnost)
- **Hromadné testování**: Testujte více konfigurací modelů současně a najděte optimální nastavení pro edge
- **Vlastní hodnocení**: Vytvářejte vlastní kritéria hodnocení specifická pro případy použití Edge AI
- **Profilování zdrojů**: Analyzujte požadavky na paměť a výpočetní výkon pro plánování nasazení na edge

### 5. Konverze a optimalizace modelů
- **Konverze do ONNX**: Převádějte modely z různých formátů do ONNX pro kompatibilitu s edge
- **Kvantizace**: Snižte velikost modelu a zlepšete rychlost inference pomocí technik kvantizace
- **Optimalizace hardwaru**: Optimalizujte modely pro specifický edge hardware (CPU, GPU, NPU)
- **Transformace formátů**: Transformujte modely z Hugging Face a dalších zdrojů pro nasazení na edge

### 6. Doladění pro scénáře na edge
- **Adaptace na doménu**: Přizpůsobte modely pro specifické případy použití a prostředí na edge
- **Lokální trénování**: Trénujte modely lokálně s podporou GPU pro specifické požadavky na edge
- **Integrace Azure**: Využívejte Azure Container Apps pro doladění v cloudu před nasazením na edge
- **Transfer Learning**: Přizpůsobte předtrénované modely pro úkoly a omezení specifická pro edge

### 7. Monitorování výkonu a sledování
- **Analýza výkonu na edge**: Sledujte výkon modelu v podmínkách podobných edge
- **Sběr trasování**: Sbírejte podrobné údaje o výkonu pro optimalizaci
- **Identifikace úzkých míst**: Identifikujte problémy s výkonem před nasazením na edge zařízení
- **Sledování využití zdrojů**: Monitorujte paměť, CPU a čas inference pro optimalizaci na edge

## Pracovní postup vývoje Edge AI

### Fáze 1: Objevování a výběr modelů
1. **Prozkoumejte katalog modelů**: Použijte katalog modelů k nalezení modelů vhodných pro nasazení na edge
2. **Porovnejte výkon**: Hodnoťte modely na základě velikosti, přesnosti a rychlosti inference
3. **Testujte lokálně**: Použijte modely Ollama nebo ONNX k lokálnímu testování před nasazením na edge
4. **Posuďte požadavky na zdroje**: Určete potřeby paměti a výpočetního výkonu pro cílová edge zařízení

### Fáze 2: Optimalizace modelů
1. **Převod do ONNX**: Převádějte vybrané modely do formátu ONNX pro kompatibilitu s edge
2. **Použijte kvantizaci**: Snižte velikost modelu pomocí kvantizace INT8 nebo INT4
3. **Optimalizace hardwaru**: Optimalizujte pro cílový edge hardware (ARM, x86, specializované akcelerátory)
4. **Validace výkonu**: Ověřte, že optimalizované modely zachovávají přijatelnou přesnost

### Fáze 3: Vývoj aplikací
1. **Návrh agentů**: Použijte Agent Builder k vytvoření AI agentů optimalizovaných pro edge
2. **Návrh promptů**: Vyvíjejte prompty, které efektivně fungují s menšími modely
3. **Testování integrace**: Testujte agenty v simulovaných podmínkách na edge
4. **Generování kódu**: Generujte produkční kód optimalizovaný pro nasazení na edge

### Fáze 4: Hodnocení a testování
1. **Hromadné hodnocení**: Testujte více konfigurací a najděte optimální nastavení pro edge
2. **Profilování výkonu**: Analyzujte rychlost inference, využití paměti a přesnost
3. **Simulace na edge**: Testujte v podmínkách podobných cílovému prostředí nasazení na edge
4. **Zátěžové testování**: Hodnoťte výkon za různých podmínek zatížení

### Fáze 5: Příprava na nasazení
1. **Finální optimalizace**: Proveďte finální optimalizace na základě výsledků testování
2. **Balíčkování pro nasazení**: Zabalte modely a kód pro nasazení na edge
3. **Dokumentace**: Dokumentujte požadavky na nasazení a konfiguraci
4. **Nastavení monitorování**: Připravte monitorování a logování pro nasazení do produkce

## Cílová skupina pro vývoj Edge AI

### Vývojáři Edge AI
- Vývojáři aplikací vytvářející edge zařízení a IoT řešení poháněná AI
- Vývojáři vestavěných systémů integrující AI schopnosti do zařízení s omezenými zdroji
- Mobilní vývojáři vytvářející AI aplikace běžící přímo na zařízeních

### Inženýři Edge AI
- AI inženýři optimalizující modely pro nasazení na edge a spravující inference pipeline
- DevOps inženýři nasazující a spravující AI modely na distribuované edge infrastruktuře
- Inženýři výkonu optimalizující AI pracovní zátěže pro omezení edge hardwaru

### Výzkumníci a pedagogové
- AI výzkumníci vyvíjející efektivní modely a algoritmy pro edge computing
- Pedagogové vyučující koncepty Edge AI a demonstrující optimalizační techniky
- Studenti učící se o výzvách a řešeních při nasazení Edge AI

## Případy použití Edge AI

### Chytrá IoT zařízení
- **Rozpoznávání obrazu v reálném čase**: Nasazení modelů počítačového vidění na IoT kamerách a senzorech
- **Zpracování hlasu**: Implementace rozpoznávání řeči a zpracování přirozeného jazyka na chytrých reproduktorech
- **Prediktivní údržba**: Spouštění modelů detekce anomálií na průmyslových edge zařízeních
- **Monitorování prostředí**: Nasazení modelů analýzy dat ze senzorů pro environmentální aplikace

### Mobilní a vestavěné aplikace
- **Překlad na zařízení**: Implementace modelů překladu jazyků, které fungují offline
- **Rozšířená realita**: Nasazení rozpoznávání objektů v reálném čase a sledování pro AR aplikace
- **Monitorování zdraví**: Spouštění modelů analýzy zdraví na nositelných zařízeních a lékařském vybavení
- **Autonomní systémy**: Implementace modelů rozhodování pro drony, roboty a vozidla

### Edge výpočetní infrastruktura
- **Edge datová centra**: Nasazení AI modelů v edge datových centrech pro aplikace s nízkou latencí
- **Integrace CDN**: Integrace schopností AI zpracování do sítí pro doručování obsahu
- **5G Edge**: Využití edge computingu s 5G pro aplikace poháněné AI
- **Fog Computing**: Implementace AI zpracování v prostředích fog computingu

## Instalace a nastavení

### Rychlá instalace
Nainstalujte rozšíření AI Toolkit přímo z Visual Studio Code Marketplace:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Předpoklady pro vývoj Edge AI
- **ONNX Runtime**: Nainstalujte ONNX Runtime pro inference modelů
- **Ollama** (volitelné): Nainstalujte Ollama pro lokální obsluhu modelů
- **Python prostředí**: Nastavte Python s požadovanými AI knihovnami
- **Nástroje pro edge hardware**: Nainstalujte nástroje pro vývoj specifické pro hardware (CUDA, OpenVINO, atd.)

### Počáteční konfigurace
1. Otevřete VS Code a nainstalujte rozšíření AI Toolkit
2. Nakonfigurujte zdroje modelů (ONNX, Ollama, poskytovatelé cloudu)
3. Nastavte lokální vývojové prostředí pro testování na edge
4. Nakonfigurujte možnosti hardwarové akcelerace pro váš vývojový stroj

## Začínáme s vývojem Edge AI

### Krok 1: Výběr modelu
1. Otevřete zobrazení AI Toolkit v Activity Bar
2. Procházejte katalog modelů pro modely kompatibilní s edge
3. Filtrovat podle velikosti modelu, formátu (ONNX) a charakteristik výkonu
4. Porovnávejte modely pomocí vestavěných nástrojů pro porovnání

### Krok 2: Lokální testování
1. Použijte Playground k testování vybraných modelů lokálně
2. Experimentujte s různými prompty a parametry
3. Sledujte metriky výkonu během testování
4. Hodnoťte odpovědi modelů pro požadavky na edge případy použití

### Krok 3: Optimalizace modelu
1. Použijte nástroje pro konverzi modelů k optimalizaci pro nasazení na edge
2. Použijte kvantizaci ke snížení velikosti modelu
3. Testujte optimalizované modely pro zajištění přijatelného výkonu
4. Dokumentujte nastavení optimalizace a kompromisy výkonu

### Krok 4: Vývoj agentů
1. Použijte Agent Builder k vytvoření AI agentů optimalizovaných pro
- **Zabezpečení**: Implementujte vhodná bezpečnostní opatření pro aplikace Edge AI

## Integrace s Edge AI frameworky

### ONNX Runtime
- **Nasazení napříč platformami**: Nasazujte ONNX modely na různých edge platformách
- **Optimalizace hardwaru**: Využijte hardwarově specifické optimalizace ONNX Runtime
- **Podpora mobilních zařízení**: Používejte ONNX Runtime Mobile pro aplikace na smartphonech a tabletech
- **Integrace s IoT**: Nasazujte na IoT zařízení pomocí lehkých distribucí ONNX Runtime

### Windows ML
- **Zařízení s Windows**: Optimalizujte pro edge zařízení a PC s Windows
- **Akcelerace pomocí NPU**: Využijte Neural Processing Units na zařízeních s Windows
- **DirectML**: Používejte DirectML pro akceleraci GPU na platformách Windows
- **Integrace s UWP**: Integrujte s aplikacemi Universal Windows Platform

### TensorFlow Lite
- **Optimalizace pro mobilní zařízení**: Nasazujte TensorFlow Lite modely na mobilní a vestavěná zařízení
- **Hardwaroví delegáti**: Používejte specializované hardwarové delegáty pro akceleraci
- **Mikrokontroléry**: Nasazujte na mikrokontroléry pomocí TensorFlow Lite Micro
- **Podpora napříč platformami**: Nasazujte na Android, iOS a vestavěné systémy Linux

### Azure IoT Edge
- **Hybridní cloud-edge**: Kombinujte trénování v cloudu s inferencí na edge
- **Nasazení modulů**: Nasazujte AI modely jako moduly IoT Edge
- **Správa zařízení**: Spravujte edge zařízení a aktualizace modelů na dálku
- **Telemetrie**: Sbírejte data o výkonu a metriky modelů z edge nasazení

## Pokročilé scénáře Edge AI

### Nasazení více modelů
- **Modelové ensemble**: Nasazujte více modelů pro zlepšení přesnosti nebo redundanci
- **A/B testování**: Testujte různé modely současně na edge zařízeních
- **Dynamický výběr**: Volte modely na základě aktuálních podmínek zařízení
- **Sdílení zdrojů**: Optimalizujte využití zdrojů napříč nasazenými modely

### Federované učení
- **Distribuované trénování**: Trénujte modely na více edge zařízeních
- **Zachování soukromí**: Uchovávejte trénovací data lokálně a sdílejte pouze vylepšení modelů
- **Spolupracující učení**: Umožněte zařízením učit se z kolektivních zkušeností
- **Koordinace edge-cloud**: Koordinujte učení mezi edge zařízeními a cloudovou infrastrukturou

### Zpracování v reálném čase
- **Streamové zpracování**: Zpracovávejte kontinuální datové toky na edge zařízeních
- **Inferenční nízká latence**: Optimalizujte pro minimální latenci inferencí
- **Batchové zpracování**: Efektivně zpracovávejte dávky dat na edge zařízeních
- **Adaptivní zpracování**: Přizpůsobte zpracování na základě aktuálních schopností zařízení

## Řešení problémů při vývoji Edge AI

### Běžné problémy
- **Paměťová omezení**: Model je příliš velký pro paměť cílového zařízení
- **Rychlost inferencí**: Inferenční rychlost modelu je příliš pomalá pro požadavky reálného času
- **Degradace přesnosti**: Optimalizace nepřijatelně snižuje přesnost modelu
- **Kompatibilita hardwaru**: Model není kompatibilní s cílovým hardwarem

### Strategie ladění
- **Profilování výkonu**: Používejte funkce sledování AI Toolkit k identifikaci úzkých míst
- **Monitorování zdrojů**: Sledujte využití paměti a CPU během vývoje
- **Postupné testování**: Testujte optimalizace postupně, abyste izolovali problémy
- **Simulace hardwaru**: Používejte vývojové nástroje k simulaci cílového hardwaru

### Řešení optimalizace
- **Další kvantizace**: Aplikujte agresivnější techniky kvantizace
- **Architektura modelu**: Zvažte různé architektury modelů optimalizované pro edge
- **Optimalizace předzpracování**: Optimalizujte předzpracování dat pro omezení na edge
- **Optimalizace inferencí**: Používejte hardwarově specifické optimalizace inferencí

## Zdroje a další kroky

### Dokumentace
- [AI Toolkit Models Guide](https://code.visualstudio.com/docs/intelligentapps/models)
- [Model Playground Documentation](https://code.visualstudio.com/docs/intelligentapps/playground)
- [ONNX Runtime Documentation](https://onnxruntime.ai/)
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)

### Komunita a podpora
- [VS Code AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [ONNX Community](https://github.com/onnx/onnx)
- [Edge AI Developer Community](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Výukové materiály
- [Kurz základů Edge AI](./Module01/README.md)
- [Průvodce malými jazykovými modely](./Module02/README.md)
- [Strategie nasazení na edge](./Module03/README.md)
- [Vývoj Edge AI na Windows](./windowdeveloper.md)

## Závěr

AI Toolkit pro Visual Studio Code poskytuje komplexní platformu pro vývoj Edge AI, od objevování a optimalizace modelů až po jejich nasazení a monitorování. Díky integrovaným nástrojům a pracovním postupům mohou vývojáři efektivně vytvářet, testovat a nasazovat AI aplikace, které fungují efektivně na zařízeních s omezenými zdroji.

Podpora nástrojů jako ONNX, Ollama a různých poskytovatelů cloudových služeb, spolu s optimalizačními a hodnotícími schopnostmi, činí AI Toolkit ideální volbou pro vývoj Edge AI. Ať už vytváříte IoT aplikace, mobilní AI funkce nebo vestavěné inteligentní systémy, AI Toolkit poskytuje nástroje a pracovní postupy potřebné pro úspěšné nasazení Edge AI.

Jak se Edge AI dále vyvíjí, AI Toolkit pro VS Code zůstává v čele, poskytuje vývojářům špičkové nástroje a schopnosti pro budování nové generace inteligentních edge aplikací.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.