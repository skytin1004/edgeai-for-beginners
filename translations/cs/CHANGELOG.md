<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-23T00:44:39+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "cs"
}
-->
# Changelog

Všechny významné změny v EdgeAI pro začátečníky jsou zde dokumentovány. Tento projekt používá záznamy založené na datech a styl Keep a Changelog (Přidáno, Změněno, Opraveno, Odstraněno, Dokumentace, Přesunuto).

## 2025-09-18

### Přidáno
- Modul 08: Microsoft Foundry Local – Kompletní vývojářská sada
  - Šest sezení: nastavení, integrace Azure AI Foundry, open-source modely, nejmodernější ukázky, agenti a modely jako nástroje
  - Spustitelné příklady pod `Module08/samples/01`–`06` s instrukcemi pro Windows cmd
    - `01` REST rychlý chat (`chat_quickstart.py`)
    - `02` SDK rychlý start s OpenAI/Foundry Local a podporou Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI seznam a benchmark (`list_and_bench.cmd`)
    - `04` Ukázka Chainlit (`app.py`)
    - `05` Orchestrace více agentů (`python -m samples.05.agents.coordinator`)
    - `06` Router modelů jako nástrojů (`router.py`)
- Podpora Azure OpenAI v SDK příkladu z druhého sezení s konfigurací prostředí
- `.vscode/settings.json` nastaveno na `Module08/.venv` pro zlepšení analýzy Pythonu
- `.env` s nápovědou `PYTHONPATH` pro povědomí VS Code/Pylance

### Změněno
- Výchozí model aktualizován na `phi-4-mini` v dokumentaci a příkladech Modulu 08; odstraněny zbývající zmínky o `phi-3.5` v rámci Modulu 08
- Vylepšení routeru (`Module08/samples/06/router.py`):
  - Zjišťování endpointů pomocí `foundry service status` s regex analýzou
  - Kontrola zdraví `/v1/models` při spuštění
  - Konfigurovatelný registr modelů prostřednictvím prostředí (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Aktualizované požadavky: `Module08/requirements.txt` nyní zahrnuje `openai` (spolu s `requests`, `chainlit`)
- Zpřesněné pokyny k ukázce Chainlit a přidána řešení problémů; importy vyřešeny pomocí nastavení pracovního prostoru

### Opraveno
- Vyřešeny problémy s importem:
  - Router již nezávisí na neexistujícím modulu `utils`; funkce jsou vloženy přímo
  - Koordinátor používá relativní import (`from .specialists import ...`) a je spuštěn přes cestu modulu
  - Konfigurace VS Code/Pylance pro vyřešení importů `chainlit` a balíčků
- Opraven drobný překlep v `STUDY_GUIDE.md` a přidáno pokrytí Modulu 08

### Odstraněno
- Smazán nepoužívaný `Module08/infra/obs.py` a odstraněn prázdný adresář `infra/`; vzory pozorovatelnosti zachovány jako volitelné v dokumentaci

### Přesunuto
- Konsolidovány ukázky Modulu 08 pod `Module08/samples` s adresáři očíslovanými podle sezení
  - Chainlit aplikace přesunuta do `samples/04`
  - Agenti přesunuti do `samples/05` a přidány soubory `__init__.py` pro vyřešení balíčků

### Dokumentace
- Dokumentace sezení Modulu 08 a všechny README soubory příkladů obohaceny o odkazy na Microsoft Learn a důvěryhodné dodavatele
- `Module08/README.md` aktualizováno s přehledem příkladů, konfigurací routeru a tipy pro validaci
- `Module07/README.md` sekce Windows Foundry Local ověřena proti dokumentaci Learn
- `STUDY_GUIDE.md` aktualizováno:
  - Přidán Modul 08 do přehledu, rozvrhů, sledovače pokroku
  - Přidána komplexní sekce Referencí (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historické (shrnutí)
- Založena architektura kurzu a moduly (Moduly 01–07)
- Iterativní modernizace obsahu, standardizace formátování a přidání případových studií
- Rozšířené pokrytí optimalizačních rámců (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nevydáno / Záloha (návrhy)
- Volitelné testy pro jednotlivé příklady k ověření dostupnosti Foundry Local
- Revize překladů pro sladění odkazů na modely (např. `phi-4-mini`) tam, kde je to vhodné
- Přidání minimální konfigurace pyright, pokud týmy preferují přísnost na úrovni pracovního prostoru

---

