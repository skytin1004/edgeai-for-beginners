<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-23T00:46:07+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "my"
}
-->
# Changelog

EdgeAI for Beginners တွင် အရေးပါသော ပြောင်းလဲမှုများအားလုံးကို ဒီနေရာတွင် မှတ်တမ်းတင်ထားသည်။ ဒီပရောဂျက်သည် ရက်စွဲအခြေခံ မှတ်တမ်းများနှင့် Keep a Changelog စတိုင် (Added, Changed, Fixed, Removed, Docs, Moved) ကို အသုံးပြုသည်။

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Developer Toolkit အပြည့်အစုံ
  - Sessions ခြောက်ခု: setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, နှင့် models-as-tools
  - `Module08/samples/01`–`06` အောက်တွင် Windows cmd အညွှန်းများနှင့် runnable samples
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart with OpenAI/Foundry Local နှင့် Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Session 2 SDK sample တွင် Azure OpenAI support နှင့် environment variable configuration
- `.vscode/settings.json` ကို `Module08/.venv` ကိုညွှန်းရန်နှင့် Python analysis resolution ကိုတိုးတက်စေရန်
- `.env` တွင် VS Code/Pylance awareness အတွက် `PYTHONPATH` hint

### Changed
- Module 08 docs နှင့် samples အတွင်း `phi-4-mini` ကို default model အဖြစ် update လုပ်ပြီး `phi-3.5` mentions များကို ဖယ်ရှားခဲ့သည်
- Router (`Module08/samples/06/router.py`) အဆင့်မြှင့်တင်မှုများ:
  - `foundry service status` ကို regex parsing ဖြင့် endpoint discovery
  - `/v1/models` health check ကို startup မှာ run
  - Env-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requirements update: `Module08/requirements.txt` တွင် `openai` ကိုထည့်သွင်းပြီး (`requests`, `chainlit` နှင့်အတူ)
- Chainlit sample အညွှန်းများကိုရှင်းလင်းပြီး troubleshooting ထည့်သွင်း; workspace settings ဖြင့် import resolution

### Fixed
- Import ပြဿနာများကို ဖြေရှင်းခဲ့သည်:
  - Router သည် မရှိသော `utils` module ကို မလိုအပ်တော့ဘဲ functions များကို inline လုပ်ထားသည်
  - Coordinator သည် relative import (`from .specialists import ...`) ကိုအသုံးပြုပြီး module path မှာ run
  - VS Code/Pylance configuration ကို `chainlit` နှင့် package imports ကို resolve လုပ်ရန်
- `STUDY_GUIDE.md` တွင် အနည်းငယ်သော typo ကိုပြင်ပြီး Module 08 coverage ထည့်သွင်း

### Removed
- မအသုံးပြုသော `Module08/infra/obs.py` ကိုဖျက်ပြီး `infra/` directory ကိုလည်းဖယ်ရှားခဲ့သည်; observability patterns များကို docs တွင် optional အဖြစ်ထားရှိ

### Moved
- Module 08 demos များကို `Module08/samples` အောက်တွင် session-numbered folders အဖြစ်စုစည်း
  - Chainlit app ကို `samples/04` သို့ရွှေ့
  - Agents များကို `samples/05` သို့ရွှေ့ပြီး package resolution အတွက် `__init__.py` files ထည့်သွင်း

### Docs
- Module 08 session docs နှင့် sample READMEs များကို Microsoft Learn နှင့် trusted vendor references ဖြင့်ချဲ့ထွင်
- `Module08/README.md` ကို Samples Overview, router configuration, နှင့် validation tips ဖြင့် update
- `Module07/README.md` Windows Foundry Local အပိုင်းကို Learn docs နှင့် validate
- `STUDY_GUIDE.md` ကို update:
  - Module 08 ကို overview, schedules, progress tracker တွင်ထည့်သွင်း
  - References အပိုင်းကို Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML ဖြင့်ပြည့်စုံစေ

---

## Historical (summary)
- Course architecture နှင့် modules များကိုတည်ဆောက် (Modules 01–07)
- Iterative content modernization, formatting standardization, နှင့် case studies ထည့်သွင်း
- Optimization frameworks coverage (Llama.cpp, Olive, OpenVINO, Apple MLX) ကိုချဲ့ထွင်

## Unreleased / Backlog (proposals)
- Foundry Local availability ကို validate လုပ်ရန် optional per-sample smoke tests
- Model references (ဥပမာ `phi-4-mini`) နှင့် alignment ရှိရန် translations ကိုပြန်လည်သုံးသပ်
- Workspace-wide strictness ကို prefer လုပ်ပါက minimal pyright config ထည့်သွင်း

---

