<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a887b7e85782dadd3fd1216cd63b6c23",
  "translation_date": "2025-10-08T15:27:18+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "sk"
}
-->
# Workshop Samples - Rýchla referenčná karta

**Posledná aktualizácia**: 8. október 2025

---

## 🚀 Rýchly štart

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

## 📂 Prehľad vzoriek

| Relácia | Vzor | Účel | Čas |
|---------|------|------|-----|
| 01 | `chat_bootstrap.py` | Základný chat + streamovanie | ~30s |
| 02 | `rag_pipeline.py` | RAG s embeddingami | ~45s |
| 02 | `rag_eval_ragas.py` | Hodnotenie RAG | ~60s |
| 03 | `benchmark_oss_models.py` | Porovnanie modelov | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Systém viacerých agentov | ~60s |
| 06 | `models_router.py` | Smerovanie podľa zámeru | ~45s |
| 06 | `models_pipeline.py` | Viackroková pipeline | ~60s |

---

## 🛠️ Premenné prostredia

### Základné
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Špecifické pre reláciu
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

## ✅ Validácia a testovanie

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

## 🐛 Riešenie problémov

### Chyba pripojenia
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Chyba importu
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Model nebol nájdený
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Pomalý výkon
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Bežné vzory

### Základný chat
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Získanie klienta
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Spracovanie chýb
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Streamovanie
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

## 📊 Výber modelu

| Model | Veľkosť | Najlepšie pre | Rýchlosť |
|-------|---------|--------------|----------|
| `qwen2.5-0.5b` | 0.5B | Rýchla klasifikácia | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Rýchla generácia kódu | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Kreatívne písanie | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Kód, refaktoring | ⚡⚡ |
| `phi-4-mini` | 4B | Všeobecné, zhrnutie | ⚡⚡ |
| `qwen2.5-7b` | 7B | Komplexné uvažovanie | ⚡ |

---

## 🔗 Zdroje

- **SDK dokumentácia**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Rýchla referenčná karta**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Zhrnutie aktualizácií**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **Poznámky k migrácii**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 Tipy

1. **Cache klientov**: `workshop_utils` to za vás urobí automaticky
2. **Používajte menšie modely**: Na testovanie začnite s `qwen2.5-0.5b`
3. **Povoľte štatistiky používania**: Nastavte `SHOW_USAGE=1` na sledovanie tokenov
4. **Batch spracovanie**: Spracujte viacero promptov postupne
5. **Znížte max_tokens**: Zníži latenciu pre rýchle odpovede

---

## 🎯 Pracovné postupy vzoriek

### Otestujte všetko
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Porovnanie modelov
```bash
cd samples/session03
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=3
python benchmark_oss_models.py
```

### RAG pipeline
```bash
cd samples/session02
set RAG_QUESTION="What is RAG?"
python rag_pipeline.py
```

### Systém viacerých agentov
```bash
cd samples/session05
set AGENT_QUESTION="Why edge AI for healthcare?"
python agents_orchestrator.py
```

---

**Rýchla pomoc**: Spustite akúkoľvek vzorku s `--help` alebo si pozrite docstring:
```bash
python chat_bootstrap.py --help
# or
python -c "import chat_bootstrap; help(chat_bootstrap)"
```

---

**Všetky vzorky aktualizované v októbri 2025 podľa najlepších praktík Foundry Local SDK** ✨

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.