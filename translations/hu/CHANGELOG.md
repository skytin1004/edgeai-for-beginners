<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T01:05:52+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "hu"
}
-->
# Változások naplója

Az EdgeAI for Beginners minden jelentős változása itt van dokumentálva. Ez a projekt dátum-alapú bejegyzéseket és a Keep a Changelog stílust használja (Hozzáadva, Módosítva, Javítva, Eltávolítva, Dokumentáció, Áthelyezve).

## 2025-09-23

### Módosítva - Modul 08 jelentős modernizáció
- **Átfogó igazítás a Microsoft Foundry-Local repository mintákhoz**
  - Minden kódpélda frissítése modern `FoundryLocalManager` és OpenAI SDK integrációval
  - Elavult manuális `requests` hívások lecserélése megfelelő SDK használatra
  - Implementációs minták igazítása hivatalos Microsoft dokumentációval és mintákkal

- **05.AIPoweredAgents.md modernizáció**:
  - Többügynökös orkestráció frissítése modern SDK minták használatával
  - Koordinátor implementáció fejlesztése fejlett funkciókkal (visszacsatolási hurkok, teljesítményfigyelés)
  - Átfogó hibakezelés és szolgáltatás-egészség ellenőrzés hozzáadása
  - Helyi mintákra való megfelelő hivatkozások integrálása (`samples/05/multi_agent_orchestration.ipynb`)
  - Funkcióhívási példák frissítése modern `tools` paraméter használatával az elavult `functions` helyett
  - Termelésre kész minták hozzáadása monitorozással és statisztikai követéssel

- **06.ModelsAsTools.md teljes újraírása**:
  - Alapvető eszközregiszter lecserélése intelligens modellirányító implementációval
  - Kulcsszó-alapú modellválasztás hozzáadása különböző feladattípusokhoz (általános, érvelés, kód, kreatív)
  - Környezet-alapú konfiguráció integrálása rugalmas modellkiosztással
  - Szolgáltatás-egészség figyelés és hibakezelés átfogó fejlesztése
  - Termelési telepítési minták hozzáadása kérésfigyeléssel és teljesítménykövetéssel
  - Helyi implementációval való igazítás `samples/06/router.py` és `samples/06/model_router.ipynb` fájlokban

- **Dokumentációs struktúra fejlesztések**:
  - Áttekintő szekciók hozzáadása, amelyek kiemelik a modernizációt és az SDK igazítást
  - Emojik és jobb formázás hozzáadása az olvashatóság javítása érdekében
  - Helyi mintafájlokra való megfelelő hivatkozások hozzáadása a dokumentációban
  - Termelésre kész implementációs útmutatók és legjobb gyakorlatok beépítése

### Hozzáadva
- Átfogó áttekintő szekciók a Modul 08 fájlokban, amelyek kiemelik a modern SDK integrációt
- Architektúra kiemelések, amelyek bemutatják a fejlett funkciókat (többügynökös rendszerek, intelligens irányítás)
- Közvetlen hivatkozások helyi mintaimplementációkra gyakorlati tapasztalatokhoz
- Termelési telepítési útmutatók monitorozási és hibakezelési mintákkal
- Interaktív Jupyter notebook példák fejlett funkciókkal és benchmarkokkal

### Javítva
- Igazítási eltérések a dokumentáció és a tényleges mintaimplementációk között
- Elavult SDK használati minták a Modul 08-ban
- Hiányzó hivatkozások az átfogó helyi mintakönyvtárra
- Inkonzisztens implementációs megközelítések különböző szekciókban

---

## 2025-09-18

### Hozzáadva
- Modul 08: Microsoft Foundry Local – Teljes fejlesztői eszközkészlet
  - Hat szekció: beállítás, Azure AI Foundry integráció, nyílt forráskódú modellek, élvonalbeli demók, ügynökök és modellek mint eszközök
  - Futtatható minták `Module08/samples/01`–`06` alatt Windows cmd utasításokkal
    - `01` REST gyors chat (`chat_quickstart.py`)
    - `02` SDK gyorsindító OpenAI/Foundry Local és Azure OpenAI támogatással (`sdk_quickstart.py`)
    - `03` CLI listázás és benchmark (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Többügynökös orkestráció (`python -m samples.05.agents.coordinator`)
    - `06` Modellek mint eszközök irányító (`router.py`)
- Azure OpenAI támogatás a 2. szekció SDK mintájában környezeti változó konfigurációval
- `.vscode/settings.json` a `Module08/.venv`-re mutatva a Python elemzés felbontásának javítása érdekében
- `.env` `PYTHONPATH` utalással a VS Code/Pylance felismeréshez

### Módosítva
- Alapértelmezett modell frissítése `phi-4-mini`-re a Modul 08 dokumentációban és mintákban; az összes `phi-3.5` említés eltávolítása a Modul 08-ban
- Irányító (`Module08/samples/06/router.py`) fejlesztések:
  - Végpont felfedezése `foundry service status` regex elemzéssel
  - `/v1/models` egészségellenőrzés indításkor
  - Környezet-konfigurálható modellregiszter (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Követelmények frissítése: `Module08/requirements.txt` most tartalmazza az `openai`-t (a `requests`, `chainlit` mellett)
- Chainlit minta útmutató tisztázása és hibaelhárítás hozzáadása; import feloldás munkaterület beállításokkal

### Javítva
- Import problémák megoldása:
  - Az irányító már nem függ egy nem létező `utils` modultól; funkciók inline módon vannak
  - A koordinátor relatív importot használ (`from .specialists import ...`) és modul útvonalon keresztül van meghívva
  - VS Code/Pylance konfiguráció a `chainlit` és csomagimportok feloldásához
- Kisebb elírás javítása a `STUDY_GUIDE.md` fájlban és a Modul 08 lefedettség hozzáadása

### Eltávolítva
- Nem használt `Module08/infra/obs.py` törlése és az üres `infra/` könyvtár eltávolítása; megfigyelési minták opcionálisan megmaradtak a dokumentációban

### Áthelyezve
- Modul 08 demók konszolidálása `Module08/samples` alatt szekció-számozott mappákkal
  - Chainlit alkalmazás áthelyezése `samples/04`-be
  - Ügynökök áthelyezése `samples/05`-be és `__init__.py` fájlok hozzáadása a csomagfeloldáshoz

### Dokumentáció
- Modul 08 szekció dokumentációk és minden minta README gazdagítása Microsoft Learn és megbízható gyártói hivatkozásokkal
- `Module08/README.md` frissítése minták áttekintésével, irányító konfigurációval és validációs tippekkel
- `Module07/README.md` Windows Foundry Local szekció validálása Learn dokumentációval
- `STUDY_GUIDE.md` frissítése:
  - Modul 08 hozzáadása az áttekintéshez, ütemtervekhez, haladáskövetőhöz
  - Átfogó hivatkozások szekció hozzáadása (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Történeti (összefoglaló)
- Kurzus architektúra és modulok létrehozása (01–07 modulok)
- Iteratív tartalom modernizáció, formázási standardizáció és esettanulmányok hozzáadása
- Optimalizációs keretrendszerek lefedettségének bővítése (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Kiadatlan / Hátralévő (javaslatok)
- Opcionális mintánkénti gyors tesztek a Foundry Local elérhetőség validálásához
- Fordítások felülvizsgálata a modellhivatkozások igazításához (pl. `phi-4-mini`)
- Minimális pyright konfiguráció hozzáadása, ha a csapatok munkaterület-szintű szigorúságot preferálnak

---

