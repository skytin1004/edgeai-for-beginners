# Changelog

All notable changes to EdgeAI for Beginners are documented here. This project uses date-based entries and the Keep a Changelog style (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-10-08

### Added - Workshop Comprehensive Update
- **Workshop README.md complete rewrite**:
  - Added comprehensive introduction explaining Edge AI value proposition (privacy, performance, cost)
  - Created 6 core learning objectives with detailed competencies
  - Added learning outcomes table with deliverables and competency matrix
  - Included career-ready skills section for industry relevance
  - Added quick start guide with prerequisites and 3-step setup
  - Created resource tables for Python samples (8 files with run times)
  - Added Jupyter notebooks table (8 notebooks with difficulty ratings)
  - Created documentation table (7 key docs with "Use When" guidance)
  - Added learning path recommendations for different skill levels

- **Workshop validation and testing infrastructure**:
  - Created `scripts/validate_samples.py` - Comprehensive validation tool for syntax, imports, and best practices
  - Created `scripts/test_samples.py` - Smoke test runner for all Python samples
  - Added validation documentation to `scripts/README.md`

- **Comprehensive documentation**:
  - Created `SAMPLES_UPDATE_SUMMARY.md` - 400+ line detailed guide covering all improvements
  - Created `UPDATE_COMPLETE.md` - Executive summary of update completion
  - Created `QUICK_REFERENCE.md` - Quick reference card for Workshop

### Changed - Workshop Python Sample Modernization
- **All 8 Python samples updated with best practices**:
  - Enhanced error handling with try-except blocks around all I/O operations
  - Added type hints and comprehensive docstrings
  - Implemented consistent [INFO]/[ERROR]/[RESULT] logging pattern
  - Protected optional imports with installation hints
  - Improved user feedback throughout all samples

- **session01/chat_bootstrap.py**:
  - Enhanced client initialization with comprehensive error messages
  - Improved streaming error handling with chunk validation
  - Added better exception handling for service unavailability

- **session02/rag_pipeline.py**:
  - Added import guards for sentence-transformers with installation hints
  - Enhanced error handling for embedding and generation operations
  - Improved output formatting with structured results

- **session02/rag_eval_ragas.py**:
  - Protected optional imports (ragas, datasets) with user-friendly error messages
  - Added error handling for evaluation metrics
  - Enhanced output formatting for evaluation results

- **session03/benchmark_oss_models.py**:
  - Implemented graceful degradation (continues on model failures)
  - Added detailed progress reporting and per-model error handling
  - Enhanced statistics calculation with comprehensive error recovery

- **session04/model_compare.py**:
  - Added type hints (Tuple return types)
  - Enhanced output formatting with structured JSON results
  - Implemented per-model error handling with recovery

- **session05/agents_orchestrator.py**:
  - Enhanced Agent.act() with comprehensive docstrings
  - Added pipeline error handling with stage-by-stage logging
  - Improved memory management and state tracking

- **session06/models_router.py**:
  - Enhanced function documentation for all routing components
  - Added detailed logging in route() function
  - Improved test output with structured results

- **session06/models_pipeline.py**:
  - Added error handling to chat() helper function
  - Enhanced pipeline() with stage logging and progress reporting
  - Improved main() with comprehensive error recovery

### Docs - Workshop Documentation Enhancement
- Updated main README.md with Workshop section highlighting hands-on learning path
- Enhanced STUDY_GUIDE.md with comprehensive Workshop section including:
  - Learning objectives and study focus areas
  - Self-assessment questions
  - Hands-on exercises with time estimates
  - Time allocation for concentrated and part-time study
  - Added Workshop to progress tracking template
- Updated time allocation guide from 20 hours to 30 hours (including Workshop)
- Added Workshop sample descriptions and learning outcomes to README

### Fixed
- Resolved inconsistent error handling patterns across Workshop samples
- Fixed optional dependency import errors with proper guards
- Corrected missing type hints in critical functions
- Addressed insufficient user feedback in error scenarios
- Fixed validation issues with comprehensive testing infrastructure

---

## 2025-09-23

### Changed - Major Module 08 Modernization
- **Comprehensive alignment with Microsoft Foundry-Local repository patterns**
  - Updated all code examples to use modern `FoundryLocalManager` and OpenAI SDK integration
  - Replaced deprecated manual `requests` calls with proper SDK usage
  - Aligned implementation patterns with official Microsoft documentation and samples

- **05.AIPoweredAgents.md modernization**:
  - Updated multi-agent orchestration to use modern SDK patterns
  - Enhanced coordinator implementation with advanced features (feedback loops, performance monitoring)
  - Added comprehensive error handling and service health checking
  - Integrated proper references to local samples (`samples/05/multi_agent_orchestration.ipynb`)
  - Updated function calling examples to use modern `tools` parameter instead of deprecated `functions`
  - Added production-ready patterns with monitoring and statistics tracking

- **06.ModelsAsTools.md complete rewrite**:
  - Replaced basic tool registry with intelligent model router implementation
  - Added keyword-based model selection for different task types (general, reasoning, code, creative)
  - Integrated environment-based configuration with flexible model assignment
  - Enhanced with comprehensive service health monitoring and error handling
  - Added production deployment patterns with request monitoring and performance tracking
  - Aligned with local implementation in `samples/06/router.py` and `samples/06/model_router.ipynb`

- **Documentation structure improvements**:
  - Added overview sections highlighting modernization and SDK alignment
  - Enhanced with emojis and better formatting for improved readability
  - Added proper references to local sample files throughout documentation
  - Included production-ready implementation guidance and best practices

### Added
- Comprehensive overview sections in Module 08 files highlighting modern SDK integration
- Architecture highlights showcasing advanced features (multi-agent systems, intelligent routing)
- Direct references to local sample implementations for hands-on experience
- Production deployment guidance with monitoring and error handling patterns
- Interactive Jupyter notebook examples with advanced features and benchmarks

### Fixed
- Alignment discrepancies between documentation and actual sample implementations
- Outdated SDK usage patterns throughout Module 08
- Missing references to comprehensive local sample library
- Inconsistent implementation approaches across different sections

---

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
