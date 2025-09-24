<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T22:43:37+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sv"
}
-->
# Ändringslogg

Alla betydande ändringar i EdgeAI för Nybörjare dokumenteras här. Detta projekt använder datum-baserade poster och stilen "Keep a Changelog" (Added, Changed, Fixed, Removed, Docs, Moved).

## 2025-09-23

### Changed - Större modernisering av Modul 08
- **Omfattande anpassning till Microsoft Foundry-Local repository-mönster**
  - Uppdaterade alla kodexempel för att använda moderna `FoundryLocalManager` och OpenAI SDK-integration
  - Ersatte föråldrade manuella `requests`-anrop med korrekt SDK-användning
  - Anpassade implementeringsmönster till officiell Microsoft-dokumentation och exempel

- **05.AIPoweredAgents.md modernisering**:
  - Uppdaterade orkestrering av flera agenter för att använda moderna SDK-mönster
  - Förbättrade koordinatorimplementering med avancerade funktioner (feedback-loopar, prestandaövervakning)
  - Lade till omfattande felhantering och kontroll av tjänstehälsa
  - Integrerade korrekta referenser till lokala exempel (`samples/05/multi_agent_orchestration.ipynb`)
  - Uppdaterade funktionsanropsexempel för att använda moderna `tools`-parametrar istället för föråldrade `functions`
  - Lade till produktionsklara mönster med övervakning och statistikspårning

- **06.ModelsAsTools.md total omskrivning**:
  - Ersatte grundläggande verktygsregister med intelligent modellrouter-implementering
  - Lade till nyckelordsbaserad modellval för olika uppgiftstyper (generell, resonemang, kod, kreativ)
  - Integrerade miljöbaserad konfiguration med flexibel modelltilldelning
  - Förbättrade med omfattande övervakning av tjänstehälsa och felhantering
  - Lade till produktionsimplementeringsmönster med begäranövervakning och prestandaspårning
  - Anpassade till lokal implementering i `samples/06/router.py` och `samples/06/model_router.ipynb`

- **Förbättringar av dokumentationsstruktur**:
  - Lade till översiktssektioner som lyfter fram modernisering och SDK-anpassning
  - Förbättrade med emojis och bättre formatering för förbättrad läsbarhet
  - Lade till korrekta referenser till lokala exempel genom hela dokumentationen
  - Inkluderade vägledning för produktionsklara implementeringar och bästa praxis

### Added
- Omfattande översiktssektioner i Modul 08-filer som lyfter fram modern SDK-integration
- Arkitekturhöjdpunkter som visar avancerade funktioner (system med flera agenter, intelligent routing)
- Direkta referenser till lokala exempelimplementeringar för praktisk erfarenhet
- Vägledning för produktionsimplementering med övervakning och felhanteringsmönster
- Interaktiva Jupyter-notebook-exempel med avancerade funktioner och benchmarks

### Fixed
- Justerade skillnader mellan dokumentation och faktiska exempelimplementeringar
- Föråldrade SDK-användningsmönster genom hela Modul 08
- Saknade referenser till omfattande lokalt exempelbibliotek
- Inkonsekventa implementeringsmetoder mellan olika sektioner

---

## 2025-09-18

### Added
- Modul 08: Microsoft Foundry Local – Komplett utvecklarverktyg
  - Sex sessioner: installation, Azure AI Foundry-integration, öppen källkod-modeller, avancerade demos, agenter och modeller-som-verktyg
  - Körbara exempel under `Module08/samples/01`–`06` med Windows cmd-instruktioner
    - `01` REST snabbchatt (`chat_quickstart.py`)
    - `02` SDK snabbstart med OpenAI/Foundry Local och Azure OpenAI-stöd (`sdk_quickstart.py`)
    - `03` CLI lista-och-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Orkestrering av flera agenter (`python -m samples.05.agents.coordinator`)
    - `06` Router för modeller-som-verktyg (`router.py`)
- Azure OpenAI-stöd i Session 2 SDK-exempel med miljövariabelkonfiguration
- `.vscode/settings.json` pekar på `Module08/.venv` för att förbättra Python-analysupplösning
- `.env` med `PYTHONPATH`-hint för VS Code/Pylance-medvetenhet

### Changed
- Standardmodell uppdaterad till `phi-4-mini` genom Modul 08-dokument och exempel; tog bort kvarvarande omnämnanden av `phi-3.5` inom Modul 08
- Förbättringar av router (`Module08/samples/06/router.py`):
  - Upptäckt av slutpunkter via `foundry service status` med regex-parsing
  - `/v1/models` hälsokontroll vid start
  - Miljökonfigurerbart modellregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Krav uppdaterade: `Module08/requirements.txt` inkluderar nu `openai` (tillsammans med `requests`, `chainlit`)
- Förtydligad vägledning för Chainlit-exempel och felsökning; importupplösning via arbetsplatsinställningar

### Fixed
- Löste importproblem:
  - Router är inte längre beroende av en icke-existerande `utils`-modul; funktioner är inlinade
  - Koordinator använder relativ import (`from .specialists import ...`) och anropas via modulväg
  - VS Code/Pylance-konfiguration för att lösa `chainlit` och paketimporter
- Korrigerade mindre stavfel i `STUDY_GUIDE.md` och lade till täckning av Modul 08

### Removed
- Tog bort oanvänd `Module08/infra/obs.py` och raderade den tomma `infra/`-katalogen; mönster för observabilitet behålls som valfria i dokumentationen

### Moved
- Konsoliderade Modul 08-demos under `Module08/samples` med sessionnumrerade mappar
  - Flyttade Chainlit-app till `samples/04`
  - Flyttade agenter till `samples/05` och lade till `__init__.py`-filer för paketupplösning

### Docs
- Modul 08-sessionsdokument och alla exempel-README-filer berikade med referenser till Microsoft Learn och betrodda leverantörer
- `Module08/README.md` uppdaterad med översikt över exempel, routerkonfiguration och valideringstips
- `Module07/README.md` Windows Foundry Local-sektion validerad mot Learn-dokument
- `STUDY_GUIDE.md` uppdaterad:
  - Lade till Modul 08 i översikt, scheman, framstegsspårare
  - Lade till omfattande referenssektion (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historiskt (sammanfattning)
- Kursarkitektur och moduler etablerade (Moduler 01–07)
- Iterativ modernisering av innehåll, standardisering av formatering och tillagda fallstudier
- Utökad täckning av optimeringsramverk (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Ej släppt / Backlog (förslag)
- Valfria röktester per exempel för att validera Foundry Local-tillgänglighet
- Granska översättningar för att anpassa modellreferenser (t.ex. `phi-4-mini`) där det är lämpligt
- Lägg till minimal pyright-konfiguration om team föredrar strikthet över hela arbetsplatsen

---

