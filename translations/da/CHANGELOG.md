<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T14:05:48+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "da"
}
-->
# Ændringslog

Alle væsentlige ændringer i EdgeAI for Beginners er dokumenteret her. Dette projekt bruger dato-baserede indgange og Keep a Changelog-stilen (Tilføjet, Ændret, Rettet, Fjernet, Dokumentation, Flyttet).

## 2025-10-08

### Tilføjet - Omfattende Workshop-opdatering
- **Workshop README.md fuldstændig omskrevet**:
  - Tilføjet omfattende introduktion, der forklarer Edge AI's værdi (privatliv, ydeevne, omkostninger)
  - Oprettet 6 kerne-læringsmål med detaljerede kompetencer
  - Tilføjet tabel over læringsresultater med leverancer og kompetencematrix
  - Inkluderet sektion om karriereklare færdigheder for branche-relevans
  - Tilføjet hurtig start-guide med forudsætninger og 3-trins opsætning
  - Oprettet ressource-tabeller for Python-eksempler (8 filer med køretider)
  - Tilføjet tabel over Jupyter-notebooks (8 notebooks med sværhedsgrader)
  - Oprettet dokumentationstabel (7 nøgle-dokumenter med "Brug Når"-vejledning)
  - Tilføjet anbefalinger til læringsstier for forskellige færdighedsniveauer

- **Workshop validerings- og testinfrastruktur**:
  - Oprettet `scripts/validate_samples.py` - Omfattende valideringsværktøj til syntaks, imports og bedste praksis
  - Oprettet `scripts/test_samples.py` - Smoke-test runner for alle Python-eksempler
  - Tilføjet valideringsdokumentation til `scripts/README.md`

- **Omfattende dokumentation**:
  - Oprettet `SAMPLES_UPDATE_SUMMARY.md` - 400+ linjer detaljeret guide, der dækker alle forbedringer
  - Oprettet `UPDATE_COMPLETE.md` - Executive summary af opdateringens færdiggørelse
  - Oprettet `QUICK_REFERENCE.md` - Hurtig referencekort til Workshop

### Ændret - Workshop Python-eksempler moderniseret
- **Alle 8 Python-eksempler opdateret med bedste praksis**:
  - Forbedret fejlhåndtering med try-except blokke omkring alle I/O-operationer
  - Tilføjet type hints og omfattende docstrings
  - Implementeret konsistent [INFO]/[ERROR]/[RESULT] logningsmønster
  - Beskyttet valgfrie imports med installationsvejledninger
  - Forbedret brugerfeedback i alle eksempler

- **session01/chat_bootstrap.py**:
  - Forbedret klientinitialisering med omfattende fejlmeddelelser
  - Forbedret streaming-fejlhåndtering med chunk-validering
  - Tilføjet bedre undtagelseshåndtering for tjenesteutilgængelighed

- **session02/rag_pipeline.py**:
  - Tilføjet import guards for sentence-transformers med installationsvejledninger
  - Forbedret fejlhåndtering for embedding- og genereringsoperationer
  - Forbedret outputformatering med strukturerede resultater

- **session02/rag_eval_ragas.py**:
  - Beskyttet valgfrie imports (ragas, datasets) med brugervenlige fejlmeddelelser
  - Tilføjet fejlhåndtering for evalueringsmetrikker
  - Forbedret outputformatering for evalueringsresultater

- **session03/benchmark_oss_models.py**:
  - Implementeret graceful degradation (fortsætter ved modelfejl)
  - Tilføjet detaljeret statusrapportering og fejlhåndtering pr. model
  - Forbedret statistikberegning med omfattende fejlgenopretning

- **session04/model_compare.py**:
  - Tilføjet type hints (Tuple returtyper)
  - Forbedret outputformatering med strukturerede JSON-resultater
  - Implementeret fejlhåndtering pr. model med genopretning

- **session05/agents_orchestrator.py**:
  - Forbedret Agent.act() med omfattende docstrings
  - Tilføjet pipeline-fejlhåndtering med trin-for-trin logning
  - Forbedret hukommelsesstyring og tilstandssporing

- **session06/models_router.py**:
  - Forbedret funktionsdokumentation for alle routing-komponenter
  - Tilføjet detaljeret logning i route()-funktionen
  - Forbedret testoutput med strukturerede resultater

- **session06/models_pipeline.py**:
  - Tilføjet fejlhåndtering til chat()-hjælpefunktionen
  - Forbedret pipeline() med trinlogning og statusrapportering
  - Forbedret main() med omfattende fejlgenopretning

### Dokumentation - Workshop dokumentationsforbedring
- Opdateret hoved-README.md med Workshop-sektion, der fremhæver hands-on læringssti
- Forbedret STUDY_GUIDE.md med omfattende Workshop-sektion, der inkluderer:
  - Læringsmål og fokusområder
  - Selv-evalueringsspørgsmål
  - Hands-on øvelser med tidsestimater
  - Tidsallokering for koncentreret og deltidsstudie
  - Tilføjet Workshop til fremskridts-sporingsskabelon
- Opdateret tidsallokeringsguide fra 20 timer til 30 timer (inklusive Workshop)
- Tilføjet Workshop-eksempeldeskriptioner og læringsresultater til README

### Rettet
- Løst inkonsistente mønstre for fejlhåndtering på tværs af Workshop-eksempler
- Rettet valgfrie afhængighedsimportfejl med korrekte guards
- Korrigeret manglende type hints i kritiske funktioner
- Adresseret utilstrækkelig brugerfeedback i fejlscenarier
- Rettet valideringsproblemer med omfattende testinfrastruktur

---

## 2025-09-23

### Ændret - Større modernisering af Modul 08
- **Omfattende tilpasning til Microsoft Foundry-Local repository-mønstre**:
  - Opdateret alle kodeeksempler til at bruge moderne `FoundryLocalManager` og OpenAI SDK-integration
  - Erstattet forældede manuelle `requests`-kald med korrekt SDK-brug
  - Tilpasset implementeringsmønstre til officiel Microsoft-dokumentation og eksempler

- **05.AIPoweredAgents.md modernisering**:
  - Opdateret multi-agent orkestrering til at bruge moderne SDK-mønstre
  - Forbedret koordinatorimplementering med avancerede funktioner (feedback loops, ydeevneovervågning)
  - Tilføjet omfattende fejlhåndtering og tjeneste-sundhedstjek
  - Integreret korrekte referencer til lokale eksempler (`samples/05/multi_agent_orchestration.ipynb`)
  - Opdateret funktionskaldseksempler til at bruge moderne `tools`-parameter i stedet for forældede `functions`
  - Tilføjet produktionsklare mønstre med overvågning og statistiksporing

- **06.ModelsAsTools.md fuldstændig omskrevet**:
  - Erstattet grundlæggende værktøjsregister med intelligent model-router implementering
  - Tilføjet nøgleordsbaseret modelvalg til forskellige opgavetyper (generel, ræsonnement, kode, kreativ)
  - Integreret miljøbaseret konfiguration med fleksibel modeltildeling
  - Forbedret med omfattende tjeneste-sundhedsovervågning og fejlhåndtering
  - Tilføjet produktionsudrulningsmønstre med anmodningsovervågning og ydeevnesporing
  - Tilpasset lokal implementering i `samples/06/router.py` og `samples/06/model_router.ipynb`

- **Forbedringer i dokumentationsstruktur**:
  - Tilføjet oversigtssektioner, der fremhæver modernisering og SDK-tilpasning
  - Forbedret med emojis og bedre formatering for forbedret læsbarhed
  - Tilføjet korrekte referencer til lokale prøvefiler i hele dokumentationen
  - Inkluderet produktionsklar implementeringsvejledning og bedste praksis

### Tilføjet
- Omfattende oversigtssektioner i Modul 08-filer, der fremhæver moderne SDK-integration
- Arkitekturhøjdepunkter, der viser avancerede funktioner (multi-agent systemer, intelligent routing)
- Direkte referencer til lokale prøveimplementeringer for hands-on erfaring
- Produktionsudrulningsvejledning med overvågnings- og fejlhåndteringsmønstre
- Interaktive Jupyter-notebook-eksempler med avancerede funktioner og benchmarks

### Rettet
- Tilpasningsforskelle mellem dokumentation og faktiske prøveimplementeringer
- Forældede SDK-brugsmønstre i hele Modul 08
- Manglende referencer til omfattende lokal prøvebibliotek
- Inkonsistente implementeringsmetoder på tværs af forskellige sektioner

---

## 2025-09-18

### Tilføjet
- Modul 08: Microsoft Foundry Local – Komplet udviklerværktøjssæt
  - Seks sessioner: opsætning, Azure AI Foundry-integration, open-source modeller, banebrydende demoer, agenter og modeller-som-værktøjer
  - Kørbare eksempler under `Module08/samples/01`–`06` med Windows cmd-instruktioner
    - `01` REST hurtig chat (`chat_quickstart.py`)
    - `02` SDK hurtigstart med OpenAI/Foundry Local og Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orkestrering (`python -m samples.05.agents.coordinator`)
    - `06` Modeller-som-værktøjer router (`router.py`)
- Azure OpenAI support i Session 2 SDK-eksempel med miljøvariabelkonfiguration
- `.vscode/settings.json` til at pege på `Module08/.venv` og forbedre Python-analyseopløsning
- `.env` med `PYTHONPATH` hint for VS Code/Pylance bevidsthed

### Ændret
- Standardmodel opdateret til `phi-4-mini` på tværs af Modul 08-dokumenter og eksempler; fjernet resterende `phi-3.5` omtaler inden for Modul 08
- Router (`Module08/samples/06/router.py`) forbedringer:
  - Endpoint-opdagelse via `foundry service status` med regex-parsing
  - `/v1/models` sundhedstjek ved opstart
  - Miljø-konfigurerbart modelregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Krav opdateret: `Module08/requirements.txt` inkluderer nu `openai` (sammen med `requests`, `chainlit`)
- Chainlit prøvevejledning præciseret og fejlfinding tilføjet; importopløsning via arbejdsområdets indstillinger

### Rettet
- Løst importproblemer:
  - Router afhænger ikke længere af et ikke-eksisterende `utils`-modul; funktioner er inlined
  - Koordinator bruger relativ import (`from .specialists import ...`) og kaldes via modulsti
  - VS Code/Pylance-konfiguration til at løse `chainlit` og pakkeimporter
- Korrigeret mindre stavefejl i `STUDY_GUIDE.md` og tilføjet Modul 08-dækning

### Fjernet
- Slettet ubrugte `Module08/infra/obs.py` og fjernet den tomme `infra/`-mappe; observabilitetsmønstre bevaret som valgfri i dokumentation

### Flyttet
- Konsolideret Modul 08-demoer under `Module08/samples` med session-nummererede mapper
  - Flyttet Chainlit-app til `samples/04`
  - Flyttet agenter til `samples/05` og tilføjet `__init__.py`-filer for pakkeopløsning

### Dokumentation
- Modul 08-sessionsdokumenter og alle prøve-README'er beriget med Microsoft Learn og betroede leverandørreferencer
- `Module08/README.md` opdateret med Samples Oversigt, router-konfiguration og valideringstips
- `Module07/README.md` Windows Foundry Local-sektion valideret mod Learn-dokumenter
- `STUDY_GUIDE.md` opdateret:
  - Tilføjet Modul 08 til oversigt, tidsplaner, fremskridts-tracker
  - Tilføjet omfattende Referencer-sektion (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisk (resumé)
- Kursusarkitektur og moduler etableret (Moduler 01–07)
- Iterativ indholdsmodernisering, formateringsstandardisering og tilføjede casestudier
- Udvidet dækning af optimeringsrammer (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Uudgivet / Backlog (forslag)
- Valgfrie smoke-tests pr. prøve for at validere Foundry Local tilgængelighed
- Gennemgå oversættelser for at tilpasse modelreferencer (f.eks. `phi-4-mini`) hvor det er relevant
- Tilføj minimal pyright-konfiguration, hvis teams foretrækker arbejdsområde-bred strenghed

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.