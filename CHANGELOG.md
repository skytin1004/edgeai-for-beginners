# Changelog

All notable changes to EdgeAI for Beginners are documented here. This project uses date-based entries and the Keep a Changelog style (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Complete Developer Toolkit
  - Six sessions: setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, and models-as-tools
  - Runnable samples under `Module08/samples/01`–`06` with Windows cmd instructions
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart with OpenAI/Foundry Local and Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI support in Session 2 SDK sample with environment variable configuration
- `.vscode/settings.json` to point to `Module08/.venv` and improve Python analysis resolution
- `.env` with `PYTHONPATH` hint for VS Code/Pylance awareness

### Changed
- Default model updated to `phi-4-mini` across Module 08 docs and samples; removed remaining `phi-3.5` mentions within Module 08
- Router (`Module08/samples/06/router.py`) improvements:
  - Endpoint discovery via `foundry service status` with regex parsing
  - `/v1/models` health check on startup
  - Env-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requirements updated: `Module08/requirements.txt` now includes `openai` (alongside `requests`, `chainlit`)
- Chainlit sample guidance clarified and troubleshooting added; import resolution via workspace settings

### Fixed
- Resolved import issues:
  - Router no longer depends on a non-existent `utils` module; functions are inlined
  - Coordinator uses relative import (`from .specialists import ...`) and is invoked via module path
  - VS Code/Pylance configuration to resolve `chainlit` and package imports
- Corrected minor typo in `STUDY_GUIDE.md` and added Module 08 coverage

### Removed
- Deleted unused `Module08/infra/obs.py` and removed the empty `infra/` directory; observability patterns retained as optional in docs

### Moved
- Consolidated Module 08 demos under `Module08/samples` with session-numbered folders
  - Moved Chainlit app to `samples/04`
  - Moved agents to `samples/05` and added `__init__.py` files for package resolution

### Docs
- Module 08 session docs and all sample READMEs enriched with Microsoft Learn and trusted vendor references
- `Module08/README.md` updated with Samples Overview, router configuration, and validation tips
- `Module07/README.md` Windows Foundry Local section validated against Learn docs
- `STUDY_GUIDE.md` updated:
  - Added Module 08 to overview, schedules, progress tracker
  - Added comprehensive References section (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historical (summary)
- Course architecture and modules established (Modules 01–07)
- Iterative content modernization, formatting standardization, and added case studies
- Expanded optimization frameworks coverage (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unreleased / Backlog (proposals)
- Optional per-sample smoke tests to validate Foundry Local availability
- Review translations to align model references (e.g., `phi-4-mini`) where appropriate
- Add minimal pyright config if teams prefer workspace-wide strictness
