<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T20:47:48+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "cs"
}
-->
# Změny

Všechny významné změny v EdgeAI pro začátečníky jsou zde zdokumentovány. Tento projekt používá záznamy podle data a styl Keep a Changelog (Přidáno, Změněno, Opraveno, Odstraněno, Dokumentace, Přesunuto).

## 2025-10-08

### Přidáno - Komplexní aktualizace workshopu
- **Kompletní přepsání README.md workshopu**:
  - Přidán komplexní úvod vysvětlující přínosy Edge AI (soukromí, výkon, náklady)
  - Vytvořeno 6 hlavních vzdělávacích cílů s podrobnými kompetencemi
  - Přidána tabulka výsledků učení s výstupy a kompetenční maticí
  - Zahrnuta sekce dovedností připravených pro kariéru s důrazem na průmyslovou relevanci
  - Přidán rychlý průvodce s požadavky a 3-krokovým nastavením
  - Vytvořeny tabulky zdrojů pro Python ukázky (8 souborů s dobou běhu)
  - Přidána tabulka Jupyter notebooků (8 notebooků s hodnocením obtížnosti)
  - Vytvořena tabulka dokumentace (7 klíčových dokumentů s doporučením "Kdy použít")
  - Přidána doporučení vzdělávací cesty pro různé úrovně dovedností

- **Validace workshopu a testovací infrastruktura**:
  - Vytvořen `scripts/validate_samples.py` - komplexní nástroj pro validaci syntaxe, importů a osvědčených postupů
  - Vytvořen `scripts/test_samples.py` - nástroj pro rychlé testování všech Python ukázek
  - Přidána dokumentace validace do `scripts/README.md`

- **Komplexní dokumentace**:
  - Vytvořen `SAMPLES_UPDATE_SUMMARY.md` - podrobný průvodce o více než 400 řádcích pokrývající všechny vylepšení
  - Vytvořen `UPDATE_COMPLETE.md` - výkonný souhrn dokončení aktualizace
  - Vytvořen `QUICK_REFERENCE.md` - rychlá referenční karta pro workshop

### Změněno - Modernizace Python ukázek workshopu
- **Všechny 8 Python ukázky aktualizovány podle osvědčených postupů**:
  - Vylepšeno zpracování chyb pomocí bloků try-except kolem všech I/O operací
  - Přidány typové anotace a podrobné docstringy
  - Implementován konzistentní vzor logování [INFO]/[ERROR]/[RESULT]
  - Ochráněny volitelné importy s návodem na instalaci
  - Zlepšena zpětná vazba uživatelům ve všech ukázkách

- **session01/chat_bootstrap.py**:
  - Vylepšena inicializace klienta s podrobnými chybovými zprávami
  - Zlepšeno zpracování chyb při streamování pomocí validace bloků
  - Přidáno lepší zpracování výjimek při nedostupnosti služby

- **session02/rag_pipeline.py**:
  - Přidány ochranné importy pro sentence-transformers s návodem na instalaci
  - Vylepšeno zpracování chyb při operacích embeddingu a generování
  - Zlepšeno formátování výstupu pomocí strukturovaných výsledků

- **session02/rag_eval_ragas.py**:
  - Ochráněny volitelné importy (ragas, datasets) s uživatelsky přívětivými chybovými zprávami
  - Přidáno zpracování chyb pro metriky hodnocení
  - Zlepšeno formátování výstupu pro výsledky hodnocení

- **session03/benchmark_oss_models.py**:
  - Implementováno elegantní degradování (pokračuje při selhání modelů)
  - Přidáno podrobné hlášení o průběhu a zpracování chyb pro každý model
  - Vylepšeno výpočty statistik s komplexním zotavením z chyb

- **session04/model_compare.py**:
  - Přidány typové anotace (návratové typy Tuple)
  - Zlepšeno formátování výstupu pomocí strukturovaných JSON výsledků
  - Implementováno zpracování chyb pro každý model s možností zotavení

- **session05/agents_orchestrator.py**:
  - Vylepšeno Agent.act() s podrobnými docstringy
  - Přidáno zpracování chyb pipeline s logováním po jednotlivých fázích
  - Zlepšeno řízení paměti a sledování stavu

- **session06/models_router.py**:
  - Vylepšena dokumentace funkcí pro všechny komponenty směrování
  - Přidáno podrobné logování ve funkci route()
  - Zlepšeno testování výstupu pomocí strukturovaných výsledků

- **session06/models_pipeline.py**:
  - Přidáno zpracování chyb do pomocné funkce chat()
  - Vylepšeno pipeline() s logováním fází a hlášením o průběhu
  - Zlepšeno main() s komplexním zotavením z chyb

### Dokumentace - Vylepšení dokumentace workshopu
- Aktualizován hlavní README.md s částí workshopu zdůrazňující praktickou vzdělávací cestu
- Vylepšen STUDY_GUIDE.md s komplexní částí workshopu zahrnující:
  - Vzdělávací cíle a oblasti zaměření studia
  - Otázky pro sebehodnocení
  - Praktická cvičení s odhady času
  - Časové rozvržení pro intenzivní a částečné studium
  - Přidán workshop do šablony sledování pokroku
- Aktualizován časový odhad z 20 hodin na 30 hodin (včetně workshopu)
- Přidány popisy ukázek workshopu a výsledky učení do README

### Opraveno
- Vyřešeny nekonzistentní vzory zpracování chyb napříč ukázkami workshopu
- Opraveny chyby volitelných importů s odpovídajícími ochrannými mechanismy
- Opraveny chybějící typové anotace v kritických funkcích
- Řešena nedostatečná zpětná vazba uživatelům v chybových scénářích
- Opraveny problémy validace pomocí komplexní testovací infrastruktury

---

## 2025-09-23

### Změněno - Modernizace hlavního modulu 08
- **Komplexní sladění s vzory úložiště Microsoft Foundry-Local**:
  - Aktualizovány všechny příklady kódu pro použití moderního `FoundryLocalManager` a integrace OpenAI SDK
  - Nahrazeny zastaralé manuální volání `requests` správným použitím SDK
  - Sladěny implementační vzory s oficiální dokumentací a ukázkami Microsoftu

- **05.AIPoweredAgents.md modernizace**:
  - Aktualizována orchestrace více agentů pro použití moderních vzorů SDK
  - Vylepšena implementace koordinátoru s pokročilými funkcemi (zpětné vazby, monitorování výkonu)
  - Přidáno komplexní zpracování chyb a kontrola stavu služeb
  - Integrované správné odkazy na místní ukázky (`samples/05/multi_agent_orchestration.ipynb`)
  - Aktualizovány příklady volání funkcí pro použití moderního parametru `tools` místo zastaralého `functions`
  - Přidány vzory připravené pro produkci s monitorováním a sledováním statistik

- **06.ModelsAsTools.md kompletní přepsání**:
  - Nahrazen základní registr nástrojů inteligentní implementací směrovače modelů
  - Přidán výběr modelů na základě klíčových slov pro různé typy úkolů (obecné, logické, kód, kreativní)
  - Integrovaná konfigurace na základě prostředí s flexibilním přiřazením modelů
  - Vylepšeno komplexním monitorováním stavu služeb a zpracováním chyb
  - Přidány vzory nasazení do produkce s monitorováním požadavků a sledováním výkonu
  - Sladěno s místní implementací v `samples/06/router.py` a `samples/06/model_router.ipynb`

- **Vylepšení struktury dokumentace**:
  - Přidány přehledové sekce zdůrazňující modernizaci a sladění SDK
  - Vylepšeno pomocí emoji a lepšího formátování pro zlepšení čitelnosti
  - Přidány správné odkazy na místní soubory ukázek napříč dokumentací
  - Zahrnuto vedení implementace připravené pro produkci a osvědčené postupy

### Přidáno
- Komplexní přehledové sekce v souborech modulu 08 zdůrazňující integraci moderního SDK
- Zvýraznění architektury ukazující pokročilé funkce (systémy více agentů, inteligentní směrování)
- Přímé odkazy na místní implementace ukázek pro praktické zkušenosti
- Vedení nasazení do produkce s monitorováním a vzory zpracování chyb
- Interaktivní příklady Jupyter notebooků s pokročilými funkcemi a benchmarky

### Opraveno
- Nesrovnalosti mezi dokumentací a skutečnými implementacemi ukázek
- Zastaralé vzory použití SDK napříč modulem 08
- Chybějící odkazy na komplexní místní knihovnu ukázek
- Nekonzistentní přístupy k implementaci napříč různými sekcemi

---

## 2025-09-18

### Přidáno
- Modul 08: Microsoft Foundry Local – Kompletní vývojářská sada
  - Šest sezení: nastavení, integrace Azure AI Foundry, open-source modely, špičkové ukázky, agenti a modely jako nástroje
  - Spustitelné ukázky pod `Module08/samples/01`–`06` s instrukcemi pro Windows cmd
    - `01` REST rychlý chat (`chat_quickstart.py`)
    - `02` SDK rychlý start s OpenAI/Foundry Local a podporou Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI seznam a benchmark (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Orchestrace více agentů (`python -m samples.05.agents.coordinator`)
    - `06` Směrovač modelů jako nástrojů (`router.py`)
- Podpora Azure OpenAI v ukázce SDK sezení 2 s konfigurací proměnných prostředí
- `.vscode/settings.json` pro ukázání na `Module08/.venv` a zlepšení rozlišení analýzy Pythonu
- `.env` s nápovědou `PYTHONPATH` pro povědomí VS Code/Pylance

### Změněno
- Výchozí model aktualizován na `phi-4-mini` napříč dokumentací a ukázkami modulu 08; odstraněny zbývající zmínky o `phi-3.5` v rámci modulu 08
- Vylepšení směrovače (`Module08/samples/06/router.py`):
  - Zjišťování endpointů pomocí `foundry service status` s regex analýzou
  - Kontrola stavu `/v1/models` při spuštění
  - Konfigurovatelný registr modelů prostředím (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Aktualizovány požadavky: `Module08/requirements.txt` nyní zahrnuje `openai` (spolu s `requests`, `chainlit`)
- Zpřesněno vedení ukázky Chainlit a přidáno řešení problémů; rozlišení importů pomocí nastavení pracovního prostoru

### Opraveno
- Vyřešeny problémy s importem:
  - Směrovač již nezávisí na neexistujícím modulu `utils`; funkce jsou vloženy
  - Koordinátor používá relativní import (`from .specialists import ...`) a je spuštěn přes cestu modulu
  - Konfigurace VS Code/Pylance pro rozlišení `chainlit` a importů balíčků
- Opraven drobný překlep v `STUDY_GUIDE.md` a přidáno pokrytí modulu 08

### Odstraněno
- Smazán nepoužívaný `Module08/infra/obs.py` a odstraněn prázdný adresář `infra/`; vzory pozorovatelnosti zachovány jako volitelné v dokumentaci

### Přesunuto
- Konsolidovány ukázky modulu 08 pod `Module08/samples` s adresáři očíslovanými podle sezení
  - Přesunuta aplikace Chainlit do `samples/04`
  - Přesunuti agenti do `samples/05` a přidány soubory `__init__.py` pro rozlišení balíčků

### Dokumentace
- Dokumentace sezení modulu 08 a všechny README ukázek obohaceny o odkazy na Microsoft Learn a důvěryhodné dodavatele
- `Module08/README.md` aktualizováno s přehledem ukázek, konfigurací směrovače a tipy na validaci
- `Module07/README.md` sekce Windows Foundry Local ověřena proti dokumentaci Learn
- `STUDY_GUIDE.md` aktualizováno:
  - Přidán modul 08 do přehledu, rozvrhů, sledovače pokroku
  - Přidána komplexní sekce Odkazy (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historické (souhrn)
- Založena architektura kurzu a moduly (Moduly 01–07)
- Iterativní modernizace obsahu, standardizace formátování a přidání případových studií
- Rozšířeno pokrytí optimalizačních rámců (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nevydáno / Záloha (návrhy)
- Volitelné rychlé testy pro každou ukázku k ověření dostupnosti Foundry Local
- Přezkoumání překladů pro sladění odkazů na modely (např. `phi-4-mini`) kde je to vhodné
- Přidání minimální konfigurace pyright, pokud týmy preferují přísnost na úrovni pracovního prostoru

---

**Upozornění**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.