<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-11T12:02:34+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "ta"
}
-->
# Foundry Local SDK மாற்றம் குறிப்பு

## கண்ணோட்டம்

Workshop கோப்புறையில் உள்ள அனைத்து Python கோப்புகளும் [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) இன் சமீபத்திய முறைமைகளை பின்பற்ற하도록 புதுப்பிக்கப்பட்டுள்ளது.

## மாற்றங்களின் சுருக்கம்

### மைய அடுக்கமைப்பு (`workshop_utils.py`)

#### மேம்பட்ட அம்சங்கள்:
- **Endpoint Override ஆதரவு**: `FOUNDRY_LOCAL_ENDPOINT` சூழல் மாறி ஆதரவு சேர்க்கப்பட்டது
- **மேம்பட்ட பிழை கையாளுதல்**: விரிவான பிழை செய்திகளுடன் சிறந்த εξαίρεση கையாளுதல்
- **மேம்பட்ட Cache**: பல endpoint சூழல்களுக்கு cache கீக்கள் endpoint உடன் சேர்க்கப்பட்டுள்ளது
- **Exponential Backoff**: மீண்டும் முயற்சிக்கும் தர்க்கம் Exponential Backoff பயன்படுத்துகிறது
- **Type Annotations**: IDE ஆதரவை மேம்படுத்த விரிவான Type Hints சேர்க்கப்பட்டது

#### புதிய திறன்கள்:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### மாதிரி பயன்பாடுகள்

#### அமர்வு 01: Chat Bootstrap (`chat_bootstrap.py`)
- இயல்புநிலை மாடல் `phi-3.5-mini` இருந்து `phi-4-mini` ஆக புதுப்பிக்கப்பட்டது
- Endpoint Override ஆதரவு சேர்க்கப்பட்டது
- SDK குறிப்பு இணைப்புகளுடன் ஆவணங்கள் மேம்படுத்தப்பட்டது

#### அமர்வு 02: RAG Pipeline (`rag_pipeline.py`)
- `phi-4-mini` ஐ இயல்புநிலை மாடலாக புதுப்பிக்கப்பட்டது
- Endpoint Override ஆதரவு சேர்க்கப்பட்டது
- சூழல் மாறி விவரங்களுடன் ஆவணங்கள் மேம்படுத்தப்பட்டது

#### அமர்வு 02: RAG மதிப்பீடு (`rag_eval_ragas.py`)
- மாடல் இயல்புநிலைகள் புதுப்பிக்கப்பட்டது
- Endpoint அமைப்பு சேர்க்கப்பட்டது
- பிழை கையாளுதல் மேம்படுத்தப்பட்டது

#### அமர்வு 03: Benchmarking (`benchmark_oss_models.py`)
- இயல்புநிலை மாடல் பட்டியல் `phi-4-mini` உடன் புதுப்பிக்கப்பட்டது
- விரிவான சூழல் மாறி ஆவணங்கள் சேர்க்கப்பட்டது
- செயல்பாட்டு ஆவணங்கள் மேம்படுத்தப்பட்டது
- Endpoint Override ஆதரவு முழுவதும் சேர்க்கப்பட்டது

#### அமர்வு 04: மாடல் ஒப்பீடு (`model_compare.py`)
- இயல்புநிலை LLM `gpt-oss-20b` இருந்து `qwen2.5-7b` ஆக மாற்றப்பட்டது
- Endpoint அமைப்பு சேர்க்கப்பட்டது
- ஆவணங்கள் மேம்படுத்தப்பட்டது

#### அமர்வு 05: பல முகவர் ஒருங்கிணைப்பு (`agents_orchestrator.py`)
- Type Hints சேர்க்கப்பட்டது (`str | None` ஐ `Optional[str]` ஆக மாற்றப்பட்டது)
- Agent வகுப்பு ஆவணங்கள் மேம்படுத்தப்பட்டது
- Endpoint Override ஆதரவு சேர்க்கப்பட்டது
- Initialization முறை மேம்படுத்தப்பட்டது

#### அமர்வு 06: மாடல் Router (`models_router.py`)
- Endpoint அமைப்பு சேர்க்கப்பட்டது
- Intent Detection ஆவணங்கள் மேம்படுத்தப்பட்டது
- Routing Logic ஆவணங்கள் மேம்படுத்தப்பட்டது

#### அமர்வு 06: Pipeline (`models_pipeline.py`)
- விரிவான செயல்பாட்டு ஆவணங்கள் சேர்க்கப்பட்டது
- படிப்படியாக ஆவணங்கள் மேம்படுத்தப்பட்டது
- பிழை கையாளுதல் மேம்படுத்தப்பட்டது

### ஸ்கிரிப்ட்கள்

#### Benchmark Export (`export_benchmark_markdown.py`)
- Endpoint Override ஆதரவு சேர்க்கப்பட்டது
- இயல்புநிலை மாடல்கள் புதுப்பிக்கப்பட்டது
- செயல்பாட்டு ஆவணங்கள் மேம்படுத்தப்பட்டது
- பிழை கையாளுதல் மேம்படுத்தப்பட்டது

#### CLI Linter (`lint_markdown_cli.py`)
- SDK குறிப்பு இணைப்புகள் சேர்க்கப்பட்டது
- பயன்பாட்டு ஆவணங்கள் மேம்படுத்தப்பட்டது

### சோதனைகள்

#### Smoke Tests (`smoke.py`)
- Endpoint Override ஆதரவு சேர்க்கப்பட்டது
- ஆவணங்கள் மேம்படுத்தப்பட்டது
- சோதனை வழக்குகள் ஆவணங்கள் மேம்படுத்தப்பட்டது
- சிறந்த பிழை அறிக்கை

## சூழல் மாறிகள்

அனைத்து மாதிரிகளும் இப்போது இந்த சூழல் மாறிகளை ஆதரிக்கின்றன:

### மைய அமைப்பு
- `FOUNDRY_LOCAL_ALIAS` - பயன்படுத்த வேண்டிய மாடல் Alias (மாதிரி அடிப்படையில் இயல்புநிலை மாறும்)
- `FOUNDRY_LOCAL_ENDPOINT` - சேவை Endpoint Override (விருப்பத்தேர்வு)
- `SHOW_USAGE` - Token பயன்பாட்டு புள்ளிவிவரங்களை காண்பிக்கவும் (இயல்புநிலை: "0")
- `RETRY_ON_FAIL` - மீண்டும் முயற்சிக்கும் தர்க்கத்தை இயக்கவும் (இயல்புநிலை: "1")
- `RETRY_BACKOFF` - ஆரம்ப Retry தாமதம் விநாடிகளில் (இயல்புநிலை: "1.0")

### மாதிரி-சிறப்பு
- `EMBED_MODEL` - RAG மாதிரிகளுக்கான Embedding மாடல்
- `BENCH_MODELS` - Benchmarking க்கான கமா-பிரிக்கப்பட்ட மாடல்கள்
- `BENCH_ROUNDS` - Benchmark சுற்றுகளின் எண்ணிக்கை
- `BENCH_PROMPT` - Benchmarks க்கான சோதனை Prompt
- `BENCH_STREAM` - முதல் Token தாமதத்தை அளவிடவும்
- `RAG_QUESTION` - RAG மாதிரிகளுக்கான சோதனை கேள்வி
- `AGENT_MODEL_PRIMARY` - முதன்மை Agent மாடல்
- `AGENT_MODEL_EDITOR` - Editor Agent மாடல்
- `SLM_ALIAS` - சிறிய மொழி மாடல் Alias
- `LLM_ALIAS` - பெரிய மொழி மாடல் Alias

## SDK சிறந்த நடைமுறைகள் செயல்படுத்தப்பட்டது

### 1. சரியான Client Initialization
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. மாடல் தகவல் பெறுதல்
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. பிழை கையாளுதல்
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Exponential Backoff உடன் Retry Logic
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Streaming ஆதரவு
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## தனிப்பயன் மாதிரிகளுக்கான மாற்ற வழிகாட்டி

புதிய மாதிரிகளை உருவாக்க அல்லது உள்ளதை புதுப்பிக்க:

1. **`workshop_utils.py` உதவிகளை பயன்படுத்தவும்**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Endpoint Override ஆதரவை ஆதரிக்கவும்**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **விரிவான ஆவணங்களை சேர்க்கவும்**:
   - Docstring இல் சூழல் மாறிகள்
   - SDK குறிப்பு இணைப்பு
   - பயன்பாட்டு உதாரணங்கள்

4. **Type Hints பயன்படுத்தவும்**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **சரியான பிழை கையாளுதலை செயல்படுத்தவும்**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## சோதனை

அனைத்து மாதிரிகளும் சோதிக்கப்படலாம்:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
python Workshop/samples/session01/chat_bootstrap.py "Test question"
python Workshop/samples/session02/rag_pipeline.py

# Run benchmark
python Workshop/samples/session03/benchmark_oss_models.py

# Run smoke tests
python -m Workshop.tests.smoke
```

## SDK ஆவண குறிப்பு இணைப்புகள்

- **முக்கிய Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API ஆவணங்கள்**: SDK Repository இல் சமீபத்திய API ஆவணங்களை சரிபார்க்கவும்

## முக்கிய மாற்றங்கள்

### எதிர்பார்க்கப்படவில்லை
அனைத்து மாற்றங்களும் பின்தங்கிய இணக்கத்துடன் உள்ளன. புதுப்பிப்புகள் முக்கியமாக:
- புதிய விருப்ப அம்சங்களை சேர்க்கிறது (Endpoint Override)
- பிழை கையாளுதலை மேம்படுத்துகிறது
- ஆவணங்களை மேம்படுத்துகிறது
- இயல்புநிலை மாடல் பெயர்களை தற்போதைய பரிந்துரைகளுக்கு புதுப்பிக்கிறது

### விருப்ப மேம்பாடுகள்
உங்கள் குறியீட்டை புதுப்பிக்க விரும்பலாம்:
- Explicit Endpoint கட்டுப்பாட்டுக்கு `FOUNDRY_LOCAL_ENDPOINT` பயன்படுத்தவும்
- Token பயன்பாட்டு காட்சிக்கு `SHOW_USAGE=1` பயன்படுத்தவும்
- புதுப்பிக்கப்பட்ட மாடல் இயல்புநிலைகள் (`phi-4-mini` `phi-3.5-mini` இற்கு பதிலாக)

## பொதுவான பிரச்சினைகள் & தீர்வுகள்

### பிரச்சினை: "Client Initialization தோல்வியடைந்தது"
**தீர்வு**: Foundry Local சேவை இயங்குகிறது என்பதை உறுதிப்படுத்தவும்:
```bash
foundry service start
foundry model run phi-4-mini
```

### பிரச்சினை: "மாடல் கிடைக்கவில்லை"
**தீர்வு**: கிடைக்கக்கூடிய மாடல்களை சரிபார்க்கவும்:
```bash
foundry model list
```

### பிரச்சினை: Endpoint இணைப்பு பிழைகள்
**தீர்வு**: Endpoint ஐ சரிபார்க்கவும்:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## அடுத்த படிகள்

1. **Module08 மாதிரிகளை புதுப்பிக்கவும்**: Module08/samples இல் இதே முறைமைகளை பயன்படுத்தவும்
2. **ஒருங்கிணைப்பு சோதனைகள் சேர்க்கவும்**: விரிவான சோதனை தொகுப்பை உருவாக்கவும்
3. **செயல்திறன் மதிப்பீடு**: முன்னால்/பின்னால் செயல்திறனை ஒப்பிடவும்
4. **ஆவண புதுப்பிப்புகள்**: புதிய முறைமைகளுடன் முக்கிய README ஐ புதுப்பிக்கவும்

## பங்களிப்பு வழிகாட்டிகள்

புதிய மாதிரிகளை சேர்க்கும்போது:
1. `workshop_utils.py` ஐ ஒத்திசைவிற்கு பயன்படுத்தவும்
2. உள்ள மாதிரிகளில் உள்ள முறைமையை பின்பற்றவும்
3. விரிவான Docstrings சேர்க்கவும்
4. SDK குறிப்பு இணைப்புகளை சேர்க்கவும்
5. Endpoint Override ஆதரவை ஆதரிக்கவும்
6. சரியான Type Hints சேர்க்கவும்
7. Docstring இல் பயன்பாட்டு உதாரணங்களை சேர்க்கவும்

## பதிப்பு இணக்கத்தன்மை

இந்த புதுப்பிப்புகள் இணக்கமானவை:
- `foundry-local-sdk` (சமீபத்தியது)
- `openai>=1.30.0`
- Python 3.8+

---

**இறுதியாக புதுப்பிக்கப்பட்டது**: 2025-01-08  
**பராமரிப்பாளர்**: EdgeAI Workshop குழு  
**SDK பதிப்பு**: Foundry Local SDK (சமீபத்தியது 0.7.117+67073234e7)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.