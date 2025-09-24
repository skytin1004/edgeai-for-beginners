<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T23:23:51+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "fi"
}
-->
# Muutosloki

Kaikki merkittävät muutokset EdgeAI for Beginners -projektiin dokumentoidaan täällä. Tämä projekti käyttää päivämääräperusteisia merkintöjä ja Keep a Changelog -tyyliä (Lisätty, Muutettu, Korjattu, Poistettu, Dokumentaatio, Siirretty).

## 2025-09-23

### Muutettu - Modulaarinen modernisointi: Moduuli 08
- **Laaja yhdenmukaistaminen Microsoft Foundry-Local -repositoryn mallien kanssa**
  - Päivitetty kaikki koodiesimerkit käyttämään modernia `FoundryLocalManager`-integraatiota ja OpenAI SDK:ta
  - Korvattu vanhentuneet manuaaliset `requests`-kutsut asianmukaisella SDK:n käytöllä
  - Yhdenmukaistettu toteutusmallit Microsoftin virallisen dokumentaation ja esimerkkien kanssa

- **05.AIPoweredAgents.md modernisointi**:
  - Päivitetty monen agentin orkestrointi käyttämään moderneja SDK-malleja
  - Parannettu koordinaattorin toteutusta edistyneillä ominaisuuksilla (palautesilmukat, suorituskyvyn seuranta)
  - Lisätty kattava virheenkäsittely ja palvelun terveystarkistus
  - Integroitu asianmukaiset viittaukset paikallisiin esimerkkeihin (`samples/05/multi_agent_orchestration.ipynb`)
  - Päivitetty funktiokutsuesimerkit käyttämään modernia `tools`-parametria vanhentuneen `functions`-parametrin sijaan
  - Lisätty tuotantovalmiita malleja, joissa on seuranta ja tilastojen kerääminen

- **06.ModelsAsTools.md täydellinen uudelleenkirjoitus**:
  - Korvattu yksinkertainen työkalurekisteri älykkäällä mallireitittimen toteutuksella
  - Lisätty avainsanapohjainen mallivalinta eri tehtävätyypeille (yleinen, päättely, koodi, luova)
  - Integroitu ympäristöpohjainen konfiguraatio joustavalla mallin määrityksellä
  - Parannettu kattavalla palvelun terveystarkistuksella ja virheenkäsittelyllä
  - Lisätty tuotantokäyttöön soveltuvia malleja, joissa on pyyntöjen seuranta ja suorituskyvyn tarkkailu
  - Yhdenmukaistettu paikallisen toteutuksen kanssa `samples/06/router.py` ja `samples/06/model_router.ipynb`

- **Dokumentaation rakenteen parannukset**:
  - Lisätty yleiskatsausosioita, jotka korostavat modernisointia ja SDK-yhdenmukaistamista
  - Parannettu emojeilla ja paremmalla muotoilulla luettavuuden parantamiseksi
  - Lisätty asianmukaiset viittaukset paikallisiin esimerkkitiedostoihin dokumentaation läpi
  - Sisällytetty tuotantovalmiiden toteutusten ohjeet ja parhaat käytännöt

### Lisätty
- Kattavat yleiskatsausosiot Moduuli 08 -tiedostoihin, jotka korostavat modernia SDK-integraatiota
- Arkkitehtuurin kohokohdat, jotka esittelevät edistyneitä ominaisuuksia (monen agentin järjestelmät, älykäs reititys)
- Suorat viittaukset paikallisiin esimerkkitoteutuksiin käytännön kokemuksen saamiseksi
- Tuotantokäyttöön liittyvät ohjeet, joissa on seuranta ja virheenkäsittelymallit
- Interaktiiviset Jupyter-notebook-esimerkit, joissa on edistyneitä ominaisuuksia ja vertailutuloksia

### Korjattu
- Yhdenmukaisuuserot dokumentaation ja todellisten esimerkkitoteutusten välillä
- Vanhentuneet SDK:n käyttömallit Moduuli 08:ssa
- Puuttuvat viittaukset kattavaan paikalliseen esimerkkikirjastoon
- Epäjohdonmukaiset toteutustavat eri osioiden välillä

---

## 2025-09-18

### Lisätty
- Moduuli 08: Microsoft Foundry Local – Täydellinen kehittäjätyökalupakki
  - Kuusi istuntoa: asennus, Azure AI Foundry -integraatio, avoimen lähdekoodin mallit, huipputason demot, agentit ja mallit työkaluna
  - Suoritettavat esimerkit `Module08/samples/01`–`06`-hakemistoissa Windows cmd-ohjeilla
    - `01` REST-pikakeskustelu (`chat_quickstart.py`)
    - `02` SDK-pikakäynnistys OpenAI/Foundry Local- ja Azure OpenAI -tuella (`sdk_quickstart.py`)
    - `03` CLI-listaus ja vertailu (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Monen agentin orkestrointi (`python -m samples.05.agents.coordinator`)
    - `06` Mallit työkaluna -reititin (`router.py`)
- Azure OpenAI -tuki istunnon 2 SDK-esimerkissä ympäristömuuttujakonfiguraatiolla
- `.vscode/settings.json` osoittamaan `Module08/.venv`-hakemistoon Python-analyysin parantamiseksi
- `.env` tiedosto, jossa `PYTHONPATH`-vihje VS Code/Pylance-tietoisuutta varten

### Muutettu
- Oletusmalli päivitetty `phi-4-mini`:ksi Moduuli 08 -dokumentaatiossa ja esimerkeissä; poistettu jäljellä olevat `phi-3.5`-maininnat Moduuli 08:ssa
- Reititin (`Module08/samples/06/router.py`) parannukset:
  - Päätepisteiden haku `foundry service status`-komennolla regex-parsinnalla
  - `/v1/models`-terveystarkistus käynnistyksen yhteydessä
  - Ympäristökonfiguroitava mallirekisteri (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Vaatimukset päivitetty: `Module08/requirements.txt` sisältää nyt `openai` (yhdessä `requests`- ja `chainlit`-kirjastojen kanssa)
- Chainlit-esimerkin ohjeistus selkeytetty ja vianetsintä lisätty; tuontiresoluutio työtilan asetusten kautta

### Korjattu
- Ratkaistu tuontiongelmat:
  - Reititin ei enää riipu olemattomasta `utils`-moduulista; funktiot on sisällytetty
  - Koordinaattori käyttää suhteellista tuontia (`from .specialists import ...`) ja käynnistetään moduulipolun kautta
  - VS Code/Pylance-konfiguraatio ratkaisemaan `chainlit`- ja pakettituonnit
- Korjattu pieni kirjoitusvirhe `STUDY_GUIDE.md`-tiedostossa ja lisätty Moduuli 08:n kattavuus

### Poistettu
- Poistettu käyttämätön `Module08/infra/obs.py` ja tyhjä `infra/`-hakemisto; havainnointimallit säilytetty valinnaisina dokumentaatiossa

### Siirretty
- Konsolidoitu Moduuli 08 -demot `Module08/samples`-hakemistoon istuntojen numeroiduilla kansioilla
  - Siirretty Chainlit-sovellus `samples/04`-hakemistoon
  - Siirretty agentit `samples/05`-hakemistoon ja lisätty `__init__.py`-tiedostot pakettiratkaisua varten

### Dokumentaatio
- Moduuli 08:n istuntodokumentaatio ja kaikki esimerkkien README-tiedostot rikastettu Microsoft Learn- ja luotettavien toimittajien viittauksilla
- `Module08/README.md` päivitetty sisältämään Esimerkkien yleiskatsaus, reitittimen konfiguraatio ja validointivinkit
- `Module07/README.md` Windows Foundry Local -osio validoitu Learn-dokumentaation kanssa
- `STUDY_GUIDE.md` päivitetty:
  - Lisätty Moduuli 08 yleiskatsaukseen, aikatauluihin, edistymisen seurantaan
  - Lisätty kattava Viittaukset-osio (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historiallinen (yhteenveto)
- Kurssin arkkitehtuuri ja moduulit perustettu (Moduulit 01–07)
- Iteratiivinen sisällön modernisointi, muotoilun standardointi ja lisätyt tapaustutkimukset
- Laajennettu optimointikehysten kattavuus (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Julkaisematon / Backlog (ehdotukset)
- Valinnaiset per-esimerkki savutestit Foundry Local -saatavuuden validointiin
- Tarkista käännökset yhdenmukaistamaan malliviittaukset (esim. `phi-4-mini`) tarvittaessa
- Lisää minimaalinen pyright-konfiguraatio, jos tiimit suosivat työtilan laajuista tiukkuutta

---

