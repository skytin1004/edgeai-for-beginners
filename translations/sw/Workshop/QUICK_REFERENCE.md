<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a887b7e85782dadd3fd1216cd63b6c23",
  "translation_date": "2025-10-09T21:37:21+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "sw"
}
-->
# Kadi ya Marejeleo ya Haraka - Sampuli za Warsha

**Imesasishwa Mwisho**: Oktoba 8, 2025

---

## 🚀 Kuanza Haraka

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

## 📂 Muhtasari wa Sampuli

| Kipindi | Sampuli | Kusudi | Muda |
|---------|--------|---------|------|
| 01 | `chat_bootstrap.py` | Gumzo la msingi + utiririshaji | ~30s |
| 02 | `rag_pipeline.py` | RAG na embeddings | ~45s |
| 02 | `rag_eval_ragas.py` | Tathmini ya RAG | ~60s |
| 03 | `benchmark_oss_models.py` | Upimaji wa modeli | ~2m |
| 04 | `model_compare.py` | SLM dhidi ya LLM | ~45s |
| 05 | `agents_orchestrator.py` | Mfumo wa mawakala wengi | ~60s |
| 06 | `models_router.py` | Uelekezaji wa nia | ~45s |
| 06 | `models_pipeline.py` | Njia ya hatua nyingi | ~60s |

---

## 🛠️ Vigezo vya Mazingira

### Muhimu
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Maalum kwa Kipindi
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

## ✅ Uthibitishaji & Upimaji

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

## 🐛 Utatuzi wa Shida

### Hitilafu ya Muunganisho
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Hitilafu ya Uingizaji
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Modeli Haikupatikana
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Utendaji Polepole
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Mifumo ya Kawaida

### Gumzo la Msingi
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Kupata Mteja
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Kushughulikia Hitilafu
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Utiririshaji
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

## 📊 Uchaguzi wa Modeli

| Modeli | Ukubwa | Bora Kwa | Kasi |
|-------|------|----------|-------|
| `qwen2.5-0.5b` | 0.5B | Uainishaji wa haraka | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Uzalishaji wa haraka wa msimbo | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Uandishi wa ubunifu | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Msimbo, marekebisho | ⚡⚡ |
| `phi-4-mini` | 4B | Jumla, matumizi ya jumla | ⚡⚡ |
| `qwen2.5-7b` | 7B | Ufikiri wa hali ngumu | ⚡ |

---

## 🔗 Rasilimali

- **SDK Docs**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Marejeleo ya Haraka**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Muhtasari wa Sasisho**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **Vidokezo vya Uhamishaji**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 Vidokezo

1. **Hifadhi wateja**: `workshop_utils` inahifadhi kwa ajili yako
2. **Tumia modeli ndogo**: Anza na `qwen2.5-0.5b` kwa majaribio
3. **Wezesha takwimu za matumizi**: Weka `SHOW_USAGE=1` kufuatilia tokeni
4. **Usindikaji wa kundi**: Shughulikia maelekezo mengi mfululizo
5. **Punguza max_tokens**: Inapunguza ucheleweshaji kwa majibu ya haraka

---

## 🎯 Mifumo ya Sampuli

### Jaribu Kila Kitu
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Pima Modeli
```bash
cd samples/session03
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=3
python benchmark_oss_models.py
```

### Njia ya RAG
```bash
cd samples/session02
set RAG_QUESTION="What is RAG?"
python rag_pipeline.py
```

### Mfumo wa Mawakala Wengi
```bash
cd samples/session05
set AGENT_QUESTION="Why edge AI for healthcare?"
python agents_orchestrator.py
```

---

**Msaada wa Haraka**: Endesha sampuli yoyote kwa `--help` au angalia docstring:
```bash
python chat_bootstrap.py --help
# or
python -c "import chat_bootstrap; help(chat_bootstrap)"
```

---

**Sampuli zote zimesasishwa Oktoba 2025 kwa mbinu bora za Foundry Local SDK** ✨

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.