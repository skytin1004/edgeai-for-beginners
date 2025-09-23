<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-23T00:44:05+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "en"
}
-->
# Changelog

All significant updates to EdgeAI for Beginners are recorded here. This project uses date-based entries and follows the Keep a Changelog format (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Complete Developer Toolkit
  - Six sessions: setup, Azure AI Foundry integration, open-source models, advanced demos, agents, and models-as-tools
  - Runnable examples located in `Module08/samples/01`–`06` with Windows cmd instructions
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart with OpenAI/Foundry Local and Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI support added to Session 2 SDK sample with environment variable configuration
- `.vscode/settings.json` updated to point to `Module08/.venv` for improved Python analysis resolution
- `.env` file added with `PYTHONPATH` hint for better VS Code/Pylance integration

### Changed
- Default model updated to `phi-4-mini` across Module 08 documentation and samples; removed remaining references to `phi-3.5` within Module 08
- Router (`Module08/samples/06/router.py`) enhancements:
  - Endpoint discovery using `foundry service status` with regex parsing
  - `/v1/models` health check during startup
  - Environment-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requirements updated: `Module08/requirements.txt` now includes `openai` (alongside `requests`, `chainlit`)
- Chainlit sample instructions clarified with added troubleshooting; import resolution improved via workspace settings

### Fixed
- Resolved import issues:
  - Router no longer relies on a non-existent `utils` module; functions are now inlined
  - Coordinator uses relative imports (`from .specialists import ...`) and is executed via module path
  - VS Code/Pylance configuration updated to resolve `chainlit` and package imports
- Corrected minor typo in `STUDY_GUIDE.md` and added Module 08 coverage

### Removed
- Deleted unused `Module08/infra/obs.py` and removed the empty `infra/` directory; observability patterns retained as optional in documentation

### Moved
- Consolidated Module 08 demos under `Module08/samples` with session-numbered folders
  - Moved Chainlit app to `samples/04`
  - Moved agents to `samples/05` and added `__init__.py` files for package resolution

### Docs
- Module 08 session documentation and all sample READMEs enriched with references to Microsoft Learn and trusted vendors
- `Module08/README.md` updated with Samples Overview, router configuration, and validation tips
- `Module07/README.md` Windows Foundry Local section validated against Learn documentation
- `STUDY_GUIDE.md` updated:
  - Added Module 08 to overview, schedules, and progress tracker
  - Expanded References section (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historical (summary)
- Course structure and modules established (Modules 01–07)
- Iterative updates for content modernization, formatting consistency, and added case studies
- Expanded coverage of optimization frameworks (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unreleased / Backlog (proposals)
- Optional smoke tests for each sample to validate Foundry Local availability
- Review translations to ensure model references (e.g., `phi-4-mini`) are consistent
- Add minimal pyright configuration for teams preferring workspace-wide strictness

---

