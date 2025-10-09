<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T20:40:07+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "hu"
}
-->
# Változások naplója

Az EdgeAI for Beginners minden jelentős változása itt kerül dokumentálásra. Ez a projekt dátum-alapú bejegyzéseket és a Keep a Changelog stílust használja (Hozzáadva, Módosítva, Javítva, Eltávolítva, Dokumentáció, Áthelyezve).

## 2025-10-08

### Hozzáadva - Workshop átfogó frissítés
- **Workshop README.md teljes újraírása**:
  - Átfogó bevezető hozzáadása, amely bemutatja az Edge AI értékajánlatát (adatvédelem, teljesítmény, költség)
  - 6 alapvető tanulási célkitűzés létrehozása részletes kompetenciákkal
  - Tanulási eredmények táblázat hozzáadása szállítmányokkal és kompetenciamátrixszal
  - Karrierre kész készségek szekció hozzáadása az iparági relevancia érdekében
  - Gyors kezdési útmutató létrehozása előfeltételekkel és 3 lépéses beállítással
  - Erőforrástáblák létrehozása Python mintákhoz (8 fájl futási idővel)
  - Jupyter notebookok táblázata (8 notebook nehézségi besorolással)
  - Dokumentációs táblázat létrehozása (7 kulcsfontosságú dokumentum "Használja, amikor" útmutatással)
  - Tanulási útvonal ajánlások hozzáadása különböző készségszintekhez

- **Workshop validációs és tesztelési infrastruktúra**:
  - `scripts/validate_samples.py` létrehozása - Átfogó validációs eszköz szintaxis, importok és legjobb gyakorlatok ellenőrzésére
  - `scripts/test_samples.py` létrehozása - Gyors teszt futtató az összes Python mintához
  - Validációs dokumentáció hozzáadása a `scripts/README.md` fájlhoz

- **Átfogó dokumentáció**:
  - `SAMPLES_UPDATE_SUMMARY.md` létrehozása - 400+ soros részletes útmutató az összes fejlesztésről
  - `UPDATE_COMPLETE.md` létrehozása - Frissítés befejezésének vezetői összefoglalója
  - `QUICK_REFERENCE.md` létrehozása - Gyors referencia kártya a Workshophoz

### Módosítva - Workshop Python minták modernizálása
- **Mind a 8 Python minta frissítése legjobb gyakorlatokkal**:
  - Hibakezelés javítása try-except blokkokkal minden I/O művelet körül
  - Típusjelzések és átfogó docstringek hozzáadása
  - Egységes [INFO]/[ERROR]/[RESULT] naplózási minta megvalósítása
  - Opcionális importok védelme telepítési útmutatóval
  - Felhasználói visszajelzés javítása az összes mintában

- **session01/chat_bootstrap.py**:
  - Ügyfél inicializálásának javítása átfogó hibaüzenetekkel
  - Streaming hibakezelés javítása szakaszellenőrzéssel
  - Jobb kivételkezelés hozzáadása szolgáltatás elérhetetlensége esetén

- **session02/rag_pipeline.py**:
  - Importőrök hozzáadása sentence-transformers esetében telepítési útmutatóval
  - Hibakezelés javítása beágyazási és generálási műveleteknél
  - Kimenet formázásának javítása strukturált eredményekkel

- **session02/rag_eval_ragas.py**:
  - Opcionális importok védelme (ragas, datasets) felhasználóbarát hibaüzenetekkel
  - Hibakezelés hozzáadása értékelési metrikákhoz
  - Kimenet formázásának javítása értékelési eredményekhez

- **session03/benchmark_oss_models.py**:
  - Kegyes degradáció megvalósítása (folytatja modellhibák esetén)
  - Részletes haladási jelentés és modellenkénti hibakezelés hozzáadása
  - Statisztikai számítások javítása átfogó hibakezeléssel

- **session04/model_compare.py**:
  - Típusjelzések hozzáadása (Tuple visszatérési típusok)
  - Kimenet formázásának javítása strukturált JSON eredményekkel
  - Modellenkénti hibakezelés megvalósítása helyreállítással

- **session05/agents_orchestrator.py**:
  - Agent.act() javítása átfogó docstringekkel
  - Pipeline hibakezelés hozzáadása szakaszok szerinti naplózással
  - Memóriakezelés és állapotkövetés javítása

- **session06/models_router.py**:
  - Funkciódokumentáció javítása az összes útválasztási komponenshez
  - Részletes naplózás hozzáadása a route() funkcióban
  - Tesztkimenet javítása strukturált eredményekkel

- **session06/models_pipeline.py**:
  - Hibakezelés hozzáadása a chat() segédfunkcióhoz
  - Pipeline() javítása szakasznaplózással és haladási jelentéssel
  - main() javítása átfogó hibakezeléssel

### Dokumentáció - Workshop dokumentáció fejlesztése
- Fő README.md frissítése Workshop szekcióval, amely kiemeli a gyakorlati tanulási útvonalat
- STUDY_GUIDE.md fejlesztése átfogó Workshop szekcióval, amely tartalmazza:
  - Tanulási célkitűzések és tanulmányi fókuszterületek
  - Önértékelési kérdések
  - Gyakorlati feladatok időbecslésekkel
  - Időbeosztás koncentrált és részmunkaidős tanulmányokhoz
  - Workshop hozzáadása a haladáskövetési sablonhoz
- Időbeosztási útmutató frissítése 20 óráról 30 órára (beleértve a Workshopot)
- Workshop mintaleírások és tanulási eredmények hozzáadása a README-hez

### Javítva
- Inkonzisztens hibakezelési minták megoldása a Workshop minták között
- Opcionális függőség importálási hibák javítása megfelelő védelmekkel
- Hiányzó típusjelzések javítása kritikus funkciókban
- Elégtelen felhasználói visszajelzés kezelése hibás helyzetekben
- Validációs problémák megoldása átfogó tesztelési infrastruktúrával

---

## 2025-09-23

### Módosítva - Modul 08 jelentős modernizálása
- **Átfogó igazítás a Microsoft Foundry-Local repository mintákhoz**
  - Minden kódpélda frissítése modern `FoundryLocalManager` és OpenAI SDK integrációval
  - Elavult manuális `requests` hívások cseréje megfelelő SDK használatra
  - Implementációs minták igazítása hivatalos Microsoft dokumentációval és mintákkal

- **05.AIPoweredAgents.md modernizálása**:
  - Többügynökös orkestráció frissítése modern SDK minták használatával
  - Koordinátor implementációjának fejlesztése fejlett funkciókkal (visszacsatolási hurkok, teljesítményfigyelés)
  - Átfogó hibakezelés és szolgáltatás egészségellenőrzés hozzáadása
  - Megfelelő hivatkozások integrálása helyi mintákhoz (`samples/05/multi_agent_orchestration.ipynb`)
  - Funkcióhívási példák frissítése modern `tools` paraméter használatával az elavult `functions` helyett
  - Termelésre kész minták hozzáadása monitorozással és statisztikai követéssel

- **06.ModelsAsTools.md teljes újraírása**:
  - Alapvető eszközregiszter cseréje intelligens modell útválasztó implementációval
  - Kulcsszó-alapú modellválasztás hozzáadása különböző feladattípusokhoz (általános, érvelés, kód, kreatív)
  - Környezet-alapú konfiguráció integrálása rugalmas modellhozzárendeléssel
  - Fejlesztés átfogó szolgáltatás egészségfigyeléssel és hibakezeléssel
  - Termelési telepítési minták hozzáadása kérésfigyeléssel és teljesítménykövetéssel
  - Igazítás helyi implementációval a `samples/06/router.py` és `samples/06/model_router.ipynb` fájlokban

- **Dokumentációs struktúra fejlesztések**:
  - Áttekintő szekciók hozzáadása, amelyek kiemelik a modernizációt és SDK igazítást
  - Fejlesztés emojikkal és jobb formázással az olvashatóság javítása érdekében
  - Megfelelő hivatkozások hozzáadása helyi mintafájlokhoz a dokumentációban
  - Termelésre kész implementációs útmutató és legjobb gyakorlatok integrálása

### Hozzáadva
- Átfogó áttekintő szekciók a Modul 08 fájlokban, amelyek kiemelik a modern SDK integrációt
- Architektúra kiemelések, amelyek bemutatják a fejlett funkciókat (többügynökös rendszerek, intelligens útválasztás)
- Közvetlen hivatkozások helyi mintaimplementációkra gyakorlati tapasztalatokhoz
- Termelési telepítési útmutató monitorozási és hibakezelési mintákkal
- Interaktív Jupyter notebook példák fejlett funkciókkal és benchmarkokkal

### Javítva
- Igazítási eltérések a dokumentáció és a tényleges mintaimplementációk között
- Elavult SDK használati minták a Modul 08-ban
- Hiányzó hivatkozások átfogó helyi mintakönyvtárhoz
- Inkonzisztens implementációs megközelítések különböző szekciókban

---

## 2025-09-18

### Hozzáadva
- Modul 08: Microsoft Foundry Local – Teljes fejlesztői eszközkészlet
  - Hat szekció: beállítás, Azure AI Foundry integráció, nyílt forráskódú modellek, élvonalbeli demók, ügynökök és modellek mint eszközök
  - Futtatható minták a `Module08/samples/01`–`06` alatt Windows cmd utasításokkal
    - `01` REST gyors chat (`chat_quickstart.py`)
    - `02` SDK gyorsindító OpenAI/Foundry Local és Azure OpenAI támogatással (`sdk_quickstart.py`)
    - `03` CLI listázás és benchmark (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Többügynökös orkestráció (`python -m samples.05.agents.coordinator`)
    - `06` Modellek mint eszközök útválasztó (`router.py`)
- Azure OpenAI támogatás a 2. szekció SDK mintában környezeti változó konfigurációval
- `.vscode/settings.json` a `Module08/.venv`-re mutat, javítva a Python elemzési felbontást
- `.env` a `PYTHONPATH` utalással a VS Code/Pylance tudatosság érdekében

### Módosítva
- Alapértelmezett modell frissítése `phi-4-mini`-re a Modul 08 dokumentációban és mintákban; az összes fennmaradó `phi-3.5` említés eltávolítása a Modul 08-ban
- Útválasztó (`Module08/samples/06/router.py`) fejlesztések:
  - Végpont felfedezése `foundry service status` regex elemzéssel
  - `/v1/models` egészségellenőrzés indításkor
  - Környezet-konfigurálható modellregiszter (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Követelmények frissítése: `Module08/requirements.txt` most tartalmazza az `openai`-t (a `requests`, `chainlit` mellett)
- Chainlit minta útmutató tisztázása és hibaelhárítás hozzáadása; import feloldás munkaterület beállításokkal

### Javítva
- Importálási problémák megoldása:
  - Az útválasztó már nem függ egy nem létező `utils` modultól; funkciók inline kerültek
  - A koordinátor relatív importot használ (`from .specialists import ...`) és modul útvonalon keresztül van meghívva
  - VS Code/Pylance konfiguráció a `chainlit` és csomagimportok feloldására
- Kisebb elírás javítása a `STUDY_GUIDE.md` fájlban és Modul 08 lefedettség hozzáadása

### Eltávolítva
- Nem használt `Module08/infra/obs.py` törlése és az üres `infra/` könyvtár eltávolítása; megfigyelési minták opcionálisan megmaradtak a dokumentációban

### Áthelyezve
- Modul 08 demók konszolidálása a `Module08/samples` alatt szekció-számozott mappákkal
  - Chainlit alkalmazás áthelyezése a `samples/04`-be
  - Ügynökök áthelyezése a `samples/05`-be és `__init__.py` fájlok hozzáadása a csomagfeloldáshoz

### Dokumentáció
- Modul 08 szekció dokumentációk és minden minta README gazdagítása Microsoft Learn és megbízható szállítói hivatkozásokkal
- `Module08/README.md` frissítése minták áttekintésével, útválasztó konfigurációval és validációs tippekkel
- `Module07/README.md` Windows Foundry Local szekció validálása Learn dokumentációval
- `STUDY_GUIDE.md` frissítése:
  - Modul 08 hozzáadása áttekintéshez, ütemtervekhez, haladáskövetőhöz
  - Átfogó Hivatkozások szekció hozzáadása (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Történeti (összefoglaló)
- Kurzus architektúra és modulok létrehozása (01–07 modulok)
- Iteratív tartalom modernizálás, formázási szabványosítás és esettanulmányok hozzáadása
- Optimalizációs keretrendszerek lefedettségének bővítése (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Kiadatlan / Hátralévő (javaslatok)
- Opcionális mintánkénti gyors tesztek a Foundry Local elérhetőség validálására
- Fordítások felülvizsgálata a modellhivatkozások igazítására (pl. `phi-4-mini`)
- Minimális pyright konfiguráció hozzáadása, ha a csapatok munkaterület-szintű szigorúságot preferálnak

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.