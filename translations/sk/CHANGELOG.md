<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T15:03:37+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sk"
}
-->
# Zmeny

Všetky významné zmeny v EdgeAI pre začiatočníkov sú zdokumentované tu. Tento projekt používa záznamy založené na dátume a štýl Keep a Changelog (Pridané, Zmenené, Opravené, Odstránené, Dokumentácia, Presunuté).

## 2025-10-08

### Pridané - Komplexná aktualizácia workshopu
- **Kompletné prepracovanie README.md pre workshop**:
  - Pridaný komplexný úvod vysvetľujúci hodnotu Edge AI (súkromie, výkon, náklady)
  - Vytvorených 6 hlavných vzdelávacích cieľov s podrobnými kompetenciami
  - Pridaná tabuľka výsledkov učenia s výstupmi a maticou kompetencií
  - Zahrnutá sekcia zručností pripravených na kariéru pre relevantnosť v priemysle
  - Pridaný rýchly sprievodca s predpokladmi a 3-krokovým nastavením
  - Vytvorené tabuľky zdrojov pre Python vzorky (8 súborov s časmi spustenia)
  - Pridaná tabuľka Jupyter notebookov (8 notebookov s hodnotením obtiažnosti)
  - Vytvorená tabuľka dokumentácie (7 kľúčových dokumentov s odporúčaniami „Použiť kedy“)
  - Pridané odporúčania pre vzdelávaciu cestu pre rôzne úrovne zručností

- **Validácia workshopu a testovacia infraštruktúra**:
  - Vytvorený `scripts/validate_samples.py` - Komplexný validačný nástroj pre syntax, importy a najlepšie postupy
  - Vytvorený `scripts/test_samples.py` - Nástroj na rýchle testovanie všetkých Python vzoriek
  - Pridaná dokumentácia validácie do `scripts/README.md`

- **Komplexná dokumentácia**:
  - Vytvorený `SAMPLES_UPDATE_SUMMARY.md` - 400+ riadkový podrobný sprievodca pokrývajúci všetky vylepšenia
  - Vytvorený `UPDATE_COMPLETE.md` - Výkonný súhrn dokončenia aktualizácie
  - Vytvorený `QUICK_REFERENCE.md` - Rýchla referenčná karta pre workshop

### Zmenené - Modernizácia Python vzoriek workshopu
- **Všetkých 8 Python vzoriek aktualizovaných podľa najlepších postupov**:
  - Vylepšené spracovanie chýb pomocou blokov try-except okolo všetkých I/O operácií
  - Pridané typové anotácie a komplexné docstringy
  - Implementovaný konzistentný vzor logovania [INFO]/[ERROR]/[RESULT]
  - Chránené voliteľné importy s inštalačnými odporúčaniami
  - Zlepšená spätná väzba používateľovi vo všetkých vzorkách

- **session01/chat_bootstrap.py**:
  - Vylepšená inicializácia klienta s komplexnými chybovými správami
  - Zlepšené spracovanie chýb pri streamovaní s validáciou blokov
  - Pridané lepšie spracovanie výnimiek pri nedostupnosti služby

- **session02/rag_pipeline.py**:
  - Pridané ochranné importy pre sentence-transformers s inštalačnými odporúčaniami
  - Vylepšené spracovanie chýb pri operáciách vkladania a generovania
  - Zlepšené formátovanie výstupu so štruktúrovanými výsledkami

- **session02/rag_eval_ragas.py**:
  - Chránené voliteľné importy (ragas, datasets) s užívateľsky prívetivými chybovými správami
  - Pridané spracovanie chýb pre hodnotiace metriky
  - Zlepšené formátovanie výstupu pre hodnotiace výsledky

- **session03/benchmark_oss_models.py**:
  - Implementovaná elegantná degradácia (pokračuje pri zlyhaní modelov)
  - Pridané podrobné hlásenie o pokroku a spracovanie chýb pre každý model
  - Zlepšené výpočty štatistík s komplexným zotavením po chybách

- **session04/model_compare.py**:
  - Pridané typové anotácie (návratové typy Tuple)
  - Zlepšené formátovanie výstupu so štruktúrovanými JSON výsledkami
  - Implementované spracovanie chýb pre každý model s možnosťou zotavenia

- **session05/agents_orchestrator.py**:
  - Vylepšené Agent.act() s komplexnými docstringami
  - Pridané spracovanie chýb v pipeline s logovaním po jednotlivých etapách
  - Zlepšené spravovanie pamäte a sledovanie stavu

- **session06/models_router.py**:
  - Vylepšená dokumentácia funkcií pre všetky komponenty smerovania
  - Pridané podrobné logovanie vo funkcii route()
  - Zlepšený testovací výstup so štruktúrovanými výsledkami

- **session06/models_pipeline.py**:
  - Pridané spracovanie chýb do pomocnej funkcie chat()
  - Vylepšené pipeline() s logovaním etáp a hlásením o pokroku
  - Zlepšené main() s komplexným zotavením po chybách

### Dokumentácia - Vylepšenie dokumentácie workshopu
- Aktualizovaný hlavný README.md so sekciou workshopu zdôrazňujúcou praktickú vzdelávaciu cestu
- Vylepšený STUDY_GUIDE.md s komplexnou sekciou workshopu vrátane:
  - Vzdelávacích cieľov a oblastí zamerania štúdia
  - Otázok na sebahodnotenie
  - Praktických cvičení s odhadmi času
  - Časového rozvrhu pre intenzívne a čiastočné štúdium
  - Pridaný workshop do šablóny sledovania pokroku
- Aktualizovaný časový rozvrh z 20 hodín na 30 hodín (vrátane workshopu)
- Pridané popisy vzoriek workshopu a výsledky učenia do README

### Opravené
- Vyriešené nekonzistentné vzory spracovania chýb naprieč vzorkami workshopu
- Opravené chyby voliteľných importov závislostí s vhodnými ochrannými mechanizmami
- Opravené chýbajúce typové anotácie v kritických funkciách
- Riešené nedostatočné spätné väzby používateľovi v scenároch chýb
- Opravené validačné problémy s komplexnou testovacou infraštruktúrou

---

## 2025-09-23

### Zmenené - Modernizácia hlavného modulu 08
- **Komplexné zosúladenie so vzormi úložiska Microsoft Foundry-Local**:
  - Aktualizované všetky príklady kódu na použitie moderného `FoundryLocalManager` a integrácie OpenAI SDK
  - Nahradené zastarané manuálne volania `requests` správnym použitím SDK
  - Zosúladené implementačné vzory s oficiálnou dokumentáciou a vzorkami Microsoftu

- **Modernizácia 05.AIPoweredAgents.md**:
  - Aktualizovaná orchestrácia viacerých agentov na použitie moderných vzorov SDK
  - Vylepšená implementácia koordinátora s pokročilými funkciami (spätné väzby, monitorovanie výkonu)
  - Pridané komplexné spracovanie chýb a kontrola zdravia služby
  - Integrované správne odkazy na lokálne vzorky (`samples/05/multi_agent_orchestration.ipynb`)
  - Aktualizované príklady volania funkcií na použitie moderného parametra `tools` namiesto zastaraného `functions`
  - Pridané vzory pripravené na produkciu s monitorovaním a sledovaním štatistík

- **Kompletné prepracovanie 06.ModelsAsTools.md**:
  - Nahradený základný register nástrojov inteligentnou implementáciou smerovača modelov
  - Pridaný výber modelov na základe kľúčových slov pre rôzne typy úloh (všeobecné, logické, kód, kreatívne)
  - Integrovaná konfigurácia na základe prostredia s flexibilným priradením modelov
  - Vylepšené komplexným monitorovaním zdravia služby a spracovaním chýb
  - Pridané vzory nasadenia do produkcie s monitorovaním požiadaviek a sledovaním výkonu
  - Zosúladené s lokálnou implementáciou v `samples/06/router.py` a `samples/06/model_router.ipynb`

- **Vylepšenia štruktúry dokumentácie**:
  - Pridané sekcie prehľadu zdôrazňujúce modernizáciu a zosúladenie SDK
  - Vylepšené s emotikonmi a lepším formátovaním pre zlepšenie čitateľnosti
  - Pridané správne odkazy na lokálne súbory vzoriek naprieč dokumentáciou
  - Zahrnuté pokyny na implementáciu pripravenú na produkciu a najlepšie postupy

### Pridané
- Komplexné sekcie prehľadu v súboroch modulu 08 zdôrazňujúce modernú integráciu SDK
- Hlavné body architektúry ukazujúce pokročilé funkcie (systémy viacerých agentov, inteligentné smerovanie)
- Priame odkazy na lokálne implementácie vzoriek pre praktické skúsenosti
- Pokyny na nasadenie do produkcie so vzormi monitorovania a spracovania chýb
- Interaktívne príklady Jupyter notebookov s pokročilými funkciami a benchmarkmi

### Opravené
- Nesúlady medzi dokumentáciou a skutočnými implementáciami vzoriek
- Zastarané vzory používania SDK naprieč modulom 08
- Chýbajúce odkazy na komplexnú knižnicu lokálnych vzoriek
- Nekonzistentné prístupy k implementácii v rôznych sekciách

---

## 2025-09-18

### Pridané
- Modul 08: Microsoft Foundry Local – Kompletná vývojárska sada nástrojov
  - Šesť relácií: nastavenie, integrácia Azure AI Foundry, open-source modely, špičkové ukážky, agenti a modely ako nástroje
  - Spustiteľné vzorky pod `Module08/samples/01`–`06` s inštrukciami pre Windows cmd
    - `01` REST rýchly chat (`chat_quickstart.py`)
    - `02` SDK rýchly štart s podporou OpenAI/Foundry Local a Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI zoznam a benchmark (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Orchestrácia viacerých agentov (`python -m samples.05.agents.coordinator`)
    - `06` Smerovač modelov ako nástrojov (`router.py`)
- Podpora Azure OpenAI v SDK vzorke relácie 2 s konfiguráciou premenných prostredia
- `.vscode/settings.json` na ukázanie na `Module08/.venv` a zlepšenie rozlíšenia analýzy Pythonu
- `.env` s náznakom `PYTHONPATH` pre povedomie VS Code/Pylance

### Zmenené
- Predvolený model aktualizovaný na `phi-4-mini` naprieč dokumentáciou a vzorkami modulu 08; odstránené zostávajúce zmienky o `phi-3.5` v module 08
- Vylepšenia smerovača (`Module08/samples/06/router.py`):
  - Zisťovanie koncových bodov cez `foundry service status` s regex analýzou
  - Kontrola zdravia `/v1/models` pri štarte
  - Konfigurovateľný register modelov prostredím (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Aktualizované požiadavky: `Module08/requirements.txt` teraz zahŕňa `openai` (spolu s `requests`, `chainlit`)
- Ujasnené pokyny pre vzorku Chainlit a pridané riešenie problémov; rozlíšenie importu cez nastavenia pracovného priestoru

### Opravené
- Vyriešené problémy s importom:
  - Smerovač už nezávisí na neexistujúcom module `utils`; funkcie sú vložené
  - Koordinátor používa relatívny import (`from .specialists import ...`) a je spustený cez cestu modulu
  - Konfigurácia VS Code/Pylance na rozlíšenie `chainlit` a importov balíkov
- Opravená drobná chyba v `STUDY_GUIDE.md` a pridané pokrytie modulu 08

### Odstránené
- Odstránený nepoužívaný `Module08/infra/obs.py` a vymazaný prázdny adresár `infra/`; vzory pozorovateľnosti ponechané ako voliteľné v dokumentácii

### Presunuté
- Konsolidované ukážky modulu 08 pod `Module08/samples` s priečinkami očíslovanými podľa relácií
  - Presunutá aplikácia Chainlit do `samples/04`
  - Presunutí agenti do `samples/05` a pridané súbory `__init__.py` pre rozlíšenie balíkov

### Dokumentácia
- Dokumenty relácií modulu 08 a všetky README vzoriek obohatené o odkazy na Microsoft Learn a dôveryhodných dodávateľov
- `Module08/README.md` aktualizovaný s prehľadom vzoriek, konfiguráciou smerovača a tipmi na validáciu
- `Module07/README.md` sekcia Windows Foundry Local validovaná oproti dokumentom Learn
- `STUDY_GUIDE.md` aktualizovaný:
  - Pridaný modul 08 do prehľadu, rozvrhov, sledovača pokroku
  - Pridaná komplexná sekcia Referencie (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historické (zhrnutie)
- Založená architektúra kurzu a moduly (Moduly 01–07)
- Iteratívna modernizácia obsahu, štandardizácia formátovania a pridané prípadové štúdie
- Rozšírené pokrytie optimalizačných rámcov (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nevydané / Zoznam úloh (návrhy)
- Voliteľné rýchle testy pre každú vzorku na validáciu dostupnosti Foundry Local
- Preskúmanie prekladov na zosúladenie referencií modelov (napr. `phi-4-mini`) kde je to vhodné
- Pridanie minimálnej konfigurácie pyright, ak tímy preferujú prísnosť na úrovni pracovného priestoru

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.