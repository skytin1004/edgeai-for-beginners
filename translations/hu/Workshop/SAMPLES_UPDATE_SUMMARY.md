<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T21:40:00+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "hu"
}
-->
# Workshop Minták - Foundry Local SDK Frissítési Összefoglaló

## Áttekintés

A `Workshop/samples` könyvtárban található összes Python minta frissítve lett, hogy kövesse a Foundry Local SDK legjobb gyakorlatait, és biztosítsa az egységességet a workshop során.

**Dátum**: 2025. október 8.  
**Hatókör**: 9 Python fájl 6 workshop szekcióban  
**Fő fókusz**: Hibakezelés, dokumentáció, SDK minták, felhasználói élmény

---

## Frissített fájlok

### 01. szekció: Első lépések
- ✅ `chat_bootstrap.py` - Alapvető chat és streaming példák

### 02. szekció: RAG Megoldások
- ✅ `rag_pipeline.py` - RAG megvalósítás beágyazásokkal
- ✅ `rag_eval_ragas.py` - RAG értékelés RAGAS metrikákkal

### 03. szekció: Nyílt Forráskódú Modellek
- ✅ `benchmark_oss_models.py` - Több modell összehasonlítása

### 04. szekció: Legújabb Modellek
- ✅ `model_compare.py` - SLM és LLM összehasonlítás

### 05. szekció: AI-Alapú Ügynökök
- ✅ `agents_orchestrator.py` - Több ügynök koordinációja

### 06. szekció: Modellek Eszközként
- ✅ `models_router.py` - Szándékalapú modellirányítás
- ✅ `models_pipeline.py` - Többlépéses irányított folyamat

### Támogató infrastruktúra
- ✅ `workshop_utils.py` - Már követi a legjobb gyakorlatokat (nem szükséges változtatás)

---

## Főbb fejlesztések

### 1. Fejlettebb hibakezelés

**Korábban:**
```python
manager, client, model_id = get_client(alias)
```

**Utána:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Előnyök:**
- Kifinomult hibakezelés egyértelmű hibaüzenetekkel
- Cselekvésre ösztönző hibaelhárítási tippek
- Megfelelő kilépési kódok szkriptekhez

### 2. Jobb import kezelés

**Korábban:**
```python
from sentence_transformers import SentenceTransformer
```

**Utána:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Előnyök:**
- Egyértelmű útmutatás hiányzó függőségek esetén
- Rejtélyes import hibák megelőzése
- Felhasználóbarát telepítési utasítások

### 3. Átfogó dokumentáció

**Minden mintához hozzáadva:**
- Környezeti változók dokumentációja docstringekben
- SDK referencia linkek
- Használati példák
- Részletes függvény/paraméter dokumentáció
- Típusjelzések a jobb IDE támogatás érdekében

**Példa:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Javított felhasználói visszajelzés

**Tájékoztató naplózás hozzáadva:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Haladásjelzők:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Strukturált kimenet:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Robusztus összehasonlítás

**03. szekció fejlesztései:**
- Modellenkénti hibakezelés (folytatás hiba esetén)
- Részletes haladásjelentés
- Bemelegítő körök megfelelő végrehajtása
- Első token késleltetés mérésének támogatása
- Szakaszok egyértelmű szétválasztása

### 6. Következetes típusjelzések

**Mindenhol hozzáadva:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Előnyök:**
- Jobb IDE automatikus kiegészítés
- Korai hibaérzékelés
- Öndokumentáló kód

### 7. Fejlesztett modellirányító

**06. szekció fejlesztései:**
- Átfogó szándékérzékelési dokumentáció
- Modellválasztási algoritmus magyarázata
- Részletes irányítási naplók
- Teszt kimeneti formázás
- Hibahelyreállítás csoportos tesztelés során

### 8. Több ügynök összehangolása

**05. szekció fejlesztései:**
- Szakaszról szakaszra haladásjelentés
- Ügynökönkénti hibakezelés
- Egyértelmű folyamatstruktúra
- Jobb memóriahasználati dokumentáció

---

## Tesztelési ellenőrzőlista

### Előfeltételek
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Minden minta tesztelése

#### 01. szekció
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### 02. szekció
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### 03. szekció
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### 04. szekció
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### 05. szekció
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### 06. szekció
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## Környezeti változók referencia

### Globális (minden minta)
| Változó | Leírás | Alapértelmezett |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Használt modell alias | Mintánként változó |
| `FOUNDRY_LOCAL_ENDPOINT` | Szolgáltatási végpont felülírása | Automatikusan észlelt |
| `SHOW_USAGE` | Tokenhasználat megjelenítése | `0` |
| `RETRY_ON_FAIL` | Újrapróbálkozási logika engedélyezése | `1` |
| `RETRY_BACKOFF` | Kezdeti újrapróbálkozási késleltetés | `1.0` |

### Mintaspecifikus
| Változó | Használja | Leírás |
|----------|---------|-------------|
| `EMBED_MODEL` | 02. szekció | Beágyazási modell neve |
| `RAG_QUESTION` | 02. szekció | Tesztkérdés RAG-hez |
| `BENCH_MODELS` | 03. szekció | Összehasonlítandó modellek vesszővel elválasztva |
| `BENCH_ROUNDS` | 03. szekció | Összehasonlítási körök száma |
| `BENCH_PROMPT` | 03. szekció | Teszt prompt az összehasonlításhoz |
| `BENCH_STREAM` | 03. szekció | Első token késleltetés mérése |
| `SLM_ALIAS` | 04. szekció | Kis nyelvi modell |
| `LLM_ALIAS` | 04. szekció | Nagy nyelvi modell |
| `COMPARE_PROMPT` | 04. szekció | Összehasonlítási teszt prompt |
| `AGENT_MODEL_PRIMARY` | 05. szekció | Elsődleges ügynök modell |
| `AGENT_MODEL_EDITOR` | 05. szekció | Szerkesztő ügynök modell |
| `AGENT_QUESTION` | 05. szekció | Tesztkérdés ügynökökhöz |
| `PIPELINE_TASK` | 06. szekció | Feladat a folyamatban |

---

## Kompatibilitást érintő változások

**Nincsenek** - Minden változás visszafelé kompatibilis.

A meglévő szkriptek továbbra is működnek. Az új funkciók:
- Opcionális környezeti változók
- Fejlettebb hibaüzenetek (nem törik meg a funkcionalitást)
- További naplózás (elnyomható)
- Jobb típusjelzések (nincs futásidejű hatás)

---

## Bevezetett legjobb gyakorlatok

### 1. Mindig használja a Workshop Utils-t
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Megfelelő hibakezelési minta
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Tájékoztató naplózás
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Típusjelzések
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Átfogó docstringek
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Környezeti változók támogatása
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Kifinomult degradáció
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Gyakori problémák és megoldások

### Probléma: Import hibák
**Megoldás:** Hiányzó függőségek telepítése
```bash
pip install sentence-transformers ragas datasets numpy
```

### Probléma: Kapcsolódási hibák
**Megoldás:** Ellenőrizze, hogy a Foundry Local fut-e
```bash
foundry service status
foundry model run phi-4-mini
```

### Probléma: Modell nem található
**Megoldás:** Ellenőrizze az elérhető modelleket
```bash
foundry model ls
foundry model download <alias>
```

### Probléma: Lassú teljesítmény
**Megoldás:** Használjon kisebb modelleket vagy állítsa be a paramétereket
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Következő lépések

### 1. Minden minta tesztelése
Futtassa végig a fenti tesztelési ellenőrzőlistát, hogy megbizonyosodjon arról, hogy minden minta helyesen működik.

### 2. Dokumentáció frissítése
- Frissítse a szekció markdown fájlokat új példákkal
- Adjon hozzá hibaelhárítási szekciót a fő README-hez
- Készítsen gyors referencia útmutatót

### 3. Integrációs tesztek létrehozása
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Teljesítmény összehasonlítások hozzáadása
Kövesse nyomon a hibakezelési fejlesztésekből származó teljesítményjavulásokat.

### 5. Felhasználói visszajelzés
Gyűjtsön visszajelzést a workshop résztvevőitől a következőkről:
- Hibaüzenetek egyértelműsége
- Dokumentáció teljessége
- Használhatóság

---

## Források

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Gyors referencia**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migrációs jegyzetek**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Fő tároló**: https://github.com/microsoft/Foundry-Local

---

## Karbantartás

### Új minták hozzáadása
Kövesse ezeket a mintákat új minták létrehozásakor:

1. Használja a `workshop_utils`-t az ügyfélkezeléshez
2. Adjon hozzá átfogó hibakezelést
3. Támogassa a környezeti változókat
4. Adjon hozzá típusjelzéseket és docstringeket
5. Biztosítson tájékoztató naplózást
6. Tartalmazzon használati példákat a docstringben
7. Linkeljen az SDK dokumentációhoz

### Frissítések áttekintése
Frissítések áttekintésekor ellenőrizze:
- [ ] Hibakezelés minden I/O műveleten
- [ ] Típusjelzések nyilvános függvényeken
- [ ] Átfogó docstringek
- [ ] Környezeti változók dokumentációja
- [ ] Tájékoztató felhasználói visszajelzés
- [ ] SDK referencia linkek
- [ ] Következetes kódstílus

---

**Összefoglaló**: A Workshop Python minták mostantól követik a Foundry Local SDK legjobb gyakorlatait, fejlettebb hibakezeléssel, átfogó dokumentációval és javított felhasználói élménnyel. Nincsenek kompatibilitást érintő változások - minden meglévő funkcionalitás megmaradt és továbbfejlesztett.

---

**Felelősségkizárás**:  
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével fordították le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.