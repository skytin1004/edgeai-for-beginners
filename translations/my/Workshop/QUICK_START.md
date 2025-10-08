<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-08T11:58:57+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "my"
}
-->
# အလုပ်ရုံဆွေးနွေးပွဲ အစောပိုင်း လမ်းညွှန်

## ကြိုတင်လိုအပ်ချက်များ

### 1. Foundry Local ကို ထည့်သွင်းပါ

တရားဝင် ထည့်သွင်းလမ်းညွှန်ကို လိုက်နာပါ:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Python အခြေခံလိုအပ်ချက်များ ထည့်သွင်းပါ

Workshop ဖိုင်တွဲမှ:

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

## Workshop နမူနာများကို အလုပ်လုပ်စေခြင်း

### အစည်းအဝေး 01: အခြေခံ စကားပြော

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**ပတ်ဝန်းကျင် အပြောင်းအလဲများ:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### အစည်းအဝေး 02: RAG ပိုက်လိုင်း

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**ပတ်ဝန်းကျင် အပြောင်းအလဲများ:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### အစည်းအဝေး 02: RAG အကဲဖြတ်ခြင်း (Ragas)

```bash
python rag_eval_ragas.py
```

**မှတ်ချက်**: `requirements.txt` မှတဆင့် ထပ်ဆင့်လိုအပ်ချက်များ ထည့်သွင်းရန် လိုအပ်သည်

### အစည်းအဝေး 03: စမ်းသပ်မှု

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**ပတ်ဝန်းကျင် အပြောင်းအလဲများ:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**အထွက်**: JSON ဖြင့် latency, throughput, နှင့် first-token အချက်အလက်များ

### အစည်းအဝေး 04: မော်ဒယ် နှိုင်းယှဉ်မှု

```bash
cd Workshop/samples/session04
python model_compare.py
```

**ပတ်ဝန်းကျင် အပြောင်းအလဲများ:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### အစည်းအဝေး 05: Multi-Agent Orchestration

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**ပတ်ဝန်းကျင် အပြောင်းအလဲများ:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### အစည်းအဝေး 06: မော်ဒယ် Router

```bash
cd Workshop/samples/session06
python models_router.py
```

**စမ်းသပ်မှု**: အမျိုးမျိုးသော ရည်ရွယ်ချက်များ (code, summarize, classification) ဖြင့် routing logic

### အစည်းအဝေး 06: ပိုက်လိုင်း

```bash
python models_pipeline.py
```

**ရှုပ်ထွေးသော အဆင့်များစွာပါဝင်သော ပိုက်လိုင်း** - စီစဉ်ခြင်း၊ အကောင်အထည်ဖော်ခြင်း၊ ပြန်လည်တိုးတက်မှု

## စာရွက်စာတမ်းများ

### စမ်းသပ်မှု အစီရင်ခံစာ ထုတ်ယူခြင်း

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**အထွက်**: Markdown ဇယား + JSON အချက်အလက်များ

### Markdown CLI ပုံစံများကို Lint

```bash
python lint_markdown_cli.py --verbose
```

**ရည်ရွယ်ချက်**: စာရွက်စာတမ်းများတွင် သက်တမ်းကုန် CLI ပုံစံများ ရှာဖွေခြင်း

## စမ်းသပ်မှု

### Smoke စမ်းသပ်မှု

```bash
cd Workshop
python -m tests.smoke
```

**စမ်းသပ်မှုများ**: အဓိက နမူနာများ၏ အခြေခံ လုပ်ဆောင်မှု

## ပြဿနာများ ဖြေရှင်းခြင်း

### ဝန်ဆောင်မှု မသွားခြင်း

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Module Import ပြဿနာများ

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### ချိတ်ဆက်မှု ပြဿနာများ

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### မော်ဒယ် မတွေ့ရှိခြင်း

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## ပတ်ဝန်းကျင် အပြောင်းအလဲ ကိုးကားချက်

### အဓိက ဖွဲ့စည်းမှု
| Variable | Default | Description |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Varies | အသုံးပြုမည့် မော်ဒယ် အမည် |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | ဝန်ဆောင်မှု endpoint ကို ပြောင်းလဲရန် |
| `SHOW_USAGE` | `0` | Token အသုံးပြုမှု အချက်အလက် ပြရန် |
| `RETRY_ON_FAIL` | `1` | ပြန်လည်ကြိုးစားမှု logic ဖွင့်ရန် |
| `RETRY_BACKOFF` | `1.0` | ပြန်လည်ကြိုးစားမှု အချိန်နှောင့်နှေးမှု (စက္ကန့်) |

### အစည်းအဝေးအလိုက်
| Variable | Default | Description |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding မော်ဒယ် |
| `RAG_QUESTION` | See sample | RAG စမ်းသပ်မေးခွန်း |
| `BENCH_MODELS` | Varies | Comma ဖြင့် ခွဲထားသော မော်ဒယ်များ |
| `BENCH_ROUNDS` | `3` | စမ်းသပ်မှု အကြိမ်ရေ |
| `BENCH_PROMPT` | See sample | စမ်းသပ်မှု prompt |
| `BENCH_STREAM` | `0` | First-token latency ကို တိုင်းတာရန် |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | အဓိက agent မော်ဒယ် |
| `AGENT_MODEL_EDITOR` | Primary | Editor agent မော်ဒယ် |
| `SLM_ALIAS` | `phi-4-mini` | Small language model |
| `LLM_ALIAS` | `qwen2.5-7b` | Large language model |
| `COMPARE_PROMPT` | See sample | နှိုင်းယှဉ်မှု prompt |

## အကြံပြု မော်ဒယ်များ

### ဖွံ့ဖြိုးမှုနှင့် စမ်းသပ်မှု
- **phi-4-mini** - အရည်အသွေးနှင့် အမြန်နှုန်း အချိုးကျ
- **qwen2.5-0.5b** - Classification အတွက် အလွန်မြန်ဆန်
- **gemma-2-2b** - အရည်အသွေးကောင်း၊ အလတ်စား အမြန်နှုန်း

### ထုတ်လုပ်မှု အခြေအနေများ
- **phi-4-mini** - အထွေထွေ ရည်ရွယ်ချက်
- **deepseek-coder-1.3b** - Code ဖန်တီးမှု
- **qwen2.5-7b** - အရည်အသွေးမြင့် ပြန်လည်ဖြေရှင်းမှု

## SDK စာရွက်စာတမ်း

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## အကူအညီ ရယူခြင်း

1. ဝန်ဆောင်မှု အခြေအနေ စစ်ဆေးရန်: `foundry service status`
2. Log များ ကြည့်ရန်: Foundry Local ဝန်ဆောင်မှု log များကို စစ်ဆေးပါ
3. SDK စာရွက်စာတမ်း ကြည့်ရန်: https://github.com/microsoft/Foundry-Local
4. နမူနာကုဒ် ပြန်လည်ကြည့်ရန်: နမူနာများတွင် အသေးစိတ် docstring များ ပါဝင်သည်

## နောက်တစ်ဆင့်

1. အလုပ်ရုံဆွေးနွေးပွဲ အစည်းအဝေးများအားလုံး အစဉ်လိုက် ပြီးမြောက်ပါ
2. မော်ဒယ်အမျိုးမျိုးဖြင့် စမ်းသပ်ပါ
3. သင့်ရည်ရွယ်ချက်အတွက် နမူနာများ ပြင်ဆင်ပါ
4. `SDK_MIGRATION_NOTES.md` ကို ကြည့်ပြီး အဆင့်မြင့် ပုံစံများကို လေ့လာပါ

---

**နောက်ဆုံး အပ်ဒိတ်**: 2025-01-08  
**Workshop ဗားရှင်း**: နောက်ဆုံး  
**SDK**: Foundry Local Python SDK

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။