<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T19:07:01+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "tl"
}
-->
# Changelog

Ang lahat ng mahahalagang pagbabago sa EdgeAI for Beginners ay dokumentado dito. Ang proyektong ito ay gumagamit ng mga entry na nakabase sa petsa at ang estilo ng Keep a Changelog (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-10-08

### Idinagdag - Komprehensibong Update sa Workshop
- **Ganap na muling pagsulat ng Workshop README.md**:
  - Idinagdag ang komprehensibong pagpapakilala na nagpapaliwanag ng halaga ng Edge AI (privacy, performance, cost)
  - Nilikha ang 6 pangunahing layunin sa pag-aaral na may detalyadong kakayahan
  - Idinagdag ang talahanayan ng mga resulta ng pag-aaral na may mga deliverable at competency matrix
  - Isinama ang seksyon ng mga kasanayan para sa industriya
  - Idinagdag ang quick start guide na may mga kinakailangan at 3-step na setup
  - Nilikha ang mga talahanayan ng resources para sa Python samples (8 files na may run times)
  - Idinagdag ang talahanayan ng Jupyter notebooks (8 notebooks na may difficulty ratings)
  - Nilikha ang talahanayan ng dokumentasyon (7 pangunahing dokumento na may "Use When" guidance)
  - Idinagdag ang mga rekomendasyon sa learning path para sa iba't ibang antas ng kasanayan

- **Imprastraktura ng pag-validate at pag-test ng Workshop**:
  - Nilikha ang `scripts/validate_samples.py` - Komprehensibong tool para sa pag-validate ng syntax, imports, at best practices
  - Nilikha ang `scripts/test_samples.py` - Smoke test runner para sa lahat ng Python samples
  - Idinagdag ang dokumentasyon ng validation sa `scripts/README.md`

- **Komprehensibong dokumentasyon**:
  - Nilikha ang `SAMPLES_UPDATE_SUMMARY.md` - 400+ linya ng detalyadong gabay na sumasaklaw sa lahat ng mga pagpapabuti
  - Nilikha ang `UPDATE_COMPLETE.md` - Executive summary ng pagkumpleto ng update
  - Nilikha ang `QUICK_REFERENCE.md` - Quick reference card para sa Workshop

### Binago - Modernisasyon ng Workshop Python Sample
- **Na-update ang lahat ng 8 Python samples gamit ang best practices**:
  - Pinahusay ang error handling gamit ang try-except blocks sa lahat ng I/O operations
  - Idinagdag ang type hints at komprehensibong docstrings
  - Ipinatupad ang consistent [INFO]/[ERROR]/[RESULT] logging pattern
  - Protektado ang optional imports gamit ang installation hints
  - Pinahusay ang feedback ng user sa lahat ng samples

- **session01/chat_bootstrap.py**:
  - Pinahusay ang client initialization gamit ang komprehensibong error messages
  - Pinahusay ang streaming error handling gamit ang chunk validation
  - Idinagdag ang mas mahusay na exception handling para sa service unavailability

- **session02/rag_pipeline.py**:
  - Idinagdag ang import guards para sa sentence-transformers gamit ang installation hints
  - Pinahusay ang error handling para sa embedding at generation operations
  - Pinahusay ang output formatting gamit ang structured results

- **session02/rag_eval_ragas.py**:
  - Protektado ang optional imports (ragas, datasets) gamit ang user-friendly error messages
  - Idinagdag ang error handling para sa evaluation metrics
  - Pinahusay ang output formatting para sa evaluation results

- **session03/benchmark_oss_models.py**:
  - Ipinatupad ang graceful degradation (nagpapatuloy kahit may model failures)
  - Idinagdag ang detalyadong progress reporting at per-model error handling
  - Pinahusay ang statistics calculation gamit ang komprehensibong error recovery

- **session04/model_compare.py**:
  - Idinagdag ang type hints (Tuple return types)
  - Pinahusay ang output formatting gamit ang structured JSON results
  - Ipinatupad ang per-model error handling gamit ang recovery

- **session05/agents_orchestrator.py**:
  - Pinahusay ang Agent.act() gamit ang komprehensibong docstrings
  - Idinagdag ang pipeline error handling gamit ang stage-by-stage logging
  - Pinahusay ang memory management at state tracking

- **session06/models_router.py**:
  - Pinahusay ang function documentation para sa lahat ng routing components
  - Idinagdag ang detalyadong logging sa route() function
  - Pinahusay ang test output gamit ang structured results

- **session06/models_pipeline.py**:
  - Idinagdag ang error handling sa chat() helper function
  - Pinahusay ang pipeline() gamit ang stage logging at progress reporting
  - Pinahusay ang main() gamit ang komprehensibong error recovery

### Docs - Pagpapahusay ng Dokumentasyon ng Workshop
- Na-update ang pangunahing README.md na may seksyon ng Workshop na nagha-highlight ng hands-on learning path
- Pinahusay ang STUDY_GUIDE.md gamit ang komprehensibong seksyon ng Workshop kabilang ang:
  - Mga layunin sa pag-aaral at mga focus area
  - Mga tanong para sa self-assessment
  - Mga hands-on exercises na may time estimates
  - Time allocation para sa concentrated at part-time study
  - Idinagdag ang Workshop sa progress tracking template
- Na-update ang time allocation guide mula 20 oras sa 30 oras (kasama ang Workshop)
- Idinagdag ang mga deskripsyon ng Workshop samples at mga resulta ng pag-aaral sa README

### Naayos
- Naresolba ang hindi pare-parehong error handling patterns sa Workshop samples
- Naayos ang mga error sa optional dependency imports gamit ang tamang guards
- Na-correct ang mga nawawalang type hints sa mga critical functions
- Tinugunan ang kakulangan ng user feedback sa mga error scenarios
- Naayos ang mga validation issues gamit ang komprehensibong testing infrastructure

---

## 2025-09-23

### Binago - Major Module 08 Modernization
- **Komprehensibong pag-align sa Microsoft Foundry-Local repository patterns**:
  - Na-update ang lahat ng code examples upang gumamit ng modernong `FoundryLocalManager` at OpenAI SDK integration
  - Pinalitan ang deprecated manual `requests` calls gamit ang tamang SDK usage
  - In-align ang implementation patterns sa opisyal na Microsoft documentation at samples

- **05.AIPoweredAgents.md modernization**:
  - Na-update ang multi-agent orchestration upang gumamit ng modern SDK patterns
  - Pinahusay ang coordinator implementation gamit ang advanced features (feedback loops, performance monitoring)
  - Idinagdag ang komprehensibong error handling at service health checking
  - Isinama ang tamang references sa local samples (`samples/05/multi_agent_orchestration.ipynb`)
  - Na-update ang function calling examples upang gumamit ng modern `tools` parameter sa halip na deprecated `functions`
  - Idinagdag ang production-ready patterns gamit ang monitoring at statistics tracking

- **06.ModelsAsTools.md ganap na muling pagsulat**:
  - Pinalitan ang basic tool registry gamit ang intelligent model router implementation
  - Idinagdag ang keyword-based model selection para sa iba't ibang task types (general, reasoning, code, creative)
  - Isinama ang environment-based configuration gamit ang flexible model assignment
  - Pinahusay gamit ang komprehensibong service health monitoring at error handling
  - Idinagdag ang production deployment patterns gamit ang request monitoring at performance tracking
  - In-align sa local implementation sa `samples/06/router.py` at `samples/06/model_router.ipynb`

- **Mga pagpapabuti sa istruktura ng dokumentasyon**:
  - Idinagdag ang overview sections na nagha-highlight ng modernization at SDK alignment
  - Pinahusay gamit ang emojis at mas magandang formatting para sa mas mahusay na readability
  - Idinagdag ang tamang references sa local sample files sa buong dokumentasyon
  - Isinama ang production-ready implementation guidance at best practices

### Idinagdag
- Komprehensibong overview sections sa Module 08 files na nagha-highlight ng modern SDK integration
- Mga highlight ng architecture na nagpapakita ng advanced features (multi-agent systems, intelligent routing)
- Direktang references sa local sample implementations para sa hands-on experience
- Production deployment guidance gamit ang monitoring at error handling patterns
- Interactive Jupyter notebook examples na may advanced features at benchmarks

### Naayos
- Mga discrepancies sa alignment sa pagitan ng dokumentasyon at aktwal na sample implementations
- Mga outdated SDK usage patterns sa buong Module 08
- Mga nawawalang references sa komprehensibong local sample library
- Hindi pare-parehong implementation approaches sa iba't ibang seksyon

---

## 2025-09-18

### Idinagdag
- Module 08: Microsoft Foundry Local – Kumpletong Developer Toolkit
  - Anim na session: setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, at models-as-tools
  - Mga runnable samples sa ilalim ng `Module08/samples/01`–`06` na may Windows cmd instructions
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart gamit ang OpenAI/Foundry Local at Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI support sa Session 2 SDK sample gamit ang environment variable configuration
- `.vscode/settings.json` upang ituro sa `Module08/.venv` at mapabuti ang Python analysis resolution
- `.env` na may `PYTHONPATH` hint para sa VS Code/Pylance awareness

### Binago
- Default model na-update sa `phi-4-mini` sa buong Module 08 docs at samples; tinanggal ang natitirang `phi-3.5` mentions sa loob ng Module 08
- Mga pagpapabuti sa Router (`Module08/samples/06/router.py`):
  - Endpoint discovery gamit ang `foundry service status` na may regex parsing
  - `/v1/models` health check sa startup
  - Env-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Na-update ang requirements: `Module08/requirements.txt` ngayon ay kasama ang `openai` (kasama ang `requests`, `chainlit`)
- Na-clarify ang Chainlit sample guidance at idinagdag ang troubleshooting; import resolution gamit ang workspace settings

### Naayos
- Naresolba ang mga import issues:
  - Ang Router ay hindi na umaasa sa isang non-existent `utils` module; ang mga functions ay in-line na
  - Ang Coordinator ay gumagamit ng relative import (`from .specialists import ...`) at ini-invoke gamit ang module path
  - VS Code/Pylance configuration upang ma-resolve ang `chainlit` at package imports
- Na-correct ang minor typo sa `STUDY_GUIDE.md` at idinagdag ang Module 08 coverage

### Tinanggal
- Tinanggal ang hindi nagagamit na `Module08/infra/obs.py` at tinanggal ang walang laman na `infra/` directory; ang observability patterns ay nanatiling optional sa docs

### Inilipat
- Pinagsama-sama ang Module 08 demos sa ilalim ng `Module08/samples` na may session-numbered folders
  - Inilipat ang Chainlit app sa `samples/04`
  - Inilipat ang agents sa `samples/05` at idinagdag ang `__init__.py` files para sa package resolution

### Docs
- Ang mga dokumento ng Module 08 session at lahat ng sample READMEs ay pinayaman gamit ang Microsoft Learn at mga trusted vendor references
- Na-update ang `Module08/README.md` na may Samples Overview, router configuration, at validation tips
- Na-validate ang Windows Foundry Local section ng `Module07/README.md` laban sa Learn docs
- Na-update ang `STUDY_GUIDE.md`:
  - Idinagdag ang Module 08 sa overview, schedules, progress tracker
  - Idinagdag ang komprehensibong References section (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historical (summary)
- Na-establish ang course architecture at modules (Modules 01–07)
- Iterative na content modernization, formatting standardization, at idinagdag ang mga case studies
- Pinalawak ang coverage ng optimization frameworks (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unreleased / Backlog (proposals)
- Optional na per-sample smoke tests upang i-validate ang Foundry Local availability
- Review ng translations upang i-align ang model references (hal., `phi-4-mini`) kung saan naaangkop
- Idagdag ang minimal pyright config kung mas gusto ng mga team ang workspace-wide strictness

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.