<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-08T14:16:27+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "hr"
}
-->
# Sesija 3: Open-Source modeli u Foundry Local

## Sažetak

Otkrijte kako integrirati Hugging Face i druge open-source modele u Foundry Local. Naučite strategije odabira, radne procese za doprinos zajednici, metodologiju usporedbe performansi i kako proširiti Foundry prilagođenim registracijama modela. Ova sesija povezuje se s tjednim temama istraživanja "Model Mondays" i osposobljava vas za procjenu i operativno korištenje open-source modela lokalno prije skaliranja na Azure.

## Ciljevi učenja

Na kraju sesije moći ćete:

- **Otkriti i procijeniti**: Identificirati potencijalne modele (mistral, gemma, qwen, deepseek) koristeći kompromis između kvalitete i resursa.
- **Učitati i pokrenuti**: Koristiti Foundry Local CLI za preuzimanje, predmemoriranje i pokretanje modela iz zajednice.
- **Benchmark**: Primijeniti dosljedne heuristike za latenciju, propusnost tokena i kvalitetu.
- **Proširiti**: Registrirati ili prilagoditi prilagođeni model koristeći SDK-kompatibilne obrasce.
- **Usporediti**: Izraditi strukturirane usporedbe za odluke između SLM i srednje velikih LLM modela.

## Preduvjeti

- Završene sesije 1 i 2
- Python okruženje s instaliranim `foundry-local-sdk`
- Najmanje 15GB slobodnog prostora na disku za predmemoriranje više modela
- Opcionalno: Omogućena GPU/WebGPU akceleracija (`foundry config list`)

### Brzi početak za više platformi

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

Prilikom benchmarkinga s macOS-a prema Windows host servisu, postavite:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo tijek (30 min)

### 1. Učitavanje Hugging Face modela putem CLI (8 min)

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


### 2. Pokretanje i brza provjera (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Benchmark skripta (8 min)

Kreirajte `samples/03-oss-models/benchmark_models.py`:

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

Pokrenite:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Usporedba performansi (5 min)

Raspravite o kompromisima: vrijeme učitavanja, memorijski otisak (promatrajte Task Manager / `nvidia-smi` / OS monitor resursa), kvaliteta izlaza u odnosu na brzinu. Koristite Python benchmark skriptu (Sesija 3) za latenciju i propusnost; ponovite nakon omogućavanja GPU akceleracije.

### 5. Početni projekt (4 min)

Izradite generator izvještaja za usporedbu modela (proširite benchmark skriptu s izvozom u markdown).

## Početni projekt: Proširenje `03-huggingface-models`

Poboljšajte postojeći uzorak dodavanjem:

1. Agregacije benchmarka + izlaza u CSV/Markdown.
2. Implementacije jednostavnog kvalitativnog ocjenjivanja (set parova upita + datoteka za ručnu anotaciju).
3. Uvođenja JSON konfiguracije (`models.json`) za prilagodljivi popis modela i set upita.

## Provjera valjanosti

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Svi ciljani modeli trebaju se pojaviti i odgovoriti na zahtjev za probni chat.

## Primjer scenarija i mapiranje radionice

| Skripta radionice | Scenarij | Cilj | Izvor upita / skupa podataka |
|-------------------|----------|------|-----------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Tim za platformu na rubu odabire zadani SLM za ugrađeni sažimač | Izraditi usporedbu latencije + p95 + tokena/sec među kandidatskim modelima | Inline `PROMPT` var + okruženje `BENCH_MODELS` popis |

### Narativ scenarija

Inženjerski tim mora odabrati zadani lagani model za sažimanje za offline značajku bilješki sa sastanka. Provode kontrolirane determinističke benchmarke (temperature=0) na fiksnom setu upita (vidi primjer dolje) i prikupljaju metrike latencije i propusnosti s i bez GPU akceleracije.

### Primjer JSON seta upita (proširiv)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Prođite svaki upit po modelu, zabilježite latenciju po upitu kako biste izveli metrike distribucije i otkrili odstupanja.

## Okvir za odabir modela

| Dimenzija | Metrika | Zašto je važna |
|-----------|---------|----------------|
| Latencija | prosjek / p95 | Dosljednost korisničkog iskustva |
| Propusnost | tokeni/sec | Skalabilnost za batch i streaming |
| Memorija | rezidentna veličina | Prilagodba uređaju i konkurentnost |
| Kvaliteta | rubrika upita | Prikladnost za zadatak |
| Otisak | predmemorija diska | Distribucija i ažuriranja |
| Licenca | dopuštenje za korištenje | Komercijalna usklađenost |

## Proširenje s prilagođenim modelom

Visokorazinski obrazac (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Konzultirajte službeni repozitorij za evolucijske adapter sučelja:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Rješavanje problema

| Problem | Uzrok | Rješenje |
|---------|-------|----------|
| OOM na mistral-7b | Nedovoljno RAM-a/GPU-a | Zaustavite druge modele; pokušajte manju varijantu |
| Spori prvi odgovor | Hladno učitavanje | Održavajte toplim s periodičnim laganim upitom |
| Zastoj preuzimanja | Nestabilnost mreže | Pokušajte ponovno; unaprijed preuzmite tijekom slabog opterećenja |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Trajanje sesije**: 30 min (+ opcionalno detaljno istraživanje)  
**Težina**: Srednje

### Opcionalna poboljšanja

| Poboljšanje | Prednost | Kako |
|-------------|----------|------|
| Latencija prvog tokena u streamingu | Mjeri percipiranu odzivnost | Pokrenite benchmark s `BENCH_STREAM=1` (poboljšana skripta u `Workshop/samples/session03`) |
| Deterministički način rada | Stabilne regresijske usporedbe | `temperature=0`, fiksni set upita, zabilježite JSON izlaze pod kontrolom verzija |
| Ocjenjivanje prema rubrici kvalitete | Dodaje kvalitativnu dimenziju | Održavajte `prompts.json` s očekivanim aspektima; ručno ocjenjujte (1–5) ili putem sekundarnog modela |
| Izvoz u CSV / Markdown | Dijeljivi izvještaj | Proširite skriptu za pisanje `benchmark_report.md` s tablicom i istaknutim dijelovima |
| Oznake sposobnosti modela | Pomaže kasnijem automatiziranom usmjeravanju | Održavajte `models.json` s `{alias: {capabilities:[], size_mb:..}}` |
| Faza zagrijavanja predmemorije | Smanjuje pristranost hladnog starta | Izvršite jedan krug zagrijavanja prije vremenske petlje (već implementirano) |
| Točnost percentila | Robusna latencija repa | Koristite numpy percentil (već u refaktoriranoj skripti) |
| Procjena troška tokena | Ekonomska usporedba | Približni trošak = (tokeni/sec * prosječni tokeni po zahtjevu) * energetska heuristika |
| Automatsko preskakanje neuspjelih modela | Otpornost u batch pokretanjima | Omotajte svaki benchmark u try/except i označite statusno polje |

#### Minimalni isječak za izvoz u Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Primjer determinističkog seta upita

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Prođite statički popis umjesto nasumičnih upita za usporedive metrike kroz commitove.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.