<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e9e31a2b5ff0f6a682a258fa859a8ff5",
  "translation_date": "2025-09-26T19:41:44+00:00",
  "source_file": "Module07/README.md",
  "language_code": "hu"
}
-->
# 7. fejezet: EdgeAI minták

Az Edge AI az intelligens számítástechnika és az edge computing találkozását jelenti, lehetővé téve az intelligens feldolgozást közvetlenül az eszközökön, anélkül, hogy a felhőkapcsolatra támaszkodnánk. Ez a fejezet öt különböző EdgeAI megvalósítást mutat be különböző platformokon és keretrendszereken, bemutatva az AI modellek edge környezetben történő futtatásának sokoldalúságát és erejét.

## 1. EdgeAI az NVIDIA Jetson Orin Nano platformon

Az NVIDIA Jetson Orin Nano áttörést jelent az elérhető edge AI számítástechnikában, akár 67 TOPS AI teljesítményt nyújtva egy kompakt, hitelkártya méretű formában. Ez a hatékony edge AI platform demokratizálja a generatív AI fejlesztést hobbisták, diákok és professzionális fejlesztők számára.

### Főbb jellemzők
- Akár 67 TOPS AI teljesítményt nyújt—a korábbi modellhez képest 1,7-szeres javulás
- 1024 CUDA mag és akár 32 Tensor Core az AI feldolgozáshoz
- 6-magos Arm Cortex-A78AE v8.2 64 bites CPU, maximum 1,5 GHz frekvenciával
- Mindössze 249 dolláros áron, a legmegfizethetőbb és legelérhetőbb platformot kínálva fejlesztők, diákok és alkotók számára

### Alkalmazások
A Jetson Orin Nano kiválóan alkalmas modern generatív AI modellek futtatására, beleértve a látás transzformátorokat, nagy nyelvi modelleket és látás-nyelv modelleket. Kifejezetten GenAI felhasználási esetekre tervezték, és most már több LLM-et is futtathat egy tenyérnyi eszközön. Népszerű felhasználási területek közé tartoznak az AI-alapú robotika, okos drónok, intelligens kamerák és autonóm edge eszközök.

**További információ**: [NVIDIA Jetson Orin Nano szuperkomputer: Az EdgeAI következő nagy dobása](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI mobilalkalmazásokban .NET MAUI és ONNX Runtime GenAI segítségével

Ez a megoldás bemutatja, hogyan integrálhatók a Generatív AI és Nagy Nyelvi Modellek (LLM-ek) keresztplatformos mobilalkalmazásokba a .NET MAUI (Multi-platform App UI) és az ONNX Runtime GenAI segítségével. Ez a megközelítés lehetővé teszi a .NET fejlesztők számára, hogy kifinomult AI-alapú mobilalkalmazásokat építsenek, amelyek natívan futnak Android és iOS eszközökön.

### Főbb jellemzők
- A .NET MAUI keretrendszerre épül, amely egyetlen kódbázist biztosít Android és iOS alkalmazásokhoz
- Az ONNX Runtime GenAI integráció lehetővé teszi generatív AI modellek futtatását közvetlenül mobil eszközökön
- Támogatja a mobil eszközökre szabott különféle hardvergyorsítókat, beleértve a CPU-t, GPU-t és speciális mobil AI processzorokat
- Platformspecifikus optimalizációk, mint például CoreML iOS-hez és NNAPI Androidhoz az ONNX Runtime segítségével
- Megvalósítja a teljes generatív AI folyamatot, beleértve az elő- és utófeldolgozást, az inferenciát, a logit feldolgozást, a keresést és mintavételezést, valamint a KV cache kezelését

### Fejlesztési előnyök
A .NET MAUI megközelítés lehetővé teszi a fejlesztők számára, hogy meglévő C# és .NET készségeiket kihasználva építsenek keresztplatformos AI alkalmazásokat. Az ONNX Runtime GenAI keretrendszer több modellarchitektúrát támogat, beleértve a Llama, Mistral, Phi, Gemma és sok más modellt. Az optimalizált ARM64 kernel gyorsítja az INT4 kvantált mátrixszorzást, biztosítva a hatékony teljesítményt mobil hardveren, miközben megőrzi a megszokott .NET fejlesztési élményt.

### Felhasználási esetek
Ez a megoldás ideális azoknak a fejlesztőknek, akik AI-alapú mobilalkalmazásokat szeretnének építeni .NET technológiák segítségével, beleértve az intelligens chatbotokat, képfelismerő alkalmazásokat, nyelvfordító eszközöket és személyre szabott ajánlórendszereket, amelyek teljes mértékben eszközön futnak a fokozott adatvédelem és offline képességek érdekében.

**További információ**: [.NET MAUI ONNX Runtime GenAI példa](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI az Azure-ban Kis Nyelvi Modellek Motorjával

A Microsoft Azure-alapú EdgeAI megoldása a Kis Nyelvi Modellek (SLM-ek) hatékony telepítésére összpontosít felhő-edge hibrid környezetekben. Ez a megközelítés áthidalja a felhőméretű AI szolgáltatások és az edge telepítési követelmények közötti szakadékot.

### Architektúra előnyei
- Zökkenőmentes integráció az Azure AI szolgáltatásokkal
- SLM-ek/LLM-ek és multimodális modellek futtatása eszközön és felhőben az ONNX Runtime segítségével
- Optimalizált vállalati méretű telepítéshez
- Támogatás a folyamatos modellfrissítésekhez és kezeléshez

### Felhasználási esetek
Az Azure EdgeAI megvalósítás kiválóan alkalmas olyan helyzetekben, amelyek vállalati szintű AI telepítést igényelnek felhőkezelési képességekkel. Ide tartozik az intelligens dokumentumfeldolgozás, valós idejű elemzés és hibrid AI munkafolyamatok, amelyek a felhő és az edge számítástechnikai erőforrásokat egyaránt kihasználják.

**További információ**: [Azure EdgeAI SLM Motor](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI a Windows ML segítségével](./windowdeveloper.md)

A Windows ML a Microsoft legmodernebb futtatókörnyezete, amely optimalizált eszközön történő modellinferenciát és egyszerűsített telepítést kínál, a Windows AI Foundry alapjaként szolgálva. Ez a platform lehetővé teszi a fejlesztők számára, hogy AI-alapú Windows alkalmazásokat hozzanak létre, amelyek kihasználják a PC hardver teljes spektrumát.

### Platform képességek
- Minden Windows 11 PC-n működik, amely a 24H2 verziót (build 26100) vagy annál újabbat futtat
- Minden x64 és ARM64 PC hardveren működik, még olyan PC-ken is, amelyek nem rendelkeznek NPU-val vagy GPU-val
- Lehetővé teszi a fejlesztők számára, hogy saját modelleiket hozzák és hatékonyan telepítsék az AMD, Intel, NVIDIA és Qualcomm szilícium partnerökoszisztémájában, beleértve a CPU-t, GPU-t, NPU-t
- Az infrastruktúra API-k kihasználásával a fejlesztőknek már nem kell többféle buildet készíteniük alkalmazásukhoz, hogy különböző szilíciumot célozzanak meg

### Fejlesztői előnyök
A Windows ML absztrahálja a hardvert és a végrehajtási szolgáltatókat, így Ön a kódírásra koncentrálhat. Ráadásul a Windows ML automatikusan frissül, hogy támogassa a legújabb NPU-kat, GPU-kat és CPU-kat, amint azok megjelennek. A platform egységes keretrendszert biztosít az AI fejlesztéshez a Windows hardverökoszisztéma sokszínűségén belül.

**További információ**: 
- [Windows ML áttekintés](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI fejlesztési útmutató](./windowdeveloper.md) - Átfogó útmutató a Windows Edge AI fejlesztéséhez

## [5. EdgeAI Foundry Local alkalmazásokkal](./foundrylocal.md)

A Foundry Local lehetővé teszi Windows és Mac fejlesztők számára, hogy Retrieval Augmented Generation (RAG) alkalmazásokat építsenek helyi erőforrások felhasználásával .NET-ben, kombinálva a helyi nyelvi modelleket szemantikus keresési képességekkel. Ez a megközelítés adatvédelemre összpontosító AI megoldásokat kínál, amelyek teljes mértékben helyi infrastruktúrán működnek.

### Technikai architektúra
- Kombinálja a Phi nyelvi modellt, helyi beágyazásokat és a Semantic Kernel-t egy RAG forgatókönyv létrehozásához
- Beágyazásokat használ vektorokként (lebegőpontos értékek tömbjei), amelyek tartalmat és annak szemantikai jelentését képviselik
- A Semantic Kernel a fő koordinátor szerepét tölti be, integrálva a Phi-t és az intelligens komponenseket egy zökkenőmentes RAG csővezeték létrehozásához
- Támogatja a helyi vektoradatbázisokat, beleértve az SQLite-t és Qdrant-t

### Megvalósítási előnyök
A RAG, vagy Retrieval Augmented Generation, egyszerűen azt jelenti, hogy "keressünk meg néhány dolgot, és tegyük bele a promptba". Ez a helyi megvalósítás biztosítja az adatvédelmet, miközben intelligens válaszokat nyújt, amelyek egyedi tudásbázisokon alapulnak. Ez a megközelítés különösen értékes olyan vállalati helyzetekben, amelyek adatfüggetlenséget és offline működési képességeket igényelnek.

**További információ**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG minták](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

A Microsoft Foundry Local egy OpenAI-kompatibilis REST szervert biztosít, amelyet az ONNX Runtime hajt, lehetővé téve modellek helyi futtatását Windows rendszeren. Az alábbiakban egy gyors, validált összefoglaló található; a teljes részletekért lásd a hivatalos dokumentációt.

- Első lépések: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architektúra: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI referencia: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Teljes Windows útmutató ebben a repóban: [foundrylocal.md](./foundrylocal.md)

Telepítés vagy frissítés Windows rendszeren (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

CLI kategóriák felfedezése:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Modell futtatása és dinamikus végpont felfedezése:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Gyors REST ellenőrzés a modellek listázásához (cserélje ki a PORT-ot az állapotból):
```cmd
curl -s http://localhost:PORT/v1/models
```

Tippek:
- SDK integráció: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Saját modell hozása (fordítás): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI fejlesztési források

A kifejezetten Windows platformot célzó fejlesztők számára átfogó útmutatót készítettünk, amely a teljes Windows EdgeAI ökoszisztémát lefedi. Ez az erőforrás részletes információkat nyújt a Windows AI Foundry-ról, beleértve az API-kat, eszközöket és legjobb gyakorlatokat a Windows EdgeAI fejlesztéséhez.

### Windows AI Foundry platform
A Windows AI Foundry platform átfogó eszköz- és API-készletet biztosít, amelyet kifejezetten Edge AI fejlesztésre terveztek Windows eszközökön. Ez magában foglalja az NPU-gyorsított hardverek speciális támogatását, a Windows ML integrációt és a platformspecifikus optimalizációs technikákat.

**Átfogó útmutató**: [Windows EdgeAI fejlesztési útmutató](../windowdeveloper.md)

Ez az útmutató lefedi:
- A Windows AI Foundry platform áttekintése és komponensei
- Phi Silica API hatékony inferenciához NPU hardveren
- Számítógépes látás API-k képfeldolgozáshoz és OCR-hez
- Windows ML futtatókörnyezet integrációja és optimalizálása
- Foundry Local CLI helyi fejlesztéshez és teszteléshez
- Hardveroptimalizálási stratégiák Windows eszközökhöz
- Gyakorlati megvalósítási példák és legjobb gyakorlatok

### [AI Toolkit Edge AI fejlesztéshez](./aitoolkit.md)
A Visual Studio Code-ot használó fejlesztők számára az AI Toolkit kiterjesztés átfogó fejlesztési környezetet biztosít, amelyet kifejezetten Edge AI alkalmazások építésére, tesztelésére és telepítésére terveztek. Ez az eszközkészlet leegyszerűsíti az Edge AI fejlesztési munkafolyamatot a VS Code-on belül.

**Fejlesztési útmutató**: [AI Toolkit Edge AI fejlesztéshez](./aitoolkit.md)

Az AI Toolkit útmutató lefedi:
- Modell felfedezése és kiválasztása edge telepítéshez
- Helyi tesztelési és optimalizálási munkafolyamatok
- ONNX és Ollama integráció edge modellekhez
- Modellkonverziós és kvantálási technikák
- Ügynökfejlesztés edge forgatókönyvekhez
- Teljesítményértékelés és monitorozás
- Telepítési előkészületek és legjobb gyakorlatok

## Összegzés

Ez az öt EdgeAI megvalósítás bemutatja az edge AI megoldások érettségét és sokszínűségét, amelyek ma elérhetők. A Jetson Orin Nano hardvergyorsított edge eszközöktől kezdve az ONNX Runtime GenAI keresztplatformos mobilfejlesztési keretrendszerén és a Windows ML Windows-natív alkalmazásain át a Foundry Local adatvédelemre összpontosító RAG megvalósításáig, a fejlesztőknek példátlan lehetőségeik vannak intelligens alkalmazások telepítésére az edge környezetben.

A közös szál ezekben a platformokban az AI képességek demokratizálása, amely lehetővé teszi a fejlett gépi tanulás elérését különböző szintű készségekkel és felhasználási esetekkel rendelkező fejlesztők számára. Legyen szó mobilalkalmazások, asztali szoftverek vagy beágyazott rendszerek építéséről, ezek az EdgeAI megoldások alapot nyújtanak a következő generációs intelligens alkalmazásokhoz, amelyek hatékonyan és privát módon működnek az edge környezetben.

Minden platform egyedi előnyöket kínál: Jetson Orin Nano a hardvergyorsított edge számítástechnikához, ONNX Runtime GenAI a keresztplatformos mobilfejlesztéshez, Azure EdgeAI a vállalati felhő-edge integrációhoz, Windows ML a Windows-natív alkalmazásokhoz, és Foundry Local az adatvédelemre összpontosító RAG megvalósításokhoz. Együtt átfogó ökoszisztémát képviselnek az EdgeAI fejlesztéshez.

---

