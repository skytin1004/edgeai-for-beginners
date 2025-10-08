<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T11:41:48+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sl"
}
-->
# Dnevnik sprememb

Vse pomembne spremembe v EdgeAI za začetnike so dokumentirane tukaj. Ta projekt uporablja zapise, ki temeljijo na datumih, in slog Keep a Changelog (Dodano, Spremenjeno, Popravljeno, Odstranjeno, Dokumentacija, Premaknjeno).

## 2025-10-08

### Dodano - Celovita posodobitev delavnice
- **Popolna prenova README.md za delavnico**:
  - Dodan celovit uvod, ki pojasnjuje prednosti Edge AI (zasebnost, zmogljivost, stroški)
  - Ustvarjenih 6 ključnih učnih ciljev z natančno opredeljenimi kompetencami
  - Dodana tabela učnih rezultatov z dostavki in matriko kompetenc
  - Vključen razdelek o veščinah, pripravljenih za kariero, za industrijsko relevantnost
  - Dodan vodič za hiter začetek z zahtevami in 3-stopenjsko nastavitvijo
  - Ustvarjene tabele virov za Python vzorce (8 datotek z časom izvajanja)
  - Dodana tabela Jupyter zvezkov (8 zvezkov z oceno težavnosti)
  - Ustvarjena tabela dokumentacije (7 ključnih dokumentov z navodili "Kdaj uporabiti")
  - Dodana priporočila za učne poti za različne ravni znanja

- **Infrastruktura za validacijo in testiranje delavnice**:
  - Ustvarjen `scripts/validate_samples.py` - Celovito orodje za validacijo sintakse, uvozov in najboljših praks
  - Ustvarjen `scripts/test_samples.py` - Orodje za hitre teste vseh Python vzorcev
  - Dodana dokumentacija za validacijo v `scripts/README.md`

- **Celovita dokumentacija**:
  - Ustvarjen `SAMPLES_UPDATE_SUMMARY.md` - 400+ vrstic podroben vodič, ki pokriva vse izboljšave
  - Ustvarjen `UPDATE_COMPLETE.md` - Izvršni povzetek dokončanja posodobitve
  - Ustvarjen `QUICK_REFERENCE.md` - Hitri referenčni karton za delavnico

### Spremenjeno - Posodobitev Python vzorcev v delavnici
- **Vsi 8 Python vzorcev posodobljeni z najboljšimi praksami**:
  - Izboljšano obravnavanje napak z bloki try-except okoli vseh I/O operacij
  - Dodani namigi tipov in podrobni docstringi
  - Uveden dosleden vzorec beleženja [INFO]/[ERROR]/[RESULT]
  - Zaščiteni opcijski uvozi z namigi za namestitev
  - Izboljšana povratna informacija uporabniku v vseh vzorcih

- **session01/chat_bootstrap.py**:
  - Izboljšana inicializacija odjemalca z obsežnimi sporočili o napakah
  - Izboljšano obravnavanje napak pri pretakanju z validacijo kosov
  - Dodano boljše obravnavanje izjem za nedostopnost storitve

- **session02/rag_pipeline.py**:
  - Dodani zaščitni uvozi za sentence-transformers z namigi za namestitev
  - Izboljšano obravnavanje napak pri operacijah vdelave in generiranja
  - Izboljšano formatiranje izhodov z strukturiranimi rezultati

- **session02/rag_eval_ragas.py**:
  - Zaščiteni opcijski uvozi (ragas, datasets) z uporabniku prijaznimi sporočili o napakah
  - Dodano obravnavanje napak za evalvacijske metrike
  - Izboljšano formatiranje izhodov za evalvacijske rezultate

- **session03/benchmark_oss_models.py**:
  - Uvedeno elegantno zmanjševanje (nadaljuje ob neuspehu modelov)
  - Dodano podrobno poročanje o napredku in obravnavanje napak za vsak model
  - Izboljšano izračunavanje statistike z obsežnim okrevanjem po napakah

- **session04/model_compare.py**:
  - Dodani namigi tipov (Tuple vrnjene vrednosti)
  - Izboljšano formatiranje izhodov z strukturiranimi JSON rezultati
  - Uvedeno obravnavanje napak za vsak model z okrevanjem

- **session05/agents_orchestrator.py**:
  - Izboljšana funkcija Agent.act() z obsežnimi docstringi
  - Dodano obravnavanje napak v cevovodu z beleženjem po fazah
  - Izboljšano upravljanje pomnilnika in sledenje stanju

- **session06/models_router.py**:
  - Izboljšana dokumentacija funkcij za vse komponente usmerjanja
  - Dodano podrobno beleženje v funkciji route()
  - Izboljšan testni izhod z strukturiranimi rezultati

- **session06/models_pipeline.py**:
  - Dodano obravnavanje napak v pomožni funkciji chat()
  - Izboljšano pipeline() z beleženjem faz in poročanjem o napredku
  - Izboljšano main() z obsežnim okrevanjem po napakah

### Dokumentacija - Izboljšanje dokumentacije delavnice
- Posodobljen glavni README.md z razdelkom delavnice, ki poudarja praktično učno pot
- Izboljšan STUDY_GUIDE.md z obsežnim razdelkom delavnice, vključno z:
  - Učnimi cilji in področji študijskega fokusa
  - Vprašanja za samoocenjevanje
  - Praktične vaje z oceno časa
  - Časovna razporeditev za intenzivno in delno študijo
  - Dodana delavnica v predlogo za sledenje napredku
- Posodobljen vodič za časovno razporeditev z 20 ur na 30 ur (vključno z delavnico)
- Dodani opisi vzorcev delavnice in učni rezultati v README

### Popravljeno
- Odpravljeni neskladni vzorci obravnavanja napak v vzorcih delavnice
- Popravljene napake pri uvozu opcijskih odvisnosti z ustreznimi zaščitami
- Popravljeni manjkajoči namigi tipov v ključnih funkcijah
- Odpravljena nezadostna povratna informacija uporabniku v scenarijih napak
- Popravljene težave pri validaciji z obsežno infrastrukturo testiranja

---

## 2025-09-23

### Spremenjeno - Velika posodobitev modula 08
- **Celovita uskladitev z vzorci repozitorija Microsoft Foundry-Local**:
  - Posodobljeni vsi primeri kode za uporabo sodobnega `FoundryLocalManager` in integracije OpenAI SDK
  - Zamenjani zastareli ročni klici `requests` z ustrezno uporabo SDK
  - Usklajeni vzorci implementacije z uradno Microsoft dokumentacijo in vzorci

- **Posodobitev 05.AIPoweredAgents.md**:
  - Posodobljena orkestracija več agentov za uporabo sodobnih vzorcev SDK
  - Izboljšana implementacija koordinatorja z naprednimi funkcijami (povratne zanke, spremljanje zmogljivosti)
  - Dodano obsežno obravnavanje napak in preverjanje zdravja storitev
  - Integrirane ustrezne reference na lokalne vzorce (`samples/05/multi_agent_orchestration.ipynb`)
  - Posodobljeni primeri klicanja funkcij za uporabo sodobnega parametra `tools` namesto zastarelega `functions`
  - Dodani vzorci, pripravljeni za produkcijo, z nadzorom in spremljanjem statistike

- **Popolna prenova 06.ModelsAsTools.md**:
  - Zamenjana osnovna registracija orodij z inteligentno implementacijo usmerjevalnika modelov
  - Dodana izbira modelov na podlagi ključnih besed za različne vrste nalog (splošno, razmišljanje, koda, ustvarjalno)
  - Integrirana konfiguracija na podlagi okolja z fleksibilno dodelitvijo modelov
  - Izboljšano z obsežnim spremljanjem zdravja storitev in obravnavanjem napak
  - Dodani vzorci za produkcijsko implementacijo z nadzorom zahtevkov in spremljanjem zmogljivosti
  - Usklajeno z lokalno implementacijo v `samples/06/router.py` in `samples/06/model_router.ipynb`

- **Izboljšave strukture dokumentacije**:
  - Dodani pregledni razdelki, ki poudarjajo posodobitve in uskladitev SDK
  - Izboljšano z emojiji in boljšo oblikovanjem za izboljšano berljivost
  - Dodane ustrezne reference na lokalne vzorce datotek skozi dokumentacijo
  - Vključena navodila za implementacijo, pripravljena za produkcijo, in najboljše prakse

### Dodano
- Celoviti pregledni razdelki v datotekah modula 08, ki poudarjajo sodobno integracijo SDK
- Poudarki arhitekture, ki prikazujejo napredne funkcije (sistemi več agentov, inteligentno usmerjanje)
- Neposredne reference na lokalne implementacije vzorcev za praktično izkušnjo
- Navodila za produkcijsko implementacijo z vzorci spremljanja in obravnavanja napak
- Interaktivni primeri Jupyter zvezkov z naprednimi funkcijami in meritvami

### Popravljeno
- Neskladja med dokumentacijo in dejanskimi implementacijami vzorcev
- Zastareli vzorci uporabe SDK skozi modul 08
- Manjkajoče reference na obsežno lokalno knjižnico vzorcev
- Neskladni pristopi implementacije skozi različne razdelke

---

## 2025-09-18

### Dodano
- Modul 08: Microsoft Foundry Local – Celovit razvojni komplet
  - Šest sej: nastavitev, integracija Azure AI Foundry, odprtokodni modeli, napredni demoji, agenti in modeli kot orodja
  - Izvedljivi vzorci pod `Module08/samples/01`–`06` z navodili za Windows cmd
    - `01` REST hitri klepet (`chat_quickstart.py`)
    - `02` SDK hitri začetek z OpenAI/Foundry Local in podporo Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI seznam in primerjava (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Orkestracija več agentov (`python -m samples.05.agents.coordinator`)
    - `06` Usmerjevalnik modelov kot orodij (`router.py`)
- Podpora Azure OpenAI v vzorcu SDK za sejo 2 z nastavitvijo spremenljivk okolja
- `.vscode/settings.json` za usmerjanje na `Module08/.venv` in izboljšanje analize Python kode
- `.env` z namigom `PYTHONPATH` za zavedanje VS Code/Pylance

### Spremenjeno
- Privzeti model posodobljen na `phi-4-mini` skozi dokumentacijo in vzorce modula 08; odstranjene preostale omembe `phi-3.5` znotraj modula 08
- Izboljšave usmerjevalnika (`Module08/samples/06/router.py`):
  - Odkritje končne točke prek `foundry service status` z regex analizo
  - Preverjanje zdravja `/v1/models` ob zagonu
  - Registracija modelov, nastavljiva prek okolja (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Posodobljene zahteve: `Module08/requirements.txt` zdaj vključuje `openai` (poleg `requests`, `chainlit`)
- Pojasnjena navodila za vzorec Chainlit in dodana odprava težav; rešitev uvoza prek nastavitev delovnega prostora

### Popravljeno
- Odpravljene težave z uvozom:
  - Usmerjevalnik ne temelji več na neobstoječem modulu `utils`; funkcije so vgrajene
  - Koordinator uporablja relativni uvoz (`from .specialists import ...`) in se kliče prek poti modula
  - Konfiguracija VS Code/Pylance za rešitev uvozov `chainlit` in paketov
- Popravljena manjša tipkarska napaka v `STUDY_GUIDE.md` in dodana pokritost modula 08

### Odstranjeno
- Izbrisano neuporabljeno `Module08/infra/obs.py` in odstranjena prazna mapa `infra/`; vzorci opazovanja ohranjeni kot opcijski v dokumentaciji

### Premaknjeno
- Konsolidirani demoji modula 08 pod `Module08/samples` z mapami, oštevilčenimi po sejah
  - Premaknjen Chainlit app v `samples/04`
  - Premaknjeni agenti v `samples/05` in dodane datoteke `__init__.py` za rešitev paketov

### Dokumentacija
- Dokumenti sej modula 08 in vsi vzorčni README-ji obogateni z referencami Microsoft Learn in zaupanja vrednih ponudnikov
- `Module08/README.md` posodobljen s pregledom vzorcev, konfiguracijo usmerjevalnika in nasveti za validacijo
- `Module07/README.md` razdelek Windows Foundry Local potrjen glede na Learn dokumentacijo
- `STUDY_GUIDE.md` posodobljen:
  - Dodan modul 08 v pregled, urnike, sledilnik napredka
  - Dodan obsežen razdelek Referenc (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Zgodovinsko (povzetek)
- Ustanovljena arhitektura tečaja in moduli (Moduli 01–07)
- Iterativna modernizacija vsebine, standardizacija oblikovanja in dodane študije primerov
- Razširjena pokritost optimizacijskih okvirov (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Neobjavljeno / Načrt (predlogi)
- Opcijski hitri testi za vsak vzorec za validacijo razpoložljivosti Foundry Local
- Pregled prevodov za uskladitev referenc modelov (npr. `phi-4-mini`) kjer je primerno
- Dodaj minimalno konfiguracijo pyright, če ekipe raje uporabljajo strogo nastavitev na ravni delovnega prostora

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.