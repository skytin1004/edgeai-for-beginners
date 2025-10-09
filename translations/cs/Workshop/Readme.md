<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "48d0fb38be925084a6ebd957d4b045e5",
  "translation_date": "2025-10-09T21:26:14+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "cs"
}
-->
# EdgeAI pro začátečníky - Workshop

> **Praktická cesta k vytváření produkčně připravených Edge AI aplikací**
>
> Ovládněte nasazení lokální AI s Microsoft Foundry Local, od prvního chatovacího dokončení po orchestraci více agentů v šesti postupných lekcích.

---

## 🎯 Úvod

Vítejte na **workshopu EdgeAI pro začátečníky** – vašem praktickém průvodci pro vytváření inteligentních aplikací, které běží výhradně na lokálním hardwaru. Tento workshop přetváří teoretické koncepty Edge AI do reálných dovedností prostřednictvím postupně náročnějších cvičení s využitím Microsoft Foundry Local a malých jazykových modelů (SLM).

### Proč tento workshop?

**Revoluce Edge AI je tady**

Organizace po celém světě přecházejí z cloudově závislé AI na edge computing ze tří klíčových důvodů:

1. **Soukromí a shoda s předpisy** – Zpracovávejte citlivá data lokálně bez přenosu do cloudu (HIPAA, GDPR, finanční regulace)
2. **Výkon** – Eliminujte síťovou latenci (50–500 ms lokálně vs. 500–2000 ms při přenosu do cloudu)
3. **Kontrola nákladů** – Odstraňte náklady na API za token a škálujte bez výdajů na cloud

**Ale Edge AI je jiná**

Provozování AI na místě vyžaduje nové dovednosti:
- Výběr a optimalizace modelů pro omezené zdroje
- Správa lokálních služeb a hardwarová akcelerace
- Návrh promptů pro menší modely
- Vzory nasazení pro zařízení na okraji sítě

**Tento workshop vás tyto dovednosti naučí**

Během 6 zaměřených lekcí (~3 hodiny celkem) postoupíte od „Hello World“ k nasazení produkčně připravených systémů s více agenty – vše běžící lokálně na vašem zařízení.

---

## 📚 Cíle učení

Po absolvování tohoto workshopu budete schopni:

### Klíčové dovednosti
1. **Nasazení a správa lokálních AI služeb**
   - Instalace a konfigurace Microsoft Foundry Local
   - Výběr vhodných modelů pro nasazení na okraji
   - Správa životního cyklu modelů (stahování, načítání, ukládání do mezipaměti)
   - Monitorování využití zdrojů a optimalizace výkonu

2. **Vytváření aplikací poháněných AI**
   - Implementace OpenAI-kompatibilních chatovacích dokončení lokálně
   - Návrh efektivních promptů pro malé jazykové modely
   - Zpracování streamovaných odpovědí pro lepší uživatelský zážitek
   - Integrace lokálních modelů do stávajících aplikací

3. **Vytváření systémů RAG (Retrieval Augmented Generation)**
   - Budování sémantického vyhledávání s využitím embeddingů
   - Ukotvení odpovědí LLM v doménově specifických znalostech
   - Hodnocení kvality RAG pomocí průmyslových standardů
   - Škálování od prototypu k produkci

4. **Optimalizace výkonu modelů**
   - Benchmarking více modelů pro váš případ použití
   - Měření latence, propustnosti a času prvního tokenu
   - Výběr optimálních modelů na základě kompromisů mezi rychlostí a kvalitou
   - Porovnání kompromisů mezi SLM a LLM v reálných scénářích

5. **Orchestraci systémů s více agenty**
   - Návrh specializovaných agentů pro různé úkoly
   - Implementace paměti agentů a správy kontextu
   - Koordinace agentů v komplexních pracovních postupech
   - Inteligentní směrování požadavků mezi více modely

6. **Nasazení produkčně připravených řešení**
   - Implementace zpracování chyb a logiky opakování
   - Monitorování využití tokenů a systémových zdrojů
   - Vytváření škálovatelných architektur s využitím vzorů model-as-tools
   - Plánování migračních cest z okraje na hybridní řešení (okraj + cloud)

---

## 🎓 Výstupy učení

### Co vytvoříte

Na konci tohoto workshopu budete mít vytvořeno:

| Lekce | Výstup | Demonstrované dovednosti |
|-------|--------|--------------------------|
| **1** | Chatovací aplikace se streamováním | Nastavení služby, základní dokončení, UX streamování |
| **2** | RAG systém s hodnocením | Embeddingy, sémantické vyhledávání, metriky kvality |
| **3** | Sada benchmarků pro více modelů | Měření výkonu, porovnání modelů |
| **4** | Porovnání SLM vs LLM | Analýza kompromisů, optimalizační strategie |
| **5** | Orchestrátor s více agenty | Návrh agentů, správa paměti, koordinace |
| **6** | Inteligentní směrovací systém | Detekce záměru, výběr modelu, škálovatelnost |

### Matice dovedností

| Úroveň dovedností | Lekce 1-2 | Lekce 3-4 | Lekce 5-6 |
|-------------------|-----------|-----------|-----------|
| **Začátečník** | ✅ Nastavení a základy | ⚠️ Náročné | ❌ Příliš pokročilé |
| **Středně pokročilý** | ✅ Rychlé zopakování | ✅ Klíčové učení | ⚠️ Cíle pro pokročilé |
| **Pokročilý** | ✅ Snadno zvládnutelné | ✅ Zjemnění dovedností | ✅ Produkční vzory |

### Kariérní dovednosti

**Po tomto workshopu budete připraveni:**

✅ **Vytvářet aplikace s důrazem na soukromí**
- Zdravotnické aplikace zpracovávající PHI/PII lokálně
- Finanční služby splňující regulační požadavky
- Vládní systémy s potřebou datové suverenity

✅ **Optimalizovat pro prostředí na okraji**
- IoT zařízení s omezenými zdroji
- Mobilní aplikace s prioritou offline režimu
- Systémy s nízkou latencí v reálném čase

✅ **Navrhovat inteligentní architektury**
- Systémy s více agenty pro komplexní pracovní postupy
- Hybridní nasazení okraj-cloud
- Nákladově optimalizovaná AI infrastruktura

✅ **Vést iniciativy Edge AI**
- Hodnotit proveditelnost Edge AI pro projekty
- Vybrat vhodné modely a frameworky
- Navrhnout škálovatelná lokální AI řešení

---

## 🗺️ Struktura workshopu

### Přehled lekcí (6 lekcí × 30 minut = 3 hodiny)

| Lekce | Téma | Zaměření | Doba trvání |
|-------|------|----------|-------------|
| **1** | Začínáme s Foundry Local | Instalace, ověření, první dokončení | 30 min |
| **2** | Vytváření AI řešení s RAG | Návrh promptů, embeddingy, hodnocení | 30 min |
| **3** | Open Source modely | Objevování modelů, benchmarking, výběr | 30 min |
| **4** | Nejmodernější modely | SLM vs LLM, optimalizace, frameworky | 30 min |
| **5** | AI pohánění agenti | Návrh agentů, orchestrace, paměť | 30 min |
| **6** | Modely jako nástroje | Směrování, řetězení, strategie škálování | 30 min |

---

## 🚀 Rychlý start

### Požadavky

**Systémové požadavky:**
- **OS**: Windows 10/11, macOS 11+ nebo Linux (Ubuntu 20.04+)
- **RAM**: Minimálně 8 GB, doporučeno 16 GB+
- **Úložiště**: 10 GB+ volného místa pro modely
- **CPU**: Moderní procesor s podporou AVX2
- **GPU** (volitelné): CUDA-kompatibilní nebo Qualcomm NPU pro akceleraci

**Softwarové požadavky:**
- **Python 3.8+** ([Stáhnout](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Průvodce instalací](../../../Workshop))
- **Git** ([Stáhnout](https://git-scm.com/downloads))
- **Visual Studio Code** (doporučeno) ([Stáhnout](https://code.visualstudio.com/))

### Nastavení ve 3 krocích

#### 1. Instalace Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Ověření instalace:**
```bash
foundry --version
foundry service status
```

#### 2. Klonování repozitáře a instalace závislostí

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

#### 3. Spuštění prvního příkladu

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples/session01
python chat_bootstrap.py "What is edge AI?"
```

**✅ Úspěch!** Měli byste vidět streamovanou odpověď o Edge AI.

---

## 📦 Zdroje workshopu

### Python příklady

Postupné praktické ukázky demonstrující každý koncept:

| Lekce | Příklad | Popis | Doba běhu |
|-------|---------|-------|-----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Základní a streamovací chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG s embeddingy | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Hodnocení kvality RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking více modelů | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Porovnání SLM vs LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Systém s více agenty | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Směrování na základě záměru | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Vícekroková pipeline | ~60s |

### Jupyter Notebooks

Interaktivní průzkum s vysvětleními a vizualizacemi:

| Lekce | Notebook | Popis | Obtížnost |
|-------|----------|-------|-----------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Základy chatu a streamování | ⭐ Začátečník |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Vytvoření systému RAG | ⭐⭐ Středně pokročilý |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Hodnocení kvality RAG | ⭐⭐ Středně pokročilý |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking modelů | ⭐⭐ Středně pokročilý |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Porovnání modelů | ⭐⭐ Středně pokročilý |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orchestrace agentů | ⭐⭐⭐ Pokročilý |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Směrování na základě záměru | ⭐⭐⭐ Pokročilý |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orchestrace pipeline | ⭐⭐⭐ Pokročilý |

### Dokumentace

Komplexní průvodce a referenční materiály:

| Dokument | Popis | Použít kdy |
|----------|-------|------------|
| [QUICK_START.md](./QUICK_START.md) | Průvodce rychlým nastavením | Začínáte od nuly |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Přehled příkazů a API | Potřebujete rychlé odpovědi |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Vzory a příklady SDK | Píšete kód |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Průvodce proměnnými prostředí | Konfigurace příkladů |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Nejnovější vylepšení příkladů | Pochopení změn |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Průvodce migrací | Aktualizace kódu |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Běžné problémy a opravy | Řešení problémů |

---

## 🎓 Doporučení pro učební cestu

### Pro začátečníky (3-4 hodiny)
1. ✅ Lekce 1: Začínáme (zaměřte se na nastavení a základní chat)
2. ✅ Lekce 2: Základy RAG (zpočátku přeskočte hodnocení)
3. ✅ Lekce 3: Jednoduchý benchmarking (pouze 2 modely)
4. ⏭️ Lekce 4-6 zatím přeskočte
5. 🔄 Vraťte se k lekcím 4-6 po vytvoření první aplikace

### Pro středně pokročilé vývojáře (3 hodiny)
1. ⚡ Lekce 1: Rychlé ověření nastavení
2. ✅ Lekce 2: Kompletní pipeline RAG s hodnocením
3. ✅ Lekce 3: Kompletní sada benchmarků
4. ✅ Lekce 4: Optimalizace modelů
5. ✅ Lekce 5-6: Zaměřte se na architektonické vzory

### Pro pokročilé odborníky (2-3 hodiny)
1. ⚡ Lekce 1-3: Rychlé zopakování a ověření
2. ✅ Lekce 4: Hlubší ponor do optimalizace
3. ✅ Lekce 5: Architektura s více agenty
4. ✅ Lekce 6: Produkční vzory a škálování
5. 🚀 Rozšíření: Vytvořte vlastní logiku směrování a hybridní nasazení

---

## Balíček workshopových lekcí (zaměřené 30minutové laboratoře)

Pokud sledujete zhuštěný formát workshopu o 6 lekcích, použijte tyto specializované průvodce (každý odpovídá a doplňuje širší modulovou dokumentaci výše):

| Workshopová lekce | Průvodce | Hlavní zaměření |
|-------------------|----------|-----------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalace, ověření, spuštění phi & GPT-OSS-20B, akcelerace |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Návrh promptů, vzory RAG, ukotvení CSV a dokumentů, migrace |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integrace Hugging Face, benchmarking, výběr modelů |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, akcelerace ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Role agentů, paměť, nástroje, orchestrace |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Směrování, řetězení, cesta ke škálování na Azure |
Každý soubor relace obsahuje: abstrakt, výukové cíle, 30minutový průběh ukázky, startovací projekt, kontrolní seznam validace, řešení problémů a odkazy na oficiální Foundry Local Python SDK.

### Ukázkové skripty

Instalace závislostí workshopu (Windows):

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

Pokud běží služba Foundry Local na jiném (Windows) stroji nebo VM z macOS, exportujte endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Relace | Skript(y) | Popis |
|--------|-----------|-------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap služby & streamovací chat |
| 2 | `samples/session02/rag_pipeline.py` | Minimalistický RAG (embeddings v paměti) |
|   | `samples/session02/rag_eval_ragas.py` | Hodnocení RAG pomocí metrik ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking latence & propustnosti více modelů |
| 4 | `samples/session04/model_compare.py` | Porovnání SLM vs LLM (latence & ukázkový výstup) |
| 5 | `samples/session05/agents_orchestrator.py` | Výzkumný → redakční pipeline dvou agentů |
| 6 | `samples/session06/models_router.py` | Demo směrování na základě záměru |
|   | `samples/session06/models_pipeline.py` | Vícekrokový plán/realizace/zlepšení řetězec |

### Proměnné prostředí (společné pro všechny ukázky)

| Proměnná | Účel | Příklad |
|----------|------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Výchozí alias jednoho modelu pro základní ukázky | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Explicitní SLM vs větší model pro porovnání | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Seznam aliasů modelů pro benchmarking | `qwen2.5-0.5b,gemma-2-2b,mistral-7b` |
| `BENCH_ROUNDS` | Opakování benchmarku na model | `3` |
| `BENCH_PROMPT` | Prompt použitý při benchmarkingu | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Přepsání testovacího dotazu pro RAG pipeline | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Přepsání dotazu pro pipeline agentů | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias modelu pro výzkumného agenta | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias modelu pro redakčního agenta (může se lišit) | `gpt-oss-20b` |
| `SHOW_USAGE` | Pokud `1`, tiskne využití tokenů na dokončení | `1` |
| `RETRY_ON_FAIL` | Pokud `1`, jednou se pokusí znovu při přechodných chybách chatu | `1` |
| `RETRY_BACKOFF` | Sekundy čekání před opakováním | `1.0` |

Pokud není proměnná nastavena, skripty se vrátí k rozumným výchozím hodnotám. Pro ukázky s jedním modelem obvykle stačí pouze `FOUNDRY_LOCAL_ALIAS`.

### Pomocný modul

Všechny ukázky nyní sdílejí pomocný modul `samples/workshop_utils.py`, který poskytuje:

* Vytvoření cache `FoundryLocalManager` + klienta OpenAI
* Pomocnou funkci `chat_once()` s volitelným opakováním + tiskem využití
* Jednoduché hlášení využití tokenů (aktivace přes `SHOW_USAGE=1`)

To snižuje duplicitu a zdůrazňuje osvědčené postupy pro efektivní orchestraci lokálních modelů.

## Volitelná vylepšení (napříč relacemi)

| Téma | Vylepšení | Relace | Env / Přepínač |
|------|-----------|--------|---------------|
| Determinismus | Fixní teplota + stabilní sady promptů | 1–6 | Nastavte `temperature=0`, `top_p=1` |
| Viditelnost využití tokenů | Konzistentní výuka nákladů/efektivity | 1–6 | `SHOW_USAGE=1` |
| Streamování prvního tokenu | Metrika vnímané latence | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Odolnost při opakování | Řeší přechodné studené starty | Vše | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-modeloví agenti | Specializace rolí | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptivní směrování | Záměr + heuristika nákladů | 6 | Rozšíření routeru o logiku eskalace |
| Vektorová paměť | Dlouhodobé sémantické vybavení | 2,5,6 | Integrace FAISS/Chroma embedding indexu |
| Export trasování | Auditování & hodnocení | 2,5,6 | Přidání JSON řádků na krok |
| Kvalitativní rubriky | Kvalitativní sledování | 3–6 | Sekundární scoring promptů |
| Smoke testy | Rychlá validace před workshopem | Vše | `python Workshop/tests/smoke.py` |

### Deterministický rychlý start

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Očekávejte stabilní počty tokenů při opakovaných identických vstupech.

### Hodnocení RAG (Relace 2)

Použijte `rag_eval_ragas.py` pro výpočet relevance odpovědí, věrnosti a přesnosti kontextu na malém syntetickém datasetu:

```powershell
python samples/session02/rag_eval_ragas.py
```

Rozšiřte dodáním většího JSONL souboru otázek, kontextů a pravdivých odpovědí, poté konvertujte na Hugging Face `Dataset`.

## Příloha přesnosti CLI příkazů

Workshop záměrně používá pouze aktuálně dokumentované / stabilní CLI příkazy Foundry Local.

### Stabilní příkazy použité

| Kategorie | Příkaz | Účel |
|-----------|--------|------|
| Jádro | `foundry --version` | Zobrazení nainstalované verze |
| Jádro | `foundry init` | Inicializace konfigurace |
| Služba | `foundry service start` | Spuštění lokální služby (pokud není automatické) |
| Služba | `foundry status` | Zobrazení stavu služby |
| Modely | `foundry model list` | Seznam katalogu / dostupných modelů |
| Modely | `foundry model download <alias>` | Stažení váhy modelu do cache |
| Modely | `foundry model run <alias>` | Spuštění (nahrání) modelu lokálně; kombinace s `--prompt` pro jednorázové použití |
| Modely | `foundry model unload <alias>` / `foundry model stop <alias>` | Vyložení modelu z paměti (pokud je podporováno) |
| Cache | `foundry cache list` | Seznam cacheovaných (stažených) modelů |
| Systém | `foundry system info` | Snímek hardwarových & akceleračních schopností |
| Systém | `foundry system gpu-info` | Diagnostické informace o GPU |
| Konfigurace | `foundry config list` | Zobrazení aktuálních hodnot konfigurace |
| Konfigurace | `foundry config set <key> <value>` | Aktualizace konfigurace |

### Jednorázový prompt vzor

Namísto zastaralého podpříkazu `model chat` použijte:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Tím se provede jednorázový cyklus prompt/odpověď a poté se ukončí.

### Odstraněné / vyhnuté vzory

| Zastaralé / Nedokumentované | Náhrada / Doporučení |
|-----------------------------|----------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Použijte prosté `foundry model list` + nedávná aktivita / logy |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Použijte benchmarkovací Python skript + nástroje OS (Správce úloh / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetrie

- Latence, p95, tokeny/sec: `samples/session03/benchmark_oss_models.py`
- Latence prvního tokenu (streamování): nastavte `BENCH_STREAM=1`
- Využití zdrojů: OS monitory (Správce úloh, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Jakmile se nové CLI telemetrické příkazy stabilizují upstream, mohou být začleněny s minimálními úpravami do markdownů relací.

### Automatická kontrola linterem

Automatický linter zabraňuje opětovnému zavedení zastaralých CLI vzorů uvnitř ohraničených bloků kódu v markdown souborech:

Skript: `Workshop/scripts/lint_markdown_cli.py`

Zastaralé vzory jsou blokovány uvnitř ohraničených bloků kódu.

Doporučené náhrady:
| Zastaralé | Náhrada |
|-----------|---------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmarkovací skript + systémové nástroje |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Spusťte lokálně:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` běží při každém push & PR.

Volitelný pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Rychlá tabulka migrace CLI → SDK

| Úkol | CLI Jednorázový příkaz | SDK (Python) Ekvivalent | Poznámky |
|------|------------------------|-------------------------|----------|
| Spuštění modelu jednou (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK automaticky inicializuje službu & cache |
| Stažení (cache) modelu | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager vybírá nejlepší variantu, pokud alias mapuje na více buildů |
| Seznam katalogu | `foundry model list` | `# použijte manager pro každý alias nebo udržujte známý seznam` | CLI agreguje; SDK aktuálně instancuje per-alias |
| Seznam cacheovaných modelů | `foundry cache list` | `manager.list_cached_models()` | Po inicializaci manageru (jakýkoli alias) |
| Aktivace GPU akcelerace | `foundry config set compute.onnx.enable_gpu true` | `# CLI akce; SDK předpokládá, že konfigurace již byla aplikována` | Konfigurace je externí vedlejší efekt |
| Získání URL endpointu | (implicitní) | `manager.endpoint` | Používá se k vytvoření klienta kompatibilního s OpenAI |
| Zahřátí modelu | `foundry model run <alias>` a poté první prompt | `chat_once(alias, messages=[...])` (utility) | Utility řeší počáteční studenou latenci zahřátí |
| Měření latence | `python benchmark_oss_models.py` | `import benchmark_oss_models` (nebo nový exportní skript) | Preferujte skript pro konzistentní metriky |
| Zastavení / vyložení modelu | `foundry model unload <alias>` | (Není vystaveno – restartujte službu / proces) | Typicky není vyžadováno pro průběh workshopu |
| Získání využití tokenů | (zobrazení výstupu) | `resp.usage.total_tokens` | Poskytováno, pokud backend vrací objekt využití |

## Export benchmarků do Markdownu

Použijte skript `Workshop/scripts/export_benchmark_markdown.py` pro spuštění čerstvého benchmarku (stejná logika jako `samples/session03/benchmark_oss_models.py`) a generování tabulky Markdown přátelské GitHubu plus surového JSON.

### Příklad

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Generované soubory:
| Soubor | Obsah |
|--------|-------|
| `benchmark_report.md` | Tabulka Markdown + interpretační tipy |
| `benchmark_report.json` | Surové pole metrik (pro porovnání / sledování trendů) |

Nastavte `BENCH_STREAM=1` v prostředí pro zahrnutí latence prvního tokenu, pokud je podporována.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.