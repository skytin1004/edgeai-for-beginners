<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T00:32:24+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "en"
}
-->
# Changelog

All significant updates to EdgeAI for Beginners are documented here. This project uses date-based entries and follows the Keep a Changelog format (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-09-23

### Changed - Major Module 08 Modernization
- **Comprehensive alignment with Microsoft Foundry-Local repository patterns**
  - Updated all code examples to utilize the modern `FoundryLocalManager` and OpenAI SDK integration.
  - Replaced outdated manual `requests` calls with proper SDK usage.
  - Adjusted implementation patterns to align with official Microsoft documentation and samples.

- **05.AIPoweredAgents.md modernization**:
  - Updated multi-agent orchestration to follow modern SDK patterns.
  - Enhanced the coordinator implementation with advanced features like feedback loops and performance monitoring.
  - Added robust error handling and service health checks.
  - Integrated references to local samples (`samples/05/multi_agent_orchestration.ipynb`).
  - Updated function call examples to use the modern `tools` parameter instead of the deprecated `functions`.
  - Included production-ready patterns with monitoring and statistics tracking.

- **06.ModelsAsTools.md complete rewrite**:
  - Replaced the basic tool registry with an intelligent model router implementation.
  - Added keyword-based model selection for various task types (general, reasoning, code, creative).
  - Integrated environment-based configuration for flexible model assignment.
  - Enhanced service health monitoring and error handling.
  - Included production deployment patterns with request monitoring and performance tracking.
  - Aligned with local implementations in `samples/06/router.py` and `samples/06/model_router.ipynb`.

- **Documentation structure improvements**:
  - Added overview sections emphasizing modernization and SDK alignment.
  - Improved readability with emojis and better formatting.
  - Included references to local sample files throughout the documentation.
  - Provided production-ready implementation guidance and best practices.

### Added
- Comprehensive overview sections in Module 08 files highlighting modern SDK integration.
- Architecture highlights showcasing advanced features like multi-agent systems and intelligent routing.
- Direct references to local sample implementations for hands-on learning.
- Production deployment guidance with monitoring and error handling patterns.
- Interactive Jupyter notebook examples featuring advanced functionalities and benchmarks.

### Fixed
- Resolved discrepancies between documentation and actual sample implementations.
- Updated outdated SDK usage patterns across Module 08.
- Added missing references to the comprehensive local sample library.
- Standardized implementation approaches across different sections.

---

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Complete Developer Toolkit
  - Six sessions covering setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, and models-as-tools.
  - Runnable samples located under `Module08/samples/01`–`06` with Windows cmd instructions:
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart with OpenAI/Foundry Local and Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI support in Session 2 SDK sample with environment variable configuration.
- `.vscode/settings.json` configured to point to `Module08/.venv` for improved Python analysis resolution.
- `.env` file with `PYTHONPATH` hint for VS Code/Pylance awareness.

### Changed
- Default model updated to `phi-4-mini` across Module 08 documentation and samples; removed remaining references to `phi-3.5` within Module 08.
- Router (`Module08/samples/06/router.py`) improvements:
  - Endpoint discovery via `foundry service status` with regex parsing.
  - `/v1/models` health check during startup.
  - Environment-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON).
- Requirements updated: `Module08/requirements.txt` now includes `openai` (alongside `requests`, `chainlit`).
- Clarified Chainlit sample guidance and added troubleshooting steps; import resolution via workspace settings.

### Fixed
- Resolved import issues:
  - Router no longer depends on a non-existent `utils` module; functions are now inlined.
  - Coordinator uses relative imports (`from .specialists import ...`) and is invoked via module path.
  - VS Code/Pylance configuration updated to resolve `chainlit` and package imports.
- Corrected minor typo in `STUDY_GUIDE.md` and added Module 08 coverage.

### Removed
- Deleted unused `Module08/infra/obs.py` and removed the empty `infra/` directory; observability patterns retained as optional in documentation.

### Moved
- Consolidated Module 08 demos under `Module08/samples` with session-numbered folders:
  - Moved Chainlit app to `samples/04`.
  - Moved agents to `samples/05` and added `__init__.py` files for package resolution.

### Docs
- Module 08 session documentation and all sample READMEs enriched with references to Microsoft Learn and trusted vendors.
- `Module08/README.md` updated with a Samples Overview, router configuration, and validation tips.
- `Module07/README.md` Windows Foundry Local section validated against Learn documentation.
- `STUDY_GUIDE.md` updated:
  - Added Module 08 to the overview, schedules, and progress tracker.
  - Included a comprehensive References section (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML).

---

## Historical (summary)
- Course architecture and modules established (Modules 01–07).
- Iterative content modernization, formatting standardization, and added case studies.
- Expanded coverage of optimization frameworks (Llama.cpp, Olive, OpenVINO, Apple MLX).

## Unreleased / Backlog (proposals)
- Optional smoke tests for each sample to validate Foundry Local availability.
- Review translations to ensure model references (e.g., `phi-4-mini`) are consistent.
- Add minimal pyright configuration for teams preferring workspace-wide strictness.

---

