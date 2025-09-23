<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-23T00:46:32+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "lt"
}
-->
# Pakeitimų žurnalas

Visi svarbūs EdgeAI for Beginners pakeitimai dokumentuojami čia. Šis projektas naudoja įrašus pagal datas ir Keep a Changelog stilių (Pridėta, Pakeista, Ištaisyta, Pašalinta, Dokumentacija, Perkelta).

## 2025-09-18

### Pridėta
- Modulis 08: Microsoft Foundry Local – Pilnas kūrėjų įrankių rinkinys
  - Šešios sesijos: nustatymas, Azure AI Foundry integracija, atvirojo kodo modeliai, pažangūs demonstraciniai pavyzdžiai, agentai ir modeliai kaip įrankiai
  - Veikiantys pavyzdžiai aplanke `Module08/samples/01`–`06` su Windows cmd instrukcijomis
    - `01` REST greitas pokalbis (`chat_quickstart.py`)
    - `02` SDK greitas startas su OpenAI/Foundry Local ir Azure OpenAI palaikymu (`sdk_quickstart.py`)
    - `03` CLI sąrašas ir testavimas (`list_and_bench.cmd`)
    - `04` Chainlit demonstracija (`app.py`)
    - `05` Daugiagentė koordinacija (`python -m samples.05.agents.coordinator`)
    - `06` Modeliai kaip įrankiai maršrutizatorius (`router.py`)
- Azure OpenAI palaikymas 2 sesijos SDK pavyzdyje su aplinkos kintamųjų konfigūracija
- `.vscode/settings.json`, nukreipiantis į `Module08/.venv`, kad pagerintų Python analizės sprendimą
- `.env` su `PYTHONPATH` užuomina VS Code/Pylance supratimui

### Pakeista
- Numatytasis modelis atnaujintas į `phi-4-mini` visoje 08 modulio dokumentacijoje ir pavyzdžiuose; pašalintos likusios `phi-3.5` nuorodos 08 modulyje
- Maršrutizatoriaus (`Module08/samples/06/router.py`) patobulinimai:
  - Galinių taškų aptikimas per `foundry service status` su regex analize
  - `/v1/models` sveikatos patikrinimas paleidimo metu
  - Aplinkos konfigūruojamas modelių registras (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Reikalavimai atnaujinti: `Module08/requirements.txt` dabar apima `openai` (kartu su `requests`, `chainlit`)
- Chainlit pavyzdžių instrukcijos patikslintos ir pridėta trikčių šalinimo informacija; importų sprendimas per darbo aplinkos nustatymus

### Ištaisyta
- Išspręstos importavimo problemos:
  - Maršrutizatorius nebepasitiki neegzistuojančiu `utils` moduliu; funkcijos integruotos
  - Koordinatorius naudoja santykinį importą (`from .specialists import ...`) ir paleidžiamas per modulio kelią
  - VS Code/Pylance konfigūracija, kad išspręstų `chainlit` ir paketų importus
- Ištaisyta nedidelė klaida `STUDY_GUIDE.md` ir pridėta 08 modulio aprėptis

### Pašalinta
- Pašalintas nenaudojamas `Module08/infra/obs.py` ir ištrintas tuščias `infra/` katalogas; stebėjimo šablonai išlaikyti kaip pasirenkami dokumentacijoje

### Perkelta
- 08 modulio demonstracijos sujungtos į `Module08/samples` su sesijos numeriais pažymėtais aplankais
  - Chainlit programa perkelta į `samples/04`
  - Agentai perkelti į `samples/05` ir pridėti `__init__.py` failai paketų sprendimui

### Dokumentacija
- 08 modulio sesijų dokumentacija ir visi pavyzdžių README papildyti Microsoft Learn ir patikimų tiekėjų nuorodomis
- `Module08/README.md` atnaujintas su pavyzdžių apžvalga, maršrutizatoriaus konfigūracija ir patikrinimo patarimais
- `Module07/README.md` Windows Foundry Local skyrius patikrintas pagal Learn dokumentaciją
- `STUDY_GUIDE.md` atnaujintas:
  - Pridėtas 08 modulis į apžvalgą, tvarkaraščius, progreso sekimo įrankį
  - Pridėta išsami Nuorodų sekcija (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Istorinė (santrauka)
- Kurso architektūra ir moduliai sukurti (Moduliai 01–07)
- Iteratyvus turinio modernizavimas, formatavimo standartizavimas ir pridėtos atvejų analizės
- Išplėsta optimizavimo sistemų aprėptis (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Neišleista / Laukiama (pasiūlymai)
- Pasirenkami kiekvieno pavyzdžio greiti testai, kad patikrintų Foundry Local prieinamumą
- Peržiūrėti vertimus, kad modelių nuorodos (pvz., `phi-4-mini`) būtų suderintos, kur tinkama
- Pridėti minimalų pyright konfigūracijos failą, jei komandos pageidauja griežtumo visoje darbo aplinkoje

---

