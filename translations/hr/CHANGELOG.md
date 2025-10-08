<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T13:53:47+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "hr"
}
-->
# Dnevnik promjena

Sve značajne promjene u EdgeAI za početnike dokumentirane su ovdje. Ovaj projekt koristi unose temeljene na datumima i stil "Keep a Changelog" (Dodano, Promijenjeno, Ispravljeno, Uklonjeno, Dokumentacija, Premješteno).

## 2025-10-08

### Dodano - Sveobuhvatna nadogradnja radionice
- **Potpuno prepisan README.md radionice**:
  - Dodan sveobuhvatan uvod koji objašnjava vrijednost Edge AI-a (privatnost, performanse, trošak)
  - Kreirano 6 ključnih ciljeva učenja s detaljnim kompetencijama
  - Dodana tablica ishoda učenja s isporukama i matricom kompetencija
  - Uključena sekcija s vještinama spremnim za karijeru za industrijsku relevantnost
  - Dodan vodič za brzi početak s preduvjetima i 3 koraka za postavljanje
  - Kreirane tablice resursa za Python primjere (8 datoteka s vremenima izvođenja)
  - Dodana tablica Jupyter bilježnica (8 bilježnica s ocjenama težine)
  - Kreirana tablica dokumentacije (7 ključnih dokumenata s smjernicama "Kada koristiti")
  - Dodane preporuke za put učenja za različite razine vještina

- **Infrastruktura za validaciju i testiranje radionice**:
  - Kreiran `scripts/validate_samples.py` - Sveobuhvatan alat za validaciju sintakse, uvoza i najboljih praksi
  - Kreiran `scripts/test_samples.py` - Alat za osnovno testiranje svih Python primjera
  - Dodana dokumentacija za validaciju u `scripts/README.md`

- **Sveobuhvatna dokumentacija**:
  - Kreiran `SAMPLES_UPDATE_SUMMARY.md` - Detaljan vodič od 400+ linija koji pokriva sva poboljšanja
  - Kreiran `UPDATE_COMPLETE.md` - Izvršni sažetak završetka nadogradnje
  - Kreiran `QUICK_REFERENCE.md` - Kartica za brzu referencu za radionicu

### Promijenjeno - Modernizacija Python primjera radionice
- **Ažurirano svih 8 Python primjera s najboljim praksama**:
  - Poboljšano rukovanje greškama s try-except blokovima oko svih I/O operacija
  - Dodani tipovi podataka i sveobuhvatni docstringovi
  - Implementiran dosljedan obrazac zapisivanja [INFO]/[ERROR]/[RESULT]
  - Zaštićeni opcionalni uvozi s uputama za instalaciju
  - Poboljšana povratna informacija korisnicima u svim primjerima

- **session01/chat_bootstrap.py**:
  - Poboljšana inicijalizacija klijenta s detaljnim porukama o greškama
  - Poboljšano rukovanje greškama u streamingu s validacijom dijelova
  - Dodano bolje rukovanje iznimkama za nedostupnost usluge

- **session02/rag_pipeline.py**:
  - Dodani zaštitni mehanizmi za uvoze sentence-transformers s uputama za instalaciju
  - Poboljšano rukovanje greškama za operacije ugrađivanja i generiranja
  - Poboljšano formatiranje izlaza sa strukturiranim rezultatima

- **session02/rag_eval_ragas.py**:
  - Zaštićeni opcionalni uvozi (ragas, datasets) s porukama o greškama prilagođenim korisnicima
  - Dodano rukovanje greškama za evaluacijske metrike
  - Poboljšano formatiranje izlaza za rezultate evaluacije

- **session03/benchmark_oss_models.py**:
  - Implementirano graciozno degradiranje (nastavlja se na neuspjeh modela)
  - Dodano detaljno izvještavanje o napretku i rukovanje greškama po modelu
  - Poboljšano izračunavanje statistike s sveobuhvatnim oporavkom od grešaka

- **session04/model_compare.py**:
  - Dodani tipovi podataka (Tuple povratni tipovi)
  - Poboljšano formatiranje izlaza sa strukturiranim JSON rezultatima
  - Implementirano rukovanje greškama po modelu s oporavkom

- **session05/agents_orchestrator.py**:
  - Poboljšano Agent.act() s sveobuhvatnim docstringovima
  - Dodano rukovanje greškama u cjevovodu s zapisivanjem po fazama
  - Poboljšano upravljanje memorijom i praćenje stanja

- **session06/models_router.py**:
  - Poboljšana dokumentacija funkcija za sve komponente usmjeravanja
  - Dodano detaljno zapisivanje u funkciji route()
  - Poboljšan izlaz testova sa strukturiranim rezultatima

- **session06/models_pipeline.py**:
  - Dodano rukovanje greškama u pomoćnoj funkciji chat()
  - Poboljšano pipeline() s zapisivanjem faza i izvještavanjem o napretku
  - Poboljšano main() s sveobuhvatnim oporavkom od grešaka

### Dokumentacija - Poboljšanje dokumentacije radionice
- Ažuriran glavni README.md s sekcijom radionice koja ističe praktični put učenja
- Poboljšan STUDY_GUIDE.md s sveobuhvatnom sekcijom radionice uključujući:
  - Ciljeve učenja i fokusna područja studija
  - Pitanja za samoprocjenu
  - Praktične vježbe s procjenama vremena
  - Dodjela vremena za koncentrirano i povremeno učenje
  - Dodane opise primjera radionice i ishode učenja u README

### Ispravljeno
- Riješeni nekonzistentni obrasci rukovanja greškama u primjerima radionice
- Ispravljene greške u opcionalnim uvozima s odgovarajućim zaštitama
- Ispravljeni nedostajući tipovi podataka u ključnim funkcijama
- Riješena nedovoljna povratna informacija korisnicima u scenarijima grešaka
- Ispravljeni problemi validacije s sveobuhvatnom infrastrukturom testiranja

---

## 2025-09-23

### Promijenjeno - Velika modernizacija Modula 08
- **Sveobuhvatno usklađivanje s obrascima repozitorija Microsoft Foundry-Local**:
  - Ažurirani svi primjeri koda za korištenje modernog `FoundryLocalManager` i integracije OpenAI SDK-a
  - Zamijenjeni zastarjeli ručni pozivi `requests` s odgovarajućim korištenjem SDK-a
  - Usklađeni obrasci implementacije s službenom Microsoft dokumentacijom i primjerima

- **05.AIPoweredAgents.md modernizacija**:
  - Ažurirana orkestracija više agenata za korištenje modernih SDK obrazaca
  - Poboljšana implementacija koordinatora s naprednim značajkama (povratne informacije, praćenje performansi)
  - Dodano sveobuhvatno rukovanje greškama i provjera zdravlja usluge
  - Integrirane odgovarajuće reference na lokalne primjere (`samples/05/multi_agent_orchestration.ipynb`)
  - Ažurirani primjeri poziva funkcija za korištenje modernog parametra `tools` umjesto zastarjelog `functions`
  - Dodani obrasci spremni za produkciju s praćenjem i statistikom

- **06.ModelsAsTools.md potpuna prepiska**:
  - Zamijenjen osnovni registar alata s inteligentnom implementacijom usmjerivača modela
  - Dodana selekcija modela temeljena na ključnim riječima za različite vrste zadataka (opći, zaključivanje, kod, kreativni)
  - Integrirana konfiguracija temeljena na okruženju s fleksibilnim dodjeljivanjem modela
  - Poboljšano sveobuhvatnim praćenjem zdravlja usluge i rukovanjem greškama
  - Dodani obrasci za produkcijsko postavljanje s praćenjem zahtjeva i praćenjem performansi
  - Usklađeno s lokalnom implementacijom u `samples/06/router.py` i `samples/06/model_router.ipynb`

- **Poboljšanja strukture dokumentacije**:
  - Dodane sekcije pregleda koje ističu modernizaciju i usklađivanje sa SDK-om
  - Poboljšano s emojijima i boljim formatiranjem za poboljšanu čitljivost
  - Dodane odgovarajuće reference na lokalne datoteke primjera kroz dokumentaciju
  - Uključene smjernice za implementaciju spremnu za produkciju i najbolje prakse

### Dodano
- Sveobuhvatne sekcije pregleda u datotekama Modula 08 koje ističu modernu integraciju SDK-a
- Istaknute arhitekture koje prikazuju napredne značajke (sustavi više agenata, inteligentno usmjeravanje)
- Izravne reference na lokalne implementacije primjera za praktično iskustvo
- Smjernice za produkcijsko postavljanje s obrascima za praćenje i rukovanje greškama
- Interaktivni primjeri Jupyter bilježnica s naprednim značajkama i usporedbama

### Ispravljeno
- Nesklad između dokumentacije i stvarnih implementacija primjera
- Zastarjeli obrasci korištenja SDK-a kroz Modul 08
- Nedostajuće reference na sveobuhvatnu lokalnu biblioteku primjera
- Nekonzistentni pristupi implementaciji kroz različite sekcije

---

## 2025-09-18

### Dodano
- Modul 08: Microsoft Foundry Local – Kompletan alat za razvojne programere
  - Šest sesija: postavljanje, integracija Azure AI Foundry, open-source modeli, najnoviji demo primjeri, agenti i modeli-kao-alati
  - Primjeri za pokretanje pod `Module08/samples/01`–`06` s Windows cmd uputama
    - `01` REST brzi chat (`chat_quickstart.py`)
    - `02` SDK brzi početak s OpenAI/Foundry Local i podrškom za Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI popis-i-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Orkestracija više agenata (`python -m samples.05.agents.coordinator`)
    - `06` Usmjerivač modela-kao-alata (`router.py`)
- Podrška za Azure OpenAI u SDK primjeru Sesije 2 s konfiguracijom varijabli okruženja
- `.vscode/settings.json` za usmjeravanje na `Module08/.venv` i poboljšanje rezolucije Python analize
- `.env` s naznakom `PYTHONPATH` za svijest VS Code/Pylance-a

### Promijenjeno
- Zadani model ažuriran na `phi-4-mini` kroz dokumentaciju i primjere Modula 08; uklonjeni preostali spomeni `phi-3.5` unutar Modula 08
- Poboljšanja usmjerivača (`Module08/samples/06/router.py`):
  - Otkrivanje krajnjih točaka putem `foundry service status` s regex parsiranjem
  - Provjera zdravlja `/v1/models` pri pokretanju
  - Registar modela konfigurabilan putem okruženja (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Ažurirani zahtjevi: `Module08/requirements.txt` sada uključuje `openai` (uz `requests`, `chainlit`)
- Pojašnjene upute za Chainlit primjer i dodano rješavanje problema; rezolucija uvoza putem postavki radnog prostora

### Ispravljeno
- Riješeni problemi s uvozima:
  - Usmjerivač više ne ovisi o nepostojećem modulu `utils`; funkcije su integrirane
  - Koordinator koristi relativni uvoz (`from .specialists import ...`) i pokreće se putem putanje modula
  - Konfiguracija VS Code/Pylance za rješavanje `chainlit` i uvoza paketa
- Ispravljena manja tipografska greška u `STUDY_GUIDE.md` i dodana pokrivenost Modula 08

### Uklonjeno
- Izbrisano neiskorišteno `Module08/infra/obs.py` i uklonjen prazan direktorij `infra/`; obrasci za promatranje zadržani kao opcionalni u dokumentaciji

### Premješteno
- Konsolidirani demo primjeri Modula 08 pod `Module08/samples` s mapama numeriranim po sesijama
  - Premješten Chainlit app u `samples/04`
  - Premješteni agenti u `samples/05` i dodane `__init__.py` datoteke za rezoluciju paketa

### Dokumentacija
- Dokumentacija sesija Modula 08 i svi README primjeri obogaćeni referencama na Microsoft Learn i pouzdane dobavljače
- `Module08/README.md` ažuriran s Pregledom primjera, konfiguracijom usmjerivača i savjetima za validaciju
- `Module07/README.md` sekcija Windows Foundry Local validirana prema Learn dokumentaciji
- `STUDY_GUIDE.md` ažuriran:
  - Dodan Modul 08 u pregled, rasporede, praćenje napretka
  - Dodana sveobuhvatna sekcija Referenci (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Povijesno (sažetak)
- Uspostavljena arhitektura tečaja i moduli (Moduli 01–07)
- Iterativna modernizacija sadržaja, standardizacija formatiranja i dodane studije slučaja
- Proširena pokrivenost okvira za optimizaciju (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Neobjavljeno / Zaostaci (prijedlozi)
- Opcionalni osnovni testovi po primjeru za validaciju dostupnosti Foundry Local
- Pregled prijevoda za usklađivanje referenci modela (npr. `phi-4-mini`) gdje je primjenjivo
- Dodavanje minimalne konfiguracije pyright ako timovi preferiraju strogoću na razini radnog prostora

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.