<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-08T15:15:07+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "ro"
}
-->
# Ghid de Pornire Rapidă pentru Workshop

## Cerințe Prealabile

### 1. Instalează Foundry Local

Urmează ghidul oficial de instalare:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Instalează Dependențele Python

Din directorul Workshop:

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

## Rularea Exemplelor din Workshop

### Sesiunea 01: Chat de Bază

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**Variabile de Mediu:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sesiunea 02: Pipeline RAG

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**Variabile de Mediu:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sesiunea 02: Evaluarea RAG (Ragas)

```bash
python rag_eval_ragas.py
```

**Notă**: Necesită dependențe suplimentare instalate prin `requirements.txt`

### Sesiunea 03: Benchmarking

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**Variabile de Mediu:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Output**: JSON cu metrici de latență, throughput și primul token

### Sesiunea 04: Compararea Modelelor

```bash
cd Workshop/samples/session04
python model_compare.py
```

**Variabile de Mediu:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sesiunea 05: Orchestrarea Multi-Agent

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**Variabile de Mediu:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sesiunea 06: Router de Modele

```bash
cd Workshop/samples/session06
python models_router.py
```

**Testează logica de rutare** cu multiple intenții (cod, sumarizare, clasificare)

### Sesiunea 06: Pipeline

```bash
python models_pipeline.py
```

**Pipeline complex multi-pas** cu planificare, execuție și rafinare

## Scripturi

### Exportă Raportul de Benchmark

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Output**: Tabel Markdown + metrici JSON

### Verifică Modele CLI Depășite

```bash
python lint_markdown_cli.py --verbose
```

**Scop**: Detectează modele CLI depășite în documentație

## Testare

### Teste de Bază

```bash
cd Workshop
python -m tests.smoke
```

**Teste**: Funcționalitatea de bază a exemplelor cheie

## Depanare

### Serviciul Nu Rulează

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Erori de Import al Modulului

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Erori de Conexiune

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Modelul Nu a Fost Găsit

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referință pentru Variabilele de Mediu

### Configurație de Bază
| Variabilă | Implicit | Descriere |
|-----------|----------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | Variază | Alias-ul modelului utilizat |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Suprascrie endpoint-ul serviciului |
| `SHOW_USAGE` | `0` | Afișează statisticile de utilizare a token-urilor |
| `RETRY_ON_FAIL` | `1` | Activează logica de retry |
| `RETRY_BACKOFF` | `1.0` | Întârzierea inițială pentru retry (secunde) |

### Specific Sesiunii
| Variabilă | Implicit | Descriere |
|-----------|----------|-----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model de embedding |
| `RAG_QUESTION` | Vezi exemplu | Întrebare de test pentru RAG |
| `BENCH_MODELS` | Variază | Modele separate prin virgulă |
| `BENCH_ROUNDS` | `3` | Iterații de benchmark |
| `BENCH_PROMPT` | Vezi exemplu | Prompt pentru benchmark |
| `BENCH_STREAM` | `0` | Măsoară latența primului token |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Modelul principal al agentului |
| `AGENT_MODEL_EDITOR` | Primar | Modelul editor al agentului |
| `SLM_ALIAS` | `phi-4-mini` | Model de limbaj mic |
| `LLM_ALIAS` | `qwen2.5-7b` | Model de limbaj mare |
| `COMPARE_PROMPT` | Vezi exemplu | Prompt pentru comparație |

## Modele Recomandate

### Dezvoltare & Testare
- **phi-4-mini** - Echilibru între calitate și viteză
- **qwen2.5-0.5b** - Foarte rapid pentru clasificare
- **gemma-2-2b** - Calitate bună, viteză moderată

### Scenarii de Producție
- **phi-4-mini** - Scop general
- **deepseek-coder-1.3b** - Generare de cod
- **qwen2.5-7b** - Răspunsuri de înaltă calitate

## Documentația SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  

## Obținerea Ajutorului

1. Verifică starea serviciului: `foundry service status`  
2. Vizualizează jurnalele: Verifică jurnalele serviciului Foundry Local  
3. Consultă documentația SDK: https://github.com/microsoft/Foundry-Local  
4. Revizuiește codul exemplu: Toate exemplele au comentarii detaliate  

## Pași Următori

1. Completează toate sesiunile workshop-ului în ordine  
2. Experimentează cu diferite modele  
3. Modifică exemplele pentru cazurile tale de utilizare  
4. Revizuiește `SDK_MIGRATION_NOTES.md` pentru modele avansate  

---

**Ultima Actualizare**: 2025-01-08  
**Versiunea Workshop-ului**: Cea mai recentă  
**SDK**: Foundry Local Python SDK

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.