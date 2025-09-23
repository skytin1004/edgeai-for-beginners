<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-23T00:47:40+00:00",
  "source_file": "Module08/README.md",
  "language_code": "hu"
}
-->
# Modul 08: Gyakorlati munka a Microsoft Foundry Local - Teljes fejlesztői eszköztárral

## Áttekintés

A Microsoft Foundry Local az edge AI fejlesztés következő generációját képviseli, amely lehetővé teszi a fejlesztők számára, hogy erőteljes eszközökkel építsenek, telepítsenek és méretezzenek AI alkalmazásokat helyben, miközben zökkenőmentesen integrálódnak az Azure AI Foundry-val. Ez a modul átfogó bemutatást nyújt a Foundry Local-ról, az installációtól kezdve a fejlett ügynökfejlesztésig.

**Kulcstechnológiák:**
- Microsoft Foundry Local CLI és SDK
- Azure AI Foundry integráció
- Eszközön történő modellkövetkeztetés
- Helyi modellgyorsítótár és optimalizálás
- Ügynök-alapú architektúrák

## Modul tanulási céljai

A modul elvégzésével:

- **Elsajátítod a Foundry Local beállítását**: Telepítés, konfigurálás és optimalizálás Windows 11 fejlesztéshez
- **Különböző modelleket telepítesz**: Phi, Qwen, Deepseek és GPT-OSS-20B modellek futtatása helyben CLI parancsokkal
- **Gyártási megoldásokat építesz**: AI alkalmazások létrehozása fejlett prompt mérnöki és adatintegrációs technikákkal
- **Nyílt forráskódú ökoszisztémát használsz**: Hugging Face modellek és közösségi kiegészítések integrálása
- **AI architektúrákat hasonlítasz össze**: LLM-ek és SLM-ek közötti kompromisszumok és telepítési stratégiák megértése
- **AI ügynököket fejlesztesz**: Intelligens ügynökök építése a Foundry Local architektúrájával és alapozási képességeivel
- **Modelleket eszközként alkalmazol**: Moduláris, testreszabható AI megoldások létrehozása vállalati alkalmazásokhoz

## Foglalkozások felépítése

### [1: Bevezetés a Foundry Local-ba](./01.FoundryLocalSetup.md)
**Fókusz**: Telepítés, CLI beállítás, modellgyorsítótár és hardvergyorsítás

**Amit megtanulsz:**
- Foundry Local teljes telepítése Windows 11-en
- CLI konfiguráció és parancsstruktúra
- Modellgyorsítótár stratégiák az optimális teljesítmény érdekében
- Hardvergyorsítás beállítása és optimalizálása
- Phi, Qwen, Deepseek és GPT-OSS-20B modellek gyakorlati telepítése

**Időtartam**: 2-3 óra  
**Előfeltételek**: Windows 11, alapvető parancssori ismeretek

---

### [2: AI megoldások építése az Azure AI Foundry-val](./02.AzureAIFoundryIntegration.md)
**Fókusz**: Fejlett prompt mérnöki, adatintegráció és cselekvési feladatok

**Amit megtanulsz:**
- Fejlett prompt mérnöki technikák
- Adatintegrációs minták és legjobb gyakorlatok
- Cselekvési AI feladatok építése Foundry Local-lal
- Zökkenőmentes Azure AI Foundry integrációs munkafolyamatok
- Teljesítményoptimalizálás és monitorozás

**Időtartam**: 2-3 óra  
**Előfeltételek**: 1. foglalkozás elvégzése, Azure fiók (opcionális)

---

### [3: Nyílt forráskódú modellek Foundry Local-ban](./03.OpenSourceModels.md)
**Fókusz**: Hugging Face integráció, modellválasztási stratégiák és közösségi kiegészítések

**Amit megtanulsz:**
- Hugging Face modellek integrációja Foundry Local-lal
- Saját modell (BYOM) stratégiák és megvalósítás
- Model Mondays sorozat betekintései és közösségi hozzájárulások
- Egyedi modellek telepítése és optimalizálása
- Közösségi modellek értékelési és kiválasztási kritériumai

**Időtartam**: 2-3 óra  
**Előfeltételek**: 1-2. foglalkozás elvégzése, Hugging Face fiók

---

### [4: Legmodernebb modellek felfedezése - LLM-ek, SLM-ek és eszközön történő következtetés](./04.CuttingEdgeModels.md)
**Fókusz**: Modellösszehasonlítás, EdgeAI Phi-val és ONNX Runtime-mal, fejlett demók

**Amit megtanulsz:**
- Átfogó LLM-ek és SLM-ek összehasonlítása és felhasználási esetek
- Helyi és felhő alapú következtetés közötti kompromisszumok és döntési keretek
- EdgeAI megvalósítás Phi-val és ONNX Runtime-mal
- Chainlit RAG Chat App fejlesztése és telepítése
- WebGPU következtetés optimalizálási technikák
- AI PC SDK integráció és képességek

**Időtartam**: 3-4 óra  
**Előfeltételek**: 1-3. foglalkozás elvégzése, következtetési koncepciók megértése

---

### [5: AI-alapú ügynökök gyors fejlesztése Foundry Local-lal](./05.AIPoweredAgents.md)
**Fókusz**: Gyors GenAI alkalmazásfejlesztés, rendszerpromptok, alapozás és ügynökarchitektúrák

**Amit megtanulsz:**
- Foundry Local ügynökarchitektúra és tervezési minták
- Rendszerprompt mérnöki az ügynök viselkedéséhez
- Alapozási technikák megbízható ügynökválaszokhoz
- Gyors GenAI alkalmazásfejlesztési munkafolyamatok
- Ügynökök koordinációja és többügynökös rendszerek
- AI ügynökök gyártási telepítési stratégiái

**Időtartam**: 3-4 óra  
**Előfeltételek**: 1-4. foglalkozás elvégzése, AI ügynökök alapvető ismerete

---

### [6: Foundry Local - Modellek mint eszközök](./06.ModelsAsTools.md)
**Fókusz**: Moduláris AI megoldások, eszközön történő telepítés és vállalati méretezés

**Amit megtanulsz:**
- AI modellek moduláris, testreszabható eszközként való kezelése
- Eszközön történő telepítés felhőfüggőség nélkül
- Alacsony késleltetésű, költséghatékony és adatvédelmet biztosító következtetés
- SDK, API és CLI integrációs minták
- Modell testreszabása specifikus felhasználási esetekhez
- Méretezési stratégiák helyi prototípusoktól Azure AI Foundry-ig
- Vállalati szintű AI alkalmazásarchitektúrák

**Időtartam**: 3-4 óra  
**Előfeltételek**: Az összes korábbi foglalkozás elvégzése, vállalati fejlesztési tapasztalat előnyös

## Előfeltételek

### Rendszerkövetelmények
- **Operációs rendszer**: Windows 11 (22H2 vagy újabb)
- **Memória**: 16GB RAM (32GB ajánlott nagyobb modellekhez)
- **Tárhely**: 50GB szabad hely modellgyorsítótárhoz
- **Hardver**: NPU-val rendelkező eszköz ajánlott (Copilot+ PC), GPU opcionális
- **Hálózat**: Nagy sebességű internet az első modellletöltésekhez

### Fejlesztési környezet
- Visual Studio Code AI Toolkit bővítménnyel
- Python 3.10+ és pip
- Git verziókezeléshez
- PowerShell vagy Command Prompt
- Azure CLI (opcionális felhőintegrációhoz)

### Tudás előfeltételek
- AI/ML alapfogalmak alapvető ismerete
- Parancssori ismeretek
- Python programozási alapok
- REST API fogalmak
- Promptolás és modellkövetkeztetés alapvető ismerete

## Modul idővonala

**Teljes becsült idő**: 15-20 óra

| Foglalkozás | Fókuszterület | Idő | Nehézség |
|-------------|---------------|------|----------|
|  1 | Beállítás és alapok | 2-3 óra | Kezdő |
|  2 | AI megoldások | 2-3 óra | Középhaladó |
|  3 | Nyílt forráskód | 2-3 óra | Középhaladó |
|  4 | Fejlett modellek | 3-4 óra | Haladó |
|  5 | AI ügynökök | 3-4 óra | Haladó |
|  6 | Vállalati eszközök | 3-4 óra | Szakértő |

## Kulcsfontosságú források

### Elsődleges dokumentáció
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Dokumentáció](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays Sorozat](https://aka.ms/model-mondays)

### Közösségi források
- [Foundry Local Közösségi Beszélgetések](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry Minták](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Fejlesztői Közösség](https://techcommunity.microsoft.com/category/artificialintelligence)

## Tanulási eredmények

A modul elvégzése után képes leszel:

### Technikai jártasság
- **Telepítés és kezelés**: Foundry Local telepítése fejlesztési és gyártási környezetekben
- **Modellek integrációja**: Különböző modellcsaládok zökkenőmentes használata Microsofttól, Hugging Face-től és közösségi forrásokból
- **Alkalmazások építése**: Gyártásra kész AI alkalmazások létrehozása fejlett funkciókkal és optimalizálásokkal
- **Ügynökök fejlesztése**: Fejlett AI ügynökök megvalósítása alapozással, érveléssel és eszközintegrációval

### Stratégiai megértés
- **Architektúra döntések**: Tájékozott választások helyi és felhő alapú telepítés között
- **Teljesítményoptimalizálás**: Következtetési teljesítmény optimalizálása különböző hardverkonfigurációkban
- **Vállalati méretezés**: Alkalmazások tervezése, amelyek helyi prototípusoktól vállalati telepítésekig skálázhatók
- **Adatvédelem és biztonság**: Adatvédelmet biztosító AI megoldások megvalósítása helyi következtetéssel

### Innovációs képességek
- **Gyors prototípus készítés**: AI alkalmazásötletek gyors építése és tesztelése
- **Közösségi integráció**: Nyílt forráskódú modellek használata és hozzájárulás az ökoszisztémához
- **Fejlett minták**: Legmodernebb AI minták megvalósítása, beleértve a RAG-et, ügynököket és eszközintegrációt
- **Jövőre kész fejlesztés**: Alkalmazások építése, amelyek készen állnak a feltörekvő AI technológiákra és mintákra

## Kezdés

1. **Készítsd elő a környezeted**: Biztosítsd a Windows 11-et az ajánlott hardver specifikációkkal
2. **Telepítsd az előfeltételeket**: Állítsd be a fejlesztési eszközöket és függőségeket
3. **Kezdd az 1. foglalkozással**: Indítsd el a Foundry Local telepítését és alapbeállítását
4. **Haladj sorrendben**: Végezd el a foglalkozásokat egymás után az optimális tanulási haladás érdekében
5. **Gyakorolj folyamatosan**: Alkalmazd a koncepciókat gyakorlati feladatokon és projekteken keresztül

## Sikerességi mutatók

Kövesd nyomon a modulban elért haladásodat:

- [ ] Foundry Local sikeres telepítése és konfigurálása
- [ ] Legalább 4 különböző modellcsalád telepítése és futtatása
- [ ] Teljes AI megoldás építése adatintegrációval
- [ ] Legalább 2 nyílt forráskódú modell integrálása
- [ ] Funkcionális RAG chat alkalmazás létrehozása
- [ ] AI ügynök fejlesztése és telepítése
- [ ] Modellek mint eszközök architektúra megvalósítása

## Gyors kezdés mintákhoz

### 1) Környezet beállítása (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Helyi modell indítása (új terminál)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Chainlit demo futtatása (4. foglalkozás)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Többügynökös koordinátor futtatása (5. foglalkozás)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Ha kapcsolat hibákat tapasztalsz, ellenőrizd a Foundry Local-t:
```cmd
curl http://localhost:8000/v1/models
```

### Router konfiguráció (6. foglalkozás)
A router gyors állapotellenőrzést végez és támogatja az env-alapú konfigurációt:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Ez a modul az edge AI fejlesztés élvonalát képviseli, ötvözve a Microsoft vállalati szintű eszközeit a nyílt forráskódú ökoszisztéma rugalmasságával és innovációjával. A Foundry Local elsajátításával az AI alkalmazásfejlesztés élvonalába kerülsz.

Az Azure OpenAI-hoz (2. foglalkozás) lásd a minta README-t a szükséges környezeti változók és API verzió beállításokhoz.

## Minták áttekintése

- `samples/01`: Gyors REST chat a Foundry Local-hoz (`chat_quickstart.py`).
- `samples/02`: OpenAI SDK integráció (`sdk_quickstart.py`).
- `samples/03`: Modell felfedezés + gyors teszt (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG demo (`app.py`).
- `samples/05`: Többügynökös koordináció (`python -m samples.05.agents.coordinator`).
- `samples/06`: Modellek mint eszközök router (`python samples\06\router.py`).

---

