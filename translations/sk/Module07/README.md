<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-18T19:09:32+00:00",
  "source_file": "Module07/README.md",
  "language_code": "sk"
}
-->
# Kapitola 07: EdgeAI Príklady

Edge AI predstavuje spojenie umelej inteligencie s edge computingom, umožňujúce inteligentné spracovanie priamo na zariadeniach bez závislosti na cloudovej konektivite. Táto kapitola skúma päť rôznych implementácií EdgeAI na rôznych platformách a frameworkoch, ktoré ukazujú všestrannosť a silu spúšťania AI modelov na edge zariadeniach.

## 1. EdgeAI na NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano predstavuje prelom v dostupnom edge AI computingu, poskytujúc až 67 TOPS AI výkonu v kompaktnom formáte veľkosti kreditnej karty. Táto výkonná edge AI platforma demokratizuje vývoj generatívnej AI pre nadšencov, študentov a profesionálnych vývojárov.

### Kľúčové vlastnosti
- Poskytuje až 67 TOPS AI výkonu—zlepšenie o 1,7X oproti predchodcovi
- 1024 CUDA jadier a až 32 Tensor jadier pre AI spracovanie
- 6-jadrový Arm Cortex-A78AE v8.2 64-bitový CPU s maximálnou frekvenciou 1,5 GHz
- Cena len $249, čo poskytuje vývojárom, študentom a tvorcom najdostupnejšiu platformu

### Aplikácie
Jetson Orin Nano vyniká pri spúšťaní moderných generatívnych AI modelov vrátane vision transformerov, veľkých jazykových modelov a vision-language modelov. Je špeciálne navrhnutý pre GenAI prípady použitia a teraz môžete spúšťať niekoľko LLM na zariadení veľkosti dlane. Populárne prípady použitia zahŕňajú AI-poháňanú robotiku, inteligentné drony, inteligentné kamery a autonómne edge zariadenia.

**Viac informácií**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI v mobilných aplikáciách s .NET MAUI a ONNX Runtime GenAI

Toto riešenie demonštruje, ako integrovať Generatívnu AI a Veľké Jazykové Modely (LLMs) do multiplatformových mobilných aplikácií pomocou .NET MAUI (Multi-platform App UI) a ONNX Runtime GenAI. Tento prístup umožňuje .NET vývojárom vytvárať sofistikované AI-poháňané mobilné aplikácie, ktoré bežia natívne na Android a iOS zariadeniach.

### Kľúčové vlastnosti
- Postavené na .NET MAUI frameworku, poskytujúcom jeden kódový základ pre Android aj iOS aplikácie
- Integrácia ONNX Runtime GenAI umožňuje spúšťanie generatívnych AI modelov priamo na mobilných zariadeniach
- Podpora rôznych hardvérových akcelerátorov prispôsobených pre mobilné zariadenia, vrátane CPU, GPU a špecializovaných mobilných AI procesorov
- Platformovo špecifické optimalizácie ako CoreML pre iOS a NNAPI pre Android cez ONNX Runtime
- Implementuje kompletný generatívny AI cyklus vrátane predspracovania, inferencie, spracovania logits, vyhľadávania a vzorkovania, a správy KV cache

### Výhody vývoja
Prístup .NET MAUI umožňuje vývojárom využiť ich existujúce C# a .NET zručnosti pri vytváraní multiplatformových AI aplikácií. ONNX Runtime GenAI framework podporuje rôzne modelové architektúry vrátane Llama, Mistral, Phi, Gemma a mnohých ďalších. Optimalizované ARM64 jadrá urýchľujú INT4 kvantizované násobenie matíc, čím zabezpečujú efektívny výkon na mobilnom hardvéri pri zachovaní známeho .NET vývojového prostredia.

### Prípady použitia
Toto riešenie je ideálne pre vývojárov, ktorí chcú vytvárať AI-poháňané mobilné aplikácie pomocou .NET technológií, vrátane inteligentných chatbotov, aplikácií na rozpoznávanie obrázkov, nástrojov na preklad jazykov a personalizovaných odporúčacích systémov, ktoré fungujú úplne na zariadení pre zvýšenú ochranu súkromia a offline schopnosti.

**Viac informácií**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI v Azure s Small Language Models Engine

Microsoftova Azure-based EdgeAI riešenie sa zameriava na efektívne nasadenie Malých Jazykových Modelov (SLMs) v hybridných cloud-edge prostrediach. Tento prístup prekonáva medzeru medzi cloudovými AI službami a požiadavkami na edge nasadenie.

### Výhody architektúry
- Bezproblémová integrácia s Azure AI službami
- Spúšťanie SLMs/LLMs a multimodálnych modelov na zariadení aj v cloude pomocou ONNX Runtime
- Optimalizované pre nasadenie v podnikovej škále
- Podpora kontinuálnych aktualizácií a správy modelov

### Prípady použitia
Azure EdgeAI implementácia vyniká v scenároch vyžadujúcich podnikové AI nasadenie s cloudovými manažmentovými schopnosťami. To zahŕňa inteligentné spracovanie dokumentov, analýzu v reálnom čase a hybridné AI pracovné postupy, ktoré využívajú cloud aj edge computingové zdroje.

**Viac informácií**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI s Windows ML

Windows ML predstavuje najmodernejší runtime od Microsoftu optimalizovaný pre výkonné inferencie modelov na zariadení a zjednodušené nasadenie, slúžiaci ako základ Windows AI Foundry. Táto platforma umožňuje vývojárom vytvárať AI-poháňané Windows aplikácie, ktoré využívajú plné spektrum PC hardvéru.

### Schopnosti platformy
- Funguje na všetkých Windows 11 PC s verziou 24H2 (build 26100) alebo vyššou
- Funguje na všetkom x64 a ARM64 PC hardvéri, dokonca aj na PC bez NPU alebo GPU
- Umožňuje vývojárom priniesť vlastné modely a efektívne ich nasadiť naprieč ekosystémom silikónových partnerov vrátane AMD, Intel, NVIDIA a Qualcomm, pokrývajúc CPU, GPU, NPU
- Vďaka infraštruktúrnym API vývojári už nemusia vytvárať viacero buildov aplikácie na zacielenie rôznych silikónov

### Výhody pre vývojárov
Windows ML abstrahuje hardvér a poskytovateľov vykonávania, takže sa môžete sústrediť na písanie kódu. Navyše, Windows ML sa automaticky aktualizuje na podporu najnovších NPU, GPU a CPU, keď sú vydané. Platforma poskytuje jednotný framework pre AI vývoj naprieč rôznorodým Windows hardvérovým ekosystémom.

**Viac informácií**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](../windowdeveloper.md) - Komplexný sprievodca pre Windows Edge AI vývoj

## 5. EdgeAI s Foundry Local aplikáciami

Foundry Local umožňuje vývojárom vytvárať aplikácie na Retrieval Augmented Generation (RAG) pomocou lokálnych zdrojov v .NET, kombinujúc lokálne jazykové modely so semantickými vyhľadávacími schopnosťami. Tento prístup poskytuje AI riešenia zamerané na ochranu súkromia, ktoré fungujú úplne na lokálnej infraštruktúre.

### Technická architektúra
- Kombinuje jazykový model Phi-3, Lokálne Embeddingy a Semantické Jadro na vytvorenie RAG scenára
- Používa embeddingy ako vektory (polia) hodnôt s plávajúcou desatinnou čiarkou, ktoré reprezentujú obsah a jeho semantický význam
- Semantické Jadro funguje ako hlavný orchestrátor, integrujúci Phi-3 a Inteligentné Komponenty na vytvorenie plynulého RAG pipeline
- Podpora lokálnych vektorových databáz vrátane SQLite a Qdrant

### Výhody implementácie
RAG, alebo Retrieval Augmented Generation, je len sofistikovaný spôsob, ako povedať „vyhľadajte nejaké informácie a vložte ich do promptu“. Táto lokálna implementácia zabezpečuje ochranu údajov pri poskytovaní inteligentných odpovedí založených na vlastných znalostných databázach. Prístup je obzvlášť cenný pre podnikové scenáre vyžadujúce suverenitu údajov a offline schopnosti.

**Viac informácií**: [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Windows EdgeAI Vývojové zdroje

Pre vývojárov špecificky zameraných na Windows platformu sme vytvorili komplexný sprievodca, ktorý pokrýva celý Windows EdgeAI ekosystém. Tento zdroj poskytuje podrobné informácie o Windows AI Foundry, vrátane API, nástrojov a najlepších praktík pre EdgeAI vývoj na Windows.

### Windows AI Foundry Platforma
Windows AI Foundry platforma poskytuje komplexný súbor nástrojov a API špeciálne navrhnutých pre Edge AI vývoj na Windows zariadeniach. To zahŕňa špecializovanú podporu pre NPU-akcelerovaný hardvér, integráciu Windows ML a platformovo špecifické optimalizačné techniky.

**Komplexný sprievodca**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Tento sprievodca pokrýva:
- Prehľad a komponenty Windows AI Foundry platformy
- Phi Silica API pre efektívnu inferenciu na NPU hardvéri
- API pre počítačové videnie na spracovanie obrázkov a OCR
- Integráciu a optimalizáciu Windows ML runtime
- Foundry Local CLI pre lokálny vývoj a testovanie
- Stratégie optimalizácie hardvéru pre Windows zariadenia
- Praktické príklady implementácie a najlepšie praktiky

### AI Toolkit pre Edge AI vývoj
Pre vývojárov používajúcich Visual Studio Code poskytuje rozšírenie AI Toolkit komplexné vývojové prostredie špeciálne navrhnuté na vytváranie, testovanie a nasadzovanie Edge AI aplikácií. Tento toolkit zjednodušuje celý Edge AI vývojový workflow v rámci VS Code.

**Vývojový sprievodca**: [AI Toolkit for Edge AI Development](../aitoolkit.md)

Sprievodca AI Toolkit pokrýva:
- Objavovanie a výber modelov pre edge nasadenie
- Lokálne testovanie a optimalizačné workflowy
- Integráciu ONNX a Ollama pre edge modely
- Techniky konverzie a kvantizácie modelov
- Vývoj agentov pre edge scenáre
- Hodnotenie výkonu a monitorovanie
- Prípravu na nasadenie a najlepšie praktiky

## Záver

Týchto päť implementácií EdgeAI demonštruje vyspelosť a rozmanitosť edge AI riešení dostupných dnes. Od hardvérovo akcelerovaných edge zariadení ako Jetson Orin Nano po softvérové frameworky ako ONNX Runtime GenAI a Windows ML, vývojári majú bezprecedentné možnosti na nasadenie inteligentných aplikácií na edge.

Spoločným prvkom všetkých týchto platforiem je demokratizácia AI schopností, ktorá robí sofistikované strojové učenie dostupným pre vývojárov na rôznych úrovniach zručností a pre rôzne prípady použitia. Či už ide o tvorbu mobilných aplikácií, desktopového softvéru alebo embedded systémov, tieto EdgeAI riešenia poskytujú základ pre ďalšiu generáciu inteligentných aplikácií, ktoré fungujú efektívne a súkromne na edge.

Každá platforma ponúka jedinečné výhody: Jetson Orin Nano pre hardvérovo akcelerovaný edge computing, ONNX Runtime GenAI pre multiplatformový mobilný vývoj, Azure EdgeAI pre podnikové cloud-edge integrácie, Windows ML pre Windows-native aplikácie a Foundry Local pre implementácie RAG zamerané na ochranu súkromia. Spoločne predstavujú komplexný ekosystém pre EdgeAI vývoj.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.