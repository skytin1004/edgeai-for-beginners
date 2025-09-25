<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T01:22:22+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sk"
}
-->
# Zmeny

Všetky významné zmeny v EdgeAI pre začiatočníkov sú zdokumentované tu. Tento projekt používa záznamy založené na dátume a štýl Keep a Changelog (Pridané, Zmenené, Opravené, Odstránené, Dokumentácia, Presunuté).

## 2025-09-23

### Zmenené - Modernizácia hlavného modulu 08
- **Komplexné zosúladenie so vzormi úložiska Microsoft Foundry-Local**
  - Aktualizované všetky príklady kódu na použitie moderného `FoundryLocalManager` a integrácie OpenAI SDK
  - Nahradené zastarané manuálne volania `requests` správnym použitím SDK
  - Zosúladené implementačné vzory s oficiálnou dokumentáciou a vzorkami od Microsoftu

- **Modernizácia 05.AIPoweredAgents.md**:
  - Aktualizovaná orchestrácia viacerých agentov na použitie moderných vzorov SDK
  - Vylepšená implementácia koordinátora s pokročilými funkciami (spätné väzby, monitorovanie výkonu)
  - Pridané komplexné spracovanie chýb a kontrola zdravia služieb
  - Integrované správne odkazy na lokálne vzorky (`samples/05/multi_agent_orchestration.ipynb`)
  - Aktualizované príklady volania funkcií na použitie moderného parametra `tools` namiesto zastaraného `functions`
  - Pridané vzory pripravené na produkciu s monitorovaním a sledovaním štatistík

- **Kompletné prepracovanie 06.ModelsAsTools.md**:
  - Nahradený základný register nástrojov inteligentnou implementáciou smerovača modelov
  - Pridaný výber modelov na základe kľúčových slov pre rôzne typy úloh (všeobecné, logické, kódovanie, kreatívne)
  - Integrovaná konfigurácia na základe prostredia s flexibilným priradením modelov
  - Vylepšené komplexným monitorovaním zdravia služieb a spracovaním chýb
  - Pridané vzory nasadenia do produkcie s monitorovaním požiadaviek a sledovaním výkonu
  - Zosúladené s lokálnou implementáciou v `samples/06/router.py` a `samples/06/model_router.ipynb`

- **Vylepšenia štruktúry dokumentácie**:
  - Pridané sekcie prehľadu zdôrazňujúce modernizáciu a zosúladenie SDK
  - Vylepšené pomocou emotikonov a lepšieho formátovania pre zlepšenie čitateľnosti
  - Pridané správne odkazy na lokálne súbory vzoriek v celej dokumentácii
  - Zahrnuté pokyny na implementáciu pripravenú na produkciu a osvedčené postupy

### Pridané
- Komplexné sekcie prehľadu v súboroch modulu 08 zdôrazňujúce modernú integráciu SDK
- Architektonické zvýraznenia ukazujúce pokročilé funkcie (systémy viacerých agentov, inteligentné smerovanie)
- Priame odkazy na lokálne implementácie vzoriek pre praktické skúsenosti
- Pokyny na nasadenie do produkcie s monitorovaním a vzormi spracovania chýb
- Interaktívne príklady Jupyter notebookov s pokročilými funkciami a benchmarkmi

### Opravené
- Nesúlady medzi dokumentáciou a skutočnými implementáciami vzoriek
- Zastarané vzory používania SDK v celom module 08
- Chýbajúce odkazy na komplexnú knižnicu lokálnych vzoriek
- Nekonzistentné prístupy k implementácii v rôznych sekciách

---

## 2025-09-18

### Pridané
- Modul 08: Microsoft Foundry Local – Kompletná vývojárska sada nástrojov
  - Šesť relácií: nastavenie, integrácia Azure AI Foundry, open-source modely, špičkové ukážky, agenti a modely ako nástroje
  - Spustiteľné vzorky pod `Module08/samples/01`–`06` s inštrukciami pre Windows cmd
    - `01` REST rýchly chat (`chat_quickstart.py`)
    - `02` SDK rýchly štart s OpenAI/Foundry Local a podporou Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI zoznam a benchmark (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Orchestrácia viacerých agentov (`python -m samples.05.agents.coordinator`)
    - `06` Smerovač modelov ako nástrojov (`router.py`)
- Podpora Azure OpenAI v ukážke SDK relácie 2 s konfiguráciou prostredia
- `.vscode/settings.json` na ukázanie na `Module08/.venv` a zlepšenie rozlíšenia analýzy Pythonu
- `.env` s náznakom `PYTHONPATH` pre povedomie VS Code/Pylance

### Zmenené
- Predvolený model aktualizovaný na `phi-4-mini` v celej dokumentácii a vzorkách modulu 08; odstránené zostávajúce zmienky o `phi-3.5` v rámci modulu 08
- Vylepšenia smerovača (`Module08/samples/06/router.py`):
  - Zisťovanie koncových bodov cez `foundry service status` s analýzou regexu
  - Kontrola zdravia `/v1/models` pri štarte
  - Konfigurovateľný register modelov prostredím (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Aktualizované požiadavky: `Module08/requirements.txt` teraz zahŕňa `openai` (spolu s `requests`, `chainlit`)
- Vysvetlenie vzorky Chainlit a pridané riešenie problémov; rozlíšenie importu cez nastavenia pracovného priestoru

### Opravené
- Vyriešené problémy s importom:
  - Smerovač už nezávisí od neexistujúceho modulu `utils`; funkcie sú vložené
  - Koordinátor používa relatívny import (`from .specialists import ...`) a je spustený cez cestu modulu
  - Konfigurácia VS Code/Pylance na rozlíšenie `chainlit` a importov balíkov
- Opravená drobná chyba v `STUDY_GUIDE.md` a pridané pokrytie modulu 08

### Odstránené
- Odstránený nepoužívaný `Module08/infra/obs.py` a odstránený prázdny adresár `infra/`; vzory pozorovateľnosti ponechané ako voliteľné v dokumentácii

### Presunuté
- Konsolidované ukážky modulu 08 pod `Module08/samples` s priečinkami očíslovanými podľa relácií
  - Presunutá aplikácia Chainlit do `samples/04`
  - Presunutí agenti do `samples/05` a pridané súbory `__init__.py` pre rozlíšenie balíkov

### Dokumentácia
- Dokumenty relácií modulu 08 a všetky README vzoriek obohatené o odkazy na Microsoft Learn a dôveryhodných dodávateľov
- `Module08/README.md` aktualizované s prehľadom vzoriek, konfiguráciou smerovača a tipmi na validáciu
- `Module07/README.md` sekcia Windows Foundry Local overená voči dokumentácii Learn
- `STUDY_GUIDE.md` aktualizované:
  - Pridaný modul 08 do prehľadu, harmonogramov, sledovača pokroku
  - Pridaná komplexná sekcia Referencie (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historické (zhrnutie)
- Založená architektúra kurzu a moduly (Moduly 01–07)
- Iteratívna modernizácia obsahu, štandardizácia formátovania a pridané prípadové štúdie
- Rozšírené pokrytie optimalizačných rámcov (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nevydané / Zoznam úloh (návrhy)
- Voliteľné testy funkčnosti pre každú vzorku na overenie dostupnosti Foundry Local
- Prehodnotenie prekladov na zosúladenie referencií modelov (napr. `phi-4-mini`) kde je to vhodné
- Pridanie minimálnej konfigurácie pyright, ak tímy preferujú prísnosť na úrovni pracovného priestoru

---

