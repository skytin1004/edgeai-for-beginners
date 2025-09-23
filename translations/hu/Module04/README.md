<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c0cb9f7bcff2bc170532d8870a891f38",
  "translation_date": "2025-09-18T16:51:26+00:00",
  "source_file": "Module04/README.md",
  "language_code": "hu"
}
-->
# 4. fejezet: Modellformátum átalakítása és kvantálás - Fejezet áttekintése

Az EdgeAI megjelenése a modellformátum átalakítását és kvantálását alapvető technológiákká tette a fejlett gépi tanulási képességek erőforrás-korlátozott eszközökön történő telepítéséhez. Ez az átfogó fejezet teljes útmutatót nyújt a modellek megértéséhez, megvalósításához és optimalizálásához az edge telepítési környezetekben.

## 📚 Fejezet felépítése és tanulási útvonal

Ez a fejezet hat egymásra épülő szakaszra van osztva, amelyek egymásra épülve átfogó megértést nyújtanak a modellek optimalizálásáról az edge számítástechnika számára:

---

## [1. szakasz: Modellformátum átalakítás és kvantálás alapjai](./01.Introduce.md)

### 🎯 Áttekintés
Ez az alapvető szakasz elméleti keretet biztosít a modellek optimalizálásához edge számítástechnikai környezetekben, lefedve a kvantálási határokat az 1-bites és 8-bites pontossági szintek között, valamint a kulcsfontosságú formátum átalakítási stratégiákat.

**Fő témák:**
- Pontossági osztályozási keret (ultra-alacsony, alacsony, közepes pontosság)
- GGUF és ONNX formátum előnyei és felhasználási esetei
- A kvantálás előnyei az operatív hatékonyság és telepítési rugalmasság szempontjából
- Teljesítmény-összehasonlítások és memóriahasználati összevetések

**Tanulási eredmények:**
- Értsd meg a kvantálási határokat és osztályozásokat
- Azonosítsd a megfelelő formátum átalakítási technikákat
- Tanuld meg az edge telepítéshez szükséges fejlett optimalizálási stratégiákat

---

## [2. szakasz: Llama.cpp megvalósítási útmutató](./02.Llamacpp.md)

### 🎯 Áttekintés
Átfogó útmutató a Llama.cpp megvalósításához, egy erőteljes C++ keretrendszerhez, amely minimális beállítással hatékony Nagy Nyelvi Modell következtetést tesz lehetővé különböző hardverkonfigurációkon.

**Fő témák:**
- Telepítés Windows, macOS és Linux platformokon
- GGUF formátum átalakítás és különböző kvantálási szintek (Q2_K-tól Q8_0-ig)
- Hardvergyorsítás CUDA, Metal, OpenCL és Vulkan segítségével
- Python integráció és termelési telepítési stratégiák

**Tanulási eredmények:**
- Sajátítsd el a többplatformos telepítést és forrásból történő építést
- Valósítsd meg a modell kvantálási és optimalizálási technikákat
- Telepítsd a modelleket szerver módban REST API integrációval

---

## [3. szakasz: Microsoft Olive optimalizációs csomag](./03.MicrosoftOlive.md)

### 🎯 Áttekintés
A Microsoft Olive felfedezése, egy hardver-tudatos modelloptimalizáló eszköztár, amely több mint 40 beépített optimalizációs komponenst kínál, és vállalati szintű modelltelepítést tesz lehetővé különböző hardverplatformokon.

**Fő témák:**
- Automatikus optimalizáció dinamikus és statikus kvantálással
- Hardver-tudatos intelligencia CPU, GPU és NPU telepítéshez
- Népszerű modellek támogatása (Llama, Phi, Qwen, Gemma) azonnal használhatóan
- Vállalati integráció Azure ML-lel és termelési munkafolyamatokkal

**Tanulási eredmények:**
- Használd az automatikus optimalizációt különböző modellarchitektúrákhoz
- Valósítsd meg a többplatformos telepítési stratégiákat
- Hozz létre vállalati szintű optimalizációs csatornákat

---

## [4. szakasz: OpenVINO Toolkit optimalizációs csomag](./04.openvino.md)

### 🎯 Áttekintés
Az Intel OpenVINO eszköztárának átfogó bemutatása, egy nyílt forráskódú platform, amely fejlett AI megoldások telepítését teszi lehetővé felhőben, helyszínen és edge környezetekben, fejlett Neurális Hálózat Kompressziós Keretrendszer (NNCF) képességekkel.

**Fő témák:**
- Többplatformos telepítés hardvergyorsítással (CPU, GPU, VPU, AI gyorsítók)
- Neurális Hálózat Kompressziós Keretrendszer (NNCF) fejlett kvantáláshoz és metszéshez
- OpenVINO GenAI nagy nyelvi modellek optimalizálásához és telepítéséhez
- Vállalati szintű modell szerver képességek és skálázható telepítési stratégiák

**Tanulási eredmények:**
- Sajátítsd el az OpenVINO modell átalakítási és optimalizálási munkafolyamatokat
- Valósítsd meg fejlett kvantálási technikákat az NNCF segítségével
- Telepítsd az optimalizált modelleket különböző hardverplatformokon Modell Szerverrel

---

## [5. szakasz: Apple MLX keretrendszer mélyreható bemutatása](./05.AppleMLX.md)

### 🎯 Áttekintés
Az Apple MLX átfogó bemutatása, egy forradalmi keretrendszer, amelyet kifejezetten hatékony gépi tanulásra terveztek Apple Siliconon, különös hangsúlyt fektetve a Nagy Nyelvi Modell képességekre és helyi telepítésre.

**Fő témák:**
- Egységes memóriaarchitektúra előnyei és Metal Performance Shaders
- LLaMA, Mistral, Phi-3, Qwen és Code Llama modellek támogatása
- LoRA finomhangolás hatékony modell testreszabáshoz
- Hugging Face integráció és kvantálási támogatás (4-bites és 8-bites)

**Tanulási eredmények:**
- Sajátítsd el az Apple Silicon optimalizálását LLM telepítéshez
- Valósítsd meg a finomhangolási és modell testreszabási technikákat
- Építs vállalati AI alkalmazásokat fokozott adatvédelmi funkciókkal

---

## [6. szakasz: Edge AI fejlesztési munkafolyamat szintézise](./06.workflow-synthesis.md)

### 🎯 Áttekintés
Az összes optimalizációs keretrendszer átfogó szintézise egységes munkafolyamatokba, döntési mátrixokba és legjobb gyakorlatokba a termelésre kész Edge AI telepítéshez különböző platformokon és felhasználási esetekben.

**Fő témák:**
- Egységes munkafolyamat architektúra több optimalizációs keretrendszer integrálásával
- Keretrendszer kiválasztási döntési fák és teljesítmény kompromisszumok elemzése
- Termelési készség validálása és átfogó telepítési stratégiák
- Jövőbiztos stratégiák feltörekvő hardverekhez és modellarchitektúrákhoz

**Tanulási eredmények:**
- Sajátítsd el a keretrendszer kiválasztásának szisztematikus megközelítését az igények és korlátok alapján
- Valósítsd meg termelési szintű Edge AI csatornákat átfogó monitorozással
- Tervezd meg az alkalmazkodó munkafolyamatokat, amelyek fejlődnek az új technológiákkal és igényekkel

---

## 🎯 Fejezet tanulási eredményei

A fejezet elvégzése után az olvasók elérik:

### **Technikai jártasság**
- Mély megértés a kvantálási határokról és gyakorlati alkalmazásokról
- Gyakorlati tapasztalat több optimalizációs keretrendszerrel
- Termelési telepítési készségek edge számítástechnikai környezetekhez

### **Stratégiai megértés**
- Hardver-tudatos optimalizációs kiválasztási képességek
- Tájékozott döntéshozatal a teljesítmény kompromisszumokról
- Vállalati szintű telepítési és monitorozási stratégiák

### **Teljesítmény összevetések**

| Keretrendszer | Kvantálás | Memóriahasználat | Sebességnövekedés | Felhasználási eset |
|---------------|-----------|------------------|-------------------|--------------------|
| Llama.cpp     | Q4_K_M    | ~4GB            | 2-3x             | Többplatformos telepítés |
| Olive         | INT4      | 60-75% csökkenés | 2-6x             | Vállalati munkafolyamatok |
| OpenVINO      | INT8/INT4 | 50-75% csökkenés | 2-5x             | Intel hardver optimalizáció |
| MLX           | 4-bites   | ~4GB            | 2-4x             | Apple Silicon optimalizáció |

## 🚀 Következő lépések és fejlett alkalmazások

Ez a fejezet teljes alapot nyújt:
- Egyedi modellek fejlesztéséhez specifikus területekre
- Kutatáshoz az edge AI optimalizáció területén
- Kereskedelmi AI alkalmazások fejlesztéséhez
- Nagy léptékű vállalati edge AI telepítésekhez

A fejezet hat szakaszából származó tudás átfogó eszköztárat kínál az edge AI modelloptimalizáció és telepítés gyorsan változó világának navigálásához.

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.