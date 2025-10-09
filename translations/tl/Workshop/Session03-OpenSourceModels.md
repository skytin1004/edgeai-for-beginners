<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-09T19:26:30+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "tl"
}
-->
# Session 3: Mga Open-Source na Modelo sa Foundry Local

## Abstrak

Alamin kung paano dalhin ang mga modelo mula sa Hugging Face at iba pang open-source na modelo sa Foundry Local. Matutunan ang mga estratehiya sa pagpili, mga workflow para sa kontribusyon sa komunidad, metodolohiya ng paghahambing ng performance, at kung paano palawakin ang Foundry gamit ang custom na pagpaparehistro ng modelo. Ang sesyong ito ay nakatuon sa lingguhang tema ng "Model Mondays" at magbibigay sa iyo ng kakayahang suriin at gamitin ang mga open-source na modelo nang lokal bago ito i-scale sa Azure.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng sesyon, magagawa mo ang:

- **Matuklasan at Suriin**: Tukuyin ang mga posibleng modelo (mistral, gemma, qwen, deepseek) gamit ang trade-offs sa kalidad at resources.
- **I-load at Patakbuhin**: Gamitin ang Foundry Local CLI upang mag-download, mag-cache, at magpatakbo ng mga modelo mula sa komunidad.
- **Benchmark**: Mag-apply ng pare-parehong latency + token throughput + mga heuristics ng kalidad.
- **Palawakin**: Magparehistro o mag-adapt ng custom na model wrapper gamit ang mga pattern na compatible sa SDK.
- **Ihambing**: Gumawa ng mga nakabalangkas na paghahambing para sa mga desisyon sa pagpili ng SLM vs mid-size LLM.

## Mga Kinakailangan

- Natapos ang Sessions 1 & 2
- Python environment na may naka-install na `foundry-local-sdk`
- Hindi bababa sa 15GB na libreng disk space para sa maraming model caches
- Opsyonal: Naka-enable na GPU/WebGPU acceleration (`foundry config list`)

### Mabilis na Simula sa Cross-Platform Environment

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

Kapag nagbe-benchmark mula sa macOS laban sa Windows host service, itakda:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Daloy ng Demo (30 minuto)

### 1. I-load ang Hugging Face Models gamit ang CLI (8 minuto)

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

### 2. Patakbuhin at Mabilisang Suriin (5 minuto)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```

### 3. Benchmark Script (8 minuto)

Gumawa ng `samples/03-oss-models/benchmark_models.py`:

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

Patakbuhin:

```powershell
python samples/03-oss-models/benchmark_models.py
```

### 4. Ihambing ang Performance (5 minuto)

Talakayin ang mga trade-offs: oras ng pag-load, memory footprint (obserbahan ang Task Manager / `nvidia-smi` / OS resource monitor), kalidad ng output laban sa bilis. Gamitin ang Python benchmark script (Session 3) para sa latency at throughput; ulitin pagkatapos i-enable ang GPU acceleration.

### 5. Panimulang Proyekto (4 minuto)

Gumawa ng generator para sa ulat ng paghahambing ng modelo (palawakin ang benchmarking script gamit ang markdown export).

## Panimulang Proyekto: Palawakin ang `03-huggingface-models`

Pagandahin ang umiiral na sample sa pamamagitan ng:

1. Pagdaragdag ng benchmark aggregation + output ng CSV/Markdown.
2. Pagpapatupad ng simpleng qualitative scoring (prompt pair set + manual annotation stub file).
3. Pagpapakilala ng JSON config (`models.json`) para sa pluggable na listahan ng modelo at prompt set.

## Checklist ng Pagpapatunay

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Lahat ng target na modelo ay dapat lumabas at tumugon sa isang probe chat request.

## Halimbawang Scenario at Pagmamapa ng Workshop

| Workshop Script | Scenario | Layunin | Pinagmulan ng Prompt / Dataset |
|-----------------|----------|---------|--------------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Edge platform team na pumipili ng default na SLM para sa embedded summarizer | Gumawa ng paghahambing ng latency + p95 + tokens/sec sa mga posibleng modelo | Inline `PROMPT` var + environment `BENCH_MODELS` list |

### Naratibo ng Scenario
Kailangang pumili ang product engineering ng default na magaan na summarization model para sa offline na tampok ng meeting-notes. Sila ay nagsasagawa ng kontroladong deterministic benchmarks (temperature=0) gamit ang nakapirming prompt set (tingnan ang halimbawa sa ibaba) at nangongolekta ng latency + throughput metrics na may at walang GPU acceleration.

### Halimbawa ng Prompt Set JSON (maaaring palawakin)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

I-loop ang bawat prompt sa bawat modelo, kunin ang latency per-prompt upang makuha ang mga distribution metrics at matukoy ang mga outlier.

## Framework sa Pagpili ng Modelo

| Dimensyon | Sukatan | Bakit Mahalaga |
|-----------|---------|----------------|
| Latency   | avg / p95 | Konsistensya ng karanasan ng user |
| Throughput | tokens/sec | Batch at streaming scalability |
| Memory    | laki ng residente | Kakayahan ng device at concurrency |
| Kalidad   | rubric prompts | Angkop para sa gawain |
| Footprint | disk cache | Pamamahagi at mga update |
| Lisensya  | pahintulot sa paggamit | Pagsunod sa komersyal na patakaran |

## Pagpapalawak Gamit ang Custom na Modelo

Pangkalahatang pattern (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Konsultahin ang opisyal na repo para sa mga umuusbong na adapter interfaces:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Pag-aayos ng Problema

| Isyu | Sanhi | Solusyon |
|------|-------|----------|
| OOM sa mistral-7b | Kulang na RAM/GPU | Itigil ang ibang mga modelo; subukan ang mas maliit na variant |
| Mabagal na unang tugon | Cold load | Panatilihing mainit gamit ang periodic na magaan na prompt |
| Pagkaantala sa pag-download | Kawalan ng katatagan sa network | Subukang muli; mag-prefetch sa off-peak na oras |

## Mga Sanggunian

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Tagal ng Session**: 30 minuto (+ opsyonal na mas malalim na talakayan)  
**Kahirapan**: Intermediate

### Opsyonal na Mga Pagpapahusay

| Pagpapahusay | Benepisyo | Paano |
|--------------|-----------|-------|
| Streaming First-Token Latency | Sinusukat ang nararamdamang responsiveness | Patakbuhin ang benchmark gamit ang `BENCH_STREAM=1` (pinahusay na script sa `Workshop/samples/session03`) |
| Deterministic Mode | Matatag na paghahambing ng regression | `temperature=0`, nakapirming prompt set, kunin ang mga JSON output sa ilalim ng version control |
| Quality Rubric Scoring | Nagdadagdag ng qualitative na dimensyon | Panatilihin ang `prompts.json` na may inaasahang aspeto; i-annotate ang mga score (1–5) nang manu-mano o gamit ang pangalawang modelo |
| CSV / Markdown Export | Maibabahaging ulat | Palawakin ang script upang magsulat ng `benchmark_report.md` na may table at highlights |
| Model Capability Tags | Tumutulong sa automated na pag-route sa hinaharap | Panatilihin ang `models.json` na may `{alias: {capabilities:[], size_mb:..}}` |
| Cache Warmup Phase | Binabawasan ang bias ng cold-start | Magpatupad ng isang warm round bago ang timing loop (naipatupad na) |
| Percentile Accuracy | Matatag na tail latency | Gamitin ang numpy percentile (na sa refactored script na) |
| Token Cost Approximation | Paghahambing ng gastos | Approx cost = (tokens/sec * avg tokens per request) * energy heuristic |
| Auto-Skipping Failed Models | Resilience sa batch runs | I-wrap ang bawat benchmark sa try/except at markahan ang status field |

#### Minimal na Snippet para sa Markdown Export

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### Halimbawa ng Deterministic Prompt Set

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

I-loop ang static na listahan sa halip na random na mga prompt para sa maihahambing na mga sukatan sa bawat commit.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.