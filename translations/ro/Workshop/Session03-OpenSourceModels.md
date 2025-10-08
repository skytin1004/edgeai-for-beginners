<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-08T15:25:06+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "ro"
}
-->
# Sesiunea 3: Modele Open-Source în Foundry Local

## Rezumat

Descoperă cum să integrezi modelele Hugging Face și alte modele open-source în Foundry Local. Învață strategii de selecție, fluxuri de contribuție comunitară, metodologii de comparare a performanței și cum să extinzi Foundry cu înregistrări personalizate de modele. Această sesiune se aliniază temelor săptămânale de explorare "Model Mondays" și te pregătește să evaluezi și să operationalizezi modelele open-source local înainte de a le scala pe Azure.

## Obiective de Învățare

La final vei putea:

- **Descoperi & Evalua**: Identifica modele candidate (mistral, gemma, qwen, deepseek) utilizând compromisuri între calitate și resurse.
- **Încărca & Rula**: Folosi CLI-ul Foundry Local pentru a descărca, cache-ui și lansa modele comunitare.
- **Benchmark**: Aplica euristici consistente pentru latență + debit de tokeni + calitate.
- **Extinde**: Înregistra sau adapta un wrapper de model personalizat conform modelelor compatibile SDK.
- **Compara**: Produce comparații structurate pentru decizii de selecție între SLM și LLM de dimensiuni medii.

## Cerințe Prealabile

- Finalizarea sesiunilor 1 și 2
- Mediu Python cu `foundry-local-sdk` instalat
- Cel puțin 15GB spațiu liber pe disc pentru cache-uri multiple de modele
- Opțional: Accelerație GPU/WebGPU activată (`foundry config list`)

### Ghid Rapid pentru Mediu Cross-Platform

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

Când faci benchmark de pe macOS către un serviciu gazdă Windows, setează:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Flux Demo (30 min)

### 1. Încărcare Modele Hugging Face prin CLI (8 min)

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


### 2. Rulare & Testare Rapidă (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Script de Benchmark (8 min)

Creează `samples/03-oss-models/benchmark_models.py`:

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

Rulează:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Comparare Performanță (5 min)

Discută compromisurile: timpul de încărcare, amprenta de memorie (observă Task Manager / `nvidia-smi` / monitorul de resurse al OS-ului), calitatea output-ului vs viteza. Folosește scriptul de benchmark Python (Sesiunea 3) pentru latență & debit; repetă după activarea accelerației GPU.

### 5. Proiect de Start (4 min)

Creează un generator de rapoarte de comparație a modelelor (extinde scriptul de benchmark cu export în markdown).

## Proiect de Start: Extinde `03-huggingface-models`

Îmbunătățește exemplul existent prin:

1. Adăugarea agregării benchmark + output CSV/Markdown.
2. Implementarea unui scor calitativ simplu (set de perechi de prompturi + fișier stub de adnotare manuală).
3. Introducerea unui config JSON (`models.json`) pentru lista de modele pluggable & setul de prompturi.

## Checklist de Validare

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Toate modelele țintă ar trebui să apară și să răspundă la o cerere de chat de test.

## Scenariu Exemplu & Mapare Workshop

| Script Workshop | Scenariu | Obiectiv | Sursă Prompt / Dataset |
|-----------------|----------|----------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Echipa platformei edge selectând SLM-ul implicit pentru un sumarizator integrat | Produce comparații de latență + p95 + tokeni/sec între modelele candidate | Variabila `PROMPT` inline + lista `BENCH_MODELS` din mediu |

### Narațiunea Scenariului

Echipa de inginerie a produsului trebuie să aleagă un model de sumarizare ușor pentru o funcție offline de notițe de întâlnire. Ei rulează benchmark-uri deterministe controlate (temperature=0) pe un set fix de prompturi (vezi exemplul de mai jos) și colectează metrici de latență + debit cu și fără accelerație GPU.

### Exemplu Set de Prompturi JSON (expandabil)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Rulează fiecare prompt pentru fiecare model, capturează latența per-prompt pentru a deriva metrici de distribuție și a detecta valori aberante.

## Cadru de Selecție a Modelului

| Dimensiune | Metrică | De ce contează |
|------------|---------|----------------|
| Latență | medie / p95 | Consistența experienței utilizatorului |
| Debit | tokeni/sec | Scalabilitate batch & streaming |
| Memorie | dimensiune rezidentă | Compatibilitate cu dispozitivul & concurență |
| Calitate | rubrică prompturi | Potrivire pentru sarcină |
| Amprentă | cache pe disc | Distribuție & actualizări |
| Licență | permisiuni de utilizare | Conformitate comercială |

## Extinderea cu Model Personalizat

Model general (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Consultă repo-ul oficial pentru interfețe de adaptor în evoluție:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Depanare

| Problemă | Cauză | Soluție |
|----------|-------|---------|
| OOM pe mistral-7b | RAM/GPU insuficient | Oprește alte modele; încearcă o variantă mai mică |
| Răspuns lent la prima cerere | Încărcare la rece | Menține activ cu un prompt ușor periodic |
| Descărcare blocată | Instabilitate rețea | Reîncearcă; prefetch în perioade de vârf redus |

## Referințe

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Descoperire Modele Hugging Face: https://huggingface.co/models

---

**Durata Sesiunii**: 30 min (+ aprofundare opțională)  
**Dificultate**: Intermediar

### Îmbunătățiri Opționale

| Îmbunătățire | Beneficiu | Cum |
|--------------|-----------|-----|
| Latență Primul Token Streaming | Măsoară receptivitatea percepută | Rulează benchmark cu `BENCH_STREAM=1` (script îmbunătățit în `Workshop/samples/session03`) |
| Mod Determinist | Comparații stabile de regresie | `temperature=0`, set fix de prompturi, capturează output-uri JSON sub controlul versiunii |
| Scorare Rubrică Calitate | Adaugă o dimensiune calitativă | Menține `prompts.json` cu fațete așteptate; adnotează scoruri (1–5) manual sau printr-un model secundar |
| Export CSV / Markdown | Raport partajabil | Extinde scriptul pentru a scrie `benchmark_report.md` cu tabel & evidențieri |
| Etichete Capacitate Model | Ajută la rutare automată ulterioară | Menține `models.json` cu `{alias: {capabilities:[], size_mb:..}}` |
| Fază de Încălzire Cache | Reduce bias-ul de start la rece | Execută o rundă de încălzire înainte de bucla de timing (deja implementată) |
| Precizie Percentilă | Latență robustă în coadă | Folosește percentila numpy (deja în scriptul refactorizat) |
| Aproximare Cost Token | Comparație economică | Cost aproximativ = (tokeni/sec * medie tokeni per cerere) * euristică energie |
| Sărire Automată Modele Eșuate | Reziliență în rulări batch | Învelește fiecare benchmark în try/except și marchează câmpul de status |

#### Fragment Minimal Export Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Exemplu Set Prompturi Determinist

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Rulează lista statică în loc de prompturi aleatorii pentru metrici comparabile între commit-uri.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.