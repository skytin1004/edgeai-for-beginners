<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a887b7e85782dadd3fd1216cd63b6c23",
  "translation_date": "2025-10-09T19:29:49+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "tl"
}
-->
# Workshop Samples - Quick Reference Card

**Huling Na-update**: Oktubre 8, 2025

---

## 🚀 Mabilisang Simula

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

## 📂 Pangkalahatang-ideya ng Mga Halimbawa

| Session | Halimbawa | Layunin | Oras |
|---------|-----------|---------|------|
| 01 | `chat_bootstrap.py` | Pangunahing chat + streaming | ~30s |
| 02 | `rag_pipeline.py` | RAG gamit ang embeddings | ~45s |
| 02 | `rag_eval_ragas.py` | Pagsusuri ng RAG | ~60s |
| 03 | `benchmark_oss_models.py` | Benchmarking ng modelo | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Multi-agent system | ~60s |
| 06 | `models_router.py` | Intent routing | ~45s |
| 06 | `models_pipeline.py` | Multi-step pipeline | ~60s |

---

## 🛠️ Mga Environment Variable

### Mahalaga
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Para sa Bawat Session
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

## ✅ Pagpapatunay at Pagsubok

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

## 🐛 Pag-aayos ng Problema

### Error sa Koneksyon
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Error sa Import
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Modelong Hindi Natagpuan
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Mabagal na Performance
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Karaniwang Pattern

### Pangunahing Chat
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Kunin ang Client
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Pag-aayos ng Error
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

## 📊 Pagpili ng Modelo

| Modelo | Sukat | Pinakamahusay Para sa | Bilis |
|--------|-------|-----------------------|-------|
| `qwen2.5-0.5b` | 0.5B | Mabilis na klasipikasyon | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Mabilis na pagbuo ng code | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Malikhaing pagsusulat | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Code, refactoring | ⚡⚡ |
| `phi-4-mini` | 4B | Pangkalahatan, buod | ⚡⚡ |
| `qwen2.5-7b` | 7B | Masalimuot na pangangatwiran | ⚡ |

---

## 🔗 Mga Mapagkukunan

- **SDK Docs**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Quick Ref**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Update Summary**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **Migration Notes**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 Mga Tip

1. **Cache ang mga client**: Ang `workshop_utils` ay nagka-cache para sa iyo
2. **Gumamit ng mas maliliit na modelo**: Simulan gamit ang `qwen2.5-0.5b` para sa pagsubok
3. **I-enable ang usage stats**: Itakda ang `SHOW_USAGE=1` para subaybayan ang mga token
4. **Batch processing**: Iproseso ang maraming prompt nang sunud-sunod
5. **Ibaba ang max_tokens**: Binabawasan ang latency para sa mabilisang tugon

---

## 🎯 Mga Workflow ng Halimbawa

### Subukan Lahat
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Benchmark ng Mga Modelo
```bash
cd samples/session03
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=3
python benchmark_oss_models.py
```

### RAG Pipeline
```bash
cd samples/session02
set RAG_QUESTION="What is RAG?"
python rag_pipeline.py
```

### Multi-Agent System
```bash
cd samples/session05
set AGENT_QUESTION="Why edge AI for healthcare?"
python agents_orchestrator.py
```

---

**Mabilisang Tulong**: Patakbuhin ang anumang halimbawa gamit ang `--help` o tingnan ang docstring:
```bash
python chat_bootstrap.py --help
# or
python -c "import chat_bootstrap; help(chat_bootstrap)"
```

---

**Lahat ng halimbawa ay na-update noong Oktubre 2025 gamit ang pinakamahusay na kasanayan sa Foundry Local SDK** ✨

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.