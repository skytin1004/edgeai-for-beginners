<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-11T10:56:38+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "et"
}
-->
# Muudatuste logi

Kõik olulised muudatused algajatele mõeldud EdgeAI projektis on dokumenteeritud siin. See projekt kasutab kuupäevapõhiseid sissekandeid ja Keep a Changelog stiili (Lisatud, Muudetud, Parandatud, Eemaldatud, Dokumentatsioon, Ümber paigutatud).

## 2025-10-08

### Lisatud - Töötuba põhjalik uuendus
- **Töötoa README.md täielik ümberkirjutus**:
  - Lisatud põhjalik sissejuhatus, mis selgitab Edge AI väärtuspakkumist (privaatsus, jõudlus, kulud)
  - Loodud 6 põhieesmärki koos detailsete oskuste kirjeldustega
  - Lisatud õpitulemuste tabel koos tulemuste ja oskuste maatriksiga
  - Lisatud karjäärivalmiduse oskuste sektsioon tööstuse asjakohasuse jaoks
  - Lisatud kiirjuhend koos eeltingimuste ja 3-etapilise seadistusega
  - Loodud ressursitabelid Python näidete jaoks (8 faili koos käitusaegadega)
  - Lisatud Jupyter märkmike tabel (8 märkmikku koos raskusastmetega)
  - Loodud dokumentatsioonitabel (7 põhidokumenti koos "Kasutamise juhistega")
  - Lisatud õpitee soovitused erinevatele oskustasemetele

- **Töötoa valideerimis- ja testimisinfrastruktuur**:
  - Loodud `scripts/validate_samples.py` - põhjalik valideerimistööriist süntaksi, impordivigade ja parimate tavade kontrollimiseks
  - Loodud `scripts/test_samples.py` - suitsutestide käivitaja kõigile Python näidetele
  - Lisatud valideerimise dokumentatsioon `scripts/README.md`-sse

- **Põhjalik dokumentatsioon**:
  - Loodud `SAMPLES_UPDATE_SUMMARY.md` - üle 400-realine detailne juhend kõigi täiustuste kohta
  - Loodud `UPDATE_COMPLETE.md` - uuenduse lõpuleviimise kokkuvõte
  - Loodud `QUICK_REFERENCE.md` - kiire viitekaart töötoa jaoks

### Muudetud - Töötoa Python näidete moderniseerimine
- **Kõik 8 Python näidet uuendatud parimate tavade järgi**:
  - Täiustatud veakäsitlust try-except plokkidega kõigi I/O operatsioonide ümber
  - Lisatud tüübiviited ja põhjalikud docstringid
  - Rakendatud ühtne [INFO]/[ERROR]/[RESULT] logimismuster
  - Kaitstud valikulised impordid koos paigaldusjuhistega
  - Parandatud kasutajate tagasisidet kõigis näidetes

- **session01/chat_bootstrap.py**:
  - Täiustatud kliendi initsialiseerimist põhjalike veateadetega
  - Parandatud voogedastusveakäsitlust tükkide valideerimisega
  - Lisatud parem erandite käsitlus teenuse kättesaamatuse korral

- **session02/rag_pipeline.py**:
  - Lisatud impordikaitsed sentence-transformers jaoks koos paigaldusjuhistega
  - Täiustatud veakäsitlust sisestamise ja genereerimise operatsioonide jaoks
  - Parandatud väljundi vormindamist struktureeritud tulemustega

- **session02/rag_eval_ragas.py**:
  - Kaitstud valikulised impordid (ragas, datasets) kasutajasõbralike veateadetega
  - Lisatud veakäsitlus hindamismõõdikute jaoks
  - Täiustatud väljundi vormindamist hindamistulemustele

- **session03/benchmark_oss_models.py**:
  - Rakendatud sujuv degradeerumine (jätkab mudelite tõrgete korral)
  - Lisatud detailne edenemisaruandlus ja mudelipõhine veakäsitlus
  - Täiustatud statistika arvutamist põhjaliku veakäsitlusega

- **session04/model_compare.py**:
  - Lisatud tüübiviited (Tuple tagastustüübid)
  - Täiustatud väljundi vormindamist struktureeritud JSON tulemustega
  - Rakendatud mudelipõhine veakäsitlus koos taastumisega

- **session05/agents_orchestrator.py**:
  - Täiustatud Agent.act() põhjalike docstringidega
  - Lisatud torujuhtme veakäsitlus etappide kaupa logimisega
  - Parandatud mälu haldamist ja oleku jälgimist

- **session06/models_router.py**:
  - Täiustatud funktsioonide dokumentatsiooni kõigi marsruutimiskomponentide jaoks
  - Lisatud detailne logimine route() funktsioonis
  - Parandatud testide väljund struktureeritud tulemustega

- **session06/models_pipeline.py**:
  - Lisatud veakäsitlus chat() abifunktsioonile
  - Täiustatud pipeline() etappide logimise ja edenemisaruandlusega
  - Parandatud main() põhjaliku veakäsitlusega

### Dokumentatsioon - Töötoa dokumentatsiooni täiustamine
- Uuendatud peamine README.md töötoa sektsiooniga, mis rõhutab praktilist õpiteed
- Täiustatud STUDY_GUIDE.md põhjaliku töötoa sektsiooniga, mis sisaldab:
  - Õpieesmärke ja õppe fookusvaldkondi
  - Enesehindamise küsimusi
  - Praktilisi harjutusi koos ajahinnangutega
  - Aja jaotust intensiivseks ja osaliseks õppimiseks
  - Lisatud töötuba edusammude jälgimise mallile
- Uuendatud aja jaotuse juhend 20 tunnilt 30 tunnile (sh töötuba)
- Lisatud töötoa näidete kirjeldused ja õpitulemused README-sse

### Parandatud
- Lahendatud ebajärjekindlad veakäsitluse mustrid töötoa näidetes
- Parandatud valikuliste sõltuvuste impordivead koos korralike kaitsetega
- Parandatud puuduvad tüübiviited kriitilistes funktsioonides
- Lahendatud ebapiisav kasutajate tagasiside veastsenaariumides
- Parandatud valideerimisprobleemid põhjaliku testimisinfrastruktuuriga

---

## 2025-09-23

### Muudetud - Suur mooduli 08 moderniseerimine
- **Põhjalik joondamine Microsoft Foundry-Local repositooriumi mustritega**
  - Kõik koodinäited uuendatud kasutama kaasaegset `FoundryLocalManager`-i ja OpenAI SDK integratsiooni
  - Asendatud vananenud manuaalsed `requests`-kutsed korraliku SDK kasutamisega
  - Joondatud rakendusmustrid ametliku Microsofti dokumentatsiooni ja näidetega

- **05.AIPoweredAgents.md moderniseerimine**:
  - Uuendatud multi-agent orkestreerimine kaasaegsete SDK mustrite kasutamiseks
  - Täiustatud koordinaatori rakendamine täiustatud funktsioonidega (tagasiside tsüklid, jõudluse jälgimine)
  - Lisatud põhjalik veakäsitlus ja teenuse tervise kontroll
  - Integreeritud korralikud viited kohalikele näidetele (`samples/05/multi_agent_orchestration.ipynb`)
  - Uuendatud funktsioonikutsed kasutama kaasaegset `tools` parameetrit, mitte vananenud `functions`
  - Lisatud tootmisvalmis mustrid jälgimise ja statistika jälgimisega

- **06.ModelsAsTools.md täielik ümberkirjutus**:
  - Asendatud lihtne tööriistade register intelligentse mudelite marsruutimise rakendusega
  - Lisatud märksõnapõhine mudelivalik erinevate ülesandetüüpide jaoks (üldine, põhjendamine, kood, loominguline)
  - Integreeritud keskkonnapõhine konfiguratsioon paindliku mudelite määramisega
  - Täiustatud põhjaliku teenuse tervise jälgimise ja veakäsitlusega
  - Lisatud tootmisjuurutamise mustrid koos päringute jälgimise ja jõudluse jälgimisega
  - Joondatud kohaliku rakendusega `samples/06/router.py` ja `samples/06/model_router.ipynb`

- **Dokumentatsiooni struktuuri täiustused**:
  - Lisatud ülevaate sektsioonid, mis rõhutavad moderniseerimist ja SDK joondamist
  - Täiustatud emotikonide ja parema vormindusega, et parandada loetavust
  - Lisatud korralikud viited kohalikele näidistele kogu dokumentatsioonis
  - Kaasatud tootmisvalmis rakenduse juhised ja parimad tavad

### Lisatud
- Põhjalikud ülevaate sektsioonid mooduli 08 failides, mis rõhutavad kaasaegset SDK integratsiooni
- Arhitektuuri esiletõstmised, mis näitavad täiustatud funktsioone (multi-agent süsteemid, intelligentne marsruutimine)
- Otsesed viited kohalikele näidistele praktilise kogemuse saamiseks
- Tootmisjuurutamise juhised jälgimise ja veakäsitluse mustritega
- Interaktiivsed Jupyter märkmike näited täiustatud funktsioonide ja võrdlustega

### Parandatud
- Joondamise lahknevused dokumentatsiooni ja tegelike näidiste vahel
- Vananenud SDK kasutusmustrid kogu moodulis 08
- Puuduvad viited põhjalikule kohalikule näidiste raamatukogule
- Ebajärjekindlad rakenduslähenemised erinevates sektsioonides

---

## 2025-09-18

### Lisatud
- Moodul 08: Microsoft Foundry Local – täielik arendaja tööriistakomplekt
  - Kuus sessiooni: seadistamine, Azure AI Foundry integratsioon, avatud lähtekoodiga mudelid, tipptasemel demod, agendid ja mudelid-tööriistadena
  - Käivitatavad näited kaustas `Module08/samples/01`–`06` koos Windows cmd juhistega
    - `01` REST kiire vestlus (`chat_quickstart.py`)
    - `02` SDK kiire algus OpenAI/Foundry Local ja Azure OpenAI toega (`sdk_quickstart.py`)
    - `03` CLI loetelu ja võrdlus (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orkestreerimine (`python -m samples.05.agents.coordinator`)
    - `06` Mudelid-tööriistadena marsruuter (`router.py`)
- Azure OpenAI tugi sessiooni 2 SDK näites koos keskkonnamuutuja konfiguratsiooniga
- `.vscode/settings.json`, et osutada `Module08/.venv`-ile ja parandada Pythoni analüüsi lahendust
- `.env` koos `PYTHONPATH` vihjega VS Code/Pylance'i jaoks

### Muudetud
- Vaikimisi mudel uuendatud `phi-4-mini`-ks kogu mooduli 08 dokumentides ja näidetes; eemaldatud ülejäänud viited `phi-3.5`-le
- Marsruuteri (`Module08/samples/06/router.py`) täiustused:
  - Lõpp-punktide avastamine `foundry service status` regex-parsimisega
  - `/v1/models` tervisekontroll käivitamisel
  - Keskkonnaga konfigureeritav mudeliregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Nõuded uuendatud: `Module08/requirements.txt` sisaldab nüüd `openai` (koos `requests`, `chainlit`-iga)
- Chainlit näidise juhised täpsustatud ja lisatud tõrkeotsing; impordi lahendamine tööruumi seadistuste kaudu

### Parandatud
- Lahendatud impordiprobleemid:
  - Marsruuter ei sõltu enam olematust `utils` moodulist; funktsioonid on integreeritud
  - Koordinaator kasutab suhtelist importi (`from .specialists import ...`) ja käivitatakse mooduli teel
  - VS Code/Pylance konfiguratsioon, et lahendada `chainlit` ja paketi impordid
- Parandatud väike kirjaviga `STUDY_GUIDE.md`-s ja lisatud mooduli 08 kajastus

### Eemaldatud
- Kustutatud kasutamata `Module08/infra/obs.py` ja eemaldatud tühi `infra/` kaust; jälgitavuse mustrid säilitatud valikulistena dokumentatsioonis

### Ümber paigutatud
- Konsolideeritud mooduli 08 demod kausta `Module08/samples` sessiooni numbriga kaustadesse
  - Chainlit rakendus viidud kausta `samples/04`
  - Agendid viidud kausta `samples/05` ja lisatud `__init__.py` failid paketi lahendamiseks

### Dokumentatsioon
- Mooduli 08 sessiooni dokumendid ja kõik näidiste README-d rikastatud Microsoft Learn ja usaldusväärsete tarnijate viidetega
- `Module08/README.md` uuendatud näidiste ülevaate, marsruuteri konfiguratsiooni ja valideerimise näpunäidetega
- `Module07/README.md` Windows Foundry Local sektsioon valideeritud Learn dokumentide vastu
- `STUDY_GUIDE.md` uuendatud:
  - Lisatud moodul 08 ülevaatesse, ajakavadesse, edusammude jälgijasse
  - Lisatud põhjalik viidete sektsioon (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Ajalooline (kokkuvõte)
- Kursuse arhitektuur ja moodulid loodud (Moodulid 01–07)
- Iteratiivne sisu moderniseerimine, vormindamise standardiseerimine ja lisatud juhtumiuuringud
- Laiendatud optimeerimisraamistike kajastus (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Avaldamata / Ootel (ettepanekud)
- Valikulised näidiste suitsutestid Foundry Local saadavuse valideerimiseks
- Tõlgete ülevaatus mudelite viidete joondamiseks (nt `phi-4-mini`)
- Minimaalse pyright konfiguratsiooni lisamine, kui meeskonnad eelistavad tööruumi tasemel rangust

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.