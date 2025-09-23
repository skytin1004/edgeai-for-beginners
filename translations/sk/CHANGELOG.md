<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-23T00:44:52+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sk"
}
-->
# Zmeny

Všetky významné zmeny v EdgeAI pre začiatočníkov sú zdokumentované tu. Tento projekt používa záznamy založené na dátume a štýl Keep a Changelog (Pridané, Zmenené, Opravené, Odstránené, Dokumentácia, Presunuté).

## 2025-09-18

### Pridané
- Modul 08: Microsoft Foundry Local – Kompletná vývojárska sada nástrojov
  - Šesť relácií: nastavenie, integrácia Azure AI Foundry, open-source modely, najnovšie ukážky, agenti a modely ako nástroje
  - Spustiteľné vzorky pod `Module08/samples/01`–`06` s inštrukciami pre Windows cmd
    - `01` REST rýchly chat (`chat_quickstart.py`)
    - `02` SDK rýchly štart s podporou OpenAI/Foundry Local a Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI zoznam a testovanie (`list_and_bench.cmd`)
    - `04` Chainlit ukážka (`app.py`)
    - `05` Orchestrácia viacerých agentov (`python -m samples.05.agents.coordinator`)
    - `06` Router modelov ako nástrojov (`router.py`)
- Podpora Azure OpenAI v SDK vzorke relácie 2 s konfiguráciou environmentálnych premenných
- `.vscode/settings.json` na ukázanie na `Module08/.venv` a zlepšenie rozlíšenia analýzy Pythonu
- `.env` s náznakom `PYTHONPATH` pre lepšie rozpoznanie VS Code/Pylance

### Zmenené
- Predvolený model aktualizovaný na `phi-4-mini` v dokumentácii a vzorkách Modulu 08; odstránené zostávajúce zmienky o `phi-3.5` v Module 08
- Vylepšenia routera (`Module08/samples/06/router.py`):
  - Zisťovanie endpointov cez `foundry service status` s regex analýzou
  - Kontrola zdravia `/v1/models` pri štarte
  - Konfigurovateľný register modelov cez environmentálne premenné (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Aktualizované požiadavky: `Module08/requirements.txt` teraz zahŕňa `openai` (spolu s `requests`, `chainlit`)
- Ujasnené pokyny k vzorke Chainlit a pridané riešenie problémov; rozlíšenie importov cez nastavenia pracovného priestoru

### Opravené
- Vyriešené problémy s importom:
  - Router už nezávisí na neexistujúcom module `utils`; funkcie sú vložené
  - Koordinátor používa relatívny import (`from .specialists import ...`) a je spustený cez cestu modulu
  - Konfigurácia VS Code/Pylance na rozlíšenie `chainlit` a importov balíkov
- Opravená drobná chyba v `STUDY_GUIDE.md` a pridané pokrytie Modulu 08

### Odstránené
- Vymazaný nepoužívaný `Module08/infra/obs.py` a odstránený prázdny adresár `infra/`; vzory pozorovateľnosti ponechané ako voliteľné v dokumentácii

### Presunuté
- Konsolidované ukážky Modulu 08 pod `Module08/samples` s priečinkami očíslovanými podľa relácií
  - Chainlit aplikácia presunutá do `samples/04`
  - Agenti presunutí do `samples/05` a pridané súbory `__init__.py` pre rozlíšenie balíkov

### Dokumentácia
- Dokumentácia relácií Modulu 08 a všetky README vzorky obohatené o odkazy na Microsoft Learn a dôveryhodných dodávateľov
- `Module08/README.md` aktualizované s prehľadom vzoriek, konfiguráciou routera a tipmi na validáciu
- `Module07/README.md` sekcia Windows Foundry Local overená voči dokumentácii Learn
- `STUDY_GUIDE.md` aktualizované:
  - Pridaný Modul 08 do prehľadu, harmonogramov, sledovača pokroku
  - Pridaná komplexná sekcia Referencie (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historické (zhrnutie)
- Založená architektúra kurzu a moduly (Moduly 01–07)
- Iteratívna modernizácia obsahu, štandardizácia formátovania a pridané prípadové štúdie
- Rozšírené pokrytie optimalizačných rámcov (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nezverejnené / Zoznam úloh (návrhy)
- Voliteľné testy pre každú vzorku na overenie dostupnosti Foundry Local
- Skontrolovať preklady na zosúladenie odkazov na modely (napr. `phi-4-mini`) kde je to vhodné
- Pridať minimálnu konfiguráciu pyright, ak tímy preferujú prísnosť na úrovni pracovného priestoru

---

