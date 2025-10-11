<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-11T11:57:14+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "ta"
}
-->
# அமர்வு 3: Foundry Local-ல் திறந்த மூல மாடல்கள்

## சுருக்கம்

Hugging Face மற்றும் பிற திறந்த மூல மாடல்களை Foundry Local-க்கு கொண்டு வருவது எப்படி என்பதை அறிக. தேர்வு உத்திகள், சமூக பங்களிப்பு பணிமுறைகள், செயல்திறன் ஒப்பீடு முறைமைகள் மற்றும் Foundry-யை தனிப்பயன் மாடல் பதிவு மூலம் விரிவாக்குவது எப்படி என்பதை கற்றுக்கொள்ளுங்கள். இந்த அமர்வு வாராந்திர "Model Mondays" ஆராய்ச்சி கருப்பொருள்களுடன் இணைக்கப்படுகிறது மற்றும் Azure-க்கு பரப்புவதற்கு முன் திறந்த மூல மாடல்களை உள்ளூர் அளவில் மதிப்பீடு செய்து செயல்படுத்த உங்களை சீரமைக்கிறது.

## கற்றல் நோக்கங்கள்

இவ்வமர்வு முடிவில், நீங்கள்:

- **கண்டறிதல் & மதிப்பீடு**: தரம் மற்றும் வளங்களின் சமநிலையைப் பயன்படுத்தி (mistral, gemma, qwen, deepseek போன்ற) மாடல்களை அடையாளம் காணவும்.
- **ஏற்றுதல் & இயக்கம்**: Foundry Local CLI-யை பயன்படுத்தி சமூக மாடல்களை பதிவிறக்கவும், சேமிக்கவும், இயக்கவும்.
- **மதிப்பீடு**: மாறாத தாமதம் + டோக்கன் துரிதம் + தரம் அளவுகோல்களைப் பயன்படுத்தவும்.
- **விரிவாக்கம்**: SDK-க்கு இணக்கமான முறைமைகளைப் பின்பற்றும் தனிப்பயன் மாடல் மூடிகளை பதிவு செய்யவும் அல்லது மாற்றவும்.
- **ஒப்பீடு**: SLM மற்றும் நடுத்தர அளவிலான LLM தேர்வு முடிவுகளுக்கான அமைப்பான ஒப்பீடுகளை உருவாக்கவும்.

## முன் தேவைகள்

- அமர்வு 1 மற்றும் 2 முடிக்கப்பட்டிருக்க வேண்டும்
- `foundry-local-sdk` நிறுவப்பட்ட Python சூழல்
- பல மாடல் சேமிப்புகளுக்காக குறைந்தது 15GB இலவச டிஸ்க் இடம்
- விருப்பம்: GPU/WebGPU வேகப்படுத்தல் இயக்கப்பட்டது (`foundry config list`)

### பல்வேறு தள சூழல் விரைவான தொடக்கம்

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

macOS-ல் இருந்து Windows ஹோஸ்ட் சேவையை மதிப்பீடு செய்யும்போது அமைக்கவும்:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## டெமோ ஓட்டம் (30 நிமிடங்கள்)

### 1. CLI மூலம் Hugging Face மாடல்களை ஏற்றுதல் (8 நிமிடங்கள்)

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


### 2. இயக்கம் & விரைவான சோதனை (5 நிமிடங்கள்)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. மதிப்பீடு ஸ்கிரிப்ட் (8 நிமிடங்கள்)

`samples/03-oss-models/benchmark_models.py` உருவாக்கவும்:

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

இயக்கவும்:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. செயல்திறன் ஒப்பீடு (5 நிமிடங்கள்)

சந்தேகங்கள்: ஏற்றுதல் நேரம், நினைவக அளவு (Task Manager / `nvidia-smi` / OS resource monitor-ஐ கவனிக்கவும்), வெளியீட்டு தரம் மற்றும் வேகம். Python மதிப்பீடு ஸ்கிரிப்டை (அமர்வு 3) தாமதம் மற்றும் துரிதத்திற்காக பயன்படுத்தவும்; GPU வேகப்படுத்தலை இயக்கிய பிறகு மீண்டும் முயற்சிக்கவும்.

### 5. தொடக்க திட்டம் (4 நிமிடங்கள்)

மாடல் ஒப்பீடு அறிக்கை உருவாக்கியை உருவாக்கவும் (மதிப்பீடு ஸ்கிரிப்டை markdown ஏற்றுமதியுடன் விரிவாக்கவும்).

## தொடக்க திட்டம்: `03-huggingface-models`-ஐ விரிவாக்கம்

இருக்கக்கூடிய மாதிரியை மேம்படுத்தவும்:

1. மதிப்பீடு தொகுப்பு + CSV/Markdown வெளியீட்டைச் சேர்க்கவும்.
2. எளிய தரமான மதிப்பீடு (உரையாடல் ஜோடி தொகுப்பு + கையேடு குறிப்பு கோப்பு) செயல்படுத்தவும்.
3. JSON அமைப்பை (`models.json`) மாடல் பட்டியல் மற்றும் உரையாடல் தொகுப்புக்காக அறிமுகப்படுத்தவும்.

## சரிபார்ப்பு சோதனை பட்டியல்

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

அனைத்து இலக்கு மாடல்களும் தோன்ற வேண்டும் மற்றும் ஒரு சோதனை உரையாடல் கோரிக்கைக்கு பதிலளிக்க வேண்டும்.

## மாதிரி சூழல் & பணிமுறை வரைபடம்

| பணிமுறை ஸ்கிரிப்ட் | சூழல் | இலக்கு | உரையாடல் / தரவுத்தொகுப்பு மூலங்கள் |
|--------------------|--------|-------|------------------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | எட்ஜ் தளம் குழு, உள்ளமைக்கப்பட்ட சுருக்கமூட்டியைத் தேர்ந்தெடுக்கும் | வேகத்தன்மை + p95 + டோக்கன்கள்/வினாடி ஒப்பீடு உருவாக்கவும் | Inline `PROMPT` var + சூழல் `BENCH_MODELS` பட்டியல் |

### சூழல் கதை

தயாரிப்பு பொறியியல் குழு, ஆஃப்லைன் கூட்டக் குறிப்புகளுக்கான சிறிய சுருக்கமூட்டல் மாடலைத் தேர்ந்தெடுக்க வேண்டும். அவர்கள் கட்டுப்படுத்தப்பட்ட தீர்மானமிக்க மதிப்பீடுகளை (temperature=0) நிரந்தர உரையாடல் தொகுப்பில் (கீழே உள்ள உதாரணத்தைப் பார்க்கவும்) இயக்கி, GPU வேகப்படுத்தலுடன் மற்றும் இல்லாமல் தாமதம் + துரித அளவுகோல்களை சேகரிக்கின்றனர்.

### உதாரண உரையாடல் தொகுப்பு JSON (விரிவாக்கக்கூடியது)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

ஒவ்வொரு மாடலுக்கும் ஒவ்வொரு உரையாடலையும் மடக்கி, ஒவ்வொரு உரையாடலின் தாமதத்தைப் பதிவு செய்து விநியோக அளவுகோல்களை உருவாக்கவும் மற்றும் வெளிப்படையான மதிப்பீடுகளை கண்டறியவும்.

## மாடல் தேர்வு கட்டமைப்பு

| பரிமாணம் | அளவுகோல் | ஏன் இது முக்கியம் |
|----------|----------|-------------------|
| தாமதம் | சராசரி / p95 | பயனர் அனுபவத்தின் நிலைத்தன்மை |
| துரிதம் | டோக்கன்கள்/வினாடி | தொகுதி மற்றும் ஸ்ட்ரீமிங் அளவீடு |
| நினைவகம் | நிலையான அளவு | சாதன பொருத்தம் மற்றும் ஒரே நேரத்தில் செயல்பாடு |
| தரம் | அளவுகோல் உரையாடல்கள் | பணிக்கான பொருத்தம் |
| தடம் | டிஸ்க் சேமிப்பு | விநியோகம் மற்றும் புதுப்பிப்புகள் |
| உரிமம் | பயன்பாட்டு அனுமதி | வணிக இணக்கம் |

## தனிப்பயன் மாடலுடன் விரிவாக்கம்

உயர் நிலை முறை (பசுடோ):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

மாறும் அடாப்டர் இடைமுகங்களுக்கான அதிகாரப்பூர்வ களஞ்சியத்தைப் பார்க்கவும்:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## சிக்கல்களை சரிசெய்தல்

| சிக்கல் | காரணம் | தீர்வு |
|--------|--------|-------|
| mistral-7b-ல் OOM | போதுமான RAM/GPU இல்லை | பிற மாடல்களை நிறுத்தவும்; சிறிய மாறுபாட்டை முயற்சிக்கவும் |
| முதல் பதில் மெதுவாக | குளிர்ந்த ஏற்றுதல் | ஒரு குறைந்த எடை உரையாடலுடன் காலகட்டமாக சூடாக வைத்திருக்கவும் |
| பதிவிறக்கம் தடைபடுகிறது | நெட்வொர்க் நிலைத்தன்மை | மீண்டும் முயற்சிக்கவும்; குறைந்த பீக் நேரத்தில் முன்னேற்றம் செய்யவும் |

## குறிப்புகள்

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face மாடல் கண்டறிதல்: https://huggingface.co/models

---

**அமர்வு காலம்**: 30 நிமிடங்கள் (+ விருப்பமான ஆழமான ஆராய்ச்சி)  
**சிரமம்**: நடுத்தர

### விருப்பமான மேம்பாடுகள்

| மேம்பாடு | நன்மை | எப்படி |
|----------|-------|-------|
| ஸ்ட்ரீமிங் முதல்-டோக்கன் தாமதம் | உணரப்பட்ட பதிலளிப்பு அளவீடு | `BENCH_STREAM=1`-ஐப் பயன்படுத்தி மதிப்பீடு இயக்கவும் (`Workshop/samples/session03`-ல் மேம்படுத்தப்பட்ட ஸ்கிரிப்ட்) |
| தீர்மானமிக்க முறை | நிலையான பின்வாங்க ஒப்பீடுகள் | `temperature=0`, நிரந்தர உரையாடல் தொகுப்பு, JSON வெளியீடுகளை பதிப்பு கட்டுப்பாட்டின் கீழ் பதிவு செய்யவும் |
| தரம் அளவுகோல் மதிப்பீடு | தரமான பரிமாணத்தைச் சேர்க்கிறது | `prompts.json`-ஐ பரிந்துரைக்கப்பட்ட அம்சங்களுடன் பராமரிக்கவும்; மதிப்பீடுகளை (1–5) கையேடாக அல்லது இரண்டாம் நிலை மாடல் மூலம் குறிக்கவும் |
| CSV / Markdown ஏற்றுமதி | பகிரக்கூடிய அறிக்கை | `benchmark_report.md`-ஐ அட்டவணை மற்றும் முக்கிய அம்சங்களுடன் எழுத ஸ்கிரிப்டை விரிவாக்கவும் |
| மாடல் திறன் குறிச்சொற்கள் | பின்னர் தானியங்கி வழிமாற்றத்திற்கு உதவுகிறது | `{alias: {capabilities:[], size_mb:..}}` உடன் `models.json`-ஐ பராமரிக்கவும் |
| சேமிப்பு சூடாக்க கட்டம் | குளிர்ந்த தொடக்க பாகுபாட்டை குறைக்கிறது | நேரம் மடக்கி மடக்குவதற்கு முன் ஒரு சூடான சுற்றை இயக்கவும் (ஏற்கனவே செயல்படுத்தப்பட்டுள்ளது) |
| சதவீத துல்லியம் | வலுவான வால் தாமதம் | numpy சதவீதத்தைப் பயன்படுத்தவும் (ஏற்கனவே மறுசீரமைக்கப்பட்ட ஸ்கிரிப்டில் உள்ளது) |
| டோக்கன் செலவு மதிப்பீடு | பொருளாதார ஒப்பீடு | மதிப்பீடு செலவு = (டோக்கன்கள்/வினாடி * கோரிக்கைக்கு சராசரி டோக்கன்கள்) * ஆற்றல் அளவுகோல் |
| தோல்வியுற்ற மாடல்களை தானாகத் தவிர்க்கும் | தொகுதி இயக்கங்களில் நிலைத்தன்மை | ஒவ்வொரு மதிப்பீட்டையும் try/except-ல் மடக்கி நிலை புலத்தை குறிக்கவும் |

#### குறைந்தபட்ச Markdown ஏற்றுமதி துணுக்குகள்

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### தீர்மானமிக்க உரையாடல் தொகுப்பு உதாரணம்

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

நிரந்தர பட்டியலை மாறுபட்ட உரையாடல்களுக்கு பதிலாக மடக்கி, commit-களுக்கு மாறுபட்ட அளவுகோல்களை உருவாக்கவும்.

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.