<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-23T00:44:25+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "hu"
}
-->
# Változásnapló

Minden jelentős változás az EdgeAI for Beginners projektben itt van dokumentálva. Ez a projekt dátum-alapú bejegyzéseket és a Keep a Changelog stílust használja (Hozzáadva, Módosítva, Javítva, Eltávolítva, Dokumentáció, Áthelyezve).

## 2025-09-18

### Hozzáadva
- Modul 08: Microsoft Foundry Local – Teljes fejlesztői eszközkészlet
  - Hat szekció: beállítás, Azure AI Foundry integráció, nyílt forráskódú modellek, legmodernebb demók, ügynökök és modellek mint eszközök
  - Futtatható minták a `Module08/samples/01`–`06` alatt Windows cmd utasításokkal
    - `01` REST gyors chat (`chat_quickstart.py`)
    - `02` SDK gyorsindító OpenAI/Foundry Local és Azure OpenAI támogatással (`sdk_quickstart.py`)
    - `03` CLI listázás és tesztelés (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Több ügynök összehangolása (`python -m samples.05.agents.coordinator`)
    - `06` Modellek mint eszközök router (`router.py`)
- Azure OpenAI támogatás a 2. szekció SDK mintájában környezeti változó konfigurációval
- `.vscode/settings.json` a `Module08/.venv`-re mutat, hogy javítsa a Python elemzési felbontást
- `.env` `PYTHONPATH` utalással a VS Code/Pylance felismeréshez

### Módosítva
- Alapértelmezett modell frissítve `phi-4-mini`-re a Modul 08 dokumentációjában és mintáiban; eltávolítva a fennmaradó `phi-3.5` említések a Modul 08-ban
- Router (`Module08/samples/06/router.py`) fejlesztések:
  - Végpont-felismerés a `foundry service status` regex elemzésével
  - `/v1/models` állapotellenőrzés indításkor
  - Környezeti változóval konfigurálható modellregisztráció (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Követelmények frissítve: `Module08/requirements.txt` most tartalmazza az `openai`-t (a `requests`, `chainlit` mellett)
- Chainlit minta útmutató tisztázva és hibaelhárítás hozzáadva; import feloldás munkaterület beállításokkal

### Javítva
- Import problémák megoldva:
  - A router már nem függ egy nem létező `utils` modultól; funkciók beépítve
  - A koordinátor relatív importot használ (`from .specialists import ...`) és modul útvonalon keresztül van meghívva
  - VS Code/Pylance konfiguráció a `chainlit` és csomag importok feloldásához
- Kisebb elírás javítva a `STUDY_GUIDE.md`-ben, és hozzáadva a Modul 08 lefedettsége

### Eltávolítva
- Törölve a nem használt `Module08/infra/obs.py` és az üres `infra/` könyvtár; megfigyelési minták opcionálisan megtartva a dokumentációban

### Áthelyezve
- Modul 08 demók konszolidálva a `Module08/samples` alatt szekció-számozott mappákkal
  - Chainlit alkalmazás áthelyezve a `samples/04`-be
  - Ügynökök áthelyezve a `samples/05`-be, és hozzáadva `__init__.py` fájlok a csomagfeloldáshoz

### Dokumentáció
- Modul 08 szekció dokumentációk és minden minta README gazdagítva Microsoft Learn és megbízható gyártói hivatkozásokkal
- `Module08/README.md` frissítve minták áttekintésével, router konfigurációval és validációs tippekkel
- `Module07/README.md` Windows Foundry Local szekció validálva a Learn dokumentációval
- `STUDY_GUIDE.md` frissítve:
  - Modul 08 hozzáadva az áttekintéshez, ütemtervekhez, haladáskövetőhöz
  - Átfogó Hivatkozások szekció hozzáadva (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Történeti (összefoglaló)
- Kurzus architektúra és modulok létrehozva (Modulok 01–07)
- Iteratív tartalom modernizálás, formázási szabványosítás és esettanulmányok hozzáadása
- Optimalizációs keretrendszerek lefedettsége bővítve (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Kiadatlan / Hátralévő (javaslatok)
- Opcionális mintánkénti gyors tesztek a Foundry Local elérhetőségének validálására
- Fordítások felülvizsgálata a modellhivatkozások összehangolására (pl. `phi-4-mini`)
- Minimális pyright konfiguráció hozzáadása, ha a csapatok munkaterület-szintű szigorúságot preferálnak

---

