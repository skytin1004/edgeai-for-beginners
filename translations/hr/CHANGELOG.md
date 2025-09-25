<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T02:00:00+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "hr"
}
-->
# Dnevnik promjena

Sve značajne promjene u projektu EdgeAI za početnike dokumentirane su ovdje. Ovaj projekt koristi unose temeljene na datumima i stil "Keep a Changelog" (Dodano, Promijenjeno, Ispravljeno, Uklonjeno, Dokumentacija, Premješteno).

## 2025-09-23

### Promijenjeno - Velika modernizacija Modula 08
- **Sveobuhvatno usklađivanje s obrascima repozitorija Microsoft Foundry-Local**
  - Ažurirani svi primjeri koda za korištenje modernog `FoundryLocalManager` i integracije OpenAI SDK-a
  - Zamijenjeni zastarjeli ručni pozivi `requests` odgovarajućom upotrebom SDK-a
  - Usklađeni obrasci implementacije s službenom Microsoft dokumentacijom i uzorcima

- **Modernizacija 05.AIPoweredAgents.md**:
  - Ažurirana orkestracija više agenata za korištenje modernih SDK obrazaca
  - Poboljšana implementacija koordinatora s naprednim značajkama (povratne petlje, praćenje performansi)
  - Dodano sveobuhvatno rukovanje greškama i provjera zdravlja usluge
  - Integrirane odgovarajuće reference na lokalne uzorke (`samples/05/multi_agent_orchestration.ipynb`)
  - Ažurirani primjeri pozivanja funkcija za korištenje modernog parametra `tools` umjesto zastarjelog `functions`
  - Dodani obrasci spremni za produkciju s praćenjem i statistikom

- **Potpuno prepisivanje 06.ModelsAsTools.md**:
  - Zamijenjen osnovni registar alata inteligentnim implementacijom modela usmjerivača
  - Dodana selekcija modela temeljena na ključnim riječima za različite vrste zadataka (opći, zaključivanje, kod, kreativni)
  - Integrirana konfiguracija temeljena na okruženju s fleksibilnim dodjeljivanjem modela
  - Poboljšano sveobuhvatnim praćenjem zdravlja usluge i rukovanjem greškama
  - Dodani obrasci za produkcijsko postavljanje s praćenjem zahtjeva i performansi
  - Usklađeno s lokalnom implementacijom u `samples/06/router.py` i `samples/06/model_router.ipynb`

- **Poboljšanja strukture dokumentacije**:
  - Dodani pregledni odjeljci koji ističu modernizaciju i usklađivanje s SDK-om
  - Poboljšano s emotikonima i boljim formatiranjem za bolju čitljivost
  - Dodane odgovarajuće reference na lokalne uzorke datoteka kroz dokumentaciju
  - Uključene smjernice za implementaciju spremnu za produkciju i najbolje prakse

### Dodano
- Sveobuhvatni pregledni odjeljci u datotekama Modula 08 koji ističu modernu integraciju SDK-a
- Istaknute arhitekture koje prikazuju napredne značajke (sustavi više agenata, inteligentno usmjeravanje)
- Izravne reference na lokalne implementacije uzoraka za praktično iskustvo
- Smjernice za produkcijsko postavljanje s obrascima za praćenje i rukovanje greškama
- Interaktivni primjeri Jupyter bilježnica s naprednim značajkama i usporednim testovima

### Ispravljeno
- Nepodudarnosti između dokumentacije i stvarnih implementacija uzoraka
- Zastarjeli obrasci korištenja SDK-a kroz Modul 08
- Nedostajuće reference na sveobuhvatnu lokalnu biblioteku uzoraka
- Nedosljedni pristupi implementaciji u različitim odjeljcima

---

## 2025-09-18

### Dodano
- Modul 08: Microsoft Foundry Local – Kompletan alat za razvojne programere
  - Šest sesija: postavljanje, integracija Azure AI Foundry, open-source modeli, najnoviji demo primjeri, agenti i modeli kao alati
  - Izvedivi uzorci pod `Module08/samples/01`–`06` s Windows cmd uputama
    - `01` REST brzi chat (`chat_quickstart.py`)
    - `02` SDK brzi početak s OpenAI/Foundry Local i podrškom za Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI popis i usporedba (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Orkestracija više agenata (`python -m samples.05.agents.coordinator`)
    - `06` Usmjerivač modela kao alata (`router.py`)
- Podrška za Azure OpenAI u uzorku SDK-a Sesije 2 s konfiguracijom varijabli okruženja
- `.vscode/settings.json` za usmjeravanje na `Module08/.venv` i poboljšanje rezolucije analize Python-a
- `.env` s naznakom `PYTHONPATH` za svijest VS Code/Pylance-a

### Promijenjeno
- Zadani model ažuriran na `phi-4-mini` kroz dokumentaciju i uzorke Modula 08; uklonjeni preostali spomeni `phi-3.5` unutar Modula 08
- Poboljšanja usmjerivača (`Module08/samples/06/router.py`):
  - Otkrivanje krajnjih točaka putem `foundry service status` s regex analizom
  - Provjera zdravlja `/v1/models` pri pokretanju
  - Registar modela konfiguriran putem okruženja (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Ažurirani zahtjevi: `Module08/requirements.txt` sada uključuje `openai` (uz `requests`, `chainlit`)
- Pojašnjene smjernice za uzorak Chainlit i dodano rješavanje problema; rezolucija uvoza putem postavki radnog prostora

### Ispravljeno
- Riješeni problemi s uvozom:
  - Usmjerivač više ne ovisi o nepostojećem modulu `utils`; funkcije su integrirane
  - Koordinator koristi relativni uvoz (`from .specialists import ...`) i pokreće se putem putanje modula
  - Konfiguracija VS Code/Pylance za rješavanje `chainlit` i uvoza paketa
- Ispravljena manja tipografska greška u `STUDY_GUIDE.md` i dodana pokrivenost Modula 08

### Uklonjeno
- Izbrisano neiskorišteno `Module08/infra/obs.py` i uklonjen prazan direktorij `infra/`; obrasci za promatranje zadržani kao opcionalni u dokumentaciji

### Premješteno
- Konsolidirani demo primjeri Modula 08 pod `Module08/samples` s mapama numeriranim po sesijama
  - Chainlit aplikacija premještena u `samples/04`
  - Agenti premješteni u `samples/05` i dodane `__init__.py` datoteke za rezoluciju paketa

### Dokumentacija
- Dokumentacija sesija Modula 08 i svi README uzorci obogaćeni referencama na Microsoft Learn i pouzdane dobavljače
- `Module08/README.md` ažuriran s Pregledom uzoraka, konfiguracijom usmjerivača i savjetima za validaciju
- `Module07/README.md` odjeljak Windows Foundry Local validiran prema Learn dokumentaciji
- `STUDY_GUIDE.md` ažuriran:
  - Dodan Modul 08 u pregled, rasporede, praćenje napretka
  - Dodan sveobuhvatan odjeljak Referenci (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Povijesno (sažetak)
- Arhitektura tečaja i moduli uspostavljeni (Moduli 01–07)
- Iterativna modernizacija sadržaja, standardizacija formatiranja i dodani studiji slučaja
- Proširena pokrivenost okvira za optimizaciju (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nepušteno / Zaostaci (prijedlozi)
- Opcionalni testovi po uzorku za provjeru dostupnosti Foundry Local
- Pregled prijevoda za usklađivanje referenci modela (npr. `phi-4-mini`) gdje je primjenjivo
- Dodavanje minimalne konfiguracije pyright ako timovi preferiraju strogoću na razini radnog prostora

---

