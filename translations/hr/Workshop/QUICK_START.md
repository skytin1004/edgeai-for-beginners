<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-08T14:00:04+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "hr"
}
-->
# Brzi vodič za radionicu

## Preduvjeti

### 1. Instalirajte Foundry Local

Slijedite službeni vodič za instalaciju:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Instalirajte Python ovisnosti

Iz direktorija radionice:

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

## Pokretanje primjera iz radionice

### Sesija 01: Osnovni chat

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**Varijable okruženja:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sesija 02: RAG cjevovod

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**Varijable okruženja:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sesija 02: RAG evaluacija (Ragas)

```bash
python rag_eval_ragas.py
```

**Napomena**: Zahtijeva dodatne ovisnosti instalirane putem `requirements.txt`

### Sesija 03: Benchmarking

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**Varijable okruženja:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Izlaz**: JSON s metrikama latencije, propusnosti i vremena za prvi token

### Sesija 04: Usporedba modela

```bash
cd Workshop/samples/session04
python model_compare.py
```

**Varijable okruženja:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sesija 05: Orkestracija više agenata

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**Varijable okruženja:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sesija 06: Usmjerivač modela

```bash
cd Workshop/samples/session06
python models_router.py
```

**Testira logiku usmjeravanja** s više namjera (kod, sažetak, klasifikacija)

### Sesija 06: Cjevovod

```bash
python models_pipeline.py
```

**Složen višestupanjski cjevovod** s planiranjem, izvršenjem i doradom

## Skripte

### Izvoz izvještaja o benchmarku

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Izlaz**: Markdown tablica + JSON metrike

### Provjera CLI uzoraka u Markdownu

```bash
python lint_markdown_cli.py --verbose
```

**Svrha**: Otkrivanje zastarjelih CLI uzoraka u dokumentaciji

## Testiranje

### Brzi testovi

```bash
cd Workshop
python -m tests.smoke
```

**Testovi**: Osnovna funkcionalnost ključnih primjera

## Rješavanje problema

### Usluga ne radi

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Pogreške pri uvozu modula

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Pogreške povezivanja

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model nije pronađen

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referenca varijabli okruženja

### Osnovna konfiguracija
| Varijabla | Zadano | Opis |
|-----------|--------|------|
| `FOUNDRY_LOCAL_ALIAS` | Razlikuje se | Alias modela koji se koristi |
| `FOUNDRY_LOCAL_ENDPOINT` | Automatski | Prepisuje krajnju točku usluge |
| `SHOW_USAGE` | `0` | Prikazuje statistiku korištenja tokena |
| `RETRY_ON_FAIL` | `1` | Omogućuje logiku ponovnog pokušaja |
| `RETRY_BACKOFF` | `1.0` | Početno kašnjenje ponovnog pokušaja (sekunde) |

### Specifično za sesiju
| Varijabla | Zadano | Opis |
|-----------|--------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model za ugrađivanje |
| `RAG_QUESTION` | Pogledajte primjer | Testno pitanje za RAG |
| `BENCH_MODELS` | Razlikuje se | Modeli odvojeni zarezom |
| `BENCH_ROUNDS` | `3` | Iteracije benchmarka |
| `BENCH_PROMPT` | Pogledajte primjer | Prompt za benchmark |
| `BENCH_STREAM` | `0` | Mjeri latenciju prvog tokena |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Primarni model agenta |
| `AGENT_MODEL_EDITOR` | Primarni | Model agenta za uređivanje |
| `SLM_ALIAS` | `phi-4-mini` | Mali jezični model |
| `LLM_ALIAS` | `qwen2.5-7b` | Veliki jezični model |
| `COMPARE_PROMPT` | Pogledajte primjer | Prompt za usporedbu |

## Preporučeni modeli

### Razvoj i testiranje
- **phi-4-mini** - Uravnotežena kvaliteta i brzina
- **qwen2.5-0.5b** - Vrlo brz za klasifikaciju
- **gemma-2-2b** - Dobra kvaliteta, umjerena brzina

### Produkcijski scenariji
- **phi-4-mini** - Opća namjena
- **deepseek-coder-1.3b** - Generiranje koda
- **qwen2.5-7b** - Visokokvalitetni odgovori

## SDK dokumentacija

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Dobivanje pomoći

1. Provjerite status usluge: `foundry service status`  
2. Pregledajte logove: Provjerite logove usluge Foundry Local  
3. Pregledajte SDK dokumentaciju: https://github.com/microsoft/Foundry-Local  
4. Pregledajte primjere koda: Svi primjeri imaju detaljne docstringove

## Sljedeći koraci

1. Završite sve sesije radionice redoslijedom  
2. Eksperimentirajte s različitim modelima  
3. Prilagodite primjere za svoje slučajeve korištenja  
4. Pregledajte `SDK_MIGRATION_NOTES.md` za napredne uzorke

---

**Zadnje ažuriranje**: 2025-01-08  
**Verzija radionice**: Najnovija  
**SDK**: Foundry Local Python SDK

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.