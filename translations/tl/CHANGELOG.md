<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T22:34:26+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "tl"
}
-->
# Changelog

Ang lahat ng mahahalagang pagbabago sa EdgeAI for Beginners ay dokumentado dito. Ang proyektong ito ay gumagamit ng mga entry na nakabase sa petsa at ang estilo ng Keep a Changelog (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Kumpletong Toolkit para sa Developer
  - Anim na sesyon: setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, at models-as-tools
  - Mga sample na maaaring patakbuhin sa ilalim ng `Module08/samples/01`–`06` na may mga tagubilin para sa Windows cmd
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart gamit ang OpenAI/Foundry Local at Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI support sa Session 2 SDK sample na may configuration ng environment variable
- `.vscode/settings.json` para ituro sa `Module08/.venv` at mapabuti ang Python analysis resolution
- `.env` na may `PYTHONPATH` hint para sa VS Code/Pylance awareness

### Changed
- Default model na-update sa `phi-4-mini` sa lahat ng Module 08 docs at samples; tinanggal ang natitirang mga banggit sa `phi-3.5` sa loob ng Module 08
- Mga pagpapabuti sa Router (`Module08/samples/06/router.py`):
  - Endpoint discovery gamit ang `foundry service status` na may regex parsing
  - `/v1/models` health check sa startup
  - Env-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Mga requirements na-update: `Module08/requirements.txt` ngayon ay kasama ang `openai` (kasama ang `requests`, `chainlit`)
- Paliwanag sa Chainlit sample guidance at troubleshooting na idinagdag; import resolution gamit ang workspace settings

### Fixed
- Naresolba ang mga isyu sa import:
  - Ang Router ay hindi na umaasa sa isang hindi umiiral na `utils` module; ang mga function ay in-line na
  - Ang Coordinator ay gumagamit ng relative import (`from .specialists import ...`) at pinapatakbo gamit ang module path
  - VS Code/Pylance configuration para ma-resolve ang `chainlit` at mga package imports
- Naayos ang maliit na typo sa `STUDY_GUIDE.md` at idinagdag ang Module 08 coverage

### Removed
- Tinanggal ang hindi nagagamit na `Module08/infra/obs.py` at tinanggal ang walang laman na `infra/` directory; ang mga observability patterns ay nanatiling opsyonal sa docs

### Moved
- Pinagsama-sama ang Module 08 demos sa ilalim ng `Module08/samples` na may mga folder na naka-base sa session number
  - Inilipat ang Chainlit app sa `samples/04`
  - Inilipat ang agents sa `samples/05` at idinagdag ang mga `__init__.py` files para sa package resolution

### Docs
- Ang mga dokumento ng Module 08 session at lahat ng sample READMEs ay pinayaman ng Microsoft Learn at mga pinagkakatiwalaang vendor references
- `Module08/README.md` na-update na may Samples Overview, router configuration, at validation tips
- `Module07/README.md` Windows Foundry Local section na-validate laban sa Learn docs
- `STUDY_GUIDE.md` na-update:
  - Idinagdag ang Module 08 sa overview, schedules, progress tracker
  - Idinagdag ang komprehensibong References section (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historical (summary)
- Na-establish ang course architecture at mga module (Modules 01–07)
- Iterative na modernisasyon ng content, standardisasyon ng formatting, at idinagdag ang mga case studies
- Pinalawak ang saklaw ng optimization frameworks (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unreleased / Backlog (proposals)
- Opsyonal na per-sample smoke tests para i-validate ang Foundry Local availability
- Review ng mga translation para i-align ang mga model references (hal., `phi-4-mini`) kung naaangkop
- Magdagdag ng minimal pyright config kung mas gusto ng mga team ang workspace-wide strictness

---

