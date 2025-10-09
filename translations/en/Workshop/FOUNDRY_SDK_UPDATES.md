<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T21:04:17+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "en"
}
-->
# Foundry Local SDK Updates

## Overview

The Workshop notebooks and utilities have been updated to properly utilize the **official Foundry Local Python SDK**, following the patterns outlined in:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Files Modified

### 1. `Workshop/samples/workshop_utils.py`

**Changes:**
- ✅ Added error handling for missing `foundry-local-sdk` package
- ✅ Enhanced documentation to align with official SDK patterns
- ✅ Improved logging with Unicode symbols (✓, ✗, ⚠)
- ✅ Added detailed docstrings with examples
- ✅ Enhanced error messages with CLI command references
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
- Added detailed documentation on SDK initialization patterns
- Clarified that `FoundryLocalManager` automatically starts the service
- Explained model alias resolution for hardware-optimized variants
- Improved logging with endpoint details
- Enhanced error messages with troubleshooting suggestions

#### Enhanced `chat_once()` Function
- Added detailed docstring with usage examples
- Clarified compatibility with OpenAI SDK
- Documented streaming support (via kwargs)
- Improved error messages with CLI command references
- Included notes on checking model availability

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Changes:**
- ✅ Updated all markdown cells with SDK references
- ✅ Enhanced code comments with explanations of SDK patterns
- ✅ Improved cell documentation and explanations
- ✅ Added troubleshooting guidance
- ✅ Updated model catalog (replaced 'gpt-oss-20b' with 'phi-3.5-mini')
- ✅ Enhanced output formatting with visual indicators
- ✅ Added SDK links and references throughout

**Cell-by-Cell Updates:**

#### Cell 1 (Title)
- Added links to SDK documentation
- Referenced official GitHub repositories

#### Cell 2 (Scenario)
- Reformatted with numbered steps
- Clarified intent-based routing pattern
- Highlighted benefits of local execution

#### Cell 3 (Dependency Installation)
- Explained the purpose of each package
- Documented SDK capabilities (alias resolution, hardware optimization)

#### Cell 4 (Environment Setup)
- Enhanced function docstrings
- Added inline comments explaining SDK patterns
- Documented model catalog structure
- Clarified priority/capability matching

#### Cell 5 (Catalog Check)
- Added visual checkmarks (✓)
- Improved output formatting

#### Cell 6 (Intent Detection Test)
- Reformatted output into a table-style display
- Showed both intent and selected model

#### Cell 7 (Routing Function)
- Comprehensive explanation of SDK patterns
- Documented initialization flow
- Listed all features (retry, tracking, error handling)
- Added SDK reference link

#### Cell 8 (Batch Demo)
- Enhanced explanation of expected results
- Added troubleshooting section
- Included CLI commands for debugging
- Improved output formatting

### 3. `Workshop/notebooks/session06_README.md` (New File)

**Comprehensive documentation created, covering:**

1. **Overview**: Architecture diagram and component details
2. **SDK Integration**: Code examples following official patterns
3. **Prerequisites**: Step-by-step setup instructions
4. **Usage**: How to run and customize the notebook
5. **Model Aliases**: Explanation of hardware-optimized variants
6. **Troubleshooting**: Common issues and solutions
7. **Extending**: How to add intents, models, and custom logic
8. **Performance Tips**: Best practices for production use
9. **Resources**: Links to official documentation and community

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
- ✅ Strict adherence to official SDK patterns
- ✅ Added caching to avoid repeated initialization
- ✅ Included retry logic for production robustness
- ✅ Supported token usage tracking
- ✅ Provided improved error messages
- ✅ Maintained compatibility with official examples

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

These are the only packages required for Foundry Local integration.

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

Ensure the following models are available or will auto-download:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Run the Notebook

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Or open in VS Code and execute all cells.

### 4. Expected Behavior

**Cell 1 (Install):** Successfully installs packages  
**Cell 2 (Setup):** No errors, imports work  
**Cell 3 (Verify):** Displays ✓ with model list  
**Cell 4 (Test Intent):** Shows intent detection results  
**Cell 5 (Router):** Displays ✓ Route function ready  
**Cell 6 (Execute):** Routes prompts to models and shows results  

### 5. Troubleshooting Connection Errors

If you encounter `APIConnectionError: Connection error`:

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
| `SHOW_USAGE` | `0` | Set to `1` to display token usage |
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
- ✅ Improved error handling
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

1. **Review Changes**: Go through the updated files
2. **Test Notebook**: Run session06_models_router.ipynb
3. **Verify SDK**: Ensure foundry-local-sdk is installed
4. **Check Service**: Confirm Foundry Local is running
5. **Explore Docs**: Read the new session06_README.md

## Summary

These updates ensure the Workshop materials strictly follow the **official Foundry Local SDK patterns** as documented in the GitHub repository. All code examples, documentation, and utilities now align with Microsoft's recommended best practices for deploying AI models locally.

The changes improve:
- ✅ **Accuracy**: Adheres to official SDK patterns
- ✅ **Documentation**: Detailed explanations and examples
- ✅ **Error Handling**: Enhanced messages and troubleshooting guidance
- ✅ **Maintainability**: Follows official conventions
- ✅ **User Experience**: Clearer instructions and debugging support

---

**Updated:** October 8, 2025  
**SDK Version:** foundry-local-sdk (latest)  
**Workshop Branch:** Reactor

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.