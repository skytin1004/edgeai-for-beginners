<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-09T21:07:19+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "cs"
}
-->
# Rychlý průvodce workshopem

## Předpoklady

### 1. Nainstalujte Foundry Local

Postupujte podle oficiálního průvodce instalací:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Nainstalujte Python závislosti

Z adresáře workshopu:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Spouštění ukázek workshopu

### Sezení 01: Základní chat

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**Proměnné prostředí:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sezení 02: RAG Pipeline

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**Proměnné prostředí:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sezení 02: Hodnocení RAG (Ragas)

```bash
python rag_eval_ragas.py
```

**Poznámka**: Vyžaduje instalaci dalších závislostí přes `requirements.txt`

### Sezení 03: Benchmarking

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**Proměnné prostředí:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Výstup**: JSON s metrikami latence, propustnosti a prvního tokenu

### Sezení 04: Porovnání modelů

```bash
cd Workshop/samples/session04
python model_compare.py
```

**Proměnné prostředí:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sezení 05: Orchestrace více agentů

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**Proměnné prostředí:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sezení 06: Směrovač modelů

```bash
cd Workshop/samples/session06
python models_router.py
```

**Testuje logiku směrování** s více záměry (kód, shrnutí, klasifikace)

### Sezení 06: Pipeline

```bash
python models_pipeline.py
```

**Komplexní vícekrokový proces** s plánováním, provedením a zdokonalením

## Skripty

### Export benchmarkové zprávy

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Výstup**: Tabulka v Markdownu + JSON metriky

### Lintování CLI vzorů v Markdownu

```bash
python lint_markdown_cli.py --verbose
```

**Účel**: Detekce zastaralých CLI vzorů v dokumentaci

## Testování

### Rychlé testy

```bash
cd Workshop
python -m tests.smoke
```

**Testy**: Základní funkčnost klíčových ukázek

## Řešení problémů

### Služba neběží

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Chyby při importu modulů

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Chyby připojení

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model nebyl nalezen

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referenční proměnné prostředí

### Základní konfigurace
| Proměnná | Výchozí hodnota | Popis |
|----------|-----------------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Různé | Alias modelu k použití |
| `FOUNDRY_LOCAL_ENDPOINT` | Automaticky | Přepsání koncového bodu služby |
| `SHOW_USAGE` | `0` | Zobrazení statistik využití tokenů |
| `RETRY_ON_FAIL` | `1` | Povolení logiky opakování |
| `RETRY_BACKOFF` | `1.0` | Počáteční zpoždění opakování (v sekundách) |

### Specifické pro sezení
| Proměnná | Výchozí hodnota | Popis |
|----------|-----------------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model pro vkládání |
| `RAG_QUESTION` | Viz ukázka | Testovací otázka pro RAG |
| `BENCH_MODELS` | Různé | Modely oddělené čárkou |
| `BENCH_ROUNDS` | `3` | Iterace benchmarku |
| `BENCH_PROMPT` | Viz ukázka | Výzva pro benchmark |
| `BENCH_STREAM` | `0` | Měření latence prvního tokenu |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Primární model agenta |
| `AGENT_MODEL_EDITOR` | Primární | Model agenta editoru |
| `SLM_ALIAS` | `phi-4-mini` | Malý jazykový model |
| `LLM_ALIAS` | `qwen2.5-7b` | Velký jazykový model |
| `COMPARE_PROMPT` | Viz ukázka | Výzva pro porovnání |

## Doporučené modely

### Vývoj a testování
- **phi-4-mini** - Vyvážená kvalita a rychlost
- **qwen2.5-0.5b** - Velmi rychlý pro klasifikaci
- **gemma-2-2b** - Dobrá kvalita, střední rychlost

### Produkční scénáře
- **phi-4-mini** - Obecné použití
- **deepseek-coder-1.3b** - Generování kódu
- **qwen2.5-7b** - Vysoce kvalitní odpovědi

## Dokumentace SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Získání pomoci

1. Zkontrolujte stav služby: `foundry service status`  
2. Prohlédněte si logy: Zkontrolujte logy služby Foundry Local  
3. Zkontrolujte dokumentaci SDK: https://github.com/microsoft/Foundry-Local  
4. Projděte si ukázkový kód: Všechny ukázky obsahují podrobné komentáře

## Další kroky

1. Dokončete všechna sezení workshopu v pořadí  
2. Experimentujte s různými modely  
3. Upravte ukázky pro své případy použití  
4. Projděte si `SDK_MIGRATION_NOTES.md` pro pokročilé vzory

---

**Poslední aktualizace**: 8. ledna 2025  
**Verze workshopu**: Nejnovější  
**SDK**: Foundry Local Python SDK

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.