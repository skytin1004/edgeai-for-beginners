<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-18T17:27:26+00:00",
  "source_file": "Module07/README.md",
  "language_code": "cs"
}
-->
# Kapitola 07: Ukázky EdgeAI

Edge AI představuje spojení umělé inteligence s edge computingem, umožňující inteligentní zpracování přímo na zařízeních bez nutnosti připojení ke cloudu. Tato kapitola zkoumá pět různých implementací EdgeAI na různých platformách a v různých rámcích, ukazující všestrannost a sílu provozování AI modelů na edge.

## 1. EdgeAI na NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano představuje průlom v dostupném edge AI computingu, poskytující až 67 TOPS výkonu AI v kompaktním formátu velikosti kreditní karty. Tato výkonná platforma pro edge AI demokratizuje vývoj generativní AI pro nadšence, studenty i profesionální vývojáře.

### Klíčové vlastnosti
- Poskytuje až 67 TOPS výkonu AI—zlepšení o 1,7X oproti předchozí generaci
- 1024 CUDA jader a až 32 Tensor jader pro AI zpracování
- 6jádrový Arm Cortex-A78AE v8.2 64bitový CPU s maximální frekvencí 1,5 GHz
- Cena pouhých $249, což poskytuje vývojářům, studentům a tvůrcům nejdostupnější platformu

### Aplikace
Jetson Orin Nano vyniká při provozování moderních generativních AI modelů, včetně vision transformerů, velkých jazykových modelů a vision-language modelů. Je speciálně navržen pro použití v generativní AI a nyní můžete provozovat několik LLM na zařízení velikosti dlaně. Mezi oblíbené případy použití patří robotika poháněná AI, chytré drony, inteligentní kamery a autonomní edge zařízení.

**Více informací**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI v mobilních aplikacích s .NET MAUI a ONNX Runtime GenAI

Toto řešení ukazuje, jak integrovat generativní AI a velké jazykové modely (LLMs) do multiplatformních mobilních aplikací pomocí .NET MAUI (Multi-platform App UI) a ONNX Runtime GenAI. Tento přístup umožňuje .NET vývojářům vytvářet sofistikované mobilní aplikace poháněné AI, které běží nativně na zařízeních Android a iOS.

### Klíčové vlastnosti
- Postaveno na frameworku .NET MAUI, poskytující jednotný kódový základ pro aplikace na Androidu i iOS
- Integrace ONNX Runtime GenAI umožňuje provozování generativních AI modelů přímo na mobilních zařízeních
- Podpora různých hardwarových akcelerátorů přizpůsobených mobilním zařízením, včetně CPU, GPU a specializovaných mobilních AI procesorů
- Platformově specifické optimalizace jako CoreML pro iOS a NNAPI pro Android prostřednictvím ONNX Runtime
- Implementuje kompletní generativní AI smyčku včetně předzpracování, inference, zpracování logits, vyhledávání a vzorkování, a správy KV cache

### Výhody pro vývojáře
Přístup .NET MAUI umožňuje vývojářům využít jejich stávající znalosti C# a .NET při vytváření multiplatformních AI aplikací. Framework ONNX Runtime GenAI podporuje různé modelové architektury, včetně Llama, Mistral, Phi, Gemma a dalších. Optimalizované ARM64 jádra urychlují INT4 kvantizované násobení matic, což zajišťuje efektivní výkon na mobilním hardwaru při zachování známého prostředí .NET.

### Případy použití
Toto řešení je ideální pro vývojáře, kteří chtějí vytvářet mobilní aplikace poháněné AI pomocí .NET technologií, včetně inteligentních chatbotů, aplikací pro rozpoznávání obrazu, nástrojů pro překlad jazyků a personalizovaných doporučovacích systémů, které běží zcela na zařízení pro zvýšené soukromí a offline schopnosti.

**Více informací**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI v Azure s Small Language Models Engine

Řešení EdgeAI od Microsoftu založené na Azure se zaměřuje na efektivní nasazení malých jazykových modelů (SLMs) v hybridních prostředích cloud-edge. Tento přístup překonává propast mezi cloudovými AI službami a požadavky na nasazení na edge.

### Výhody architektury
- Bezproblémová integrace s Azure AI službami
- Provozování SLMs/LLMs a multimodálních modelů na zařízení i v cloudu pomocí ONNX Runtime
- Optimalizováno pro nasazení v měřítku podniků
- Podpora kontinuálních aktualizací a správy modelů

### Případy použití
Implementace Azure EdgeAI vyniká ve scénářích vyžadujících AI nasazení na podnikové úrovni s možnostmi správy v cloudu. To zahrnuje inteligentní zpracování dokumentů, analýzu v reálném čase a hybridní AI pracovní postupy, které využívají jak cloud, tak edge computing.

**Více informací**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI s Windows ML

Windows ML představuje špičkový runtime od Microsoftu optimalizovaný pro výkonné modelové inference na zařízení a zjednodušené nasazení, sloužící jako základ Windows AI Foundry. Tato platforma umožňuje vývojářům vytvářet aplikace pro Windows poháněné AI, které využívají plný potenciál PC hardwaru.

### Schopnosti platformy
- Funguje na všech PC s Windows 11, verze 24H2 (build 26100) nebo vyšší
- Funguje na všech x64 a ARM64 PC hardwaru, dokonce i na PC bez NPU nebo GPU
- Umožňuje vývojářům přinést vlastní modely a efektivně je nasadit napříč ekosystémem hardwarových partnerů, včetně AMD, Intel, NVIDIA a Qualcomm, pokrývající CPU, GPU, NPU
- Díky infrastrukturním API již vývojáři nemusí vytvářet více buildů aplikace pro cílení na různé typy hardwaru

### Výhody pro vývojáře
Windows ML abstrahuje hardware a poskytovatele exekuce, takže se můžete soustředit na psaní svého kódu. Navíc se Windows ML automaticky aktualizuje, aby podporoval nejnovější NPU, GPU a CPU, jakmile jsou vydány. Platforma poskytuje jednotný rámec pro vývoj AI napříč různorodým ekosystémem hardwaru Windows.

**Více informací**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](../windowdeveloper.md) - Komplexní průvodce pro vývoj Edge AI na Windows

## 5. EdgeAI s Foundry Local Applications

Foundry Local umožňuje vývojářům vytvářet aplikace pro Retrieval Augmented Generation (RAG) pomocí lokálních zdrojů v .NET, kombinující lokální jazykové modely se schopnostmi sémantického vyhledávání. Tento přístup poskytuje řešení AI zaměřená na soukromí, která fungují zcela na lokální infrastruktuře.

### Technická architektura
- Kombinuje jazykový model Phi-3, lokální embeddings a Semantic Kernel pro vytvoření RAG scénáře
- Používá embeddings jako vektory (pole) hodnot s plovoucí desetinnou čárkou, které reprezentují obsah a jeho sémantický význam
- Semantic Kernel funguje jako hlavní orchestrátor, integrující Phi-3 a chytré komponenty pro vytvoření plynulého RAG pipeline
- Podpora lokálních vektorových databází včetně SQLite a Qdrant

### Výhody implementace
RAG, neboli Retrieval Augmented Generation, je jen sofistikovaný způsob, jak říci "vyhledej nějaké informace a vlož je do promptu". Tato lokální implementace zajišťuje ochranu dat při poskytování inteligentních odpovědí založených na vlastních znalostních bázích. Přístup je obzvláště cenný pro podnikové scénáře vyžadující suverenitu dat a schopnosti offline provozu.

**Více informací**: [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Vývojové zdroje pro Windows EdgeAI

Pro vývojáře zaměřené specificky na platformu Windows jsme vytvořili komplexní průvodce, který pokrývá celý ekosystém Windows EdgeAI. Tento zdroj poskytuje podrobné informace o Windows AI Foundry, včetně API, nástrojů a osvědčených postupů pro vývoj EdgeAI na Windows.

### Platforma Windows AI Foundry
Platforma Windows AI Foundry poskytuje komplexní sadu nástrojů a API speciálně navržených pro vývoj Edge AI na zařízeních Windows. To zahrnuje specializovanou podporu pro hardware akcelerovaný NPU, integraci Windows ML a techniky optimalizace specifické pro platformu.

**Komplexní průvodce**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Tento průvodce zahrnuje:
- Přehled platformy Windows AI Foundry a jejích komponent
- Phi Silica API pro efektivní inference na NPU hardwaru
- API pro počítačové vidění pro zpracování obrazu a OCR
- Integraci a optimalizaci runtime Windows ML
- Foundry Local CLI pro lokální vývoj a testování
- Strategie optimalizace hardwaru pro zařízení Windows
- Praktické příklady implementace a osvědčené postupy

### AI Toolkit pro vývoj Edge AI
Pro vývojáře používající Visual Studio Code poskytuje rozšíření AI Toolkit komplexní vývojové prostředí speciálně navržené pro vytváření, testování a nasazování Edge AI aplikací. Tento nástroj zjednodušuje celý pracovní postup vývoje Edge AI v rámci VS Code.

**Průvodce vývojem**: [AI Toolkit for Edge AI Development](../aitoolkit.md)

Průvodce AI Toolkit zahrnuje:
- Objevování a výběr modelů pro nasazení na edge
- Lokální testování a optimalizační pracovní postupy
- Integraci ONNX a Ollama pro edge modely
- Techniky konverze a kvantizace modelů
- Vývoj agentů pro edge scénáře
- Hodnocení výkonu a monitorování
- Přípravu na nasazení a osvědčené postupy

## Závěr

Těchto pět implementací EdgeAI demonstruje vyspělost a rozmanitost dostupných řešení Edge AI. Od zařízení s hardwarovou akcelerací, jako je Jetson Orin Nano, po softwarové rámce, jako jsou ONNX Runtime GenAI a Windows ML, mají vývojáři bezprecedentní možnosti pro nasazení inteligentních aplikací na edge.

Společným prvkem všech těchto platforem je demokratizace schopností AI, která zpřístupňuje sofistikované strojové učení vývojářům různých úrovní dovedností a případů použití. Ať už vytváříte mobilní aplikace, desktopový software nebo embedded systémy, tato řešení EdgeAI poskytují základ pro novou generaci inteligentních aplikací, které fungují efektivně a soukromě na edge.

Každá platforma nabízí jedinečné výhody: Jetson Orin Nano pro hardwarově akcelerovaný edge computing, ONNX Runtime GenAI pro multiplatformní mobilní vývoj, Azure EdgeAI pro integraci cloud-edge na podnikové úrovni, Windows ML pro nativní aplikace na Windows a Foundry Local pro implementace RAG zaměřené na soukromí. Společně představují komplexní ekosystém pro vývoj EdgeAI.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.