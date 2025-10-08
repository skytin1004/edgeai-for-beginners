<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "48d0fb38be925084a6ebd957d4b045e5",
  "translation_date": "2025-10-08T15:22:58+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "ro"
}
-->
# EdgeAI pentru Începători - Atelier

> **Cale de învățare practică pentru construirea aplicațiilor Edge AI gata de producție**
>
> Stăpânește implementarea AI locală cu Microsoft Foundry Local, de la prima completare de chat la orchestrarea multi-agent în 6 sesiuni progresive.

---

## 🎯 Introducere

Bine ați venit la **Atelierul EdgeAI pentru Începători** - ghidul dumneavoastră practic pentru a construi aplicații inteligente care rulează complet pe hardware local. Acest atelier transformă conceptele teoretice ale Edge AI în abilități practice prin exerciții progresive folosind Microsoft Foundry Local și Small Language Models (SLMs).

### De ce acest atelier?

**Revoluția Edge AI este aici**

Organizațiile din întreaga lume trec de la AI dependent de cloud la calculul la margine (edge computing) din trei motive critice:

1. **Confidențialitate & Conformitate** - Procesarea datelor sensibile local, fără transmiterea lor în cloud (HIPAA, GDPR, reglementări financiare)
2. **Performanță** - Eliminarea latenței rețelei (50-500ms local vs 500-2000ms tur-retur în cloud)
3. **Controlul costurilor** - Eliminarea costurilor per token ale API-urilor și scalarea fără cheltuieli de cloud

**Dar Edge AI este diferit**

Rularea AI-ului local necesită abilități noi:
- Selectarea și optimizarea modelelor pentru constrângeri de resurse
- Gestionarea serviciilor locale și accelerarea hardware-ului
- Ingineria prompturilor pentru modele mai mici
- Modele de implementare în producție pentru dispozitive edge

**Acest atelier vă oferă aceste abilități**

În 6 sesiuni concentrate (~3 ore în total), veți progresa de la "Hello World" la implementarea sistemelor multi-agent gata de producție - toate rulând local pe mașina dumneavoastră.

---

## 📚 Obiectivele de învățare

Prin completarea acestui atelier, veți putea:

### Competențe de bază
1. **Implementați și gestionați servicii AI locale**
   - Instalați și configurați Microsoft Foundry Local
   - Selectați modelele potrivite pentru implementarea la margine
   - Gestionați ciclul de viață al modelului (descărcare, încărcare, cache)
   - Monitorizați utilizarea resurselor și optimizați performanța

2. **Construiți aplicații alimentate de AI**
   - Implementați completări de chat compatibile cu OpenAI local
   - Proiectați prompturi eficiente pentru Small Language Models
   - Gestionați răspunsurile în flux pentru o experiență mai bună a utilizatorului
   - Integrați modelele locale în aplicațiile existente

3. **Creați sisteme RAG (Retrieval Augmented Generation)**
   - Construiți căutări semantice cu embeddings
   - Fundamentați răspunsurile LLM în cunoștințe specifice domeniului
   - Evaluați calitatea RAG cu metrici standard din industrie
   - Scalați de la prototip la producție

4. **Optimizați performanța modelului**
   - Evaluați mai multe modele pentru cazul dumneavoastră de utilizare
   - Măsurați latența, debitul și timpul primului token
   - Selectați modelele optime pe baza compromisurilor viteză/calitate
   - Comparați compromisurile SLM vs LLM în scenarii reale

5. **Orchestrați sisteme multi-agent**
   - Proiectați agenți specializați pentru diferite sarcini
   - Implementați memoria agenților și gestionarea contextului
   - Coordonați agenții în fluxuri de lucru complexe
   - Direcționați cererile inteligent între mai multe modele

6. **Implementați soluții gata de producție**
   - Implementați gestionarea erorilor și logica de retry
   - Monitorizați utilizarea token-urilor și resursele sistemului
   - Construiți arhitecturi scalabile cu modele ca instrumente
   - Planificați căile de migrare de la margine la hibrid (margine + cloud)

---

## 🎓 Rezultatele învățării

### Ce veți construi

Până la finalul acestui atelier, veți fi creat:

| Sesiune | Rezultat | Abilități demonstrate |
|---------|----------|------------------------|
| **1** | Aplicație de chat cu streaming | Configurare serviciu, completări de bază, UX streaming |
| **2** | Sistem RAG cu evaluare | Embeddings, căutare semantică, metrici de calitate |
| **3** | Suită de benchmark multi-model | Măsurarea performanței, compararea modelelor |
| **4** | Comparator SLM vs LLM | Analiza compromisurilor, strategii de optimizare |
| **5** | Orchestrator multi-agent | Proiectare agenți, gestionarea memoriei, coordonare |
| **6** | Sistem de rutare inteligentă | Detectarea intenției, selecția modelului, scalabilitate |

### Matricea competențelor

| Nivel de abilități | Sesiunea 1-2 | Sesiunea 3-4 | Sesiunea 5-6 |
|---------------------|--------------|--------------|--------------|
| **Începător** | ✅ Configurare & bază | ⚠️ Provocator | ❌ Prea avansat |
| **Intermediar** | ✅ Revizuire rapidă | ✅ Învățare de bază | ⚠️ Obiective avansate |
| **Avansat** | ✅ Ușor de parcurs | ✅ Perfecționare | ✅ Modele de producție |

### Abilități pentru carieră

**După acest atelier, veți fi pregătit să:**

✅ **Construiți aplicații orientate pe confidențialitate**
- Aplicații de sănătate care gestionează PHI/PII local
- Servicii financiare cu cerințe de conformitate
- Sisteme guvernamentale cu cerințe de suveranitate a datelor

✅ **Optimizați pentru medii Edge**
- Dispozitive IoT cu resurse limitate
- Aplicații mobile offline-first
- Sisteme în timp real cu latență scăzută

✅ **Proiectați arhitecturi inteligente**
- Sisteme multi-agent pentru fluxuri de lucru complexe
- Implementări hibride margine-cloud
- Infrastructură AI optimizată pentru costuri

✅ **Conduceți inițiative Edge AI**
- Evaluați fezabilitatea Edge AI pentru proiecte
- Selectați modelele și cadrele potrivite
- Arhitecturați soluții AI locale scalabile

---

## 🗺️ Structura atelierului

### Prezentare generală a sesiunilor (6 sesiuni × 30 minute = 3 ore)

| Sesiune | Subiect | Focus | Durată |
|---------|---------|-------|--------|
| **1** | Începeți cu Foundry Local | Instalare, validare, primele completări | 30 min |
| **2** | Construirea soluțiilor AI cu RAG | Ingineria prompturilor, embeddings, evaluare | 30 min |
| **3** | Modele Open Source | Descoperirea modelelor, benchmarking, selecție | 30 min |
| **4** | Modele de ultimă generație | SLM vs LLM, optimizare, cadre | 30 min |
| **5** | Agenți alimentați de AI | Proiectare agenți, orchestrare, memorie | 30 min |
| **6** | Modele ca instrumente | Rutare, lanțuri, strategii de scalare | 30 min |

---

## 🚀 Început rapid

### Cerințe preliminare

**Cerințe de sistem:**
- **OS**: Windows 10/11, macOS 11+ sau Linux (Ubuntu 20.04+)
- **RAM**: minim 8GB, recomandat 16GB+
- **Spațiu de stocare**: minim 10GB liber pentru modele
- **CPU**: Procesor modern cu suport AVX2
- **GPU** (opțional): Compatibil CUDA sau Qualcomm NPU pentru accelerare

**Cerințe software:**
- **Python 3.8+** ([Descarcă](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Ghid de instalare](../../../Workshop))
- **Git** ([Descarcă](https://git-scm.com/downloads))
- **Visual Studio Code** (recomandat) ([Descarcă](https://code.visualstudio.com/))

### Configurare în 3 pași

#### 1. Instalați Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verificați instalarea:**
```bash
foundry --version
foundry service status
```

#### 2. Clonați Repozitoriul & Instalați Dependențele

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

#### 3. Rulați primul exemplu

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples/session01
python chat_bootstrap.py "What is edge AI?"
```

**✅ Succes!** Ar trebui să vedeți un răspuns în flux despre Edge AI.

---

## 📦 Resursele atelierului

### Exemple Python

Exemple practice progresive care demonstrează fiecare concept:

| Sesiune | Exemplu | Descriere | Timp de rulare |
|---------|---------|-----------|----------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Chat de bază & streaming | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG cu embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Evaluarea calității RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking multi-model | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Comparație SLM vs LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Sistem multi-agent | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Rutare bazată pe intenție | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Orchestrare pipeline multi-pas | ~60s |

### Jupyter Notebooks

Explorare interactivă cu explicații și vizualizări:

| Sesiune | Notebook | Descriere | Dificultate |
|---------|----------|-----------|-------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Bazele chat-ului & streaming | ⭐ Începător |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Construirea unui sistem RAG | ⭐⭐ Intermediar |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Evaluarea calității RAG | ⭐⭐ Intermediar |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking modele | ⭐⭐ Intermediar |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Comparație modele | ⭐⭐ Intermediar |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orchestrarea agenților | ⭐⭐⭐ Avansat |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Rutare pe baza intenției | ⭐⭐⭐ Avansat |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orchestrare pipeline | ⭐⭐⭐ Avansat |

### Documentație

Ghiduri și referințe complete:

| Document | Descriere | Când să-l folosiți |
|----------|-----------|--------------------|
| [QUICK_START.md](./QUICK_START.md) | Ghid rapid de configurare | La început |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Fișă de referință pentru comenzi & API | Când aveți nevoie de răspunsuri rapide |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Modele și exemple SDK | Scrierea codului |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Ghid pentru variabilele de mediu | Configurarea exemplelor |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Îmbunătățiri recente ale exemplelor | Înțelegerea schimbărilor |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Ghid de migrare | Actualizarea codului |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Probleme comune & soluții | Depanarea problemelor |

---

## 🎓 Recomandări pentru calea de învățare

### Pentru Începători (3-4 ore)
1. ✅ Sesiunea 1: Începeți (focus pe configurare și chat de bază)
2. ✅ Sesiunea 2: Bazele RAG (săriți peste evaluare inițial)
3. ✅ Sesiunea 3: Benchmarking simplu (doar 2 modele)
4. ⏭️ Săriți peste sesiunile 4-6 pentru moment
5. 🔄 Revenire la sesiunile 4-6 după construirea primei aplicații

### Pentru Dezvoltatori Intermediari (3 ore)
1. ⚡ Sesiunea 1: Validare rapidă a configurării
2. ✅ Sesiunea 2: Finalizați pipeline-ul RAG cu evaluare
3. ✅ Sesiunea 3: Suită completă de benchmarking
4. ✅ Sesiunea 4: Optimizarea modelului
5. ✅ Sesiunile 5-6: Focus pe modelele arhitecturale

### Pentru Practicieni Avansați (2-3 ore)
1. ⚡ Sesiunile 1-3: Revizuire și validare rapidă
2. ✅ Sesiunea 4: Detalii despre optimizare
3. ✅ Sesiunea 5: Arhitectură multi-agent
4. ✅ Sesiunea 6: Modele de producție și scalare
5. 🚀 Extindere: Construiți logica personalizată de rutare și implementări hibride

---

## Pachetul de sesiuni ale atelierului (Laboratoare concentrate de 30 de minute)

Dacă urmați formatul condensat al atelierului de 6 sesiuni, utilizați aceste ghiduri dedicate (fiecare se corelează și completează documentația mai amplă de mai sus):

| Sesiunea atelierului | Ghid | Focus principal |
|----------------------|------|-----------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalare, validare, rulare phi & GPT-OSS-20B, accelerare |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Ingineria prompturilor, modele RAG, fundamentare CSV & documente, migrare |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integrare Hugging Face, benchmarking, selecția modelelor |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, accelerare ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Roluri agenți, memorie, instrumente, orchestrare |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Rutare, lanțuri, strategii de scalare către Azure |
Fiecare fișier de sesiune include: rezumat, obiective de învățare, flux demo de 30 de minute, proiect de început, listă de verificare pentru validare, depanare și referințe la SDK-ul oficial Foundry Local Python.

### Scripturi Exemplu

Instalare dependențe pentru workshop (Windows):

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

Dacă serviciul Foundry Local rulează pe o altă mașină (Windows) sau VM de pe macOS, exportați endpoint-ul:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sesiune | Script(uri) | Descriere |
|---------|-------------|-----------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap service & streaming chat |
| 2 | `samples/session02/rag_pipeline.py` | RAG minimal (embedding-uri în memorie) |
|   | `samples/session02/rag_eval_ragas.py` | Evaluare RAG cu metrici ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking multi-model pentru latență și debit |
| 4 | `samples/session04/model_compare.py` | Comparație SLM vs LLM (latență & ieșire exemplu) |
| 5 | `samples/session05/agents_orchestrator.py` | Pipeline de cercetare cu doi agenți → editorial |
| 6 | `samples/session06/models_router.py` | Demo de rutare bazată pe intenție |
|   | `samples/session06/models_pipeline.py` | Lanț multi-pas planificare/executare/perfecționare |

### Variabile de Mediu (Comune pentru Exemple)

| Variabilă | Scop | Exemplu |
|-----------|------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias implicit pentru un singur model în exemplele de bază | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | SLM explicit vs model mai mare pentru comparație | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Listă de aliasuri pentru benchmark | `qwen2.5-0.5b,gemma-2-2b,mistral-7b` |
| `BENCH_ROUNDS` | Repetiții benchmark per model | `3` |
| `BENCH_PROMPT` | Prompt utilizat în benchmark | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Model de embedding pentru sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Suprascriere query test pentru pipeline-ul RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Suprascriere query pentru pipeline-ul agenților | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias model pentru agentul de cercetare | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias model pentru agentul editor (poate fi diferit) | `gpt-oss-20b` |
| `SHOW_USAGE` | Când este `1`, afișează utilizarea token-urilor per completare | `1` |
| `RETRY_ON_FAIL` | Când este `1`, reîncearcă o dată în caz de erori temporare de chat | `1` |
| `RETRY_BACKOFF` | Secunde de așteptare înainte de reîncercare | `1.0` |

Dacă o variabilă nu este setată, scripturile vor folosi valori implicite rezonabile. Pentru demo-urile cu un singur model, de obicei aveți nevoie doar de `FOUNDRY_LOCAL_ALIAS`.

### Modul Utilitar

Toate exemplele împărtășesc acum un helper `samples/workshop_utils.py` care oferă:

* Crearea cache-ului pentru `FoundryLocalManager` + client OpenAI
* Helper `chat_once()` cu retry opțional + afișare utilizare
* Raportare simplă a utilizării token-urilor (activată prin `SHOW_USAGE=1`)

Acest lucru reduce duplicarea și evidențiază cele mai bune practici pentru orchestrarea eficientă a modelelor locale.

## Îmbunătățiri Opționale (Între Sesiuni)

| Temă | Îmbunătățire | Sesiuni | Env / Toggle |
|------|--------------|---------|--------------|
| Determinism | Temperatură fixă + seturi de prompt stabile | 1–6 | Setează `temperature=0`, `top_p=1` |
| Vizibilitate Utilizare Token-uri | Predare consistentă a costului/eficienței | 1–6 | `SHOW_USAGE=1` |
| Streaming Primul Token | Metrică de latență percepută | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Reziliență la Retry | Gestionează pornirea lentă temporară | Toate | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Agenți Multi-Model | Specializare pe roluri eterogene | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Rutare Adaptivă | Intenție + euristici de cost | 6 | Extinde router-ul cu logică de escaladare |
| Memorie Vectorială | Rechemare semantică pe termen lung | 2,5,6 | Integrează index embedding FAISS/Chroma |
| Export Traseu | Auditare & evaluare | 2,5,6 | Adaugă linii JSON per pas |
| Rubrici de Calitate | Urmărire calitativă | 3–6 | Prompts secundare pentru scorare |
| Teste Smoke | Validare rapidă pre-workshop | Toate | `python Workshop/tests/smoke.py` |

### Start Rapid Determinist

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Așteptați număr stabil de token-uri pentru intrări identice repetate.

### Evaluare RAG (Sesiunea 2)

Utilizați `rag_eval_ragas.py` pentru a calcula relevanța răspunsului, fidelitatea și precizia contextului pe un set de date sintetic mic:

```powershell
python samples/session02/rag_eval_ragas.py
```

Extindeți furnizând un JSONL mai mare cu întrebări, contexte și adevăruri de bază, apoi convertiți-l într-un `Dataset` Hugging Face.

## Anexă Comenzi CLI Precise

Workshop-ul folosește deliberat doar comenzi CLI Foundry Local documentate / stabile.

### Comenzi Stabile Referite

| Categorie | Comandă | Scop |
|-----------|---------|------|
| Bază | `foundry --version` | Afișează versiunea instalată |
| Bază | `foundry init` | Inițializează configurația |
| Serviciu | `foundry service start` | Pornește serviciul local (dacă nu este auto) |
| Serviciu | `foundry status` | Afișează statusul serviciului |
| Modele | `foundry model list` | Listează catalogul / modelele disponibile |
| Modele | `foundry model download <alias>` | Descarcă greutățile modelului în cache |
| Modele | `foundry model run <alias>` | Rulează (încarcă) un model local; combină cu `--prompt` pentru one-shot |
| Modele | `foundry model unload <alias>` / `foundry model stop <alias>` | Dezîncarcă un model din memorie (dacă este suportat) |
| Cache | `foundry cache list` | Listează modelele cache-uite (descărcate) |
| Sistem | `foundry system info` | Snapshot capabilități hardware & accelerare |
| Sistem | `foundry system gpu-info` | Info diagnostic GPU |
| Config | `foundry config list` | Afișează valorile de configurare curente |
| Config | `foundry config set <key> <value>` | Actualizează configurația |

### Model One‑Shot Prompt

În loc de subcomanda `model chat` depreciată, utilizați:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Aceasta execută un ciclu prompt/răspuns unic și apoi se închide.

### Modele Depreciate / Evitate

| Depreciat / Nedocumentat | Înlocuire / Ghidare |
|--------------------------|---------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Utilizați `foundry model list` simplu + activitate recentă / loguri |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Utilizați scriptul benchmark Python + unelte OS (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetrie

- Latență, p95, tokens/sec: `samples/session03/benchmark_oss_models.py`
- Latență primul token (streaming): setați `BENCH_STREAM=1`
- Utilizare resurse: monitoare OS (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Pe măsură ce noi comenzi CLI de telemetrie se stabilizează, acestea pot fi integrate cu modificări minime în markdown-urile sesiunilor.

### Lint Automatizat

Un linter automat previne reintroducerea modelelor CLI depreciate în interiorul blocurilor de cod din fișierele markdown:

Script: `Workshop/scripts/lint_markdown_cli.py`

Modelele depreciate sunt blocate în interiorul blocurilor de cod.

Înlocuiri recomandate:
| Depreciat | Înlocuire |
|-----------|-----------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Script benchmark + unelte sistem |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Rulați local:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` rulează la fiecare push & PR.

Hook opțional pre-commit:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Tabel Rapid Migrare CLI → SDK

| Sarcină | Linie CLI | Echivalent SDK (Python) | Note |
|---------|-----------|--------------------------|------|
| Rulează un model o dată (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK inițializează automat serviciul & cache-ul |
| Descarcă (cache) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # declanșează descărcare/încărcare` | Managerul alege cea mai bună variantă dacă aliasul corespunde mai multor versiuni |
| Listează catalogul | `foundry model list` | `# folosiți manager pentru fiecare alias sau mențineți o listă cunoscută` | CLI agregă; SDK în prezent instanțiere per-alias |
| Listează modelele cache-uite | `foundry cache list` | `manager.list_cached_models()` | După inițializarea managerului (orice alias) |
| Activează accelerarea GPU | `foundry config set compute.onnx.enable_gpu true` | `# Acțiune CLI; SDK presupune că setarea este deja aplicată` | Configurația este un efect extern |
| Obține URL endpoint | (implicit) | `manager.endpoint` | Utilizat pentru a crea un client compatibil OpenAI |
| Încălzește un model | `foundry model run <alias>` apoi primul prompt | `chat_once(alias, messages=[...])` (utilitar) | Utilitarele gestionează încălzirea inițială a latenței |
| Măsoară latența | `python benchmark_oss_models.py` | `import benchmark_oss_models` (sau un nou script exportator) | Preferă scriptul pentru metrici consistente |
| Oprește / dezîncarcă modelul | `foundry model unload <alias>` | (Nu este expus – reporniți serviciul / procesul) | De obicei, nu este necesar pentru fluxul workshop-ului |
| Recuperează utilizarea token-urilor | (vizualizați ieșirea) | `resp.usage.total_tokens` | Furnizat dacă backend-ul returnează obiectul de utilizare |

## Export Markdown Benchmark

Utilizați scriptul `Workshop/scripts/export_benchmark_markdown.py` pentru a rula un benchmark proaspăt (aceeași logică ca `samples/session03/benchmark_oss_models.py`) și pentru a genera un tabel Markdown prietenos cu GitHub plus JSON brut.

### Exemplu

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Fișiere generate:
| Fișier | Conținut |
|--------|----------|
| `benchmark_report.md` | Tabel Markdown + sugestii de interpretare |
| `benchmark_report.json` | Array de metrici brute (pentru comparare / urmărirea tendințelor) |

Setați `BENCH_STREAM=1` în mediu pentru a include latența primului token, dacă este suportată.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.