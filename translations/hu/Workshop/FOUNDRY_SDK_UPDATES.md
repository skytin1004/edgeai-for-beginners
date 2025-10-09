<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T21:05:04+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "hu"
}
-->
# Foundry Local SDK frissítések

## Áttekintés

Frissítettük a Workshop jegyzetfüzeteket és segédprogramokat, hogy megfelelően használják az **hivatalos Foundry Local Python SDK-t**, az alábbi minták alapján:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Módosított fájlok

### 1. `Workshop/samples/workshop_utils.py`

**Változások:**
- ✅ Hozzáadtuk az importálási hibakezelést a `foundry-local-sdk` csomaghoz
- ✅ Kibővítettük a dokumentációt a hivatalos SDK mintákkal
- ✅ Javítottuk a naplózást Unicode szimbólumokkal (✓, ✗, ⚠)
- ✅ Részletes docstringeket adtunk példákkal
- ✅ Jobb hibaüzeneteket készítettünk CLI parancsokra hivatkozva
- ✅ Frissítettük a megjegyzéseket, hogy megfeleljenek a hivatalos SDK dokumentációnak

**Főbb fejlesztések:**

#### Importálási hibakezelés
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Fejlesztett `get_client()` függvény
- Részletes dokumentációt adtunk az SDK inicializálási mintájáról
- Tisztáztuk, hogy a `FoundryLocalManager` automatikusan elindítja a szolgáltatást
- Elmagyaráztuk a modell aliasok hardver-optimalizált változatokra történő feloldását
- Javítottuk a naplózást végpont információkkal
- Jobb hibaüzeneteket készítettünk, amelyek javaslatokat adnak a hibaelhárításhoz

#### Fejlesztett `chat_once()` függvény
- Részletes docstringet adtunk használati példákkal
- Tisztáztuk az OpenAI SDK kompatibilitást
- Dokumentáltuk a streaming támogatást (kwargs segítségével)
- Javított hibaüzeneteket készítettünk CLI parancsokra hivatkozva
- Megjegyzéseket adtunk a modell elérhetőségének ellenőrzéséről

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Változások:**
- ✅ Frissítettük az összes markdown cellát SDK hivatkozásokkal
- ✅ Javítottuk a kódbeli megjegyzéseket az SDK minták magyarázatával
- ✅ Javítottuk a cellák dokumentációját és magyarázatait
- ✅ Hibaelhárítási útmutatót adtunk hozzá
- ✅ Frissítettük a modellkatalógust (a 'gpt-oss-20b'-t lecseréltük 'phi-3.5-mini'-re)
- ✅ Jobb kimeneti formázást készítettünk vizuális jelzőkkel
- ✅ SDK hivatkozásokat és referenciákat adtunk hozzá

**Cellánkénti frissítések:**

#### Cell 1 (Cím)
- SDK dokumentációs hivatkozásokat adtunk hozzá
- Hivatkoztunk a hivatalos GitHub repókra

#### Cell 2 (Forgatókönyv)
- Számozott lépésekkel formáztuk át
- Tisztáztuk a szándék-alapú útválasztási mintát
- Kiemeltük a helyi végrehajtás előnyeit

#### Cell 3 (Függőségek telepítése)
- Magyarázatot adtunk arra, hogy mit biztosít minden csomag
- Dokumentáltuk az SDK képességeit (alias feloldás, hardver optimalizáció)

#### Cell 4 (Környezet beállítása)
- Részletes docstringeket adtunk a függvényekhez
- Inline megjegyzéseket adtunk az SDK minták magyarázatához
- Dokumentáltuk a modellkatalógus struktúráját
- Tisztáztuk a prioritás/képesség egyeztetést

#### Cell 5 (Katalógus ellenőrzése)
- Vizsgálati pipákat (✓) adtunk hozzá
- Jobban formázott kimenetet készítettünk

#### Cell 6 (Szándék felismerési teszt)
- Táblázat-stílusú formázással alakítottuk át a kimenetet
- Megjeleníti a szándékot és a kiválasztott modellt

#### Cell 7 (Útválasztási függvény)
- Átfogó SDK mintamagyarázatot adtunk
- Dokumentáltuk az inicializálási folyamatot
- Felsoroltuk az összes funkciót (újrapróbálkozás, nyomon követés, hibák)
- SDK hivatkozási linket adtunk hozzá

#### Cell 8 (Batch bemutató)
- Kibővítettük a magyarázatot arról, hogy mit várhatunk
- Hibaelhárítási szekciót adtunk hozzá
- CLI parancsokat adtunk a hibakereséshez
- Jobban formázott kimeneti megjelenítést készítettünk

### 3. `Workshop/notebooks/session06_README.md` (Új fájl)

**Átfogó dokumentációt készítettünk, amely tartalmazza:**

1. **Áttekintés**: Architektúra diagram és komponens magyarázat
2. **SDK integráció**: Kódpéldák hivatalos minták alapján
3. **Előfeltételek**: Lépésről lépésre beállítási útmutató
4. **Használat**: Hogyan futtassuk és testre szabjuk a jegyzetfüzetet
5. **Modell aliasok**: Hardver-optimalizált változatok magyarázata
6. **Hibaelhárítás**: Gyakori problémák és megoldások
7. **Kiterjesztés**: Hogyan adjunk hozzá szándékokat, modelleket és egyedi logikát
8. **Teljesítmény tippek**: Legjobb gyakorlatok a termelési használathoz
9. **Erőforrások**: Hivatkozások hivatalos dokumentációkra és közösségre

## SDK minták megvalósítása

### Hivatalos minta (Foundry Local dokumentációból)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Saját megvalósítás (workshop_utils-ban)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Előnyeink:**
- ✅ Pontosan követi a hivatalos SDK mintát
- ✅ Gyorsítótárat ad hozzá az ismételt inicializálás elkerülésére
- ✅ Újrapróbálkozási logikát tartalmaz a termelési robusztusság érdekében
- ✅ Támogatja a tokenhasználat nyomon követését
- ✅ Jobb hibaüzeneteket biztosít
- ✅ Kompatibilis marad a hivatalos példákkal

## Modellkatalógus változások

### Korábban
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Utána
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Ok:** Lecseréltük a 'gpt-oss-20b'-t (nem szabványos alias) 'phi-3.5-mini'-re (hivatalos Foundry Local alias).

## Függőségek

### Frissített requirements.txt

A Workshop requirements.txt már tartalmazza:
```
foundry-local-sdk
openai>=1.30.0
```

Ezek az egyetlen szükséges csomagok a Foundry Local integrációhoz.

## A frissítések tesztelése

### 1. Ellenőrizze, hogy a Foundry Local fut-e

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Ellenőrizze az elérhető modelleket

```bash
foundry model ls
```

Győződjön meg arról, hogy ezek a modellek elérhetők vagy automatikusan letöltődnek:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Futtassa a jegyzetfüzetet

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Vagy nyissa meg VS Code-ban, és futtassa az összes cellát.

### 4. Várható viselkedés

**Cell 1 (Telepítés):** Sikeresen telepíti a csomagokat  
**Cell 2 (Beállítás):** Nincs hiba, az importálás működik  
**Cell 3 (Ellenőrzés):** ✓ jelenik meg a modell listával  
**Cell 4 (Szándék teszt):** Megjeleníti a szándék felismerési eredményeket  
**Cell 5 (Útválasztó):** ✓ Útválasztási függvény készen áll  
**Cell 6 (Végrehajtás):** Útválasztja a promptokat a modellekhez, megjeleníti az eredményeket  

### 5. Kapcsolati hibák hibaelhárítása

Ha `APIConnectionError: Connection error` hibát lát:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Környezeti változók

Az alábbi környezeti változók támogatottak:

| Változó | Alapértelmezett | Leírás |
|---------|----------------|--------|
| `SHOW_USAGE` | `0` | Állítsa `1`-re a tokenhasználat nyomtatásához |
| `RETRY_ON_FAIL` | `1` | Újrapróbálkozási logika engedélyezése |
| `RETRY_BACKOFF` | `1.0` | Kezdeti újrapróbálkozási késleltetés (másodperc) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Szolgáltatás végpontjának felülírása |

### Használati példák

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migráció régi mintáról

Ha meglévő kódja közvetlen API hívásokat használ, itt van, hogyan migrálhat:

### Korábban (Közvetlen API)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### Utána (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Migráció előnyei
- ✅ Automatikus szolgáltatáskezelés
- ✅ Modell alias feloldás
- ✅ Hardver optimalizáció kiválasztása
- ✅ Jobb hibakezelés
- ✅ OpenAI SDK kompatibilitás
- ✅ Streaming támogatás

## Referenciák

### Hivatalos dokumentáció
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK forrás**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI referenciák**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Hibaelhárítás**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop erőforrások
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop segédprogramok**: `Workshop/samples/workshop_utils.py`
- **Minta jegyzetfüzet**: `Workshop/notebooks/session06_models_router.ipynb`

### Közösség
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub hibák**: https://github.com/microsoft/Foundry-Local/issues

## Következő lépések

1. **Változások áttekintése**: Olvassa át a frissített fájlokat  
2. **Jegyzetfüzet tesztelése**: Futtassa a session06_models_router.ipynb fájlt  
3. **SDK ellenőrzése**: Győződjön meg arról, hogy a foundry-local-sdk telepítve van  
4. **Szolgáltatás ellenőrzése**: Győződjön meg arról, hogy a Foundry Local fut  
5. **Dokumentáció felfedezése**: Olvassa el az új session06_README.md fájlt  

## Összefoglaló

Ezek a frissítések biztosítják, hogy a Workshop anyagai pontosan kövessék a **hivatalos Foundry Local SDK mintákat**, ahogyan az a GitHub repóban dokumentálva van. Minden kódpélda, dokumentáció és segédprogram mostantól igazodik a Microsoft által ajánlott legjobb gyakorlatokhoz a helyi AI modell telepítéshez.

A változások javítják:
- ✅ **Pontosság**: Hivatalos SDK minták használata  
- ✅ **Dokumentáció**: Átfogó magyarázatok és példák  
- ✅ **Hibakezelés**: Jobb üzenetek és hibaelhárítási útmutató  
- ✅ **Karbantarthatóság**: Hivatalos konvenciók követése  
- ✅ **Felhasználói élmény**: Érthetőbb utasítások és hibakeresési segítség  

---

**Frissítve:** 2025. október 8.  
**SDK verzió:** foundry-local-sdk (legújabb)  
**Workshop ág:** Reactor

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.