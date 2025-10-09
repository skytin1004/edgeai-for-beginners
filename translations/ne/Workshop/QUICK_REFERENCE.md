<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a887b7e85782dadd3fd1216cd63b6c23",
  "translation_date": "2025-10-09T09:40:17+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "ne"
}
-->
# कार्यशाला नमूना - छिटो सन्दर्भ कार्ड

**अन्तिम अद्यावधिक**: अक्टोबर ८, २०२५

---

## 🚀 छिटो सुरु गर्नुहोस्

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

## 📂 नमूना अवलोकन

| सत्र | नमूना | उद्देश्य | समय |
|------|-------|----------|------|
| 01 | `chat_bootstrap.py` | आधारभूत च्याट + स्ट्रिमिङ | ~30 सेकेन्ड |
| 02 | `rag_pipeline.py` | RAG इम्बेडिङसहित | ~45 सेकेन्ड |
| 02 | `rag_eval_ragas.py` | RAG मूल्याङ्कन | ~60 सेकेन्ड |
| 03 | `benchmark_oss_models.py` | मोडेल बेंचमार्किङ | ~2 मिनेट |
| 04 | `model_compare.py` | SLM बनाम LLM | ~45 सेकेन्ड |
| 05 | `agents_orchestrator.py` | बहु-एजेन्ट प्रणाली | ~60 सेकेन्ड |
| 06 | `models_router.py` | उद्देश्य रुटिङ | ~45 सेकेन्ड |
| 06 | `models_pipeline.py` | बहु-चरण पाइपलाइन | ~60 सेकेन्ड |

---

## 🛠️ वातावरण चरहरू

### आवश्यक
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### सत्र-विशिष्ट
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

## ✅ मान्यता र परीक्षण

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

## 🐛 समस्या समाधान

### जडान त्रुटि
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### आयात त्रुटि
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### मोडेल फेला परेन
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### ढिलो प्रदर्शन
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 सामान्य ढाँचा

### आधारभूत च्याट
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### क्लाइन्ट प्राप्त गर्नुहोस्
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### त्रुटि ह्यान्डलिङ
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### स्ट्रिमिङ
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

## 📊 मोडेल चयन

| मोडेल | आकार | उपयुक्त | गति |
|-------|-------|----------|------|
| `qwen2.5-0.5b` | 0.5B | छिटो वर्गीकरण | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | छिटो कोड उत्पादन | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | सिर्जनात्मक लेखन | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | कोड, पुनःसंरचना | ⚡⚡ |
| `phi-4-mini` | 4B | सामान्य, सारांश | ⚡⚡ |
| `qwen2.5-7b` | 7B | जटिल तर्क | ⚡ |

---

## 🔗 स्रोतहरू

- **SDK कागजातहरू**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **छिटो सन्दर्भ**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **अद्यावधिक सारांश**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **माइग्रेसन नोट्स**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 सुझावहरू

1. **क्लाइन्टहरू क्यास गर्नुहोस्**: `workshop_utils` ले तपाईंको लागि क्यास गर्छ
2. **सानो मोडेल प्रयोग गर्नुहोस्**: परीक्षणको लागि `qwen2.5-0.5b` बाट सुरु गर्नुहोस्
3. **प्रयोग तथ्याङ्क सक्षम गर्नुहोस्**: टोकन ट्र्याक गर्न `SHOW_USAGE=1` सेट गर्नुहोस्
4. **ब्याच प्रशोधन**: धेरै प्रम्प्टहरू क्रमिक रूपमा प्रशोधन गर्नुहोस्
5. **कम max_tokens सेट गर्नुहोस्**: छिटो प्रतिक्रिया प्राप्त गर्न ढिलाइ घटाउँछ

---

## 🎯 नमूना कार्यप्रवाहहरू

### सबै परीक्षण गर्नुहोस्
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### मोडेल बेंचमार्क गर्नुहोस्
```bash
cd samples/session03
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=3
python benchmark_oss_models.py
```

### RAG पाइपलाइन
```bash
cd samples/session02
set RAG_QUESTION="What is RAG?"
python rag_pipeline.py
```

### बहु-एजेन्ट प्रणाली
```bash
cd samples/session05
set AGENT_QUESTION="Why edge AI for healthcare?"
python agents_orchestrator.py
```

---

**छिटो सहायता**: कुनै पनि नमूना `--help` प्रयोग गरेर चलाउनुहोस् वा डकस्ट्रिङ जाँच गर्नुहोस्:
```bash
python chat_bootstrap.py --help
# or
python -c "import chat_bootstrap; help(chat_bootstrap)"
```

---

**सबै नमूनाहरू अक्टोबर २०२५ मा Foundry Local SDK का उत्कृष्ट अभ्यासहरूसँग अद्यावधिक गरियो** ✨

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।