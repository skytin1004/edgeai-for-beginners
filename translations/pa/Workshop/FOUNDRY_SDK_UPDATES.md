<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T10:34:18+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "pa"
}
-->
# ਫਾਉਂਡਰੀ ਲੋਕਲ SDK ਅੱਪਡੇਟਸ

## ਓਵਰਵਿਊ

ਵਰਕਸ਼ਾਪ ਨੋਟਬੁੱਕਾਂ ਅਤੇ ਯੂਟਿਲਿਟੀਜ਼ ਨੂੰ ਅਧਿਕਾਰਕ **Foundry Local Python SDK** ਦੇ ਪੈਟਰਨਾਂ ਅਨੁਸਾਰ ਅੱਪਡੇਟ ਕੀਤਾ ਗਿਆ ਹੈ:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## ਫਾਈਲਾਂ ਵਿੱਚ ਕੀਤੇ ਗਏ ਬਦਲਾਅ

### 1. `Workshop/samples/workshop_utils.py`

**ਬਦਲਾਅ:**
- ✅ `foundry-local-sdk` ਪੈਕੇਜ ਲਈ ਇੰਪੋਰਟ ਐਰਰ ਹੈਂਡਲਿੰਗ ਸ਼ਾਮਲ ਕੀਤੀ
- ✅ ਅਧਿਕਾਰਕ SDK ਪੈਟਰਨਾਂ ਨਾਲ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ
- ✅ ਯੂਨਿਕੋਡ ਚਿੰਨ੍ਹਾਂ (✓, ✗, ⚠) ਨਾਲ ਲੌਗਿੰਗ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ
- ✅ ਉਦਾਹਰਣਾਂ ਦੇ ਨਾਲ ਵਿਸਥਾਰਤ ਡੌਕਸਟ੍ਰਿੰਗਜ਼ ਸ਼ਾਮਲ ਕੀਤੀਆਂ
- ✅ CLI ਕਮਾਂਡਾਂ ਦਾ ਹਵਾਲਾ ਦਿੰਦੇ ਹੋਏ ਬਿਹਤਰ ਗਲਤੀ ਸੁਨੇਹੇ ਸ਼ਾਮਲ ਕੀਤੇ
- ✅ ਅਧਿਕਾਰਕ SDK ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹੋਏ ਟਿੱਪਣੀਆਂ ਅੱਪਡੇਟ ਕੀਤੀਆਂ

**ਮੁੱਖ ਸੁਧਾਰ:**

#### ਇੰਪੋਰਟ ਐਰਰ ਹੈਂਡਲਿੰਗ
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### ਸੁਧਾਰਿਆ ਗਿਆ `get_client()` ਫੰਕਸ਼ਨ
- SDK ਸ਼ੁਰੂਆਤੀਕਰਨ ਪੈਟਰਨ ਬਾਰੇ ਵਿਸਥਾਰਤ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਸ਼ਾਮਲ ਕੀਤੀ
- ਸਪੱਸ਼ਟ ਕੀਤਾ ਕਿ `FoundryLocalManager` ਸੇਵਾ ਨੂੰ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ
- ਮਾਡਲ ਐਲਿਆਸ ਨੂੰ ਹਾਰਡਵੇਅਰ-ਅਪਟਿਮਾਈਜ਼ਡ ਵਰਜਨਾਂ ਵਿੱਚ ਰਿਜ਼ੋਲਵ ਕਰਨ ਦੀ ਵਿਵਰਣ ਦਿੱਤੀ
- ਐਂਡਪੌਇੰਟ ਜਾਣਕਾਰੀ ਨਾਲ ਲੌਗਿੰਗ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ
- ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ ਕਦਮਾਂ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹੋਏ ਬਿਹਤਰ ਗਲਤੀ ਸੁਨੇਹੇ ਸ਼ਾਮਲ ਕੀਤੇ

#### ਸੁਧਾਰਿਆ ਗਿਆ `chat_once()` ਫੰਕਸ਼ਨ
- ਵਰਤੋਂ ਦੇ ਉਦਾਹਰਣਾਂ ਦੇ ਨਾਲ ਵਿਸਥਾਰਤ ਡੌਕਸਟ੍ਰਿੰਗ ਸ਼ਾਮਲ ਕੀਤੀ
- OpenAI SDK ਅਨੁਕੂਲਤਾ ਨੂੰ ਸਪੱਸ਼ਟ ਕੀਤਾ
- ਸਟ੍ਰੀਮਿੰਗ ਸਹਾਇਤਾ (kwargs ਰਾਹੀਂ) ਦਾ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਕੀਤਾ
- CLI ਕਮਾਂਡ ਸੁਝਾਵਾਂ ਦੇ ਨਾਲ ਗਲਤੀ ਸੁਨੇਹੇ ਸੁਧਾਰੇ
- ਮਾਡਲ ਉਪਲਬਧਤਾ ਚੈੱਕ ਕਰਨ ਬਾਰੇ ਟਿੱਪਣੀਆਂ ਸ਼ਾਮਲ ਕੀਤੀਆਂ

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**ਬਦਲਾਅ:**
- ✅ SDK ਹਵਾਲਿਆਂ ਨਾਲ ਸਾਰੇ ਮਾਰਕਡਾਊਨ ਸੈੱਲ ਅੱਪਡੇਟ ਕੀਤੇ
- ✅ SDK ਪੈਟਰਨ ਦੀ ਵਿਆਖਿਆ ਦੇ ਨਾਲ ਕੋਡ ਟਿੱਪਣੀਆਂ ਸੁਧਾਰੀਆਂ
- ✅ ਸੈੱਲ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਅਤੇ ਵਿਆਖਿਆਵਾਂ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ
- ✅ ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ ਮਦਦ ਸ਼ਾਮਲ ਕੀਤੀ
- ✅ ਮਾਡਲ ਕੈਟਾਲੌਗ ਅੱਪਡੇਟ ਕੀਤਾ (ਗੈਰ-ਮਿਆਰੀ 'gpt-oss-20b' ਨੂੰ 'phi-3.5-mini' ਨਾਲ ਬਦਲਿਆ)
- ✅ ਵਿਜੁਅਲ ਇੰਡੀਕੇਟਰਾਂ ਨਾਲ ਬਿਹਤਰ ਆਉਟਪੁੱਟ ਫਾਰਮੈਟਿੰਗ
- ✅ SDK ਲਿੰਕ ਅਤੇ ਹਵਾਲੇ ਹਰ ਜਗ੍ਹਾ ਸ਼ਾਮਲ ਕੀਤੇ

**ਸੈੱਲ-ਦਰ-ਸੈੱਲ ਅੱਪਡੇਟਸ:**

#### ਸੈੱਲ 1 (ਸਿਰਲੇਖ)
- SDK ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲਿੰਕ ਸ਼ਾਮਲ ਕੀਤੇ
- ਅਧਿਕਾਰਕ GitHub ਰਿਪੋਜ਼ਿਟਰੀਆਂ ਦਾ ਹਵਾਲਾ ਦਿੱਤਾ

#### ਸੈੱਲ 2 (ਦ੍ਰਿਸ਼)
- ਨੰਬਰਦਾਰ ਕਦਮਾਂ ਨਾਲ ਫਾਰਮੈਟ ਕੀਤਾ
- ਇਰਾਦਾ-ਅਧਾਰਿਤ ਰਾਊਟਿੰਗ ਪੈਟਰਨ ਨੂੰ ਸਪੱਸ਼ਟ ਕੀਤਾ
- ਸਥਾਨਕ ਐਗਜ਼ਿਕਿਊਸ਼ਨ ਦੇ ਫਾਇਦੇ ਉਤੇ ਜ਼ੋਰ ਦਿੱਤਾ

#### ਸੈੱਲ 3 (ਡਿਪੈਂਡੈਂਸੀ ਇੰਸਟਾਲੇਸ਼ਨ)
- ਹਰ ਪੈਕੇਜ ਦੇ ਫਾਇਦੇ ਦੀ ਵਿਆਖਿਆ ਸ਼ਾਮਲ ਕੀਤੀ
- SDK ਸਮਰੱਥਾਵਾਂ (ਐਲਿਆਸ ਰਿਜ਼ੋਲਵਸ਼ਨ, ਹਾਰਡਵੇਅਰ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ) ਦਾ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਕੀਤਾ

#### ਸੈੱਲ 4 (ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ)
- ਫੰਕਸ਼ਨ ਡੌਕਸਟ੍ਰਿੰਗਜ਼ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ
- SDK ਪੈਟਰਨ ਦੀ ਵਿਆਖਿਆ ਕਰਨ ਵਾਲੀਆਂ ਇਨਲਾਈਨ ਟਿੱਪਣੀਆਂ ਸ਼ਾਮਲ ਕੀਤੀਆਂ
- ਮਾਡਲ ਕੈਟਾਲੌਗ ਸਟ੍ਰਕਚਰ ਦਾ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਕੀਤਾ
- ਪ੍ਰਾਇਰਟੀ/ਸਮਰੱਥਾ ਮੇਲ ਬਾਰੇ ਸਪੱਸ਼ਟਤਾ ਦਿੱਤੀ

#### ਸੈੱਲ 5 (ਕੈਟਾਲੌਗ ਚੈੱਕ)
- ਵਿਜੁਅਲ ਚੈਕਮਾਰਕ (✓) ਸ਼ਾਮਲ ਕੀਤੇ
- ਬਿਹਤਰ ਫਾਰਮੈਟ ਕੀਤਾ ਆਉਟਪੁੱਟ

#### ਸੈੱਲ 6 (ਇਰਾਦਾ ਪਛਾਣ ਟੈਸਟ)
- ਆਉਟਪੁੱਟ ਨੂੰ ਟੇਬਲ-ਸ਼ੈਲੀ ਵਿੱਚ ਫਾਰਮੈਟ ਕੀਤਾ
- ਦਿਖਾਇਆ ਕਿ ਇਰਾਦਾ ਅਤੇ ਚੁਣਿਆ ਗਿਆ ਮਾਡਲ ਕੀ ਹੈ

#### ਸੈੱਲ 7 (ਰਾਊਟਿੰਗ ਫੰਕਸ਼ਨ)
- SDK ਪੈਟਰਨ ਦੀ ਵਿਸਥਾਰਤ ਵਿਆਖਿਆ
- ਸ਼ੁਰੂਆਤੀਕਰਨ ਦੇ ਪ੍ਰਵਾਹ ਦਾ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਕੀਤਾ
- ਸਾਰੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੀ ਸੂਚੀ ਦਿੱਤੀ (ਰੀਟ੍ਰਾਈ, ਟ੍ਰੈਕਿੰਗ, ਗਲਤੀਆਂ)
- SDK ਹਵਾਲੇ ਦਾ ਲਿੰਕ ਸ਼ਾਮਲ ਕੀਤਾ

#### ਸੈੱਲ 8 (ਬੈਚ ਡੈਮੋ)
- ਕੀ ਉਮੀਦ ਰੱਖਣੀ ਹੈ ਇਸ ਦੀ ਵਿਆਖਿਆ ਵਿੱਚ ਸੁਧਾਰ ਕੀਤਾ
- ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ ਸੈਕਸ਼ਨ ਸ਼ਾਮਲ ਕੀਤਾ
- ਡਿਬੱਗਿੰਗ ਲਈ CLI ਕਮਾਂਡ ਸ਼ਾਮਲ ਕੀਤੀਆਂ
- ਬਿਹਤਰ ਫਾਰਮੈਟ ਕੀਤਾ ਆਉਟਪੁੱਟ ਪ੍ਰਦਰਸ਼ਨ

### 3. `Workshop/notebooks/session06_README.md` (ਨਵੀਂ ਫਾਈਲ)

**ਵਿਸਥਾਰਤ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਬਣਾਈ ਜੋ ਕਵਰ ਕਰਦੀ ਹੈ:**

1. **ਓਵਰਵਿਊ**: ਆਰਕੀਟੈਕਚਰ ਡਾਇਗ੍ਰਾਮ ਅਤੇ ਕੰਪੋਨੈਂਟ ਵਿਆਖਿਆ
2. **SDK ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: ਅਧਿਕਾਰਕ ਪੈਟਰਨਾਂ ਦੇ ਅਨੁਸਾਰ ਕੋਡ ਉਦਾਹਰਣ
3. **ਪੂਰਵ ਸ਼ਰਤਾਂ**: ਕਦਮ-ਦਰ-ਕਦਮ ਸੈਟਅੱਪ ਨਿਰਦੇਸ਼
4. **ਵਰਤੋਂ**: ਨੋਟਬੁੱਕ ਨੂੰ ਕਿਵੇਂ ਚਲਾਉਣਾ ਅਤੇ ਕਸਟਮਾਈਜ਼ ਕਰਨਾ
5. **ਮਾਡਲ ਐਲਿਆਸ**: ਹਾਰਡਵੇਅਰ-ਅਪਟਿਮਾਈਜ਼ਡ ਵਰਜਨਾਂ ਦੀ ਵਿਆਖਿਆ
6. **ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ**: ਆਮ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਹੱਲ
7. **ਵਿਸਥਾਰ ਕਰਨਾ**: ਇਰਾਦੇ, ਮਾਡਲ ਅਤੇ ਕਸਟਮ ਲੌਜਿਕ ਕਿਵੇਂ ਸ਼ਾਮਲ ਕਰਨੇ ਹਨ
8. **ਪ੍ਰਦਰਸ਼ਨ ਸੁਝਾਵ**: ਉਤਪਾਦਨ ਵਰਤੋਂ ਲਈ ਸਰਬੋਤਮ ਅਭਿਆਸ
9. **ਸੰਸਾਧਨ**: ਅਧਿਕਾਰਕ ਦਸਤਾਵੇਜ਼ ਅਤੇ ਕਮਿਊਨਿਟੀ ਲਈ ਲਿੰਕ

## SDK ਪੈਟਰਨ ਅਮਲ

### ਅਧਿਕਾਰਕ ਪੈਟਰਨ (Foundry Local ਦਸਤਾਵੇਜ਼ ਤੋਂ)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### ਸਾਡਾ ਅਮਲ (workshop_utils ਵਿੱਚ)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**ਸਾਡੇ ਪਹੁੰਚ ਦੇ ਫਾਇਦੇ:**
- ✅ ਅਧਿਕਾਰਕ SDK ਪੈਟਰਨ ਦਾ ਪੂਰੀ ਤਰ੍ਹਾਂ ਪਾਲਣ
- ✅ ਦੁਬਾਰਾ ਸ਼ੁਰੂਆਤੀਕਰਨ ਤੋਂ ਬਚਣ ਲਈ ਕੈਸ਼ਿੰਗ ਸ਼ਾਮਲ
- ✅ ਉਤਪਾਦਨ ਮਜ਼ਬੂਤੀ ਲਈ ਰੀਟ੍ਰਾਈ ਲੌਜਿਕ ਸ਼ਾਮਲ
- ✅ ਟੋਕਨ ਵਰਤੋਂ ਟ੍ਰੈਕਿੰਗ ਦਾ ਸਮਰਥਨ
- ✅ ਬਿਹਤਰ ਗਲਤੀ ਸੁਨੇਹੇ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ
- ✅ ਅਧਿਕਾਰਕ ਉਦਾਹਰਣਾਂ ਨਾਲ ਅਨੁਕੂਲ ਰਹਿੰਦਾ ਹੈ

## ਮਾਡਲ ਕੈਟਾਲੌਗ ਬਦਲਾਅ

### ਪਹਿਲਾਂ
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### ਬਾਅਦ
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**ਕਾਰਨ:** 'gpt-oss-20b' (ਗੈਰ-ਮਿਆਰੀ ਐਲਿਆਸ) ਨੂੰ 'phi-3.5-mini' (ਅਧਿਕਾਰਕ Foundry Local ਐਲਿਆਸ) ਨਾਲ ਬਦਲਿਆ ਗਿਆ।

## ਡਿਪੈਂਡੈਂਸੀਜ਼

### ਅੱਪਡੇਟ ਕੀਤੀ requirements.txt

ਵਰਕਸ਼ਾਪ ਦੀ requirements.txt ਪਹਿਲਾਂ ਹੀ ਸ਼ਾਮਲ ਕਰਦੀ ਹੈ:
```
foundry-local-sdk
openai>=1.30.0
```

ਇਹ Foundry Local ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲਈ ਲੋੜੀਂਦੇ ਸਿਰਫ ਪੈਕੇਜ ਹਨ।

## ਅੱਪਡੇਟਸ ਦੀ ਜਾਂਚ

### 1. ਯਕੀਨੀ ਬਣਾਓ ਕਿ Foundry Local ਚੱਲ ਰਿਹਾ ਹੈ

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. ਉਪਲਬਧ ਮਾਡਲਾਂ ਦੀ ਜਾਂਚ ਕਰੋ

```bash
foundry model ls
```

ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਇਹ ਮਾਡਲ ਉਪਲਬਧ ਹਨ ਜਾਂ ਆਟੋ-ਡਾਊਨਲੋਡ ਹੋਣਗੇ:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. ਨੋਟਬੁੱਕ ਚਲਾਓ

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

ਜਾਂ VS Code ਵਿੱਚ ਖੋਲ੍ਹੋ ਅਤੇ ਸਾਰੇ ਸੈੱਲ ਚਲਾਓ।

### 4. ਉਮੀਦ ਕੀਤੀ ਗਈ ਵਿਵਹਾਰ

**ਸੈੱਲ 1 (ਇੰਸਟਾਲ):** ਪੈਕੇਜ ਸਫਲਤਾਪੂਰਵਕ ਇੰਸਟਾਲ ਕਰਦਾ ਹੈ  
**ਸੈੱਲ 2 (ਸੈਟਅੱਪ):** ਕੋਈ ਗਲਤੀ ਨਹੀਂ, ਇੰਪੋਰਟ ਕੰਮ ਕਰਦੇ ਹਨ  
**ਸੈੱਲ 3 (ਜਾਂਚ):** ✓ ਦੇ ਨਾਲ ਮਾਡਲ ਸੂਚੀ ਦਿਖਾਉਂਦਾ ਹੈ  
**ਸੈੱਲ 4 (ਇਰਾਦਾ ਟੈਸਟ):** ਇਰਾਦਾ ਪਛਾਣ ਦੇ ਨਤੀਜੇ ਦਿਖਾਉਂਦਾ ਹੈ  
**ਸੈੱਲ 5 (ਰਾਊਟਰ):** ✓ ਰਾਊਟ ਫੰਕਸ਼ਨ ਤਿਆਰ ਦਿਖਾਉਂਦਾ ਹੈ  
**ਸੈੱਲ 6 (ਐਗਜ਼ਿਕਿਊਟ):** ਪ੍ਰੋੰਪਟ ਨੂੰ ਮਾਡਲਾਂ ਤੱਕ ਰਾਊਟ ਕਰਦਾ ਹੈ, ਨਤੀਜੇ ਦਿਖਾਉਂਦਾ ਹੈ  

### 5. ਕਨੈਕਸ਼ਨ ਗਲਤੀਆਂ ਟ੍ਰਬਲਸ਼ੂਟ ਕਰਨਾ

ਜੇ ਤੁਸੀਂ `APIConnectionError: Connection error` ਵੇਖਦੇ ਹੋ:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

ਹੇਠ ਲਿਖੇ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਾਂ ਦਾ ਸਮਰਥਨ ਕੀਤਾ ਜਾਂਦਾ ਹੈ:

| ਵੈਰੀਏਬਲ | ਡਿਫਾਲਟ | ਵੇਰਵਾ |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | ਟੋਕਨ ਵਰਤੋਂ ਪ੍ਰਿੰਟ ਕਰਨ ਲਈ `1` 'ਤੇ ਸੈੱਟ ਕਰੋ |
| `RETRY_ON_FAIL` | `1` | ਰੀਟ੍ਰਾਈ ਲੌਜਿਕ ਨੂੰ ਯੋਗ ਕਰੋ |
| `RETRY_BACKOFF` | `1.0` | ਸ਼ੁਰੂਆਤੀ ਰੀਟ੍ਰਾਈ ਦੇਰੀ (ਸਕਿੰਟਾਂ ਵਿੱਚ) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | ਸੇਵਾ ਐਂਡਪੌਇੰਟ ਨੂੰ ਓਵਰਰਾਈਡ ਕਰੋ |

### ਵਰਤੋਂ ਦੇ ਉਦਾਹਰਣ

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## ਪੁਰਾਣੇ ਪੈਟਰਨ ਤੋਂ ਮਾਈਗ੍ਰੇਸ਼ਨ

ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਸਿੱਧੇ API ਕਾਲਾਂ ਵਰਤਣ ਵਾਲਾ ਮੌਜੂਦਾ ਕੋਡ ਹੈ, ਤਾਂ ਇਸ ਤਰ੍ਹਾਂ ਮਾਈਗ੍ਰੇਟ ਕਰੋ:

### ਪਹਿਲਾਂ (ਸਿੱਧਾ API)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### ਬਾਅਦ (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### ਮਾਈਗ੍ਰੇਸ਼ਨ ਦੇ ਫਾਇਦੇ
- ✅ ਆਟੋਮੈਟਿਕ ਸੇਵਾ ਪ੍ਰਬੰਧਨ
- ✅ ਮਾਡਲ ਐਲਿਆਸ ਰਿਜ਼ੋਲਵਸ਼ਨ
- ✅ ਹਾਰਡਵੇਅਰ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ ਚੋਣ
- ✅ ਬਿਹਤਰ ਗਲਤੀ ਹੈਂਡਲਿੰਗ
- ✅ OpenAI SDK ਅਨੁਕੂਲਤਾ
- ✅ ਸਟ੍ਰੀਮਿੰਗ ਸਹਾਇਤਾ

## ਹਵਾਲੇ

### ਅਧਿਕਾਰਕ ਦਸਤਾਵੇਜ਼
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local  
- **Python SDK ਸਰੋਤ**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  
- **CLI ਹਵਾਲਾ**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md  
- **ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md  

### ਵਰਕਸ਼ਾਪ ਸੰਸਾਧਨ
- **ਸੈਸ਼ਨ 06 README**: `Workshop/notebooks/session06_README.md`  
- **ਵਰਕਸ਼ਾਪ ਯੂਟਿਲਿਟੀਜ਼**: `Workshop/samples/workshop_utils.py`  
- **ਨਮੂਨਾ ਨੋਟਬੁੱਕ**: `Workshop/notebooks/session06_models_router.ipynb`  

### ਕਮਿਊਨਿਟੀ
- **Discord**: https://aka.ms/foundry-local-discord  
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues  

## ਅਗਲੇ ਕਦਮ

1. **ਬਦਲਾਅ ਦੀ ਸਮੀਖਿਆ ਕਰੋ**: ਅੱਪਡੇਟ ਕੀਤੀਆਂ ਫਾਈਲਾਂ ਨੂੰ ਪੜ੍ਹੋ  
2. **ਨੋਟਬੁੱਕ ਟੈਸਟ ਕਰੋ**: session06_models_router.ipynb ਚਲਾਓ  
3. **SDK ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ foundry-local-sdk ਇੰਸਟਾਲ ਹੈ  
4. **ਸੇਵਾ ਦੀ ਜਾਂਚ ਕਰੋ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ Foundry Local ਚੱਲ ਰਿਹਾ ਹੈ  
5. **ਦਸਤਾਵੇਜ਼ ਪੜ੍ਹੋ**: ਨਵਾਂ session06_README.md ਪੜ੍ਹੋ  

## ਸਾਰ

ਇਹ ਅੱਪਡੇਟਸ ਯਕੀਨੀ ਬਣਾਉਂਦੀਆਂ ਹਨ ਕਿ ਵਰਕਸ਼ਾਪ ਸਮੱਗਰੀ **ਅਧਿਕਾਰਕ Foundry Local SDK ਪੈਟਰਨਾਂ** ਦਾ ਪੂਰੀ ਤਰ੍ਹਾਂ ਪਾਲਣ ਕਰਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ GitHub ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਕੀਤਾ ਗਿਆ ਹੈ। ਸਾਰੇ ਕੋਡ ਉਦਾਹਰਣ, ਦਸਤਾਵੇਜ਼ੀਕਰਨ, ਅਤੇ ਯੂਟਿਲਿਟੀਜ਼ ਹੁਣ ਮਾਈਕਰੋਸੌਫਟ ਦੇ ਸਥਾਨਕ AI ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ ਲਈ ਸਿਫਾਰਸ਼ੀ ਸਰਬੋਤਮ ਅਭਿਆਸਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ।

ਇਹ ਬਦਲਾਅ ਸੁਧਾਰਦੇ ਹਨ:
- ✅ **ਸਹੀਪਨ**: ਅਧਿਕਾਰਕ SDK ਪੈਟਰਨ ਵਰਤਦਾ ਹੈ  
- ✅ **ਦਸਤਾਵੇਜ਼ੀਕਰਨ**: ਵਿਸਥਾਰਤ ਵਿਆਖਿਆਵਾਂ ਅਤੇ ਉਦਾਹਰਣ  
- ✅ **ਗਲਤੀ ਹੈਂਡਲਿੰਗ**: ਬਿਹਤਰ ਸੁਨੇਹੇ ਅਤੇ ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ ਮਦਦ  
- ✅ **ਰੱਖ-ਰਖਾਵ**: ਅਧਿਕਾਰਕ ਰਿਵਾਜਾਂ ਦਾ ਪਾਲਣ  
- ✅ **ਵਰਤੋਂਕਾਰ ਅਨੁਭਵ**: ਸਪੱਸ਼ਟ ਨਿਰਦੇਸ਼ ਅਤੇ ਡਿਬੱਗਿੰਗ ਮਦਦ  

---

**ਅੱਪਡੇਟ ਕੀਤਾ ਗਿਆ:** ਅਕਤੂਬਰ 8, 2025  
**SDK ਵਰਜਨ:** foundry-local-sdk (ਤਾਜ਼ਾ)  
**ਵਰਕਸ਼ਾਪ ਸ਼ਾਖਾ:** ਰਿਏਕਟਰ  

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।