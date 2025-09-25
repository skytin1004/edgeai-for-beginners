<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T00:50:28+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "tl"
}
-->
# Changelog

Ang lahat ng mahahalagang pagbabago sa EdgeAI for Beginners ay dokumentado dito. Ang proyektong ito ay gumagamit ng mga entry na nakabase sa petsa at ang estilo ng Keep a Changelog (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-09-23

### Changed - Malaking Modernisasyon ng Module 08
- **Komprehensibong pag-aayon sa mga pattern ng Microsoft Foundry-Local repository**
  - In-update ang lahat ng halimbawa ng code upang gumamit ng modernong `FoundryLocalManager` at OpenAI SDK integration
  - Pinalitan ang deprecated manual na `requests` calls gamit ang tamang paggamit ng SDK
  - Inayon ang mga pattern ng implementasyon sa opisyal na dokumentasyon at mga sample ng Microsoft

- **Modernisasyon ng 05.AIPoweredAgents.md**:
  - In-update ang multi-agent orchestration upang gumamit ng modernong mga pattern ng SDK
  - Pinahusay ang implementasyon ng coordinator gamit ang mga advanced na tampok (feedback loops, performance monitoring)
  - Idinagdag ang komprehensibong error handling at service health checking
  - Inintegrate ang tamang mga reference sa mga lokal na sample (`samples/05/multi_agent_orchestration.ipynb`)
  - In-update ang mga halimbawa ng function calling upang gumamit ng modernong `tools` parameter sa halip na deprecated na `functions`
  - Idinagdag ang mga production-ready pattern na may monitoring at statistics tracking

- **Kompletong rewrite ng 06.ModelsAsTools.md**:
  - Pinalitan ang basic tool registry ng intelligent model router implementation
  - Idinagdag ang keyword-based model selection para sa iba't ibang uri ng task (general, reasoning, code, creative)
  - Inintegrate ang environment-based configuration na may flexible model assignment
  - Pinahusay gamit ang komprehensibong service health monitoring at error handling
  - Idinagdag ang mga production deployment pattern na may request monitoring at performance tracking
  - Inayon sa lokal na implementasyon sa `samples/06/router.py` at `samples/06/model_router.ipynb`

- **Mga pagpapabuti sa istruktura ng dokumentasyon**:
  - Idinagdag ang mga overview section na nagha-highlight ng modernisasyon at pag-aayon sa SDK
  - Pinahusay gamit ang emojis at mas magandang formatting para sa mas madaling mabasa
  - Idinagdag ang tamang mga reference sa mga lokal na sample file sa buong dokumentasyon
  - Kasama ang mga production-ready implementation guidance at best practices

### Added
- Komprehensibong overview sections sa mga file ng Module 08 na nagha-highlight ng modern SDK integration
- Mga highlight ng arkitektura na nagpapakita ng mga advanced na tampok (multi-agent systems, intelligent routing)
- Direktang mga reference sa mga lokal na sample implementation para sa hands-on na karanasan
- Gabay sa production deployment na may monitoring at error handling patterns
- Mga interactive na Jupyter notebook na may advanced na tampok at benchmarks

### Fixed
- Mga discrepancy sa pag-aayon sa pagitan ng dokumentasyon at aktwal na mga sample implementation
- Mga outdated na pattern ng paggamit ng SDK sa buong Module 08
- Mga nawawalang reference sa komprehensibong lokal na sample library
- Hindi magkakatugmang mga approach sa implementasyon sa iba't ibang seksyon

---

## 2025-09-18

### Added
- Module 08: Microsoft Foundry Local – Kompletong Toolkit para sa Developer
  - Anim na session: setup, Azure AI Foundry integration, open-source models, cutting-edge demos, agents, at models-as-tools
  - Mga runnable sample sa ilalim ng `Module08/samples/01`–`06` na may Windows cmd instructions
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart gamit ang OpenAI/Foundry Local at Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orchestration (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI support sa Session 2 SDK sample na may environment variable configuration
- `.vscode/settings.json` upang ituro sa `Module08/.venv` at mapabuti ang Python analysis resolution
- `.env` na may `PYTHONPATH` hint para sa VS Code/Pylance awareness

### Changed
- Default na model in-update sa `phi-4-mini` sa buong Module 08 docs at samples; tinanggal ang natitirang mga banggit sa `phi-3.5` sa loob ng Module 08
- Mga pagpapabuti sa Router (`Module08/samples/06/router.py`):
  - Endpoint discovery gamit ang `foundry service status` na may regex parsing
  - `/v1/models` health check sa startup
  - Env-configurable model registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Mga requirements in-update: `Module08/requirements.txt` ngayon ay kasama ang `openai` (kasama ang `requests`, `chainlit`)
- Gabay sa Chainlit sample nilinaw at troubleshooting idinagdag; import resolution gamit ang workspace settings

### Fixed
- Naresolba ang mga isyu sa import:
  - Ang Router ay hindi na umaasa sa isang hindi umiiral na `utils` module; ang mga function ay in-line na
  - Ang Coordinator ay gumagamit ng relative import (`from .specialists import ...`) at ini-invoke gamit ang module path
  - VS Code/Pylance configuration upang ma-resolve ang `chainlit` at mga package import
- Na-correct ang minor typo sa `STUDY_GUIDE.md` at idinagdag ang Module 08 coverage

### Removed
- Tinanggal ang hindi nagagamit na `Module08/infra/obs.py` at tinanggal ang walang laman na `infra/` directory; ang mga observability pattern ay nanatiling opsyonal sa dokumentasyon

### Moved
- Pinagsama-sama ang mga demo ng Module 08 sa ilalim ng `Module08/samples` na may mga folder na naka-session number
  - Inilipat ang Chainlit app sa `samples/04`
  - Inilipat ang mga agents sa `samples/05` at idinagdag ang mga `__init__.py` file para sa package resolution

### Docs
- Mga session docs ng Module 08 at lahat ng sample READMEs pinayaman gamit ang Microsoft Learn at mga trusted vendor reference
- `Module08/README.md` in-update gamit ang Samples Overview, router configuration, at validation tips
- `Module07/README.md` Windows Foundry Local section validated laban sa Learn docs
- `STUDY_GUIDE.md` in-update:
  - Idinagdag ang Module 08 sa overview, schedules, progress tracker
  - Idinagdag ang komprehensibong References section (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historical (summary)
- Itinatag ang arkitektura ng kurso at mga module (Modules 01–07)
- Iterative na modernisasyon ng content, standardisasyon ng formatting, at idinagdag na mga case study
- Pinalawak ang saklaw ng optimization frameworks (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unreleased / Backlog (proposals)
- Opsyonal na per-sample smoke tests upang i-validate ang Foundry Local availability
- Review ng mga translation upang iayon ang mga model reference (hal., `phi-4-mini`) kung saan naaangkop
- Magdagdag ng minimal na pyright config kung mas gusto ng mga team ang workspace-wide strictness

---

