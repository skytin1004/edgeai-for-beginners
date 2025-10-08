<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7c8a73e11384e3462674273498d0f9a6",
  "translation_date": "2025-10-08T12:05:10+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "my"
}
-->
# အပိုင်း ၁: Foundry Local ကို စတင်အသုံးပြုခြင်း

## အကျဉ်းချုပ်

Windows 11 တွင် Foundry Local ကို ထည့်သွင်းပြီး အဆင်ပြေစွာ ပြင်ဆင်ပါ။ CLI ကို စတင်အသုံးပြုခြင်း၊ hardware acceleration ကို ဖွင့်ခြင်း၊ မော်ဒယ်များကို cache လုပ်ခြင်းတို့ကို လေ့လာပြီး အမြန်ဆုံး local inference ကို ရယူပါ။ ဒီလက်တွေ့အပိုင်းမှာ Phi, Qwen, DeepSeek, GPT-OSS-20B မော်ဒယ်များကို reproducible CLI command များဖြင့် အဆင့်ဆင့် အသုံးပြုနည်းကို လမ်းညွှန်ပေးပါမည်။

## သင်ယူရမည့် ရည်ရွယ်ချက်များ

ဒီအပိုင်းအဆုံးသတ်ချိန်တွင် သင်သည်:

- **ထည့်သွင်းခြင်းနှင့် ပြင်ဆင်ခြင်း**: Windows 11 တွင် Foundry Local ကို အကောင်းဆုံး performance setting များဖြင့် ပြင်ဆင်ပါ
- **CLI လုပ်ဆောင်မှုများကို ကျွမ်းကျင်ခြင်း**: Foundry Local CLI ကို အသုံးပြု၍ မော်ဒယ်များကို စီမံခန့်ခွဲခြင်းနှင့် တင်သွင်းခြင်း
- **Hardware Acceleration ဖွင့်ခြင်း**: ONNXRuntime သို့မဟုတ် WebGPU ဖြင့် GPU acceleration ကို ပြင်ဆင်ပါ
- **မော်ဒယ်များစွာ တင်သွင်းခြင်း**: phi-4, GPT-OSS-20B, Qwen, DeepSeek မော်ဒယ်များကို locally run လုပ်ပါ
- **သင့်ရဲ့ ပထမဆုံး App တည်ဆောက်ခြင်း**: Foundry Local Python SDK ကို အသုံးပြုရန် ရှိပြီးသား နမူနာများကို ပြင်ဆင်ပါ

# မော်ဒယ်ကို စမ်းသပ်ခြင်း (non-interactive single prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

- Windows 11 (22H2 သို့မဟုတ် အထက်)
# Catalog မော်ဒယ်များကို စစ်ဆေးခြင်း (run လုပ်ပြီးမှ loaded မော်ဒယ်များကို တွေ့နိုင်သည်)
foundry model list
## NOTE: လက်ရှိတွင် `--running` flag သီးသန့်မရှိသေးပါ; loaded ဖြစ်နေသည်ကို ကြည့်ရန် chat စတင်ခြင်း သို့မဟုတ် service logs ကို စစ်ဆေးပါ။
- Python 3.10+ ထည့်သွင်းထား
- Visual Studio Code (Python extension ပါဝင်)
- Administrator အခွင့်အရေးများ installation အတွက်လိုအပ်

### (Optional) Environment Variables

`.env` ဖိုင်တစ်ခု ဖန်တီးပါ (သို့မဟုတ် shell တွင် set လုပ်ပါ) scripts များကို portable ဖြစ်စေရန်:
# Compare responses (non-interactive)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
| Variable | ရည်ရွယ်ချက် | ဥပမာ |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | မော်ဒယ် alias ကို သတ်မှတ်ခြင်း (catalog မှ အကောင်းဆုံး variant ကို auto-select လုပ်သည်) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | endpoint ကို override လုပ်ခြင်း (otherwise manager မှ auto) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | streaming demo ကို ဖွင့်ခြင်း | `true` |

> `FOUNDRY_LOCAL_ENDPOINT=auto` (သို့မဟုတ် unset) ဖြစ်ပါက SDK manager မှ derive လုပ်ပါသည်။

## Demo Flow (30 မိနစ်)

### ၁. Foundry Local ကို ထည့်သွင်းပြီး CLI Setup ကို Verify လုပ်ပါ (10 မိနစ်)

# Cached မော်ဒယ်များကို စစ်ဆေးပါ
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Preview / If Supported)**

macOS native package ရှိပါက (latest အတွက် official docs ကို စစ်ဆေးပါ):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

macOS native binaries မရှိသေးပါက:
1. Windows 11 ARM/Intel VM (Parallels / UTM) ကို အသုံးပြု၍ Windows အဆင့်များကို လိုက်နာပါ။
2. Container image ရှိပါက container မှတဆင့် မော်ဒယ်များကို run လုပ်ပြီး `FOUNDRY_LOCAL_ENDPOINT` ကို exposed port သို့ set လုပ်ပါ။

**Python Virtual Environment ဖန်တီးခြင်း (Cross‑Platform)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

pip ကို upgrade လုပ်ပြီး core dependencies များကို ထည့်သွင်းပါ:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### အဆင့် ၁.၂: Installation ကို Verify လုပ်ပါ

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### အဆင့် ၁.၃: Environment ကို ပြင်ဆင်ပါ

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (အကြံပြုထားသည်)

Service ကို manually start လုပ်ပြီး မော်ဒယ်များကို run လုပ်ခြင်းအစား **Foundry Local Python SDK** ကို အသုံးပြု၍ အားလုံးကို bootstrap လုပ်ပါ:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Explicit control ကို သင်နှစ်သက်ပါက CLI + OpenAI client ကို အောက်တွင် ဖော်ပြထားသည့်နည်းဖြင့် အသုံးပြုနိုင်ပါသည်။

### ၂. GPU Acceleration ကို ဖွင့်ပါ (5 မိနစ်)

#### အဆင့် ၂.၁: Hardware Capabilities ကို စစ်ဆေးပါ

```powershell
# Check available compute providers
foundry system info

# List GPU capabilities
foundry system gpu-info
```

#### အဆင့် ၂.၂: Hardware Acceleration ကို ပြင်ဆင်ပါ

```powershell
# Enable ONNX Runtime GPU (if NVIDIA GPU available)
foundry config set compute.onnx.enable_gpu true

# Enable WebGPU for broader hardware support
foundry config set compute.webgpu.enabled true

# Verify configuration
foundry config list
```

### ၃. CLI ဖြင့် မော်ဒယ်များကို locally run လုပ်ပါ (10 မိနစ်)

#### အဆင့် ၃.၁: Phi-4 Model ကို Deploy လုပ်ပါ

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### အဆင့် ၃.၂: GPT-OSS-20B ကို Deploy လုပ်ပါ

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### အဆင့် ၃.၃: အခြား မော်ဒယ်များကို Load လုပ်ပါ

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### ၄. Starter Project: Foundry Local အတွက် 01-run-phi ကို ပြင်ဆင်ပါ (5 မိနစ်)

#### အဆင့် ၄.၁: Basic Chat Application တစ်ခု ဖန်တီးပါ

`samples/01-foundry-quickstart/chat_quickstart.py` ဖိုင်ကို ဖန်တီးပါ (manager ရှိပါက အသုံးပြုရန် update လုပ်ထားသည်):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### အဆင့် ၄.၂: Application ကို စမ်းသပ်ပါ

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## အဓိက အကြောင်းအရာများ

### ၁. Foundry Local Architecture

- **Local Inference Engine**: မော်ဒယ်များကို သင့် device ပေါ်တွင် run လုပ်ပါ
- **OpenAI SDK Compatibility**: ရှိပြီးသား OpenAI code နှင့် seamless integration
- **Model Management**: မော်ဒယ်များကို download, cache, run လုပ်ခြင်း
- **Hardware Optimization**: GPU, NPU, CPU acceleration ကို အသုံးပြုခြင်း

### ၂. CLI Command Reference

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### ၃. Python SDK Integration

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## အခက်အခဲများကို ဖြေရှင်းခြင်း

### အခက်အခဲ ၁: "Foundry command not found"

**ဖြေရှင်းနည်း**:
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### အခက်အခဲ ၂: "Model failed to load"

**ဖြေရှင်းနည်း**:
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### အခက်အခဲ ၃: "Connection refused on localhost:5273"

**ဖြေရှင်းနည်း**:
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Performance Optimization အကြံပြုချက်များ

### ၁. Model Selection Strategy

- **Phi-4-mini**: General tasks အတွက် အကောင်းဆုံး၊ memory usage နည်း
- **Qwen2.5-0.5b**: Inference အမြန်ဆုံး၊ resources နည်း
- **GPT-OSS-20B**: အရည်အသွေး အမြင့်ဆုံး၊ resources ပိုလိုအပ်
- **DeepSeek-Coder**: Programming tasks အတွက် optimize လုပ်ထား

### ၂. Hardware Optimization

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### ၃. Performance ကို စောင့်ကြည့်ခြင်း

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### Optional Enhancements

| Enhancement | ဘာလဲ | ဘယ်လို |
|-------------|------|-----|
| Shared Utilities | client/bootstrap logic ကို duplicate မဖြစ်အောင် ဖယ်ရှားပါ | `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) ကို အသုံးပြုပါ |
| Token Usage Visibility | cost/efficiency ကို စဉ်းစားရန် သင်ကြားပါ | `SHOW_USAGE=1` ကို set လုပ်ပြီး prompt/completion/total tokens ကို print လုပ်ပါ |
| Deterministic Comparisons | benchmarking & regression checks အတွက် စိတ်ချရမှုရှိ | `temperature=0`, `top_p=1`, consistent prompt text ကို အသုံးပြုပါ |
| First-Token Latency | responsiveness metric ကို တိုးတက်စေ | streaming (`BENCH_STREAM=1`) ဖြင့် benchmark script ကို ပြင်ဆင်ပါ |
| Retry on Transient Errors | cold start အတွက် resilient demos | `RETRY_ON_FAIL=1` (default) & `RETRY_BACKOFF` ကို ပြင်ဆင်ပါ |
| Smoke Testing | key flows အတွက် quick sanity | workshop မတိုင်မီ `python Workshop/tests/smoke.py` ကို run လုပ်ပါ |
| Model Alias Profiles | machines အကြား model set ကို အလွယ်တကူ ပြောင်းနိုင် | `.env` ကို `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` ဖြင့် maintain လုပ်ပါ |
| Caching Efficiency | multi-sample run တွင် repeated warmups မဖြစ်အောင် | Utilities cache managers; scripts/notebooks အကြား reuse လုပ်ပါ |
| First Run Warmup | p95 latency spikes ကို လျော့ချ | `FoundryLocalManager` ဖန်တီးပြီး tiny prompt တစ်ခုကို fire လုပ်ပါ |

PowerShell မှ deterministic warm baseline ဥပမာ:

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

ဒုတိယအကြိမ် run လုပ်သော output နှင့် token count တူညီမှုကို တွေ့ရမည်ဖြစ်ပြီး determinism ကို အတည်ပြုပါသည်။

## နောက်တစ်ဆင့်များ

ဒီ session ကို ပြီးဆုံးပြီးနောက်:

1. **Session 2 ကို Explore လုပ်ပါ**: Azure AI Foundry RAG ဖြင့် AI solution များ တည်ဆောက်ပါ
2. **မော်ဒယ်များကို စမ်းသပ်ပါ**: Qwen, DeepSeek နှင့် အခြား မော်ဒယ်များကို စမ်းသပ်ပါ
3. **Performance ကို Optimize လုပ်ပါ**: သင့် hardware အတွက် setting များကို ပြင်ဆင်ပါ
4. **Custom Applications တည်ဆောက်ပါ**: Foundry Local SDK ကို သင့်ရဲ့ project များတွင် အသုံးပြုပါ

## အပိုဆောင်း အရင်းအမြစ်များ

### Documentation
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Sample Code
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### Community
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Session Duration**: 30 မိနစ် လက်တွေ့လုပ်ဆောင်မှု + 15 မိနစ် Q&A
**အဆင့်အတန်း**: Beginner
**လိုအပ်ချက်များ**: Windows 11, Python 3.10+, Administrator access

## Sample Scenario & Workshop Mapping

| Workshop Script / Notebook | Scenario | ရည်ရွယ်ချက် | ဥပမာ Input(s) | Dataset လိုအပ်မှု |
|----------------------------|----------|------|------------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Internal IT team သည် privacy assessment portal အတွက် on‑device inference ကို စမ်းသပ်နေသည် | local SLM သည် standard prompts တွင် sub‑second latency ဖြင့် တုံ့ပြန်နိုင်ကြောင်း သက်သေပြပါ | "List two benefits of local inference." | None (single prompt) |
| Quickstart adaptation code block | Developer သည် ရှိပြီးသား OpenAI script ကို Foundry Local သို့ ပြောင်းနေသည် | drop‑in compatibility ကို ပြပါ | "Give two benefits of local inference." | Inline prompt only |

### Scenario Narrative
Security & compliance team သည် sensitive prototype data ကို locally process လုပ်နိုင်မည်ဖြစ်ကြောင်း အတည်ပြုရန် လိုအပ်သည်။ သူတို့သည် bootstrap script ကို privacy, latency, cost စသည့် prompts များဖြင့် deterministic temperature=0 mode ဖြင့် run လုပ်ပြီး baseline outputs ကို later comparison အတွက် capture လုပ်သည် (Session 3 benchmarking နှင့် Session 4 SLM vs LLM contrast).

### Minimal Prompt Set JSON (optional)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

ဒီ list ကို reproducible evaluation loop တစ်ခု ဖန်တီးရန် သို့မဟုတ် အနာဂတ် regression test harness အတွက် seed လုပ်ရန် အသုံးပြုပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် ရှုယူသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။