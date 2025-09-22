<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T20:19:01+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "fi"
}
-->
# Muutosloki

Kaikki merkittävät muutokset EdgeAI for Beginners -projektiin dokumentoidaan täällä. Tämä projekti käyttää päivämääräperusteisia merkintöjä ja Keep a Changelog -tyyliä (Lisätty, Muutettu, Korjattu, Poistettu, Dokumentaatio, Siirretty).

## 2025-09-18

### Lisätty
- Moduuli 08: Microsoft Foundry Local – Täydellinen kehittäjätyökalupaketti
  - Kuusi istuntoa: asennus, Azure AI Foundry -integraatio, avoimen lähdekoodin mallit, huipputason demot, agentit ja mallit työkaluna
  - Suoritettavat esimerkit `Module08/samples/01`–`06` -kansiossa Windows cmd-ohjeilla
    - `01` REST-pikakeskustelu (`chat_quickstart.py`)
    - `02` SDK-pikakäynnistys OpenAI/Foundry Local- ja Azure OpenAI -tuella (`sdk_quickstart.py`)
    - `03` CLI listaus ja vertailu (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Moniagenttien orkestrointi (`python -m samples.05.agents.coordinator`)
    - `06` Mallit työkaluna -reititin (`router.py`)
- Azure OpenAI -tuki SDK-esimerkissä istunnossa 2 ympäristömuuttujien konfiguroinnilla
- `.vscode/settings.json` osoittamaan `Module08/.venv`-kansioon Python-analyysin parantamiseksi
- `.env` tiedosto, jossa `PYTHONPATH`-vihje VS Code/Pylance-tunnistusta varten

### Muutettu
- Oletusmalli päivitetty `phi-4-mini`:ksi Moduuli 08:n dokumenteissa ja esimerkeissä; jäljellä olevat `phi-3.5`-maininnat poistettu Moduuli 08:ssa
- Reitittimen (`Module08/samples/06/router.py`) parannukset:
  - Päätepisteiden haku `foundry service status` -komennolla regex-parsinnalla
  - `/v1/models`-terveystarkistus käynnistyksen yhteydessä
  - Ympäristökonfiguroitava mallirekisteri (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Vaatimukset päivitetty: `Module08/requirements.txt` sisältää nyt `openai` (yhdessä `requests` ja `chainlit` kanssa)
- Chainlit-esimerkin ohjeistus selkeytetty ja vianetsintä lisätty; tuontien ratkaisu työtilan asetuksilla

### Korjattu
- Tuontiongelmat ratkaistu:
  - Reititin ei enää riipu olemattomasta `utils`-moduulista; funktiot sisällytetty suoraan
  - Koordinaattori käyttää suhteellista tuontia (`from .specialists import ...`) ja käynnistetään moduulipolun kautta
  - VS Code/Pylance-konfiguraatio ratkaisee `chainlit`- ja pakettituonnit
- Pieni kirjoitusvirhe korjattu `STUDY_GUIDE.md`-tiedostossa ja lisätty Moduuli 08:n kattavuus

### Poistettu
- Poistettu käyttämätön `Module08/infra/obs.py` ja tyhjä `infra/`-hakemisto; havainnointimallit säilytetty valinnaisina dokumentaatiossa

### Siirretty
- Moduuli 08:n demot koottu `Module08/samples`-kansioon istuntojen numeroiduilla alikansioilla
  - Chainlit-sovellus siirretty `samples/04`-kansioon
  - Agentit siirretty `samples/05`-kansioon ja lisätty `__init__.py`-tiedostot pakettien tunnistusta varten

### Dokumentaatio
- Moduuli 08:n istuntodokumentaatio ja kaikki esimerkkien README-tiedostot rikastettu Microsoft Learn- ja luotettavien toimittajien viitteillä
- `Module08/README.md` päivitetty sisältämään Esimerkkien yleiskatsaus, reitittimen konfigurointi ja validointivinkit
- `Module07/README.md` Windows Foundry Local -osio validoitu Learn-dokumentaation perusteella
- `STUDY_GUIDE.md` päivitetty:
  - Lisätty Moduuli 08 yleiskatsaukseen, aikatauluihin ja etenemisen seurantaan
  - Lisätty kattava Viitteet-osio (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historiallinen (yhteenveto)
- Kurssin rakenne ja moduulit luotu (Moduulit 01–07)
- Sisällön iteratiivinen modernisointi, muotoilun standardointi ja lisäcase-tutkimukset
- Laajennettu optimointikehysten kattavuus (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Julkaisematon / Taustalla (ehdotukset)
- Valinnaiset per-esimerkki savutestit Foundry Local -saatavuuden validointiin
- Käännösten tarkistus malliviittausten yhdenmukaistamiseksi (esim. `phi-4-mini`)
- Lisää minimaalinen pyright-konfiguraatio, jos tiimit suosivat työtilan laajuista tiukkuutta

---

