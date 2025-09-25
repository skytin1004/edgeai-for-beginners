<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T23:49:31+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "nl"
}
-->
# Changelog

Alle belangrijke wijzigingen aan EdgeAI for Beginners worden hier gedocumenteerd. Dit project gebruikt datumgebaseerde vermeldingen en de Keep a Changelog-stijl (Toegevoegd, Gewijzigd, Gerepareerd, Verwijderd, Documentatie, Verplaatst).

## 2025-09-23

### Gewijzigd - Grote modernisering van Module 08
- **Uitgebreide afstemming met Microsoft Foundry-Local repository-patronen**
  - Alle codevoorbeelden bijgewerkt om moderne `FoundryLocalManager` en OpenAI SDK-integratie te gebruiken
  - Verouderde handmatige `requests`-aanroepen vervangen door correcte SDK-gebruik
  - Implementatiepatronen afgestemd op officiële Microsoft-documentatie en voorbeelden

- **Modernisering van 05.AIPoweredAgents.md**:
  - Multi-agent orkestratie bijgewerkt om moderne SDK-patronen te gebruiken
  - Coördinatorimplementatie verbeterd met geavanceerde functies (feedbackloops, prestatiemonitoring)
  - Uitgebreide foutafhandeling en controle van de gezondheid van services toegevoegd
  - Correcte verwijzingen naar lokale voorbeelden geïntegreerd (`samples/05/multi_agent_orchestration.ipynb`)
  - Voorbeelden van functieaanroepen bijgewerkt om moderne `tools`-parameter te gebruiken in plaats van verouderde `functions`
  - Productieklare patronen toegevoegd met monitoring en statistiektracking

- **Volledige herschrijving van 06.ModelsAsTools.md**:
  - Basis tool registry vervangen door intelligente modelrouterimplementatie
  - Trefwoordgebaseerde modelselectie toegevoegd voor verschillende taaktypes (algemeen, redeneren, code, creatief)
  - Geïntegreerde configuratie op basis van omgeving met flexibele modeltoewijzing
  - Verbeterd met uitgebreide servicegezondheidsmonitoring en foutafhandeling
  - Productie-implementatiepatronen toegevoegd met verzoekmonitoring en prestatie-tracking
  - Afgestemd op lokale implementatie in `samples/06/router.py` en `samples/06/model_router.ipynb`

- **Verbeteringen in documentatiestructuur**:
  - Overzichtsecties toegevoegd die modernisering en SDK-afstemming benadrukken
  - Verbeterd met emoji's en betere opmaak voor verbeterde leesbaarheid
  - Correcte verwijzingen naar lokale voorbeeldbestanden toegevoegd in de hele documentatie
  - Productieklare implementatierichtlijnen en best practices opgenomen

### Toegevoegd
- Uitgebreide overzichtsecties in Module 08-bestanden die moderne SDK-integratie benadrukken
- Architectuurhoogtepunten met geavanceerde functies (multi-agentsystemen, intelligente routering)
- Directe verwijzingen naar lokale voorbeeldimplementaties voor praktische ervaring
- Richtlijnen voor productie-implementatie met monitoring en foutafhandelingspatronen
- Interactieve Jupyter-notebookvoorbeelden met geavanceerde functies en benchmarks

### Gerepareerd
- Afstemmingsverschillen tussen documentatie en daadwerkelijke voorbeeldimplementaties
- Verouderde SDK-gebruikspatronen in de hele Module 08
- Ontbrekende verwijzingen naar uitgebreide lokale voorbeeldbibliotheek
- Inconsistente implementatiebenaderingen in verschillende secties

---

## 2025-09-18

### Toegevoegd
- Module 08: Microsoft Foundry Local – Complete ontwikkelaarstoolkit
  - Zes sessies: setup, Azure AI Foundry-integratie, open-source modellen, geavanceerde demo's, agents en modellen-als-tools
  - Uitvoerbare voorbeelden onder `Module08/samples/01`–`06` met Windows cmd-instructies
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart met OpenAI/Foundry Local en Azure OpenAI-ondersteuning (`sdk_quickstart.py`)
    - `03` CLI lijst-en-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Multi-agent orkestratie (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI-ondersteuning in Session 2 SDK-voorbeeld met configuratie van omgevingsvariabelen
- `.vscode/settings.json` om te verwijzen naar `Module08/.venv` en Python-analyse te verbeteren
- `.env` met `PYTHONPATH`-hint voor VS Code/Pylance-bewustzijn

### Gewijzigd
- Standaardmodel bijgewerkt naar `phi-4-mini` in de hele Module 08-documentatie en voorbeelden; resterende vermeldingen van `phi-3.5` verwijderd binnen Module 08
- Router (`Module08/samples/06/router.py`) verbeteringen:
  - Endpointdetectie via `foundry service status` met regex-parsing
  - `/v1/models` gezondheidscontrole bij opstarten
  - Omgevingsconfigureerbare modelregistry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Vereisten bijgewerkt: `Module08/requirements.txt` bevat nu `openai` (naast `requests`, `chainlit`)
- Chainlit-voorbeeldrichtlijnen verduidelijkt en probleemoplossing toegevoegd; importresolutie via werkruimte-instellingen

### Gerepareerd
- Importproblemen opgelost:
  - Router is niet langer afhankelijk van een niet-bestaande `utils`-module; functies zijn inlined
  - Coördinator gebruikt relatieve import (`from .specialists import ...`) en wordt aangeroepen via modulepad
  - VS Code/Pylance-configuratie om `chainlit` en pakketimporten op te lossen
- Kleine typfout gecorrigeerd in `STUDY_GUIDE.md` en Module 08-dekking toegevoegd

### Verwijderd
- Ongebruikte `Module08/infra/obs.py` verwijderd en de lege `infra/`-directory verwijderd; observatiepatronen behouden als optioneel in documentatie

### Verplaatst
- Module 08-demo's geconsolideerd onder `Module08/samples` met sessienummer-mappen
  - Chainlit-app verplaatst naar `samples/04`
  - Agents verplaatst naar `samples/05` en `__init__.py`-bestanden toegevoegd voor pakketresolutie

### Documentatie
- Module 08-sessiedocumentatie en alle voorbeeld-README's verrijkt met Microsoft Learn en vertrouwde leveranciersverwijzingen
- `Module08/README.md` bijgewerkt met Samples Overzicht, routerconfiguratie en validatietips
- `Module07/README.md` Windows Foundry Local-sectie gevalideerd tegen Learn-documentatie
- `STUDY_GUIDE.md` bijgewerkt:
  - Module 08 toegevoegd aan overzicht, schema's, voortgangstracker
  - Uitgebreide Referenties-sectie toegevoegd (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisch (samenvatting)
- Cursusarchitectuur en modules vastgesteld (Modules 01–07)
- Iteratieve inhoudsmodernisering, standaardisatie van opmaak en toegevoegde casestudies
- Uitgebreide dekking van optimalisatieframeworks (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Niet uitgebracht / Backlog (voorstellen)
- Optionele rooktests per voorbeeld om Foundry Local-beschikbaarheid te valideren
- Vertalingen herzien om modelverwijzingen af te stemmen (bijv. `phi-4-mini`) waar nodig
- Minimale pyright-configuratie toevoegen als teams voorkeur geven aan werkruimtebrede strengheid

---

