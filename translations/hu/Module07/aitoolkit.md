<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T14:01:32+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "hu"
}
-->
# AI Toolkit for Visual Studio Code - Útmutató az Edge AI fejlesztéséhez

## Bevezetés

Üdvözlünk az AI Toolkit for Visual Studio Code átfogó útmutatójában, amely az Edge AI fejlesztéséhez készült. Ahogy a mesterséges intelligencia a központosított felhőalapú számítástechnikáról a decentralizált él-eszközökre helyeződik át, a fejlesztőknek olyan erőteljes, integrált eszközökre van szükségük, amelyek képesek kezelni az él-alapú telepítés egyedi kihívásait - a korlátozott erőforrásoktól az offline működési követelményekig.

Az AI Toolkit for Visual Studio Code áthidalja ezt a szakadékot azáltal, hogy egy teljes fejlesztési környezetet biztosít, amely kifejezetten az él-eszközökön hatékonyan futó AI alkalmazások építésére, tesztelésére és optimalizálására készült. Legyen szó IoT érzékelőkről, mobil eszközökről, beágyazott rendszerekről vagy él-szerverekről, ez az eszköztár leegyszerűsíti a teljes fejlesztési munkafolyamatot a megszokott VS Code környezetben.

Ez az útmutató végigvezet az alapvető fogalmakon, eszközökön és legjobb gyakorlatokon, amelyek segítségével az AI Toolkit-et hatékonyan használhatod Edge AI projektjeidben, a kezdeti modellválasztástól a termelési telepítésig.

## Áttekintés

Az AI Toolkit for Visual Studio Code egy erőteljes kiterjesztés, amely leegyszerűsíti az ügynökfejlesztést és az AI alkalmazások létrehozását. Az eszköztár átfogó képességeket kínál AI modellek felfedezésére, értékelésére és telepítésére számos szolgáltatótól - például Anthropic, OpenAI, GitHub, Google - miközben támogatja a helyi modellfuttatást ONNX és Ollama segítségével.

Ami megkülönbözteti az AI Toolkit-et, az a mesterséges intelligencia fejlesztési életciklusának átfogó megközelítése. A hagyományos AI fejlesztési eszközökkel ellentétben, amelyek egyetlen aspektusra összpontosítanak, az AI Toolkit egy integrált környezetet biztosít, amely lefedi a modell felfedezését, kísérletezését, ügynökfejlesztést, értékelést és telepítést - mindezt a megszokott VS Code környezetben.

A platformot kifejezetten gyors prototípus-készítésre és termelési telepítésre tervezték, olyan funkciókkal, mint a prompt generálás, gyors kezdők, zökkenőmentes MCP (Model Context Protocol) eszközintegrációk és kiterjedt értékelési képességek. Az Edge AI fejlesztéshez ez azt jelenti, hogy hatékonyan fejlesztheted, tesztelheted és optimalizálhatod az AI alkalmazásokat él-alapú telepítési forgatókönyvekhez, miközben a teljes fejlesztési munkafolyamatot a VS Code-ban tartod.

## Tanulási célok

Az útmutató végére képes leszel:

### Alapvető kompetenciák
- **Telepíteni és konfigurálni** az AI Toolkit-et a Visual Studio Code-ban az Edge AI fejlesztési munkafolyamatokhoz
- **Navigálni és használni** az AI Toolkit felületét, beleértve a Model Catalog, Playground és Agent Builder funkciókat
- **Kiválasztani és értékelni** az él-alapú telepítésre alkalmas AI modelleket teljesítmény és erőforrás-korlátok alapján
- **Átalakítani és optimalizálni** modelleket ONNX formátum és kvantálási technikák segítségével él-eszközökhöz

### Edge AI fejlesztési készségek
- **Edge AI alkalmazásokat tervezni és megvalósítani** az integrált fejlesztési környezetben
- **Modelleket tesztelni** él-szerű körülmények között helyi inferencia és erőforrás-figyelés segítségével
- **AI ügynököket létrehozni és testreszabni**, amelyek optimalizáltak él-alapú telepítési forgatókönyvekhez
- **Modellek teljesítményét értékelni** az él-számításhoz releváns metrikák alapján (késleltetés, memóriahasználat, pontosság)

### Optimalizálás és telepítés
- **Kvantálási és metszési technikákat alkalmazni**, hogy csökkentsd a modell méretét, miközben elfogadható teljesítményt tartasz fenn
- **Modelleket optimalizálni** specifikus él-hardver platformokhoz, beleértve a CPU, GPU és NPU gyorsítást
- **Legjobb gyakorlatokat megvalósítani** az Edge AI fejlesztéshez, beleértve az erőforrás-kezelést és a visszaesési stratégiákat
- **Modelleket és alkalmazásokat előkészíteni** termelési telepítésre él-eszközökön

### Haladó Edge AI fogalmak
- **Integrálni él AI keretrendszerekkel**, például ONNX Runtime, Windows ML és TensorFlow Lite
- **Többmodell-architektúrákat és federált tanulási forgatókönyveket megvalósítani** él-környezetekhez
- **Gyakori Edge AI problémákat elhárítani**, beleértve a memória-korlátokat, inferencia sebességet és hardver-kompatibilitást
- **Felügyeleti és naplózási stratégiákat tervezni** Edge AI alkalmazásokhoz termelési környezetben

### Gyakorlati alkalmazás
- **Teljes körű Edge AI megoldásokat építeni** a modellválasztástól a telepítésig
- **Bizonyítani a jártasságot** él-specifikus fejlesztési munkafolyamatokban és optimalizálási technikákban
- **Alkalmazni a tanult fogalmakat** valós Edge AI felhasználási esetekben, beleértve az IoT-t, mobil és beágyazott alkalmazásokat
- **Értékelni és összehasonlítani** különböző él-alapú telepítési stratégiákat és azok kompromisszumait

## Kulcsfunkciók az Edge AI fejlesztéshez

### 1. Modellkatalógus és felfedezés
- **Több szolgáltató támogatása**: Böngészés és hozzáférés AI modellekhez Anthropic, OpenAI, GitHub, Google és más szolgáltatóktól
- **Helyi modell integráció**: ONNX és Ollama modellek egyszerűsített felfedezése él-alapú telepítéshez
- **GitHub modellek**: Közvetlen integráció a GitHub modell-tárolásával a zökkenőmentes hozzáférés érdekében
- **Modell összehasonlítás**: Modellek összehasonlítása egymás mellett az él-eszközök korlátainak optimális egyensúlyának megtalálásához

### 2. Interaktív Playground
- **Interaktív tesztkörnyezet**: Gyors kísérletezés a modellek képességeivel ellenőrzött környezetben
- **Többmódú támogatás**: Tesztelés képekkel, szövegekkel és más bemenetekkel, amelyek tipikusak él-forgatókönyvekben
- **Valós idejű kísérletezés**: Azonnali visszajelzés a modellek válaszairól és teljesítményéről
- **Paraméter optimalizálás**: Modellparaméterek finomhangolása él-alapú telepítési követelményekhez

### 3. Prompt (Agent) Builder
- **Természetes nyelvi generálás**: Kezdő promptok generálása természetes nyelvi leírások alapján
- **Iteratív finomítás**: Promptok javítása a modellek válaszai és teljesítménye alapján
- **Feladatbontás**: Összetett feladatok lebontása promptláncolással és strukturált kimenetekkel
- **Változók támogatása**: Változók használata promptokban a dinamikus ügynökviselkedéshez
- **Termelési kód generálása**: Termelésre kész kód generálása gyors alkalmazásfejlesztéshez

### 4. Tömeges futtatás és értékelés
- **Többmodell tesztelés**: Több prompt futtatása kiválasztott modelleken egyidejűleg
- **Hatékony tesztelés nagy léptékben**: Különböző bemenetek és konfigurációk hatékony tesztelése
- **Egyedi tesztesetek**: Ügynökök futtatása tesztesetekkel a funkcionalitás validálásához
- **Teljesítmény összehasonlítás**: Eredmények összehasonlítása különböző modellek és konfigurációk között

### 5. Modellértékelés adathalmazokkal
- **Standard metrikák**: AI modellek tesztelése beépített értékelőkkel (F1 pontszám, relevancia, hasonlóság, koherencia)
- **Egyedi értékelők**: Saját értékelési metrikák létrehozása specifikus felhasználási esetekhez
- **Adathalmaz integráció**: Modellek tesztelése átfogó adathalmazokkal
- **Teljesítménymérés**: Modell teljesítményének számszerűsítése él-alapú telepítési döntésekhez

### 6. Finomhangolási képességek
- **Modell testreszabás**: Modellek testreszabása specifikus felhasználási esetekhez és területekhez
- **Speciális adaptáció**: Modellek adaptálása speciális területekhez és követelményekhez
- **Él-optimalizálás**: Modellek finomhangolása kifejezetten él-alapú telepítési korlátokhoz
- **Terület-specifikus képzés**: Modellek létrehozása, amelyek kifejezetten él-alapú felhasználási esetekhez készültek

### 7. MCP eszközintegráció
- **Külső eszközkapcsolat**: Ügynökök csatlakoztatása külső eszközökhöz Model Context Protocol szervereken keresztül
- **Valós cselekvések**: Ügynökök engedélyezése adatbázisok lekérdezésére, API-k elérésére vagy egyedi logika végrehajtására
- **Meglévő MCP szerverek**: Eszközök használata parancs (stdio) vagy HTTP (server-sent event) protokollokon keresztül
- **Egyedi MCP fejlesztés**: Új MCP szerverek építése és vázlatkészítése teszteléssel az Agent Builderben

### 8. Ügynökfejlesztés és tesztelés
- **Funkcióhívás támogatása**: Ügynökök engedélyezése külső funkciók dinamikus meghívására
- **Valós idejű integrációs tesztelés**: Integrációk tesztelése valós idejű futtatásokkal és eszközhasználattal
- **Ügynök verziókezelés**: Verziókezelés ügynökökhöz összehasonlítási képességekkel az értékelési eredményekhez
- **Hibakeresés és nyomkövetés**: Helyi nyomkövetési és hibakeresési képességek az ügynökfejlesztéshez

## Edge AI fejlesztési munkafolyamat

### 1. fázis: Modell felfedezése és kiválasztása
1. **Modellkatalógus felfedezése**: Használd a modellkatalógust az él-alapú telepítésre alkalmas modellek megtalálásához
2. **Teljesítmény összehasonlítása**: Modellek értékelése méret, pontosság és inferencia sebesség alapján
3. **Helyi tesztelés**: Ollama vagy ONNX modellek használata helyi teszteléshez az él-alapú telepítés előtt
4. **Erőforrásigények felmérése**: Memória- és számítási igények meghatározása a célzott él-eszközökhöz

### 2. fázis: Modell optimalizálása
1. **Átalakítás ONNX formátumba**: A kiválasztott modellek átalakítása ONNX formátumba az él-kompatibilitás érdekében
2. **Kvantálás alkalmazása**: Modellméret csökkentése INT8 vagy INT4 kvantálással
3. **Hardver optimalizálás**: Optimalizálás a célzott él-hardverhez (ARM, x86, speciális gyorsítók)
4. **Teljesítmény validálása**: Az optimalizált modellek elfogadható pontosságának fenntartása

### 3. fázis: Alkalmazásfejlesztés
1. **Ügynök tervezése**: Az Agent Builder használata él-optimalizált AI ügynökök létrehozásához
2. **Prompt mérnökség**: Promptok fejlesztése, amelyek hatékonyan működnek kisebb él-modellekkel
3. **Integrációs tesztelés**: Ügynökök tesztelése szimulált él-körülmények között
4. **Kód generálása**: Termelésre optimalizált kód generálása él-alapú telepítéshez

### 4. fázis: Értékelés és tesztelés
1. **Tömeges értékelés**: Több konfiguráció tesztelése az optimális él-beállítások megtalálásához
2. **Teljesítmény profilozása**: Inferencia sebesség, memóriahasználat és pontosság elemzése
3. **Él-szimuláció**: Tesztelés a célzott él-alapú telepítési környezethez hasonló körülmények között
4. **Terhelési tesztelés**: Teljesítmény értékelése különböző terhelési körülmények között

### 5. fázis: Telepítés előkészítése
1. **Végső optimalizálás**: Végső optimalizálások alkalmazása a tesztelési eredmények alapján
2. **Telepítési csomagolás**: Modellek és kód csomagolása él-alapú telepítéshez
3. **Dokumentáció**: Telepítési követelmények és konfiguráció dokumentálása
4. **Felügyeleti beállítás**: Felügyelet és naplózás előkészítése él-alapú telepítéshez

## Célközönség az Edge AI fejlesztéshez

### Edge AI fejlesztők
- Alkalmazásfejlesztők, akik AI-alapú él-eszközöket és IoT megoldásokat építenek
- Beágyazott rendszerek fejlesztői, akik AI képességeket integrálnak erőforrás-korlátozott eszközökbe
- Mobilfejlesztők, akik AI alkalmazásokat készítenek okostelefonokra és táblagépekre

### Edge AI mérnökök
- AI mérnökök, akik modelleket optimalizálnak él-alapú telepítéshez és inferencia csatornákat kezelnek
- DevOps mérnökök, akik AI modelleket telepítenek és kezelnek elosztott él-infrastruktúrában
- Teljesítmény mérnökök, akik AI munkaterheléseket optimalizálnak él-hardver korlátokhoz

### Kutatók és oktatók
- AI kutatók, akik hatékony modelleket és algoritmusokat fejlesztenek él-számításhoz
- Oktatók, akik Edge AI fogalmakat tanítanak és optimalizálási technikákat demonstrálnak
- Diákok, akik az Edge AI telepítés kihívásait és megoldásait tanulják

## Edge AI felhasználási esetek

### Okos IoT eszközök
- **Valós idejű képfelismerés**: Számítógépes látás modellek telepítése IoT kamerákon és érzékelőkön
- **Hangfeldolgozás**: Beszédfelismerés és természetes nyelvi feldolgozás megvalósítása okos hangszórókon
2. Induló promptok létrehozása természetes nyelvi leírások alapján  
3. Promptok iterálása és finomítása a modell válaszai alapján  
4. MCP eszközök integrálása az ügynökök képességeinek növelésére  

#### 3. lépés: Tesztelés és értékelés  
1. Használja a **Bulk Run** funkciót több prompt tesztelésére a kiválasztott modellek között  
2. Futtassa az ügynököket tesztesetekkel a funkcionalitás validálásához  
3. Értékelje a pontosságot és teljesítményt beépített vagy egyedi metrikák segítségével  
4. Hasonlítsa össze különböző modelleket és konfigurációkat  

#### 4. lépés: Finomhangolás és optimalizálás  
1. Testreszabja a modelleket specifikus edge használati esetekhez  
2. Alkalmazzon domain-specifikus finomhangolást  
3. Optimalizálja az edge telepítési korlátokhoz  
4. Verziózza és hasonlítsa össze az ügynökök különböző konfigurációit  

#### 5. lépés: Telepítési előkészületek  
1. Generáljon gyártásra kész kódot az Agent Builder segítségével  
2. Állítsa be az MCP szerverkapcsolatokat gyártási használatra  
3. Készítse elő a telepítési csomagokat edge eszközökhöz  
4. Konfigurálja a monitorozási és értékelési metrikákat  

## Legjobb gyakorlatok az Edge AI fejlesztéshez  

### Modellválasztás  
- **Méretkorlátok**: Válasszon olyan modelleket, amelyek illeszkednek a cél eszközök memóriakorlátaihoz  
- **Következtetési sebesség**: Részesítse előnyben a gyors következtetési idővel rendelkező modelleket valós idejű alkalmazásokhoz  
- **Pontossági kompromisszumok**: Egyensúlyozza a modell pontosságát az erőforrás-korlátokkal  
- **Formátumkompatibilitás**: Részesítse előnyben az ONNX vagy hardver-optimalizált formátumokat edge telepítéshez  

### Optimalizálási technikák  
- **Kvantálás**: Használjon INT8 vagy INT4 kvantálást a modell méretének csökkentésére és sebesség növelésére  
- **Metszés**: Távolítsa el a felesleges modellparamétereket a számítási igény csökkentésére  
- **Tudásdesztilláció**: Hozzon létre kisebb modelleket, amelyek megtartják a nagyobb modellek teljesítményét  
- **Hardvergyorsítás**: Használjon NPU-kat, GPU-kat vagy speciális gyorsítókat, ha elérhetők  

### Fejlesztési munkafolyamat  
- **Iteratív tesztelés**: Teszteljen gyakran edge-szerű körülmények között a fejlesztés során  
- **Teljesítményfigyelés**: Folyamatosan figyelje az erőforrás-használatot és a következtetési sebességet  
- **Verziókezelés**: Kövesse nyomon a modellverziókat és optimalizálási beállításokat  
- **Dokumentáció**: Dokumentálja az összes optimalizálási döntést és teljesítmény-kompromisszumot  

### Telepítési szempontok  
- **Erőforrás-figyelés**: Figyelje a memória-, CPU- és energiahasználatot a gyártásban  
- **Visszaesési stratégiák**: Implementáljon visszaesési mechanizmusokat modellhibák esetére  
- **Frissítési mechanizmusok**: Tervezze meg a modellfrissítéseket és verziókezelést  
- **Biztonság**: Alkalmazzon megfelelő biztonsági intézkedéseket az edge AI alkalmazásokhoz  

## Integráció az Edge AI keretrendszerekkel  

### ONNX Runtime  
- **Platformközi telepítés**: Telepítse az ONNX modelleket különböző edge platformokon  
- **Hardver-optimalizáció**: Használja az ONNX Runtime hardver-specifikus optimalizációit  
- **Mobil támogatás**: Használja az ONNX Runtime Mobile-t okostelefonokhoz és tabletekhez  
- **IoT integráció**: Telepítse IoT eszközökre az ONNX Runtime könnyű disztribúcióival  

### Windows ML  
- **Windows eszközök**: Optimalizálja Windows-alapú edge eszközökhöz és PC-khez  
- **NPU gyorsítás**: Használja a Windows eszközök Neural Processing Unit-jait  
- **DirectML**: Használja a DirectML-t GPU gyorsításhoz Windows platformokon  
- **UWP integráció**: Integrálja Universal Windows Platform alkalmazásokkal  

### TensorFlow Lite  
- **Mobil optimalizáció**: Telepítse a TensorFlow Lite modelleket mobil és beágyazott eszközökre  
- **Hardver delegáltak**: Használjon speciális hardver delegáltakat a gyorsításhoz  
- **Mikrokontrollerek**: Telepítse mikrokontrollerekre a TensorFlow Lite Micro segítségével  
- **Platformközi támogatás**: Telepítse Android, iOS és beágyazott Linux rendszerekre  

### Azure IoT Edge  
- **Felhő-edge hibrid**: Kombinálja a felhőben történő tanítást az edge következtetéssel  
- **Modul telepítés**: Telepítse az AI modelleket IoT Edge modulokként  
- **Eszközkezelés**: Kezelje edge eszközöket és modellfrissítéseket távolról  
- **Telemetria**: Gyűjtsön teljesítményadatokat és modellmetrikákat edge telepítésekből  

## Fejlett Edge AI forgatókönyvek  

### Többmodellű telepítés  
- **Modellcsoportok**: Telepítsen több modellt a pontosság vagy redundancia javítására  
- **A/B tesztelés**: Teszteljen különböző modelleket egyidejűleg edge eszközökön  
- **Dinamikus kiválasztás**: Válasszon modelleket az aktuális eszközállapot alapján  
- **Erőforrás-megosztás**: Optimalizálja az erőforrás-használatot több telepített modell között  

### Federált tanulás  
- **Elosztott tanítás**: Tanítsa a modelleket több edge eszközön  
- **Adatvédelem megőrzése**: Tartsa helyben a tanítási adatokat, miközben megosztja a modellfejlesztéseket  
- **Kollaboratív tanulás**: Tegye lehetővé az eszközök számára, hogy tanuljanak a közös tapasztalatokból  
- **Edge-felhő koordináció**: Koordinálja a tanulást az edge eszközök és a felhő infrastruktúra között  

### Valós idejű feldolgozás  
- **Stream feldolgozás**: Folyamatos adatfolyamok feldolgozása edge eszközökön  
- **Alacsony késleltetésű következtetés**: Optimalizálja a minimális következtetési késleltetés érdekében  
- **Batch feldolgozás**: Hatékonyan dolgozza fel az adatcsomagokat edge eszközökön  
- **Adaptív feldolgozás**: Igazítsa a feldolgozást az aktuális eszközképességekhez  

## Edge AI fejlesztés hibaelhárítása  

### Gyakori problémák  
- **Memóriakorlátok**: A modell túl nagy a cél eszköz memóriájához  
- **Következtetési sebesség**: A modell következtetése túl lassú valós idejű követelményekhez  
- **Pontosságromlás**: Az optimalizálás elfogadhatatlanul csökkenti a modell pontosságát  
- **Hardverkompatibilitás**: A modell nem kompatibilis a cél hardverrel  

### Hibakeresési stratégiák  
- **Teljesítményprofilozás**: Használja az AI Toolkit nyomkövetési funkcióit a szűk keresztmetszetek azonosításához  
- **Erőforrás-figyelés**: Figyelje a memória- és CPU-használatot a fejlesztés során  
- **Inkrementális tesztelés**: Tesztelje az optimalizálásokat fokozatosan a problémák elkülönítéséhez  
- **Hardverszimuláció**: Használja a fejlesztési eszközöket a cél hardver szimulálásához  

### Optimalizálási megoldások  
- **További kvantálás**: Alkalmazzon agresszívebb kvantálási technikákat  
- **Modellarchitektúra**: Fontolja meg különböző modellarchitektúrákat, amelyek edge-re optimalizáltak  
- **Előfeldolgozási optimalizálás**: Optimalizálja az adat előfeldolgozását az edge korlátokhoz  
- **Következtetési optimalizálás**: Használjon hardver-specifikus következtetési optimalizációkat  

## Erőforrások és következő lépések  

### Hivatalos dokumentáció  
- [AI Toolkit fejlesztői dokumentáció](https://aka.ms/AIToolkit/doc)  
- [Telepítési és beállítási útmutató](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps dokumentáció](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) dokumentáció](https://modelcontextprotocol.io/)  

### Közösség és támogatás  
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub hibák és funkciókérések](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord közösség](https://aka.ms/azureaifoundry/discord)  
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Technikai erőforrások  
- [ONNX Runtime dokumentáció](https://onnxruntime.ai/)  
- [Ollama dokumentáció](https://ollama.ai/)  
- [Windows ML dokumentáció](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry dokumentáció](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Tanulási útvonalak  
- [Edge AI alapok kurzus](../Module01/README.md)  
- [Kis nyelvi modellek útmutató](../Module02/README.md)  
- [Edge telepítési stratégiák](../Module03/README.md)  
- [Windows Edge AI fejlesztés](./windowdeveloper.md)  

### További erőforrások  
- **Repository statisztikák**: Több mint 1.8k csillag, 150+ fork, 18+ közreműködő  
- **Licenc**: MIT Licenc  
- **Biztonság**: Microsoft biztonsági irányelvek érvényesek  
- **Telemetria**: Tiszteletben tartja a VS Code telemetria beállításait  

## Összegzés  

Az AI Toolkit for Visual Studio Code egy átfogó platformot képvisel a modern AI fejlesztéshez, amely különösen értékes az Edge AI alkalmazások számára. Kiterjedt modellkatalógusával, amely támogatja az olyan szolgáltatókat, mint az Anthropic, OpenAI, GitHub és Google, valamint az ONNX és Ollama helyi futtatásával, a toolkit biztosítja a rugalmasságot a különféle edge telepítési forgatókönyvekhez.  

A toolkit ereje az integrált megközelítésében rejlik—modellfelfedezéstől és kísérletezéstől a Playgroundban, a Prompt Builderrel történő kifinomult ügynökfejlesztésen, átfogó értékelési képességeken és zökkenőmentes MCP eszközintegráción keresztül. Az Edge AI fejlesztők számára ez gyors prototípus-készítést és AI ügynökök tesztelését jelenti edge telepítés előtt, azzal a képességgel, hogy gyorsan iteráljanak és optimalizáljanak erőforrás-korlátozott környezetekhez.  

Az Edge AI fejlesztés kulcsfontosságú előnyei:  
- **Gyors kísérletezés**: Modellek és ügynökök gyors tesztelése edge telepítés előtt  
- **Több szolgáltató rugalmassága**: Modellek elérése különböző forrásokból az optimális edge megoldások megtalálásához  
- **Helyi fejlesztés**: Tesztelés ONNX és Ollama segítségével offline és adatvédelmi szempontból biztonságos környezetben  
- **Gyártási készség**: Gyártásra kész kód generálása és külső eszközökkel való integráció MCP-n keresztül  
- **Átfogó értékelés**: Beépített és egyedi metrikák használata az edge AI teljesítmény validálásához  

Ahogy az AI egyre inkább az edge telepítési forgatókönyvek felé mozdul, az AI Toolkit for VS Code biztosítja azt a fejlesztési környezetet és munkafolyamatot, amely szükséges az intelligens alkalmazások építéséhez, teszteléséhez és optimalizálásához erőforrás-korlátozott környezetekben. Akár IoT megoldásokat, mobil AI alkalmazásokat vagy beágyazott intelligens rendszereket fejleszt, a toolkit átfogó funkciókészlete és integrált munkafolyamata támogatja az egész edge AI fejlesztési életciklust.  

A folyamatos fejlesztés és aktív közösség (több mint 1.8k GitHub csillag) révén az AI Toolkit továbbra is az élvonalban marad az AI fejlesztési eszközök között, folyamatosan fejlődve, hogy megfeleljen a modern AI fejlesztők igényeinek, akik edge telepítési forgatókönyvekre építenek.  

[Next Foundry Local](./foundrylocal.md)  

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.