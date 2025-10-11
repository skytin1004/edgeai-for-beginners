<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-11T11:57:58+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "et"
}
-->
# Sessioon 3: Avatud lähtekoodiga mudelid Foundry Localis

## Kokkuvõte

Õpi, kuidas tuua Hugging Face'i ja teisi avatud lähtekoodiga mudeleid Foundry Locali. Tutvu mudelite valikustrateegiate, kogukonna panustamise töövoogude, jõudluse võrdlusmeetodite ja Foundry laiendamise võimalustega kohandatud mudeliregistratsioonide abil. See sessioon järgib iganädalasi "Model Mondays" uurimisteemasid ja annab oskused avatud lähtekoodiga mudelite hindamiseks ja rakendamiseks lokaalselt enne Azure'i skaleerimist.

## Õpieesmärgid

Sessiooni lõpuks oskad:

- **Avastada ja hinnata**: Tuvastada kandidaatmudeleid (mistral, gemma, qwen, deepseek), arvestades kvaliteedi ja ressursside kompromisse.
- **Laadida ja käivitada**: Kasutada Foundry Local CLI-d kogukonna mudelite allalaadimiseks, vahemällu salvestamiseks ja käivitamiseks.
- **Võrdlusuuringud**: Rakendada järjepidevaid latentsuse, tokenite läbilaskevõime ja kvaliteedi heuristikuid.
- **Laiendada**: Registreerida või kohandada SDK-ga ühilduvat mudeli wrapperit.
- **Võrrelda**: Luua struktureeritud võrdlusi SLM-i ja keskmise suurusega LLM-i valikute jaoks.

## Eeltingimused

- Sessioonid 1 ja 2 läbitud
- Python keskkond koos `foundry-local-sdk` paigaldatud
- Vähemalt 15GB vaba kettaruumi mitme mudeli vahemälu jaoks
- Valikuline: GPU/WebGPU kiirendus lubatud (`foundry config list`)

### Kiire alustamine mitme platvormi keskkonnas

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

Kui benchmarkid macOS-ist Windowsi hostiteenuse vastu, seadista:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo voog (30 min)

### 1. Hugging Face'i mudelite laadimine CLI kaudu (8 min)

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

### 2. Käivitamine ja kiire testimine (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```

### 3. Võrdlusuuringu skript (8 min)

Loo `samples/03-oss-models/benchmark_models.py`:

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

Käivita:

```powershell
python samples/03-oss-models/benchmark_models.py
```

### 4. Jõudluse võrdlemine (5 min)

Arutle kompromisside üle: laadimisaeg, mälukasutus (vaata Task Manager / `nvidia-smi` / OS-i ressursimonitor), väljundi kvaliteet vs kiirus. Kasuta Python võrdlusuuringu skripti (Sessioon 3) latentsuse ja läbilaskevõime mõõtmiseks; korda pärast GPU kiirenduse lubamist.

### 5. Algprojekt (4 min)

Loo mudelite võrdlusaruande generaator (laienda võrdlusuuringu skripti markdowni eksportimisega).

## Algprojekt: Laienda `03-huggingface-models`

Täienda olemasolevat näidist järgmiselt:

1. Lisa võrdlusuuringu koondamine + CSV/Markdown väljund.
2. Rakenda lihtne kvalitatiivne hindamine (küsimuste paaride komplekt + käsitsi annotatsiooni stub-fail).
3. Lisa JSON-konfiguratsioon (`models.json`) mudelite nimekirja ja küsimuste komplekti jaoks.

## Kontroll-loend valideerimiseks

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Kõik sihtmudelid peaksid ilmuma ja vastama testvestluse päringule.

## Näidistsenaarium ja töötoa kaardistamine

| Töötoa skript | Stsenaarium | Eesmärk | Küsimuste/Dataseti allikas |
|---------------|------------|---------|---------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Servaplatvormi meeskond valib vaikimisi SLM-i sisseehitatud kokkuvõtja jaoks | Toota latentsuse + p95 + tokenite/sekundis võrdlus kandidaatmudeleid | Inline `PROMPT` var + keskkonna `BENCH_MODELS` nimekiri |

### Stsenaariumi narratiiv
Tootearendus peab valima vaikimisi kerge kokkuvõtva mudeli offline koosolekumärkmete funktsiooni jaoks. Nad viivad läbi kontrollitud deterministlikud võrdlusuuringud (temperature=0) fikseeritud küsimuste komplekti alusel (vt näidet allpool) ja koguvad latentsuse + läbilaskevõime mõõdikuid koos ja ilma GPU kiirenduseta.

### Näide küsimuste komplekti JSON (laiendatav)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Loopi iga küsimus mudeli kohta, jäädvusta iga küsimuse latentsus, et tuletada jaotusmõõdikud ja tuvastada kõrvalekalded.

## Mudeli valiku raamistik

| Dimensioon | Mõõdik | Miks see oluline on |
|------------|--------|---------------------|
| Latentsus | keskmine / p95 | Kasutajakogemuse järjepidevus |
| Läbilaskevõime | tokenid/sekundis | Partii- ja voogedastuse skaleeritavus |
| Mälu | residentne suurus | Seadme sobivus ja samaaegsus |
| Kvaliteet | rubriigi küsimused | Ülesande sobivus |
| Jalajälg | kettavahemälu | Jaotamine ja uuendused |
| Litsents | kasutusõigused | Kaubanduslik vastavus |

## Kohandatud mudeli lisamine

Kõrgetasemeline muster (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Vaata ametlikku repo, et tutvuda arenevate adapteriliidestega:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Tõrkeotsing

| Probleem | Põhjus | Lahendus |
|----------|--------|---------|
| OOM mistral-7b puhul | Ebapiisav RAM/GPU | Peata teised mudelid; proovi väiksemat varianti |
| Aeglane esimene vastus | Külm laadimine | Hoia soojana perioodilise kerge küsimusega |
| Allalaadimine takerdub | Võrgu ebastabiilsus | Proovi uuesti; eel-laadi vaikse ajal |

## Viited

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face mudelite avastamine: https://huggingface.co/models

---

**Sessiooni kestus**: 30 min (+ valikuline süvitsiminek)  
**Raskusaste**: Keskmine

### Valikulised täiustused

| Täiustus | Kasu | Kuidas |
|----------|------|-------|
| Esimese tokeni latentsus voogesituses | Mõõdab tajutavat reageerimiskiirust | Käivita benchmark `BENCH_STREAM=1` (täiustatud skript `Workshop/samples/session03`) |
| Deterministlik režiim | Stabiilsed regressioonivõrdlused | `temperature=0`, fikseeritud küsimuste komplekt, jäädvusta JSON väljundid versioonikontrolli all |
| Kvaliteedi rubriigi hindamine | Lisab kvalitatiivse mõõtme | Halda `prompts.json` eeldatavate aspektidega; hinda skoorid (1–5) käsitsi või teise mudeli abil |
| CSV / Markdown eksport | Jagatav aruanne | Laienda skripti, et kirjutada `benchmark_report.md` tabeli ja esiletõstetega |
| Mudeli võimekuse sildid | Aitab hiljem automatiseeritud suunamist | Halda `models.json` koos `{alias: {capabilities:[], size_mb:..}}` |
| Vahemälu soojendusfaas | Vähendab külmkäivituse kallutatust | Käivita üks soojendusring enne ajastamise tsüklit (juba rakendatud) |
| Protsentuaalne täpsus | Tugev latentsuse saba | Kasuta numpy protsentiili (juba refaktooritud skriptis) |
| Tokenite kulu ligikaudne arvutus | Majanduslik võrdlus | Ligikaudne kulu = (tokenid/sekundis * keskmine tokenite arv päringu kohta) * energia heuristik |
| Ebaõnnestunud mudelite automaatne vahelejätmine | Vastupidavus partii käitustes | Mähi iga benchmark try/except sisse ja märgi olekuväli |

#### Minimaalne Markdowni eksportimise snippet

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### Deterministliku küsimuste komplekti näide

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Loopi staatilist nimekirja juhuslike küsimuste asemel, et saada võrreldavaid mõõdikuid üle commitide.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.