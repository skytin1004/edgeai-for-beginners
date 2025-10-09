<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dd4a5b9ec82d35599b0abc9af89e7c9e",
  "translation_date": "2025-10-09T09:22:16+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "ne"
}
-->
# वातावरण कन्फिगरेसन गाइड

## अवलोकन

वर्कशपका नमूनाहरूले `.env` फाइलमा केन्द्रित वातावरण चरहरू प्रयोग गरेर कन्फिगरेसन गर्छ। यसले कोड परिवर्तन नगरी सजिलै अनुकूलन गर्न अनुमति दिन्छ।

## छिटो सुरु

### १. आवश्यकताहरू पुष्टि गर्नुहोस्

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### २. वातावरण कन्फिगर गर्नुहोस्

`.env` फाइल पहिले नै उपयुक्त डिफल्ट सेटिङहरूसँग कन्फिगर गरिएको छ। अधिकांश प्रयोगकर्ताहरूले केही परिवर्तन गर्न आवश्यक पर्दैन।

**वैकल्पिक**: सेटिङहरू समीक्षा र अनुकूलन गर्नुहोस्:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### ३. कन्फिगरेसन लागू गर्नुहोस्

**Python स्क्रिप्टहरूको लागि:**
```bash
cd Workshop/samples/session01
python chat_bootstrap.py
# Environment variables automatically loaded
```

**नोटबुकहरूको लागि:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## वातावरण चरहरूको सन्दर्भ

### मुख्य कन्फिगरेसन

| चर | डिफल्ट | विवरण |
|-----|--------|--------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | नमूनाहरूको लागि डिफल्ट मोडेल |
| `FOUNDRY_LOCAL_ENDPOINT` | (खाली) | सेवा अन्त बिन्दु ओभरराइड गर्नुहोस् |
| `PYTHONPATH` | वर्कशप पथहरू | Python मोड्युल खोज पथ |

**FOUNDRY_LOCAL_ENDPOINT कहिले सेट गर्ने:**
- रिमोट Foundry Local इन्स्ट्यान्स
- कस्टम पोर्ट कन्फिगरेसन
- विकास/उत्पादन छुट्याउने

**उदाहरण:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### सत्र-विशिष्ट चरहरू

#### सत्र ०२: RAG पाइपलाइन
| चर | डिफल्ट | उद्देश्य |
|-----|--------|----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | एम्बेडिङ मोडेल |
| `RAG_QUESTION` | पूर्व-कन्फिगर गरिएको | परीक्षण प्रश्न |

#### सत्र ०३: बेंचमार्किङ
| चर | डिफल्ट | उद्देश्य |
|-----|--------|----------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b,gemma-2-2b` | बेंचमार्क गर्न मोडेलहरू |
| `BENCH_ROUNDS` | `3` | प्रत्येक मोडेलको लागि पुनरावृत्ति |
| `BENCH_PROMPT` | पूर्व-कन्फिगर गरिएको | परीक्षण प्रम्प्ट |
| `BENCH_STREAM` | `0` | पहिलो-टोकन विलम्बता मापन गर्नुहोस् |

#### सत्र ०४: मोडेल तुलना
| चर | डिफल्ट | उद्देश्य |
|-----|--------|----------|
| `SLM_ALIAS` | `phi-4-mini` | सानो भाषा मोडेल |
| `LLM_ALIAS` | `qwen2.5-7b` | ठूलो भाषा मोडेल |
| `COMPARE_PROMPT` | पूर्व-कन्फिगर गरिएको | तुलना प्रम्प्ट |
| `COMPARE_RETRIES` | `2` | पुन: प्रयासको संख्या |

#### सत्र ०५: बहु-एजेन्ट समन्वय
| चर | डिफल्ट | उद्देश्य |
|-----|--------|----------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | अनुसन्धानकर्ता एजेन्ट मोडेल |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | सम्पादक एजेन्ट मोडेल |
| `AGENT_QUESTION` | पूर्व-कन्फिगर गरिएको | परीक्षण प्रश्न |

### विश्वसनीयता कन्फिगरेसन

| चर | डिफल्ट | उद्देश्य |
|-----|--------|----------|
| `SHOW_USAGE` | `1` | टोकन प्रयोग प्रिन्ट गर्नुहोस् |
| `RETRY_ON_FAIL` | `1` | पुन: प्रयास तर्क सक्षम गर्नुहोस् |
| `RETRY_BACKOFF` | `1.0` | पुन: प्रयास ढिलाइ (सेकेन्ड) |

## सामान्य कन्फिगरेसनहरू

### विकास सेटअप (छिटो पुनरावृत्ति)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### उत्पादन सेटअप (गुणस्तर केन्द्रित)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### बेंचमार्किङ सेटअप
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b,gemma-2-2b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### बहु-एजेन्ट विशेषज्ञता
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### रिमोट विकास
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## सिफारिस गरिएका मोडेलहरू

### प्रयोग केस अनुसार

**सामान्य उद्देश्य:**
- `phi-4-mini` - सन्तुलित गुणस्तर र गति

**छिटो प्रतिक्रिया:**
- `qwen2.5-0.5b` - धेरै छिटो, वर्गीकरणको लागि राम्रो
- `phi-4-mini` - राम्रो गुणस्तरको साथ छिटो

**उच्च गुणस्तर:**
- `qwen2.5-7b` - उत्कृष्ट गुणस्तर, उच्च स्रोत प्रयोग
- `phi-4-mini` - राम्रो गुणस्तर, कम स्रोतहरू

**कोड उत्पादन:**
- `deepseek-coder-1.3b` - कोडको लागि विशेष
- `phi-4-mini` - सामान्य उद्देश्य कोडिङ

### स्रोत उपलब्धता अनुसार

**कम स्रोतहरू (< ८GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**मध्यम स्रोतहरू (८-१६GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**उच्च स्रोतहरू (१६GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## उन्नत कन्फिगरेसन

### कस्टम अन्त बिन्दुहरू

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### तापमान र नमूना (कोडमा ओभरराइड गर्नुहोस्)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI हाइब्रिड सेटअप

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## समस्या समाधान

### वातावरण चरहरू लोड भएन

**लक्षणहरू:**
- स्क्रिप्टहरूले गलत मोडेल प्रयोग गर्छन्
- जडान त्रुटिहरू
- चरहरू मान्यता प्राप्त छैनन्

**समाधानहरू:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### सेवा जडान समस्याहरू

**लक्षणहरू:**
- "जडान अस्वीकृत" त्रुटिहरू
- "सेवा उपलब्ध छैन"
- टाइमआउट त्रुटिहरू

**समाधानहरू:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### मोडेल फेला परेन

**लक्षणहरू:**
- "मोडेल फेला परेन" त्रुटिहरू
- "उपनाम मान्यता प्राप्त छैन"

**समाधानहरू:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### आयात त्रुटिहरू

**लक्षणहरू:**
- "मोड्युल फेला परेन" त्रुटिहरू
- "workshop_utils आयात गर्न सकिएन"

**समाधानहरू:**
```bash
# 1. Verify PYTHONPATH in .env
PYTHONPATH=${workspaceFolder}/Workshop/samples

# 2. Install dependencies
pip install -r requirements.txt

# 3. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

## कन्फिगरेसन परीक्षण

### वातावरण लोडिङ पुष्टि गर्नुहोस्

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Foundry Local जडान परीक्षण गर्नुहोस्

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## सुरक्षा उत्तम अभ्यासहरू

### १. कहिल्यै गोप्य जानकारी कमिट नगर्नुहोस्

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### २. छुट्टै .env फाइलहरू प्रयोग गर्नुहोस्

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### ३. API कुञ्जीहरू घुमाउनुहोस्

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### ४. वातावरण-विशिष्ट कन्फिग प्रयोग गर्नुहोस्

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK दस्तावेज

- **मुख्य रिपोजिटरी**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API दस्तावेज**: नवीनतम जानकारीको लागि SDK रिपोजिटरी जाँच गर्नुहोस्

## थप स्रोतहरू

- `QUICK_START.md` - सुरु गर्ने गाइड
- `SDK_MIGRATION_NOTES.md` - SDK अपडेट विवरण
- `Workshop/samples/*/README.md` - नमूना-विशिष्ट गाइडहरू

---

**अन्तिम अपडेट**: २०२५-०१-०८  
**संस्करण**: २.०  
**SDK**: Foundry Local Python SDK (नवीनतम)

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथासम्भव शुद्धता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।