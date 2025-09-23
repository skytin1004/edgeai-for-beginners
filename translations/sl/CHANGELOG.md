<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-23T00:45:56+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sl"
}
-->
# Dnevnik sprememb

Vse pomembne spremembe v EdgeAI za začetnike so dokumentirane tukaj. Ta projekt uporablja zapise na podlagi datumov in slog Keep a Changelog (Dodano, Spremenjeno, Popravljeno, Odstranjeno, Dokumentacija, Premaknjeno).

## 2025-09-18

### Dodano
- Modul 08: Microsoft Foundry Local – Celovit razvojni komplet
  - Šest sej: nastavitev, integracija Azure AI Foundry, odprtokodni modeli, najnovejše demonstracije, agenti in modeli kot orodja
  - Zagonljivi primeri pod `Module08/samples/01`–`06` z navodili za Windows cmd
    - `01` REST hitri klepet (`chat_quickstart.py`)
    - `02` SDK hitri začetek z OpenAI/Foundry Local in podporo Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI seznam in testiranje (`list_and_bench.cmd`)
    - `04` Chainlit demonstracija (`app.py`)
    - `05` Orkestracija več agentov (`python -m samples.05.agents.coordinator`)
    - `06` Usmerjevalnik modelov kot orodij (`router.py`)
- Podpora Azure OpenAI v vzorcu SDK za sejo 2 z nastavitvijo okoljske spremenljivke
- `.vscode/settings.json` za usmerjanje na `Module08/.venv` in izboljšanje analize Python kode
- `.env` z namigom `PYTHONPATH` za zavedanje VS Code/Pylance

### Spremenjeno
- Privzeti model posodobljen na `phi-4-mini` v dokumentaciji in vzorcih Modula 08; odstranjene preostale omembe `phi-3.5` znotraj Modula 08
- Izboljšave usmerjevalnika (`Module08/samples/06/router.py`):
  - Odkrivanje končnih točk prek `foundry service status` z regex analizo
  - Preverjanje zdravja `/v1/models` ob zagonu
  - Registracija modelov, nastavljiva prek okolja (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Posodobljene zahteve: `Module08/requirements.txt` zdaj vključuje `openai` (poleg `requests`, `chainlit`)
- Pojasnjena navodila za vzorec Chainlit in dodana odprava težav; rešitev uvoza prek nastavitev delovnega prostora

### Popravljeno
- Rešene težave z uvozi:
  - Usmerjevalnik ne temelji več na neobstoječem modulu `utils`; funkcije so vključene
  - Koordinator uporablja relativni uvoz (`from .specialists import ...`) in se zažene prek poti modula
  - Konfiguracija VS Code/Pylance za rešitev uvozov `chainlit` in paketov
- Popravljena manjša tipkarska napaka v `STUDY_GUIDE.md` in dodana pokritost Modula 08

### Odstranjeno
- Izbrisano neuporabljeno `Module08/infra/obs.py` in odstranjena prazna mapa `infra/`; vzorci opazovanja ohranjeni kot opcijski v dokumentaciji

### Premaknjeno
- Konsolidirane demonstracije Modula 08 pod `Module08/samples` z mapami, oštevilčenimi po sejah
  - Chainlit aplikacija premaknjena v `samples/04`
  - Agenti premaknjeni v `samples/05` in dodane datoteke `__init__.py` za rešitev paketov

### Dokumentacija
- Dokumentacija sej Modula 08 in vsi vzorčni README-ji obogateni z referencami Microsoft Learn in zaupanja vrednih ponudnikov
- `Module08/README.md` posodobljen s Pregledom vzorcev, konfiguracijo usmerjevalnika in nasveti za validacijo
- `Module07/README.md` odsek Windows Foundry Local potrjen glede na dokumentacijo Learn
- `STUDY_GUIDE.md` posodobljen:
  - Dodan Modul 08 v pregled, urnike, sledilnik napredka
  - Dodan obsežen odsek Referenc (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Zgodovinsko (povzetek)
- Ustanovljena arhitektura tečaja in moduli (Moduli 01–07)
- Iterativna modernizacija vsebine, standardizacija formatiranja in dodane študije primerov
- Razširjena pokritost optimizacijskih okvirov (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Neobjavljeno / Načrt (predlogi)
- Opcijski testi za preverjanje razpoložljivosti Foundry Local za posamezne vzorce
- Pregled prevodov za uskladitev referenc modelov (npr. `phi-4-mini`) kjer je primerno
- Dodaj minimalno konfiguracijo pyright, če ekipe preferirajo strogo nastavitev na ravni delovnega prostora

---

