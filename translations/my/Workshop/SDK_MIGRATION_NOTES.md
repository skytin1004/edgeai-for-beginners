<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-08T12:21:40+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "my"
}
-->
# Foundry Local SDK ပြောင်းရွှေ့မှတ်စုများ

## အကျဉ်းချုပ်

Workshop ဖိုလ်ဒါထဲရှိ Python ဖိုင်များအား Foundry Local Python SDK [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) ၏ နောက်ဆုံးပုံစံများနှင့်အညီ ပြင်ဆင်ပြီးဖြစ်သည်။

## ပြောင်းလဲမှုအကျဉ်းချုပ်

### အခြေခံအဆောက်အအုံ (`workshop_utils.py`)

#### တိုးတက်မှုများ:
- **Endpoint Override Support**: `FOUNDRY_LOCAL_ENDPOINT` အပတ်ဝန်းကျင် variable ကို ထည့်သွင်းထားသည်
- **Error Handling တိုးတက်မှု**: အမှားများကို ပိုမိုသေချာစွာ ကိုင်တွယ်နိုင်ရန် error message များကို အသေးစိတ်ထည့်သွင်းထားသည်
- **Caching တိုးတက်မှု**: Multi-endpoint အခြေအနေများအတွက် cache key များတွင် endpoint ကို ထည့်သွင်းထားသည်
- **Exponential Backoff**: ပြန်လည်ကြိုးစားမှု logic ကို ပိုမိုယုံကြည်စိတ်ချရစေရန် exponential backoff ကို အသုံးပြုထားသည်
- **Type Annotations**: IDE support ပိုမိုကောင်းမွန်စေရန် type hints များကို ထည့်သွင်းထားသည်

#### အသစ်ထည့်သွင်းထားသောစွမ်းရည်များ:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### နမူနာအပလီကေးရှင်းများ

#### Session 01: Chat Bootstrap (`chat_bootstrap.py`)
- မူရင်းမော်ဒယ်ကို `phi-3.5-mini` မှ `phi-4-mini` သို့ ပြောင်းလဲထားသည်
- Endpoint override support ထည့်သွင်းထားသည်
- SDK ကို ရည်ညွှန်းထားသော documentation တိုးတက်မှု

#### Session 02: RAG Pipeline (`rag_pipeline.py`)
- မူရင်းမော်ဒယ်ကို `phi-4-mini` သို့ ပြောင်းလဲထားသည်
- Endpoint override support ထည့်သွင်းထားသည်
- Environment variable အသေးစိတ်များပါဝင်သော documentation တိုးတက်မှု

#### Session 02: RAG Evaluation (`rag_eval_ragas.py`)
- မော်ဒယ် default များကို ပြောင်းလဲထားသည်
- Endpoint configuration ထည့်သွင်းထားသည်
- Error handling တိုးတက်မှု

#### Session 03: Benchmarking (`benchmark_oss_models.py`)
- မူရင်းမော်ဒယ်စာရင်းကို `phi-4-mini` ထည့်သွင်းထားသည်
- Environment variable documentation အပြည့်အစုံ
- Function documentation တိုးတက်မှု
- Endpoint override support ထည့်သွင်းထားသည်

#### Session 04: Model Comparison (`model_compare.py`)
- Default LLM ကို `gpt-oss-20b` မှ `qwen2.5-7b` သို့ ပြောင်းလဲထားသည်
- Endpoint configuration ထည့်သွင်းထားသည်
- Documentation တိုးတက်မှု

#### Session 05: Multi-Agent Orchestration (`agents_orchestrator.py`)
- Type hints ထည့်သွင်းထားသည် (`str | None` ကို `Optional[str]` သို့ ပြောင်းလဲထားသည်)
- Agent class documentation တိုးတက်မှု
- Endpoint override support ထည့်သွင်းထားသည်
- Initialization pattern တိုးတက်မှု

#### Session 06: Model Router (`models_router.py`)
- Endpoint configuration ထည့်သွင်းထားသည်
- Intent detection documentation တိုးတက်မှု
- Routing logic documentation တိုးတက်မှု

#### Session 06: Pipeline (`models_pipeline.py`)
- Function documentation အပြည့်အစုံ
- အဆင့်ဆင့် documentation တိုးတက်မှု
- Error handling တိုးတက်မှု

### Scripts

#### Benchmark Export (`export_benchmark_markdown.py`)
- Endpoint override support ထည့်သွင်းထားသည်
- Default models ပြောင်းလဲထားသည်
- Function documentation တိုးတက်မှု
- Error handling တိုးတက်မှု

#### CLI Linter (`lint_markdown_cli.py`)
- SDK reference links ထည့်သွင်းထားသည်
- Usage documentation တိုးတက်မှု

### Tests

#### Smoke Tests (`smoke.py`)
- Endpoint override support ထည့်သွင်းထားသည်
- Documentation တိုးတက်မှု
- Test case documentation တိုးတက်မှု
- Error reporting ပိုမိုကောင်းမွန်စေရန် ပြင်ဆင်ထားသည်

## အပတ်ဝန်းကျင် Variables

နမူနာအားလုံးသည် အောက်ပါ environment variables များကို အထောက်အပံ့ပေးသည်:

### အခြေခံ Configuration
- `FOUNDRY_LOCAL_ALIAS` - အသုံးပြုမည့် Model alias (default သည် နမူနာအလိုက် မတူညီနိုင်သည်)
- `FOUNDRY_LOCAL_ENDPOINT` - Service endpoint ကို override လုပ်ရန် (optional)
- `SHOW_USAGE` - Token အသုံးပြုမှု စာရင်းပြရန် (default: "0")
- `RETRY_ON_FAIL` - Retry logic ကို enable လုပ်ရန် (default: "1")
- `RETRY_BACKOFF` - Retry အချိန်နှောင့်နှေးမှု စတင် seconds (default: "1.0")

### နမူနာအလိုက်
- `EMBED_MODEL` - RAG နမူနာများအတွက် Embedding model
- `BENCH_MODELS` - Benchmarking အတွက် Comma-separated models
- `BENCH_ROUNDS` - Benchmark rounds အရေအတွက်
- `BENCH_PROMPT` - Benchmark အတွက် Test prompt
- `BENCH_STREAM` - First-token latency ကိုတိုင်းတာရန်
- `RAG_QUESTION` - RAG နမူနာများအတွက် Test question
- `AGENT_MODEL_PRIMARY` - Primary agent model
- `AGENT_MODEL_EDITOR` - Editor agent model
- `SLM_ALIAS` - Small language model alias
- `LLM_ALIAS` - Large language model alias

## SDK အကောင်းဆုံးအလေ့အကျင့်များ

### 1. Client Initialization ကို သေချာပြုလုပ်ခြင်း
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

### 2. Model အချက်အလက် ရယူခြင်း
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Error Handling
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Exponential Backoff ဖြင့် Retry Logic
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

### 5. Streaming Support
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

## Custom နမူနာများအတွက် ပြောင်းရွှေ့လမ်းညွှန်

သင်အသစ်သော နမူနာများဖန်တီးခြင်း သို့မဟုတ် ရှိပြီးသားနမူနာများကို ပြင်ဆင်လိုပါက:

1. **`workshop_utils.py` helper များကို အသုံးပြုပါ**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Endpoint override ကို အထောက်အပံ့ပေးပါ**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Documentation အပြည့်အစုံ ထည့်သွင်းပါ**:
   - Environment variables ကို docstring တွင် ထည့်သွင်းပါ
   - SDK reference link
   - Usage နမူနာများ

4. **Type hints ကို အသုံးပြုပါ**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Error handling ကို သေချာပြုလုပ်ပါ**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## စမ်းသပ်ခြင်း

နမူနာအားလုံးကို အောက်ပါနည်းဖြင့် စမ်းသပ်နိုင်သည်:

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

## SDK Documentation References

- **Main Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Documentation**: SDK repository တွင် နောက်ဆုံး API docs ကို ကြည့်ပါ

## Breaking Changes

### မရှိပါ
ပြောင်းလဲမှုများသည် အနောက်ဆုံးပေါ်နည်းစနစ်များနှင့်အညီဖြစ်ပြီး အနောက် compatibility ကို ထိခိုက်မှုမရှိပါ။ ပြောင်းလဲမှုများသည် အဓိကအားဖြင့်:
- Optional features အသစ်များထည့်သွင်းထားသည် (endpoint override)
- Error handling တိုးတက်မှု
- Documentation တိုးတက်မှု
- မော်ဒယ်အမည်များကို လက်ရှိအကြံပြုချက်များနှင့်အညီ update လုပ်ထားသည်

### Optional Enhancements
သင်၏ code ကို အောက်ပါအတိုင်း update လုပ်လိုနိုင်သည်:
- `FOUNDRY_LOCAL_ENDPOINT` ကို အသုံးပြု၍ endpoint ကို ထိန်းချုပ်ရန်
- `SHOW_USAGE=1` ကို အသုံးပြု၍ token usage visibility ရရှိရန်
- Updated model defaults (`phi-4-mini` ကို `phi-3.5-mini` အစား)

## အများဆုံးတွေ့ရသောပြဿနာများနှင့် ဖြေရှင်းနည်းများ

### ပြဿနာ: "Client initialization failed"
**ဖြေရှင်းနည်း**: Foundry Local service ကို run လုပ်ထားကြောင်း သေချာပါ:
```bash
foundry service start
foundry model run phi-4-mini
```

### ပြဿနာ: "Model not found"
**ဖြေရှင်းနည်း**: ရရှိနိုင်သော models ကို စစ်ဆေးပါ:
```bash
foundry model list
```

### ပြဿနာ: Endpoint connection errors
**ဖြေရှင်းနည်း**: Endpoint ကို စစ်ဆေးပါ:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## နောက်တစ်ဆင့်များ

1. **Module08 နမူနာများကို update လုပ်ပါ**: Module08/samples တွင် အလားတူ pattern များကို အသုံးပြုပါ
2. **Integration tests ထည့်သွင်းပါ**: Comprehensive test suite ဖန်တီးပါ
3. **Performance benchmarking**: ပြောင်းလဲမှုမတိုင်မီ/ပြီးနောက် performance ကို နှိုင်းယှဉ်ပါ
4. **Documentation updates**: နောက်ဆုံးပုံစံ pattern များနှင့်အညီ main README ကို update လုပ်ပါ

## Contribution Guidelines

နမူနာအသစ်များထည့်သွင်းသောအခါ:
1. `workshop_utils.py` ကို အသုံးပြု၍ consistency ရရှိစေရန်
2. ရှိပြီးသားနမူနာ pattern ကို လိုက်နာပါ
3. Comprehensive docstrings ထည့်သွင်းပါ
4. SDK reference links ထည့်သွင်းပါ
5. Endpoint override ကို အထောက်အပံ့ပေးပါ
6. Type hints ကို ထည့်သွင်းပါ
7. Docstring တွင် usage နမူနာများ ထည့်သွင်းပါ

## Version Compatibility

ပြောင်းလဲမှုများသည် အောက်ပါများနှင့် အညီဖြစ်သည်:
- `foundry-local-sdk` (latest)
- `openai>=1.30.0`
- Python 3.8+

---

**နောက်ဆုံး Update**: 2025-01-08  
**Maintainer**: EdgeAI Workshop Team  
**SDK Version**: Foundry Local SDK (latest 0.7.117+67073234e7)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။