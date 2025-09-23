<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T20:18:50+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "no"
}
-->
# Endringslogg

Alle vesentlige endringer i EdgeAI for Beginners er dokumentert her. Dette prosjektet bruker dato-baserte oppføringer og Keep a Changelog-stil (Lagt til, Endret, Fikset, Fjernet, Dokumentasjon, Flyttet).

## 2025-09-18

### Lagt til
- Modul 08: Microsoft Foundry Local – Komplett utviklerverktøysett
  - Seks økter: oppsett, Azure AI Foundry-integrasjon, åpen kildekode-modeller, banebrytende demoer, agenter og modeller som verktøy
  - Kjørbare eksempler under `Module08/samples/01`–`06` med Windows cmd-instruksjoner
    - `01` REST rask chat (`chat_quickstart.py`)
    - `02` SDK rask start med OpenAI/Foundry Local og Azure OpenAI-støtte (`sdk_quickstart.py`)
    - `03` CLI liste-og-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Multi-agent orkestrering (`python -m samples.05.agents.coordinator`)
    - `06` Modeller-som-verktøy router (`router.py`)
- Azure OpenAI-støtte i Session 2 SDK-eksempel med miljøvariabelkonfigurasjon
- `.vscode/settings.json` peker til `Module08/.venv` for å forbedre Python-analyseoppløsning
- `.env` med `PYTHONPATH` hint for VS Code/Pylance-bevissthet

### Endret
- Standardmodell oppdatert til `phi-4-mini` i Modul 08-dokumentasjon og eksempler; fjernet gjenværende referanser til `phi-3.5` i Modul 08
- Router (`Module08/samples/06/router.py`) forbedringer:
  - Endepunktoppdagelse via `foundry service status` med regex-parsing
  - `/v1/models` helsesjekk ved oppstart
  - Miljøkonfigurerbar modellregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Krav oppdatert: `Module08/requirements.txt` inkluderer nå `openai` (sammen med `requests`, `chainlit`)
- Chainlit-eksempelveiledning klargjort og feilsøking lagt til; importoppløsning via arbeidsområdets innstillinger

### Fikset
- Løste importproblemer:
  - Router avhenger ikke lenger av en ikke-eksisterende `utils`-modul; funksjoner er inlinet
  - Koordinator bruker relativ import (`from .specialists import ...`) og kalles via modulsti
  - VS Code/Pylance-konfigurasjon for å løse `chainlit` og pakkeimporter
- Rettet mindre skrivefeil i `STUDY_GUIDE.md` og la til Modul 08-dekning

### Fjernet
- Slettet ubrukt `Module08/infra/obs.py` og fjernet den tomme `infra/`-mappen; observasjonsmønstre beholdt som valgfrie i dokumentasjonen

### Flyttet
- Konsoliderte Modul 08-demoer under `Module08/samples` med øktnummererte mapper
  - Flyttet Chainlit-app til `samples/04`
  - Flyttet agenter til `samples/05` og la til `__init__.py`-filer for pakkeoppløsning

### Dokumentasjon
- Modul 08-øktdokumentasjon og alle eksempel-README-er beriket med Microsoft Learn og pålitelige leverandørreferanser
- `Module08/README.md` oppdatert med oversikt over eksempler, router-konfigurasjon og valideringstips
- `Module07/README.md` Windows Foundry Local-seksjon validert mot Learn-dokumentasjon
- `STUDY_GUIDE.md` oppdatert:
  - La til Modul 08 i oversikt, tidsplaner, fremdriftssporing
  - La til omfattende Referanseseksjon (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisk (sammendrag)
- Kursarkitektur og moduler etablert (Moduler 01–07)
- Iterativ modernisering av innhold, standardisering av formatering og tilføyde casestudier
- Utvidet dekning av optimaliseringsrammeverk (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Uutgitt / Backlog (forslag)
- Valgfrie røyktester per eksempel for å validere Foundry Local tilgjengelighet
- Gjennomgå oversettelser for å tilpasse modellreferanser (f.eks. `phi-4-mini`) der det er relevant
- Legg til minimal pyright-konfigurasjon hvis team foretrekker strenghet på tvers av arbeidsområdet

---

