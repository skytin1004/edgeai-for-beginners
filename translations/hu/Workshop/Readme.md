<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "48d0fb38be925084a6ebd957d4b045e5",
  "translation_date": "2025-10-09T21:25:16+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "hu"
}
-->
# EdgeAI kezdőknek - Workshop

> **Gyakorlati tanulási útmutató a gyártásra kész Edge AI alkalmazások fejlesztéséhez**
>
> Sajátítsd el a helyi AI telepítés alapjait a Microsoft Foundry Local segítségével, az első chat-válaszadástól a többügynökös koordinációig, 6 egymásra épülő szekcióban.

---

## 🎯 Bevezetés

Üdvözlünk az **EdgeAI kezdőknek Workshopon** - ez egy gyakorlati útmutató intelligens alkalmazások fejlesztéséhez, amelyek teljes mértékben helyi hardveren futnak. Ez a workshop az elméleti Edge AI koncepciókat valós készségekké alakítja át, egyre nehezedő gyakorlatokon keresztül, a Microsoft Foundry Local és Kis Nyelvi Modellek (SLM-ek) használatával.

### Miért érdemes részt venni ezen a workshopon?

**Az Edge AI forradalma megérkezett**

Világszerte egyre több szervezet tér át a felhőalapú AI-ról az edge computingra három kulcsfontosságú okból:

1. **Adatvédelem és megfelelőség** - Érzékeny adatok helyi feldolgozása felhőbe történő továbbítás nélkül (HIPAA, GDPR, pénzügyi szabályozások)
2. **Teljesítmény** - Hálózati késleltetés kiküszöbölése (50-500 ms helyi vs 500-2000 ms felhő körüli utazás)
3. **Költségkontroll** - Tokenenkénti API költségek megszüntetése és skálázás felhő költségek nélkül

**De az Edge AI más**

Az AI helyi futtatása új készségeket igényel:
- Modellek kiválasztása és optimalizálása erőforrás-korlátokhoz
- Helyi szolgáltatáskezelés és hardveres gyorsítás
- Prompt tervezés kisebb modellekhez
- Gyártási telepítési minták edge eszközökhöz

**Ez a workshop ezeket a készségeket adja át**

6 fókuszált szekcióban (~3 óra összesen) haladhatsz a "Hello World"-től a gyártásra kész többügynökös rendszerek telepítéséig - mindezt helyben, a saját gépeden futtatva.

---

## 📚 Tanulási célok

A workshop elvégzése után képes leszel:

### Alapvető kompetenciák
1. **Helyi AI szolgáltatások telepítése és kezelése**
   - Microsoft Foundry Local telepítése és konfigurálása
   - Megfelelő modellek kiválasztása edge telepítéshez
   - Modell életciklusának kezelése (letöltés, betöltés, gyorsítótárazás)
   - Erőforrás-felhasználás figyelése és teljesítmény optimalizálása

2. **AI-alapú alkalmazások fejlesztése**
   - OpenAI-kompatibilis chat-válaszok helyi implementálása
   - Hatékony promptok tervezése Kis Nyelvi Modellekhez
   - Streaming válaszok kezelése a jobb felhasználói élmény érdekében
   - Helyi modellek integrálása meglévő alkalmazásokba

3. **RAG (Retrieval Augmented Generation) rendszerek létrehozása**
   - Szemantikus keresés építése embeddingekkel
   - LLM válaszok megalapozása domain-specifikus tudásban
   - RAG minőségének értékelése ipari szabvány metrikákkal
   - Prototípusból gyártásra való skálázás

4. **Modell teljesítményének optimalizálása**
   - Több modell benchmarkolása az adott felhasználási esethez
   - Késleltetés, áteresztőképesség és első token idő mérése
   - Optimális modellek kiválasztása sebesség/minőség kompromisszumok alapján
   - SLM és LLM közötti kompromisszumok összehasonlítása valós helyzetekben

5. **Többügynökös rendszerek koordinálása**
   - Speciális ügynökök tervezése különböző feladatokhoz
   - Ügynök memória és kontextuskezelés implementálása
   - Ügynökök koordinálása összetett munkafolyamatokban
   - Kérések intelligens irányítása több modell között

6. **Gyártásra kész megoldások telepítése**
   - Hibakezelés és újrapróbálkozási logika implementálása
   - Tokenhasználat és rendszererőforrások figyelése
   - Skálázható architektúrák építése modell-eszköz mintákkal
   - Migrációs utak tervezése edge-ről hibrid (edge + felhő) környezetbe

---

## 🎓 Tanulási eredmények

### Amit meg fogsz építeni

A workshop végére a következőket fogod elkészíteni:

| Szekció | Eredmény | Bemutatott készségek |
|---------|----------|-----------------------|
| **1** | Chat alkalmazás streaminggel | Szolgáltatás beállítása, alapvető válaszok, streaming UX |
| **2** | RAG rendszer értékeléssel | Embeddingek, szemantikus keresés, minőségi metrikák |
| **3** | Többmodell benchmark csomag | Teljesítménymérés, modell összehasonlítás |
| **4** | SLM vs LLM összehasonlító | Kompromisszum elemzés, optimalizálási stratégiák |
| **5** | Többügynökös koordinátor | Ügynök tervezés, memória kezelés, koordináció |
| **6** | Intelligens irányítórendszer | Szándékfelismerés, modell kiválasztás, skálázhatóság |

### Kompetencia mátrix

| Készségszint | Szekció 1-2 | Szekció 3-4 | Szekció 5-6 |
|--------------|-------------|-------------|-------------|
| **Kezdő** | ✅ Beállítás és alapok | ⚠️ Kihívást jelentő | ❌ Túl haladó |
| **Középhaladó** | ✅ Gyors áttekintés | ✅ Alapvető tanulás | ⚠️ Kihívás |
| **Haladó** | ✅ Könnyedén | ✅ Finomhangolás | ✅ Gyártási minták |

### Karrierre kész készségek

**A workshop elvégzése után képes leszel:**

✅ **Adatvédelmi szempontból elsődleges alkalmazások építése**
- Egészségügyi alkalmazások, amelyek helyben kezelik a PHI/PII adatokat
- Pénzügyi szolgáltatások megfelelőségi követelményekkel
- Kormányzati rendszerek adat-szuverenitási igényekkel

✅ **Optimalizálás edge környezetekhez**
- Korlátozott erőforrásokkal rendelkező IoT eszközök
- Offline-első mobilalkalmazások
- Alacsony késleltetésű valós idejű rendszerek

✅ **Intelligens architektúrák tervezése**
- Többügynökös rendszerek összetett munkafolyamatokhoz
- Hibrid edge-felhő telepítések
- Költséghatékony AI infrastruktúra

✅ **Edge AI kezdeményezések vezetése**
- Edge AI megvalósíthatóságának értékelése projektekhez
- Megfelelő modellek és keretrendszerek kiválasztása
- Skálázható helyi AI megoldások tervezése

---

## 🗺️ Workshop felépítése

### Szekciók áttekintése (6 szekció × 30 perc = 3 óra)

| Szekció | Téma | Fókusz | Időtartam |
|---------|------|--------|-----------|
| **1** | Bevezetés a Foundry Local használatába | Telepítés, érvényesítés, első válaszok | 30 perc |
| **2** | AI megoldások építése RAG-gal | Prompt tervezés, embeddingek, értékelés | 30 perc |
| **3** | Nyílt forráskódú modellek | Modell felfedezés, benchmarkolás, kiválasztás | 30 perc |
| **4** | Legmodernebb modellek | SLM vs LLM, optimalizálás, keretrendszerek | 30 perc |
| **5** | AI-alapú ügynökök | Ügynök tervezés, koordináció, memória | 30 perc |
| **6** | Modellek mint eszközök | Irányítás, láncolás, skálázási stratégiák | 30 perc |

---

## 🚀 Gyors kezdés

### Előfeltételek

**Rendszerkövetelmények:**
- **OS**: Windows 10/11, macOS 11+, vagy Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, ajánlott 16GB+
- **Tárhely**: Legalább 10GB szabad hely a modellekhez
- **CPU**: Modern processzor AVX2 támogatással
- **GPU** (opcionális): CUDA-kompatibilis vagy Qualcomm NPU gyorsításhoz

**Szoftverkövetelmények:**
- **Python 3.8+** ([Letöltés](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Telepítési útmutató](../../../Workshop))
- **Git** ([Letöltés](https://git-scm.com/downloads))
- **Visual Studio Code** (ajánlott) ([Letöltés](https://code.visualstudio.com/))

### Beállítás 3 lépésben

#### 1. Foundry Local telepítése

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Telepítés ellenőrzése:**
```bash
foundry --version
foundry service status
```

#### 2. Tárhely klónozása és függőségek telepítése

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Futtasd az első mintát

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples/session01
python chat_bootstrap.py "What is edge AI?"
```

**✅ Siker!** Egy streaming választ kell látnod az edge AI-ról.

---

## 📦 Workshop források

### Python minták

Fokozatos, gyakorlati példák, amelyek bemutatják az egyes koncepciókat:

| Szekció | Minta | Leírás | Futtatási idő |
|---------|-------|--------|---------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Alap és streaming chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG embeddingekkel | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG minőségértékelés | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Többmodell benchmarkolás | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM összehasonlítás | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Többügynökös rendszer | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Szándék-alapú irányítás | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Többlépéses folyamat | ~60s |

### Jupyter Notebookok

Interaktív felfedezés magyarázatokkal és vizualizációkkal:

| Szekció | Notebook | Leírás | Nehézség |
|---------|----------|--------|----------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Chat alapok és streaming | ⭐ Kezdő |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | RAG rendszer építése | ⭐⭐ Középhaladó |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | RAG minőség értékelése | ⭐⭐ Középhaladó |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Modell benchmarkolás | ⭐⭐ Középhaladó |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Modell összehasonlítás | ⭐⭐ Középhaladó |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Ügynökök koordinációja | ⭐⭐⭐ Haladó |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Szándékirányítás | ⭐⭐⭐ Haladó |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Folyamatok koordinációja | ⭐⭐⭐ Haladó |

### Dokumentáció

Átfogó útmutatók és referenciák:

| Dokumentum | Leírás | Mikor használd |
|------------|--------|----------------|
| [QUICK_START.md](./QUICK_START.md) | Gyors beállítási útmutató | Kezdéskor |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Parancs- és API-gyorsreferencia | Gyors válaszokhoz |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK minták és példák | Kódíráskor |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Környezeti változók útmutatója | Minták konfigurálásakor |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Legújabb minta fejlesztések | Változások megértése |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Migrációs útmutató | Kód frissítésekor |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Gyakori problémák és megoldások | Hibák elhárításakor |

---

## 🎓 Tanulási útmutató ajánlások

### Kezdőknek (3-4 óra)
1. ✅ 1. szekció: Kezdés (fókusz a beállításon és az alapvető chat-en)
2. ✅ 2. szekció: RAG alapok (kezdetben hagyd ki az értékelést)
3. ✅ 3. szekció: Egyszerű benchmarkolás (csak 2 modell)
4. ⏭️ Hagyd ki az 4-6. szekciókat egyelőre
5. 🔄 Térj vissza az 4-6. szekciókra, miután elkészítetted az első alkalmazást

### Középhaladó fejlesztőknek (3 óra)
1. ⚡ 1. szekció: Gyors beállítás érvényesítése
2. ✅ 2. szekció: Teljes RAG folyamat értékeléssel
3. ✅ 3. szekció: Teljes benchmark csomag
4. ✅ 4. szekció: Modell optimalizálás
5. ✅ 5-6. szekciók: Fókusz az architektúra mintákon

### Haladó szakembereknek (2-3 óra)
1. ⚡ 1-3. szekciók: Gyors áttekintés és érvényesítés
2. ✅ 4. szekció: Optimalizálási mélymerülés
3. ✅ 5. szekció: Többügynökös architektúra
4. ✅ 6. szekció: Gyártási minták és skálázás
5. 🚀 Kiterjesztés: Egyedi irányítási logika és hibrid telepítések építése

---

## Workshop szekciós csomag (Fókuszált 30 perces laborok)

Ha a sűrített 6 szekciós workshop formátumot követed, használd ezeket a dedikált útmutatókat (mindegyik megfelel és kiegészíti a fentebb említett átfogó modul dokumentációkat):

| Workshop szekció | Útmutató | Fő fókusz |
|------------------|----------|-----------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Telepítés, érvényesítés, phi & GPT-OSS-20B futtatása, gyorsítás |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Prompt tervezés, RAG minták, CSV és dokumentum alapú
Minden munkamenet fájl tartalmazza: összefoglalót, tanulási célokat, 30 perces bemutató menetét, kezdő projektet, ellenőrző listát, hibaelhárítást és hivatkozásokat a hivatalos Foundry Local Python SDK-ra.

### Példa szkriptek

Workshop függőségek telepítése (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Ha a Foundry Local szolgáltatást másik (Windows) gépen vagy virtuális gépen futtatod macOS-ről, exportáld az endpointot:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Munkamenet | Szkript(ek) | Leírás |
|------------|-------------|--------|
| 1 | `samples/session01/chat_bootstrap.py` | Szolgáltatás indítása és streaming chat |
| 2 | `samples/session02/rag_pipeline.py` | Minimális RAG (memóriában tárolt beágyazásokkal) |
|   | `samples/session02/rag_eval_ragas.py` | RAG értékelés ragas metrikákkal |
| 3 | `samples/session03/benchmark_oss_models.py` | Több modell késleltetés és áteresztőképesség benchmarking |
| 4 | `samples/session04/model_compare.py` | SLM vs LLM összehasonlítás (késleltetés és mintakimenet) |
| 5 | `samples/session05/agents_orchestrator.py` | Két ügynök kutatás → szerkesztői folyamat |
| 6 | `samples/session06/models_router.py` | Szándékalapú útválasztás bemutató |
|   | `samples/session06/models_pipeline.py` | Többlépéses tervezés/végrehajtás/finomítás lánc |

### Környezeti változók (minden mintához közös)

| Változó | Cél | Példa |
|---------|-----|-------|
| `FOUNDRY_LOCAL_ALIAS` | Alapértelmezett egyetlen modell alias egyszerű mintákhoz | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Kifejezett SLM vs nagyobb modell összehasonlításhoz | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Aliasok vesszővel elválasztott listája benchmarkinghoz | `qwen2.5-0.5b,gemma-2-2b,mistral-7b` |
| `BENCH_ROUNDS` | Benchmark ismétlések modellenként | `3` |
| `BENCH_PROMPT` | Benchmarking során használt prompt | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers beágyazási modell | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Tesztkérdés felülírása RAG pipeline-hoz | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Ügynökök pipeline kérdés felülírása | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Kutatási ügynök modell alias | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Szerkesztő ügynök modell alias (eltérhet) | `gpt-oss-20b` |
| `SHOW_USAGE` | Ha `1`, megjeleníti a tokenhasználatot befejezésenként | `1` |
| `RETRY_ON_FAIL` | Ha `1`, egyszer újrapróbálkozik átmeneti chat hibák esetén | `1` |
| `RETRY_BACKOFF` | Másodpercek várakozási idő újrapróbálkozás előtt | `1.0` |

Ha egy változó nincs beállítva, a szkriptek ésszerű alapértelmezésekre esnek vissza. Egymodelles bemutatókhoz általában csak a `FOUNDRY_LOCAL_ALIAS` szükséges.

### Segédmodul

Minden minta megosztja a `samples/workshop_utils.py` segédprogramot, amely biztosítja:

* Cache-elt `FoundryLocalManager` + OpenAI kliens létrehozását
* `chat_once()` segédprogramot opcionális újrapróbálkozással + használati nyomtatással
* Egyszerű tokenhasználati jelentést (engedélyezhető `SHOW_USAGE=1`-gyel)

Ez csökkenti a duplikációt és kiemeli a legjobb gyakorlatokat a hatékony helyi modell-orchesztrációhoz.

## Opcionális fejlesztések (munkamenetek között)

| Téma | Fejlesztés | Munkamenetek | Környezet / Kapcsoló |
|------|------------|--------------|----------------------|
| Determinizmus | Fixált hőmérséklet + stabil prompt készletek | 1–6 | Állítsd be `temperature=0`, `top_p=1` |
| Tokenhasználat láthatósága | Következetes költség/hatékonyság tanítás | 1–6 | `SHOW_USAGE=1` |
| Első token streaming | Érzékelt késleltetési metrika | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Újrapróbálkozási ellenállás | Átmeneti hidegindítás kezelése | Mind | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Többmodellű ügynökök | Heterogén szerepspecializáció | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptív útválasztás | Szándék + költség heurisztikák | 6 | Bővítsd az útválasztót eszkalációs logikával |
| Vektormemória | Hosszú távú szemantikai visszaemlékezés | 2,5,6 | Integráld FAISS/Chroma beágyazási indexet |
| Nyomkövetés exportálása | Auditálás és értékelés | 2,5,6 | JSON sorok hozzáfűzése lépésenként |
| Minőségi rubrikák | Minőségi követés | 3–6 | Másodlagos pontozási promt |
| Gyors tesztek | Workshop előtti gyors validálás | Mind | `python Workshop/tests/smoke.py` |

### Determinisztikus gyors kezdés

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Várj stabil token számokat ismételt azonos bemenetek esetén.

### RAG értékelés (2. munkamenet)

Használd a `rag_eval_ragas.py` szkriptet válasz relevancia, hitelesség és kontextus pontosság kiszámítására egy apró szintetikus adathalmazon:

```powershell
python samples/session02/rag_eval_ragas.py
```

Bővítsd egy nagyobb JSONL kérdések, kontextusok és igazságok megadásával, majd konvertáld Hugging Face `Dataset`-re.

## CLI parancs pontossági melléklet

A workshop szándékosan csak jelenleg dokumentált / stabil Foundry Local CLI parancsokat használ.

### Hivatkozott stabil parancsok

| Kategória | Parancs | Cél |
|-----------|---------|-----|
| Alap | `foundry --version` | Telepített verzió megjelenítése |
| Alap | `foundry init` | Konfiguráció inicializálása |
| Szolgáltatás | `foundry service start` | Helyi szolgáltatás indítása (ha nem automatikus) |
| Szolgáltatás | `foundry status` | Szolgáltatás állapotának megjelenítése |
| Modellek | `foundry model list` | Katalógus / elérhető modellek listázása |
| Modellek | `foundry model download <alias>` | Modell súlyok letöltése a cache-be |
| Modellek | `foundry model run <alias>` | Modell indítása helyben; kombináld `--prompt`-tal egyetlen futtatáshoz |
| Modellek | `foundry model unload <alias>` / `foundry model stop <alias>` | Modell eltávolítása a memóriából (ha támogatott) |
| Cache | `foundry cache list` | Cache-elt (letöltött) modellek listázása |
| Rendszer | `foundry system info` | Hardver és gyorsítási képességek pillanatképe |
| Rendszer | `foundry system gpu-info` | GPU diagnosztikai információ |
| Konfig | `foundry config list` | Jelenlegi konfigurációs értékek megjelenítése |
| Konfig | `foundry config set <key> <value>` | Konfiguráció frissítése |

### Egyszeri prompt minta

A `model chat` alparancs helyett használd:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Ez végrehajt egyetlen prompt/válasz ciklust, majd kilép.

### Eltávolított / kerülendő minták

| Elavult / Nem dokumentált | Helyettesítés / Útmutatás |
|---------------------------|--------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Használj egyszerű `foundry model list`-et + legutóbbi aktivitás / naplók |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Használj benchmark Python szkriptet + OS eszközöket (Feladatkezelő / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking és telemetria

- Késleltetés, p95, tokenek/másodperc: `samples/session03/benchmark_oss_models.py`
- Első token késleltetés (streaming): állítsd be `BENCH_STREAM=1`-et
- Erőforrás-használat: OS monitorok (Feladatkezelő, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Amint új CLI telemetria parancsok stabilizálódnak, minimális szerkesztéssel beépíthetők a munkamenet markdownokba.

### Automatikus lint őr

Egy automatikus linter megakadályozza az elavult CLI minták visszavezetését a markdown fájlok kódkerítéseibe:

Szkript: `Workshop/scripts/lint_markdown_cli.py`

Elavult minták blokkolva vannak a kódkerítésekben.

Ajánlott helyettesítések:
| Elavult | Helyettesítés |
|---------|--------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmark szkript + rendszereszközök |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Futtatás helyben:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` minden push és PR esetén fut.

Opcionális pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Gyors CLI → SDK migrációs táblázat

| Feladat | CLI egy soros | SDK (Python) megfelelője | Megjegyzések |
|---------|---------------|--------------------------|--------------|
| Modell futtatása egyszer (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | Az SDK automatikusan inicializálja a szolgáltatást és a cache-t |
| Modell letöltése (cache) | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | A manager a legjobb változatot választja, ha az alias több buildhez is tartozik |
| Katalógus listázása | `foundry model list` | `# use manager for each alias or maintain known list` | A CLI aggregál; az SDK jelenleg aliasonkénti inicializálást igényel |
| Cache-elt modellek listázása | `foundry cache list` | `manager.list_cached_models()` | Manager inicializálása után (bármely alias) |
| GPU gyorsítás engedélyezése | `foundry config set compute.onnx.enable_gpu true` | `# CLI action; SDK assumes config already applied` | A konfiguráció külső mellékhatás |
| Endpoint URL lekérése | (implicit) | `manager.endpoint` | OpenAI-kompatibilis kliens létrehozásához használható |
| Modell melegítése | `foundry model run <alias>` majd első prompt | `chat_once(alias, messages=[...])` (utility) | A segédprogramok kezelik a kezdeti hideg késleltetési melegítést |
| Késleltetés mérése | `python benchmark_oss_models.py` | `import benchmark_oss_models` (vagy új exportáló szkript) | A szkriptet preferáld a következetes metrikákhoz |
| Modell leállítása / eltávolítása | `foundry model unload <alias>` | (Nem elérhető – szolgáltatás / folyamat újraindítása) | Általában nem szükséges a workshop folyamathoz |
| Tokenhasználat lekérése | (kimenet megtekintése) | `resp.usage.total_tokens` | Ha a backend visszaad egy usage objektumot |

## Benchmark Markdown exportálás

Használd a `Workshop/scripts/export_benchmark_markdown.py` szkriptet friss benchmark futtatására (ugyanaz a logika, mint a `samples/session03/benchmark_oss_models.py`-ben), és GitHub-barát Markdown táblázat + nyers JSON kibocsátására.

### Példa

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Generált fájlok:
| Fájl | Tartalom |
|------|----------|
| `benchmark_report.md` | Markdown táblázat + értelmezési tippek |
| `benchmark_report.json` | Nyers metrikák tömbje (összehasonlításhoz / trendkövetéshez) |

Állítsd be `BENCH_STREAM=1`-et a környezetben, hogy az első token késleltetést is tartalmazza, ha támogatott.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.