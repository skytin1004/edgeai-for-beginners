<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-08T12:14:35+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "my"
}
-->
# အစည်းအဝေး ၃: Foundry Local တွင် Open-Source မော်ဒယ်များ

## အကျဉ်းချုပ်

Hugging Face နှင့် အခြားသော Open-Source မော်ဒယ်များကို Foundry Local တွင် အသုံးပြုနည်းကို ရှာဖွေပါ။ မော်ဒယ်ရွေးချယ်မှုနည်းလမ်းများ၊ အသိုင်းအဝိုင်းအထောက်အပံ့လုပ်ငန်းစဉ်များ၊ စွမ်းဆောင်ရည်နှိုင်းယှဉ်မှုနည်းလမ်းများနှင့် Foundry ကို မော်ဒယ်မှတ်ပုံတင်မှုအထူးပြုလုပ်နည်းများကို လေ့လာပါ။ ဒီအစည်းအဝေးသည် "Model Mondays" အပတ်စဉ်အကွေ့အကွင်းများနှင့် ဆက်စပ်ပြီး Open-Source မော်ဒယ်များကို Azure သို့ အဆင့်မြှင့်မတင်မီ ဒေသတွင်းတွင် အကဲဖြတ်ပြီး လုပ်ငန်းဆောင်တာများအတွက် အသုံးချနိုင်စေရန် သင့်အား ပြင်ဆင်ပေးပါသည်။

## သင်ယူရမည့်ရည်ရွယ်ချက်များ

ဒီအစည်းအဝေးအပြီးတွင် သင်သည် အောက်ပါအရာများကို လုပ်နိုင်မည်ဖြစ်သည်-

- **ရှာဖွေခြင်းနှင့် အကဲဖြတ်ခြင်း**: အရည်အသွေးနှင့် အရင်းအမြစ်အလဲအလှယ်များကို အသုံးပြု၍ မော်ဒယ်များ (mistral, gemma, qwen, deepseek) ရွေးချယ်ပါ။
- **တင်သွင်းခြင်းနှင့် အလုပ်လုပ်ခြင်း**: Foundry Local CLI ကို အသုံးပြု၍ အသိုင်းအဝိုင်းမော်ဒယ်များကို ဒေါင်းလုဒ်လုပ်၊ cache ထားပြီး စတင်အသုံးပြုပါ။
- **စွမ်းဆောင်ရည်တိုင်းတာခြင်း**: latency + token throughput + အရည်အသွေးအညွှန်းများကို တိကျစွာ အသုံးပြုပါ။
- **တိုးချဲ့ခြင်း**: SDK-compatible ပုံစံများကို လိုက်နာ၍ မော်ဒယ် wrapper ကို မှတ်ပုံတင်ခြင်း သို့မဟုတ် အထူးပြုလုပ်ပါ။
- **နှိုင်းယှဉ်ခြင်း**: SLM နှင့် အလယ်အလတ် LLM မော်ဒယ်ရွေးချယ်မှုအတွက် ဖွဲ့စည်းထားသော နှိုင်းယှဉ်မှုများကို ထုတ်လုပ်ပါ။

## ကြိုတင်လိုအပ်ချက်များ

- အစည်းအဝေး ၁ နှင့် ၂ ကို ပြီးစီးထားရမည်
- Python ပတ်ဝန်းကျင်တွင် `foundry-local-sdk` ကို ထည့်သွင်းထားရမည်
- မော်ဒယ် cache များအတွက် 15GB အနည်းဆုံး disk အခွင့်အာဏာရှိရမည်
- အလိုအလျောက်: GPU/WebGPU acceleration ကို ဖွင့်ထားရမည် (`foundry config list`)

### Cross-Platform ပတ်ဝန်းကျင် အမြန်စတင်ခြင်း

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS မှ Windows host service ကို benchmark လုပ်မည်ဆိုပါက:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## အစမ်းပြသမှု လုပ်ငန်းစဉ် (၃၀ မိနစ်)

### ၁. Hugging Face မော်ဒယ်များကို CLI မှတစ်ဆင့် Load လုပ်ခြင်း (၈ မိနစ်)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### ၂. အလုပ်လုပ်ခြင်းနှင့် အမြန်စစ်ဆေးခြင်း (၅ မိနစ်)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### ၃. Benchmark Script (၈ မိနစ်)

`samples/03-oss-models/benchmark_models.py` ဖိုင်ကို ဖန်တီးပါ:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Run:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### ၄. စွမ်းဆောင်ရည်နှိုင်းယှဉ်ခြင်း (၅ မိနစ်)

Trade-offs များကို ဆွေးနွေးပါ- load အချိန်၊ memory footprint (Task Manager / `nvidia-smi` / OS resource monitor တွင် ကြည့်ရှုပါ)၊ အရည်အသွေးနှင့် အမြန်နှုန်း။ Python benchmark script (Session 3) ကို latency & throughput အတွက် အသုံးပြုပါ၊ GPU acceleration ကို ဖွင့်ပြီး ထပ်မံလုပ်ဆောင်ပါ။

### ၅. Starter Project (၄ မိနစ်)

Benchmarking script ကို markdown export ဖြင့် တိုးချဲ့ပြီး မော်ဒယ်နှိုင်းယှဉ်မှုအစီရင်ခံစာ generator တစ်ခု ဖန်တီးပါ။

## Starter Project: `03-huggingface-models` ကို တိုးချဲ့ပါ

ရရှိထားသော sample ကို အောက်ပါအတိုင်း တိုးချဲ့ပါ-

1. Benchmark aggregation + CSV/Markdown output ထည့်သွင်းပါ။
2. ရိုးရှင်းသော အရည်အသွေး scoring (prompt pair set + manual annotation stub file) ကို အကောင်အထည်ဖော်ပါ။
3. Pluggable မော်ဒယ်စာရင်းနှင့် prompt set အတွက် JSON config (`models.json`) ထည့်သွင်းပါ။

## အတည်ပြုမှု စစ်ဆေးမှုစာရင်း

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Target မော်ဒယ်များအားလုံးသည် ပေါ်လာပြီး probe chat request ကို တုံ့ပြန်ရမည်။

## အစမ်းအဖြစ်အပျက်နှင့် Workshop Mapping

| Workshop Script | အဖြစ်အပျက် | ရည်ရွယ်ချက် | Prompt / Dataset အရင်းအမြစ် |
|-----------------|------------|-------------|-----------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Edge platform အဖွဲ့သည် embedded summarizer အတွက် default SLM ကို ရွေးချယ်နေသည် | latency + p95 + tokens/sec နှိုင်းယှဉ်မှုကို မော်ဒယ်များအကြား ထုတ်လုပ်ပါ | Inline `PROMPT` var + environment `BENCH_MODELS` list |

### အဖြစ်အပျက်အကြောင်းအရာ
Product engineering သည် offline meeting-notes feature အတွက် lightweight summarization မော်ဒယ်ကို default အဖြစ် ရွေးချယ်ရမည်။ သူတို့သည် ထိန်းချုပ်ထားသော deterministic benchmarks (temperature=0) ကို fixed prompt set (အောက်တွင် ဥပမာကြည့်ပါ) ဖြင့် လုပ်ဆောင်ပြီး GPU acceleration ရှိ/မရှိဖြင့် latency + throughput metrics ကို စုဆောင်းပါသည်။

### Prompt Set JSON ဥပမာ (တိုးချဲ့နိုင်သည်)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

မော်ဒယ်တစ်ခုစီအတွက် prompt တစ်ခုစီကို loop လုပ်ပြီး per-prompt latency ကို စုဆောင်းကာ distribution metrics ကို ရယူပါ၊ outliers ကို ရှာဖွေပါ။

## မော်ဒယ်ရွေးချယ်မှု Framework

| Dimension | Metric | အရေးကြီးသောအကြောင်းအရာ |
|----------|--------|--------------------------|
| Latency | avg / p95 | အသုံးပြုသူအတွေ့အကြုံအမြဲတမ်းတည်ရှိမှု |
| Throughput | tokens/sec | Batch & streaming scalability |
| Memory | resident size | Device fit & concurrency |
| Quality | rubric prompts | Task suitability |
| Footprint | disk cache | Distribution & updates |
| License | use allowance | Commercial compliance |

## Custom Model ဖြင့် တိုးချဲ့ခြင်း

အဆင့်မြင့်ပုံစံ (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Adapter interface များအတွက် တိုးတက်မှုများကို အတည်ပြုရန် အတိအကျ repo ကို ကြည့်ပါ:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## ပြဿနာများကို ဖြေရှင်းခြင်း

| ပြဿနာ | အကြောင်းအရင်း | ဖြေရှင်းနည်း |
|-------|---------------|-------------|
| mistral-7b တွင် OOM | RAM/GPU မလုံလောက်ခြင်း | အခြားမော်ဒယ်များကို ရပ်ထားပါ၊ သေးငယ်သော variant ကို စမ်းပါ |
| ပထမဆုံးတုံ့ပြန်မှုနှေးကွေး | Cold load | Periodic lightweight prompt ဖြင့် warm ထားပါ |
| Download ရပ်တန့် | Network မတည်ငြိမ်မှု | ထပ်မံကြိုးစားပါ၊ off-peak အချိန်တွင် prefetch လုပ်ပါ |

## ရင်းမြစ်များ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Session အချိန်**: ၃၀ မိနစ် (+ အလိုအလျောက် အနက်ရှိုင်းစွာ လေ့လာမှု)  
**အခက်အခဲအဆင့်**: အလယ်အလတ်

### အလိုအလျောက် တိုးချဲ့မှုများ

| တိုးချဲ့မှု | အကျိုးကျေးဇူး | လုပ်နည်း |
|-------------|--------------|---------|
| Streaming First-Token Latency | Perceived responsiveness ကို တိုင်းတာသည် | `BENCH_STREAM=1` ဖြင့် benchmark run လုပ်ပါ (`Workshop/samples/session03` တွင် တိုးချဲ့ထားသော script) |
| Deterministic Mode | Stable regression comparisons | `temperature=0`, fixed prompt set, JSON outputs ကို version control အောက်တွင် capture လုပ်ပါ |
| Quality Rubric Scoring | အရည်အသွေးအတိုင်းအတာ ထည့်သွင်းသည် | `prompts.json` ကို expected facets ဖြင့် ထိန်းသိမ်းပါ၊ score (1–5) များကို manual သို့မဟုတ် secondary model ဖြင့် annotate လုပ်ပါ |
| CSV / Markdown Export | အစီရင်ခံစာမျှဝေနိုင်သည် | `benchmark_report.md` ကို table & highlights ဖြင့် ရေးသားရန် script ကို တိုးချဲ့ပါ |
| Model Capability Tags | Automated routing အတွက် အထောက်အကူပြုသည် | `{alias: {capabilities:[], size_mb:..}}` ဖြင့် `models.json` ကို ထိန်းသိမ်းပါ |
| Cache Warmup Phase | Cold-start bias ကို လျှော့ချသည် | Timing loop မတိုင်မီ warm round တစ်ခုကို run လုပ်ပါ (ပြီးသား implementation) |
| Percentile Accuracy | Robust tail latency | numpy percentile ကို အသုံးပြုပါ (refactored script တွင် ရှိပြီးသား) |
| Token Cost Approximation | စီးပွားရေးနှိုင်းယှဉ်မှု | Approx cost = (tokens/sec * avg tokens per request) * energy heuristic |
| Auto-Skipping Failed Models | Batch runs တွင် resilience | try/except ဖြင့် benchmark တစ်ခုစီကို wrap လုပ်ပြီး status field ကို mark လုပ်ပါ |

#### Minimal Markdown Export Snippet

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Deterministic Prompt Set Example

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Static list ကို loop လုပ်ပြီး commits အကြား comparable metrics အတွက် random prompts မဟုတ်ဘဲ အသုံးပြုပါ။

---

**ဝန်ခံချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူလဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတည်သောရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအချော်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။