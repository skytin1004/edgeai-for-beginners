<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T11:51:14+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "my"
}
-->
# Changelog

EdgeAI for Beginners တွင် အရေးပါသော ပြောင်းလဲမှုများအားလုံးကို ဒီမှာ မှတ်တမ်းတင်ထားပါသည်။ ဒီပရောဂျက်သည် ရက်စွဲအခြေခံ မှတ်တမ်းများနှင့် Keep a Changelog စတိုင် (Added, Changed, Fixed, Removed, Docs, Moved) ကို အသုံးပြုပါသည်။

## 2025-10-08

### Added - Workshop Comprehensive Update
- **Workshop README.md ပြန်ရေးဆွဲခြင်း**:
  - Edge AI ၏ အရေးပါမှု (privacy, performance, cost) ကို ရှင်းလင်းဖော်ပြထားသော အကျဉ်းချုပ်ကို ထည့်သွင်းထားသည်။
  - အသေးစိတ် ကျွမ်းကျင်မှုများနှင့် ၆ ခုသော အဓိက သင်ယူရမည့် ရည်မှန်းချက်များ ဖန်တီးထားသည်။
  - Deliverables နှင့် competency matrix ပါဝင်သော သင်ယူရလဒ်များဇယား ထည့်သွင်းထားသည်။
  - စက်မှုလုပ်ငန်းနှင့် သက်ဆိုင်သော ကျွမ်းကျင်မှုများအပိုင်း ထည့်သွင်းထားသည်။
  - Prerequisites နှင့် 3-step setup ပါဝင်သော အမြန်စတင်လမ်းညွှန် ထည့်သွင်းထားသည်။
  - Python samples (8 ဖိုင်များနှင့် run times) အတွက် အရင်းအမြစ်ဇယား ဖန်တီးထားသည်။
  - Jupyter notebooks (8 notebooks နှင့် အခက်အခဲအဆင့်များ) အတွက် ဇယား ထည့်သွင်းထားသည်။
  - Documentation table (7 key docs နှင့် "Use When" လမ်းညွှန်) ဖန်တီးထားသည်။
  - အတတ်ပညာအဆင့်အလိုက် သင်ယူလမ်းကြောင်း အကြံပြုချက်များ ထည့်သွင်းထားသည်။

- **Workshop validation နှင့် testing infrastructure**:
  - `scripts/validate_samples.py` ဖိုင် ဖန်တီးထားသည် - Syntax, imports, နှင့် best practices အတွက် validation tool
  - `scripts/test_samples.py` ဖိုင် ဖန်တီးထားသည် - Python samples အားလုံးအတွက် smoke test runner
  - Validation documentation ကို `scripts/README.md` တွင် ထည့်သွင်းထားသည်။

- **Comprehensive documentation**:
  - `SAMPLES_UPDATE_SUMMARY.md` ဖိုင် ဖန်တီးထားသည် - 400+ လိုင်းပါဝင်သော အပြည့်အစုံလမ်းညွှန်
  - `UPDATE_COMPLETE.md` ဖိုင် ဖန်တီးထားသည် - Update ပြီးစီးမှုအကျဉ်းချုပ်
  - `QUICK_REFERENCE.md` ဖိုင် ဖန်တီးထားသည် - Workshop အတွက် အမြန်လမ်းညွှန်ကဒ်

### Changed - Workshop Python Sample Modernization
- **Python samples ၈ ခုအား Best Practices ဖြင့် ပြုပြင်ထားသည်**:
  - Error handling ကို try-except blocks ဖြင့် တိုးတက်စေထားသည်။
  - Type hints နှင့် docstrings အပြည့်အစုံ ထည့်သွင်းထားသည်။
  - [INFO]/[ERROR]/[RESULT] logging pattern ကို တစ်စည်းတစ်လုံးဖြစ်စေထားသည်။
  - Optional imports ကို installation hints ဖြင့် ကာကွယ်ထားသည်။
  - User feedback ကို အားလုံးသော samples တွင် တိုးတက်စေထားသည်။

- **session01/chat_bootstrap.py**:
  - Client initialization ကို error messages အပြည့်အစုံဖြင့် တိုးတက်စေထားသည်။
  - Streaming error handling ကို chunk validation ဖြင့် တိုးတက်စေထားသည်။
  - Service မရရှိနိုင်မှုအတွက် exception handling ကို တိုးတက်စေထားသည်။

- **session02/rag_pipeline.py**:
  - Sentence-transformers အတွက် import guards နှင့် installation hints ထည့်သွင်းထားသည်။
  - Embedding နှင့် generation operations အတွက် error handling တိုးတက်စေထားသည်။
  - Structured results ဖြင့် output formatting တိုးတက်စေထားသည်။

- **session02/rag_eval_ragas.py**:
  - Optional imports (ragas, datasets) ကို user-friendly error messages ဖြင့် ကာကွယ်ထားသည်။
  - Evaluation metrics အတွက် error handling ထည့်သွင်းထားသည်။
  - Evaluation results အတွက် output formatting တိုးတက်စေထားသည်။

- **session03/benchmark_oss_models.py**:
  - Model failures ဖြစ်ပေါ်ပါက graceful degradation ကို အကောင်အထည်ဖော်ထားသည်။
  - Progress reporting နှင့် per-model error handling ကို တိုးတက်စေထားသည်။
  - Statistics calculation ကို error recovery ဖြင့် တိုးတက်စေထားသည်။

- **session04/model_compare.py**:
  - Type hints (Tuple return types) ထည့်သွင်းထားသည်။
  - Structured JSON results ဖြင့် output formatting တိုးတက်စေထားသည်။
  - Per-model error handling ကို recovery ဖြင့် တိုးတက်စေထားသည်။

- **session05/agents_orchestrator.py**:
  - Agent.act() ကို docstrings အပြည့်အစုံဖြင့် တိုးတက်စေထားသည်။
  - Pipeline error handling ကို stage-by-stage logging ဖြင့် တိုးတက်စေထားသည်။
  - Memory management နှင့် state tracking ကို တိုးတက်စေထားသည်။

- **session06/models_router.py**:
  - Routing components အားလုံးအတွက် function documentation တိုးတက်စေထားသည်။
  - route() function တွင် logging အသေးစိတ် ထည့်သွင်းထားသည်။
  - Test output ကို structured results ဖြင့် တိုးတက်စေထားသည်။

- **session06/models_pipeline.py**:
  - chat() helper function တွင် error handling ထည့်သွင်းထားသည်။
  - pipeline() တွင် stage logging နှင့် progress reporting တိုးတက်စေထားသည်။
  - main() တွင် error recovery အပြည့်အစုံ ထည့်သွင်းထားသည်။

### Docs - Workshop Documentation Enhancement
- Main README.md ကို Workshop အပိုင်းနှင့် hands-on learning path ကို အထူးပြုလုပ်ထားသည်။
- STUDY_GUIDE.md ကို Workshop အပိုင်းနှင့် အပြည့်အစုံ ပြုပြင်ထားသည်။
  - Learning objectives နှင့် study focus areas
  - Self-assessment questions
  - Hands-on exercises နှင့် အချိန်ခန့်မှန်းချက်များ
  - Concentrated နှင့် part-time study အတွက် အချိန် allocation
  - Workshop ကို progress tracking template တွင် ထည့်သွင်းထားသည်။
- အချိန် allocation guide ကို 20 နာရီမှ 30 နာရီ (Workshop အပါအဝင်) အဖြစ် ပြောင်းလဲထားသည်။
- Workshop sample descriptions နှင့် learning outcomes ကို README တွင် ထည့်သွင်းထားသည်။

### Fixed
- Workshop samples များတွင် error handling patterns မညီညွတ်မှုများကို ဖြေရှင်းထားသည်။
- Optional dependency import errors ကို guards ဖြင့် ပြုပြင်ထားသည်။
- Critical functions တွင် မရှိသေးသော type hints များကို ဖြည့်စွက်ထားသည်။
- Error scenarios တွင် user feedback မလုံလောက်မှုကို ဖြေရှင်းထားသည်။
- Validation issues များကို testing infrastructure ဖြင့် ပြုပြင်ထားသည်။

---

## 2025-09-23

### Changed - Major Module 08 Modernization
- **Microsoft Foundry-Local repository patterns နှင့် အပြည့်အစုံကို လိုက်လျောညီထွေစေထားသည်**:
  - Modern `FoundryLocalManager` နှင့် OpenAI SDK integration ကို အသုံးပြုရန် code examples အားလုံးကို ပြုပြင်ထားသည်။
  - Manual `requests` calls များကို SDK usage ဖြင့် အစားထိုးထားသည်။
  - Microsoft documentation နှင့် samples တရားဝင်အတိုင်း implementation patterns ကို လိုက်လျောညီထွေစေထားသည်။

- **05.AIPoweredAgents.md modernization**:
  - Multi-agent orchestration ကို modern SDK patterns ဖြင့် ပြုပြင်ထားသည်။
  - Coordinator implementation ကို feedback loops နှင့် performance monitoring တို့ဖြင့် တိုးတက်စေထားသည်။
  - Error handling နှင့် service health checking ကို ထည့်သွင်းထားသည်။
  - Local samples (`samples/05/multi_agent_orchestration.ipynb`) ကို မှန်ကန်စွာ ရည်ညွှန်းထားသည်။
  - Function calling examples ကို modern `tools` parameter အသုံးပြုရန် ပြောင်းလဲထားသည်။
  - Monitoring နှင့် statistics tracking ဖြင့် production-ready patterns ထည့်သွင်းထားသည်။

- **06.ModelsAsTools.md complete rewrite**:
  - Basic tool registry ကို intelligent model router implementation ဖြင့် အစားထိုးထားသည်။
  - General, reasoning, code, creative tasks များအတွက် keyword-based model selection ထည့်သွင်းထားသည်။
  - Flexible model assignment ဖြင့် environment-based configuration ထည့်သွင်းထားသည်။
  - Service health monitoring နှင့် error handling ကို တိုးတက်စေထားသည်။
  - Request monitoring နှင့် performance tracking ဖြင့် production deployment patterns ထည့်သွင်းထားသည်။
  - Local implementation (`samples/06/router.py` နှင့် `samples/06/model_router.ipynb`) နှင့် လိုက်လျောညီထွေစေထားသည်။

- **Documentation structure improvements**:
  - Modernization နှင့် SDK alignment ကို အကျဉ်းချုပ်ဖော်ပြထားသော overview sections ထည့်သွင်းထားသည်။
  - Emojis နှင့် formatting တိုးတက်စေထားသည်။
  - Local sample files ကို မှန်ကန်စွာ ရည်ညွှန်းထားသည်။
  - Production-ready implementation guidance နှင့် best practices ထည့်သွင်းထားသည်။

### Added
- Module 08 files တွင် modern SDK integration ကို အကျဉ်းချုပ်ဖော်ပြထားသော overview sections
- Multi-agent systems နှင့် intelligent routing တို့ကို ဖော်ပြထားသော architecture highlights
- Local sample implementations ကို ရည်ညွှန်းထားသော hands-on experience
- Monitoring နှင့် error handling patterns ဖြင့် production deployment guidance
- Advanced features နှင့် benchmarks ပါဝင်သော interactive Jupyter notebook examples

### Fixed
- Documentation နှင့် actual sample implementations အကြား alignment discrepancies များကို ဖြေရှင်းထားသည်။
- Module 08 တွင် outdated SDK usage patterns များကို ပြုပြင်ထားသည်။
- Comprehensive local sample library ကို ရည်ညွှန်းမှုမရှိမှုကို ဖြေရှင်းထားသည်။
- Implementation approaches မညီညွတ်မှုများကို ပြုပြင်ထားသည်။

---

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Complete Developer Toolkit
  - Setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, နှင့် models-as-tools စသည့် sessions ၆ ခု
  - `Module08/samples/01`–`06` အောက်တွင် runnable samples:
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart with OpenAI/Foundry Local နှင့် Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Session 2 SDK sample တွင် Azure OpenAI support နှင့် environment variable configuration
- `.vscode/settings.json` ကို `Module08/.venv` သို့ point ပြုလုပ်ထားသည်။
- `.env` ကို `PYTHONPATH` hint ဖြင့် VS Code/Pylance awareness အတွက် ထည့်သွင်းထားသည်။

### Changed
- Module 08 docs နှင့် samples တွင် default model ကို `phi-4-mini` အဖြစ် ပြောင်းလဲထားသည်။
- Router (`Module08/samples/06/router.py`) တိုးတက်စေထားသည်:
  - Endpoint discovery ကို `foundry service status` နှင့် regex parsing ဖြင့် ပြုလုပ်ထားသည်။
  - Startup တွင် `/v1/models` health check
  - Env-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requirements (`Module08/requirements.txt`) တွင် `openai` ကို ထည့်သွင်းထားသည်။
- Chainlit sample guidance ကို ရှင်းလင်းစွာ ဖော်ပြထားသည်။

### Fixed
- Import issues များကို ဖြေရှင်းထားသည်:
  - Router သည် မရှိသေးသော `utils` module ကို မလိုအပ်တော့ပါ။
  - Coordinator သည် relative import (`from .specialists import ...`) ကို အသုံးပြုထားသည်။
  - VS Code/Pylance configuration ကို `chainlit` နှင့် package imports အတွက် ပြုပြင်ထားသည်။
- `STUDY_GUIDE.md` တွင် typo များကို ဖြေရှင်းထားပြီး Module 08 coverage ထည့်သွင်းထားသည်။

### Removed
- မအသုံးပြုသော `Module08/infra/obs.py` ကို ဖျက်ထားပြီး `infra/` directory ကို ဖယ်ရှားထားသည်။

### Moved
- Module 08 demos များကို `Module08/samples` အောက်တွင် session-numbered folders အဖြစ် ပြောင်းထားသည်။
  - Chainlit app ကို `samples/04` သို့ ပြောင်းထားသည်။
  - Agents ကို `samples/05` သို့ ပြောင်းထားပြီး `__init__.py` files ထည့်သွင်းထားသည်။

### Docs
- Module 08 session docs နှင့် sample READMEs များကို Microsoft Learn နှင့် trusted vendor references ဖြင့် ပြုပြင်ထားသည်။
- `Module08/README.md` ကို Samples Overview, router configuration, နှင့် validation tips ဖြင့် ပြုပြင်ထားသည်။
- `Module07/README.md` Windows Foundry Local အပိုင်းကို Learn docs နှင့် validated ပြုလုပ်ထားသည်။
- `STUDY_GUIDE.md` ကို ပြုပြင်ထားသည်:
  - Module 08 ကို overview, schedules, progress tracker တွင် ထည့်သွင်းထားသည်။
  - Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML စသည့် References အပိုင်း ထည့်သွင်းထားသည်။

---

## Historical (summary)
- Course architecture နှင့် modules (Modules 01–07) ကို တည်ဆောက်ထားသည်။
- Iterative content modernization, formatting standardization, နှင့် case studies ထည့်သွင်းထားသည်။
- Optimization frameworks (Llama.cpp, Olive, OpenVINO, Apple MLX) coverage တိုးချဲ့ထားသည်။

## Unreleased / Backlog (proposals)
- Foundry Local availability ကို validate ပြုလုပ်ရန် per-sample smoke tests ကို optional အဖြစ် ထည့်သွင်းရန်။
- Model references (e.g., `phi-4-mini`) ကို align ပြုလုပ်ရန် translation များကို ပြန်လည်သုံးသပ်ရန်။
- Workspace-wide strictness အတွက် minimal pyright config ထည့်သွင်းရန်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပာယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။