<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T20:18:39+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "da"
}
-->
# Ændringslog

Alle væsentlige ændringer i EdgeAI for Beginners er dokumenteret her. Dette projekt bruger dato-baserede indgange og Keep a Changelog-stilen (Tilføjet, Ændret, Rettet, Fjernet, Dokumentation, Flyttet).

## 2025-09-18

### Tilføjet
- Modul 08: Microsoft Foundry Local – Komplet udviklerværktøjssæt
  - Seks sessioner: opsætning, Azure AI Foundry-integration, open source-modeller, avancerede demoer, agenter og modeller-som-værktøjer
  - Kørbare eksempler under `Module08/samples/01`–`06` med Windows cmd-instruktioner
    - `01` REST hurtig chat (`chat_quickstart.py`)
    - `02` SDK hurtigstart med OpenAI/Foundry Local og Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI liste-og-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orkestrering (`python -m samples.05.agents.coordinator`)
    - `06` Modeller-som-værktøjer router (`router.py`)
- Azure OpenAI support i Session 2 SDK-eksempel med miljøvariabelkonfiguration
- `.vscode/settings.json` peger på `Module08/.venv` og forbedrer Python-analyseopløsning
- `.env` med `PYTHONPATH` hint for VS Code/Pylance opmærksomhed

### Ændret
- Standardmodel opdateret til `phi-4-mini` på tværs af Modul 08 dokumentation og eksempler; fjernet resterende `phi-3.5` omtaler inden for Modul 08
- Router (`Module08/samples/06/router.py`) forbedringer:
  - Endpoint-opdagelse via `foundry service status` med regex-parsing
  - `/v1/models` sundhedstjek ved opstart
  - Miljø-konfigurerbar modelregistrering (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Krav opdateret: `Module08/requirements.txt` inkluderer nu `openai` (sammen med `requests`, `chainlit`)
- Chainlit-eksempelvejledning præciseret og fejlfinding tilføjet; importopløsning via arbejdsområdets indstillinger

### Rettet
- Løste importproblemer:
  - Router afhænger ikke længere af et ikke-eksisterende `utils` modul; funktioner er inlined
  - Koordinator bruger relativ import (`from .specialists import ...`) og kaldes via modulsti
  - VS Code/Pylance-konfiguration til at løse `chainlit` og pakkeimporter
- Rettede mindre stavefejl i `STUDY_GUIDE.md` og tilføjede Modul 08 dækning

### Fjernet
- Slettede ubrugte `Module08/infra/obs.py` og fjernede den tomme `infra/` mappe; observabilitetsmønstre bevaret som valgfri i dokumentationen

### Flyttet
- Konsoliderede Modul 08 demoer under `Module08/samples` med session-nummererede mapper
  - Flyttede Chainlit app til `samples/04`
  - Flyttede agenter til `samples/05` og tilføjede `__init__.py` filer for pakkeopløsning

### Dokumentation
- Modul 08 session dokumentation og alle eksempel-README'er beriget med Microsoft Learn og betroede leverandørreferencer
- `Module08/README.md` opdateret med Oversigt over eksempler, routerkonfiguration og valideringstips
- `Module07/README.md` Windows Foundry Local sektion valideret mod Learn dokumentation
- `STUDY_GUIDE.md` opdateret:
  - Tilføjet Modul 08 til oversigt, tidsplaner, fremskridts-tracker
  - Tilføjet omfattende Referencer sektion (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisk (resumé)
- Kursusarkitektur og moduler etableret (Moduler 01–07)
- Iterativ modernisering af indhold, standardisering af formatering og tilføjede casestudier
- Udvidet dækning af optimeringsrammer (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Uudgivet / Backlog (forslag)
- Valgfrie røgt-tests pr. eksempel for at validere Foundry Local tilgængelighed
- Gennemgå oversættelser for at tilpasse modelreferencer (f.eks. `phi-4-mini`) hvor det er relevant
- Tilføj minimal pyright-konfiguration, hvis teams foretrækker arbejdsområde-bred strenghed

---

