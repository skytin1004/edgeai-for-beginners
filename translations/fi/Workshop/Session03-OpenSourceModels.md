<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d6ad6c8b4a0e3ecef3afb86a6f578e1c",
  "translation_date": "2025-10-09T14:39:05+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "fi"
}
-->
# Istunto 3: Avoimen lähdekoodin mallit Foundry Localissa

## Tiivistelmä

Tutustu siihen, miten Hugging Face ja muut avoimen lähdekoodin mallit tuodaan Foundry Localiin. Opit valintastrategioita, yhteisön kontribuutiotyönkulkuja, suorituskyvyn vertailumenetelmiä ja tapoja laajentaa Foundrya mukautetuilla mallirekisteröinneillä. Tämä istunto liittyy viikoittaisiin "Model Mondays" -tutkimusteemoihin ja antaa valmiudet arvioida ja ottaa käyttöön avoimen lähdekoodin malleja paikallisesti ennen laajentamista Azureen.

## Oppimistavoitteet

Istunnon lopussa osaat:

- **Löytää ja arvioida**: Tunnistaa ehdokasmalleja (mistral, gemma, qwen, deepseek) laadun ja resurssien välisen tasapainon perusteella.
- **Ladata ja suorittaa**: Käyttää Foundry Local CLI:tä yhteisön mallien lataamiseen, välimuistiin tallentamiseen ja käynnistämiseen.
- **Vertailuarvioida**: Soveltaa johdonmukaisia viive-, token-läpäisy- ja laatuheuristiikkoja.
- **Laajentaa**: Rekisteröidä tai mukauttaa oma mallikääre SDK-yhteensopivien mallien mukaisesti.
- **Verrata**: Tuottaa rakenteellisia vertailuja SLM:n ja keskikokoisten LLM-mallien valintapäätösten tueksi.

## Esitietovaatimukset

- Istunnot 1 ja 2 suoritettu
- Python-ympäristö, jossa `foundry-local-sdk` asennettuna
- Vähintään 15GB vapaata levytilaa useiden mallivälimuistien tallentamiseen
- Valinnainen: GPU/WebGPU-kiihdytys käytössä (`foundry config list`)

### Nopea aloitus monialustaympäristössä

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

Kun suoritat vertailuarviointia macOS:stä Windows-isäntäpalveluun, aseta:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Flow (30 min)

### 1. Lataa Hugging Face -mallit CLI:n kautta (8 min)

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


### 2. Suorita ja tee nopea tarkistus (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Vertailuarviointiskripti (8 min)

Luo `samples/03-oss-models/benchmark_models.py`:

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

Suorita:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Vertaa suorituskykyä (5 min)

Keskustele kompromisseista: latausaika, muistinkäyttö (seuraa Task Manageria / `nvidia-smi` / käyttöjärjestelmän resurssimonitoria), tulosten laatu vs nopeus. Käytä Python-vertailuarviointiskriptiä (istunto 3) viiveen ja läpäisyn mittaamiseen; toista GPU-kiihdytyksen ollessa käytössä.

### 5. Aloitusprojekti (4 min)

Luo mallivertailuraporttigeneraattori (laajenna vertailuarviointiskriptiä markdown-viennillä).

## Aloitusprojekti: Laajenna `03-huggingface-models`

Paranna olemassa olevaa esimerkkiä seuraavasti:

1. Lisää vertailuarvioinnin aggregointi + CSV/Markdown-vienti.
2. Toteuta yksinkertainen laadullinen pisteytys (kehotepareja + manuaalinen annotointitiedosto).
3. Ota käyttöön JSON-konfiguraatio (`models.json`) mallilistan ja kehotesarjan liittämiseksi.

## Vahvistuslista

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Kaikkien kohdemallien tulisi näkyä ja vastata kokeilukeskustelupyyntöön.

## Esimerkkitilanne ja työpajan kartoitus

| Työpajaskripti | Tilanne | Tavoite | Kehote / datasetin lähde |
|-----------------|----------|------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Reuna-alustatiimi valitsee oletus-SLM:n upotetulle tiivistämistoiminnolle | Tuota viive + p95 + tokenit/sek vertailu ehdokasmallien välillä | Inline `PROMPT` var + ympäristö `BENCH_MODELS` lista |

### Tilannekuvaus

Tuotetekniikkatiimin täytyy valita oletuskevyt tiivistämismalli offline-kokousmuistiinpanojen ominaisuutta varten. He suorittavat kontrolloituja deterministisiä vertailuarviointeja (temperature=0) kiinteän kehotesarjan avulla (katso esimerkki alla) ja keräävät viive- ja läpäisymittareita GPU-kiihdytyksen ollessa käytössä ja ilman sitä.

### Esimerkkikehotesarja JSON (laajennettavissa)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Käy läpi jokainen kehote per malli, tallenna kehotekohtainen viive jakaumamittareiden johdannaiseksi ja poikkeamien havaitsemiseksi.

## Mallin valintakehys

| Ulottuvuus | Mittari | Miksi tärkeää |
|----------|--------|----------------|
| Viive | keskiarvo / p95 | Käyttäjäkokemuksen johdonmukaisuus |
| Läpäisy | tokenit/sek | Erä- ja suoratoistettavuus |
| Muisti | käytössä oleva koko | Laitteeseen sopivuus ja samanaikaisuus |
| Laatu | arviointikehotteet | Tehtävän soveltuvuus |
| Jälki | levyvälimuisti | Jakelu ja päivitykset |
| Lisenssi | käyttöoikeus | Kaupallinen yhteensopivuus |

## Laajentaminen mukautetulla mallilla

Korkean tason malli (pseudokoodi):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Katso virallinen repo kehittyvien adapteriliittymien osalta:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Vianmääritys

| Ongelma | Syy | Korjaus |
|-------|-------|-----|
| OOM mistral-7b:ssä | Riittämätön RAM/GPU | Lopeta muut mallit; kokeile pienempää varianttia |
| Hidas ensimmäinen vastaus | Kylmä lataus | Pidä lämpimänä kevyellä kehotteella säännöllisesti |
| Lataus pysähtyy | Verkkoyhteyden epävakaus | Yritä uudelleen; esilataa hiljaisina aikoina |

## Viitteet

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Istunnon kesto**: 30 min (+ valinnainen syventävä osuus)  
**Vaikeustaso**: Keskitaso

### Valinnaiset parannukset

| Parannus | Hyöty | Miten |
|-------------|---------|-----|
| Suoratoiston ensimmäisen tokenin viive | Mittaa koettua reagointinopeutta | Suorita vertailuarviointi `BENCH_STREAM=1` (parannettu skripti `Workshop/samples/session03`) |
| Deterministinen tila | Vakaa regressiovertailu | `temperature=0`, kiinteä kehotesarja, tallenna JSON-tulokset versionhallintaan |
| Laadullinen arviointipisteytys | Lisää laadullinen ulottuvuus | Ylläpidä `prompts.json` odotettujen ominaisuuksien kanssa; pisteytä (1–5) manuaalisesti tai toissijaisen mallin avulla |
| CSV / Markdown-vienti | Jaettava raportti | Laajenna skripti kirjoittamaan `benchmark_report.md` taulukon ja kohokohtien kanssa |
| Mallin ominaisuustunnisteet | Auttaa automatisoidussa reitityksessä myöhemmin | Ylläpidä `models.json` muodossa `{alias: {capabilities:[], size_mb:..}}` |
| Välimuistin esilämmitys | Vähentää kylmäkäynnistysvinoumaa | Suorita yksi lämmittelykierros ennen ajoitusjaksoa (jo toteutettu) |
| Prosenttipisteen tarkkuus | Vahva viiveen häntä | Käytä numpy-prosenttipistettä (jo refaktoroidussa skriptissä) |
| Token-kustannusarvio | Taloudellinen vertailu | Arvioitu kustannus = (tokenit/sek * keskimääräinen tokenien määrä per pyyntö) * energiakustannusheuristiikka |
| Epäonnistuneiden mallien automaattinen ohitus | Kestävyys eräajoissa | Kääri jokainen vertailuarviointi try/except-lohkoon ja merkitse tilakenttä |

#### Minimal Markdown Export Snippet

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Deterministinen kehotesarjaesimerkki

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Käytä staattista listaa satunnaisten kehotteiden sijaan vertailukelpoisten mittareiden saamiseksi eri commitien välillä.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.