<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T14:10:18+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "no"
}
-->
# Endringslogg

Alle vesentlige endringer i EdgeAI for Beginners er dokumentert her. Dette prosjektet bruker dato-baserte oppføringer og følger stilen til Keep a Changelog (Lagt til, Endret, Fikset, Fjernet, Dokumentasjon, Flyttet).

## 2025-10-08

### Lagt til - Omfattende oppdatering av workshop
- **Fullstendig omskriving av Workshop README.md**:
  - Lagt til en omfattende introduksjon som forklarer verdien av Edge AI (personvern, ytelse, kostnad)
  - Opprettet 6 kjerne-læringsmål med detaljerte kompetanser
  - Lagt til en tabell over læringsutbytte med leveranser og kompetansematrise
  - Inkludert en seksjon om karriereklare ferdigheter for bransjerelevans
  - Lagt til en hurtigstartguide med forutsetninger og 3-trinns oppsett
  - Opprettet ressurs-tabeller for Python-eksempler (8 filer med kjøretider)
  - Lagt til en tabell for Jupyter-notebooks (8 notebooks med vanskelighetsgrader)
  - Opprettet en dokumentasjonstabell (7 nøkkeldokumenter med "Bruk når"-veiledning)
  - Lagt til anbefalinger for læringsstier for ulike ferdighetsnivåer

- **Validerings- og testinfrastruktur for workshop**:
  - Opprettet `scripts/validate_samples.py` - Omfattende valideringsverktøy for syntaks, imports og beste praksis
  - Opprettet `scripts/test_samples.py` - Smoke-test for alle Python-eksempler
  - Lagt til valideringsdokumentasjon i `scripts/README.md`

- **Omfattende dokumentasjon**:
  - Opprettet `SAMPLES_UPDATE_SUMMARY.md` - 400+ linjer detaljert veiledning som dekker alle forbedringer
  - Opprettet `UPDATE_COMPLETE.md` - Sammendrag av oppdateringens fullføring
  - Opprettet `QUICK_REFERENCE.md` - Hurtigreferansekort for workshop

### Endret - Modernisering av Python-eksempler i workshop
- **Alle 8 Python-eksempler oppdatert med beste praksis**:
  - Forbedret feilhåndtering med try-except-blokker rundt alle I/O-operasjoner
  - Lagt til typehinting og omfattende docstrings
  - Implementert konsistent [INFO]/[ERROR]/[RESULT]-loggmønster
  - Beskyttet valgfrie imports med installasjonsveiledning
  - Forbedret brukerfeedback i alle eksempler

- **session01/chat_bootstrap.py**:
  - Forbedret klientinitialisering med omfattende feilmeldinger
  - Forbedret feilhåndtering for streaming med validering av chunks
  - Lagt til bedre unntakshåndtering for tjenesteutilgjengelighet

- **session02/rag_pipeline.py**:
  - Lagt til importbeskyttelse for sentence-transformers med installasjonsveiledning
  - Forbedret feilhåndtering for embedding- og genereringsoperasjoner
  - Forbedret output-format med strukturerte resultater

- **session02/rag_eval_ragas.py**:
  - Beskyttet valgfrie imports (ragas, datasets) med brukervennlige feilmeldinger
  - Lagt til feilhåndtering for evalueringsmetrikker
  - Forbedret output-format for evalueringsresultater

- **session03/benchmark_oss_models.py**:
  - Implementert grasiøs degradering (fortsetter ved modellfeil)
  - Lagt til detaljert fremdriftsrapportering og feilhåndtering per modell
  - Forbedret statistikkberegning med omfattende feilgjenoppretting

- **session04/model_compare.py**:
  - Lagt til typehinting (Tuple-returtyper)
  - Forbedret output-format med strukturerte JSON-resultater
  - Implementert feilhåndtering per modell med gjenoppretting

- **session05/agents_orchestrator.py**:
  - Forbedret Agent.act() med omfattende docstrings
  - Lagt til feilhåndtering i pipeline med logging for hvert steg
  - Forbedret minnehåndtering og tilstandssporing

- **session06/models_router.py**:
  - Forbedret funksjonsdokumentasjon for alle rutekomponenter
  - Lagt til detaljert logging i route()-funksjonen
  - Forbedret testoutput med strukturerte resultater

- **session06/models_pipeline.py**:
  - Lagt til feilhåndtering i chat()-hjelpefunksjonen
  - Forbedret pipeline() med logging for hvert steg og fremdriftsrapportering
  - Forbedret main() med omfattende feilgjenoppretting

### Dokumentasjon - Forbedring av workshop-dokumentasjon
- Oppdatert hoved-README.md med workshop-seksjon som fremhever praktisk læringssti
- Forbedret STUDY_GUIDE.md med omfattende workshop-seksjon inkludert:
  - Læringsmål og fokusområder for studier
  - Selv-evalueringsspørsmål
  - Praktiske øvelser med tidsestimater
  - Tidsallokering for konsentrert og deltidsstudie
  - Lagt til workshop i fremdriftssporingsmal
- Oppdatert tidsallokeringsveiledning fra 20 timer til 30 timer (inkludert workshop)
- Lagt til beskrivelser av workshop-eksempler og læringsutbytte i README

### Fikset
- Løst inkonsekvente mønstre for feilhåndtering i workshop-eksempler
- Fikset feil med valgfrie avhengighetsimports ved å legge til riktige beskyttelser
- Rettet manglende typehinting i kritiske funksjoner
- Adressert utilstrekkelig brukerfeedback i feilscenarier
- Fikset valideringsproblemer med omfattende testinfrastruktur

---

## 2025-09-23

### Endret - Større modernisering av Modul 08
- **Omfattende tilpasning til Microsoft Foundry-Local repository-mønstre**
  - Oppdatert alle kodeeksempler til å bruke moderne `FoundryLocalManager` og OpenAI SDK-integrasjon
  - Erstattet utdaterte manuelle `requests`-kall med korrekt SDK-bruk
  - Tilpasset implementeringsmønstre til offisiell Microsoft-dokumentasjon og eksempler

- **05.AIPoweredAgents.md modernisering**:
  - Oppdatert multi-agent orkestrering til å bruke moderne SDK-mønstre
  - Forbedret koordinatorimplementering med avanserte funksjoner (feedback-loops, ytelsesovervåking)
  - Lagt til omfattende feilhåndtering og helsesjekk for tjenester
  - Integrert riktige referanser til lokale eksempler (`samples/05/multi_agent_orchestration.ipynb`)
  - Oppdatert funksjonskalleksempler til å bruke moderne `tools`-parameter i stedet for utdaterte `functions`
  - Lagt til produksjonsklare mønstre med overvåking og statistikksporing

- **06.ModelsAsTools.md full omskriving**:
  - Erstattet grunnleggende verktøyregister med intelligent modellruter-implementering
  - Lagt til nøkkelordbasert modellvalg for ulike oppgavetyper (generelt, resonnering, kode, kreativt)
  - Integrert miljøbasert konfigurasjon med fleksibel modelltilordning
  - Forbedret med omfattende helsesjekk for tjenester og feilhåndtering
  - Lagt til produksjonsutsettingsmønstre med forespørselsovervåking og ytelsessporing
  - Tilpasset til lokal implementering i `samples/06/router.py` og `samples/06/model_router.ipynb`

- **Forbedringer i dokumentasjonsstruktur**:
  - Lagt til oversiktsseksjoner som fremhever modernisering og SDK-tilpasning
  - Forbedret med emojis og bedre formatering for økt lesbarhet
  - Lagt til riktige referanser til lokale eksempel-filer gjennom dokumentasjonen
  - Inkludert veiledning for produksjonsklare implementeringer og beste praksis

### Lagt til
- Omfattende oversiktsseksjoner i Modul 08-filer som fremhever moderne SDK-integrasjon
- Arkitekturhøydepunkter som viser avanserte funksjoner (multi-agent-systemer, intelligent ruting)
- Direkte referanser til lokale eksempelimplementeringer for praktisk erfaring
- Veiledning for produksjonsutsetting med overvåking og feilhåndteringsmønstre
- Interaktive Jupyter-notebook-eksempler med avanserte funksjoner og benchmarks

### Fikset
- Uoverensstemmelser mellom dokumentasjon og faktiske eksempelimplementeringer
- Utdaterte SDK-bruksmønstre gjennom Modul 08
- Manglende referanser til omfattende lokal eksempelbibliotek
- Inkonsekvente implementeringsmetoder på tvers av ulike seksjoner

---

## 2025-09-18

### Lagt til
- Modul 08: Microsoft Foundry Local – Komplett utviklerverktøy
  - Seks sesjoner: oppsett, Azure AI Foundry-integrasjon, open-source-modeller, banebrytende demoer, agenter og modeller-som-verktøy
  - Kjørbare eksempler under `Module08/samples/01`–`06` med Windows cmd-instruksjoner
    - `01` REST hurtigchat (`chat_quickstart.py`)
    - `02` SDK hurtigstart med OpenAI/Foundry Local og Azure OpenAI-støtte (`sdk_quickstart.py`)
    - `03` CLI liste-og-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Multi-agent orkestrering (`python -m samples.05.agents.coordinator`)
    - `06` Modeller-som-verktøy ruter (`router.py`)
- Azure OpenAI-støtte i Session 2 SDK-eksempel med miljøvariabelkonfigurasjon
- `.vscode/settings.json` for å peke til `Module08/.venv` og forbedre Python-analyseoppløsning
- `.env` med `PYTHONPATH`-hint for VS Code/Pylance-bevissthet

### Endret
- Standardmodell oppdatert til `phi-4-mini` gjennom Modul 08-dokumenter og eksempler; fjernet gjenværende `phi-3.5`-referanser i Modul 08
- Router (`Module08/samples/06/router.py`) forbedringer:
  - Endepunktoppdagelse via `foundry service status` med regex-parsing
  - `/v1/models` helsesjekk ved oppstart
  - Miljøkonfigurerbart modellregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Krav oppdatert: `Module08/requirements.txt` inkluderer nå `openai` (sammen med `requests`, `chainlit`)
- Chainlit-eksempelveiledning klargjort og feilsøking lagt til; importoppløsning via arbeidsområdets innstillinger

### Fikset
- Løst importproblemer:
  - Router avhenger ikke lenger av en ikke-eksisterende `utils`-modul; funksjoner er inlinet
  - Koordinator bruker relativ import (`from .specialists import ...`) og kalles via modulsti
  - VS Code/Pylance-konfigurasjon for å løse `chainlit` og pakkeimports
- Rettet mindre skrivefeil i `STUDY_GUIDE.md` og lagt til Modul 08-dekning

### Fjernet
- Slettet ubrukt `Module08/infra/obs.py` og fjernet den tomme `infra/`-mappen; observasjonsmønstre beholdt som valgfrie i dokumentasjonen

### Flyttet
- Konsolidert Modul 08-demoer under `Module08/samples` med sesjonsnummererte mapper
  - Flyttet Chainlit-app til `samples/04`
  - Flyttet agenter til `samples/05` og lagt til `__init__.py`-filer for pakkeoppløsning

### Dokumentasjon
- Modul 08-sesjonsdokumenter og alle eksempel-README-er beriket med Microsoft Learn og pålitelige leverandørreferanser
- `Module08/README.md` oppdatert med oversikt over eksempler, router-konfigurasjon og valideringstips
- `Module07/README.md` Windows Foundry Local-seksjon validert mot Learn-dokumenter
- `STUDY_GUIDE.md` oppdatert:
  - Lagt til Modul 08 i oversikt, tidsplaner, fremdriftssporing
  - Lagt til omfattende referanseseksjon (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisk (sammendrag)
- Kursarkitektur og moduler etablert (Moduler 01–07)
- Iterativ modernisering av innhold, standardisering av formatering og tilføyelse av casestudier
- Utvidet dekning av optimaliseringsrammeverk (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Uutgitt / Backlog (forslag)
- Valgfrie smoke-tester per eksempel for å validere Foundry Local tilgjengelighet
- Gjennomgå oversettelser for å tilpasse modellreferanser (f.eks. `phi-4-mini`) der det er relevant
- Legg til minimal pyright-konfigurasjon hvis team foretrekker strenghet på arbeidsområdenivå

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.