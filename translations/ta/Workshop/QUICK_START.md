<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-11T11:47:32+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "ta"
}
-->
# வேலைநிறுவனத்தின் விரைவான தொடக்க வழிகாட்டி

## முன்பதிவுகள்

### 1. Foundry Local நிறுவவும்

அதிகாரப்பூர்வ நிறுவல் வழிகாட்டியை பின்பற்றவும்:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Python சார்ந்த தேவைகளை நிறுவவும்

Workshop கோப்பகத்திலிருந்து:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Workshop மாதிரிகளை இயக்குதல்

### அமர்வு 01: அடிப்படை உரையாடல்

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**சுற்றுச்சூழல் மாறிகள்:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### அமர்வு 02: RAG குழாய்

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**சுற்றுச்சூழல் மாறிகள்:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### அமர்வு 02: RAG மதிப்பீடு (Ragas)

```bash
python rag_eval_ragas.py
```

**குறிப்பு**: `requirements.txt` மூலம் கூடுதல் தேவைகளை நிறுவ வேண்டும்

### அமர்வு 03: தரநிலை மதிப்பீடு

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**சுற்றுச்சூழல் மாறிகள்:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**வெளியீடு**: JSON, தாமதம், திறன், மற்றும் முதல்-டோக்கன் அளவீடுகள்

### அமர்வு 04: மாதிரி ஒப்பீடு

```bash
cd Workshop/samples/session04
python model_compare.py
```

**சுற்றுச்சூழல் மாறிகள்:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### அமர்வு 05: பல முகவர் ஒருங்கிணைப்பு

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**சுற்றுச்சூழல் மாறிகள்:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### அமர்வு 06: மாதிரி வழிமாற்றி

```bash
cd Workshop/samples/session06
python models_router.py
```

**சோதனை வழிமாற்று தர்க்கம்** பல நோக்கங்களுடன் (கோடு, சுருக்கம், வகைப்படுத்தல்)

### அமர்வு 06: குழாய்

```bash
python models_pipeline.py
```

**சிக்கலான பல படிகள் கொண்ட குழாய்** திட்டமிடல், செயல்படுத்தல், மற்றும் திருத்தம்

## ஸ்கிரிப்ட்கள்

### தரநிலை அறிக்கையை ஏற்றுமதி செய்யவும்

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**வெளியீடு**: Markdown அட்டவணை + JSON அளவீடுகள்

### Markdown CLI முறைகளை சோதிக்கவும்

```bash
python lint_markdown_cli.py --verbose
```

**நோக்கம்**: ஆவணங்களில் காலாவதியான CLI முறைகளை கண்டறிதல்

## சோதனை

### புகை சோதனைகள்

```bash
cd Workshop
python -m tests.smoke
```

**சோதனைகள்**: முக்கிய மாதிரிகளின் அடிப்படை செயல்பாடு

## சிக்கல்களை சரிசெய்தல்

### சேவை இயங்கவில்லை

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### தொகுதி இறக்குமதி பிழைகள்

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### இணைப்பு பிழைகள்

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### மாதிரி கிடைக்கவில்லை

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## சுற்றுச்சூழல் மாறி குறிப்புகள்

### முக்கிய கட்டமைப்பு
| மாறி | இயல்புநிலை | விளக்கம் |
|------|------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | மாறுபடும் | பயன்படுத்த வேண்டிய மாதிரி பெயர் |
| `FOUNDRY_LOCAL_ENDPOINT` | தானாக | சேவை முடுக்கத்தை மாற்றவும் |
| `SHOW_USAGE` | `0` | டோக்கன் பயன்பாட்டு புள்ளிவிவரங்களை காண்பிக்கவும் |
| `RETRY_ON_FAIL` | `1` | மீண்டும் முயற்சி தர்க்கத்தை இயக்கவும் |
| `RETRY_BACKOFF` | `1.0` | ஆரம்ப மீண்டும் முயற்சி தாமதம் (விநாடிகள்) |

### அமர்வு-குறிப்பிட்ட
| மாறி | இயல்புநிலை | விளக்கம் |
|------|------------|----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | எம்பெடிங் மாதிரி |
| `RAG_QUESTION` | மாதிரி பார்க்கவும் | RAG சோதனை கேள்வி |
| `BENCH_MODELS` | மாறுபடும் | கமா-பிரிக்கப்பட்ட மாதிரிகள் |
| `BENCH_ROUNDS` | `3` | தரநிலை மீளுருவாக்கங்கள் |
| `BENCH_PROMPT` | மாதிரி பார்க்கவும் | தரநிலை உந்துதல் |
| `BENCH_STREAM` | `0` | முதல்-டோக்கன் தாமதத்தை அளவிடவும் |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | முதன்மை முகவர் மாதிரி |
| `AGENT_MODEL_EDITOR` | முதன்மை | திருத்தும் முகவர் மாதிரி |
| `SLM_ALIAS` | `phi-4-mini` | சிறிய மொழி மாதிரி |
| `LLM_ALIAS` | `qwen2.5-7b` | பெரிய மொழி மாதிரி |
| `COMPARE_PROMPT` | மாதிரி பார்க்கவும் | ஒப்பீட்டு உந்துதல் |

## பரிந்துரைக்கப்பட்ட மாதிரிகள்

### மேம்பாடு மற்றும் சோதனை
- **phi-4-mini** - தரம் மற்றும் வேகத்தில் சமநிலை
- **qwen2.5-0.5b** - வகைப்படுத்தலுக்கு மிகவும் வேகமானது
- **gemma-2-2b** - நல்ல தரம், மிதமான வேகம்

### உற்பத்தி சூழல்கள்
- **phi-4-mini** - பொதுவான பயன்பாடு
- **deepseek-coder-1.3b** - குறியீடு உருவாக்கம்
- **qwen2.5-7b** - உயர்தர பதில்கள்

## SDK ஆவணங்கள்

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## உதவி பெறுதல்

1. சேவை நிலையை சரிபார்க்கவும்: `foundry service status`
2. பதிவுகளை பார்க்கவும்: Foundry Local சேவை பதிவுகளை சரிபார்க்கவும்
3. SDK ஆவணங்களை பார்க்கவும்: https://github.com/microsoft/Foundry-Local
4. மாதிரி குறியீட்டை மதிப்பாய்வு செய்யவும்: அனைத்து மாதிரிகளுக்கும் விரிவான docstrings உள்ளது

## அடுத்த படிகள்

1. அனைத்து workshop அமர்வுகளையும் வரிசையாக முடிக்கவும்
2. பல மாதிரிகளை முயற்சிக்கவும்
3. உங்கள் பயன்பாடுகளுக்கு மாதிரிகளை மாற்றவும்
4. `SDK_MIGRATION_NOTES.md` ஐ மேம்பட்ட முறைகளுக்கு மதிப்பாய்வு செய்யவும்

---

**கடைசியாக புதுப்பிக்கப்பட்டது**: 2025-01-08  
**Workshop பதிப்பு**: சமீபத்தியது  
**SDK**: Foundry Local Python SDK

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சித்தாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது துல்லியக்குறைவுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.