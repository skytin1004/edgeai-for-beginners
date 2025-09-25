<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T02:34:58+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "lt"
}
-->
# Pakeitimų žurnalas

Visi svarbūs pakeitimai, susiję su EdgeAI pradedantiesiems, yra dokumentuoti čia. Šis projektas naudoja įrašus pagal datas ir „Keep a Changelog“ stilių (Pridėta, Pakeista, Ištaisyta, Pašalinta, Dokumentacija, Perkelta).

## 2025-09-23

### Pakeista - Didelė 08 modulio modernizacija
- **Visapusiškas suderinimas su „Microsoft Foundry-Local“ saugyklos šablonais**
  - Atnaujinti visi kodo pavyzdžiai, kad būtų naudojamas modernus `FoundryLocalManager` ir OpenAI SDK integravimas
  - Pakeisti pasenę rankiniai `requests` skambučiai tinkamu SDK naudojimu
  - Suderinti įgyvendinimo šablonus su oficialia „Microsoft“ dokumentacija ir pavyzdžiais

- **05.AIPoweredAgents.md modernizacija**:
  - Atnaujinta daugiaveiksnių orkestracija, naudojant modernius SDK šablonus
  - Patobulinta koordinatoriaus įgyvendinimas su pažangiomis funkcijomis (grįžtamojo ryšio ciklai, našumo stebėjimas)
  - Pridėtas išsamus klaidų tvarkymas ir paslaugų sveikatos tikrinimas
  - Integruotos tinkamos nuorodos į vietinius pavyzdžius (`samples/05/multi_agent_orchestration.ipynb`)
  - Atnaujinti funkcijų skambučiai, naudojant modernų `tools` parametrą vietoj pasenusio `functions`
  - Pridėti gamybai paruošti šablonai su stebėjimu ir statistikos sekimu

- **06.ModelsAsTools.md visiškas perrašymas**:
  - Pakeista paprasta įrankių registracija į pažangią modelių maršrutizatoriaus įgyvendinimą
  - Pridėtas modelių pasirinkimas pagal raktinius žodžius skirtingoms užduotims (bendros, loginės, kodo, kūrybinės)
  - Integruota aplinkos pagrindu konfigūracija su lankstiu modelių priskyrimu
  - Patobulinta išsamiu paslaugų sveikatos stebėjimu ir klaidų tvarkymu
  - Pridėti gamybos diegimo šablonai su užklausų stebėjimu ir našumo sekimu
  - Suderinta su vietiniu įgyvendinimu `samples/06/router.py` ir `samples/06/model_router.ipynb`

- **Dokumentacijos struktūros patobulinimai**:
  - Pridėtos apžvalgos sekcijos, pabrėžiančios modernizaciją ir SDK suderinimą
  - Patobulinta su emocijomis ir geresniu formatavimu, siekiant pagerinti skaitomumą
  - Pridėtos tinkamos nuorodos į vietinius pavyzdžių failus visoje dokumentacijoje
  - Įtraukta gamybai paruošto įgyvendinimo gairės ir geriausios praktikos

### Pridėta
- Išsamios apžvalgos sekcijos 08 modulio failuose, pabrėžiančios modernų SDK integravimą
- Architektūros akcentai, pristatantys pažangias funkcijas (daugiaveiksnių sistemos, pažangus maršrutizavimas)
- Tiesioginės nuorodos į vietinius pavyzdžių įgyvendinimus praktiniam mokymuisi
- Gamybos diegimo gairės su stebėjimo ir klaidų tvarkymo šablonais
- Interaktyvūs Jupyter užrašų knygelės pavyzdžiai su pažangiomis funkcijomis ir našumo testais

### Ištaisyta
- Suderinimo neatitikimai tarp dokumentacijos ir faktinių pavyzdžių įgyvendinimų
- Pasenę SDK naudojimo šablonai visame 08 modulyje
- Trūkstamos nuorodos į išsamų vietinių pavyzdžių biblioteką
- Nenuoseklūs įgyvendinimo metodai skirtingose sekcijose

---

## 2025-09-18

### Pridėta
- Modulis 08: „Microsoft Foundry Local“ – Pilnas kūrėjų įrankių rinkinys
  - Šešios sesijos: nustatymas, Azure AI Foundry integracija, atvirojo kodo modeliai, pažangūs demonstraciniai pavyzdžiai, agentai ir modeliai kaip įrankiai
  - Paleidžiami pavyzdžiai `Module08/samples/01`–`06` su Windows cmd instrukcijomis
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
- Numatytasis modelis atnaujintas į `phi-4-mini` visame 08 modulio dokumentacijoje ir pavyzdžiuose; pašalinti likę `phi-3.5` paminėjimai 08 modulyje
- Maršrutizatoriaus (`Module08/samples/06/router.py`) patobulinimai:
  - Galinių taškų aptikimas per `foundry service status` su regex analizavimu
  - `/v1/models` sveikatos patikrinimas paleidimo metu
  - Aplinkos konfigūruojama modelių registracija (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Reikalavimai atnaujinti: `Module08/requirements.txt` dabar apima `openai` (kartu su `requests`, `chainlit`)
- Chainlit pavyzdžių gairės patikslintos ir pridėtas trikčių šalinimas; importo sprendimas per darbo aplinkos nustatymus

### Ištaisyta
- Išspręstos importo problemos:
  - Maršrutizatorius nebepriklauso nuo neegzistuojančio `utils` modulio; funkcijos yra integruotos
  - Koordinatorius naudoja santykinį importą (`from .specialists import ...`) ir paleidžiamas per modulio kelią
  - VS Code/Pylance konfigūracija, kad išspręstų `chainlit` ir paketų importus
- Ištaisyta nedidelė klaida `STUDY_GUIDE.md` ir pridėta 08 modulio aprėptis

### Pašalinta
- Ištrintas nenaudojamas `Module08/infra/obs.py` ir pašalintas tuščias `infra/` katalogas; stebėjimo šablonai išlaikyti kaip pasirenkami dokumentacijoje

### Perkelta
- Konsoliduoti 08 modulio demonstraciniai pavyzdžiai `Module08/samples` su sesijos numeriais pažymėtais katalogais
  - Chainlit programa perkelta į `samples/04`
  - Agentai perkelti į `samples/05` ir pridėti `__init__.py` failai paketų sprendimui

### Dokumentacija
- 08 modulio sesijos dokumentacija ir visi pavyzdžių README failai praturtinti „Microsoft Learn“ ir patikimų tiekėjų nuorodomis
- `Module08/README.md` atnaujintas su pavyzdžių apžvalga, maršrutizatoriaus konfigūracija ir patikrinimo patarimais
- `Module07/README.md` Windows Foundry Local sekcija patikrinta pagal Learn dokumentaciją
- `STUDY_GUIDE.md` atnaujintas:
  - Pridėtas 08 modulis į apžvalgą, tvarkaraščius, pažangos sekimo įrankį
  - Pridėta išsami nuorodų sekcija (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Istorinė (santrauka)
- Kurso architektūra ir moduliai sukurti (Moduliai 01–07)
- Iteratyvi turinio modernizacija, formatavimo standartizavimas ir pridėti atvejų tyrimai
- Išplėsta optimizavimo sistemų aprėptis (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Neišleista / Laukiama (pasiūlymai)
- Pasirenkami kiekvieno pavyzdžio testai, skirti patikrinti Foundry Local prieinamumą
- Peržiūrėti vertimus, kad suderintų modelių nuorodas (pvz., `phi-4-mini`) kur tinkama
- Pridėti minimalų pyright konfigūraciją, jei komandos pageidauja griežtumo visoje darbo aplinkoje

---

