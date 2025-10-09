<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-09T21:06:42+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "sw"
}
-->
# Mwongozo wa Haraka wa Warsha

## Mahitaji ya Awali

### 1. Sakinisha Foundry Local

Fuata mwongozo rasmi wa usakinishaji:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Sakinisha Mahitaji ya Python

Kutoka kwenye saraka ya Warsha:

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

## Kuendesha Sampuli za Warsha

### Kipindi 01: Gumzo la Msingi

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**Vigezo vya Mazingira:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Kipindi 02: RAG Pipeline

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**Vigezo vya Mazingira:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Kipindi 02: Tathmini ya RAG (Ragas)

```bash
python rag_eval_ragas.py
```

**Kumbuka**: Inahitaji mahitaji ya ziada kusakinishwa kupitia `requirements.txt`

### Kipindi 03: Upimaji wa Utendaji

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**Vigezo vya Mazingira:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Matokeo**: JSON yenye vipimo vya ucheleweshaji, kasi ya usindikaji, na kipimo cha tokeni ya kwanza

### Kipindi 04: Ulinganisho wa Miundo

```bash
cd Workshop/samples/session04
python model_compare.py
```

**Vigezo vya Mazingira:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Kipindi 05: Uratibu wa Wakala Wengi

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**Vigezo vya Mazingira:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Kipindi 06: Router ya Miundo

```bash
cd Workshop/samples/session06
python models_router.py
```

**Inajaribu mantiki ya uelekezaji** kwa nia mbalimbali (kodi, muhtasari, uainishaji)

### Kipindi 06: Pipeline

```bash
python models_pipeline.py
```

**Pipeline ya hatua nyingi ngumu** yenye upangaji, utekelezaji, na uboreshaji

## Scripti

### Hamisha Ripoti ya Upimaji

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Matokeo**: Jedwali la Markdown + vipimo vya JSON

### Kagua Mifumo ya CLI ya Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Madhumuni**: Kugundua mifumo ya CLI iliyopitwa na wakati katika nyaraka

## Upimaji

### Majaribio ya Haraka

```bash
cd Workshop
python -m tests.smoke
```

**Majaribio**: Utendaji wa msingi wa sampuli muhimu

## Utatuzi wa Shida

### Huduma Haifanyi Kazi

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Hitilafu za Uingizaji wa Moduli

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Hitilafu za Muunganisho

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Muundo Haupatikani

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Marejeleo ya Vigezo vya Mazingira

### Usanidi wa Msingi
| Kigezo | Chaguo-msingi | Maelezo |
|--------|--------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Inatofautiana | Jina la muundo wa kutumia |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Badilisha endpoint ya huduma |
| `SHOW_USAGE` | `0` | Onyesha takwimu za matumizi ya tokeni |
| `RETRY_ON_FAIL` | `1` | Washa mantiki ya kujaribu tena |
| `RETRY_BACKOFF` | `1.0` | Muda wa kuchelewa wa kujaribu tena (sekunde) |

### Mahususi kwa Kipindi
| Kigezo | Chaguo-msingi | Maelezo |
|--------|--------------|----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Muundo wa kuingiza |
| `RAG_QUESTION` | Tazama sampuli | Swali la majaribio ya RAG |
| `BENCH_MODELS` | Inatofautiana | Miundo iliyotenganishwa kwa koma |
| `BENCH_ROUNDS` | `3` | Mizunguko ya upimaji |
| `BENCH_PROMPT` | Tazama sampuli | Maelezo ya upimaji |
| `BENCH_STREAM` | `0` | Pima ucheleweshaji wa tokeni ya kwanza |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Muundo wa wakala wa msingi |
| `AGENT_MODEL_EDITOR` | Msingi | Muundo wa wakala wa mhariri |
| `SLM_ALIAS` | `phi-4-mini` | Muundo mdogo wa lugha |
| `LLM_ALIAS` | `qwen2.5-7b` | Muundo mkubwa wa lugha |
| `COMPARE_PROMPT` | Tazama sampuli | Maelezo ya ulinganisho |

## Miundo Inayopendekezwa

### Maendeleo na Upimaji
- **phi-4-mini** - Ubora na kasi iliyosawazishwa
- **qwen2.5-0.5b** - Kasi kubwa kwa uainishaji
- **gemma-2-2b** - Ubora mzuri, kasi ya wastani

### Matukio ya Uzalishaji
- **phi-4-mini** - Matumizi ya jumla
- **deepseek-coder-1.3b** - Uzalishaji wa kodi
- **qwen2.5-7b** - Majibu ya ubora wa juu

## Nyaraka za SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Kupata Msaada

1. Angalia hali ya huduma: `foundry service status`  
2. Tazama kumbukumbu: Angalia kumbukumbu za huduma za Foundry Local  
3. Angalia nyaraka za SDK: https://github.com/microsoft/Foundry-Local  
4. Pitia sampuli za kodi: Sampuli zote zina maelezo ya kina

## Hatua Zifuatazo

1. Kamilisha vipindi vyote vya warsha kwa mpangilio  
2. Jaribu miundo tofauti  
3. Badilisha sampuli kwa matumizi yako  
4. Pitia `SDK_MIGRATION_NOTES.md` kwa mifumo ya hali ya juu  

---

**Imeboreshwa Mwisho**: 2025-01-08  
**Toleo la Warsha**: La hivi karibuni  
**SDK**: Foundry Local Python SDK

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.