<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T10:10:49+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "pa"
}
-->
# ਚੇਂਜਲੌਗ

EdgeAI for Beginners ਵਿੱਚ ਕੀਤੇ ਗਏ ਸਾਰੇ ਮਹੱਤਵਪੂਰਨ ਬਦਲਾਅ ਇੱਥੇ ਦਰਜ ਕੀਤੇ ਗਏ ਹਨ। ਇਸ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਮਿਤੀ-ਅਧਾਰਿਤ ਐਂਟਰੀਜ਼ ਅਤੇ Keep a Changelog ਸਟਾਈਲ (Added, Changed, Fixed, Removed, Docs, Moved) ਵਰਤਿਆ ਗਿਆ ਹੈ।

## 2025-10-08

### ਜੋੜਿਆ - ਵਰਕਸ਼ਾਪ ਦੀ ਵਿਸਤ੍ਰਿਤ ਅਪਡੇਟ
- **ਵਰਕਸ਼ਾਪ README.md ਦੀ ਪੂਰੀ ਤਰ੍ਹਾਂ ਮੁੜ ਲਿਖਤ**:
  - Edge AI ਦੇ ਮੁੱਲ ਪ੍ਰਸਤਾਵ (ਗੋਪਨੀਯਤਾ, ਪ੍ਰਦਰਸ਼ਨ, ਲਾਗਤ) ਨੂੰ ਸਮਝਾਉਣ ਵਾਲਾ ਵਿਸਤ੍ਰਿਤ ਪਰਿਚਯ ਸ਼ਾਮਲ ਕੀਤਾ
  - 6 ਮੁੱਖ ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼ਾਂ ਨਾਲ ਵਿਸਤ੍ਰਿਤ ਯੋਗਤਾਵਾਂ ਬਣਾਈਆਂ
  - ਡਿਲੀਵਰੇਬਲ ਅਤੇ ਯੋਗਤਾ ਮੈਟ੍ਰਿਕਸ ਦੇ ਨਾਲ ਸਿੱਖਣ ਦੇ ਨਤੀਜੇ ਵਾਲਾ ਟੇਬਲ ਸ਼ਾਮਲ ਕੀਤਾ
  - ਉਦਯੋਗ ਸਬੰਧੀਤਾ ਲਈ ਕਰੀਅਰ-ਤਿਆਰ ਯੋਗਤਾਵਾਂ ਦਾ ਸੈਕਸ਼ਨ ਸ਼ਾਮਲ ਕੀਤਾ
  - ਪੂਰਵ ਸ਼ਰਤਾਂ ਅਤੇ 3-ਕਦਮ ਸੈਟਅਪ ਦੇ ਨਾਲ ਤੁਰੰਤ ਸ਼ੁਰੂ ਕਰਨ ਵਾਲੀ ਗਾਈਡ ਸ਼ਾਮਲ ਕੀਤੀ
  - Python ਸੈਂਪਲਾਂ ਲਈ ਸਰੋਤ ਟੇਬਲ ਬਣਾਈਆਂ (8 ਫਾਈਲਾਂ ਦੇ ਰਨ ਟਾਈਮ ਦੇ ਨਾਲ)
  - Jupyter ਨੋਟਬੁੱਕਾਂ ਦੀ ਟੇਬਲ ਸ਼ਾਮਲ ਕੀਤੀ (8 ਨੋਟਬੁੱਕਾਂ ਦੇ ਮੁਸ਼ਕਲ ਦਰਜਿਆਂ ਦੇ ਨਾਲ)
  - ਦਸਤਾਵੇਜ਼ਾਂ ਦੀ ਟੇਬਲ ਬਣਾਈ (7 ਮੁੱਖ ਦਸਤਾਵੇਜ਼ "ਕਦੋਂ ਵਰਤਣਾ ਹੈ" ਮਾਰਗਦਰਸ਼ਨ ਦੇ ਨਾਲ)
  - ਵੱਖ-ਵੱਖ ਯੋਗਤਾਵਾਂ ਦੇ ਪੱਧਰਾਂ ਲਈ ਸਿੱਖਣ ਦੇ ਰਾਹ ਦੀ ਸਿਫਾਰਸ਼ਾਂ ਸ਼ਾਮਲ ਕੀਤੀਆਂ

- **ਵਰਕਸ਼ਾਪ ਵੈਧਤਾ ਅਤੇ ਟੈਸਟਿੰਗ ਢਾਂਚਾ**:
  - `scripts/validate_samples.py` ਬਣਾਇਆ - syntax, imports, ਅਤੇ best practices ਲਈ ਵਿਸਤ੍ਰਿਤ ਵੈਧਤਾ ਟੂਲ
  - `scripts/test_samples.py` ਬਣਾਇਆ - ਸਾਰੇ Python ਸੈਂਪਲਾਂ ਲਈ smoke test runner
  - `scripts/README.md` ਵਿੱਚ ਵੈਧਤਾ ਦਸਤਾਵੇਜ਼ ਸ਼ਾਮਲ ਕੀਤੀ

- **ਵਿਸਤ੍ਰਿਤ ਦਸਤਾਵੇਜ਼**:
  - `SAMPLES_UPDATE_SUMMARY.md` ਬਣਾਇਆ - 400+ ਲਾਈਨਾਂ ਦੀ ਵਿਸਤ੍ਰਿਤ ਗਾਈਡ ਜੋ ਸਾਰੇ ਸੁਧਾਰਾਂ ਨੂੰ ਕਵਰ ਕਰਦੀ ਹੈ
  - `UPDATE_COMPLETE.md` ਬਣਾਇਆ - ਅਪਡੇਟ ਪੂਰਨ ਹੋਣ ਦੀ ਕਾਰਜਕਾਰੀ ਸੰਖੇਪ ਰਿਪੋਰਟ
  - `QUICK_REFERENCE.md` ਬਣਾਇਆ - ਵਰਕਸ਼ਾਪ ਲਈ ਤੁਰੰਤ ਸੰਦਰਭ ਕਾਰਡ

### ਬਦਲਿਆ - ਵਰਕਸ਼ਾਪ Python ਸੈਂਪਲ ਮਾਡਰਨਾਈਜ਼ੇਸ਼ਨ
- **ਸਾਰੇ 8 Python ਸੈਂਪਲਾਂ ਨੂੰ best practices ਨਾਲ ਅਪਡੇਟ ਕੀਤਾ**:
  - ਸਾਰੇ I/O ਕਾਰਵਾਈਆਂ ਦੇ ਆਸ-ਪਾਸ try-except blocks ਨਾਲ error handling ਨੂੰ ਵਧਾਇਆ
  - Type hints ਅਤੇ ਵਿਸਤ੍ਰਿਤ docstrings ਸ਼ਾਮਲ ਕੀਤੇ
  - [INFO]/[ERROR]/[RESULT] logging pattern ਨੂੰ ਲਗਾਤਾਰ ਲਾਗੂ ਕੀਤਾ
  - Installation hints ਦੇ ਨਾਲ optional imports ਨੂੰ ਸੁਰੱਖਿਅਤ ਕੀਤਾ
  - ਸਾਰੇ ਸੈਂਪਲਾਂ ਵਿੱਚ ਯੂਜ਼ਰ ਫੀਡਬੈਕ ਨੂੰ ਸੁਧਾਰਿਆ

- **session01/chat_bootstrap.py**:
  - Client initialization ਨੂੰ ਵਿਸਤ੍ਰਿਤ error messages ਦੇ ਨਾਲ ਸੁਧਾਰਿਆ
  - Streaming error handling ਨੂੰ chunk validation ਦੇ ਨਾਲ ਸੁਧਾਰਿਆ
  - Service unavailability ਲਈ ਬਿਹਤਰ exception handling ਸ਼ਾਮਲ ਕੀਤੀ

- **session02/rag_pipeline.py**:
  - Sentence-transformers ਲਈ import guards installation hints ਦੇ ਨਾਲ ਸ਼ਾਮਲ ਕੀਤੇ
  - Embedding ਅਤੇ generation ਕਾਰਵਾਈਆਂ ਲਈ error handling ਨੂੰ ਵਧਾਇਆ
  - Structured results ਦੇ ਨਾਲ output formatting ਨੂੰ ਸੁਧਾਰਿਆ

- **session02/rag_eval_ragas.py**:
  - Optional imports (ragas, datasets) ਨੂੰ ਯੂਜ਼ਰ-ਫ੍ਰੈਂਡਲੀ error messages ਦੇ ਨਾਲ ਸੁਰੱਖਿਅਤ ਕੀਤਾ
  - Evaluation metrics ਲਈ error handling ਸ਼ਾਮਲ ਕੀਤੀ
  - Evaluation results ਲਈ output formatting ਨੂੰ ਵਧਾਇਆ

- **session03/benchmark_oss_models.py**:
  - Graceful degradation ਲਾਗੂ ਕੀਤੀ (model failures ਤੇ ਕੰਮ ਜਾਰੀ ਰੱਖਦਾ ਹੈ)
  - ਵਿਸਤ੍ਰਿਤ progress reporting ਅਤੇ per-model error handling ਸ਼ਾਮਲ ਕੀਤੀ
  - Error recovery ਦੇ ਨਾਲ statistics calculation ਨੂੰ ਸੁਧਾਰਿਆ

- **session04/model_compare.py**:
  - Type hints (Tuple return types) ਸ਼ਾਮਲ ਕੀਤੇ
  - Structured JSON results ਦੇ ਨਾਲ output formatting ਨੂੰ ਵਧਾਇਆ
  - Per-model error handling ਨੂੰ recovery ਦੇ ਨਾਲ ਲਾਗੂ ਕੀਤਾ

- **session05/agents_orchestrator.py**:
  - Agent.act() ਨੂੰ ਵਿਸਤ੍ਰਿਤ docstrings ਦੇ ਨਾਲ ਸੁਧਾਰਿਆ
  - Stage-by-stage logging ਦੇ ਨਾਲ pipeline error handling ਸ਼ਾਮਲ ਕੀਤੀ
  - Memory management ਅਤੇ state tracking ਨੂੰ ਸੁਧਾਰਿਆ

- **session06/models_router.py**:
  - Routing components ਲਈ function documentation ਨੂੰ ਵਧਾਇਆ
  - route() function ਵਿੱਚ ਵਿਸਤ੍ਰਿਤ logging ਸ਼ਾਮਲ ਕੀਤੀ
  - Structured results ਦੇ ਨਾਲ test output ਨੂੰ ਸੁਧਾਰਿਆ

- **session06/models_pipeline.py**:
  - chat() helper function ਵਿੱਚ error handling ਸ਼ਾਮਲ ਕੀਤੀ
  - Stage logging ਅਤੇ progress reporting ਦੇ ਨਾਲ pipeline() ਨੂੰ ਸੁਧਾਰਿਆ
  - Comprehensive error recovery ਦੇ ਨਾਲ main() ਨੂੰ ਸੁਧਾਰਿਆ

### ਦਸਤਾਵੇਜ਼ - ਵਰਕਸ਼ਾਪ ਦਸਤਾਵੇਜ਼ ਸੁਧਾਰ
- ਮੁੱਖ README.md ਨੂੰ ਵਰਕਸ਼ਾਪ ਸੈਕਸ਼ਨ ਦੇ ਨਾਲ ਅਪਡੇਟ ਕੀਤਾ ਜੋ ਹੱਥ-ਅਨੁਭਵ ਸਿੱਖਣ ਦੇ ਰਾਹ ਨੂੰ ਹਾਈਲਾਈਟ ਕਰਦਾ ਹੈ
- STUDY_GUIDE.md ਨੂੰ ਵਿਸਤ੍ਰਿਤ ਵਰਕਸ਼ਾਪ ਸੈਕਸ਼ਨ ਦੇ ਨਾਲ ਸੁਧਾਰਿਆ ਜਿਸ ਵਿੱਚ ਸ਼ਾਮਲ ਹੈ:
  - ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼ ਅਤੇ ਅਧਿਐਨ ਫੋਕਸ ਖੇਤਰ
  - ਸਵੈ-ਮੁਲਾਂਕਣ ਪ੍ਰਸ਼ਨ
  - ਹੱਥ-ਅਨੁਭਵ ਅਭਿਆਸ ਸਮੇਂ ਦੇ ਅਨੁਮਾਨਾਂ ਦੇ ਨਾਲ
  - Concentrated ਅਤੇ part-time ਅਧਿਐਨ ਲਈ ਸਮੇਂ ਦਾ ਵੰਡ
  - ਪ੍ਰਗਤੀ ਟ੍ਰੈਕਿੰਗ ਟੈਂਪਲੇਟ ਵਿੱਚ ਵਰਕਸ਼ਾਪ ਸ਼ਾਮਲ ਕੀਤੀ
- ਸਮੇਂ ਦੇ ਵੰਡ ਗਾਈਡ ਨੂੰ 20 ਘੰਟਿਆਂ ਤੋਂ 30 ਘੰਟਿਆਂ (ਵਰਕਸ਼ਾਪ ਸਮੇਤ) ਵਿੱਚ ਅਪਡੇਟ ਕੀਤਾ
- README ਵਿੱਚ ਵਰਕਸ਼ਾਪ ਸੈਂਪਲ ਵੇਰਵੇ ਅਤੇ ਸਿੱਖਣ ਦੇ ਨਤੀਜੇ ਸ਼ਾਮਲ ਕੀਤੇ

### ਠੀਕ ਕੀਤਾ
- ਵਰਕਸ਼ਾਪ ਸੈਂਪਲਾਂ ਵਿੱਚ inconsistent error handling patterns ਨੂੰ ਹੱਲ ਕੀਤਾ
- Proper guards ਦੇ ਨਾਲ optional dependency import errors ਨੂੰ ਠੀਕ ਕੀਤਾ
- ਮਹੱਤਵਪੂਰਨ functions ਵਿੱਚ ਗੁੰਮ type hints ਨੂੰ ਠੀਕ ਕੀਤਾ
- Error scenarios ਵਿੱਚ ਯੂਜ਼ਰ ਫੀਡਬੈਕ ਦੀ ਘਾਟ ਨੂੰ ਹੱਲ ਕੀਤਾ
- Comprehensive testing infrastructure ਦੇ ਨਾਲ validation issues ਨੂੰ ਠੀਕ ਕੀਤਾ

---

## 2025-09-23

### ਬਦਲਿਆ - Module 08 ਦੀ ਮਜਬੂਤ ਮਾਡਰਨਾਈਜ਼ੇਸ਼ਨ
- **Microsoft Foundry-Local repository patterns ਨਾਲ ਪੂਰੀ ਤਰ੍ਹਾਂ ਅਨੁਕੂਲਤਾ**:
  - ਸਾਰੇ ਕੋਡ ਉਦਾਹਰਣਾਂ ਨੂੰ ਮਾਡਰਨ `FoundryLocalManager` ਅਤੇ OpenAI SDK ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਵਰਤਣ ਲਈ ਅਪਡੇਟ ਕੀਤਾ
  - Deprecated manual `requests` calls ਨੂੰ proper SDK usage ਨਾਲ ਬਦਲਿਆ
  - Microsoft ਦੀ ਅਧਿਕਾਰਕ ਦਸਤਾਵੇਜ਼ ਅਤੇ ਸੈਂਪਲਾਂ ਨਾਲ ਅਨੁਕੂਲਤਾ ਲਈ implementation patterns ਨੂੰ align ਕੀਤਾ

- **05.AIPoweredAgents.md ਮਜਬੂਤ ਬਣਾਈ**:
  - ਮਾਡਰਨ SDK patterns ਵਰਤਣ ਲਈ multi-agent orchestration ਨੂੰ ਅਪਡੇਟ ਕੀਤਾ
  - Feedback loops ਅਤੇ performance monitoring ਵਰਗੇ advanced features ਦੇ ਨਾਲ coordinator implementation ਨੂੰ ਸੁਧਾਰਿਆ
  - Comprehensive error handling ਅਤੇ service health checking ਸ਼ਾਮਲ ਕੀਤੀ
  - Local samples (`samples/05/multi_agent_orchestration.ipynb`) ਲਈ proper references ਸ਼ਾਮਲ ਕੀਤੇ
  - Deprecated `functions` ਦੀ ਬਜਾਏ ਮਾਡਰਨ `tools` parameter ਵਰਤਣ ਲਈ function calling examples ਨੂੰ ਅਪਡੇਟ ਕੀਤਾ
  - Monitoring ਅਤੇ statistics tracking ਦੇ ਨਾਲ production-ready patterns ਸ਼ਾਮਲ ਕੀਤੇ

- **06.ModelsAsTools.md ਦੀ ਪੂਰੀ ਤਰ੍ਹਾਂ ਮੁੜ ਲਿਖਤ**:
  - Basic tool registry ਨੂੰ intelligent model router implementation ਨਾਲ ਬਦਲਿਆ
  - ਵੱਖ-ਵੱਖ task types (general, reasoning, code, creative) ਲਈ keyword-based model selection ਸ਼ਾਮਲ ਕੀਤੀ
  - Flexible model assignment ਦੇ ਨਾਲ environment-based configuration ਸ਼ਾਮਲ ਕੀਤੀ
  - Comprehensive service health monitoring ਅਤੇ error handling ਦੇ ਨਾਲ ਸੁਧਾਰਿਆ
  - Request monitoring ਅਤੇ performance tracking ਦੇ ਨਾਲ production deployment patterns ਸ਼ਾਮਲ ਕੀਤੇ
  - Local implementation (`samples/06/router.py` ਅਤੇ `samples/06/model_router.ipynb`) ਨਾਲ ਅਨੁਕੂਲਤਾ

- **ਦਸਤਾਵੇਜ਼ ਢਾਂਚੇ ਵਿੱਚ ਸੁਧਾਰ**:
  - Modernization ਅਤੇ SDK alignment ਨੂੰ ਹਾਈਲਾਈਟ ਕਰਨ ਵਾਲੇ overview sections ਸ਼ਾਮਲ ਕੀਤੇ
  - Improved readability ਲਈ emojis ਅਤੇ ਬਿਹਤਰ formatting ਸ਼ਾਮਲ ਕੀਤੀ
  - Local sample files ਲਈ proper references ਸ਼ਾਮਲ ਕੀਤੇ
  - Production-ready implementation guidance ਅਤੇ best practices ਸ਼ਾਮਲ ਕੀਤੇ

### ਜੋੜਿਆ
- Module 08 ਫਾਈਲਾਂ ਵਿੱਚ modern SDK integration ਨੂੰ ਹਾਈਲਾਈਟ ਕਰਨ ਵਾਲੇ ਵਿਸਤ੍ਰਿਤ overview sections
- Multi-agent systems ਅਤੇ intelligent routing ਵਰਗੇ advanced features ਨੂੰ ਦਰਸਾਉਣ ਵਾਲੇ architecture highlights
- ਹੱਥ-ਅਨੁਭਵ ਲਈ local sample implementations ਲਈ direct references
- Monitoring ਅਤੇ error handling patterns ਦੇ ਨਾਲ production deployment guidance
- Advanced features ਅਤੇ benchmarks ਦੇ ਨਾਲ interactive Jupyter notebook examples

### ਠੀਕ ਕੀਤਾ
- Documentation ਅਤੇ actual sample implementations ਦੇ ਵਿਚਕਾਰ alignment discrepancies ਨੂੰ ਹੱਲ ਕੀਤਾ
- Module 08 ਵਿੱਚ outdated SDK usage patterns ਨੂੰ ਠੀਕ ਕੀਤਾ
- Comprehensive local sample library ਲਈ missing references ਨੂੰ ਠੀਕ ਕੀਤਾ
- ਵੱਖ-ਵੱਖ sections ਵਿੱਚ inconsistent implementation approaches ਨੂੰ ਹੱਲ ਕੀਤਾ

---

## 2025-09-18

### ਜੋੜਿਆ
- Module 08: Microsoft Foundry Local – Complete Developer Toolkit
  - ਛੇ sessions: setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, ਅਤੇ models-as-tools
  - `Module08/samples/01`–`06` ਦੇ ਹੇਠ runnable samples:
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart OpenAI/Foundry Local ਅਤੇ Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Session 2 SDK sample ਵਿੱਚ Azure OpenAI support ਅਤੇ environment variable configuration
- `.vscode/settings.json` ਨੂੰ `Module08/.venv` ਤੇ point ਕਰਨ ਲਈ ਅਤੇ Python analysis resolution ਨੂੰ ਸੁਧਾਰਨ ਲਈ
- `.env` ਵਿੱਚ `PYTHONPATH` hint VS Code/Pylance awareness ਲਈ

### ਬਦਲਿਆ
- Module 08 docs ਅਤੇ samples ਵਿੱਚ default model ਨੂੰ `phi-4-mini` ਵਿੱਚ ਅਪਡੇਟ ਕੀਤਾ; `phi-3.5` ਦੇ ਬਾਕੀ mentions ਨੂੰ ਹਟਾਇਆ
- Router (`Module08/samples/06/router.py`) ਸੁਧਾਰ:
  - Regex parsing ਦੇ ਨਾਲ `foundry service status` ਦੁਆਰਾ endpoint discovery
  - `/v1/models` health check startup ਤੇ
  - Env-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requirements ਅਪਡੇਟ ਕੀਤੇ: `Module08/requirements.txt` ਵਿੱਚ `openai` ਸ਼ਾਮਲ ਕੀਤਾ (ਸਾਥ `requests`, `chainlit`)
- Chainlit sample guidance ਨੂੰ ਸਪਸ਼ਟ ਕੀਤਾ ਅਤੇ troubleshooting ਸ਼ਾਮਲ ਕੀਤੀ; workspace settings ਦੁਆਰਾ import resolution

### ਠੀਕ ਕੀਤਾ
- Import issues ਹੱਲ ਕੀਤੇ:
  - Router ਹੁਣ non-existent `utils` module ਤੇ depend ਨਹੀਂ ਕਰਦਾ; functions inline ਕੀਤੇ
  - Coordinator relative import (`from .specialists import ...`) ਵਰਤਦਾ ਹੈ ਅਤੇ module path ਦੁਆਰਾ invoke ਹੁੰਦਾ ਹੈ
  - VS Code/Pylance configuration `chainlit` ਅਤੇ package imports ਨੂੰ resolve ਕਰਨ ਲਈ
- `STUDY_GUIDE.md` ਵਿੱਚ minor typo ਠੀਕ ਕੀਤਾ ਅਤੇ Module 08 coverage ਸ਼ਾਮਲ ਕੀਤੀ

### ਹਟਾਇਆ
- Unused `Module08/infra/obs.py` ਨੂੰ delete ਕੀਤਾ ਅਤੇ ਖਾਲੀ `infra/` ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਹਟਾਇਆ; observability patterns ਨੂੰ docs ਵਿੱਚ optional ਰੱਖਿਆ

### ਮੂਵ ਕੀਤਾ
- Module 08 demos ਨੂੰ `Module08/samples` ਦੇ session-numbered folders ਵਿੱਚ consolidate ਕੀਤਾ
  - Chainlit app ਨੂੰ `samples/04` ਵਿੱਚ ਮੂਵ ਕੀਤਾ
  - Agents ਨੂੰ `samples/05` ਵਿੱਚ ਮੂਵ ਕੀਤਾ ਅਤੇ package resolution ਲਈ `__init__.py` files ਸ਼ਾਮਲ ਕੀਤੇ

### ਦਸਤਾਵੇਜ਼
- Module 08 session docs ਅਤੇ ਸਾਰੇ sample READMEs enriched Microsoft Learn ਅਤੇ trusted vendor references ਦੇ ਨਾਲ
- `Module08/README.md` ਨੂੰ Samples Overview, router configuration, ਅਤੇ validation tips ਦੇ ਨਾਲ ਅਪਡੇਟ ਕੀਤਾ
- `Module07/README.md` Windows Foundry Local section Learn docs ਦੇ ਖਿਲਾਫ validated
- `STUDY_GUIDE.md` ਨੂੰ ਅਪਡੇਟ ਕੀਤਾ:
  - Module 08 ਨੂੰ overview, schedules, progress tracker ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤਾ
  - Comprehensive References section (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML) ਸ਼ਾਮਲ ਕੀਤੀ

---

## ਇਤਿਹਾਸਕ (ਸੰਖੇਪ)
- ਕੋਰਸ ਆਰਕੀਟੈਕਚਰ ਅਤੇ ਮੋਡਿਊਲਸ ਸਥਾਪਿਤ ਕੀਤੇ (Modules 01–07)
- Iterative content modernization, formatting standardization, ਅਤੇ case studies ਸ਼ਾਮਲ ਕੀਤੇ
- Optimization frameworks coverage (Llama.cpp, Olive, OpenVINO, Apple MLX) ਨੂੰ ਵਧਾਇਆ

## ਅਣਪ੍ਰਕਾਸ਼ਿਤ / ਬੈਕਲੌਗ (ਪ੍ਰਸਤਾਵ)
- Foundry Local availability ਨੂੰ validate ਕਰਨ ਲਈ optional per-sample smoke tests
- Model references (e.g., `phi-4-mini`) ਨੂੰ align ਕਰਨ ਲਈ translations ਦੀ ਸਮੀਖਿਆ
- Workspace-wide strictness ਲਈ minimal pyright config ਸ਼ਾਮਲ ਕਰਨ ਦੀ ਸਿਫਾਰਸ਼

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।