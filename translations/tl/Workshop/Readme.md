<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "48d0fb38be925084a6ebd957d4b045e5",
  "translation_date": "2025-10-09T19:23:46+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "tl"
}
-->
# EdgeAI para sa mga Baguhan - Workshop

> **Praktikal na Landas sa Pag-aaral para sa Pagbuo ng Production-Ready Edge AI Applications**
>
> Masterin ang lokal na AI deployment gamit ang Microsoft Foundry Local, mula sa unang chat completion hanggang sa multi-agent orchestration sa 6 na progresibong sesyon.

---

## 🎯 Panimula

Maligayang pagdating sa **EdgeAI para sa mga Baguhan Workshop** - ang iyong praktikal na gabay sa pagbuo ng mga intelligent na aplikasyon na tumatakbo nang buo sa lokal na hardware. Ang workshop na ito ay nagbabago ng mga teoretikal na konsepto ng Edge AI sa mga kasanayan sa totoong mundo sa pamamagitan ng mga progresibong hamon gamit ang Microsoft Foundry Local at Small Language Models (SLMs).

### Bakit Itong Workshop?

**Narito na ang Edge AI Revolution**

Ang mga organisasyon sa buong mundo ay lumilipat mula sa cloud-dependent AI patungo sa edge computing para sa tatlong mahahalagang dahilan:

1. **Privacy at Pagsunod** - Iproseso ang sensitibong data nang lokal nang hindi ipinapadala sa cloud (HIPAA, GDPR, mga regulasyon sa pananalapi)
2. **Pagganap** - Tanggalin ang network latency (50-500ms lokal kumpara sa 500-2000ms cloud round-trip)
3. **Kontrol sa Gastos** - Alisin ang per-token API costs at mag-scale nang walang gastos sa cloud

**Ngunit Iba ang Edge AI**

Ang pagpapatakbo ng AI on-premises ay nangangailangan ng mga bagong kasanayan:
- Pagpili at pag-optimize ng modelo para sa mga limitadong resources
- Pamamahala ng lokal na serbisyo at hardware acceleration
- Prompt engineering para sa mas maliliit na modelo
- Mga pattern ng deployment para sa mga edge device

**Ang Workshop na Ito ay Nagbibigay ng Mga Kasanayang Iyon**

Sa 6 na nakatuong sesyon (~3 oras kabuuan), magpo-progress ka mula sa "Hello World" hanggang sa pag-deploy ng production-ready multi-agent systems - lahat ay tumatakbo nang lokal sa iyong makina.

---

## 📚 Mga Layunin sa Pag-aaral

Sa pagtatapos ng workshop na ito, magagawa mo ang:

### Pangunahing Kakayahan
1. **Mag-deploy at Mag-manage ng Lokal na AI Services**
   - I-install at i-configure ang Microsoft Foundry Local
   - Pumili ng angkop na mga modelo para sa edge deployment
   - Pamahalaan ang lifecycle ng modelo (download, load, cache)
   - Subaybayan ang paggamit ng resources at i-optimize ang pagganap

2. **Bumuo ng AI-Powered Applications**
   - Mag-implement ng OpenAI-compatible chat completions nang lokal
   - Magdisenyo ng epektibong prompts para sa Small Language Models
   - Mag-handle ng streaming responses para sa mas mahusay na UX
   - Isama ang lokal na mga modelo sa umiiral na mga aplikasyon

3. **Lumikha ng RAG (Retrieval Augmented Generation) Systems**
   - Bumuo ng semantic search gamit ang embeddings
   - I-ground ang LLM responses sa domain-specific na kaalaman
   - Suriin ang kalidad ng RAG gamit ang industry-standard metrics
   - Mag-scale mula prototype hanggang production

4. **I-optimize ang Pagganap ng Modelo**
   - Mag-benchmark ng maraming modelo para sa iyong use case
   - Sukatin ang latency, throughput, at first-token time
   - Pumili ng optimal na mga modelo batay sa speed/quality tradeoffs
   - Ikumpara ang SLM vs LLM trade-offs sa totoong mga senaryo

5. **Mag-orchestrate ng Multi-Agent Systems**
   - Magdisenyo ng mga specialized na agent para sa iba't ibang gawain
   - Mag-implement ng agent memory at context management
   - Mag-coordinate ng mga agent sa mga kumplikadong workflow
   - Mag-route ng mga request nang matalino sa iba't ibang modelo

6. **Mag-deploy ng Production-Ready Solutions**
   - Mag-implement ng error handling at retry logic
   - Subaybayan ang token usage at system resources
   - Bumuo ng scalable architectures gamit ang model-as-tools patterns
   - Magplano ng migration paths mula edge patungo sa hybrid (edge + cloud)

---

## 🎓 Mga Resulta ng Pag-aaral

### Ano ang Iyong Mabubuo

Sa pagtatapos ng workshop na ito, makakabuo ka ng:

| Sesyon | Output | Mga Kasanayang Naipakita |
|--------|--------|--------------------------|
| **1** | Chat application na may streaming | Setup ng serbisyo, basic completions, streaming UX |
| **2** | RAG system na may evaluation | Embeddings, semantic search, quality metrics |
| **3** | Multi-model benchmark suite | Pagsukat ng pagganap, pagkukumpara ng modelo |
| **4** | SLM vs LLM comparator | Pagsusuri ng trade-offs, optimization strategies |
| **5** | Multi-agent orchestrator | Disenyo ng agent, memory management, coordination |
| **6** | Intelligent routing system | Intent detection, model selection, scalability |

### Competency Matrix

| Antas ng Kasanayan | Sesyon 1-2 | Sesyon 3-4 | Sesyon 5-6 |
|--------------------|------------|------------|------------|
| **Baguhan** | ✅ Setup at mga basic | ⚠️ Hamon | ❌ Masyadong advanced |
| **Intermediate** | ✅ Mabilis na review | ✅ Core learning | ⚠️ Stretch goals |
| **Advanced** | ✅ Madali lang | ✅ Refinement | ✅ Production patterns |

### Mga Kasanayang Pangkarera

**Pagkatapos ng workshop na ito, handa ka nang:**

✅ **Bumuo ng Privacy-First Applications**
- Mga healthcare app na nagha-handle ng PHI/PII nang lokal
- Mga serbisyo sa pananalapi na may mga kinakailangan sa pagsunod
- Mga sistema ng gobyerno na may pangangailangan sa data sovereignty

✅ **Mag-optimize para sa Edge Environments**
- Mga IoT device na may limitadong resources
- Offline-first na mga mobile application
- Mga low-latency real-time na sistema

✅ **Magdisenyo ng Intelligent Architectures**
- Multi-agent systems para sa mga kumplikadong workflow
- Hybrid edge-cloud deployments
- Cost-optimized AI infrastructure

✅ **Manguna sa Edge AI Initiatives**
- Suriin ang feasibility ng Edge AI para sa mga proyekto
- Pumili ng angkop na mga modelo at frameworks
- Magdisenyo ng scalable local AI solutions

---

## 🗺️ Estruktura ng Workshop

### Overview ng Sesyon (6 Sesyon × 30 Minuto = 3 Oras)

| Sesyon | Paksa | Pokus | Tagal |
|--------|-------|-------|-------|
| **1** | Pagsisimula sa Foundry Local | Install, validate, first completions | 30 min |
| **2** | Pagbuo ng AI Solutions gamit ang RAG | Prompt engineering, embeddings, evaluation | 30 min |
| **3** | Open Source Models | Model discovery, benchmarking, selection | 30 min |
| **4** | Cutting Edge Models | SLM vs LLM, optimization, frameworks | 30 min |
| **5** | AI-Powered Agents | Agent design, orchestration, memory | 30 min |
| **6** | Models as Tools | Routing, chaining, scaling strategies | 30 min |

---

## 🚀 Mabilis na Pagsisimula

### Mga Kinakailangan

**System Requirements:**
- **OS**: Windows 10/11, macOS 11+, o Linux (Ubuntu 20.04+)
- **RAM**: Minimum na 8GB, inirerekomenda ang 16GB+
- **Storage**: 10GB+ na libreng espasyo para sa mga modelo
- **CPU**: Modernong processor na may AVX2 support
- **GPU** (opsyonal): CUDA-compatible o Qualcomm NPU para sa acceleration

**Software Requirements:**
- **Python 3.8+** ([I-download](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Installation Guide](../../../Workshop))
- **Git** ([I-download](https://git-scm.com/downloads))
- **Visual Studio Code** (inirerekomenda) ([I-download](https://code.visualstudio.com/))

### Setup sa 3 Hakbang

#### 1. I-install ang Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**I-verify ang Installation:**
```bash
foundry --version
foundry service status
```

#### 2. I-clone ang Repository at I-install ang Dependencies

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Patakbuhin ang Iyong Unang Sample

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples/session01
python chat_bootstrap.py "What is edge AI?"
```

**✅ Tagumpay!** Makikita mo ang isang streaming response tungkol sa edge AI.

---

## 📦 Mga Resources ng Workshop

### Python Samples

Mga progresibong hands-on na halimbawa na nagpapakita ng bawat konsepto:

| Sesyon | Sample | Deskripsyon | Run Time |
|--------|--------|-------------|----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Basic & streaming chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG gamit ang embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Pagsusuri ng kalidad ng RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Multi-model benchmarking | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM comparison | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Multi-agent system | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Intent-based routing | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Multi-step pipeline | ~60s |

### Jupyter Notebooks

Interactive na eksplorasyon na may mga paliwanag at visualizations:

| Sesyon | Notebook | Deskripsyon | Hirap |
|--------|----------|-------------|-------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Mga basic sa chat & streaming | ⭐ Baguhan |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Bumuo ng RAG system | ⭐⭐ Intermediate |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Suriin ang kalidad ng RAG | ⭐⭐ Intermediate |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Model benchmarking | ⭐⭐ Intermediate |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Paghahambing ng modelo | ⭐⭐ Intermediate |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Agent orchestration | ⭐⭐⭐ Advanced |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Intent routing | ⭐⭐⭐ Advanced |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Pipeline orchestration | ⭐⭐⭐ Advanced |

### Dokumentasyon

Komprehensibong mga gabay at reference:

| Dokumento | Deskripsyon | Kailan Gagamitin |
|-----------|-------------|------------------|
| [QUICK_START.md](./QUICK_START.md) | Mabilis na gabay sa setup | Simula mula sa simula |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Command & API cheat sheet | Kailangan ng mabilis na sagot |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Mga pattern ng SDK & halimbawa | Pagsusulat ng code |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Gabay sa environment variable | Pag-configure ng mga sample |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Pinakabagong mga pagpapabuti sa sample | Pag-unawa sa mga pagbabago |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Gabay sa migration | Pag-upgrade ng code |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Mga karaniwang isyu at solusyon | Pag-debug ng mga problema |

---

## 🎓 Mga Rekomendasyon sa Landas ng Pag-aaral

### Para sa mga Baguhan (3-4 oras)
1. ✅ Sesyon 1: Pagsisimula (pokus sa setup at basic chat)
2. ✅ Sesyon 2: Mga Basic ng RAG (laktawan ang evaluation sa simula)
3. ✅ Sesyon 3: Simpleng Benchmarking (2 modelo lang)
4. ⏭️ Laktawan ang Sesyon 4-6 sa ngayon
5. 🔄 Bumalik sa Sesyon 4-6 pagkatapos bumuo ng unang aplikasyon

### Para sa Intermediate na mga Developer (3 oras)
1. ⚡ Sesyon 1: Mabilis na validation ng setup
2. ✅ Sesyon 2: Kumpletuhin ang RAG pipeline na may evaluation
3. ✅ Sesyon 3: Buong benchmarking suite
4. ✅ Sesyon 4: Optimization ng modelo
5. ✅ Sesyon 5-6: Pokus sa mga pattern ng arkitektura

### Para sa Advanced na mga Practitioner (2-3 oras)
1. ⚡ Sesyon 1-3: Mabilis na review at validation
2. ✅ Sesyon 4: Malalimang pag-aaral sa optimization
3. ✅ Sesyon 5: Arkitektura ng multi-agent
4. ✅ Sesyon 6: Mga pattern ng production at scaling
5. 🚀 Palawakin: Bumuo ng custom routing logic at hybrid deployments

---

## Workshop Session Pack (Nakatuon na 30‑Minutong Labs)

Kung sinusunod mo ang condensed na 6-session workshop format, gamitin ang mga dedikadong gabay na ito (bawat isa ay tumutugma at kumplemento sa mas malawak na module docs sa itaas):

| Workshop Session | Gabay | Pangunahing Pokus |
|------------------|-------|-------------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Install, validate, patakbuhin ang phi & GPT-OSS-20B, acceleration |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Prompt engineering, RAG patterns, CSV & document grounding, migration |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face integration, benchmarking, model selection |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX acceleration |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Mga role ng agent, memory, tools, orchestration |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routing, chaining, scaling path to Azure |
Ang bawat session file ay naglalaman ng: abstrak, mga layunin sa pag-aaral, 30-minutong demo flow, starter project, validation checklist, troubleshooting, at mga reference sa opisyal na Foundry Local Python SDK.

### Mga Sample na Script

I-install ang mga dependency ng workshop (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Kung ang Foundry Local service ay tumatakbo sa ibang (Windows) machine o VM mula sa macOS, i-export ang endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Session | Script(s) | Deskripsyon |
|---------|-----------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap service & streaming chat |
| 2 | `samples/session02/rag_pipeline.py` | Minimal RAG (in-memory embeddings) |
|   | `samples/session02/rag_eval_ragas.py` | RAG evaluation gamit ang ragas metrics |
| 3 | `samples/session03/benchmark_oss_models.py` | Multi-model latency & throughput benchmarking |
| 4 | `samples/session04/model_compare.py` | Paghahambing ng SLM vs LLM (latency & sample output) |
| 5 | `samples/session05/agents_orchestrator.py` | Dalawang-agent research → editorial pipeline |
| 6 | `samples/session06/models_router.py` | Intent-based routing demo |
|   | `samples/session06/models_pipeline.py` | Multi-step plan/execute/refine chain |

### Mga Environment Variable (Karaniwan sa Lahat ng Sample)

| Variable | Layunin | Halimbawa |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Default single model alias para sa basic samples | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Explicit SLM vs mas malaking model para sa paghahambing | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Comma list ng mga alias para sa benchmarking | `qwen2.5-0.5b,gemma-2-2b,mistral-7b` |
| `BENCH_ROUNDS` | Benchmark repetitions per model | `3` |
| `BENCH_PROMPT` | Prompt na ginagamit sa benchmarking | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Override test query para sa RAG pipeline | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Override agents pipeline query | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Model alias para sa research agent | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Model alias para sa editor agent (maaaring magkaiba) | `gpt-oss-20b` |
| `SHOW_USAGE` | Kapag `1`, ipinapakita ang token usage per completion | `1` |
| `RETRY_ON_FAIL` | Kapag `1`, magre-retry nang isang beses sa transient chat errors | `1` |
| `RETRY_BACKOFF` | Segundong paghihintay bago mag-retry | `1.0` |

Kung ang variable ay hindi naka-set, ang mga script ay babalik sa mga sensible defaults. Para sa single-model demos, karaniwang kailangan mo lang ang `FOUNDRY_LOCAL_ALIAS`.

### Utility Module

Ang lahat ng sample ay gumagamit ng helper `samples/workshop_utils.py` na nagbibigay ng:

* Cached `FoundryLocalManager` + OpenAI client creation
* `chat_once()` helper na may optional retry + usage printing
* Simpleng token usage reporting (i-enable gamit ang `SHOW_USAGE=1`)

Binabawasan nito ang duplication at itinatampok ang best practices para sa efficient local model orchestration.

## Mga Opsyonal na Pagpapahusay (Cross-Session)

| Tema | Pagpapahusay | Mga Session | Env / Toggle |
|-------|-------------|----------|--------------|
| Determinism | Fixed temperature + stable prompt sets | 1–6 | Set `temperature=0`, `top_p=1` |
| Token Usage Visibility | Consistent cost/efficiency teaching | 1–6 | `SHOW_USAGE=1` |
| Streaming First Token | Perceived latency metric | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Retry Resilience | Handles transient cold-start | Lahat | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-Model Agents | Heterogeneous role specialization | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptive Routing | Intent + cost heuristics | 6 | Extend router with escalation logic |
| Vector Memory | Long-term semantic recall | 2,5,6 | Integrate FAISS/Chroma embedding index |
| Trace Export | Auditing & evaluation | 2,5,6 | Append JSON lines per step |
| Quality Rubrics | Qualitative tracking | 3–6 | Secondary scoring prompts |
| Smoke Tests | Quick pre-workshop validation | Lahat | `python Workshop/tests/smoke.py` |

### Deterministic Quick Start

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Asahan ang stable token counts sa mga paulit-ulit na magkaparehong input.

### RAG Evaluation (Session 2)

Gamitin ang `rag_eval_ragas.py` para kalkulahin ang answer relevancy, faithfulness, at context precision sa isang maliit na synthetic dataset:

```powershell
python samples/session02/rag_eval_ragas.py
```

Palawakin sa pamamagitan ng pag-supply ng mas malaking JSONL ng mga tanong, konteksto, at ground truths, pagkatapos ay i-convert sa Hugging Face `Dataset`.

## CLI Command Accuracy Appendix

Ang workshop ay sadyang gumagamit lamang ng kasalukuyang dokumentado / stable na Foundry Local CLI commands.

### Stable Commands na Ginamit

| Kategorya | Command | Layunin |
|----------|---------|---------|
| Core | `foundry --version` | Ipakita ang installed version |
| Core | `foundry init` | I-initialize ang configuration |
| Service | `foundry service start` | I-start ang local service (kung hindi auto) |
| Service | `foundry status` | Ipakita ang service status |
| Models | `foundry model list` | Ilista ang catalog / available models |
| Models | `foundry model download <alias>` | I-download ang model weights sa cache |
| Models | `foundry model run <alias>` | I-launch (load) ang model locally; pagsamahin sa `--prompt` para sa one-shot |
| Models | `foundry model unload <alias>` / `foundry model stop <alias>` | I-unload ang model mula sa memory (kung supported) |
| Cache | `foundry cache list` | Ilista ang cached (downloaded) models |
| System | `foundry system info` | Snapshot ng hardware & acceleration capabilities |
| System | `foundry system gpu-info` | GPU diagnostic info |
| Config | `foundry config list` | Ipakita ang kasalukuyang config values |
| Config | `foundry config set <key> <value>` | I-update ang configuration |

### One-Shot Prompt Pattern

Sa halip na deprecated na `model chat` subcommand, gamitin:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Ito ay nag-e-execute ng isang prompt/response cycle pagkatapos ay mag-e-exit.

### Mga Tinanggal / Iwasang Pattern

| Deprecated / Undocumented | Kapalit / Gabay |
|---------------------------|------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Gamitin ang plain `foundry model list` + recent activity / logs |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Gamitin ang benchmark Python script + OS tools (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetry

- Latency, p95, tokens/sec: `samples/session03/benchmark_oss_models.py`
- First-token latency (streaming): set `BENCH_STREAM=1`
- Resource usage: OS monitors (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Kapag ang mga bagong CLI telemetry commands ay naging stable upstream, maaari itong isama nang may minimal na edits sa session markdowns.

### Automated Lint Guard

Isang automated linter ang pumipigil sa muling pagpasok ng deprecated CLI patterns sa loob ng fenced code blocks ng markdown files:

Script: `Workshop/scripts/lint_markdown_cli.py`

Ang mga deprecated patterns ay naka-block sa loob ng code fences.

Mga inirerekomendang kapalit:
| Deprecated | Kapalit |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmark script + system tools |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Patakbuhin nang lokal:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` tumatakbo sa bawat push & PR.

Opsyonal na pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Quick CLI → SDK Migration Table

| Gawain | CLI One-Liner | SDK (Python) Equivalent | Tala |
|------|---------------|-------------------------|-------|
| Patakbuhin ang model nang isang beses (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | Ang SDK ay awtomatikong nagbo-bootstrap ng service & caching |
| I-download (cache) ang model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Ang Manager ay pumipili ng pinakamahusay na variant kung ang alias ay may maraming build |
| Ilista ang catalog | `foundry model list` | `# gamitin ang manager para sa bawat alias o panatilihin ang kilalang listahan` | Ang CLI ay nag-a-aggregate; ang SDK ay kasalukuyang per-alias instantiation |
| Ilista ang cached models | `foundry cache list` | `manager.list_cached_models()` | Pagkatapos ng manager init (anumang alias) |
| I-enable ang GPU acceleration | `foundry config set compute.onnx.enable_gpu true` | `# CLI action; SDK assumes config already applied` | Ang configuration ay external side effect |
| Kunin ang endpoint URL | (implicit) | `manager.endpoint` | Ginagamit para gumawa ng OpenAI-compatible client |
| I-warm ang model | `foundry model run <alias>` pagkatapos ng unang prompt | `chat_once(alias, messages=[...])` (utility) | Ang mga utility ay humahawak sa initial cold latency warmup |
| Sukatin ang latency | `python benchmark_oss_models.py` | `import benchmark_oss_models` (o bagong exporter script) | Mas mainam ang script para sa consistent metrics |
| I-stop / i-unload ang model | `foundry model unload <alias>` | (Hindi exposed – i-restart ang service / process) | Karaniwang hindi kinakailangan para sa workshop flow |
| Kunin ang token usage | (tingnan ang output) | `resp.usage.total_tokens` | Ibinibigay kung ang backend ay nagre-return ng usage object |

## Benchmark Markdown Export

Gamitin ang script na `Workshop/scripts/export_benchmark_markdown.py` para magpatakbo ng bagong benchmark (parehong logic tulad ng `samples/session03/benchmark_oss_models.py`) at mag-emit ng GitHub-friendly Markdown table plus raw JSON.

### Halimbawa

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Mga na-generate na file:
| File | Nilalaman |
|------|----------|
| `benchmark_report.md` | Markdown table + mga hint sa interpretasyon |
| `benchmark_report.json` | Raw metrics array (para sa diffing / trend tracking) |

I-set ang `BENCH_STREAM=1` sa environment para isama ang first-token latency kung supported.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.