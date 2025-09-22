<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T19:14:43+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sv"
}
-->
# Ändringslogg

Alla betydande ändringar i EdgeAI för Nybörjare dokumenteras här. Detta projekt använder datum-baserade poster och stilen Keep a Changelog (Lagt till, Ändrat, Fixat, Borttaget, Dokumentation, Flyttat).

## 2025-09-18

### Lagt till
- Modul 08: Microsoft Foundry Local – Komplett utvecklarverktyg
  - Sex sessioner: installation, Azure AI Foundry-integration, öppen källkod-modeller, avancerade demos, agenter och modeller-som-verktyg
  - Körbara exempel under `Module08/samples/01`–`06` med Windows cmd-instruktioner
    - `01` REST snabbchatt (`chat_quickstart.py`)
    - `02` SDK snabbstart med OpenAI/Foundry Local och Azure OpenAI-stöd (`sdk_quickstart.py`)
    - `03` CLI lista-och-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orkestrering (`python -m samples.05.agents.coordinator`)
    - `06` Modeller-som-verktyg router (`router.py`)
- Azure OpenAI-stöd i Session 2 SDK-exempel med konfiguration av miljövariabler
- `.vscode/settings.json` pekar på `Module08/.venv` för att förbättra Python-analysupplösning
- `.env` med `PYTHONPATH`-hint för VS Code/Pylance medvetenhet

### Ändrat
- Standardmodell uppdaterad till `phi-4-mini` i Modul 08-dokumentation och exempel; kvarvarande omnämnanden av `phi-3.5` borttagna inom Modul 08
- Förbättringar i router (`Module08/samples/06/router.py`):
  - Endpoint-upptäckt via `foundry service status` med regex-parsing
  - `/v1/models` hälsokontroll vid start
  - Miljökonfigurerbar modellregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Krav uppdaterade: `Module08/requirements.txt` inkluderar nu `openai` (tillsammans med `requests`, `chainlit`)
- Förtydligad vägledning för Chainlit-exempel och felsökning; importupplösning via arbetsytans inställningar

### Fixat
- Lösta importproblem:
  - Router är inte längre beroende av en icke-existerande `utils`-modul; funktioner är inlinade
  - Koordinator använder relativ import (`from .specialists import ...`) och anropas via modulväg
  - VS Code/Pylance-konfiguration för att lösa `chainlit` och paketimporter
- Rättat mindre stavfel i `STUDY_GUIDE.md` och lagt till täckning för Modul 08

### Borttaget
- Raderat oanvänd `Module08/infra/obs.py` och tagit bort den tomma `infra/`-katalogen; observabilitetsmönster behålls som valfria i dokumentationen

### Flyttat
- Konsoliderat Modul 08-demos under `Module08/samples` med sessionsnumrerade mappar
  - Flyttat Chainlit-app till `samples/04`
  - Flyttat agenter till `samples/05` och lagt till `__init__.py`-filer för paketupplösning

### Dokumentation
- Modul 08-sessionsdokumentation och alla exempel-README-filer berikade med Microsoft Learn och betrodda leverantörsreferenser
- `Module08/README.md` uppdaterad med översikt över exempel, routerkonfiguration och valideringstips
- `Module07/README.md` Windows Foundry Local-sektion validerad mot Learn-dokumentation
- `STUDY_GUIDE.md` uppdaterad:
  - Lagt till Modul 08 i översikt, scheman, framstegsspårare
  - Lagt till omfattande Referenssektion (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historiskt (sammanfattning)
- Kursarkitektur och moduler etablerade (Moduler 01–07)
- Iterativ modernisering av innehåll, standardisering av format och tillagda fallstudier
- Utökad täckning av optimeringsramverk (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Ej släppt / Backlog (förslag)
- Valfria röktester per exempel för att validera Foundry Local tillgänglighet
- Granska översättningar för att anpassa modellreferenser (t.ex. `phi-4-mini`) där det är lämpligt
- Lägg till minimal pyright-konfiguration om team föredrar strikthet över hela arbetsytan

---

