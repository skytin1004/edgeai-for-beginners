<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-23T00:45:44+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "hr"
}
-->
# Dnevnik promjena

Sve značajne promjene u EdgeAI za početnike dokumentirane su ovdje. Ovaj projekt koristi unose temeljene na datumima i stil "Keep a Changelog" (Dodano, Promijenjeno, Ispravljeno, Uklonjeno, Dokumentacija, Premješteno).

## 2025-09-18

### Dodano
- Modul 08: Microsoft Foundry Local – Kompletan alat za razvojne programere
  - Šest sesija: postavljanje, integracija Azure AI Foundry, modeli otvorenog koda, najnoviji demo prikazi, agenti i modeli kao alati
  - Uzorci koji se mogu pokrenuti pod `Module08/samples/01`–`06` s uputama za Windows cmd
    - `01` REST brzi chat (`chat_quickstart.py`)
    - `02` SDK brzi početak s OpenAI/Foundry Local i podrškom za Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI popis i testiranje (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Orkestracija više agenata (`python -m samples.05.agents.coordinator`)
    - `06` Router za modele kao alate (`router.py`)
- Podrška za Azure OpenAI u uzorku SDK-a iz Sesije 2 s konfiguracijom varijabli okruženja
- `.vscode/settings.json` za usmjeravanje na `Module08/.venv` i poboljšanje analize Python koda
- `.env` s naznakom `PYTHONPATH` za bolju vidljivost u VS Code/Pylance

### Promijenjeno
- Zadani model ažuriran na `phi-4-mini` u dokumentaciji i uzorcima Modula 08; uklonjeni preostali spomeni `phi-3.5` unutar Modula 08
- Poboljšanja routera (`Module08/samples/06/router.py`):
  - Otkrivanje krajnjih točaka putem `foundry service status` s regex analizom
  - Provjera zdravlja `/v1/models` pri pokretanju
  - Registracija modela konfigurabilna putem varijabli okruženja (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Ažurirani zahtjevi: `Module08/requirements.txt` sada uključuje `openai` (uz `requests`, `chainlit`)
- Pojašnjene upute za Chainlit uzorak i dodano rješavanje problema; razlučivanje uvoza putem postavki radnog prostora

### Ispravljeno
- Riješeni problemi s uvozom:
  - Router više ne ovisi o nepostojećem modulu `utils`; funkcije su integrirane
  - Koordinator koristi relativni uvoz (`from .specialists import ...`) i pokreće se putem putanje modula
  - Konfiguracija VS Code/Pylance za razlučivanje `chainlit` i uvoza paketa
- Ispravljena manja tipografska greška u `STUDY_GUIDE.md` i dodana pokrivenost Modula 08

### Uklonjeno
- Izbrisano neiskorišteno `Module08/infra/obs.py` i uklonjen prazan direktorij `infra/`; obrasci za promatranje zadržani kao opcionalni u dokumentaciji

### Premješteno
- Konsolidirani demo prikazi Modula 08 pod `Module08/samples` s mapama numeriranim prema sesijama
  - Chainlit aplikacija premještena u `samples/04`
  - Agenti premješteni u `samples/05` i dodane `__init__.py` datoteke za razlučivanje paketa

### Dokumentacija
- Dokumentacija sesija Modula 08 i svi README uzorci obogaćeni referencama na Microsoft Learn i pouzdane dobavljače
- `Module08/README.md` ažuriran s Pregledom uzoraka, konfiguracijom routera i savjetima za validaciju
- `Module07/README.md` odjeljak o Windows Foundry Local validiran prema Learn dokumentaciji
- `STUDY_GUIDE.md` ažuriran:
  - Dodan Modul 08 u pregled, rasporede, praćenje napretka
  - Dodan sveobuhvatan odjeljak Referenci (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Povijesno (sažetak)
- Postavljena arhitektura tečaja i moduli (Moduli 01–07)
- Iterativna modernizacija sadržaja, standardizacija formatiranja i dodane studije slučaja
- Proširena pokrivenost okvira za optimizaciju (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Neobjavljeno / Zaostaci (prijedlozi)
- Opcionalni testovi za svaki uzorak kako bi se provjerila dostupnost Foundry Local
- Pregled prijevoda radi usklađivanja referenci modela (npr. `phi-4-mini`) gdje je primjenjivo
- Dodavanje minimalne konfiguracije pyright ako timovi preferiraju strogoću na razini radnog prostora

---

