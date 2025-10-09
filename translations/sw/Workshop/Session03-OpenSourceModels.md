<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-09T21:29:41+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "sw"
}
-->
# Kipindi cha 3: Miundo ya Chanzo Huria katika Foundry Local

## Muhtasari

Gundua jinsi ya kuleta miundo ya Hugging Face na mingine ya chanzo huria katika Foundry Local. Jifunze mikakati ya kuchagua, michakato ya kuchangia jamii, mbinu za kulinganisha utendaji, na jinsi ya kupanua Foundry kwa usajili wa miundo maalum. Kipindi hiki kinahusiana na mada za uchunguzi za kila wiki za "Model Mondays" na kinakupa uwezo wa kutathmini na kutumia miundo ya chanzo huria kwa ndani kabla ya kupanua hadi Azure.

## Malengo ya Kujifunza

Mwisho wa kipindi hiki utaweza:

- **Gundua & Tathmini**: Tambua miundo inayofaa (mistral, gemma, qwen, deepseek) kwa kutumia uwiano wa ubora dhidi ya rasilimali.
- **Pakua & Endesha**: Tumia Foundry Local CLI kupakua, kuhifadhi, na kuzindua miundo ya jamii.
- **Linganisho**: Tumia vigezo thabiti vya ucheleweshaji + kasi ya tokeni + ubora.
- **Panua**: Sajili au rekebisha kifungashio cha muundo maalum kufuatia mifumo inayolingana na SDK.
- **Linganisho**: Tengeneza kulinganisha kwa muundo wa SLM dhidi ya LLM za ukubwa wa kati.

## Mahitaji ya Awali

- Vipindi 1 & 2 vimekamilika
- Mazingira ya Python yenye `foundry-local-sdk` imewekwa
- Angalau 15GB ya nafasi ya diski kwa hifadhi ya miundo mingi
- Hiari: Uharakishaji wa GPU/WebGPU umewezeshwa (`foundry config list`)

### Mwanzo wa Haraka wa Mazingira ya Msalaba

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

Wakati wa kulinganisha kutoka macOS dhidi ya huduma ya mwenyeji ya Windows, weka:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Mtiririko wa Demo (Dakika 30)

### 1. Pakua Miundo ya Hugging Face kupitia CLI (Dakika 8)

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

### 2. Endesha & Uchunguzi wa Haraka (Dakika 5)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```

### 3. Script ya Kulinganisha (Dakika 8)

Tengeneza `samples/03-oss-models/benchmark_models.py`:

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

Endesha:

```powershell
python samples/03-oss-models/benchmark_models.py
```

### 4. Linganisho la Utendaji (Dakika 5)

Jadili uwiano: muda wa kupakia, matumizi ya kumbukumbu (angalia Task Manager / `nvidia-smi` / monitor ya rasilimali ya OS), ubora wa matokeo dhidi ya kasi. Tumia script ya Python ya kulinganisha (Kipindi cha 3) kwa ucheleweshaji & kasi ya tokeni; rudia baada ya kuwezesha uharakishaji wa GPU.

### 5. Mradi wa Kuanza (Dakika 4)

Tengeneza jenereta ya ripoti ya kulinganisha miundo (panua script ya kulinganisha na usafirishaji wa markdown).

## Mradi wa Kuanza: Panua `03-huggingface-models`

Boresha sampuli iliyopo kwa:

1. Kuongeza mkusanyiko wa kulinganisha + usafirishaji wa CSV/Markdown.
2. Kutekeleza upimaji rahisi wa ubora (seti ya maelezo ya majaribio + faili ya maelezo ya mwongozo).
3. Kuanzisha usanidi wa JSON (`models.json`) kwa orodha ya miundo inayoweza kuunganishwa & seti ya maelezo.

## Orodha ya Uhakiki

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Miundo yote inayolengwa inapaswa kuonekana na kujibu ombi la mazungumzo ya uchunguzi.

## Mfano wa Hali & Ulinganisho wa Warsha

| Script ya Warsha | Hali | Lengo | Chanzo cha Maelezo / Dataset |
|------------------|------|-------|-----------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Timu ya jukwaa la Edge inayochagua SLM chaguo-msingi kwa muhtasari wa kujengwa | Tengeneza kulinganisha kwa ucheleweshaji + p95 + tokeni/sec kati ya miundo inayolengwa | Inline `PROMPT` var + mazingira `BENCH_MODELS` list |

### Simulizi ya Hali
Uhandisi wa bidhaa lazima uchague muundo mwepesi wa muhtasari wa chaguo-msingi kwa kipengele cha noti za mkutano nje ya mtandao. Wanakimbia kulinganisha thabiti ya majaribio (temperature=0) katika seti ya maelezo ya kudumu (tazama mfano hapa chini) na kukusanya vigezo vya ucheleweshaji + kasi ya tokeni na bila uharakishaji wa GPU.

### Mfano wa Seti ya Maelezo ya JSON (inaweza kupanuliwa)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Rudia kila maelezo kwa kila muundo, rekodi ucheleweshaji kwa kila maelezo ili kupata vigezo vya usambazaji na kugundua matukio ya nje.

## Mfumo wa Uchaguzi wa Muundo

| Kipengele | Kipimo | Kwa Nini Kina Muhimu |
|-----------|--------|---------------------|
| Ucheleweshaji | wastani / p95 | Uthabiti wa uzoefu wa mtumiaji |
| Kasi | tokeni/sec | Uwezo wa kundi & utiririshaji |
| Kumbukumbu | ukubwa wa makazi | Uwezo wa kifaa & ushirikiano |
| Ubora | maelezo ya rubriki | Ustahiki wa kazi |
| Alama ya Kumbukumbu | hifadhi ya diski | Usambazaji & masasisho |
| Leseni | ruhusa ya matumizi | Uzingatiaji wa kibiashara |

## Kupanua Kwa Muundo Maalum

Mfumo wa kiwango cha juu (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Tazama repo rasmi kwa miingiliano ya adapta inayobadilika:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Utatuzi wa Matatizo

| Tatizo | Sababu | Suluhisho |
|--------|--------|----------|
| OOM kwenye mistral-7b | RAM/GPU haitoshi | Zima miundo mingine; jaribu toleo dogo |
| Jibu la kwanza polepole | Kupakia baridi | Weka joto kwa maelezo mepesi ya mara kwa mara |
| Kupakua kunakwama | Kutokuwa thabiti kwa mtandao | Jaribu tena; pakua mapema wakati wa saa za chini |

## Marejeleo

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Ugunduzi wa Miundo ya Hugging Face: https://huggingface.co/models

---

**Muda wa Kipindi**: Dakika 30 (+ uchunguzi wa kina wa hiari)  
**Ugumu**: Kati

### Uboreshaji wa Hiari

| Uboreshaji | Faida | Jinsi |
|------------|-------|------|
| Ucheleweshaji wa Tokeni ya Kwanza ya Utiririshaji | Inapima mwitikio unaoonekana | Endesha kulinganisha na `BENCH_STREAM=1` (script iliyoboreshwa katika `Workshop/samples/session03`) |
| Hali ya Kiamua | Kulinganisha thabiti ya regression | `temperature=0`, seti ya maelezo ya kudumu, rekodi matokeo ya JSON chini ya udhibiti wa toleo |
| Upimaji wa Rubriki ya Ubora | Ongeza kipimo cha ubora | Hifadhi `prompts.json` na vipengele vinavyotarajiwa; weka alama (1–5) kwa mwongozo au kupitia muundo wa pili |
| Usafirishaji wa CSV / Markdown | Ripoti inayoweza kushirikiwa | Panua script kuandika `benchmark_report.md` na jedwali & vivutio |
| Alama za Uwezo wa Muundo | Husaidia uelekezaji wa kiotomatiki baadaye | Hifadhi `models.json` na `{alias: {capabilities:[], size_mb:..}}` |
| Awamu ya Kupasha Joto Kumbukumbu | Punguza upendeleo wa kuanza baridi | Tekeleza mzunguko mmoja wa joto kabla ya mzunguko wa muda (tayari imetekelezwa) |
| Usahihi wa Asilimia | Ucheleweshaji thabiti wa mkia | Tumia asilimia ya numpy (tayari katika script iliyorekebishwa) |
| Makadirio ya Gharama ya Tokeni | Kulinganisha kiuchumi | Gharama ya makadirio = (tokeni/sec * wastani wa tokeni kwa ombi) * hesabu ya nishati |
| Kuruka Kiotomatiki Miundo Iliyoshindwa | Ustahimilivu katika mizunguko ya kundi | Funga kila kulinganisha katika try/except na weka uwanja wa hali |

#### Kipande Kidogo cha Usafirishaji wa Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### Mfano wa Seti ya Maelezo ya Kiamua

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Rudia orodha tuli badala ya maelezo ya nasibu kwa vigezo vinavyoweza kulinganishwa katika mabadiliko.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.