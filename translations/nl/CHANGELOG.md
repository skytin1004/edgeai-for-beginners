<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T16:22:13+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "nl"
}
-->
# Changelog

Alle belangrijke wijzigingen aan EdgeAI for Beginners worden hier gedocumenteerd. Dit project gebruikt datumgebaseerde vermeldingen en de Keep a Changelog-stijl (Toegevoegd, Gewijzigd, Gerepareerd, Verwijderd, Documentatie, Verplaatst).

## 2025-10-08

### Toegevoegd - Uitgebreide Workshop Update
- **Volledige herschrijving van Workshop README.md**:
  - Toegevoegd uitgebreide introductie die de waarde van Edge AI uitlegt (privacy, prestaties, kosten)
  - Gecreëerd 6 kernleerdoelen met gedetailleerde competenties
  - Toegevoegd tabel met leerresultaten, deliverables en competentiematrix
  - Inclusief sectie met carrièregerichte vaardigheden voor relevantie in de industrie
  - Toegevoegd snelle startgids met vereisten en 3-staps installatie
  - Gecreëerd tabellen met bronnen voor Python-samples (8 bestanden met uitvoertijden)
  - Toegevoegd tabel met Jupyter-notebooks (8 notebooks met moeilijkheidsgraden)
  - Gecreëerd documentatietabel (7 belangrijke documenten met "Gebruik Wanneer"-richtlijnen)
  - Toegevoegd aanbevelingen voor leerpaden voor verschillende vaardigheidsniveaus

- **Validatie- en testinfrastructuur voor Workshop**:
  - Gecreëerd `scripts/validate_samples.py` - Uitgebreide validatietool voor syntax, imports en best practices
  - Gecreëerd `scripts/test_samples.py` - Smoke-test runner voor alle Python-samples
  - Toegevoegd validatiedocumentatie aan `scripts/README.md`

- **Uitgebreide documentatie**:
  - Gecreëerd `SAMPLES_UPDATE_SUMMARY.md` - Gedetailleerde gids van 400+ regels over alle verbeteringen
  - Gecreëerd `UPDATE_COMPLETE.md` - Samenvatting van de voltooiing van de update
  - Gecreëerd `QUICK_REFERENCE.md` - Snelle referentiekaart voor Workshop

### Gewijzigd - Modernisering van Workshop Python-samples
- **Alle 8 Python-samples bijgewerkt met best practices**:
  - Verbeterde foutafhandeling met try-except-blokken rond alle I/O-operaties
  - Toegevoegd type hints en uitgebreide docstrings
  - Geïmplementeerd consistent [INFO]/[ERROR]/[RESULT]-logpatroon
  - Optionele imports beschermd met installatie-instructies
  - Verbeterde gebruikersfeedback in alle samples

- **session01/chat_bootstrap.py**:
  - Verbeterde clientinitialisatie met uitgebreide foutmeldingen
  - Verbeterde foutafhandeling bij streaming met chunk-validatie
  - Toegevoegd betere uitzonderingafhandeling bij onbeschikbaarheid van de service

- **session02/rag_pipeline.py**:
  - Toegevoegd importguards voor sentence-transformers met installatie-instructies
  - Verbeterde foutafhandeling bij embedden en genereren
  - Verbeterde uitvoeropmaak met gestructureerde resultaten

- **session02/rag_eval_ragas.py**:
  - Optionele imports beschermd (ragas, datasets) met gebruiksvriendelijke foutmeldingen
  - Toegevoegd foutafhandeling voor evaluatiemetrics
  - Verbeterde uitvoeropmaak voor evaluatieresultaten

- **session03/benchmark_oss_models.py**:
  - Geïmplementeerd gratievol falen (gaat door bij modelstoringen)
  - Toegevoegd gedetailleerde voortgangsrapportage en foutafhandeling per model
  - Verbeterde statistiekberekening met uitgebreide foutherstel

- **session04/model_compare.py**:
  - Toegevoegd type hints (Tuple-retourtypes)
  - Verbeterde uitvoeropmaak met gestructureerde JSON-resultaten
  - Geïmplementeerd foutafhandeling per model met herstel

- **session05/agents_orchestrator.py**:
  - Verbeterde Agent.act() met uitgebreide docstrings
  - Toegevoegd pijplijnfoutafhandeling met logging per fase
  - Verbeterd geheugenbeheer en statustracking

- **session06/models_router.py**:
  - Verbeterde functiedocumentatie voor alle routeringscomponenten
  - Toegevoegd gedetailleerde logging in de route()-functie
  - Verbeterde testuitvoer met gestructureerde resultaten

- **session06/models_pipeline.py**:
  - Toegevoegd foutafhandeling aan de chat()-helperfunctie
  - Verbeterde pipeline() met logging per fase en voortgangsrapportage
  - Verbeterde main() met uitgebreide foutherstel

### Documentatie - Verbetering van Workshop-documentatie
- Hoofd-README.md bijgewerkt met Workshop-sectie die hands-on leerpad benadrukt
- STUDY_GUIDE.md verbeterd met uitgebreide Workshop-sectie inclusief:
  - Leerdoelen en studiefocusgebieden
  - Zelfbeoordelingsvragen
  - Hands-on oefeningen met tijdschattingen
  - Tijdstoewijzing voor geconcentreerde en deeltijdstudie
  - Toegevoegd Workshop aan voortgangstrackingtemplate
- Tijdstoewijzingsgids bijgewerkt van 20 uur naar 30 uur (inclusief Workshop)
- Toegevoegd beschrijvingen van Workshop-samples en leerresultaten aan README

### Gerepareerd
- Opgelost inconsistente foutafhandelingspatronen in Workshop-samples
- Fout bij optionele afhankelijkheidsimports opgelost met juiste guards
- Ontbrekende type hints in kritieke functies gecorrigeerd
- Onvoldoende gebruikersfeedback in foutscenario's aangepakt
- Validatieproblemen opgelost met uitgebreide testinfrastructuur

---

## 2025-09-23

### Gewijzigd - Grote modernisering van Module 08
- **Uitgebreide afstemming met Microsoft Foundry-Local repositorypatronen**:
  - Alle codevoorbeelden bijgewerkt om moderne `FoundryLocalManager` en OpenAI SDK-integratie te gebruiken
  - Verouderde handmatige `requests`-aanroepen vervangen door juiste SDK-gebruik
  - Implementatiepatronen afgestemd op officiële Microsoft-documentatie en voorbeelden

- **05.AIPoweredAgents.md modernisering**:
  - Multi-agent orkestratie bijgewerkt om moderne SDK-patronen te gebruiken
  - Coördinatorimplementatie verbeterd met geavanceerde functies (feedbackloops, prestatiemonitoring)
  - Toegevoegd uitgebreide foutafhandeling en servicegezondheidscontrole
  - Correcte verwijzingen naar lokale samples geïntegreerd (`samples/05/multi_agent_orchestration.ipynb`)
  - Functieaanroepvoorbeelden bijgewerkt om moderne `tools`-parameter te gebruiken in plaats van verouderde `functions`
  - Toegevoegd productieklare patronen met monitoring en statistiektracking

- **06.ModelsAsTools.md volledige herschrijving**:
  - Basis tool registry vervangen door intelligente modelrouterimplementatie
  - Toegevoegd trefwoordgebaseerde modelselectie voor verschillende taaktypes (algemeen, redeneren, code, creatief)
  - Geïntegreerde configuratie op basis van omgeving met flexibele modeltoewijzing
  - Verbeterd met uitgebreide servicegezondheidsmonitoring en foutafhandeling
  - Toegevoegd productie-implementatiepatronen met verzoekmonitoring en prestatiemonitoring
  - Afgestemd op lokale implementatie in `samples/06/router.py` en `samples/06/model_router.ipynb`

- **Verbeteringen in documentatiestructuur**:
  - Overzichtsecties toegevoegd die modernisering en SDK-afstemming benadrukken
  - Verbeterd met emoji's en betere opmaak voor verbeterde leesbaarheid
  - Correcte verwijzingen naar lokale samplebestanden toegevoegd in de documentatie
  - Inclusief productieklare implementatierichtlijnen en best practices

### Toegevoegd
- Uitgebreide overzichtsecties in Module 08-bestanden die moderne SDK-integratie benadrukken
- Architectuurhoogtepunten met geavanceerde functies (multi-agentsystemen, intelligente routering)
- Directe verwijzingen naar lokale sample-implementaties voor hands-on ervaring
- Productie-implementatierichtlijnen met monitoring en foutafhandelingspatronen
- Interactieve Jupyter-notebookvoorbeelden met geavanceerde functies en benchmarks

### Gerepareerd
- Afstemmingsverschillen tussen documentatie en daadwerkelijke sample-implementaties
- Verouderde SDK-gebruikspatronen in Module 08
- Ontbrekende verwijzingen naar uitgebreide lokale samplebibliotheek
- Inconsistente implementatiebenaderingen in verschillende secties

---

## 2025-09-18

### Toegevoegd
- Module 08: Microsoft Foundry Local – Complete ontwikkelaarstoolkit
  - Zes sessies: setup, Azure AI Foundry-integratie, open-source modellen, geavanceerde demo's, agents en modellen-als-tools
  - Uitvoerbare samples onder `Module08/samples/01`–`06` met Windows cmd-instructies
    - `01` REST snelle chat (`chat_quickstart.py`)
    - `02` SDK quickstart met OpenAI/Foundry Local en Azure OpenAI-ondersteuning (`sdk_quickstart.py`)
    - `03` CLI lijst-en-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Multi-agent orkestratie (`python -m samples.05.agents.coordinator`)
    - `06` Modellen-als-tools router (`router.py`)
- Azure OpenAI-ondersteuning in Session 2 SDK-sample met configuratie van omgevingsvariabelen
- `.vscode/settings.json` om te wijzen naar `Module08/.venv` en Python-analyseoplossing te verbeteren
- `.env` met `PYTHONPATH` hint voor VS Code/Pylance-bewustzijn

### Gewijzigd
- Standaardmodel bijgewerkt naar `phi-4-mini` in Module 08-documenten en samples; resterende vermeldingen van `phi-3.5` verwijderd binnen Module 08
- Router (`Module08/samples/06/router.py`) verbeteringen:
  - Endpointdetectie via `foundry service status` met regex-parsing
  - `/v1/models` gezondheidscontrole bij opstarten
  - Omgevingsconfigureerbare modelregistry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Vereisten bijgewerkt: `Module08/requirements.txt` bevat nu `openai` (naast `requests`, `chainlit`)
- Chainlit-sample richtlijnen verduidelijkt en probleemoplossing toegevoegd; importoplossing via werkruimte-instellingen

### Gerepareerd
- Importproblemen opgelost:
  - Router is niet langer afhankelijk van een niet-bestaande `utils`-module; functies zijn inlined
  - Coördinator gebruikt relatieve import (`from .specialists import ...`) en wordt aangeroepen via modulepad
  - VS Code/Pylance-configuratie om `chainlit` en pakketimports op te lossen
- Kleine typfout gecorrigeerd in `STUDY_GUIDE.md` en Module 08-dekking toegevoegd

### Verwijderd
- Ongebruikte `Module08/infra/obs.py` verwijderd en de lege `infra/`-map verwijderd; observatiepatronen behouden als optioneel in documentatie

### Verplaatst
- Module 08-demo's geconsolideerd onder `Module08/samples` met sessienummer-mappen
  - Chainlit-app verplaatst naar `samples/04`
  - Agents verplaatst naar `samples/05` en `__init__.py`-bestanden toegevoegd voor pakketoplossing

### Documentatie
- Module 08-sessiedocumenten en alle sample-README's verrijkt met Microsoft Learn en vertrouwde leveranciersverwijzingen
- `Module08/README.md` bijgewerkt met Samples Overzicht, routerconfiguratie en validatietips
- `Module07/README.md` Windows Foundry Local-sectie gevalideerd tegen Learn-documenten
- `STUDY_GUIDE.md` bijgewerkt:
  - Module 08 toegevoegd aan overzicht, schema's, voortgangstracker
  - Toegevoegd uitgebreide Referentiesectie (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisch (samenvatting)
- Cursusarchitectuur en modules vastgesteld (Modules 01–07)
- Iteratieve modernisering van inhoud, standaardisatie van opmaak en toegevoegde casestudies
- Uitgebreide dekking van optimalisatieframeworks (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Niet uitgebracht / Backlog (voorstellen)
- Optionele smoke-tests per sample om Foundry Local-beschikbaarheid te valideren
- Vertalingen herzien om modelverwijzingen af te stemmen (bijv. `phi-4-mini`) waar nodig
- Minimale pyright-configuratie toevoegen als teams voorkeur geven aan werkruimtebrede strengheid

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.