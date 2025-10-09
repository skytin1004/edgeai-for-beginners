<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T20:57:30+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "lt"
}
-->
# Pakeitimų žurnalas

Visi svarbūs EdgeAI for Beginners pakeitimai dokumentuojami čia. Šis projektas naudoja įrašus pagal datas ir „Keep a Changelog“ stilių (Pridėta, Pakeista, Ištaisyta, Pašalinta, Dokumentai, Perkelta).

## 2025-10-08

### Pridėta - Išsamus dirbtuvių atnaujinimas
- **Dirbtuvių README.md visiškai perrašytas**:
  - Pridėtas išsamus įvadas, paaiškinantis Edge AI vertės pasiūlymą (privatumas, našumas, kaina)
  - Sukurti 6 pagrindiniai mokymosi tikslai su detalizuotomis kompetencijomis
  - Pridėta mokymosi rezultatų lentelė su pristatymais ir kompetencijų matrica
  - Įtraukta karjerai reikalingų įgūdžių skiltis, pabrėžianti pramonės aktualumą
  - Pridėtas greito starto vadovas su reikalavimais ir 3 žingsnių nustatymu
  - Sukurtos išteklių lentelės Python pavyzdžiams (8 failai su vykdymo laiku)
  - Pridėta Jupyter užrašų knygelių lentelė (8 užrašų knygelės su sudėtingumo įvertinimais)
  - Sukurta dokumentacijos lentelė (7 pagrindiniai dokumentai su „Naudoti kada“ gairėmis)
  - Pridėtos mokymosi kelio rekomendacijos skirtingiems įgūdžių lygiams

- **Dirbtuvių validavimo ir testavimo infrastruktūra**:
  - Sukurtas `scripts/validate_samples.py` - Išsamus validavimo įrankis sintaksei, importams ir geriausioms praktikoms
  - Sukurtas `scripts/test_samples.py` - Greitas testavimo įrankis visiems Python pavyzdžiams
  - Pridėta validavimo dokumentacija į `scripts/README.md`

- **Išsami dokumentacija**:
  - Sukurtas `SAMPLES_UPDATE_SUMMARY.md` - 400+ eilučių išsamus vadovas, apimantis visus patobulinimus
  - Sukurtas `UPDATE_COMPLETE.md` - Atnaujinimo užbaigimo vykdomoji santrauka
  - Sukurtas `QUICK_REFERENCE.md` - Greitojo nuorodų kortelė dirbtuvėms

### Pakeista - Dirbtuvių Python pavyzdžių modernizavimas
- **Visi 8 Python pavyzdžiai atnaujinti pagal geriausias praktikas**:
  - Patobulintas klaidų tvarkymas su try-except blokais aplink visus I/O veiksmus
  - Pridėtos tipų užuominos ir išsamūs docstring'ai
  - Įgyvendintas nuoseklus [INFO]/[ERROR]/[RESULT] logavimo modelis
  - Apsaugoti pasirenkami importai su diegimo užuominomis
  - Patobulintas naudotojo grįžtamasis ryšys visuose pavyzdžiuose

- **session01/chat_bootstrap.py**:
  - Patobulinta kliento inicializacija su išsamiais klaidų pranešimais
  - Pagerintas srauto klaidų tvarkymas su fragmentų validacija
  - Pridėtas geresnis išimčių tvarkymas paslaugos nepasiekiamumo atveju

- **session02/rag_pipeline.py**:
  - Pridėti importo apsaugos mechanizmai sentence-transformers su diegimo užuominomis
  - Patobulintas klaidų tvarkymas įterpimo ir generavimo veiksmuose
  - Pagerintas išvesties formatavimas su struktūrizuotais rezultatais

- **session02/rag_eval_ragas.py**:
  - Apsaugoti pasirenkami importai (ragas, datasets) su naudotojui draugiškais klaidų pranešimais
  - Pridėtas klaidų tvarkymas vertinimo metrikoms
  - Patobulintas išvesties formatavimas vertinimo rezultatams

- **session03/benchmark_oss_models.py**:
  - Įgyvendintas grakštus degradavimas (tęsia modelio gedimų atveju)
  - Pridėtas detalus pažangos ataskaitų teikimas ir klaidų tvarkymas kiekvienam modeliui
  - Patobulinta statistikos skaičiavimas su išsamiu klaidų atkūrimu

- **session04/model_compare.py**:
  - Pridėtos tipų užuominos (Tuple grąžinimo tipai)
  - Patobulintas išvesties formatavimas su struktūrizuotais JSON rezultatais
  - Įgyvendintas klaidų tvarkymas kiekvienam modeliui su atkūrimu

- **session05/agents_orchestrator.py**:
  - Patobulintas Agent.act() su išsamiais docstring'ais
  - Pridėtas klaidų tvarkymas pipeline su etapų logavimu
  - Pagerintas atminties valdymas ir būsenos sekimas

- **session06/models_router.py**:
  - Patobulinta funkcijų dokumentacija visiems maršrutizavimo komponentams
  - Pridėtas detalus logavimas route() funkcijoje
  - Pagerintas testų išvestis su struktūrizuotais rezultatais

- **session06/models_pipeline.py**:
  - Pridėtas klaidų tvarkymas chat() pagalbinėje funkcijoje
  - Patobulintas pipeline() su etapų logavimu ir pažangos ataskaitų teikimu
  - Pagerintas main() su išsamiu klaidų atkūrimu

### Dokumentai - Dirbtuvių dokumentacijos patobulinimas
- Atnaujintas pagrindinis README.md su dirbtuvių skiltimi, pabrėžiančia praktinį mokymosi kelią
- Patobulintas STUDY_GUIDE.md su išsamia dirbtuvių skiltimi, įskaitant:
  - Mokymosi tikslus ir studijų fokusavimo sritis
  - Savęs vertinimo klausimus
  - Praktinius pratimus su laiko įvertinimais
  - Laiko paskirstymą intensyviam ir daliniam studijavimui
  - Pridėta dirbtuvės į pažangos sekimo šabloną
- Atnaujintas laiko paskirstymo vadovas nuo 20 valandų iki 30 valandų (įskaitant dirbtuves)
- Pridėta dirbtuvių pavyzdžių aprašymai ir mokymosi rezultatai į README

### Ištaisyta
- Išspręstos nenuoseklios klaidų tvarkymo schemos dirbtuvių pavyzdžiuose
- Ištaisyti pasirenkamų priklausomybių importo klaidos su tinkamais apsaugos mechanizmais
- Ištaisyti trūkstami tipų užuominos kritinėse funkcijose
- Išspręstos nepakankamo naudotojo grįžtamojo ryšio problemos klaidų scenarijuose
- Ištaisyti validavimo klausimai su išsamia testavimo infrastruktūra

---

## 2025-09-23

### Pakeista - Didelis 08 modulio modernizavimas
- **Išsamus suderinimas su Microsoft Foundry-Local saugyklos šablonais**
  - Atnaujinti visi kodo pavyzdžiai, naudojant modernų `FoundryLocalManager` ir OpenAI SDK integraciją
  - Pakeisti pasenę rankiniai `requests` skambučiai tinkama SDK naudojimu
  - Suderinti įgyvendinimo šablonai su oficialia Microsoft dokumentacija ir pavyzdžiais

- **05.AIPoweredAgents.md modernizavimas**:
  - Atnaujinta daugiaveiksnių orkestracija, naudojant modernius SDK šablonus
  - Patobulinta koordinatoriaus įgyvendinimas su pažangiomis funkcijomis (grįžtamojo ryšio ciklai, našumo stebėjimas)
  - Pridėtas išsamus klaidų tvarkymas ir paslaugų sveikatos tikrinimas
  - Integruotos tinkamos nuorodos į vietinius pavyzdžius (`samples/05/multi_agent_orchestration.ipynb`)
  - Atnaujinti funkcijų skambučio pavyzdžiai, naudojant modernų `tools` parametrą vietoj pasenusio `functions`
  - Pridėti gamybai paruošti šablonai su stebėjimu ir statistikos sekimu

- **06.ModelsAsTools.md visiškai perrašytas**:
  - Pakeista paprasta įrankių registracija į intelektualų modelių maršrutizavimo įgyvendinimą
  - Pridėtas modelių pasirinkimas pagal raktinius žodžius skirtingoms užduotims (bendros, loginės, kodo, kūrybinės)
  - Integruota aplinkos pagrindu konfigūracija su lankstiu modelių priskyrimu
  - Patobulinta su išsamiu paslaugų sveikatos stebėjimu ir klaidų tvarkymu
  - Pridėti gamybos diegimo šablonai su užklausų stebėjimu ir našumo sekimu
  - Suderinta su vietiniu įgyvendinimu `samples/06/router.py` ir `samples/06/model_router.ipynb`

- **Dokumentacijos struktūros patobulinimai**:
  - Pridėtos apžvalgos skiltys, pabrėžiančios modernizavimą ir SDK suderinimą
  - Patobulinta su emocijomis ir geresniu formatavimu, siekiant pagerinti skaitomumą
  - Pridėtos tinkamos nuorodos į vietinius pavyzdžių failus visoje dokumentacijoje
  - Įtraukta gamybai paruošto įgyvendinimo gairės ir geriausios praktikos

### Pridėta
- Išsamios apžvalgos skiltys 08 modulio failuose, pabrėžiančios modernią SDK integraciją
- Architektūros akcentai, pristatantys pažangias funkcijas (daugiaveiksnių sistemas, intelektualų maršrutizavimą)
- Tiesioginės nuorodos į vietinius pavyzdžių įgyvendinimus praktinei patirčiai
- Gamybos diegimo gairės su stebėjimo ir klaidų tvarkymo šablonais
- Interaktyvūs Jupyter užrašų knygelių pavyzdžiai su pažangiomis funkcijomis ir našumo testais

### Ištaisyta
- Suderinimo neatitikimai tarp dokumentacijos ir faktinių pavyzdžių įgyvendinimų
- Pasenę SDK naudojimo šablonai visame 08 modulyje
- Trūkstamos nuorodos į išsamų vietinių pavyzdžių biblioteką
- Nenuoseklūs įgyvendinimo metodai skirtingose skiltyse

---

## 2025-09-18

### Pridėta
- Modulis 08: Microsoft Foundry Local – Pilnas kūrėjų įrankių rinkinys
  - Šešios sesijos: nustatymas, Azure AI Foundry integracija, atvirojo kodo modeliai, pažangūs demonstraciniai pavyzdžiai, agentai ir modeliai kaip įrankiai
  - Vykdomi pavyzdžiai `Module08/samples/01`–`06` su Windows cmd instrukcijomis
    - `01` REST greitas pokalbis (`chat_quickstart.py`)
    - `02` SDK greitas startas su OpenAI/Foundry Local ir Azure OpenAI palaikymu (`sdk_quickstart.py`)
    - `03` CLI sąrašas ir testavimas (`list_and_bench.cmd`)
    - `04` Chainlit demonstracija (`app.py`)
    - `05` Daugiaveiksnių orkestracija (`python -m samples.05.agents.coordinator`)
    - `06` Modeliai kaip įrankiai maršrutizatorius (`router.py`)
- Azure OpenAI palaikymas 2 sesijos SDK pavyzdyje su aplinkos kintamųjų konfigūracija
- `.vscode/settings.json`, kad nurodytų `Module08/.venv` ir pagerintų Python analizės sprendimą
- `.env` su `PYTHONPATH` užuomina VS Code/Pylance supratimui

### Pakeista
- Numatyto modelio atnaujinimas į `phi-4-mini` visame 08 modulio dokumentuose ir pavyzdžiuose; pašalinti likę `phi-3.5` paminėjimai 08 modulyje
- Maršrutizatoriaus (`Module08/samples/06/router.py`) patobulinimai:
  - Galinių taškų aptikimas per `foundry service status` su regex analizavimu
  - `/v1/models` sveikatos patikrinimas paleidimo metu
  - Aplinkos konfigūruojama modelių registracija (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Reikalavimai atnaujinti: `Module08/requirements.txt` dabar apima `openai` (kartu su `requests`, `chainlit`)
- Chainlit pavyzdžių gairės patikslintos ir pridėtas trikčių šalinimas; importo sprendimas per darbo aplinkos nustatymus

### Ištaisyta
- Išspręstos importo problemos:
  - Maršrutizatorius nebepriklauso nuo neegzistuojančio `utils` modulio; funkcijos yra įtrauktos
  - Koordinatorius naudoja santykinį importą (`from .specialists import ...`) ir yra paleidžiamas per modulio kelią
  - VS Code/Pylance konfigūracija, kad išspręstų `chainlit` ir paketų importus
- Ištaisyta nedidelė klaida `STUDY_GUIDE.md` ir pridėta 08 modulio aprėptis

### Pašalinta
- Ištrintas nenaudojamas `Module08/infra/obs.py` ir pašalintas tuščias `infra/` katalogas; stebėjimo šablonai išlaikyti kaip pasirenkami dokumentuose

### Perkelta
- Konsoliduoti 08 modulio demonstraciniai pavyzdžiai po `Module08/samples` su sesijos numeruotais aplankais
  - Perkelta Chainlit programa į `samples/04`
  - Perkelti agentai į `samples/05` ir pridėti `__init__.py` failai paketų sprendimui

### Dokumentai
- 08 modulio sesijos dokumentai ir visi pavyzdžių README praturtinti Microsoft Learn ir patikimų tiekėjų nuorodomis
- `Module08/README.md` atnaujintas su pavyzdžių apžvalga, maršrutizatoriaus konfigūracija ir validavimo patarimais
- `Module07/README.md` Windows Foundry Local skiltis patikrinta pagal Learn dokumentus
- `STUDY_GUIDE.md` atnaujintas:
  - Pridėtas 08 modulis į apžvalgą, tvarkaraščius, pažangos sekimo priemonę
  - Pridėta išsami nuorodų skiltis (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Istorinis (santrauka)
- Kurso architektūra ir moduliai sukurti (Moduliai 01–07)
- Iteratyvus turinio modernizavimas, formatavimo standartizavimas ir pridėtos atvejų studijos
- Išplėsta optimizavimo sistemų aprėptis (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Neišleista / Laukiama (pasiūlymai)
- Pasirenkami kiekvieno pavyzdžio greiti testai, kad būtų patikrintas Foundry Local prieinamumas
- Peržiūrėti vertimus, kad būtų suderinti modelių paminėjimai (pvz., `phi-4-mini`) kur tinkama
- Pridėti minimalų pyright konfigūraciją, jei komandos pageidauja griežtumo visoje darbo aplinkoje

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.