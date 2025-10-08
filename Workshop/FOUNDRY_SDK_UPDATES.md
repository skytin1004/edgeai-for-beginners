# Foundry Local SDK Updates

## Overview

Updated the Workshop notebooks and utilities to properly use the **official Foundry Local Python SDK** following the patterns from:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Files Modified

### 1. `Workshop/samples/workshop_utils.py`

**Changes:**
- ✅ Added import error handling for `foundry-local-sdk` package
- ✅ Enhanced documentation with official SDK patterns
- ✅ Improved logging with Unicode symbols (✓, ✗, ⚠)
- ✅ Added comprehensive docstrings with examples
- ✅ Better error messages referencing CLI commands
- ✅ Updated comments to match official SDK documentation

**Key Improvements:**

#### Import Error Handling
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Enhanced `get_client()` Function
- Added detailed documentation about the SDK initialization pattern
- Clarified that `FoundryLocalManager` starts the service automatically
- Explained model alias resolution to hardware-optimized variants
- Improved logging with endpoint information
- Better error messages suggesting troubleshooting steps

#### Enhanced `chat_once()` Function
- Added comprehensive docstring with usage examples
- Clarified OpenAI SDK compatibility
- Documented streaming support (via kwargs)
- Improved error messages with CLI command suggestions
- Added notes about model availability checking

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Changes:**
- ✅ Updated all markdown cells with SDK references
- ✅ Enhanced code comments with SDK pattern explanations
- ✅ Improved cell documentation and explanations
- ✅ Added troubleshooting guidance
- ✅ Updated model catalog (replaced 'gpt-oss-20b' with 'phi-3.5-mini')
- ✅ Better output formatting with visual indicators
- ✅ Added SDK links and references throughout

**Cell-by-Cell Updates:**

#### Cell 1 (Title)
- Added SDK documentation links
- Referenced official GitHub repositories

#### Cell 2 (Scenario)
- Reformatted with numbered steps
- Clarified intent-based routing pattern
- Emphasized local execution benefits

#### Cell 3 (Dependency Installation)
- Added explanation of what each package provides
- Documented SDK capabilities (alias resolution, hardware optimization)

#### Cell 4 (Environment Setup)
- Enhanced function docstrings
- Added inline comments explaining SDK patterns
- Documented model catalog structure
- Clarified priority/capability matching

#### Cell 5 (Catalog Check)
- Added visual checkmarks (✓)
- Better formatted output

#### Cell 6 (Intent Detection Test)
- Reformatted output as table-style
- Shows both intent and selected model

#### Cell 7 (Routing Function)
- Comprehensive SDK pattern explanation
- Documented the initialization flow
- Listed all features (retry, tracking, errors)
- Added SDK reference link

#### Cell 8 (Batch Demo)
- Enhanced explanation of what to expect
- Added troubleshooting section
- Included CLI commands for debugging
- Better formatted output display

### 3. `Workshop/notebooks/session06_README.md` (New File)

**Created comprehensive documentation covering:**

1. **Overview**: Architecture diagram and component explanation
2. **SDK Integration**: Code examples following official patterns
3. **Prerequisites**: Step-by-step setup instructions
4. **Usage**: How to run and customize the notebook
5. **Model Aliases**: Explanation of hardware-optimized variants
6. **Troubleshooting**: Common issues and solutions
7. **Extending**: How to add intents, models, and custom logic
8. **Performance Tips**: Best practices for production use
9. **Resources**: Links to official docs and community

## SDK Pattern Implementation

### Official Pattern (from Foundry Local docs)

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

### Our Implementation (in workshop_utils)

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

**Benefits of Our Approach:**
- ✅ Follows official SDK pattern exactly
- ✅ Adds caching to avoid repeated initialization
- ✅ Includes retry logic for production robustness
- ✅ Supports token usage tracking
- ✅ Provides better error messages
- ✅ Remains compatible with official examples

## Model Catalog Changes

### Before
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### After
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Reason:** Replaced 'gpt-oss-20b' (non-standard alias) with 'phi-3.5-mini' (official Foundry Local alias).

## Dependencies

### Updated requirements.txt

The Workshop requirements.txt already includes:
```
foundry-local-sdk
openai>=1.30.0
```

These are the only packages needed for Foundry Local integration.

## Testing the Updates

### 1. Verify Foundry Local is Running

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Check Available Models

```bash
foundry model ls
```

Ensure these models are available or will auto-download:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Run the Notebook

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Or open in VS Code and run all cells.

### 4. Expected Behavior

**Cell 1 (Install):** Successfully installs packages
**Cell 2 (Setup):** No errors, imports work
**Cell 3 (Verify):** Shows ✓ with model list
**Cell 4 (Test Intent):** Shows intent detection results
**Cell 5 (Router):** Shows ✓ Route function ready
**Cell 6 (Execute):** Routes prompts to models, shows results

### 5. Troubleshooting Connection Errors

If you see `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Environment Variables

The following environment variables are supported:

| Variable | Default | Description |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | Set to `1` to print token usage |
| `RETRY_ON_FAIL` | `1` | Enable retry logic |
| `RETRY_BACKOFF` | `1.0` | Initial retry delay (seconds) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Override service endpoint |

### Usage Examples

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migration from Old Pattern

If you have existing code using direct API calls, here's how to migrate:

### Before (Direct API)
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

### After (SDK)
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

### Benefits of Migration
- ✅ Automatic service management
- ✅ Model alias resolution
- ✅ Hardware optimization selection
- ✅ Better error handling
- ✅ OpenAI SDK compatibility
- ✅ Streaming support

## References

### Official Documentation
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK Source**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI Reference**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Troubleshooting**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop Resources
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Sample Notebook**: `Workshop/notebooks/session06_models_router.ipynb`

### Community
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues

## Next Steps

1. **Review Changes**: Read through the updated files
2. **Test Notebook**: Run session06_models_router.ipynb
3. **Verify SDK**: Ensure foundry-local-sdk is installed
4. **Check Service**: Confirm Foundry Local is running
5. **Explore Docs**: Read the new session06_README.md

## Summary

These updates ensure the Workshop materials follow the **official Foundry Local SDK patterns** exactly as documented in the GitHub repository. All code examples, documentation, and utilities now align with Microsoft's recommended best practices for local AI model deployment.

The changes improve:
- ✅ **Correctness**: Uses official SDK patterns
- ✅ **Documentation**: Comprehensive explanations and examples
- ✅ **Error Handling**: Better messages and troubleshooting guidance
- ✅ **Maintainability**: Follows official conventions
- ✅ **User Experience**: Clearer instructions and debugging help

---

**Updated:** October 8, 2025
**SDK Version:** foundry-local-sdk (latest)
**Workshop Branch:** Reactor
