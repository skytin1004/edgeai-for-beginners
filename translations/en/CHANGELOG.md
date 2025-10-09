<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T20:30:07+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "en"
}
-->
# Changelog

All significant updates to EdgeAI for Beginners are recorded here. This project uses date-based entries and follows the Keep a Changelog format (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-10-08

### Added - Workshop Comprehensive Update
- **Complete rewrite of Workshop README.md**:
  - Added a detailed introduction explaining the value of Edge AI (privacy, performance, cost).
  - Defined 6 core learning objectives with detailed competencies.
  - Included a learning outcomes table with deliverables and a competency matrix.
  - Added a section on career-ready skills for industry relevance.
  - Provided a quick start guide with prerequisites and a 3-step setup process.
  - Created resource tables for Python samples (8 files with estimated run times).
  - Added a Jupyter notebooks table (8 notebooks with difficulty ratings).
  - Developed a documentation table (7 key documents with "Use When" guidance).
  - Suggested learning paths tailored to different skill levels.

- **Workshop validation and testing infrastructure**:
  - Created `scripts/validate_samples.py` - A comprehensive validation tool for syntax, imports, and best practices.
  - Created `scripts/test_samples.py` - A smoke test runner for all Python samples.
  - Added validation documentation to `scripts/README.md`.

- **Comprehensive documentation**:
  - Created `SAMPLES_UPDATE_SUMMARY.md` - A detailed 400+ line guide covering all improvements.
  - Created `UPDATE_COMPLETE.md` - An executive summary of the update completion.
  - Created `QUICK_REFERENCE.md` - A quick reference card for the Workshop.

### Changed - Workshop Python Sample Modernization
- **Updated all 8 Python samples with best practices**:
  - Improved error handling with try-except blocks for all I/O operations.
  - Added type hints and detailed docstrings.
  - Implemented a consistent [INFO]/[ERROR]/[RESULT] logging pattern.
  - Protected optional imports with installation hints.
  - Enhanced user feedback across all samples.

- **session01/chat_bootstrap.py**:
  - Improved client initialization with detailed error messages.
  - Enhanced streaming error handling with chunk validation.
  - Added better exception handling for service unavailability.

- **session02/rag_pipeline.py**:
  - Added import guards for sentence-transformers with installation hints.
  - Improved error handling for embedding and generation operations.
  - Enhanced output formatting with structured results.

- **session02/rag_eval_ragas.py**:
  - Protected optional imports (ragas, datasets) with user-friendly error messages.
  - Added error handling for evaluation metrics.
  - Improved output formatting for evaluation results.

- **session03/benchmark_oss_models.py**:
  - Implemented graceful degradation (continues on model failures).
  - Added detailed progress reporting and per-model error handling.
  - Enhanced statistics calculation with robust error recovery.

- **session04/model_compare.py**:
  - Added type hints (Tuple return types).
  - Enhanced output formatting with structured JSON results.
  - Implemented per-model error handling with recovery mechanisms.

- **session05/agents_orchestrator.py**:
  - Enhanced Agent.act() with detailed docstrings.
  - Added pipeline error handling with stage-by-stage logging.
  - Improved memory management and state tracking.

- **session06/models_router.py**:
  - Enhanced function documentation for all routing components.
  - Added detailed logging in the route() function.
  - Improved test output with structured results.

- **session06/models_pipeline.py**:
  - Added error handling to the chat() helper function.
  - Enhanced pipeline() with stage logging and progress reporting.
  - Improved main() with robust error recovery.

### Docs - Workshop Documentation Enhancement
- Updated the main README.md to highlight the Workshop section and its hands-on learning path.
- Enhanced STUDY_GUIDE.md with a detailed Workshop section, including:
  - Learning objectives and study focus areas.
  - Self-assessment questions.
  - Hands-on exercises with estimated completion times.
  - Time allocation for both intensive and part-time study.
  - Added Workshop sample descriptions and learning outcomes to the README.
- Updated the time allocation guide from 20 hours to 30 hours (including the Workshop).

### Fixed
- Resolved inconsistent error handling patterns across Workshop samples.
- Fixed optional dependency import errors with proper guards.
- Corrected missing type hints in critical functions.
- Addressed insufficient user feedback in error scenarios.
- Fixed validation issues with the comprehensive testing infrastructure.

---

## 2025-09-23

### Changed - Major Module 08 Modernization
- **Aligned with Microsoft Foundry-Local repository patterns**:
  - Updated all code examples to use the modern `FoundryLocalManager` and OpenAI SDK integration.
  - Replaced outdated manual `requests` calls with proper SDK usage.
  - Aligned implementation patterns with official Microsoft documentation and samples.

- **05.AIPoweredAgents.md modernization**:
  - Updated multi-agent orchestration to use modern SDK patterns.
  - Enhanced coordinator implementation with advanced features (feedback loops, performance monitoring).
  - Added robust error handling and service health checks.
  - Integrated proper references to local samples (`samples/05/multi_agent_orchestration.ipynb`).
  - Updated function calling examples to use the modern `tools` parameter instead of the deprecated `functions`.
  - Added production-ready patterns with monitoring and statistics tracking.

- **06.ModelsAsTools.md complete rewrite**:
  - Replaced the basic tool registry with an intelligent model router implementation.
  - Added keyword-based model selection for different task types (general, reasoning, code, creative).
  - Integrated environment-based configuration with flexible model assignment.
  - Enhanced service health monitoring and error handling.
  - Added production deployment patterns with request monitoring and performance tracking.
  - Aligned with local implementations in `samples/06/router.py` and `samples/06/model_router.ipynb`.

- **Improved documentation structure**:
  - Added overview sections highlighting modernization and SDK alignment.
  - Enhanced readability with emojis and better formatting.
  - Included proper references to local sample files throughout the documentation.
  - Provided production-ready implementation guidance and best practices.

### Added
- Comprehensive overview sections in Module 08 files highlighting modern SDK integration.
- Architecture highlights showcasing advanced features (multi-agent systems, intelligent routing).
- Direct references to local sample implementations for hands-on experience.
- Production deployment guidance with monitoring and error handling patterns.
- Interactive Jupyter notebook examples with advanced features and benchmarks.

### Fixed
- Resolved discrepancies between documentation and actual sample implementations.
- Updated outdated SDK usage patterns throughout Module 08.
- Added missing references to the comprehensive local sample library.
- Addressed inconsistent implementation approaches across different sections.

---

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Complete Developer Toolkit:
  - Six sessions: setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, and models-as-tools.
  - Runnable samples under `Module08/samples/01`–`06` with Windows cmd instructions:
    - `01` REST quick chat (`chat_quickstart.py`).
    - `02` SDK quickstart with OpenAI/Foundry Local and Azure OpenAI support (`sdk_quickstart.py`).
    - `03` CLI list-and-bench (`list_and_bench.cmd`).
    - `04` Chainlit demo (`app.py`).
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`).
    - `06` Models-as-Tools router (`router.py`).
- Azure OpenAI support in Session 2 SDK sample with environment variable configuration.
- `.vscode/settings.json` to point to `Module08/.venv` for improved Python analysis resolution.
- `.env` with `PYTHONPATH` hint for VS Code/Pylance awareness.

### Changed
- Default model updated to `phi-4-mini` across Module 08 docs and samples; removed remaining `phi-3.5` mentions within Module 08.
- Router (`Module08/samples/06/router.py`) improvements:
  - Endpoint discovery via `foundry service status` with regex parsing.
  - `/v1/models` health check on startup.
  - Environment-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON).
- Requirements updated: `Module08/requirements.txt` now includes `openai` (alongside `requests`, `chainlit`).
- Chainlit sample guidance clarified and troubleshooting added; import resolution via workspace settings.

### Fixed
- Resolved import issues:
  - Router no longer depends on a non-existent `utils` module; functions are now inlined.
  - Coordinator uses relative imports (`from .specialists import ...`) and is invoked via the module path.
  - VS Code/Pylance configuration to resolve `chainlit` and package imports.
- Corrected minor typo in `STUDY_GUIDE.md` and added Module 08 coverage.

### Removed
- Deleted unused `Module08/infra/obs.py` and removed the empty `infra/` directory; observability patterns retained as optional in the documentation.

### Moved
- Consolidated Module 08 demos under `Module08/samples` with session-numbered folders:
  - Moved Chainlit app to `samples/04`.
  - Moved agents to `samples/05` and added `__init__.py` files for package resolution.

### Docs
- Module 08 session documentation and all sample READMEs enriched with Microsoft Learn and trusted vendor references.
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
- Review translations to ensure alignment with model references (e.g., `phi-4-mini`).
- Add minimal pyright configuration for teams preferring workspace-wide strictness.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations resulting from the use of this translation.