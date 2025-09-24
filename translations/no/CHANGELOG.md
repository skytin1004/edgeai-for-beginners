<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T23:16:05+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "no"
}
-->
# Endringslogg

Alle vesentlige endringer i EdgeAI for Beginners er dokumentert her. Dette prosjektet bruker dato-baserte oppføringer og Keep a Changelog-stil (Lagt til, Endret, Fikset, Fjernet, Dokumentasjon, Flyttet).

## 2025-09-23

### Endret - Større modernisering av Modul 08
- **Omfattende tilpasning til Microsoft Foundry-Local repository-mønstre**
  - Oppdatert alle kodeeksempler til å bruke moderne `FoundryLocalManager` og OpenAI SDK-integrasjon
  - Erstattet utdaterte manuelle `requests`-kall med korrekt SDK-bruk
  - Tilpasset implementeringsmønstre til offisiell Microsoft-dokumentasjon og eksempler

- **Modernisering av 05.AIPoweredAgents.md**:
  - Oppdatert multi-agent orkestrering til å bruke moderne SDK-mønstre
  - Forbedret koordinatorimplementering med avanserte funksjoner (feedback loops, ytelsesovervåking)
  - Lagt til omfattende feilhåndtering og helsesjekk for tjenester
  - Integrert riktige referanser til lokale eksempler (`samples/05/multi_agent_orchestration.ipynb`)
  - Oppdatert funksjonskalleksempler til å bruke moderne `tools`-parameter i stedet for utdaterte `functions`
  - Lagt til produksjonsklare mønstre med overvåking og statistikksporing

- **Fullstendig omskriving av 06.ModelsAsTools.md**:
  - Erstattet grunnleggende verktøyregister med intelligent modellruter-implementering
  - Lagt til nøkkelordbasert modellvalg for ulike oppgavetyper (generelt, resonnering, kode, kreativt)
  - Integrert miljøbasert konfigurasjon med fleksibel modelltilordning
  - Forbedret med omfattende tjenestehelseovervåking og feilhåndtering
  - Lagt til produksjonsutsettingsmønstre med forespørselsovervåking og ytelsessporing
  - Tilpasset lokal implementering i `samples/06/router.py` og `samples/06/model_router.ipynb`

- **Forbedringer i dokumentasjonsstruktur**:
  - Lagt til oversiktsseksjoner som fremhever modernisering og SDK-tilpasning
  - Forbedret med emojis og bedre formatering for økt lesbarhet
  - Lagt til riktige referanser til lokale eksempel-filer gjennom dokumentasjonen
  - Inkludert veiledning for produksjonsklare implementeringer og beste praksis

### Lagt til
- Omfattende oversiktsseksjoner i Modul 08-filer som fremhever moderne SDK-integrasjon
- Arkitekturhøydepunkter som viser avanserte funksjoner (multi-agent systemer, intelligent ruting)
- Direkte referanser til lokale eksempelimplementeringer for praktisk erfaring
- Veiledning for produksjonsutsetting med overvåking og feilhåndteringsmønstre
- Interaktive Jupyter-notebook-eksempler med avanserte funksjoner og benchmarks

### Fikset
- Uoverensstemmelser mellom dokumentasjon og faktiske eksempelimplementeringer
- Utdaterte SDK-bruksmønstre gjennom Modul 08
- Manglende referanser til omfattende lokal eksempelbibliotek
- Inkonsistente implementeringsmetoder på tvers av ulike seksjoner

---

## 2025-09-18

### Lagt til
- Modul 08: Microsoft Foundry Local – Komplett utviklerverktøysett
  - Seks sesjoner: oppsett, Azure AI Foundry-integrasjon, open-source modeller, banebrytende demoer, agenter og modeller-som-verktøy
  - Kjørbare eksempler under `Module08/samples/01`–`06` med Windows cmd-instruksjoner
    - `01` REST rask chat (`chat_quickstart.py`)
    - `02` SDK rask start med OpenAI/Foundry Local og Azure OpenAI-støtte (`sdk_quickstart.py`)
    - `03` CLI liste-og-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Multi-agent orkestrering (`python -m samples.05.agents.coordinator`)
    - `06` Modeller-som-verktøy ruter (`router.py`)
- Azure OpenAI-støtte i Sesjon 2 SDK-eksempel med miljøvariabelkonfigurasjon
- `.vscode/settings.json` for å peke til `Module08/.venv` og forbedre Python-analyseoppløsning
- `.env` med `PYTHONPATH`-hint for VS Code/Pylance-bevissthet

### Endret
- Standardmodell oppdatert til `phi-4-mini` på tvers av Modul 08-dokumenter og eksempler; fjernet gjenværende `phi-3.5`-referanser innen Modul 08
- Forbedringer i ruter (`Module08/samples/06/router.py`):
  - Endepunktoppdagelse via `foundry service status` med regex-parsing
  - `/v1/models` helsesjekk ved oppstart
  - Miljøkonfigurerbart modellregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Krav oppdatert: `Module08/requirements.txt` inkluderer nå `openai` (sammen med `requests`, `chainlit`)
- Veiledning for Chainlit-eksempel klargjort og feilsøking lagt til; importoppløsning via arbeidsområdets innstillinger

### Fikset
- Løste importproblemer:
  - Ruter avhenger ikke lenger av en ikke-eksisterende `utils`-modul; funksjoner er inlinet
  - Koordinator bruker relativ import (`from .specialists import ...`) og kalles via modulsti
  - VS Code/Pylance-konfigurasjon for å løse `chainlit` og pakkeimporter
- Rettet mindre skrivefeil i `STUDY_GUIDE.md` og la til dekning av Modul 08

### Fjernet
- Slettet ubrukt `Module08/infra/obs.py` og fjernet den tomme `infra/`-mappen; observasjonsmønstre beholdt som valgfrie i dokumentasjonen

### Flyttet
- Konsoliderte Modul 08-demoer under `Module08/samples` med sesjonsnummererte mapper
  - Flyttet Chainlit-app til `samples/04`
  - Flyttet agenter til `samples/05` og la til `__init__.py`-filer for pakkeoppløsning

### Dokumentasjon
- Modul 08-sesjonsdokumentasjon og alle eksempel-README-er beriket med Microsoft Learn og pålitelige leverandørreferanser
- `Module08/README.md` oppdatert med oversikt over eksempler, ruter-konfigurasjon og valideringstips
- `Module07/README.md` Windows Foundry Local-seksjon validert mot Learn-dokumentasjon
- `STUDY_GUIDE.md` oppdatert:
  - La til Modul 08 i oversikt, tidsplaner, fremdriftssporing
  - La til omfattende Referanseseksjon (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisk (sammendrag)
- Kursarkitektur og moduler etablert (Moduler 01–07)
- Iterativ innholdsmodernisering, formatstandardisering og tilføyde casestudier
- Utvidet dekning av optimaliseringsrammeverk (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Uutgitt / Backlog (forslag)
- Valgfrie røyktester per eksempel for å validere Foundry Local tilgjengelighet
- Gjennomgå oversettelser for å tilpasse modellreferanser (f.eks. `phi-4-mini`) der det er relevant
- Legg til minimal pyright-konfigurasjon hvis team foretrekker arbeidsområdebred strenghet

---

