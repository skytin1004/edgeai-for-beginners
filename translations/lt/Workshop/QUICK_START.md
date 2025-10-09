<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-09T21:07:34+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "lt"
}
-->
# Greito starto vadovas dirbtuvėms

## Reikalavimai

### 1. Įdiekite Foundry Local

Sekite oficialų diegimo vadovą:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Įdiekite Python priklausomybes

Iš dirbtuvių katalogo:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Dirbtuvių pavyzdžių paleidimas

### Sesija 01: Pagrindinis pokalbis

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**Aplinkos kintamieji:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sesija 02: RAG procesas

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**Aplinkos kintamieji:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sesija 02: RAG vertinimas (Ragas)

```bash
python rag_eval_ragas.py
```

**Pastaba**: Reikalingos papildomos priklausomybės, įdiegiamos per `requirements.txt`

### Sesija 03: Veikimo testavimas

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**Aplinkos kintamieji:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Rezultatas**: JSON su vėlavimo, pralaidumo ir pirmojo ženklo metrikomis

### Sesija 04: Modelių palyginimas

```bash
cd Workshop/samples/session04
python model_compare.py
```

**Aplinkos kintamieji:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sesija 05: Daugiaveiksmė orkestracija

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**Aplinkos kintamieji:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sesija 06: Modelių maršrutizatorius

```bash
cd Workshop/samples/session06
python models_router.py
```

**Testuoja maršrutizavimo logiką** su keliais ketinimais (kodas, santrauka, klasifikacija)

### Sesija 06: Procesas

```bash
python models_pipeline.py
```

**Sudėtingas daugiapakopis procesas** su planavimu, vykdymu ir tobulinimu

## Skriptai

### Eksportuoti veikimo ataskaitą

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Rezultatas**: Markdown lentelė + JSON metrikos

### Markdown CLI šablonų tikrinimas

```bash
python lint_markdown_cli.py --verbose
```

**Tikslas**: Aptikti pasenusius CLI šablonus dokumentacijoje

## Testavimas

### Greitieji testai

```bash
cd Workshop
python -m tests.smoke
```

**Testai**: Pagrindinių pavyzdžių funkcionalumo patikrinimas

## Trikčių šalinimas

### Paslauga neveikia

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Modulio importavimo klaidos

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Ryšio klaidos

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Modelis nerastas

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Aplinkos kintamųjų nuoroda

### Pagrindinė konfigūracija
| Kintamasis | Numatytasis | Aprašymas |
|------------|-------------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | Kinta | Naudojamas modelio alias |
| `FOUNDRY_LOCAL_ENDPOINT` | Automatinis | Paslaugos galinio taško perrašymas |
| `SHOW_USAGE` | `0` | Rodyti žetonų naudojimo statistiką |
| `RETRY_ON_FAIL` | `1` | Įjungti pakartotinio bandymo logiką |
| `RETRY_BACKOFF` | `1.0` | Pradinis pakartotinio bandymo vėlavimas (sekundėmis) |

### Sesijai specifiniai
| Kintamasis | Numatytasis | Aprašymas |
|------------|-------------|-----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Įterpimo modelis |
| `RAG_QUESTION` | Žr. pavyzdį | RAG testo klausimas |
| `BENCH_MODELS` | Kinta | Modeliai, atskirti kableliais |
| `BENCH_ROUNDS` | `3` | Veikimo testų iteracijos |
| `BENCH_PROMPT` | Žr. pavyzdį | Veikimo testo užklausa |
| `BENCH_STREAM` | `0` | Pirmojo ženklo vėlavimo matavimas |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Pagrindinis agento modelis |
| `AGENT_MODEL_EDITOR` | Pagrindinis | Redaktoriaus agento modelis |
| `SLM_ALIAS` | `phi-4-mini` | Mažas kalbos modelis |
| `LLM_ALIAS` | `qwen2.5-7b` | Didelis kalbos modelis |
| `COMPARE_PROMPT` | Žr. pavyzdį | Palyginimo užklausa |

## Rekomenduojami modeliai

### Kūrimas ir testavimas
- **phi-4-mini** - Subalansuota kokybė ir greitis
- **qwen2.5-0.5b** - Labai greitas klasifikavimui
- **gemma-2-2b** - Gera kokybė, vidutinis greitis

### Gamybiniai scenarijai
- **phi-4-mini** - Bendros paskirties
- **deepseek-coder-1.3b** - Kodo generavimas
- **qwen2.5-7b** - Aukštos kokybės atsakymai

## SDK dokumentacija

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  

## Pagalba

1. Patikrinkite paslaugos būseną: `foundry service status`  
2. Peržiūrėkite žurnalus: Patikrinkite Foundry Local paslaugos žurnalus  
3. Peržiūrėkite SDK dokumentaciją: https://github.com/microsoft/Foundry-Local  
4. Peržiūrėkite pavyzdinį kodą: Visi pavyzdžiai turi išsamius komentarus  

## Kiti žingsniai

1. Atlikite visas dirbtuvių sesijas iš eilės  
2. Eksperimentuokite su skirtingais modeliais  
3. Pritaikykite pavyzdžius savo poreikiams  
4. Peržiūrėkite `SDK_MIGRATION_NOTES.md` dėl pažangių šablonų  

---

**Paskutinį kartą atnaujinta**: 2025-01-08  
**Dirbtuvių versija**: Naujausia  
**SDK**: Foundry Local Python SDK

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.