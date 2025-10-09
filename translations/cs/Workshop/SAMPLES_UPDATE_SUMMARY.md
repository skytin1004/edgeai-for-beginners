<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-09T21:40:30+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "cs"
}
-->
# Ukázky workshopu - Souhrn aktualizace Foundry Local SDK

## Přehled

Všechny ukázky v Pythonu v adresáři `Workshop/samples` byly aktualizovány tak, aby odpovídaly osvědčeným postupům Foundry Local SDK a zajistila se konzistence napříč workshopem.

**Datum**: 8. října 2025  
**Rozsah**: 9 souborů v Pythonu napříč 6 workshopy  
**Hlavní zaměření**: Zpracování chyb, dokumentace, vzory SDK, uživatelská zkušenost

---

## Aktualizované soubory

### Workshop 01: Začínáme
- ✅ `chat_bootstrap.py` - Základní příklady chatu a streamování

### Workshop 02: RAG řešení
- ✅ `rag_pipeline.py` - Implementace RAG s embeddingy
- ✅ `rag_eval_ragas.py` - Hodnocení RAG pomocí metrik RAGAS

### Workshop 03: Open Source modely
- ✅ `benchmark_oss_models.py` - Benchmarking více modelů

### Workshop 04: Nejmodernější modely
- ✅ `model_compare.py` - Porovnání SLM a LLM

### Workshop 05: Agenti pohánění AI
- ✅ `agents_orchestrator.py` - Koordinace více agentů

### Workshop 06: Modely jako nástroje
- ✅ `models_router.py` - Směrování modelů na základě záměru
- ✅ `models_pipeline.py` - Vícekrokový směrovaný pipeline

### Podpůrná infrastruktura
- ✅ `workshop_utils.py` - Již odpovídá osvědčeným postupům (nebyly potřeba žádné změny)

---

## Klíčová vylepšení

### 1. Vylepšené zpracování chyb

**Před:**
```python
manager, client, model_id = get_client(alias)
```

**Po:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Výhody:**
- Elegantní zpracování chyb s jasnými chybovými zprávami
- Praktické rady pro řešení problémů
- Správné návratové kódy pro skriptování

### 2. Lepší správa importů

**Před:**
```python
from sentence_transformers import SentenceTransformer
```

**Po:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Výhody:**
- Jasné pokyny při chybějících závislostech
- Zabraňuje nejasným chybám při importu
- Uživatelsky přívětivé pokyny k instalaci

### 3. Komplexní dokumentace

**Přidáno ke všem ukázkám:**
- Dokumentace k proměnným prostředí v docstringách
- Odkazy na dokumentaci SDK
- Příklady použití
- Podrobná dokumentace funkcí/parametrů
- Typové nápovědy pro lepší podporu v IDE

**Příklad:**
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

### 4. Vylepšená zpětná vazba uživatelům

**Přidáno informativní logování:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Indikátory průběhu:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Strukturovaný výstup:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Robustní benchmarking

**Vylepšení v workshopu 03:**
- Zpracování chyb pro jednotlivé modely (pokračuje i při selhání)
- Podrobné hlášení průběhu
- Správné provedení zahřívacích kol
- Podpora měření latence prvního tokenu
- Jasné oddělení jednotlivých fází

### 6. Konzistentní typové nápovědy

**Přidáno všude:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Výhody:**
- Lepší automatické doplňování v IDE
- Včasná detekce chyb
- Samodokumentující kód

### 7. Vylepšené směrování modelů

**Vylepšení v workshopu 06:**
- Komplexní dokumentace detekce záměru
- Vysvětlení algoritmu výběru modelu
- Podrobné logy směrování
- Formátování výstupu testů
- Obnova chyb při dávkovém testování

### 8. Orchestrace více agentů

**Vylepšení v workshopu 05:**
- Hlášení průběhu po jednotlivých fázích
- Zpracování chyb pro jednotlivé agenty
- Jasná struktura pipeline
- Lepší dokumentace správy paměti

---

## Kontrolní seznam testování

### Předpoklady
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testování každé ukázky

#### Workshop 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### Workshop 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### Workshop 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### Workshop 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### Workshop 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### Workshop 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## Referenční příručka proměnných prostředí

### Globální (všechny ukázky)
| Proměnná | Popis | Výchozí hodnota |
|----------|-------|-----------------|
| `FOUNDRY_LOCAL_ALIAS` | Alias modelu k použití | Liší se podle ukázky |
| `FOUNDRY_LOCAL_ENDPOINT` | Přepsání koncového bodu služby | Automaticky detekováno |
| `SHOW_USAGE` | Zobrazit využití tokenů | `0` |
| `RETRY_ON_FAIL` | Povolit logiku opakování | `1` |
| `RETRY_BACKOFF` | Počáteční zpoždění opakování | `1.0` |

### Specifické pro ukázky
| Proměnná | Používá | Popis |
|----------|---------|-------|
| `EMBED_MODEL` | Workshop 02 | Název embedding modelu |
| `RAG_QUESTION` | Workshop 02 | Testovací otázka pro RAG |
| `BENCH_MODELS` | Workshop 03 | Modely pro benchmarking (oddělené čárkou) |
| `BENCH_ROUNDS` | Workshop 03 | Počet kol benchmarkingu |
| `BENCH_PROMPT` | Workshop 03 | Testovací prompt pro benchmarking |
| `BENCH_STREAM` | Workshop 03 | Měření latence prvního tokenu |
| `SLM_ALIAS` | Workshop 04 | Malý jazykový model |
| `LLM_ALIAS` | Workshop 04 | Velký jazykový model |
| `COMPARE_PROMPT` | Workshop 04 | Testovací prompt pro porovnání |
| `AGENT_MODEL_PRIMARY` | Workshop 05 | Primární model agenta |
| `AGENT_MODEL_EDITOR` | Workshop 05 | Model agenta editoru |
| `AGENT_QUESTION` | Workshop 05 | Testovací otázka pro agenty |
| `PIPELINE_TASK` | Workshop 06 | Úkol pro pipeline |

---

## Zásadní změny

**Žádné** - Všechny změny jsou zpětně kompatibilní.

Stávající skripty budou nadále fungovat. Nové funkce zahrnují:
- Volitelné proměnné prostředí
- Vylepšené chybové zprávy (neovlivňují funkčnost)
- Další logování (lze potlačit)
- Lepší typové nápovědy (bez dopadu na běh programu)

---

## Implementované osvědčené postupy

### 1. Vždy používejte Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Správný vzor zpracování chyb
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informativní logování
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Typové nápovědy
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Komplexní docstringy
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

### 6. Podpora proměnných prostředí
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Elegantní degradace
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

## Běžné problémy a jejich řešení

### Problém: Chyby při importu
**Řešení:** Nainstalujte chybějící závislosti
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problém: Chyby připojení
**Řešení:** Ujistěte se, že Foundry Local běží
```bash
foundry service status
foundry model run phi-4-mini
```

### Problém: Model nebyl nalezen
**Řešení:** Zkontrolujte dostupné modely
```bash
foundry model ls
foundry model download <alias>
```

### Problém: Pomalý výkon
**Řešení:** Použijte menší modely nebo upravte parametry
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Další kroky

### 1. Otestujte všechny ukázky
Projděte si výše uvedený kontrolní seznam testování a ověřte, že všechny ukázky fungují správně.

### 2. Aktualizujte dokumentaci
- Aktualizujte markdown soubory workshopu s novými příklady
- Přidejte sekci řešení problémů do hlavního README
- Vytvořte rychlou referenční příručku

### 3. Vytvořte integrační testy
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Přidejte výkonnostní benchmarky
Sledujte zlepšení výkonu díky vylepšením zpracování chyb.

### 5. Zpětná vazba od uživatelů
Sbírejte zpětnou vazbu od účastníků workshopu na:
- Jasnost chybových zpráv
- Úplnost dokumentace
- Snadnost použití

---

## Zdroje

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Rychlá referenční příručka**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Poznámky k migraci**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Hlavní repozitář**: https://github.com/microsoft/Foundry-Local

---

## Údržba

### Přidávání nových ukázek
Při vytváření nových ukázek postupujte podle těchto vzorů:

1. Používejte `workshop_utils` pro správu klientů
2. Přidejte komplexní zpracování chyb
3. Zahrňte podporu proměnných prostředí
4. Přidejte typové nápovědy a docstringy
5. Poskytněte informativní logování
6. Zahrňte příklady použití v docstringu
7. Odkazujte na dokumentaci SDK

### Kontrola aktualizací
Při kontrole aktualizací ukázek zkontrolujte:
- [ ] Zpracování chyb u všech I/O operací
- [ ] Typové nápovědy u veřejných funkcí
- [ ] Komplexní docstringy
- [ ] Dokumentaci k proměnným prostředí
- [ ] Informativní zpětnou vazbu uživatelům
- [ ] Odkazy na dokumentaci SDK
- [ ] Konzistentní styl kódu

---

**Shrnutí**: Všechny ukázky v Pythonu pro workshop nyní odpovídají osvědčeným postupům Foundry Local SDK s vylepšeným zpracováním chyb, komplexní dokumentací a zlepšenou uživatelskou zkušeností. Žádné zásadní změny - veškerá stávající funkčnost byla zachována a vylepšena.

---

**Upozornění**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.