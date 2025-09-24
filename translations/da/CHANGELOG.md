<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T23:09:57+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "da"
}
-->
# Ændringslog

Alle væsentlige ændringer i EdgeAI for Beginners er dokumenteret her. Dette projekt bruger dato-baserede indgange og Keep a Changelog-stilen (Tilføjet, Ændret, Rettet, Fjernet, Dokumentation, Flyttet).

## 2025-09-23

### Ændret - Større modernisering af Modul 08
- **Omfattende tilpasning til Microsoft Foundry-Local repository-mønstre**
  - Opdaterede alle kodeeksempler til at bruge moderne `FoundryLocalManager` og OpenAI SDK-integration
  - Udskiftede forældede manuelle `requests`-kald med korrekt SDK-brug
  - Tilpassede implementeringsmønstre til officiel Microsoft-dokumentation og eksempler

- **Modernisering af 05.AIPoweredAgents.md**:
  - Opdaterede multi-agent orkestrering til at bruge moderne SDK-mønstre
  - Forbedrede koordinatorimplementering med avancerede funktioner (feedback loops, performance monitoring)
  - Tilføjede omfattende fejlbehandling og kontrol af tjenestens helbred
  - Integrerede korrekte referencer til lokale eksempler (`samples/05/multi_agent_orchestration.ipynb`)
  - Opdaterede funktionskaldseksempler til at bruge moderne `tools`-parameter i stedet for forældede `functions`
  - Tilføjede produktionsklare mønstre med overvågning og statistiksporing

- **Fuldstændig omskrivning af 06.ModelsAsTools.md**:
  - Udskiftede grundlæggende værktøjsregister med intelligent model-router-implementering
  - Tilføjede nøgleordsbaseret modelvalg til forskellige opgavetyper (generel, ræsonnement, kode, kreativ)
  - Integrerede miljøbaseret konfiguration med fleksibel modeltildeling
  - Forbedret med omfattende overvågning af tjenestens helbred og fejlbehandling
  - Tilføjede produktionsudrulningsmønstre med anmodningsovervågning og performance-tracking
  - Tilpasset lokal implementering i `samples/06/router.py` og `samples/06/model_router.ipynb`

- **Forbedringer af dokumentationsstruktur**:
  - Tilføjede oversigtssektioner, der fremhæver modernisering og SDK-tilpasning
  - Forbedret med emojis og bedre formatering for øget læsbarhed
  - Tilføjede korrekte referencer til lokale prøvefiler i hele dokumentationen
  - Inkluderede vejledning til produktionsklare implementeringer og bedste praksis

### Tilføjet
- Omfattende oversigtssektioner i Modul 08-filer, der fremhæver moderne SDK-integration
- Arkitekturhøjdepunkter, der viser avancerede funktioner (multi-agent-systemer, intelligent routing)
- Direkte referencer til lokale prøveimplementeringer for praktisk erfaring
- Vejledning til produktionsudrulning med overvågnings- og fejlbehandlingsmønstre
- Interaktive Jupyter-notebook-eksempler med avancerede funktioner og benchmarks

### Rettet
- Uoverensstemmelser mellem dokumentation og faktiske prøveimplementeringer
- Forældede SDK-brugsmønstre i hele Modul 08
- Manglende referencer til omfattende lokal prøvebibliotek
- Inkonsistente implementeringsmetoder på tværs af forskellige sektioner

---

## 2025-09-18

### Tilføjet
- Modul 08: Microsoft Foundry Local – Komplet udviklerværktøjssæt
  - Seks sessioner: opsætning, Azure AI Foundry-integration, open-source-modeller, avancerede demoer, agenter og modeller-som-værktøjer
  - Kørbare prøver under `Module08/samples/01`–`06` med Windows cmd-instruktioner
    - `01` REST hurtig chat (`chat_quickstart.py`)
    - `02` SDK hurtigstart med OpenAI/Foundry Local og Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orkestrering (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI support i Session 2 SDK-prøve med miljøvariabelkonfiguration
- `.vscode/settings.json` til at pege på `Module08/.venv` og forbedre Python-analyseopløsning
- `.env` med `PYTHONPATH`-hint for VS Code/Pylance-bevidsthed

### Ændret
- Standardmodel opdateret til `phi-4-mini` på tværs af Modul 08-dokumenter og prøver; fjernet resterende `phi-3.5`-henvisninger inden for Modul 08
- Router (`Module08/samples/06/router.py`) forbedringer:
  - Endpoint-opdagelse via `foundry service status` med regex-parsing
  - `/v1/models` helbredstjek ved opstart
  - Miljøkonfigurerbart modelregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Krav opdateret: `Module08/requirements.txt` inkluderer nu `openai` (sammen med `requests`, `chainlit`)
- Chainlit-prøvevejledning præciseret og fejlfinding tilføjet; importopløsning via arbejdsområdets indstillinger

### Rettet
- Løste importproblemer:
  - Router afhænger ikke længere af et ikke-eksisterende `utils`-modul; funktioner er inlinede
  - Koordinator bruger relativ import (`from .specialists import ...`) og kaldes via modulsti
  - VS Code/Pylance-konfiguration til at løse `chainlit` og pakkeimporter
- Rettede mindre stavefejl i `STUDY_GUIDE.md` og tilføjede Modul 08-dækning

### Fjernet
- Slettede ubrugte `Module08/infra/obs.py` og fjernede den tomme `infra/`-mappe; observabilitetsmønstre bevaret som valgfri i dokumentationen

### Flyttet
- Konsoliderede Modul 08-demoer under `Module08/samples` med sessionnummererede mapper
  - Flyttede Chainlit-app til `samples/04`
  - Flyttede agenter til `samples/05` og tilføjede `__init__.py`-filer for pakkeopløsning

### Dokumentation
- Modul 08-sessionsdokumentation og alle prøve-README'er beriget med Microsoft Learn og betroede leverandørreferencer
- `Module08/README.md` opdateret med Prøveoversigt, routerkonfiguration og valideringstips
- `Module07/README.md` Windows Foundry Local-sektion valideret mod Learn-dokumentation
- `STUDY_GUIDE.md` opdateret:
  - Tilføjede Modul 08 til oversigt, tidsplaner, fremskridtsoversigt
  - Tilføjede omfattende Referenceliste (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisk (resumé)
- Kursusarkitektur og moduler etableret (Moduler 01–07)
- Iterativ modernisering af indhold, standardisering af formatering og tilføjede casestudier
- Udvidet dækning af optimeringsrammer (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Ikke udgivet / Backlog (forslag)
- Valgfrie røggtests pr. prøve for at validere Foundry Local tilgængelighed
- Gennemgå oversættelser for at tilpasse modelreferencer (f.eks. `phi-4-mini`) hvor det er relevant
- Tilføj minimal pyright-konfiguration, hvis teams foretrækker arbejdsområdebred strenghed

---

