<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-09T14:15:13+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "fi"
}
-->
# Muutosloki

Kaikki merkittävät muutokset EdgeAI for Beginners -projektiin dokumentoidaan täällä. Tämä projekti käyttää päivämääräperusteisia merkintöjä ja Keep a Changelog -tyyliä (Lisätty, Muutettu, Korjattu, Poistettu, Dokumentaatio, Siirretty).

## 2025-10-08

### Lisätty - Työpajan kattava päivitys
- **Työpajan README.md kokonaisuudistus**:
  - Lisätty kattava johdanto, joka selittää Edge AI:n arvon (yksityisyys, suorituskyky, kustannukset)
  - Luotu 6 keskeistä oppimistavoitetta yksityiskohtaisilla osaamisalueilla
  - Lisätty oppimistulostaulukko, jossa on toimitettavat materiaalit ja osaamismatriisi
  - Sisällytetty työelämätaitoja korostava osio alan merkityksen vuoksi
  - Lisätty pikaopas, jossa on ennakkovaatimukset ja 3-vaiheinen asennusohje
  - Luotu resurssitaulukot Python-esimerkeille (8 tiedostoa ja niiden suoritusajat)
  - Lisätty Jupyter-notebookien taulukko (8 notebookia vaikeusasteineen)
  - Luotu dokumentaatiotaulukko (7 keskeistä dokumenttia ja "Käytä kun" -ohjeet)
  - Lisätty oppimispolun suosituksia eri taitotasoille

- **Työpajan validointi- ja testausinfrastruktuuri**:
  - Luotu `scripts/validate_samples.py` - Kattava validointityökalu syntaksille, tuonneille ja parhaiden käytäntöjen noudattamiselle
  - Luotu `scripts/test_samples.py` - Savutestien suorittaja kaikille Python-esimerkeille
  - Lisätty validointidokumentaatio tiedostoon `scripts/README.md`

- **Kattava dokumentaatio**:
  - Luotu `SAMPLES_UPDATE_SUMMARY.md` - Yli 400 rivin yksityiskohtainen opas, joka kattaa kaikki parannukset
  - Luotu `UPDATE_COMPLETE.md` - Päivityksen valmistumisen tiivistelmä
  - Luotu `QUICK_REFERENCE.md` - Pikaopas työpajalle

### Muutettu - Työpajan Python-esimerkkien modernisointi
- **Kaikki 8 Python-esimerkkiä päivitetty parhaiden käytäntöjen mukaisiksi**:
  - Parannettu virheenkäsittely try-except-lohkoilla kaikissa I/O-toiminnoissa
  - Lisätty tyyppivihjeet ja kattavat docstringit
  - Toteutettu yhtenäinen [INFO]/[ERROR]/[RESULT] -lokitusmalli
  - Suojattu valinnaiset tuonnit asennusvinkeillä
  - Parannettu käyttäjäpalautetta kaikissa esimerkeissä

- **session01/chat_bootstrap.py**:
  - Parannettu asiakasohjelman alustusta kattavilla virheilmoituksilla
  - Parannettu suoratoiston virheenkäsittely chunk-tarkistuksilla
  - Lisätty parempi poikkeusten käsittely palvelun saatavuusongelmissa

- **session02/rag_pipeline.py**:
  - Lisätty tuontisuojat sentence-transformersille asennusvinkeillä
  - Parannettu virheenkäsittely upotus- ja generointitoiminnoissa
  - Parannettu tulostusmuotoilu rakenteellisilla tuloksilla

- **session02/rag_eval_ragas.py**:
  - Suojattu valinnaiset tuonnit (ragas, datasets) käyttäjäystävällisillä virheilmoituksilla
  - Lisätty virheenkäsittely arviointimetrikoille
  - Parannettu tulostusmuotoilu arviointituloksille

- **session03/benchmark_oss_models.py**:
  - Toteutettu sulava heikentyminen (jatkaa mallivirheiden kohdalla)
  - Lisätty yksityiskohtainen etenemisen raportointi ja mallikohtainen virheenkäsittely
  - Parannettu tilastolaskentaa kattavalla virheenkorjauksella

- **session04/model_compare.py**:
  - Lisätty tyyppivihjeet (Tuple-palautustyypit)
  - Parannettu tulostusmuotoilu rakenteellisilla JSON-tuloksilla
  - Toteutettu mallikohtainen virheenkäsittely palautuksella

- **session05/agents_orchestrator.py**:
  - Parannettu Agent.act() kattavilla docstringeillä
  - Lisätty putkiston virheenkäsittely vaiheittaisella lokituksella
  - Parannettu muistinhallintaa ja tilan seurantaa

- **session06/models_router.py**:
  - Parannettu funktiodokumentaatio kaikille reitityskomponenteille
  - Lisätty yksityiskohtainen lokitus route()-funktioon
  - Parannettu testitulokset rakenteellisilla tuloksilla

- **session06/models_pipeline.py**:
  - Lisätty virheenkäsittely chat()-apuohjelmaan
  - Parannettu pipeline()-funktiota vaiheittaisella lokituksella ja etenemisen raportoinnilla
  - Parannettu main()-funktiota kattavalla virheenkorjauksella

### Dokumentaatio - Työpajan dokumentaation parannus
- Päivitetty pääasiallinen README.md korostamaan työpajan osuutta käytännön oppimispolussa
- Parannettu STUDY_GUIDE.md kattavalla työpajaosuudella, joka sisältää:
  - Oppimistavoitteet ja keskittymiskohteet
  - Itsearviointikysymykset
  - Käytännön harjoitukset aikatauluarvioineen
  - Ajan jakaminen intensiiviseen ja osa-aikaiseen opiskeluun
  - Lisätty työpaja edistymisen seurantamalliin
- Päivitetty ajan jakamisen ohje 20 tunnista 30 tuntiin (sisältäen työpajan)
- Lisätty työpajan esimerkkikuvaukset ja oppimistulokset README-tiedostoon

### Korjattu
- Ratkaistu epäjohdonmukaiset virheenkäsittelymallit työpajan esimerkeissä
- Korjattu valinnaisten riippuvuuksien tuontivirheet asianmukaisilla suojauksilla
- Korjattu puuttuvat tyyppivihjeet kriittisissä funktioissa
- Korjattu riittämätön käyttäjäpalaute virhetilanteissa
- Korjattu validointiongelmat kattavalla testausinfrastruktuurilla

---

## 2025-09-23

### Muutettu - Suuri moduuli 08 modernisointi
- **Kattava yhdenmukaistaminen Microsoft Foundry-Local -arkistomallien kanssa**:
  - Päivitetty kaikki koodiesimerkit käyttämään modernia `FoundryLocalManager`- ja OpenAI SDK -integraatiota
  - Korvattu vanhentuneet manuaaliset `requests`-kutsut asianmukaisella SDK-käytöllä
  - Yhdenmukaistettu toteutusmallit virallisen Microsoft-dokumentaation ja esimerkkien kanssa

- **05.AIPoweredAgents.md modernisointi**:
  - Päivitetty monen agentin orkestrointi käyttämään moderneja SDK-malleja
  - Parannettu koordinaattorin toteutusta edistyneillä ominaisuuksilla (palautesilmukat, suorituskyvyn seuranta)
  - Lisätty kattava virheenkäsittely ja palvelun terveystarkistus
  - Integroitu asianmukaiset viittaukset paikallisiin esimerkkeihin (`samples/05/multi_agent_orchestration.ipynb`)
  - Päivitetty funktiokutsuesimerkit käyttämään modernia `tools`-parametria vanhentuneen `functions`-parametrin sijaan
  - Lisätty tuotantovalmiit mallit seurannalla ja tilastojen seurannalla

- **06.ModelsAsTools.md kokonaisuudistus**:
  - Korvattu yksinkertainen työkalurekisteri älykkäällä mallireitittimen toteutuksella
  - Lisätty avainsanapohjainen mallivalinta eri tehtävätyypeille (yleinen, päättely, koodi, luova)
  - Integroitu ympäristöön perustuva konfiguraatio joustavalla mallin määrityksellä
  - Parannettu kattavalla palvelun terveystarkistuksella ja virheenkäsittelyllä
  - Lisätty tuotantovalmiit käyttöönoton mallit pyynnön seurannalla ja suorituskyvyn seurannalla
  - Yhdenmukaistettu paikallisen toteutuksen kanssa tiedostoissa `samples/06/router.py` ja `samples/06/model_router.ipynb`

- **Dokumentaation rakenteen parannukset**:
  - Lisätty yleiskatsausosioita, jotka korostavat modernisointia ja SDK-yhdenmukaistamista
  - Parannettu emojeilla ja paremmalla muotoilulla luettavuuden parantamiseksi
  - Lisätty asianmukaiset viittaukset paikallisiin esimerkkitiedostoihin dokumentaatiossa
  - Sisällytetty tuotantovalmiiden toteutusten ohjeet ja parhaat käytännöt

### Lisätty
- Kattavat yleiskatsausosiot moduuli 08 -tiedostoihin, jotka korostavat modernia SDK-integraatiota
- Arkkitehtuurin kohokohdat, jotka esittelevät edistyneitä ominaisuuksia (monen agentin järjestelmät, älykäs reititys)
- Suorat viittaukset paikallisiin esimerkkitoteutuksiin käytännön kokemuksen saamiseksi
- Tuotantovalmiiden käyttöönoton ohjeet seuranta- ja virheenkäsittelymalleilla
- Interaktiiviset Jupyter-notebook-esimerkit edistyneillä ominaisuuksilla ja vertailuilla

### Korjattu
- Yhdenmukaisuuserot dokumentaation ja todellisten esimerkkitoteutusten välillä
- Vanhentuneet SDK-käyttömallit moduuli 08:ssa
- Puuttuvat viittaukset kattavaan paikalliseen esimerkkikirjastoon
- Epäjohdonmukaiset toteutustavat eri osioiden välillä

---

## 2025-09-18

### Lisätty
- Moduuli 08: Microsoft Foundry Local – Täydellinen kehittäjätyökalupakki
  - Kuusi istuntoa: asennus, Azure AI Foundry -integraatio, avoimen lähdekoodin mallit, huipputason demot, agentit ja mallit työkaluna
  - Suoritettavat esimerkit hakemistossa `Module08/samples/01`–`06` Windows cmd-ohjeilla
    - `01` REST-pikakeskustelu (`chat_quickstart.py`)
    - `02` SDK-pikakäynnistys OpenAI/Foundry Local- ja Azure OpenAI -tuella (`sdk_quickstart.py`)
    - `03` CLI-listaus ja vertailu (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Monen agentin orkestrointi (`python -m samples.05.agents.coordinator`)
    - `06` Mallit työkaluna -reititin (`router.py`)
- Azure OpenAI -tuki istunnon 2 SDK-esimerkissä ympäristömuuttujakonfiguraatiolla
- `.vscode/settings.json` osoittamaan `Module08/.venv`-hakemistoon Python-analyysin parantamiseksi
- `.env` `PYTHONPATH`-vihjeellä VS Code/Pylance-tietoisuuden lisäämiseksi

### Muutettu
- Oletusmalli päivitetty `phi-4-mini`:ksi moduuli 08:n dokumentaatiossa ja esimerkeissä; poistettu jäljellä olevat `phi-3.5`-maininnat moduuli 08:ssa
- Reititin (`Module08/samples/06/router.py`) parannukset:
  - Päätepisteiden haku `foundry service status` -komennolla regex-analyysillä
  - `/v1/models`-terveystarkistus käynnistyksessä
  - Ympäristökonfiguroitava mallirekisteri (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Vaatimukset päivitetty: `Module08/requirements.txt` sisältää nyt `openai` (yhdessä `requests`- ja `chainlit`-kirjastojen kanssa)
- Chainlit-esimerkin ohjeet selkeytetty ja vianetsintä lisätty; tuontiresoluutio työtilan asetuksilla

### Korjattu
- Ratkaistu tuontiongelmat:
  - Reititin ei enää riipu olemattomasta `utils`-moduulista; funktiot on sisällytetty
  - Koordinaattori käyttää suhteellista tuontia (`from .specialists import ...`) ja käynnistetään moduulipolun kautta
  - VS Code/Pylance-konfiguraatio ratkaisee `chainlit`- ja pakettituonnit
- Korjattu pieni kirjoitusvirhe tiedostossa `STUDY_GUIDE.md` ja lisätty moduuli 08:n kattavuus

### Poistettu
- Poistettu käyttämätön `Module08/infra/obs.py` ja tyhjä `infra/`-hakemisto; havainnointimallit säilytetty valinnaisina dokumentaatiossa

### Siirretty
- Konsolidoitu moduuli 08:n demot hakemistoon `Module08/samples` istuntojen numeroiduilla kansioilla
  - Siirretty Chainlit-sovellus hakemistoon `samples/04`
  - Siirretty agentit hakemistoon `samples/05` ja lisätty `__init__.py`-tiedostot pakettiratkaisua varten

### Dokumentaatio
- Moduuli 08:n istuntodokumentaatio ja kaikki esimerkkien README-tiedostot rikastettu Microsoft Learn- ja luotettavien toimittajien viittauksilla
- `Module08/README.md` päivitetty näyteyleiskatsauksella, reitittimen konfiguraatiolla ja validointivinkeillä
- `Module07/README.md` Windows Foundry Local -osio validoitu Learn-dokumentaation kanssa
- `STUDY_GUIDE.md` päivitetty:
  - Lisätty moduuli 08 yleiskatsaukseen, aikatauluihin, edistymisen seurantaan
  - Lisätty kattava viittausosio (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historiallinen (yhteenveto)
- Kurssin arkkitehtuuri ja moduulit perustettu (Moduulit 01–07)
- Iteratiivinen sisällön modernisointi, muotoilun standardointi ja lisäcase-tutkimukset
- Laajennettu optimointikehysten kattavuus (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Julkaisematon / Jono (ehdotukset)
- Valinnaiset savutestit per esimerkki Foundry Local -saatavuuden validointiin
- Tarkista käännökset malliviittausten yhdenmukaistamiseksi (esim. `phi-4-mini`) tarvittaessa
- Lisää minimaalinen pyright-konfiguraatio, jos tiimit suosivat työtilan laajuista tiukkuutta

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.