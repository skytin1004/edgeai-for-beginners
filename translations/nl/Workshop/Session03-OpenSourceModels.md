<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-09T16:52:18+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "nl"
}
-->
# Sessie 3: Open-Source Modellen in Foundry Local

## Samenvatting

Ontdek hoe je Hugging Face en andere open-source modellen kunt integreren in Foundry Local. Leer strategieën voor modelselectie, workflows voor bijdragen aan de community, methodologie voor prestatievergelijking en hoe je Foundry kunt uitbreiden met aangepaste modelregistraties. Deze sessie sluit aan bij de wekelijkse "Model Mondays"-verkenningsthema's en stelt je in staat om open-source modellen lokaal te evalueren en operationeel te maken voordat je opschaalt naar Azure.

## Leerdoelen

Aan het einde kun je:

- **Ontdekken & Evalueren**: Kandidatenmodellen identificeren (mistral, gemma, qwen, deepseek) op basis van kwaliteit versus resource-afwegingen.
- **Laden & Uitvoeren**: Foundry Local CLI gebruiken om communitymodellen te downloaden, te cachen en te starten.
- **Benchmarken**: Consistente heuristieken toepassen voor latency, token-doorvoer en kwaliteit.
- **Uitbreiden**: Een aangepaste modelwrapper registreren of aanpassen volgens SDK-compatibele patronen.
- **Vergelijken**: Gestructureerde vergelijkingen maken voor SLM versus middelgrote LLM-selectiebeslissingen.

## Vereisten

- Sessies 1 & 2 voltooid
- Python-omgeving met `foundry-local-sdk` geïnstalleerd
- Minimaal 15GB vrije schijfruimte voor meerdere modelcaches
- Optioneel: GPU/WebGPU-versnelling ingeschakeld (`foundry config list`)

### Snelstart voor Cross-Platform Omgeving

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

Bij benchmarken vanaf macOS tegen een Windows-hostservice, stel in:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (30 min)

### 1. Hugging Face Modellen Laden via CLI (8 min)

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


### 2. Uitvoeren & Snelle Controle (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Benchmarkscript (8 min)

Maak `samples/03-oss-models/benchmark_models.py`:

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

Uitvoeren:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Prestatie Vergelijken (5 min)

Bespreek afwegingen: laadtijd, geheugengebruik (observeer Taakbeheer / `nvidia-smi` / OS-resource monitor), outputkwaliteit versus snelheid. Gebruik het Python-benchmarkscript (Sessie 3) voor latency & doorvoer; herhaal na het inschakelen van GPU-versnelling.

### 5. Starterproject (4 min)

Maak een generator voor modelvergelijkingsrapporten (breid benchmarkscript uit met markdown-export).

## Starterproject: Uitbreiden `03-huggingface-models`

Verbeter het bestaande voorbeeld door:

1. Benchmarkaggregatie + CSV/Markdown-output toe te voegen.
2. Eenvoudige kwalitatieve scoring te implementeren (promptpaarset + handmatige annotatiebestand).
3. Een JSON-configuratie (`models.json`) te introduceren voor een instelbare modellenlijst & promptset.

## Validatiechecklist

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Alle doelmodellen moeten verschijnen en reageren op een chatverzoek.

## Voorbeeldscenario & Workshopmapping

| Workshopscript | Scenario | Doel | Prompt / Datasetbron |
|-----------------|----------|------|-----------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Edge-platformteam selecteert standaard SLM voor ingebouwde samenvatter | Latency + p95 + tokens/sec vergelijking produceren tussen kandidatenmodellen | Inline `PROMPT` var + omgeving `BENCH_MODELS` lijst |

### Scenarioverhaal

Productengineering moet een standaard lichtgewicht samenvattingsmodel kiezen voor een offline notulenfunctie. Ze voeren gecontroleerde deterministische benchmarks uit (temperature=0) over een vaste promptset (zie voorbeeld hieronder) en verzamelen latency- en doorvoermetingen met en zonder GPU-versnelling.

### Voorbeeld Promptset JSON (uitbreidbaar)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Loop elke prompt per model, leg latency per prompt vast om distributiemetingen af te leiden en uitschieters te detecteren.

## Modelselectiekader

| Dimensie | Metriek | Waarom Het Belangrijk Is |
|----------|--------|--------------------------|
| Latency | gemiddeld / p95 | Consistentie van gebruikerservaring |
| Doorvoer | tokens/sec | Batch- & streaming-schaalbaarheid |
| Geheugen | resident grootte | Geschiktheid voor apparaat & gelijktijdigheid |
| Kwaliteit | rubric prompts | Taakgeschiktheid |
| Voetafdruk | schijfcache | Distributie & updates |
| Licentie | gebruiksvoorwaarden | Commerciële naleving |

## Uitbreiden Met Aangepast Model

Hoog-niveau patroon (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Raadpleeg de officiële repo voor evoluerende adapterinterfaces:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Probleemoplossing

| Probleem | Oorzaak | Oplossing |
|----------|--------|----------|
| OOM op mistral-7b | Onvoldoende RAM/GPU | Stop andere modellen; probeer kleinere variant |
| Trage eerste reactie | Koude start | Houd warm met een periodieke lichte prompt |
| Download blijft hangen | Netwerkinstabiliteit | Opnieuw proberen; vooraf ophalen tijdens daluren |

## Referenties

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Sessieduur**: 30 min (+ optionele verdieping)  
**Moeilijkheidsgraad**: Gemiddeld

### Optionele Verbeteringen

| Verbetering | Voordeel | Hoe |
|-------------|----------|-----|
| Streaming Eerste-Token Latency | Meet waargenomen responsiviteit | Voer benchmark uit met `BENCH_STREAM=1` (uitgebreid script in `Workshop/samples/session03`) |
| Deterministische Modus | Stabiele regressievergelijkingen | `temperature=0`, vaste promptset, JSON-uitvoer vastleggen onder versiebeheer |
| Kwaliteitsrubriek Scoring | Voegt kwalitatieve dimensie toe | Beheer `prompts.json` met verwachte facetten; scores (1–5) handmatig annoteren of via secundair model |
| CSV / Markdown Export | Deelbaar rapport | Breid script uit om `benchmark_report.md` te schrijven met tabel & highlights |
| Modelcapaciteitstags | Helpt bij geautomatiseerde routering later | Beheer `models.json` met `{alias: {capabilities:[], size_mb:..}}` |
| Cache-opwarmfase | Vermindert koude-startbias | Voer één warme ronde uit vóór de timingloop (al geïmplementeerd) |
| Percentiele Nauwkeurigheid | Robuuste tail latency | Gebruik numpy percentiel (al in refactored script) |
| Tokenkostenbenadering | Economische vergelijking | Geschatte kosten = (tokens/sec * gemiddelde tokens per verzoek) * energieheuristiek |
| Automatisch Overslaan van Mislukte Modellen | Veerkracht in batchruns | Omwikkel elke benchmark met try/except en markeer statusveld |

#### Minimale Markdown Export Snippet

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Voorbeeld Deterministische Promptset

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Loop de statische lijst in plaats van willekeurige prompts voor vergelijkbare metingen over commits.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.