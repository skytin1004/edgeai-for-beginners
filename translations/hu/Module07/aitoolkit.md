<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-18T17:36:25+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "hu"
}
-->
# AI Toolkit for Visual Studio Code - Edge AI Fejlesztési Útmutató

## Bevezetés

Üdvözlünk az AI Toolkit for Visual Studio Code átfogó útmutatójában, amely az Edge AI fejlesztéshez készült. Ahogy a mesterséges intelligencia a központosított felhőalapú számítástechnikáról a decentralizált edge eszközökre helyeződik át, a fejlesztőknek olyan erőteljes, integrált eszközökre van szükségük, amelyek képesek kezelni az edge telepítés egyedi kihívásait - például az erőforrás-korlátokat és az offline működési követelményeket.

Az AI Toolkit for Visual Studio Code áthidalja ezt a szakadékot azáltal, hogy egy teljes fejlesztési környezetet biztosít, amelyet kifejezetten az edge eszközökön hatékonyan futó AI alkalmazások építésére, tesztelésére és optimalizálására terveztek. Legyen szó IoT szenzorokról, mobil eszközökről, beágyazott rendszerekről vagy edge szerverekről, ez az eszköztár leegyszerűsíti a teljes fejlesztési munkafolyamatot a jól ismert VS Code környezetben.

Ez az útmutató bemutatja az alapvető fogalmakat, eszközöket és legjobb gyakorlatokat, amelyek segítségével az AI Toolkit-et hatékonyan használhatod Edge AI projektjeidben, a kezdeti modell kiválasztástól egészen a termelési telepítésig.

## Áttekintés

Az AI Toolkit egy integrált fejlesztési környezetet kínál az Edge AI alkalmazások teljes életciklusához a VS Code-on belül. Zökkenőmentesen integrálódik népszerű AI modellekkel olyan szolgáltatóktól, mint az OpenAI, Anthropic, Google és GitHub, miközben támogatja a helyi modell telepítést az ONNX és Ollama segítségével - kulcsfontosságú képességek az edge AI alkalmazások számára, amelyek eszközön történő inferenciát igényelnek.

Ami az AI Toolkit-et kiemeli az Edge AI fejlesztés terén, az az edge telepítési folyamat teljes körű támogatása. A hagyományos AI fejlesztési eszközökkel ellentétben, amelyek elsősorban a felhőalapú telepítést célozzák meg, az AI Toolkit speciális funkciókat kínál a modell optimalizálásához, erőforrás-korlátos teszteléshez és edge-specifikus teljesítményértékeléshez. Az eszköztár megérti, hogy az edge AI fejlesztés különböző szempontokat igényel - kisebb modellméretek, gyorsabb inferenciaidők, offline képességek és hardver-specifikus optimalizálások.

A platform többféle telepítési forgatókönyvet támogat, az egyszerű eszközön történő inferenciától a komplex, többmodellű edge architektúrákig. Eszközöket biztosít a modell konvertálásához, kvantálásához és optimalizálásához, amelyek elengedhetetlenek a sikeres edge telepítéshez, miközben megőrzi a VS Code által nyújtott fejlesztői produktivitást.

## Tanulási célok

Az útmutató végére képes leszel:

### Alapvető kompetenciák
- **Telepíteni és konfigurálni** az AI Toolkit-et a Visual Studio Code-ban az Edge AI fejlesztési munkafolyamatokhoz
- **Navigálni és használni** az AI Toolkit felületét, beleértve a Model Catalog, Playground és Agent Builder funkciókat
- **Kiválasztani és értékelni** az edge telepítésre alkalmas AI modelleket teljesítmény és erőforrás-korlátok alapján
- **Konvertálni és optimalizálni** modelleket ONNX formátum és kvantálási technikák segítségével edge eszközökhöz

### Edge AI fejlesztési készségek
- **Edge AI alkalmazásokat tervezni és megvalósítani** az integrált fejlesztési környezetben
- **Modelleket tesztelni** edge-szerű körülmények között helyi inferencia és erőforrás-figyelés segítségével
- **AI ügynököket létrehozni és testre szabni**, amelyek optimalizáltak az edge telepítési forgatókönyvekhez
- **Modellek teljesítményét értékelni** az edge számítástechnikához releváns metrikák alapján (késleltetés, memóriahasználat, pontosság)

### Optimalizálás és telepítés
- **Kvantálási és metszési technikákat alkalmazni**, hogy csökkentsd a modell méretét, miközben elfogadható teljesítményt tartasz fenn
- **Modelleket optimalizálni** specifikus edge hardver platformokra, beleértve a CPU, GPU és NPU gyorsítást
- **Legjobb gyakorlatokat megvalósítani** az edge AI fejlesztéshez, beleértve az erőforrás-kezelést és a visszaesési stratégiákat
- **Modelleket és alkalmazásokat előkészíteni** edge eszközökön történő termelési telepítéshez

### Haladó Edge AI fogalmak
- **Integrálni edge AI keretrendszerekkel**, mint az ONNX Runtime, Windows ML és TensorFlow Lite
- **Többmodellű architektúrákat és federált tanulási forgatókönyveket megvalósítani** edge környezetekben
- **Gyakori edge AI problémákat elhárítani**, mint például memória-korlátok, inferencia sebesség és hardver-kompatibilitás
- **Figyelési és naplózási stratégiákat tervezni** edge AI alkalmazásokhoz termelési környezetben

### Gyakorlati alkalmazás
- **Teljes körű Edge AI megoldásokat építeni** a modell kiválasztástól a telepítésig
- **Profi szinten bemutatni** edge-specifikus fejlesztési munkafolyamatokat és optimalizálási technikákat
- **A tanult fogalmakat alkalmazni** valós edge AI felhasználási esetekben, beleértve az IoT, mobil és beágyazott alkalmazásokat
- **Különböző edge AI telepítési stratégiákat értékelni és összehasonlítani**, valamint azok kompromisszumait

## Kulcsfunkciók az Edge AI fejlesztéshez

### 1. Modellkatalógus és felfedezés
- **Helyi modell támogatás**: AI modellek felfedezése és elérése, amelyek kifejezetten edge telepítésre optimalizáltak
- **ONNX integráció**: ONNX formátumú modellek elérése hatékony edge inferenciához
- **Ollama támogatás**: Helyben futó modellek használata Ollama segítségével a magánélet és offline működés érdekében
- **Modell összehasonlítás**: Modellek összehasonlítása, hogy megtaláld az optimális egyensúlyt a teljesítmény és az erőforrás-fogyasztás között edge eszközökön

### 2. Interaktív Playground
- **Helyi tesztkörnyezet**: Modellek tesztelése helyben, mielőtt edge telepítésre kerülnek
- **Multimodális kísérletezés**: Tesztelés képekkel, szövegekkel és más edge forgatókönyvekben tipikus bemenetekkel
- **Paraméterhangolás**: Különböző modellparaméterekkel való kísérletezés az edge korlátok optimalizálása érdekében
- **Valós idejű teljesítményfigyelés**: Inferencia sebesség és erőforrás-használat megfigyelése a fejlesztés során

### 3. Ügynöképítő edge alkalmazásokhoz
- **Prompt Engineering**: Optimalizált promptok létrehozása, amelyek hatékonyan működnek kisebb edge modellekkel
- **MCP eszköz integráció**: Model Context Protocol eszközök integrálása a fejlettebb edge ügynök képességek érdekében
- **Kódgenerálás**: Termelésre kész kód generálása, amely optimalizált az edge telepítési forgatókönyvekhez
- **Strukturált kimenetek**: Ügynökök tervezése, amelyek következetes, strukturált válaszokat nyújtanak edge alkalmazásokhoz

### 4. Modellértékelés és tesztelés
- **Teljesítménymetrikák**: Modellek értékelése edge telepítéshez releváns metrikák alapján (késleltetés, memóriahasználat, pontosság)
- **Batch tesztelés**: Több modellkonfiguráció egyidejű tesztelése az optimális edge beállítások megtalálásához
- **Egyedi értékelés**: Egyedi értékelési kritériumok létrehozása edge AI felhasználási esetekhez
- **Erőforrás-profilozás**: Memória- és számítási igények elemzése edge telepítési tervezéshez

### 5. Modellkonvertálás és optimalizálás
- **ONNX konvertálás**: Modellek konvertálása különböző formátumokból ONNX-ba edge kompatibilitás érdekében
- **Kvantálás**: Modellméret csökkentése és inferencia sebesség javítása kvantálási technikák segítségével
- **Hardveroptimalizálás**: Modellek optimalizálása specifikus edge hardverekhez (CPU, GPU, NPU)
- **Formátum átalakítás**: Modellek átalakítása Hugging Face és más forrásokból edge telepítéshez

### 6. Finomhangolás edge forgatókönyvekhez
- **Domain Adaptation**: Modellek testreszabása specifikus edge felhasználási esetekhez és környezetekhez
- **Helyi tanítás**: Modellek helyi tanítása GPU támogatással edge-specifikus követelményekhez
- **Azure integráció**: Azure Container Apps használata felhőalapú finomhangoláshoz edge telepítés előtt
- **Transfer Learning**: Előre tanított modellek adaptálása edge-specifikus feladatokhoz és korlátokhoz

### 7. Teljesítményfigyelés és nyomkövetés
- **Edge teljesítményelemzés**: Modellek teljesítményének figyelése edge-szerű körülmények között
- **Nyomgyűjtés**: Részletes teljesítményadatok gyűjtése optimalizáláshoz
- **Szűk keresztmetszetek azonosítása**: Teljesítményproblémák azonosítása edge eszközökön történő telepítés előtt
- **Erőforrás-használat követése**: Memória, CPU és inferenciaidő figyelése edge optimalizáláshoz

## Edge AI fejlesztési munkafolyamat

### 1. fázis: Modell felfedezése és kiválasztása
1. **Modellek felfedezése**: Használd a modellkatalógust edge telepítésre alkalmas modellek megtalálásához
2. **Teljesítmény összehasonlítása**: Modellek értékelése méret, pontosság és inferencia sebesség alapján
3. **Helyi tesztelés**: Ollama vagy ONNX modellek használata helyi teszteléshez edge telepítés előtt
4. **Erőforrásigények felmérése**: Memória- és számítási igények meghatározása a cél edge eszközökhöz

### 2. fázis: Modell optimalizálása
1. **ONNX konvertálás**: A kiválasztott modellek konvertálása ONNX formátumba edge kompatibilitás érdekében
2. **Kvantálás alkalmazása**: Modellméret csökkentése INT8 vagy INT4 kvantálással
3. **Hardveroptimalizálás**: Optimalizálás cél edge hardverekhez (ARM, x86, speciális gyorsítók)
4. **Teljesítmény validálása**: Az optimalizált modellek pontosságának fenntartása

### 3. fázis: Alkalmazásfejlesztés
1. **Ügynök tervezése**: Használd az Agent Builder-t edge-optimalizált AI ügynökök létrehozásához
2. **Prompt Engineering**: Hatékony promptok fejlesztése kisebb edge modellekhez
3. **Integrációs tesztelés**: Ügynökök tesztelése szimulált edge körülmények között
4. **Kódgenerálás**: Termelésre kész kód generálása edge telepítéshez

### 4. fázis: Értékelés és tesztelés
1. **Batch értékelés**: Több konfiguráció tesztelése az optimális edge beállítások megtalálásához
2. **Teljesítményprofilozás**: Inferencia sebesség, memóriahasználat és pontosság elemzése
3. **Edge szimuláció**: Tesztelés a cél edge telepítési környezethez hasonló körülmények között
4. **Stressztesztelés**: Teljesítmény értékelése különböző terhelési körülmények között

### 5. fázis: Telepítési előkészítés
1. **Végső optimalizálás**: Végső optimalizálások alkalmazása a tesztelési eredmények alapján
2. **Telepítési csomagolás**: Modellek és kód csomagolása edge telepítéshez
3. **Dokumentáció**: Telepítési követelmények és konfiguráció dokumentálása
4. **Figyelési beállítás**: Figyelési és naplózási előkészítés edge telepítéshez

## Célközönség az Edge AI fejlesztéshez

### Edge AI fejlesztők
- Alkalmazásfejlesztők, akik AI-alapú edge eszközöket és IoT megoldásokat építenek
- Beágyazott rendszerek fejlesztői, akik AI képességeket integrálnak erőforrás-korlátos eszközökbe
- Mobilfejlesztők, akik eszközön futó AI alkalmazásokat készítenek okostelefonokra és tabletekre

### Edge AI mérnökök
- AI mérnökök, akik modelleket optimalizálnak edge telepítéshez és inferencia csatornákat kezelnek
- DevOps mérnökök, akik AI modelleket telepítenek és kezelnek elosztott edge infrastruktúrában
- Teljesítménymérnökök, akik AI munkaterheléseket optimalizálnak edge hardver korlátokhoz

### Kutatók és oktatók
- AI kutatók, akik hatékony modelleket és algoritmusokat fejlesztenek edge számítástechnikához
- Oktatók, akik edge AI fogalmakat tanítanak és optimalizálási technikákat mutatnak be
- Diákok, akik az edge AI telepítés kihívásait és megoldásait tanulják

## Edge AI felhasználási esetek

### Okos IoT eszközök
- **Valós idejű képfelismerés**: Számítógépes látás modellek telepítése IoT kamerákon és szenzorokon
- **Hangfeldolgozás**: Beszédfelismerés és természetes nyelvi feldolgozás megvalósítása okos hangszórókon
- **Prediktív karbantartás**: Anomália detektáló modellek futtatása ipari edge eszközökön
- **Környezeti monitorozás**: Szenzoradat-elemző modellek telepítése környezeti alkalmazásokhoz

### Mobil és beágyazott alkalmazások
- **Eszközön történő fordítás**: Nyelvfordító modellek megvalósítása, amelyek offline működnek
- **Kiterjesztett valóság**: Valós idejű objektumfelismerés és követés telepítése AR alkalmazásokhoz
- **Egészségügyi monitorozás**: Egészségügyi elemző modellek futtatása viselhető eszközökön és orvosi berendezéseken
- **Autonóm rendszerek**: Döntéshozó modellek megvalósítása drónok, robotok és járművek számára

### Edge számítástechnikai infrastruktúra
- **Edge adatközpontok**: AI modellek telepítése edge adatközpontokban alacsony késleltetésű alkalmazásokhoz
- **CDN integráció**: AI feldolgozási kép
- **Biztonság**: Alkalmazzon megfelelő biztonsági intézkedéseket az Edge AI alkalmazásokhoz

## Integráció Edge AI keretrendszerekkel

### ONNX Runtime
- **Platformfüggetlen telepítés**: ONNX modellek telepítése különböző edge platformokon
- **Hardveroptimalizálás**: Használja ki az ONNX Runtime hardver-specifikus optimalizációit
- **Mobil támogatás**: ONNX Runtime Mobile használata okostelefonokhoz és táblagépekhez
- **IoT integráció**: ONNX Runtime könnyű disztribúcióival telepítés IoT eszközökre

### Windows ML
- **Windows eszközök**: Optimalizálás Windows-alapú edge eszközökre és PC-kre
- **NPU gyorsítás**: Használja ki a Windows eszközökön található Neural Processing Unitokat
- **DirectML**: GPU gyorsítás DirectML segítségével Windows platformokon
- **UWP integráció**: Integráció Universal Windows Platform alkalmazásokkal

### TensorFlow Lite
- **Mobil optimalizálás**: TensorFlow Lite modellek telepítése mobil és beágyazott eszközökre
- **Hardver delegáltak**: Speciális hardver delegáltak használata a gyorsítás érdekében
- **Mikrokontrollerek**: Telepítés mikrokontrollerekre TensorFlow Lite Micro segítségével
- **Platformfüggetlen támogatás**: Telepítés Android, iOS és beágyazott Linux rendszereken

### Azure IoT Edge
- **Felhő-edge hibrid**: Felhőben történő tanítás kombinálása edge eszközökön történő következtetéssel
- **Modul telepítés**: AI modellek telepítése IoT Edge modulokként
- **Eszközkezelés**: Edge eszközök és modellfrissítések távoli kezelése
- **Telemetria**: Teljesítményadatok és modellmetrikák gyűjtése edge telepítésekből

## Fejlett Edge AI forgatókönyvek

### Több modell telepítése
- **Modellcsoportok**: Több modell telepítése a pontosság vagy redundancia javítása érdekében
- **A/B tesztelés**: Különböző modellek egyidejű tesztelése edge eszközökön
- **Dinamikus kiválasztás**: Modellek kiválasztása az aktuális eszközállapot alapján
- **Erőforrás-megosztás**: Erőforrások optimalizálása több telepített modell között

### Federált tanulás
- **Elosztott tanítás**: Modellek tanítása több edge eszközön
- **Adatvédelem**: A tanítási adatok helyben tartása, miközben megosztják a modellfejlesztéseket
- **Közös tanulás**: Eszközök képessé tétele arra, hogy kollektív tapasztalatokból tanuljanak
- **Edge-felhő koordináció**: Tanulás koordinálása edge eszközök és felhő infrastruktúra között

### Valós idejű feldolgozás
- **Folyamatos adatfeldolgozás**: Folyamatos adatfolyamok feldolgozása edge eszközökön
- **Alacsony késleltetésű következtetés**: Optimalizálás minimális következtetési késleltetésre
- **Csoportos feldolgozás**: Adatcsoportok hatékony feldolgozása edge eszközökön
- **Adaptív feldolgozás**: Feldolgozás igazítása az aktuális eszközkapacitásokhoz

## Edge AI fejlesztés hibakeresése

### Gyakori problémák
- **Memória korlátok**: Modell túl nagy a cél eszköz memóriájához
- **Következtetési sebesség**: Modell következtetése túl lassú a valós idejű követelményekhez
- **Pontosság romlása**: Optimalizálás elfogadhatatlanul csökkenti a modell pontosságát
- **Hardver kompatibilitás**: Modell nem kompatibilis a cél hardverrel

### Hibakeresési stratégiák
- **Teljesítményprofilozás**: AI Toolkit nyomkövetési funkcióinak használata a szűk keresztmetszetek azonosítására
- **Erőforrás-figyelés**: Memória- és CPU-használat figyelése a fejlesztés során
- **Lépésenkénti tesztelés**: Optimalizálások lépésenkénti tesztelése a problémák elkülönítésére
- **Hardver szimuláció**: Fejlesztői eszközök használata a cél hardver szimulálására

### Optimalizálási megoldások
- **További kvantálás**: Aggresszívebb kvantálási technikák alkalmazása
- **Modellarchitektúra**: Különböző, edge-re optimalizált modellarchitektúrák megfontolása
- **Előfeldolgozás optimalizálása**: Adatelőfeldolgozás optimalizálása edge korlátokhoz
- **Következtetés optimalizálása**: Hardver-specifikus következtetési optimalizációk használata

## Források és következő lépések

### Dokumentáció
- [AI Toolkit Models Guide](https://code.visualstudio.com/docs/intelligentapps/models)
- [Model Playground Documentation](https://code.visualstudio.com/docs/intelligentapps/playground)
- [ONNX Runtime Documentation](https://onnxruntime.ai/)
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)

### Közösség és támogatás
- [VS Code AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [ONNX Community](https://github.com/onnx/onnx)
- [Edge AI Developer Community](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Tanulási források
- [Edge AI Fundamentals Course](./Module01/README.md)
- [Small Language Models Guide](./Module02/README.md)
- [Edge Deployment Strategies](./Module03/README.md)
- [Windows Edge AI Development](./windowdeveloper.md)

## Összegzés

Az AI Toolkit for Visual Studio Code átfogó platformot kínál az Edge AI fejlesztéshez, a modellek felfedezésétől és optimalizálásától kezdve a telepítésig és monitorozásig. Az integrált eszközök és munkafolyamatok révén a fejlesztők hatékonyan hozhatnak létre, tesztelhetnek és telepíthetnek AI alkalmazásokat, amelyek hatékonyan működnek erőforrás-korlátozott edge eszközökön.

A toolkit támogatása az ONNX, Ollama és különböző felhőszolgáltatók számára, valamint az optimalizálási és értékelési képességei ideális választássá teszik az Edge AI fejlesztéshez. Legyen szó IoT alkalmazásokról, mobil AI funkciókról vagy beágyazott intelligens rendszerekről, az AI Toolkit biztosítja azokat az eszközöket és munkafolyamatokat, amelyek szükségesek a sikeres Edge AI telepítéshez.

Ahogy az Edge AI tovább fejlődik, az AI Toolkit for VS Code az élvonalban marad, és a fejlesztők számára korszerű eszközöket és képességeket kínál a következő generációs intelligens edge alkalmazások létrehozásához.

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.