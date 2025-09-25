<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T02:14:09+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "my"
}
-->
# Changelog

EdgeAI for Beginners တွင် အရေးပါသော ပြောင်းလဲမှုများအားလုံးကို ဒီမှာ မှတ်တမ်းတင်ထားသည်။ ဒီပရောဂျက်သည် ရက်စွဲအခြေခံ မှတ်တမ်းများနှင့် Keep a Changelog စတိုင် (Added, Changed, Fixed, Removed, Docs, Moved) ကို အသုံးပြုသည်။

## 2025-09-23

### Changed - Module 08 အဓိက ပြုပြင်မွမ်းမံမှု
- **Microsoft Foundry-Local repository ပုံစံများနှင့် လိုက်လျောညီထွေမှု**
  - `FoundryLocalManager` နှင့် OpenAI SDK ပေါင်းစပ်မှုကို အသုံးပြုရန် code နမူနာများအားလုံးကို ပြုပြင်ခဲ့သည်
  - ရှေးဦးစွာ အသုံးပြုခဲ့သော `requests` ကို SDK အသုံးပြုမှုဖြင့် အစားထိုးခဲ့သည်
  - Microsoft documentation နှင့် နမူနာများနှင့် လိုက်လျောညီထွေမှုကို အကောင်အထည်ဖော်ခဲ့သည်

- **05.AIPoweredAgents.md ပြုပြင်မွမ်းမံမှု**:
  - SDK ပုံစံများအသုံးပြုသော multi-agent orchestration ကို ပြုပြင်ခဲ့သည်
  - feedback loops နှင့် performance monitoring စသည်တို့ဖြင့် coordinator ကို အဆင့်မြှင့်တင်ခဲ့သည်
  - error handling နှင့် service health checking ကို ထည့်သွင်းခဲ့သည်
  - `samples/05/multi_agent_orchestration.ipynb` တွင် နမူနာများကို ရည်ညွှန်းခဲ့သည်
  - `tools` parameter ကို အသုံးပြုရန် function calling နမူနာများကို ပြုပြင်ခဲ့သည်
  - monitoring နှင့် statistics tracking ပါဝင်သော production-ready patterns ကို ထည့်သွင်းခဲ့သည်

- **06.ModelsAsTools.md ပြန်ရေးသားမှု**:
  - basic tool registry ကို intelligent model router ဖြင့် အစားထိုးခဲ့သည်
  - general, reasoning, code, creative စသည်တို့အတွက် keyword-based model selection ကို ထည့်သွင်းခဲ့သည်
  - environment-based configuration ဖြင့် flexible model assignment ကို ထည့်သွင်းခဲ့သည်
  - service health monitoring နှင့် error handling ကို အဆင့်မြှင့်တင်ခဲ့သည်
  - request monitoring နှင့် performance tracking ပါဝင်သော production deployment patterns ကို ထည့်သွင်းခဲ့သည်
  - `samples/06/router.py` နှင့် `samples/06/model_router.ipynb` တွင် နေရာအလိုက် လိုက်လျောညီထွေမှုကို ပြုလုပ်ခဲ့သည်

- **Documentation ဖွဲ့စည်းမှု အဆင့်မြှင့်တင်မှု**:
  - modernization နှင့် SDK alignment ကို အထူးပြောထားသော overview အပိုင်းများကို ထည့်သွင်းခဲ့သည်
  - emojis နှင့် ပိုမိုကောင်းမွန်သော formatting ဖြင့် readability ကို မြှင့်တင်ခဲ့သည်
  - documentation အတွင်း sample files ကို ရည်ညွှန်းမှုများ ထည့်သွင်းခဲ့သည်
  - production-ready implementation guidance နှင့် best practices ကို ထည့်သွင်းခဲ့သည်

### Added
- Module 08 ဖိုင်များတွင် modern SDK integration ကို အထူးပြောထားသော overview အပိုင်းများ
- multi-agent systems နှင့် intelligent routing စသည်တို့ပါဝင်သော architecture highlights
- local sample implementations ကို တိုက်ရိုက် ရည်ညွှန်းမှုများ
- monitoring နှင့် error handling patterns ပါဝင်သော production deployment guidance
- advanced features နှင့် benchmarks ပါဝင်သော interactive Jupyter notebook နမူနာများ

### Fixed
- documentation နှင့် sample implementations အကြား alignment မတူညီမှုများ
- Module 08 အတွင်း outdated SDK usage patterns
- comprehensive local sample library ကို ရည်ညွှန်းမှု မပါဝင်မှု
- အပိုင်းများအကြား inconsistent implementation approaches

---

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Developer Toolkit အပြည့်အစုံ
  - setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, models-as-tools စသည်တို့ပါဝင်သော session ခြောက်ခု
  - `Module08/samples/01`–`06` အတွင်း runnable samples
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart with OpenAI/Foundry Local နှင့် Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Session 2 SDK sample တွင် Azure OpenAI support နှင့် environment variable configuration
- `.vscode/settings.json` ကို `Module08/.venv` ကို ရည်ညွှန်းရန် ထည့်သွင်းခဲ့သည်
- `.env` တွင် `PYTHONPATH` hint ကို VS Code/Pylance awareness အတွက် ထည့်သွင်းခဲ့သည်

### Changed
- Module 08 docs နှင့် samples အတွင်း default model ကို `phi-4-mini` သို့ ပြောင်းလဲခဲ့သည်; `phi-3.5` mentions များကို ဖယ်ရှားခဲ့သည်
- Router (`Module08/samples/06/router.py`) အဆင့်မြှင့်တင်မှု:
  - `foundry service status` ဖြင့် endpoint discovery
  - `/v1/models` health check ကို startup အတွင်း ပြုလုပ်ခဲ့သည်
  - Env-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requirements ကို ပြုပြင်ခဲ့သည်: `Module08/requirements.txt` တွင် `openai` ကို ထည့်သွင်းခဲ့သည် (`requests`, `chainlit` နှင့်အတူ)
- Chainlit sample guidance ကို ရှင်းလင်းခဲ့ပြီး troubleshooting ကို ထည့်သွင်းခဲ့သည်; workspace settings ဖြင့် import resolution

### Fixed
- Import ပြဿနာများကို ဖြေရှင်းခဲ့သည်:
  - Router သည် မရှိသော `utils` module ကို မလိုအပ်တော့ဘဲ functions များကို inline ပြုလုပ်ခဲ့သည်
  - Coordinator သည် relative import (`from .specialists import ...`) ကို အသုံးပြုခဲ့ပြီး module path ဖြင့် invoke ပြုလုပ်ခဲ့သည်
  - VS Code/Pylance configuration ကို `chainlit` နှင့် package imports ကို ဖြေရှင်းရန် ပြုလုပ်ခဲ့သည်
- `STUDY_GUIDE.md` တွင် အနည်းငယ်သော typo ကို ပြင်ခဲ့ပြီး Module 08 coverage ကို ထည့်သွင်းခဲ့သည်

### Removed
- မအသုံးပြုသော `Module08/infra/obs.py` ကို ဖယ်ရှားခဲ့ပြီး `infra/` directory ကို ဖျက်ခဲ့သည်; observability patterns ကို docs အတွင်း optional အဖြစ် ထားရှိခဲ့သည်

### Moved
- Module 08 demos များကို `Module08/samples` အတွင်း session-numbered folders အဖြစ် ပြောင်းရွှေ့ခဲ့သည်
  - Chainlit app ကို `samples/04` သို့ ပြောင်းရွှေ့ခဲ့သည်
  - agents များကို `samples/05` သို့ ပြောင်းရွှေ့ခဲ့ပြီး package resolution အတွက် `__init__.py` files ထည့်သွင်းခဲ့သည်

### Docs
- Module 08 session docs နှင့် sample READMEs များကို Microsoft Learn နှင့် trusted vendor references ဖြင့် အဆင့်မြှင့်တင်ခဲ့သည်
- `Module08/README.md` ကို Samples Overview, router configuration, validation tips ဖြင့် ပြုပြင်ခဲ့သည်
- `Module07/README.md` Windows Foundry Local အပိုင်းကို Learn docs နှင့် validated ပြုလုပ်ခဲ့သည်
- `STUDY_GUIDE.md` ကို ပြုပြင်ခဲ့သည်:
  - Module 08 ကို overview, schedules, progress tracker အတွင်း ထည့်သွင်းခဲ့သည်
  - Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML စသည်တို့ပါဝင်သော References အပိုင်းကို ထည့်သွင်းခဲ့သည်

---

## Historical (summary)
- Course architecture နှင့် modules (Modules 01–07) ကို တည်ဆောက်ခဲ့သည်
- Iterative content modernization, formatting standardization, case studies ထည့်သွင်းမှု
- Optimization frameworks (Llama.cpp, Olive, OpenVINO, Apple MLX) coverage ကို တိုးချဲ့ခဲ့သည်

## Unreleased / Backlog (proposals)
- Foundry Local availability ကို validate ပြုလုပ်ရန် per-sample smoke tests ကို optional အဖြစ် ထည့်သွင်းရန်
- Model references (ဥပမာ `phi-4-mini`) နှင့် alignment ပြုလုပ်ရန် translation များကို ပြန်လည်သုံးသပ်ရန်
- Workspace-wide strictness အတွက် pyright config အနည်းငယ် ထည့်သွင်းရန်

---

