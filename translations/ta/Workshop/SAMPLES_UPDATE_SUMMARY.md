<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5506309052b4f332914e36b518f11b14",
  "translation_date": "2025-10-11T12:01:16+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "ta"
}
-->
# பணிமனை மாதிரிகள் - Foundry Local SDK புதுப்பிப்பு சுருக்கம்

## மேலோட்டம்

`Workshop/samples` கோப்பகத்தில் உள்ள அனைத்து Python மாதிரிகளும் Foundry Local SDK சிறந்த நடைமுறைகளை பின்பற்றவும், பணிமனை முழுவதும் ஒரே மாதிரியானதாக இருக்கவும் புதுப்பிக்கப்பட்டுள்ளன.

**தேதி**: அக்டோபர் 8, 2025  
**வாய்ப்பு**: 6 பணிமனை அமர்வுகளில் 9 Python கோப்புகள்  
**முக்கிய கவனம்**: பிழை கையாளுதல், ஆவணங்கள், SDK முறை, பயனர் அனுபவம்

---

## புதுப்பிக்கப்பட்ட கோப்புகள்

### அமர்வு 01: தொடங்குதல்
- ✅ `chat_bootstrap.py` - அடிப்படை உரையாடல் மற்றும் ஸ்ட்ரீமிங் எடுத்துக்காட்டுகள்

### அமர்வு 02: RAG தீர்வுகள்
- ✅ `rag_pipeline.py` - எம்பெடிங்ஸ் மூலம் RAG செயல்படுத்தல்
- ✅ `rag_eval_ragas.py` - RAGAS அளவுகோல்களுடன் RAG மதிப்பீடு

### அமர்வு 03: திறந்த மூல மாதிரிகள்
- ✅ `benchmark_oss_models.py` - பல மாதிரி ஒப்பீட்டு சோதனை

### அமர்வு 04: நவீன மாதிரிகள்
- ✅ `model_compare.py` - SLM மற்றும் LLM ஒப்பீடு

### அமர்வு 05: AI இயக்கப்படும் முகவர்கள்
- ✅ `agents_orchestrator.py` - பல முகவர் ஒருங்கிணைப்பு

### அமர்வு 06: கருவிகளாக மாதிரிகள்
- ✅ `models_router.py` - நோக்கத்தை அடிப்படையாகக் கொண்ட மாதிரி வழிமுறை
- ✅ `models_pipeline.py` - பல படி வழிமுறை குழாய்

### ஆதரவு கட்டமைப்பு
- ✅ `workshop_utils.py` - ஏற்கனவே சிறந்த நடைமுறைகளை பின்பற்றுகிறது (மாற்றங்கள் தேவையில்லை)

---

## முக்கிய மேம்பாடுகள்

### 1. மேம்பட்ட பிழை கையாளுதல்

**முன்பு:**
```python
manager, client, model_id = get_client(alias)
```

**பிறகு:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**நன்மைகள்:**
- தெளிவான பிழை செய்திகளுடன் மென்மையான பிழை கையாளுதல்
- செயல்படுத்தக்கூடிய பிழை தீர்வு குறிப்புகள்
- ஸ்கிரிப்டிங் சரியான வெளியீடு குறியீடுகள்

### 2. சிறந்த இறக்குமதி மேலாண்மை

**முன்பு:**
```python
from sentence_transformers import SentenceTransformer
```

**பிறகு:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**நன்மைகள்:**
- சார்புகள் இல்லாதபோது தெளிவான வழிகாட்டுதல்
- குழப்பமான இறக்குமதி பிழைகளைத் தவிர்க்கிறது
- பயனர் நட்பு நிறுவல் வழிமுறைகள்

### 3. விரிவான ஆவணங்கள்

**அனைத்து மாதிரிகளுக்கும் சேர்க்கப்பட்டது:**
- ஆவணங்களில் சூழல் மாறி விளக்கம்
- SDK குறிப்பு இணைப்புகள்
- பயன்பாட்டு எடுத்துக்காட்டுகள்
- விரிவான செயல்பாடு/அளவுரு ஆவணங்கள்
- IDE ஆதரவுக்கான வகை குறிப்புகள்

**எடுத்துக்காட்டு:**
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

### 4. மேம்பட்ட பயனர் கருத்து

**தகவல் வழங்கும் பதிவு சேர்க்கப்பட்டது:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**முன்னேற்றக் குறியீடுகள்:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**கட்டமைக்கப்பட்ட வெளியீடு:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. வலுவான ஒப்பீட்டு சோதனை

**அமர்வு 03 மேம்பாடுகள்:**
- மாதிரி ஒவ்வொன்றிற்கும் பிழை கையாளுதல் (தோல்வியின்போது தொடர்கிறது)
- விரிவான முன்னேற்ற அறிக்கைகள்
- சரியான வெப்பமூட்டல் சுற்றங்கள்
- முதல் டோக்கன் தாமத அளவீடு ஆதரவு
- கட்டமைக்கப்பட்ட கட்டங்களின் தெளிவான பிரிவு

### 6. ஒரே மாதிரியான வகை குறிப்புகள்

**அனைத்திலும் சேர்க்கப்பட்டது:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**நன்மைகள்:**
- சிறந்த IDE தானியங்கு நிறைவு
- ஆரம்ப பிழை கண்டறிதல்
- தானாகவே ஆவணமாகும் குறியீடு

### 7. மேம்பட்ட மாதிரி வழிமுறை

**அமர்வு 06 மேம்பாடுகள்:**
- விரிவான நோக்க கண்டறிதல் ஆவணங்கள்
- மாதிரி தேர்வு அல்காரிதம் விளக்கம்
- விரிவான வழிமுறை பதிவுகள்
- சோதனை வெளியீடு வடிவமைப்பு
- தொகுதி சோதனையில் பிழை மீட்பு

### 8. பல முகவர் ஒருங்கிணைப்பு

**அமர்வு 05 மேம்பாடுகள்:**
- கட்டம்-கட்டமாக முன்னேற்ற அறிக்கைகள்
- முகவர் ஒவ்வொன்றிற்கும் பிழை கையாளுதல்
- தெளிவான குழாய் அமைப்பு
- சிறந்த நினைவக மேலாண்மை ஆவணங்கள்

---

## சோதனை சரிபார்ப்பு பட்டியல்

### தேவையானவை
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### ஒவ்வொரு மாதிரியையும் சோதிக்கவும்

#### அமர்வு 01
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What is edge AI?"
```

#### அமர்வு 02
```bash
cd Workshop/samples/session02

# RAG pipeline
python rag_pipeline.py

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python rag_eval_ragas.py
```

#### அமர்வு 03
```bash
cd Workshop/samples/session03

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python benchmark_oss_models.py
```

#### அமர்வு 04
```bash
cd Workshop/samples/session04

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python model_compare.py
```

#### அமர்வு 05
```bash
cd Workshop/samples/session05

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python agents_orchestrator.py
```

#### அமர்வு 06
```bash
cd Workshop/samples/session06

# Intent-based routing
python models_router.py

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python models_pipeline.py
```

---

## சூழல் மாறிகள் குறிப்பு

### உலகளாவிய (அனைத்து மாதிரிகளுக்கும்)
| மாறி | விளக்கம் | இயல்புநிலை |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | பயன்படுத்த வேண்டிய மாதிரி பெயர் | மாதிரிக்கு மாறுபடும் |
| `FOUNDRY_LOCAL_ENDPOINT` | சேவை முடிவுக்கான மாற்று | தானாக கண்டறியப்படும் |
| `SHOW_USAGE` | டோக்கன் பயன்பாட்டைக் காட்டவும் | `0` |
| `RETRY_ON_FAIL` | மீண்டும் முயற்சி செயல்படுத்தவும் | `1` |
| `RETRY_BACKOFF` | ஆரம்ப மீண்டும் முயற்சி தாமதம் | `1.0` |

### மாதிரி-சிறப்பு
| மாறி | பயன்படுத்தும் | விளக்கம் |
|----------|---------|-------------|
| `EMBED_MODEL` | அமர்வு 02 | எம்பெடிங் மாதிரி பெயர் |
| `RAG_QUESTION` | அமர்வு 02 | RAG க்கான சோதனை கேள்வி |
| `BENCH_MODELS` | அமர்வு 03 | ஒப்பீட்டு சோதனை செய்யும் மாதிரிகள் (கமா பிரிக்கப்பட்டவை) |
| `BENCH_ROUNDS` | அமர்வு 03 | ஒப்பீட்டு சோதனை சுற்றுகள் எண்ணிக்கை |
| `BENCH_PROMPT` | அமர்வு 03 | ஒப்பீட்டு சோதனைக்கு சோதனை உத்தேசம் |
| `BENCH_STREAM` | அமர்வு 03 | முதல் டோக்கன் தாமதத்தை அளவிடவும் |
| `SLM_ALIAS` | அமர்வு 04 | சிறிய மொழி மாதிரி |
| `LLM_ALIAS` | அமர்வு 04 | பெரிய மொழி மாதிரி |
| `COMPARE_PROMPT` | அமர்வு 04 | ஒப்பீட்டு சோதனை உத்தேசம் |
| `AGENT_MODEL_PRIMARY` | அமர்வு 05 | முதன்மை முகவர் மாதிரி |
| `AGENT_MODEL_EDITOR` | அமர்வு 05 | எடிட்டர் முகவர் மாதிரி |
| `AGENT_QUESTION` | அமர்வு 05 | முகவர்களுக்கு சோதனை கேள்வி |
| `PIPELINE_TASK` | அமர்வு 06 | குழாய் பணிகள் |

---

## முக்கிய மாற்றங்கள்

**இல்லை** - அனைத்து மாற்றங்களும் பின்தங்கிய இணக்கத்துடன் உள்ளன.

இருப்பிலுள்ள ஸ்கிரிப்ட்கள் தொடர்ந்து செயல்படும். புதிய அம்சங்கள்:
- விருப்பமான சூழல் மாறிகள்
- மேம்பட்ட பிழை செய்திகள் (செயல்பாட்டை பாதிக்காது)
- கூடுதல் பதிவு (மறைக்க முடியும்)
- சிறந்த வகை குறிப்புகள் (இயக்க நேர தாக்கம் இல்லை)

---

## செயல்படுத்தப்பட்ட சிறந்த நடைமுறைகள்

### 1. எப்போதும் Workshop Utils ஐ பயன்படுத்தவும்
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. சரியான பிழை கையாளுதல் முறை
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. தகவல் வழங்கும் பதிவு
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. வகை குறிப்புகள்
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. விரிவான ஆவணங்கள்
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

### 6. சூழல் மாறி ஆதரவு
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. மென்மையான செயலிழப்பு
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

## பொதுவான பிரச்சினைகள் & தீர்வுகள்

### பிரச்சினை: இறக்குமதி பிழைகள்
**தீர்வு:** குறைவான சார்புகளை நிறுவவும்
```bash
pip install sentence-transformers ragas datasets numpy
```

### பிரச்சினை: இணைப்பு பிழைகள்
**தீர்வு:** Foundry Local இயங்குகிறதா என்பதை உறுதிப்படுத்தவும்
```bash
foundry service status
foundry model run phi-4-mini
```

### பிரச்சினை: மாதிரி கிடைக்கவில்லை
**தீர்வு:** கிடைக்கும் மாதிரிகளை சரிபார்க்கவும்
```bash
foundry model ls
foundry model download <alias>
```

### பிரச்சினை: மெதுவான செயல்திறன்
**தீர்வு:** சிறிய மாதிரிகளைப் பயன்படுத்தவும் அல்லது அளவுருக்களை சரிசெய்யவும்
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## அடுத்த படிகள்

### 1. அனைத்து மாதிரிகளையும் சோதிக்கவும்
மேலே உள்ள சோதனை சரிபார்ப்பு பட்டியலைப் பயன்படுத்தி அனைத்து மாதிரிகளும் சரியாக செயல்படுகிறதா என்பதை உறுதிப்படுத்தவும்.

### 2. ஆவணங்களை புதுப்பிக்கவும்
- புதிய எடுத்துக்காட்டுகளுடன் அமர்வு மார்க்டவுன் கோப்புகளை புதுப்பிக்கவும்
- முக்கிய README இல் பிழை தீர்வு பிரிவைச் சேர்க்கவும்
- விரைவான குறிப்பு வழிகாட்டியை உருவாக்கவும்

### 3. ஒருங்கிணைப்பு சோதனைகளை உருவாக்கவும்
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. செயல்திறன் ஒப்பீட்டு சோதனைகளைச் சேர்க்கவும்
பிழை கையாளுதல் மேம்பாடுகளிலிருந்து செயல்திறன் மேம்பாடுகளை கண்காணிக்கவும்.

### 5. பயனர் கருத்து
பணிமனை பங்கேற்பாளர்களிடமிருந்து கருத்துக்களை சேகரிக்கவும்:
- பிழை செய்தி தெளிவு
- ஆவணங்களின் முழுமை
- பயன்படுத்தும் எளிமை

---

## வளங்கள்

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **விரைவான குறிப்பு**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **மாற்றம் குறிப்புகள்**: `Workshop/SDK_MIGRATION_NOTES.md`
- **முக்கிய களஞ்சியம்**: https://github.com/microsoft/Foundry-Local

---

## பராமரிப்பு

### புதிய மாதிரிகளைச் சேர்க்க
புதிய மாதிரிகளை உருவாக்கும் போது இந்த நடைமுறைகளை பின்பற்றவும்:

1. `workshop_utils` ஐ கிளையண்ட் மேலாண்மைக்கு பயன்படுத்தவும்
2. விரிவான பிழை கையாளுதலைச் சேர்க்கவும்
3. சூழல் மாறி ஆதரவைச் சேர்க்கவும்
4. வகை குறிப்புகள் மற்றும் ஆவணங்களைச் சேர்க்கவும்
5. தகவல் வழங்கும் பதிவுகளைச் சேர்க்கவும்
6. ஆவணத்தில் பயன்பாட்டு எடுத்துக்காட்டுகளைச் சேர்க்கவும்
7. SDK ஆவண இணைப்புகளைச் சேர்க்கவும்

### புதுப்பிப்புகளை மதிப்பாய்வு செய்ய
மாதிரி புதுப்பிப்புகளை மதிப்பாய்வு செய்யும்போது, பின்வரும் விஷயங்களைச் சரிபார்க்கவும்:
- [ ] அனைத்து I/O செயல்பாடுகளிலும் பிழை கையாளுதல்
- [ ] பொது செயல்பாடுகளில் வகை குறிப்புகள்
- [ ] விரிவான ஆவணங்கள்
- [ ] சூழல் மாறி ஆவணங்கள்
- [ ] பயனருக்கு தகவல் வழங்கும் கருத்து
- [ ] SDK குறிப்பு இணைப்புகள்
- [ ] ஒரே மாதிரியான குறியீட்டு பாணி

---

**சுருக்கம்**: அனைத்து பணிமனை Python மாதிரிகளும் Foundry Local SDK சிறந்த நடைமுறைகளை பின்பற்றும் வகையில் புதுப்பிக்கப்பட்டுள்ளன. மேம்பட்ட பிழை கையாளுதல், விரிவான ஆவணங்கள் மற்றும் மேம்பட்ட பயனர் அனுபவத்துடன். எந்தவிதமான செயல்பாட்டு பாதிப்பும் இல்லை - அனைத்து உள்ளமைவுகளும் தொடர்ச்சியாக செயல்படும் மற்றும் மேம்படுத்தப்பட்டுள்ளன.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.