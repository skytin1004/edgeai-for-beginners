<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T12:41:35+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sv"
}
-->
# Ändringslogg

Alla betydande ändringar i EdgeAI för Nybörjare dokumenteras här. Detta projekt använder datum-baserade poster och stilen "Keep a Changelog" (Lagt till, Ändrat, Fixat, Borttaget, Dokumentation, Flyttat).

## 2025-10-08

### Lagt till - Omfattande Workshop-uppdatering
- **Workshop README.md omskriven**:
  - Lagt till en omfattande introduktion som förklarar Edge AI:s värde (integritet, prestanda, kostnad)
  - Skapat 6 kärnkompetenser med detaljerade lärandemål
  - Lagt till en tabell över lärandemål med leveranser och kompetensmatris
  - Inkluderat en sektion om karriärfärdigheter för branschrelevans
  - Lagt till en snabbstartsguide med förutsättningar och 3-stegsinstallation
  - Skapat resurstabeller för Python-exempel (8 filer med körtider)
  - Lagt till en tabell för Jupyter-notebooks (8 notebooks med svårighetsgrader)
  - Skapat en dokumentationstabell (7 viktiga dokument med "Använd När"-vägledning)
  - Lagt till rekommendationer för lärandespår för olika kompetensnivåer

- **Workshop validerings- och testinfrastruktur**:
  - Skapat `scripts/validate_samples.py` - Omfattande valideringsverktyg för syntax, imports och bästa praxis
  - Skapat `scripts/test_samples.py` - Snabbtest för alla Python-exempel
  - Lagt till valideringsdokumentation i `scripts/README.md`

- **Omfattande dokumentation**:
  - Skapat `SAMPLES_UPDATE_SUMMARY.md` - 400+ rader detaljerad guide som täcker alla förbättringar
  - Skapat `UPDATE_COMPLETE.md` - Sammanfattning av uppdateringens slutförande
  - Skapat `QUICK_REFERENCE.md` - Snabbreferenskort för Workshop

### Ändrat - Modernisering av Python-exempel i Workshop
- **Alla 8 Python-exempel uppdaterade med bästa praxis**:
  - Förbättrad felhantering med try-except-block runt alla I/O-operationer
  - Lagt till typanvisningar och omfattande docstrings
  - Implementerat konsekvent [INFO]/[ERROR]/[RESULT]-loggningsmönster
  - Skyddat valfria imports med installationsanvisningar
  - Förbättrad användarfeedback i alla exempel

- **session01/chat_bootstrap.py**:
  - Förbättrad klientinitialisering med omfattande felmeddelanden
  - Förbättrad felhantering vid streaming med validering av chunkar
  - Lagt till bättre undantagshantering för tjänsteotillgänglighet

- **session02/rag_pipeline.py**:
  - Lagt till importskydd för sentence-transformers med installationsanvisningar
  - Förbättrad felhantering för embedding- och genereringsoperationer
  - Förbättrad utdataformatering med strukturerade resultat

- **session02/rag_eval_ragas.py**:
  - Skyddat valfria imports (ragas, datasets) med användarvänliga felmeddelanden
  - Lagt till felhantering för utvärderingsmått
  - Förbättrad utdataformatering för utvärderingsresultat

- **session03/benchmark_oss_models.py**:
  - Implementerat graciös nedtrappning (fortsätter vid modellfel)
  - Lagt till detaljerad framstegsrapportering och felhantering per modell
  - Förbättrad statistikberäkning med omfattande felåterhämtning

- **session04/model_compare.py**:
  - Lagt till typanvisningar (Tuple-returtyper)
  - Förbättrad utdataformatering med strukturerade JSON-resultat
  - Implementerat felhantering per modell med återhämtning

- **session05/agents_orchestrator.py**:
  - Förbättrad Agent.act() med omfattande docstrings
  - Lagt till felhantering i pipeline med steg-för-steg-loggning
  - Förbättrad minneshantering och spårning av tillstånd

- **session06/models_router.py**:
  - Förbättrad funktionsdokumentation för alla routingkomponenter
  - Lagt till detaljerad loggning i route()-funktionen
  - Förbättrad testutdata med strukturerade resultat

- **session06/models_pipeline.py**:
  - Lagt till felhantering i chat()-hjälpfunktionen
  - Förbättrad pipeline() med stegloggning och framstegsrapportering
  - Förbättrad main() med omfattande felåterhämtning

### Dokumentation - Förbättring av Workshop-dokumentation
- Uppdaterad huvud-README.md med Workshop-sektion som lyfter fram praktiskt lärandespår
- Förbättrad STUDY_GUIDE.md med omfattande Workshop-sektion inklusive:
  - Lärandemål och fokusområden
  - Självbedömningsfrågor
  - Praktiska övningar med tidsuppskattningar
  - Tidsallokering för koncentrerat och deltidsstudie
  - Lagt till Workshop i framstegsspårningsmall
- Uppdaterad tidsallokeringsguide från 20 timmar till 30 timmar (inklusive Workshop)
- Lagt till beskrivningar av Workshop-exempel och lärandemål i README

### Fixat
- Löste inkonsekventa felhanteringsmönster i Workshop-exempel
- Fixade fel vid valfria beroendeimports med korrekta skydd
- Korrigerade saknade typanvisningar i kritiska funktioner
- Åtgärdade otillräcklig användarfeedback vid fel
- Fixade valideringsproblem med omfattande testinfrastruktur

---

## 2025-09-23

### Ändrat - Större modernisering av Modul 08
- **Omfattande anpassning till Microsoft Foundry-Local repository-mönster**:
  - Uppdaterade alla kodexempel för att använda moderna `FoundryLocalManager` och OpenAI SDK-integration
  - Ersatte föråldrade manuella `requests`-anrop med korrekt SDK-användning
  - Anpassade implementeringsmönster till officiell Microsoft-dokumentation och exempel

- **05.AIPoweredAgents.md modernisering**:
  - Uppdaterade multi-agent orkestrering för att använda moderna SDK-mönster
  - Förbättrad koordinatorimplementering med avancerade funktioner (feedback-loopar, prestandaövervakning)
  - Lagt till omfattande felhantering och kontroll av tjänstehälsa
  - Integrerat korrekta referenser till lokala exempel (`samples/05/multi_agent_orchestration.ipynb`)
  - Uppdaterade funktionsanropsexempel för att använda moderna `tools`-parametrar istället för föråldrade `functions`
  - Lagt till produktionsklara mönster med övervakning och statistikspårning

- **06.ModelsAsTools.md omskriven**:
  - Ersatte grundläggande verktygsregister med intelligent modellrouter-implementering
  - Lagt till nyckelordsbaserad modellval för olika uppgiftstyper (generell, resonemang, kod, kreativ)
  - Integrerat miljöbaserad konfiguration med flexibel modelltilldelning
  - Förbättrad med omfattande övervakning av tjänstehälsa och felhantering
  - Lagt till produktionsimplementeringsmönster med begäranövervakning och prestandaspårning
  - Anpassad till lokal implementering i `samples/06/router.py` och `samples/06/model_router.ipynb`

- **Förbättringar av dokumentationsstruktur**:
  - Lagt till översiktssektioner som lyfter fram modernisering och SDK-anpassning
  - Förbättrad med emojis och bättre formatering för förbättrad läsbarhet
  - Lagt till korrekta referenser till lokala exempel genom hela dokumentationen
  - Inkluderat produktionsklara implementeringsvägledning och bästa praxis

### Lagt till
- Omfattande översiktssektioner i Modul 08-filer som lyfter fram modern SDK-integration
- Arkitekturhöjdpunkter som visar avancerade funktioner (multi-agent-system, intelligent routing)
- Direkta referenser till lokala exempel för praktisk erfarenhet
- Vägledning för produktionsimplementering med övervakning och felhanteringsmönster
- Interaktiva Jupyter-notebook-exempel med avancerade funktioner och benchmarks

### Fixat
- Anpassningsavvikelser mellan dokumentation och faktiska exempelimplementeringar
- Föråldrade SDK-användningsmönster genom hela Modul 08
- Saknade referenser till omfattande lokal exempelbibliotek
- Inkonsekventa implementeringsmetoder i olika sektioner

---

## 2025-09-18

### Lagt till
- Modul 08: Microsoft Foundry Local – Komplett utvecklarverktyg
  - Sex sessioner: installation, Azure AI Foundry-integration, open-source-modeller, avancerade demos, agenter och modeller-som-verktyg
  - Körbara exempel under `Module08/samples/01`–`06` med Windows cmd-instruktioner
    - `01` REST snabbchatt (`chat_quickstart.py`)
    - `02` SDK snabbstart med OpenAI/Foundry Local och Azure OpenAI-stöd (`sdk_quickstart.py`)
    - `03` CLI lista-och-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Multi-agent orkestrering (`python -m samples.05.agents.coordinator`)
    - `06` Modeller-som-verktyg router (`router.py`)
- Azure OpenAI-stöd i Session 2 SDK-exempel med miljövariabelkonfiguration
- `.vscode/settings.json` för att peka på `Module08/.venv` och förbättra Python-analysupplösning
- `.env` med `PYTHONPATH`-hint för VS Code/Pylance medvetenhet

### Ändrat
- Standardmodell uppdaterad till `phi-4-mini` genom Modul 08-dokument och exempel; tog bort kvarvarande `phi-3.5`-omnämnanden inom Modul 08
- Router (`Module08/samples/06/router.py`) förbättringar:
  - Endpoint-upptäckt via `foundry service status` med regex-parsing
  - `/v1/models` hälsokontroll vid start
  - Miljökonfigurerbart modellregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Krav uppdaterade: `Module08/requirements.txt` inkluderar nu `openai` (tillsammans med `requests`, `chainlit`)
- Chainlit-exempelvägledning förtydligad och felsökning tillagd; importupplösning via arbetsplatsinställningar

### Fixat
- Löste importproblem:
  - Router beror inte längre på en icke-existerande `utils`-modul; funktioner är inlinade
  - Koordinator använder relativ import (`from .specialists import ...`) och anropas via modulväg
  - VS Code/Pylance-konfiguration för att lösa `chainlit` och paketimports
- Korrigerade mindre stavfel i `STUDY_GUIDE.md` och lade till Modul 08-täckning

### Borttaget
- Tog bort oanvänd `Module08/infra/obs.py` och raderade den tomma `infra/`-katalogen; observabilitetsmönster behålls som valfria i dokumentationen

### Flyttat
- Konsoliderade Modul 08-demos under `Module08/samples` med sessionsnumrerade mappar
  - Flyttade Chainlit-app till `samples/04`
  - Flyttade agenter till `samples/05` och lade till `__init__.py`-filer för paketupplösning

### Dokumentation
- Modul 08-sessionsdokument och alla exempel-README:s berikade med Microsoft Learn och betrodda leverantörsreferenser
- `Module08/README.md` uppdaterad med Exempelöversikt, routerkonfiguration och valideringstips
- `Module07/README.md` Windows Foundry Local-sektion validerad mot Learn-dokument
- `STUDY_GUIDE.md` uppdaterad:
  - Lade till Modul 08 i översikt, scheman, framstegsspårare
  - Lade till omfattande Referenssektion (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historiskt (sammanfattning)
- Kursarkitektur och moduler etablerade (Moduler 01–07)
- Iterativ modernisering av innehåll, standardisering av formatering och tillagda fallstudier
- Utökad täckning av optimeringsramverk (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Ej släppt / Backlog (förslag)
- Valfria snabbtester per exempel för att validera Foundry Local tillgänglighet
- Granska översättningar för att anpassa modellreferenser (t.ex. `phi-4-mini`) där det är lämpligt
- Lägg till minimal pyright-konfiguration om team föredrar strikthet på arbetsplatsnivå

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.