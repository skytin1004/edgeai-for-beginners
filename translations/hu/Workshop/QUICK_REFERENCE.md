<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a887b7e85782dadd3fd1216cd63b6c23",
  "translation_date": "2025-10-09T21:37:35+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "hu"
}
-->
# Workshop Minták - Gyors Referencia Kártya

**Utolsó frissítés**: 2025. október 8.

---

## 🚀 Gyors kezdés

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

---

## 📂 Minták áttekintése

| Szekció | Minta | Cél | Idő |
|---------|-------|-----|-----|
| 01 | `chat_bootstrap.py` | Alap chat + streaming | ~30s |
| 02 | `rag_pipeline.py` | RAG beágyazásokkal | ~45s |
| 02 | `rag_eval_ragas.py` | RAG értékelés | ~60s |
| 03 | `benchmark_oss_models.py` | Modell benchmarking | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Többügynökös rendszer | ~60s |
| 06 | `models_router.py` | Szándékirányítás | ~45s |
| 06 | `models_pipeline.py` | Többlépcsős folyamat | ~60s |

---

## 🛠️ Környezeti változók

### Alapvető
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Szekció-specifikus
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ Érvényesítés és tesztelés

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 Hibakeresés

### Kapcsolódási hiba
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Importálási hiba
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Modell nem található
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Lassú teljesítmény
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Gyakori minták

### Alap chat
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Ügyfél lekérése
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Hibakezelés
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Streaming
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 Modellválasztás

| Modell | Méret | Legjobb felhasználás | Sebesség |
|--------|-------|----------------------|---------|
| `qwen2.5-0.5b` | 0.5B | Gyors osztályozás | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Gyors kódgenerálás | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Kreatív írás | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Kód, refaktorálás | ⚡⚡ |
| `phi-4-mini` | 4B | Általános, összegzés | ⚡⚡ |
| `qwen2.5-7b` | 7B | Összetett érvelés | ⚡ |

---

## 🔗 Erőforrások

- **SDK Dokumentáció**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Gyors Referencia**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Frissítési összefoglaló**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **Migrációs jegyzetek**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 Tippek

1. **Ügyfelek gyorsítótárazása**: A `workshop_utils` automatikusan gyorsítótáraz
2. **Használj kisebb modelleket**: Teszteléshez kezdj a `qwen2.5-0.5b` modellel
3. **Engedélyezd a használati statisztikát**: Állítsd be `SHOW_USAGE=1` a tokenek nyomon követéséhez
4. **Tömeges feldolgozás**: Több promptot dolgozz fel egymás után
5. **Csökkentsd a max_tokens értéket**: Csökkenti a késleltetést gyors válaszokhoz

---

## 🎯 Mintafolyamatok

### Minden tesztelése
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Modellek benchmarkolása
```bash
cd samples/session03
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=3
python benchmark_oss_models.py
```

### RAG folyamat
```bash
cd samples/session02
set RAG_QUESTION="What is RAG?"
python rag_pipeline.py
```

### Többügynökös rendszer
```bash
cd samples/session05
set AGENT_QUESTION="Why edge AI for healthcare?"
python agents_orchestrator.py
```

---

**Gyors segítség**: Futtass bármely mintát `--help` opcióval, vagy nézd meg a docstringet:
```bash
python chat_bootstrap.py --help
# or
python -c "import chat_bootstrap; help(chat_bootstrap)"
```

---

**Minden minta frissítve 2025 októberében a Foundry Local SDK legjobb gyakorlataival** ✨

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.