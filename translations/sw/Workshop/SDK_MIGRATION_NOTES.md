<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-09T21:42:08+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "sw"
}
-->
# Maelezo ya Uhamishaji wa Foundry Local SDK

## Muhtasari

Faili zote za Python katika folda ya Workshop zimesasishwa kufuata mifumo ya hivi karibuni kutoka kwa [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Muhtasari wa Mabadiliko

### Miundombinu ya Msingi (`workshop_utils.py`)

#### Vipengele Vilivyoboreshwa:
- **Msaada wa Kubadilisha Endpoint**: Imeongezwa msaada wa mazingira ya `FOUNDRY_LOCAL_ENDPOINT`
- **Ushughulikiaji Bora wa Makosa**: Ushughulikiaji wa makosa na ujumbe wa kina wa makosa
- **Uboreshaji wa Caching**: Funguo za cache sasa zinajumuisha endpoint kwa hali ya multi-endpoint
- **Exponential Backoff**: Mantiki ya kurudia sasa inatumia exponential backoff kwa uaminifu bora
- **Maelezo ya Aina**: Imeongezwa maelezo ya aina kwa kina kwa msaada bora wa IDE

#### Uwezo Mpya:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Programu za Mfano

#### Kipindi 01: Chat Bootstrap (`chat_bootstrap.py`)
- Model chaguo-msingi imesasishwa kutoka `phi-3.5-mini` hadi `phi-4-mini`
- Imeongezwa msaada wa kubadilisha endpoint
- Nyaraka zimeboreshwa na marejeleo ya SDK

#### Kipindi 02: RAG Pipeline (`rag_pipeline.py`)
- Imesasishwa kutumia `phi-4-mini` kama chaguo-msingi
- Imeongezwa msaada wa kubadilisha endpoint
- Nyaraka zimeboreshwa na maelezo ya mazingira

#### Kipindi 02: RAG Evaluation (`rag_eval_ragas.py`)
- Chaguo-msingi za model zimesasishwa
- Imeongezwa usanidi wa endpoint
- Ushughulikiaji wa makosa umeboreshwa

#### Kipindi 03: Benchmarking (`benchmark_oss_models.py`)
- Orodha ya modeli chaguo-msingi imesasishwa kujumuisha `phi-4-mini`
- Nyaraka za mazingira zimeboreshwa kwa kina
- Nyaraka za kazi zimeboreshwa
- Imeongezwa msaada wa kubadilisha endpoint kote

#### Kipindi 04: Model Comparison (`model_compare.py`)
- LLM chaguo-msingi imesasishwa kutoka `gpt-oss-20b` hadi `qwen2.5-7b`
- Imeongezwa usanidi wa endpoint
- Nyaraka zimeboreshwa

#### Kipindi 05: Multi-Agent Orchestration (`agents_orchestrator.py`)
- Imeongezwa maelezo ya aina (imebadilishwa `str | None` hadi `Optional[str]`)
- Nyaraka za darasa la Agent zimeboreshwa
- Imeongezwa msaada wa kubadilisha endpoint
- Muundo wa uanzishaji umeboreshwa

#### Kipindi 06: Model Router (`models_router.py`)
- Imeongezwa usanidi wa endpoint
- Nyaraka za utambuzi wa nia zimeboreshwa
- Nyaraka za mantiki ya routing zimeboreshwa

#### Kipindi 06: Pipeline (`models_pipeline.py`)
- Nyaraka za kazi zimeboreshwa kwa kina
- Nyaraka za hatua kwa hatua zimeboreshwa
- Ushughulikiaji wa makosa umeboreshwa

### Scripti

#### Benchmark Export (`export_benchmark_markdown.py`)
- Imeongezwa msaada wa kubadilisha endpoint
- Modeli chaguo-msingi zimesasishwa
- Nyaraka za kazi zimeboreshwa
- Ushughulikiaji wa makosa umeboreshwa

#### CLI Linter (`lint_markdown_cli.py`)
- Imeongezwa viungo vya marejeleo ya SDK
- Nyaraka za matumizi zimeboreshwa

### Majaribio

#### Smoke Tests (`smoke.py`)
- Imeongezwa msaada wa kubadilisha endpoint
- Nyaraka zimeboreshwa
- Nyaraka za kesi za majaribio zimeboreshwa
- Utoaji bora wa ripoti za makosa

## Vigezo vya Mazingira

Sampuli zote sasa zinaunga mkono vigezo hivi vya mazingira:

### Usanidi wa Msingi
- `FOUNDRY_LOCAL_ALIAS` - Alias ya modeli ya kutumia (chaguo-msingi hutofautiana kwa sampuli)
- `FOUNDRY_LOCAL_ENDPOINT` - Kubadilisha endpoint ya huduma (hiari)
- `SHOW_USAGE` - Onyesha takwimu za matumizi ya tokeni (chaguo-msingi: "0")
- `RETRY_ON_FAIL` - Washa mantiki ya kurudia (chaguo-msingi: "1")
- `RETRY_BACKOFF` - Muda wa kuchelewa wa kurudia wa awali kwa sekunde (chaguo-msingi: "1.0")

### Sampuli Maalum
- `EMBED_MODEL` - Modeli ya embedding kwa sampuli za RAG
- `BENCH_MODELS` - Modeli zilizotenganishwa kwa koma kwa benchmarking
- `BENCH_ROUNDS` - Idadi ya raundi za benchmarking
- `BENCH_PROMPT` - Prompt ya majaribio kwa benchmarking
- `BENCH_STREAM` - Pima latency ya tokeni ya kwanza
- `RAG_QUESTION` - Swali la majaribio kwa sampuli za RAG
- `AGENT_MODEL_PRIMARY` - Modeli ya wakala wa msingi
- `AGENT_MODEL_EDITOR` - Modeli ya wakala wa mhariri
- `SLM_ALIAS` - Alias ya modeli ndogo ya lugha
- `LLM_ALIAS` - Alias ya modeli kubwa ya lugha

## Mazoea Bora ya SDK Yaliyotekelezwa

### 1. Uanzishaji Sahihi wa Mteja
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

### 2. Upataji wa Taarifa za Modeli
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Ushughulikiaji wa Makosa
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Mantiki ya Kurudia na Exponential Backoff
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

### 5. Msaada wa Streaming
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

## Mwongozo wa Uhamishaji kwa Sampuli Maalum

Ikiwa unaunda sampuli mpya au unasasisha zilizopo:

1. **Tumia vipengele vya `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Unganisha msaada wa kubadilisha endpoint**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Ongeza nyaraka za kina**:
   - Vigezo vya mazingira katika docstring
   - Kiungo cha marejeleo ya SDK
   - Mifano ya matumizi

4. **Tumia maelezo ya aina**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Tekeleza ushughulikiaji sahihi wa makosa**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Upimaji

Sampuli zote zinaweza kupimwa kwa:

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

## Marejeleo ya Nyaraka za SDK

- **Hifadhi Kuu**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Nyaraka za API**: Angalia hifadhi ya SDK kwa nyaraka za API za hivi karibuni

## Mabadiliko Yanayovunja

### Hakuna Yanayotarajiwa
Mabadiliko yote ni sambamba na yaliyopita. Sasisho hizi hasa:
- Ongeza vipengele vipya vya hiari (kubadilisha endpoint)
- Boresha ushughulikiaji wa makosa
- Boresha nyaraka
- Sasisha majina ya modeli chaguo-msingi kwa mapendekezo ya sasa

### Uboreshaji wa Hiari
Unaweza kutaka kusasisha msimbo wako kutumia:
- `FOUNDRY_LOCAL_ENDPOINT` kwa udhibiti wa endpoint wazi
- `SHOW_USAGE=1` kwa mwonekano wa matumizi ya tokeni
- Sasisho za modeli chaguo-msingi (`phi-4-mini` badala ya `phi-3.5-mini`)

## Masuala ya Kawaida na Suluhisho

### Tatizo: "Uanzishaji wa mteja umeshindwa"
**Suluhisho**: Hakikisha huduma ya Foundry Local inaendesha:
```bash
foundry service start
foundry model run phi-4-mini
```

### Tatizo: "Modeli haikupatikana"
**Suluhisho**: Angalia modeli zinazopatikana:
```bash
foundry model list
```

### Tatizo: Makosa ya muunganisho wa endpoint
**Suluhisho**: Thibitisha endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Hatua Zifuatazo

1. **Sasisha sampuli za Module08**: Tekeleza mifumo sawa kwa Module08/samples
2. **Ongeza majaribio ya ujumuishaji**: Unda suite ya majaribio ya kina
3. **Benchmarking ya utendaji**: Linganisha utendaji kabla/baada
4. **Sasisho za nyaraka**: Sasisha README kuu na mifumo mipya

## Miongozo ya Mchango

Unapoongeza sampuli mpya:
1. Tumia `workshop_utils.py` kwa uthabiti
2. Fuata muundo katika sampuli zilizopo
3. Ongeza docstring za kina
4. Jumuisha viungo vya marejeleo ya SDK
5. Unganisha msaada wa kubadilisha endpoint
6. Ongeza maelezo sahihi ya aina
7. Jumuisha mifano ya matumizi katika docstring

## Utangamano wa Toleo

Sasisho hizi zinaendana na:
- `foundry-local-sdk` (ya hivi karibuni)
- `openai>=1.30.0`
- Python 3.8+

---

**Tarehe ya Mwisho wa Sasisho**: 2025-01-08  
**Msimamizi**: Timu ya EdgeAI Workshop  
**Toleo la SDK**: Foundry Local SDK (ya hivi karibuni 0.7.117+67073234e7)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.