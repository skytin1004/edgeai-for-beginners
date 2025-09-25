<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T02:07:12+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sl"
}
-->
# Dnevnik sprememb

Vse pomembne spremembe v EdgeAI za začetnike so dokumentirane tukaj. Ta projekt uporablja zapise na podlagi datumov in slog Keep a Changelog (Dodano, Spremenjeno, Popravljeno, Odstranjeno, Dokumentacija, Premaknjeno).

## 2025-09-23

### Spremenjeno - Glavna posodobitev modula 08
- **Celovita uskladitev z vzorci repozitorija Microsoft Foundry-Local**
  - Posodobljeni vsi primeri kode za uporabo sodobnega `FoundryLocalManager` in integracije OpenAI SDK
  - Zamenjava zastarelih ročnih klicev `requests` z ustrezno uporabo SDK
  - Uskladitev vzorcev implementacije z uradno Microsoftovo dokumentacijo in vzorci

- **Posodobitev 05.AIPoweredAgents.md**:
  - Posodobljena orkestracija več agentov za uporabo sodobnih vzorcev SDK
  - Izboljšana implementacija koordinatorja z naprednimi funkcijami (povratne zanke, spremljanje zmogljivosti)
  - Dodano celovito obravnavanje napak in preverjanje zdravja storitev
  - Integrirane ustrezne reference na lokalne vzorce (`samples/05/multi_agent_orchestration.ipynb`)
  - Posodobljeni primeri klicanja funkcij za uporabo sodobnega parametra `tools` namesto zastarelega `functions`
  - Dodani vzorci, pripravljeni za produkcijo, z nadzorom in spremljanjem statistike

- **Popolna prenova 06.ModelsAsTools.md**:
  - Zamenjava osnovnega registra orodij z inteligentno implementacijo usmerjevalnika modelov
  - Dodana izbira modelov na podlagi ključnih besed za različne vrste nalog (splošno, razmišljanje, koda, ustvarjalno)
  - Integrirana konfiguracija na podlagi okolja z fleksibilno dodelitvijo modelov
  - Izboljšano z obsežnim spremljanjem zdravja storitev in obravnavanjem napak
  - Dodani vzorci za produkcijsko uporabo z nadzorom zahtevkov in spremljanjem zmogljivosti
  - Usklajeno z lokalno implementacijo v `samples/06/router.py` in `samples/06/model_router.ipynb`

- **Izboljšave strukture dokumentacije**:
  - Dodani pregledni odseki, ki poudarjajo posodobitve in uskladitev z SDK
  - Izboljšano z emojiji in boljšo oblikovanostjo za boljšo berljivost
  - Dodane ustrezne reference na lokalne vzorce datotek po celotni dokumentaciji
  - Vključena navodila za implementacijo, pripravljena za produkcijo, in najboljše prakse

### Dodano
- Celoviti pregledni odseki v datotekah modula 08, ki poudarjajo sodobno integracijo SDK
- Poudarki arhitekture, ki prikazujejo napredne funkcije (sistemi več agentov, inteligentno usmerjanje)
- Neposredne reference na lokalne vzorce za praktično izkušnjo
- Navodila za produkcijsko uporabo z vzorci za spremljanje in obravnavanje napak
- Interaktivni primeri Jupyter notebook z naprednimi funkcijami in merili uspešnosti

### Popravljeno
- Neskladja med dokumentacijo in dejanskimi implementacijami vzorcev
- Zastareli vzorci uporabe SDK po celotnem modulu 08
- Manjkajoče reference na obsežno lokalno knjižnico vzorcev
- Nekonsistentni pristopi implementacije v različnih odsekih

---

## 2025-09-18

### Dodano
- Modul 08: Microsoft Foundry Local – Celovit razvojni komplet
  - Šest sej: nastavitev, integracija Azure AI Foundry, odprtokodni modeli, najnovejši demoji, agenti in modeli kot orodja
  - Zagonljivi vzorci pod `Module08/samples/01`–`06` z navodili za Windows cmd
    - `01` REST hitri klepet (`chat_quickstart.py`)
    - `02` SDK hitri začetek z OpenAI/Foundry Local in podporo Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI seznam in primerjava (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Orkestracija več agentov (`python -m samples.05.agents.coordinator`)
    - `06` Usmerjevalnik modelov kot orodij (`router.py`)
- Podpora Azure OpenAI v vzorcu SDK za sejo 2 z nastavitvijo spremenljivk okolja
- `.vscode/settings.json` za usmerjanje na `Module08/.venv` in izboljšanje analize Python kode
- `.env` z namigom `PYTHONPATH` za prepoznavnost v VS Code/Pylance

### Spremenjeno
- Privzeti model posodobljen na `phi-4-mini` v celotni dokumentaciji in vzorcih modula 08; odstranjene preostale omembe `phi-3.5` znotraj modula 08
- Izboljšave usmerjevalnika (`Module08/samples/06/router.py`):
  - Odkrivanje končnih točk prek `foundry service status` z razčlenjevanjem regex
  - Preverjanje zdravja `/v1/models` ob zagonu
  - Konfigurabilni register modelov prek okolja (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Posodobljene zahteve: `Module08/requirements.txt` zdaj vključuje `openai` (poleg `requests`, `chainlit`)
- Pojasnjena navodila za vzorec Chainlit in dodano odpravljanje težav; rešitev uvoza prek nastavitev delovnega prostora

### Popravljeno
- Rešene težave z uvozi:
  - Usmerjevalnik ne temelji več na neobstoječem modulu `utils`; funkcije so vključene
  - Koordinator uporablja relativni uvoz (`from .specialists import ...`) in se zažene prek poti modula
  - Konfiguracija VS Code/Pylance za rešitev uvozov `chainlit` in paketov
- Popravljena manjša tipkarska napaka v `STUDY_GUIDE.md` in dodana pokritost modula 08

### Odstranjeno
- Izbrisana neuporabljena datoteka `Module08/infra/obs.py` in odstranjena prazna mapa `infra/`; vzorci opazovanja ohranjeni kot opcijski v dokumentaciji

### Premaknjeno
- Konsolidirani demoji modula 08 pod `Module08/samples` z mapami, oštevilčenimi po sejah
  - Premaknjen Chainlit app v `samples/04`
  - Premaknjeni agenti v `samples/05` in dodane datoteke `__init__.py` za rešitev paketov

### Dokumentacija
- Dokumentacija sej modula 08 in vsi vzorčni README-ji obogateni z referencami Microsoft Learn in zaupanja vrednih ponudnikov
- Posodobljen `Module08/README.md` s pregledom vzorcev, konfiguracijo usmerjevalnika in nasveti za validacijo
- Validiran odsek Windows Foundry Local v `Module07/README.md` glede na dokumentacijo Learn
- Posodobljen `STUDY_GUIDE.md`:
  - Dodan modul 08 v pregled, urnike, sledilnik napredka
  - Dodan obsežen odsek Referenc (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Zgodovinsko (povzetek)
- Ustanovljena arhitektura tečaja in moduli (Moduli 01–07)
- Iterativna posodobitev vsebine, standardizacija oblikovanja in dodane študije primerov
- Razširjena pokritost optimizacijskih okvirov (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Neobjavljeno / Načrtovano (predlogi)
- Opcijski testi za preverjanje razpoložljivosti Foundry Local za vsak vzorec
- Pregled prevodov za uskladitev referenc modelov (npr. `phi-4-mini`) kjer je primerno
- Dodajanje minimalne konfiguracije pyright, če ekipe želijo strožjo nastavitev na ravni delovnega prostora

---

