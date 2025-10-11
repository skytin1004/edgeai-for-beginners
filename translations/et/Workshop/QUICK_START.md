<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20ef6223850f0ab7b6e546a6df0d7d68",
  "translation_date": "2025-10-11T11:47:51+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "et"
}
-->
# Töötuba Kiire Alustamise Juhend

## Eeltingimused

### 1. Paigalda Foundry Local

Järgi ametlikku paigaldusjuhendit:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Paigalda Python'i sõltuvused

Töötuba kataloogist:

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

## Töötuba Näidiste Käivitamine

### Sessioon 01: Põhiline Vestlus

```bash
cd Workshop/samples/session01
python chat_bootstrap.py "What are the benefits of local AI?"
```

**Keskkonnamuutujad:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sessioon 02: RAG Torustik

```bash
cd Workshop/samples/session02
python rag_pipeline.py
```

**Keskkonnamuutujad:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sessioon 02: RAG Hindamine (Ragas)

```bash
python rag_eval_ragas.py
```

**Märkus**: Vajab täiendavaid sõltuvusi, mis on paigaldatud `requirements.txt` kaudu

### Sessioon 03: Võrdlusuuring

```bash
cd Workshop/samples/session03
python benchmark_oss_models.py
```

**Keskkonnamuutujad:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,gemma-2-2b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Väljund**: JSON koos latentsuse, läbilaskevõime ja esimese märgi mõõdikutega

### Sessioon 04: Mudelite Võrdlus

```bash
cd Workshop/samples/session04
python model_compare.py
```

**Keskkonnamuutujad:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sessioon 05: Multi-Agent Orkestreerimine

```bash
cd Workshop/samples/session05
python agents_orchestrator.py
```

**Keskkonnamuutujad:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sessioon 06: Mudeli Marsruuter

```bash
cd Workshop/samples/session06
python models_router.py
```

**Testib marsruutimisloogikat** mitme kavatsusega (kood, kokkuvõte, klassifikatsioon)

### Sessioon 06: Torustik

```bash
python models_pipeline.py
```

**Kompleksne mitmeastmeline torustik** koos planeerimise, täitmise ja täiustamisega

## Skriptid

### Ekspordi Võrdlusuuringu Aruanne

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Väljund**: Markdown tabel + JSON mõõdikud

### Markdown CLI Mustrite Kontrollimine

```bash
python lint_markdown_cli.py --verbose
```

**Eesmärk**: Tuvastada vananenud CLI mustrid dokumentatsioonis

## Testimine

### Kiirtestid

```bash
cd Workshop
python -m tests.smoke
```

**Testid**: Põhifunktsionaalsus oluliste näidiste jaoks

## Tõrkeotsing

### Teenus Ei Tööta

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Mooduli Importimise Vead

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Ühenduse Vead

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Mudelit Ei Leitud

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Keskkonnamuutujate Viide

### Põhikonfiguratsioon
| Muutuja | Vaikimisi | Kirjeldus |
|---------|-----------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | Muutuv | Kasutatav mudeli alias |
| `FOUNDRY_LOCAL_ENDPOINT` | Automaatne | Teenuse lõpp-punkti ülekirjutamine |
| `SHOW_USAGE` | `0` | Näita märgi kasutamise statistikat |
| `RETRY_ON_FAIL` | `1` | Luba uuesti proovimise loogika |
| `RETRY_BACKOFF` | `1.0` | Esialgne uuesti proovimise viivitus (sekundites) |

### Sessioonipõhine
| Muutuja | Vaikimisi | Kirjeldus |
|---------|-----------|-----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding mudel |
| `RAG_QUESTION` | Vaata näidist | RAG testküsimus |
| `BENCH_MODELS` | Muutuv | Komaga eraldatud mudelid |
| `BENCH_ROUNDS` | `3` | Võrdlusuuringu iteratsioonid |
| `BENCH_PROMPT` | Vaata näidist | Võrdlusuuringu küsimus |
| `BENCH_STREAM` | `0` | Mõõda esimese märgi latentsust |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Peamine agent mudel |
| `AGENT_MODEL_EDITOR` | Peamine | Redaktori agent mudel |
| `SLM_ALIAS` | `phi-4-mini` | Väike keelemudel |
| `LLM_ALIAS` | `qwen2.5-7b` | Suur keelemudel |
| `COMPARE_PROMPT` | Vaata näidist | Võrdluse küsimus |

## Soovitatud Mudelid

### Arendus ja Testimine
- **phi-4-mini** - Tasakaalustatud kvaliteet ja kiirus
- **qwen2.5-0.5b** - Väga kiire klassifikatsiooni jaoks
- **gemma-2-2b** - Hea kvaliteet, mõõdukas kiirus

### Tootmistsenaariumid
- **phi-4-mini** - Üldotstarbeline
- **deepseek-coder-1.3b** - Koodi genereerimine
- **qwen2.5-7b** - Kõrge kvaliteediga vastused

## SDK Dokumentatsioon

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Abi Saamine

1. Kontrolli teenuse olekut: `foundry service status`  
2. Vaata logisid: Kontrolli Foundry Local teenuse logisid  
3. Vaata SDK dokumentatsiooni: https://github.com/microsoft/Foundry-Local  
4. Uuri näidiskoodi: Kõigil näidistel on üksikasjalikud kommentaarid

## Järgmised Sammud

1. Lõpeta kõik töötuba sessioonid järjekorras  
2. Katseta erinevaid mudeleid  
3. Kohanda näidiseid oma kasutusjuhtude jaoks  
4. Vaata `SDK_MIGRATION_NOTES.md` edasijõudnute mustrite jaoks

---

**Viimati Uuendatud**: 2025-01-08  
**Töötuba Versioon**: Viimane  
**SDK**: Foundry Local Python SDK

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.