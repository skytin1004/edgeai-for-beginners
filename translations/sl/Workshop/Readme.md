<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "48d0fb38be925084a6ebd957d4b045e5",
  "translation_date": "2025-10-08T12:08:54+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "sl"
}
-->
# EdgeAI za začetnike - delavnica

> **Praktična učna pot za gradnjo produkcijsko pripravljenih Edge AI aplikacij**
>
> Obvladajte lokalno uvajanje umetne inteligence z Microsoft Foundry Local, od prvega klepeta do orkestracije več agentov v 6 naprednih seansah.

---

## 🎯 Uvod

Dobrodošli v **delavnici EdgeAI za začetnike** - vašem praktičnem vodniku za gradnjo inteligentnih aplikacij, ki delujejo izključno na lokalni strojni opremi. Ta delavnica pretvori teoretične koncepte Edge AI v praktične veščine prek postopno zahtevnejših vaj z uporabo Microsoft Foundry Local in majhnih jezikovnih modelov (SLM).

### Zakaj ta delavnica?

**Revolucija Edge AI je tukaj**

Organizacije po vsem svetu prehajajo od AI, ki temelji na oblaku, k robnemu računalništvu iz treh ključnih razlogov:

1. **Zasebnost in skladnost** - Obdelava občutljivih podatkov lokalno brez prenosa v oblak (HIPAA, GDPR, finančne regulative)
2. **Zmogljivost** - Odprava omrežne zakasnitve (50-500 ms lokalno proti 500-2000 ms oblačnega prenosa)
3. **Nadzor stroškov** - Odprava stroškov na žeton API in skaliranje brez oblačnih stroškov

**Toda Edge AI je drugačen**

Zagon AI na lokalni ravni zahteva nove veščine:
- Izbor in optimizacija modelov za omejene vire
- Upravljanje lokalnih storitev in pospeševanje strojne opreme
- Oblikovanje pozivov za manjše modele
- Vzorci uvajanja v produkcijo za robne naprave

**Ta delavnica prinaša te veščine**

V 6 osredotočenih seansah (~3 ure skupaj) boste napredovali od "Hello World" do uvajanja produkcijsko pripravljenih sistemov z več agenti - vse lokalno na vašem računalniku.

---

## 📚 Cilji učenja

Z dokončanjem te delavnice boste sposobni:

### Osnovne kompetence
1. **Uvajanje in upravljanje lokalnih AI storitev**
   - Namestitev in konfiguracija Microsoft Foundry Local
   - Izbor ustreznih modelov za robno uvajanje
   - Upravljanje življenjskega cikla modelov (prenos, nalaganje, predpomnjenje)
   - Spremljanje uporabe virov in optimizacija zmogljivosti

2. **Gradnja aplikacij, ki temeljijo na AI**
   - Implementacija klepetov, združljivih z OpenAI, lokalno
   - Oblikovanje učinkovitih pozivov za majhne jezikovne modele
   - Upravljanje pretočnih odgovorov za boljšo uporabniško izkušnjo
   - Integracija lokalnih modelov v obstoječe aplikacije

3. **Ustvarjanje sistemov RAG (Retrieval Augmented Generation)**
   - Gradnja semantičnega iskanja z vdelavami
   - Utemeljitev odgovorov LLM v specifičnem znanju
   - Ocena kakovosti RAG z industrijskimi standardnimi metrikami
   - Skaliranje od prototipa do produkcije

4. **Optimizacija zmogljivosti modelov**
   - Primerjava več modelov za vaš primer uporabe
   - Merjenje zakasnitve, prepustnosti in časa prvega žetona
   - Izbor optimalnih modelov na podlagi kompromisov med hitrostjo in kakovostjo
   - Primerjava kompromisov med SLM in LLM v resničnih scenarijih

5. **Orkestracija sistemov z več agenti**
   - Oblikovanje specializiranih agentov za različne naloge
   - Implementacija spomina agentov in upravljanje konteksta
   - Koordinacija agentov v kompleksnih delovnih tokovih
   - Pametno usmerjanje zahtev med več modeli

6. **Uvajanje produkcijsko pripravljenih rešitev**
   - Implementacija obravnave napak in logike ponovnih poskusov
   - Spremljanje uporabe žetonov in sistemskih virov
   - Gradnja skalabilnih arhitektur z vzorci modelov kot orodij
   - Načrtovanje migracijskih poti od roba do hibrida (rob + oblak)

---

## 🎓 Rezultati učenja

### Kaj boste zgradili

Do konca te delavnice boste ustvarili:

| Seansa | Izdelek | Prikazane veščine |
|--------|---------|-------------------|
| **1** | Klepetalna aplikacija s pretočnim odzivom | Nastavitev storitve, osnovni klepeti, pretočna UX |
| **2** | RAG sistem z ocenjevanjem | Vdelave, semantično iskanje, kakovostne metrike |
| **3** | Suite za primerjavo več modelov | Merjenje zmogljivosti, primerjava modelov |
| **4** | Primerjalnik SLM proti LLM | Analiza kompromisov, strategije optimizacije |
| **5** | Orkestrator z več agenti | Oblikovanje agentov, upravljanje spomina, koordinacija |
| **6** | Sistem za inteligentno usmerjanje | Zaznavanje namena, izbor modelov, skalabilnost |

### Matrika kompetenc

| Raven veščin | Seansa 1-2 | Seansa 3-4 | Seansa 5-6 |
|--------------|------------|------------|------------|
| **Začetnik** | ✅ Nastavitev in osnove | ⚠️ Zahtevno | ❌ Preveč napredno |
| **Srednje izkušen** | ✅ Hiter pregled | ✅ Osnovno učenje | ⚠️ Cilji raztezanja |
| **Napreden** | ✅ Hitro skozi | ✅ Izpopolnjevanje | ✅ Vzorci za produkcijo |

### Karierne veščine

**Po tej delavnici boste pripravljeni na:**

✅ **Gradnjo aplikacij, ki dajejo prednost zasebnosti**
- Zdravstvene aplikacije, ki lokalno obdelujejo PHI/PII
- Finančne storitve z zahtevami skladnosti
- Vladni sistemi z zahtevami po suverenosti podatkov

✅ **Optimizacijo za robna okolja**
- IoT naprave z omejenimi viri
- Mobilne aplikacije, ki delujejo brez povezave
- Sistemi v realnem času z nizko zakasnitvijo

✅ **Oblikovanje inteligentnih arhitektur**
- Sistemi z več agenti za kompleksne delovne tokove
- Hibridne robno-oblačne uvajanja
- Stroškovno optimizirana AI infrastruktura

✅ **Vodenje Edge AI pobud**
- Ocena izvedljivosti Edge AI za projekte
- Izbor ustreznih modelov in ogrodij
- Arhitektura skalabilnih lokalnih AI rešitev

---

## 🗺️ Struktura delavnice

### Pregled seans (6 seans × 30 minut = 3 ure)

| Seansa | Tema | Fokus | Trajanje |
|--------|------|-------|---------|
| **1** | Začetek z Foundry Local | Namestitev, validacija, prvi klepeti | 30 min |
| **2** | Gradnja AI rešitev z RAG | Oblikovanje pozivov, vdelave, ocenjevanje | 30 min |
| **3** | Odprtokodni modeli | Odkritje modelov, primerjava, izbor | 30 min |
| **4** | Napredni modeli | SLM proti LLM, optimizacija, ogrodja | 30 min |
| **5** | Agenti, ki temeljijo na AI | Oblikovanje agentov, orkestracija, spomin | 30 min |
| **6** | Modeli kot orodja | Usmerjanje, povezovanje, strategije skaliranja | 30 min |

---

## 🚀 Hiter začetek

### Predpogoji

**Sistemske zahteve:**
- **OS**: Windows 10/11, macOS 11+ ali Linux (Ubuntu 20.04+)
- **RAM**: najmanj 8 GB, priporočljivo 16 GB+
- **Shramba**: 10 GB+ prostega prostora za modele
- **CPU**: sodoben procesor s podporo za AVX2
- **GPU** (neobvezno): CUDA-kompatibilen ali Qualcomm NPU za pospeševanje

**Programske zahteve:**
- **Python 3.8+** ([Prenesi](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Navodila za namestitev](../../../Workshop))
- **Git** ([Prenesi](https://git-scm.com/downloads))
- **Visual Studio Code** (priporočeno) ([Prenesi](https://code.visualstudio.com/))

### Nastavitev v 3 korakih

#### 1. Namestitev Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Preverjanje namestitve:**
```bash
foundry --version
foundry service status
```

#### 2. Kloniranje repozitorija in namestitev odvisnosti

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

#### 3. Zagon prvega vzorca

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples/session01
python chat_bootstrap.py "What is edge AI?"
```

**✅ Uspešno!** Videti bi morali pretočni odgovor o Edge AI.

---

## 📦 Viri delavnice

### Python vzorci

Postopni praktični primeri, ki prikazujejo vsak koncept:

| Seansa | Vzorec | Opis | Čas izvajanja |
|--------|-------|------|--------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Osnovni in pretočni klepet | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG z vdelavami | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Ocena kakovosti RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Primerjava več modelov | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Primerjava SLM proti LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Sistem z več agenti | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Usmerjanje na podlagi namena | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Večstopenjska povezava | ~60s |

### Jupyter zvezki

Interaktivno raziskovanje z razlagami in vizualizacijami:

| Seansa | Zvezek | Opis | Težavnost |
|--------|-------|------|----------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Osnove klepeta in pretočni odzivi | ⭐ Začetnik |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Gradnja sistema RAG | ⭐⭐ Srednje izkušen |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Ocena kakovosti RAG | ⭐⭐ Srednje izkušen |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Primerjava modelov | ⭐⭐ Srednje izkušen |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Primerjava modelov | ⭐⭐ Srednje izkušen |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orkestracija agentov | ⭐⭐⭐ Napreden |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Usmerjanje na podlagi namena | ⭐⭐⭐ Napreden |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orkestracija povezave | ⭐⭐⭐ Napreden |

### Dokumentacija

Celoviti vodiči in reference:

| Dokument | Opis | Uporaba |
|----------|------|--------|
| [QUICK_START.md](./QUICK_START.md) | Vodnik za hitro nastavitev | Začetek od začetka |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Kratka navodila za ukaze in API | Potrebujete hitre odgovore |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Vzorci SDK in primeri | Pisanje kode |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Vodnik za konfiguracijo okolja | Konfiguracija vzorcev |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Najnovejše izboljšave vzorcev | Razumevanje sprememb |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Vodnik za migracijo | Nadgradnja kode |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Pogoste težave in rešitve | Odpravljanje težav |

---

## 🎓 Priporočila za učne poti

### Za začetnike (3-4 ure)
1. ✅ Seansa 1: Začetek (osredotočite se na nastavitev in osnovni klepet)
2. ✅ Seansa 2: Osnove RAG (sprva preskočite ocenjevanje)
3. ✅ Seansa 3: Enostavna primerjava (samo 2 modela)
4. ⏭️ Za zdaj preskočite seanse 4-6
5. 🔄 Vrnite se k seansam 4-6 po gradnji prve aplikacije

### Za srednje izkušene razvijalce (3 ure)
1. ⚡ Seansa 1: Hitra validacija nastavitve
2. ✅ Seansa 2: Popolna RAG povezava z ocenjevanjem
3. ✅ Seansa 3: Celovita primerjava modelov
4. ✅ Seansa 4: Optimizacija modelov
5. ✅ Seanse 5-6: Osredotočite se na arhitekturne vzorce

### Za napredne praktike (2-3 ure)
1. ⚡ Seanse 1-3: Hiter pregled in validacija
2. ✅ Seansa 4: Poglobljena optimizacija
3. ✅ Seansa 5: Arhitektura z več agenti
4. ✅ Seansa 6: Vzorci za produkcijo in skaliranje
5. 🚀 Razširite: Zgradite logiko za prilagojeno usmerjanje in hibridne uvajanja

---

## Paket delavnic (osredotočeni 30-minutni laboratoriji)

Če sledite strnjeni obliki delavnice s 6 seansami, uporabite te namenske vodiče (vsak se ujema in dopolnjuje širše module zgoraj):

| Seansa delavnice | Vodnik | Osrednji fokus |
|------------------|-------|---------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Namestitev, validacija, zagon phi & GPT-OSS-20B, pospeševanje |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Oblikovanje pozivov, vzorci RAG, utemeljitev CSV in dokumentov, migracija |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integracija Hugging Face, primerjava, izbor modelov |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM proti LLM, WebGPU, Chainlit RAG, pospeševanje ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Vloge agentov, spomin, orodja, orkestracija |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Usmerjanje, povezovanje, skaliranje poti do Azure |
Vsaka datoteka seje vključuje: povzetek, učne cilje, 30-minutni potek demonstracije, začetni projekt, kontrolni seznam za validacijo, odpravljanje težav in reference na uradni Foundry Local Python SDK.

### Vzorčni skripti

Namestitev odvisnosti delavnice (Windows):

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

Če se storitev Foundry Local izvaja na drugi (Windows) napravi ali VM iz macOS, izvozite končno točko:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Seja | Skript(i) | Opis |
|------|-----------|------|
| 1 | `samples/session01/chat_bootstrap.py` | Zagon storitve & pretakanje klepeta |
| 2 | `samples/session02/rag_pipeline.py` | Minimalni RAG (v pomnilniku vdelane vsebine) |
|   | `samples/session02/rag_eval_ragas.py` | Ocena RAG z metrikami ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Primerjava več modelov glede na zakasnitev & prepustnost |
| 4 | `samples/session04/model_compare.py` | Primerjava SLM in LLM (zakasnitev & vzorčni izhod) |
| 5 | `samples/session05/agents_orchestrator.py` | Raziskovalni → uredniški proces z dvema agentoma |
| 6 | `samples/session06/models_router.py` | Demonstracija usmerjanja na podlagi namena |
|   | `samples/session06/models_pipeline.py` | Veriga načrtovanja/izvajanja/izboljšanja v več korakih |

### Spremenljivke okolja (skupne za vzorce)

| Spremenljivka | Namen | Primer |
|---------------|-------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Privzeti vzdevek enega modela za osnovne vzorce | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Izrecna primerjava SLM proti večjemu modelu | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Seznam vzdevkov modelov za primerjavo | `qwen2.5-0.5b,gemma-2-2b,mistral-7b` |
| `BENCH_ROUNDS` | Število ponovitev primerjave na model | `3` |
| `BENCH_PROMPT` | Poziv, uporabljen pri primerjavi | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Model za vdelavo stavkov | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Prepis testnega vprašanja za RAG proces | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Prepis vprašanja za proces agentov | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Vzdevek modela za raziskovalnega agenta | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Vzdevek modela za uredniškega agenta (lahko se razlikuje) | `gpt-oss-20b` |
| `SHOW_USAGE` | Če je `1`, izpiše uporabo žetonov na dokončanje | `1` |
| `RETRY_ON_FAIL` | Če je `1`, poskusi znova ob začasnih napakah klepeta | `1` |
| `RETRY_BACKOFF` | Čas v sekundah za čakanje pred ponovnim poskusom | `1.0` |

Če spremenljivka ni nastavljena, skripti privzeto uporabijo smiselne vrednosti. Za demonstracije z enim modelom običajno potrebujete le `FOUNDRY_LOCAL_ALIAS`.

### Pomožni modul

Vsi vzorci zdaj uporabljajo skupni pripomoček `samples/workshop_utils.py`, ki omogoča:

* Ustvarjanje predpomnjenega `FoundryLocalManager` + OpenAI odjemalca
* Pomočnika `chat_once()` z možnostjo ponovnega poskusa + prikaz uporabe
* Preprosto poročanje o uporabi žetonov (omogočite z `SHOW_USAGE=1`)

To zmanjšuje podvajanje in poudarja najboljše prakse za učinkovito lokalno orkestracijo modelov.

## Izbirne izboljšave (med sejami)

| Tema | Izboljšava | Seje | Okolje / Preklop |
|------|------------|------|------------------|
| Determinizem | Fiksna temperatura + stabilni nabori pozivov | 1–6 | Nastavite `temperature=0`, `top_p=1` |
| Vidnost uporabe žetonov | Dosledno poučevanje o stroških/učinkovitosti | 1–6 | `SHOW_USAGE=1` |
| Pretakanje prvega žetona | Meritev zaznane zakasnitve | 1,3,4,6 | `BENCH_STREAM=1` (primerjava) |
| Odpornost na ponovne poskuse | Obvladovanje začasnih težav ob zagonu | Vse | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Večmodelni agenti | Heterogena specializacija vlog | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Prilagodljivo usmerjanje | Namenska + stroškovna heuristika | 6 | Razširite usmerjevalnik z logiko eskalacije |
| Vektorski pomnilnik | Dolgoročni semantični spomin | 2,5,6 | Integrirajte FAISS/Chroma indeks vdelave |
| Izvoz sledi | Revizija & ocenjevanje | 2,5,6 | Dodajte JSON vrstice na korak |
| Kakovostne rubrike | Kvalitativno sledenje | 3–6 | Sekundarni pozivi za ocenjevanje |
| Hitri testi | Hitro preverjanje pred delavnico | Vse | `python Workshop/tests/smoke.py` |

### Deterministični hitri začetek

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Pričakujte stabilno število žetonov pri ponavljajočih se identičnih vnosih.

### Ocena RAG (Seja 2)

Uporabite `rag_eval_ragas.py` za izračun ustreznosti odgovorov, zanesljivosti in natančnosti konteksta na majhnem sintetičnem naboru podatkov:

```powershell
python samples/session02/rag_eval_ragas.py
```

Razširite tako, da zagotovite večji JSONL z vprašanji, konteksti in resničnimi odgovori, nato pa ga pretvorite v Hugging Face `Dataset`.

## Dodatek k natančnosti ukazov CLI

Delavnica uporablja samo trenutno dokumentirane/stabilne ukaze Foundry Local CLI.

### Referencirani stabilni ukazi

| Kategorija | Ukaz | Namen |
|------------|------|-------|
| Osnovno | `foundry --version` | Prikaže nameščeno različico |
| Osnovno | `foundry init` | Inicializira konfiguracijo |
| Storitev | `foundry service start` | Zažene lokalno storitev (če ni samodejno) |
| Storitev | `foundry status` | Prikaže stanje storitve |
| Modeli | `foundry model list` | Prikaže katalog / razpoložljive modele |
| Modeli | `foundry model download <alias>` | Prenese uteži modela v predpomnilnik |
| Modeli | `foundry model run <alias>` | Zažene (naloži) model lokalno; kombinirajte z `--prompt` za enkratni poziv |
| Modeli | `foundry model unload <alias>` / `foundry model stop <alias>` | Odstrani model iz pomnilnika (če je podprto) |
| Predpomnilnik | `foundry cache list` | Prikaže predpomnjene (prenese) modele |
| Sistem | `foundry system info` | Posnetek strojne opreme & zmogljivosti pospeševanja |
| Sistem | `foundry system gpu-info` | Diagnostične informacije o GPU |
| Konfiguracija | `foundry config list` | Prikaže trenutne vrednosti konfiguracije |
| Konfiguracija | `foundry config set <key> <value>` | Posodobi konfiguracijo |

### Vzorec enkratnega poziva

Namesto zastarelega podukaza `model chat` uporabite:

```powershell
foundry model run <alias> --prompt "Your question here"
```

To izvede en sam cikel poziva/odgovora in nato izstopi.

### Odstranjeni / izogibani vzorci

| Zastarelo / Nedokumentirano | Nadomestilo / Smernice |
|-----------------------------|------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Uporabite običajni `foundry model list` + nedavna aktivnost / dnevniki |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Uporabite primerjalni Python skript + orodja OS (Upravitelj opravil / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Primerjava & Telemetrija

- Zakasnitev, p95, žetoni/sekundo: `samples/session03/benchmark_oss_models.py`
- Zakasnitev prvega žetona (pretakanje): nastavite `BENCH_STREAM=1`
- Uporaba virov: OS monitorji (Upravitelj opravil, Aktivnostni monitor, `nvidia-smi`) + `foundry system info`.

Ko se novi ukazi telemetrije CLI stabilizirajo, jih je mogoče vključiti z minimalnimi spremembami v markdown datotekah sej.

### Samodejni nadzor lint

Samodejni linter preprečuje ponovno uvedbo zastarelih CLI vzorcev znotraj blokov kode v markdown datotekah:

Skript: `Workshop/scripts/lint_markdown_cli.py`

Zastareli vzorci so blokirani znotraj blokov kode.

Priporočene zamenjave:
| Zastarelo | Nadomestilo |
|-----------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Primerjalni skript + sistemska orodja |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Zaženite lokalno:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` se zažene ob vsakem pushu & PR.

Izbirni precommit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Hitri CLI → SDK migracijski pregled

| Naloga | CLI enovrstični ukaz | SDK (Python) ekvivalent | Opombe |
|-------|-----------------------|-------------------------|--------|
| Zaženite model enkrat (poziv) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK samodejno zažene storitev & predpomnjenje |
| Prenos (predpomnjenje) modela | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager izbere najboljšo različico, če vzdevek ustreza več gradnjam |
| Prikaži katalog | `foundry model list` | `# use manager for each alias or maintain known list` | CLI združuje; SDK trenutno po vzdevku |
| Prikaži predpomnjene modele | `foundry cache list` | `manager.list_cached_models()` | Po inicializaciji managerja (katerikoli vzdevek) |
| Omogočite GPU pospeševanje | `foundry config set compute.onnx.enable_gpu true` | `# CLI action; SDK assumes config already applied` | Konfiguracija je zunanji stranski učinek |
| Pridobite URL končne točke | (implicitno) | `manager.endpoint` | Uporablja se za ustvarjanje OpenAI-kompatibilnega odjemalca |
| Ogrevanje modela | `foundry model run <alias>` nato prvi poziv | `chat_once(alias, messages=[...])` (utility) | Pripomočki obravnavajo začetno zakasnitev ob zagonu |
| Merjenje zakasnitve | `python benchmark_oss_models.py` | `import benchmark_oss_models` (ali nov izvoznik skripta) | Prednost dajte skriptu za dosledne meritve |
| Ustavitev / odstranitev modela | `foundry model unload <alias>` | (Ni izpostavljeno – ponovno zaženite storitev / proces) | Običajno ni potrebno za potek delavnice |
| Pridobitev uporabe žetonov | (oglejte si izhod) | `resp.usage.total_tokens` | Na voljo, če backend vrne objekt uporabe |

## Izvoz primerjalnega markdowna

Uporabite skript `Workshop/scripts/export_benchmark_markdown.py` za izvedbo sveže primerjave (ista logika kot `samples/session03/benchmark_oss_models.py`) in izvoz GitHub-prijazne markdown tabele ter surovega JSON-a.

### Primer

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Ustvarjene datoteke:
| Datoteka | Vsebina |
|---------|---------|
| `benchmark_report.md` | Markdown tabela + namigi za interpretacijo |
| `benchmark_report.json` | Surovo polje metrik (za primerjavo / sledenje trendom) |

Nastavite `BENCH_STREAM=1` v okolju za vključitev zakasnitve prvega žetona, če je podprto.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni prevod s strani človeka. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.