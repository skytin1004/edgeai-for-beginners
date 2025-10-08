<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-08T12:20:13+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "my"
}
-->
# Workshop Samples - Foundry Local SDK Update Summary

## အကျဉ်းချုပ်

`Workshop/samples` ဖိုင်တွဲထဲရှိ Python နမူနာအားလုံးကို Foundry Local SDK အကောင်းဆုံးအလေ့အကျင့်များနှင့်အညီ ပြင်ဆင်ပြီး workshop အတွင်းတွင် တစ်ပြိုင်တည်းဖြစ်စေရန် အတည်ပြုထားပါသည်။

**ရက်စွဲ**: 2025 ခုနှစ် အောက်တိုဘာလ 8 ရက်  
**အကျယ်အဝန်း**: workshop session 6 ခုအတွင်း Python ဖိုင် 9 ခု  
**အဓိကအာရုံစိုက်မှု**: အမှားကိုင်တွယ်မှု, documentation, SDK ပုံစံများ, အသုံးပြုသူအတွေ့အကြုံ

---

## ပြင်ဆင်ထားသော ဖိုင်များ

### Session 01: စတင်ခြင်း
- ✅ `chat_bootstrap.py` - Chat အခြေခံနမူနာနှင့် streaming နမူနာများ

### Session 02: RAG Solutions
- ✅ `rag_pipeline.py` - Embeddings ဖြင့် RAG အကောင်အထည်ဖော်မှု
- ✅ `rag_eval_ragas.py` - RAGAS metrics ဖြင့် RAG အကဲဖြတ်မှု

### Session 03: Open Source Models
- ✅ `benchmark_oss_models.py` - မော်ဒယ်များစွာကို benchmarking ပြုလုပ်ခြင်း

### Session 04: Cutting Edge Models
- ✅ `model_compare.py` - SLM နှင့် LLM နှိုင်းယှဉ်မှု

### Session 05: AI-Powered Agents
- ✅ `agents_orchestrator.py` - Multi-agent စီမံခန့်ခွဲမှု

### Session 06: Models as Tools
- ✅ `models_router.py` - ရည်ရွယ်ချက်အခြေခံ model routing
- ✅ `models_pipeline.py` - Multi-step routed pipeline

### Supporting Infrastructure
- ✅ `workshop_utils.py` - အကောင်းဆုံးအလေ့အကျင့်များကို ရှိပြီးသား (ပြင်ဆင်မှုမလိုအပ်ပါ)

---

## အဓိကတိုးတက်မှုများ

### 1. အမှားကိုင်တွယ်မှု တိုးတက်မှု

**ယခင်**:
```python
manager, client, model_id = get_client(alias)
```

**နောက်**:
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**အကျိုးကျေးဇူးများ**:
- အမှားကို သေချာစွာကိုင်တွယ်ပြီး ရှင်းလင်းသော error message များ
- ပြုပြင်ရန်အကြံဉာဏ်များ
- scripting အတွက် သင့်လျော်သော exit code များ

### 2. Import ကို ပိုမိုကောင်းမွန်စွာ စီမံခြင်း

**ယခင်**:
```python
from sentence_transformers import SentenceTransformer
```

**နောက်**:
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**အကျိုးကျေးဇူးများ**:
- လိုအပ်သော dependency များမရှိပါက ရှင်းလင်းသောအညွှန်းများ
- ရှုပ်ထွေးသော import error များကို ကာကွယ်ခြင်း
- အသုံးပြုသူအတွက် သက်သာသော installation အညွှန်းများ

### 3. Documentation အပြည့်အစုံ

**နမူနာအားလုံးတွင် ထည့်သွင်းထားသည်**:
- Environment variable documentation ကို docstring တွင် ထည့်သွင်းထားသည်
- SDK reference link များ
- အသုံးပြုနည်းနမူနာများ
- အသေးစိတ် function/parameter documentation
- IDE support အတွက် type hint များ

**နမူနာ**:
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

### 4. အသုံးပြုသူအကြောင်းပြန်မှု တိုးတက်မှု

**အသေးစိတ် log ထည့်သွင်းထားသည်**:
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**တိုးတက်မှုအညွှန်းများ**:
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**ဖွဲ့စည်းထားသော output**:
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Benchmarking တိုးတက်မှု

**Session 03 တိုးတက်မှုများ**:
- မော်ဒယ်တစ်ခုချင်းစီအတွက် အမှားကိုင်တွယ်မှု (အမှားဖြစ်ပျက်လျှင် ဆက်လက်လုပ်ဆောင်နိုင်သည်)
- တိုးတက်မှုအဆင့်များကို အသေးစိတ်ဖော်ပြခြင်း
- Warmup round များကို သေချာစွာလုပ်ဆောင်ခြင်း
- First-token latency ကိုတိုင်းတာနိုင်မှု
- အဆင့်များကို ရှင်းလင်းစွာခွဲခြားထားသည်

### 6. Type Hint တစ်ပြိုင်တည်း

**အားလုံးတွင် ထည့်သွင်းထားသည်**:
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**အကျိုးကျေးဇူးများ**:
- IDE autocomplete ပိုမိုကောင်းမွန်စေသည်
- အမှားကို စောစောမိစေသည်
- ကိုယ်တိုင် documentation ပြုလုပ်ထားသော code

### 7. Model Router တိုးတက်မှု

**Session 06 တိုးတက်မှုများ**:
- ရည်ရွယ်ချက်ကို ရှင်းလင်းစွာဖော်ပြထားသော documentation
- Model ရွေးချယ်မှု algorithm ရှင်းလင်းချက်
- Routing log အသေးစိတ်
- Test output formatting
- Batch testing အတွင်း error recovery

### 8. Multi-Agent စီမံခန့်ခွဲမှု

**Session 05 တိုးတက်မှုများ**:
- အဆင့်တစ်ဆင့်တစ်ဆင့် တိုးတက်မှုကို ဖော်ပြခြင်း
- Agent တစ်ခုချင်းစီအတွက် အမှားကိုင်တွယ်မှု
- Pipeline ဖွဲ့စည်းမှုကို ရှင်းလင်းစွာဖော်ပြထားသည်
- Memory management documentation ပိုမိုကောင်းမွန်စေသည်

---

## စမ်းသပ်မှု စစ်ဆေးရန်စာရင်း

### လိုအပ်ချက်များ
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### နမူနာတစ်ခုချင်းစီကို စမ်းသပ်ပါ

#### Session 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### Session 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### Session 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### Session 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### Session 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### Session 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## Environment Variables Reference

### Global (အားလုံးအတွက်)
| Variable | ဖော်ပြချက် | Default |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | အသုံးပြုမည့် Model alias | နမူနာအလိုက် မတူညီ |
| `FOUNDRY_LOCAL_ENDPOINT` | Service endpoint ကို override လုပ်ရန် | Auto-detected |
| `SHOW_USAGE` | Token အသုံးပြုမှုကို ဖော်ပြရန် | `0` |
| `RETRY_ON_FAIL` | Retry logic ကို ဖွင့်ရန် | `1` |
| `RETRY_BACKOFF` | Retry delay အစ | `1.0` |

### နမူနာအလိုက်
| Variable | အသုံးပြုသူ | ဖော်ပြချက် |
|----------|---------|-------------|
| `EMBED_MODEL` | Session 02 | Embedding model အမည် |
| `RAG_QUESTION` | Session 02 | RAG အတွက် စမ်းသပ်မေးခွန်း |
| `BENCH_MODELS` | Session 03 | Benchmark ပြုလုပ်မည့် မော်ဒယ်များ |
| `BENCH_ROUNDS` | Session 03 | Benchmark round အရေအတွက် |
| `BENCH_PROMPT` | Session 03 | Benchmark အတွက် စမ်းသပ် prompt |
| `BENCH_STREAM` | Session 03 | First-token latency ကိုတိုင်းတာရန် |
| `SLM_ALIAS` | Session 04 | Small language model |
| `LLM_ALIAS` | Session 04 | Large language model |
| `COMPARE_PROMPT` | Session 04 | Comparison စမ်းသပ် prompt |
| `AGENT_MODEL_PRIMARY` | Session 05 | Primary agent model |
| `AGENT_MODEL_EDITOR` | Session 05 | Editor agent model |
| `AGENT_QUESTION` | Session 05 | Agent မေးခွန်း စမ်းသပ်မှု |
| `PIPELINE_TASK` | Session 06 | Pipeline အတွက် Task |

---

## Breaking Changes

**မရှိပါ** - ပြင်ဆင်မှုအားလုံးသည် backward compatible ဖြစ်သည်။

ရရှိပြီးသား script များသည် ဆက်လက်အလုပ်လုပ်နိုင်ပါသည်။ အသစ်ထည့်သွင်းထားသော feature များမှာ:
- Optional environment variables
- အမှား message များကို တိုးတက်စေခြင်း (functionality မပျက်စီးပါ)
- အပို logging (ဖျောက်နိုင်သည်)
- Type hint များကို ပိုမိုကောင်းမွန်စေခြင်း (runtime အကျိုးသက်ရောက်မှုမရှိပါ)

---

## အကောင်းဆုံးအလေ့အကျင့်များ

### 1. Workshop Utils ကို အမြဲအသုံးပြုပါ
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. အမှားကိုင်တွယ်မှု ပုံစံကို သေချာစွာ အသုံးပြုပါ
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. အသေးစိတ် log ထည့်သွင်းပါ
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Type Hint
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Docstring အပြည့်အစုံ
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

### 6. Environment Variable Support
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Graceful Degradation
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

## အများဆုံးဖြစ်နိုင်သော ပြဿနာများနှင့် ဖြေရှင်းနည်းများ

### ပြဿနာ: Import Error
**ဖြေရှင်းနည်း**: လိုအပ်သော dependency များကို install လုပ်ပါ
```bash
pip install sentence-transformers ragas datasets numpy
```

### ပြဿနာ: Connection Error
**ဖြေရှင်းနည်း**: Foundry Local ကို run လုပ်ထားပါ
```bash
foundry service status
foundry model run phi-4-mini
```

### ပြဿနာ: Model မတွေ့ပါ
**ဖြေရှင်းနည်း**: ရရှိနိုင်သော model များကို စစ်ဆေးပါ
```bash
foundry model ls
foundry model download <alias>
```

### ပြဿနာ: အလုပ်လုပ်ဆောင်မှုနှေးကွေး
**ဖြေရှင်းနည်း**: Model အသေးစားများကို အသုံးပြုပါ သို့မဟုတ် parameter များကို ပြင်ဆင်ပါ
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## နောက်ထပ်လုပ်ဆောင်ရန်

### 1. နမူနာအားလုံးကို စမ်းသပ်ပါ
အထက်ပါ စမ်းသပ်မှု စစ်ဆေးရန်စာရင်းကို အသုံးပြု၍ နမူနာအားလုံးကို စစ်ဆေးပါ။

### 2. Documentation ကို ပြင်ဆင်ပါ
- Session markdown ဖိုင်များကို နမူနာအသစ်များဖြင့် update လုပ်ပါ
- Main README တွင် troubleshooting အပိုင်းထည့်ပါ
- Quick reference guide တစ်ခု ဖန်တီးပါ

### 3. Integration Test များ ဖန်တီးပါ
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Performance Benchmark များ ထည့်သွင်းပါ
အမှားကိုင်တွယ်မှု တိုးတက်မှုများမှ ရရှိသော performance တိုးတက်မှုများကို tracking ပြုလုပ်ပါ။

### 5. အသုံးပြုသူအကြောင်းပြန်မှု
Workshop ပါဝင်သူများထံမှ အောက်ပါအကြောင်းအရာများအတွက် feedback ရယူပါ:
- Error message ရှင်းလင်းမှု
- Documentation ပြည့်စုံမှု
- အသုံးပြုရလွယ်ကူမှု

---

## Resources

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Quick Reference**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migration Notes**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Main Repository**: https://github.com/microsoft/Foundry-Local

---

## Maintenance

### နမူနာအသစ်များ ထည့်သွင်းခြင်း
နမူနာအသစ်များ ဖန်တီးသည့်အခါ အောက်ပါ pattern များကို လိုက်နာပါ:

1. Client management အတွက် `workshop_utils` ကို အသုံးပြုပါ
2. အမှားကိုင်တွယ်မှု အပြည့်အစုံ ထည့်သွင်းပါ
3. Environment variable support ထည့်သွင်းပါ
4. Type hint နှင့် docstring များ ထည့်သွင်းပါ
5. အသေးစိတ် log ထည့်သွင်းပါ
6. Docstring တွင် အသုံးပြုနည်းနမူနာ ထည့်သွင်းပါ
7. SDK documentation link ထည့်သွင်းပါ

### Update များကို ပြန်လည်သုံးသပ်ခြင်း
နမူနာ update များကို ပြန်လည်သုံးသပ်သည့်အခါ အောက်ပါအချက်များကို စစ်ဆေးပါ:
- [ ] I/O operation အားလုံးတွင် အမှားကိုင်တွယ်မှု ရှိပါသလား
- [ ] Public function များတွင် Type hint ရှိပါသလား
- [ ] Docstring အပြည့်အစုံ ရှိပါသလား
- [ ] Environment variable documentation ရှိပါသလား
- [ ] အသုံးပြုသူအကြောင်းပြန်မှု ရှင်းလင်းမှု ရှိပါသလား
- [ ] SDK reference link ရှိပါသလား
- [ ] Code style တစ်ပြိုင်တည်းဖြစ်မှု ရှိပါသလား

---

**အကျဉ်းချုပ်**: Workshop Python နမူနာအားလုံးသည် Foundry Local SDK အကောင်းဆုံးအလေ့အကျင့်များနှင့်အညီ ပြင်ဆင်ပြီး အမှားကိုင်တွယ်မှု တိုးတက်မှု, documentation အပြည့်အစုံနှင့် အသုံးပြုသူအတွေ့အကြုံ တိုးတက်မှုများ ရရှိထားပါသည်။ Breaking changes မရှိပါ - ရှိပြီးသား functionality များကို ထိန်းသိမ်းထားပြီး တိုးတက်စေထားပါသည်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်အချော်များ သို့မဟုတ် အနားယူမှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။