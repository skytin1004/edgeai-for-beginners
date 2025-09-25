<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T01:15:20+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "cs"
}
-->
# Změny

Všechny významné změny v EdgeAI pro začátečníky jsou zde dokumentovány. Tento projekt používá záznamy založené na datech a styl Keep a Changelog (Přidáno, Změněno, Opraveno, Odstraněno, Dokumentace, Přesunuto).

## 2025-09-23

### Změněno - Modernizace hlavního modulu 08
- **Komplexní sladění se vzory úložiště Microsoft Foundry-Local**
  - Aktualizovány všechny příklady kódu pro použití moderního `FoundryLocalManager` a integrace OpenAI SDK
  - Nahrazeny zastaralé manuální volání `requests` správným použitím SDK
  - Implementační vzory sladěny s oficiální dokumentací a ukázkami od Microsoftu

- **Modernizace 05.AIPoweredAgents.md**:
  - Aktualizována orchestrace více agentů pro použití moderních vzorů SDK
  - Vylepšena implementace koordinátoru o pokročilé funkce (zpětné vazby, monitorování výkonu)
  - Přidáno komplexní zpracování chyb a kontrola stavu služeb
  - Integrované správné odkazy na lokální ukázky (`samples/05/multi_agent_orchestration.ipynb`)
  - Aktualizovány příklady volání funkcí pro použití moderního parametru `tools` místo zastaralého `functions`
  - Přidány vzory připravené pro produkci s monitorováním a sledováním statistik

- **Kompletní přepsání 06.ModelsAsTools.md**:
  - Nahrazen základní registr nástrojů inteligentním směrovačem modelů
  - Přidána volba modelů na základě klíčových slov pro různé typy úkolů (obecné, logické, kódování, kreativní)
  - Integrovaná konfigurace na základě prostředí s flexibilním přiřazením modelů
  - Vylepšeno komplexním monitorováním stavu služeb a zpracováním chyb
  - Přidány vzory nasazení do produkce s monitorováním požadavků a sledováním výkonu
  - Sladěno s lokální implementací v `samples/06/router.py` a `samples/06/model_router.ipynb`

- **Vylepšení struktury dokumentace**:
  - Přidány přehledové sekce zdůrazňující modernizaci a sladění s SDK
  - Vylepšeno pomocí emoji a lepšího formátování pro zlepšení čitelnosti
  - Přidány správné odkazy na lokální soubory s ukázkami v celé dokumentaci
  - Zahrnuto vedení pro implementaci připravenou pro produkci a osvědčené postupy

### Přidáno
- Komplexní přehledové sekce v souborech modulu 08 zdůrazňující integraci moderního SDK
- Architektonické přehledy ukazující pokročilé funkce (systémy více agentů, inteligentní směrování)
- Přímé odkazy na lokální implementace ukázek pro praktické zkušenosti
- Vedení pro nasazení do produkce s monitorováním a vzory zpracování chyb
- Interaktivní příklady v Jupyter notebooku s pokročilými funkcemi a benchmarky

### Opraveno
- Nesrovnalosti mezi dokumentací a skutečnými implementacemi ukázek
- Zastaralé vzory použití SDK v celém modulu 08
- Chybějící odkazy na komplexní knihovnu lokálních ukázek
- Nekonzistentní přístupy k implementaci v různých sekcích

---

## 2025-09-18

### Přidáno
- Modul 08: Microsoft Foundry Local – Kompletní vývojářská sada
  - Šest sezení: nastavení, integrace Azure AI Foundry, open-source modely, špičkové ukázky, agenti a modely jako nástroje
  - Spustitelné ukázky pod `Module08/samples/01`–`06` s instrukcemi pro Windows cmd
    - `01` REST rychlý chat (`chat_quickstart.py`)
    - `02` SDK rychlý start s OpenAI/Foundry Local a podporou Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI seznam a benchmark (`list_and_bench.cmd`)
    - `04` Ukázka Chainlit (`app.py`)
    - `05` Orchestrace více agentů (`python -m samples.05.agents.coordinator`)
    - `06` Směrovač modelů jako nástrojů (`router.py`)
- Podpora Azure OpenAI v ukázce SDK v sezení 2 s konfigurací proměnných prostředí
- `.vscode/settings.json` pro ukázání na `Module08/.venv` a zlepšení rozlišení analýzy Pythonu
- `.env` s nápovědou `PYTHONPATH` pro povědomí VS Code/Pylance

### Změněno
- Výchozí model aktualizován na `phi-4-mini` v celém modulu 08 dokumentace a ukázek; odstraněny zbývající zmínky o `phi-3.5` v rámci modulu 08
- Vylepšení směrovače (`Module08/samples/06/router.py`):
  - Zjišťování koncových bodů pomocí `foundry service status` s parsováním regexu
  - Kontrola stavu `/v1/models` při spuštění
  - Registr modelů konfigurovatelný prostředím (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Aktualizovány požadavky: `Module08/requirements.txt` nyní zahrnuje `openai` (vedle `requests`, `chainlit`)
- Zpřesněno vedení pro ukázku Chainlit a přidáno řešení problémů; rozlišení importu pomocí nastavení pracovního prostoru

### Opraveno
- Vyřešeny problémy s importem:
  - Směrovač již nezávisí na neexistujícím modulu `utils`; funkce jsou vloženy přímo
  - Koordinátor používá relativní import (`from .specialists import ...`) a je spuštěn přes cestu modulu
  - Konfigurace VS Code/Pylance pro rozlišení `chainlit` a importů balíčků
- Opraven drobný překlep v `STUDY_GUIDE.md` a přidáno pokrytí modulu 08

### Odstraněno
- Smazán nepoužívaný `Module08/infra/obs.py` a odstraněn prázdný adresář `infra/`; vzory pro observabilitu zachovány jako volitelné v dokumentaci

### Přesunuto
- Konsolidovány ukázky modulu 08 pod `Module08/samples` s adresáři očíslovanými podle sezení
  - Přesunuta aplikace Chainlit do `samples/04`
  - Přesunuti agenti do `samples/05` a přidány soubory `__init__.py` pro rozlišení balíčků

### Dokumentace
- Dokumentace sezení modulu 08 a všechny README ukázek obohaceny o odkazy na Microsoft Learn a důvěryhodné dodavatele
- `Module08/README.md` aktualizováno s přehledem ukázek, konfigurací směrovače a tipy pro validaci
- `Module07/README.md` sekce Windows Foundry Local ověřena proti dokumentaci Learn
- `STUDY_GUIDE.md` aktualizováno:
  - Přidán modul 08 do přehledu, rozvrhů, sledovače pokroku
  - Přidána komplexní sekce Odkazy (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historické (souhrn)
- Architektura kurzu a moduly vytvořeny (Moduly 01–07)
- Iterativní modernizace obsahu, standardizace formátování a přidání případových studií
- Rozšířené pokrytí optimalizačních rámců (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nevydáno / Záloha (návrhy)
- Volitelné testy pro každou ukázku k ověření dostupnosti Foundry Local
- Revize překladů pro sladění odkazů na modely (např. `phi-4-mini`) tam, kde je to vhodné
- Přidání minimální konfigurace pyright, pokud týmy preferují přísnost na úrovni pracovního prostoru

---

