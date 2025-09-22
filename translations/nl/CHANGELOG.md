<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T21:46:49+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "nl"
}
-->
# Changelog

Alle belangrijke wijzigingen in EdgeAI voor Beginners worden hier gedocumenteerd. Dit project gebruikt datumgebaseerde vermeldingen en de Keep a Changelog-stijl (Toegevoegd, Gewijzigd, Opgelost, Verwijderd, Documentatie, Verplaatst).

## 2025-09-18

### Toegevoegd
- Module 08: Microsoft Foundry Local – Complete Developer Toolkit
  - Zes sessies: installatie, Azure AI Foundry-integratie, open-source modellen, geavanceerde demo's, agents en modellen-als-tools
  - Uitvoerbare voorbeelden onder `Module08/samples/01`–`06` met Windows cmd-instructies
    - `01` REST snelle chat (`chat_quickstart.py`)
    - `02` SDK quickstart met OpenAI/Foundry Local en Azure OpenAI-ondersteuning (`sdk_quickstart.py`)
    - `03` CLI lijst-en-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orkestratie (`python -m samples.05.agents.coordinator`)
    - `06` Modellen-als-tools router (`router.py`)
- Azure OpenAI-ondersteuning in SDK-voorbeeld van sessie 2 met configuratie via omgevingsvariabelen
- `.vscode/settings.json` ingesteld op `Module08/.venv` om Python-analyse te verbeteren
- `.env` met `PYTHONPATH` hint voor VS Code/Pylance herkenning

### Gewijzigd
- Standaardmodel bijgewerkt naar `phi-4-mini` in alle Module 08-documentatie en voorbeelden; resterende verwijzingen naar `phi-3.5` binnen Module 08 verwijderd
- Router (`Module08/samples/06/router.py`) verbeteringen:
  - Endpoint-detectie via `foundry service status` met regex-parsing
  - `/v1/models` gezondheidscontrole bij opstarten
  - Modelregistratie configureerbaar via omgevingsvariabelen (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Vereisten bijgewerkt: `Module08/requirements.txt` bevat nu `openai` (naast `requests`, `chainlit`)
- Chainlit voorbeeldinstructies verduidelijkt en probleemoplossing toegevoegd; importoplossing via werkruimte-instellingen

### Opgelost
- Importproblemen opgelost:
  - Router is niet langer afhankelijk van een niet-bestaande `utils` module; functies zijn geïntegreerd
  - Coordinator gebruikt relatieve import (`from .specialists import ...`) en wordt aangeroepen via modulepad
  - VS Code/Pylance configuratie om `chainlit` en pakketimporten te herkennen
- Kleine typfout gecorrigeerd in `STUDY_GUIDE.md` en Module 08-dekking toegevoegd

### Verwijderd
- Ongebruikte `Module08/infra/obs.py` verwijderd en de lege `infra/` map verwijderd; observatiepatronen behouden als optioneel in documentatie

### Verplaatst
- Module 08 demo's geconsolideerd onder `Module08/samples` met sessie-genummerde mappen
  - Chainlit app verplaatst naar `samples/04`
  - Agents verplaatst naar `samples/05` en `__init__.py` bestanden toegevoegd voor pakketherkenning

### Documentatie
- Module 08 sessiedocumentatie en alle voorbeeld-README's verrijkt met Microsoft Learn en betrouwbare leveranciersreferenties
- `Module08/README.md` bijgewerkt met Overzicht van Voorbeelden, routerconfiguratie en validatietips
- `Module07/README.md` Windows Foundry Local sectie gevalideerd tegen Learn-documentatie
- `STUDY_GUIDE.md` bijgewerkt:
  - Module 08 toegevoegd aan overzicht, schema's, voortgangstracker
  - Uitgebreide Referentiesectie toegevoegd (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisch (samenvatting)
- Cursusarchitectuur en modules vastgesteld (Modules 01–07)
- Iteratieve inhoudsmodernisering, formatteringsstandaardisatie en toegevoegde casestudies
- Uitgebreide dekking van optimalisatieframeworks (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Niet uitgebracht / Backlog (voorstellen)
- Optionele rooktests per voorbeeld om beschikbaarheid van Foundry Local te valideren
- Vertalingen herzien om modelverwijzingen (bijv. `phi-4-mini`) waar nodig af te stemmen
- Minimale pyright-configuratie toevoegen als teams werkruimtebrede strengheid prefereren

---

