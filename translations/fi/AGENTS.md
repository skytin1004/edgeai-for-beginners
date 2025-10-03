<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:37:40+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fi"
}
-->
# AGENTS.md

## Projektin yleiskatsaus

EdgeAI for Beginners on kattava opetusresurssi, joka opettaa Edge AI -kehitystä pienillä kielimalleilla (SLM). Kurssi kattaa EdgeAI:n perusteet, mallien käyttöönoton, optimointitekniikat ja tuotantovalmiit toteutukset Microsoft Foundry Localin ja eri AI-kehysten avulla.

**Keskeiset teknologiat:**
- Python 3.8+ (pääasiallinen kieli AI/ML-esimerkeille)
- .NET C# (AI/ML-esimerkit)
- JavaScript/Node.js Electronin kanssa (työpöytäsovelluksia varten)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-kehykset: LangChain, Semantic Kernel, Chainlit
- Mallien optimointi: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Resurssin tyyppi:** Opetussisältöä sisältävä arkisto, jossa on 8 moduulia ja 10 kattavaa esimerkkisovellusta

**Arkkitehtuuri:** Monimoduulinen oppimispolku, jossa käytännön esimerkit havainnollistavat Edge AI:n käyttöönoton malleja

## Resurssin rakenne

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Asennuskomennot

### Resurssin asennus

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python-esimerkkien asennus (Moduuli08 ja Python-esimerkit)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Node.js-esimerkin asennus (Esimerkki 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Localin asennus

Foundry Local vaaditaan Moduuli08:n esimerkkien suorittamiseen:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Kehitystyön kulku

### Sisällön kehitys

Tämä arkisto sisältää pääasiassa **Markdown-opetussisältöä**. Muutoksia tehdessä:

1. Muokkaa `.md`-tiedostoja oikeissa moduulikansioissa
2. Noudata olemassa olevia muotoilumalleja
3. Varmista, että koodiesimerkit ovat tarkkoja ja testattuja
4. Päivitä vastaava käännetty sisältö tarvittaessa (tai anna automaation hoitaa se)

### Esimerkkisovellusten kehitys

Python-esimerkeille (esimerkit 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Electron-esimerkille (esimerkki 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Esimerkkisovellusten testaus

Python-esimerkeillä ei ole automatisoituja testejä, mutta ne voidaan validoida suorittamalla:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron-esimerkissä on testausinfrastruktuuri:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testausohjeet

### Sisällön validointi

Arkisto käyttää automatisoituja käännösprosesseja. Käännösten manuaalista testausta ei vaadita.

**Manuaalinen validointi sisällön muutoksille:**
1. Esikatsele Markdown-tiedostojen renderöinti
2. Varmista, että kaikki linkit osoittavat oikeisiin kohteisiin
3. Testaa dokumentaatiossa olevat koodiesimerkit
4. Tarkista, että kuvat latautuvat oikein

### Esimerkkisovellusten testaus

**Moduuli08/esimerkit/08 (Electron-sovellus) sisältää kattavan testauksen:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python-esimerkit tulisi testata manuaalisesti:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Koodityyliohjeet

### Markdown-sisältö

- Käytä johdonmukaista otsikkohierarkiaa (# otsikko, ## pääosat, ### aliosat)
- Sisällytä koodilohkot kielimäärityksillä: ```python, ```bash, ```javascript
- Noudata olemassa olevia muotoilumalleja taulukoille, listoille ja korostuksille
- Pidä rivit luettavina (tavoite ~80-100 merkkiä, mutta ei tiukkaa rajaa)
- Käytä suhteellisia linkkejä sisäisiin viittauksiin

### Python-koodityyli

- Noudata PEP 8 -konventioita
- Käytä tyyppivihjeitä, kun se on tarkoituksenmukaista
- Sisällytä docstringit funktioille ja luokille
- Käytä merkityksellisiä muuttujanimiä
- Pidä funktiot keskittyneinä ja tiiviinä

### JavaScript/Node.js-koodityyli

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Keskeiset konventiot:**
- ESLint-konfiguraatio mukana esimerkissä 08
- Prettier koodin muotoiluun
- Käytä modernia ES6+ syntaksia
- Noudata olemassa olevia malleja koodikannassa

## Pull Request -ohjeet

### Otsikon muoto
```
[ModuleXX] Brief description of change
```
tai
```
[Module08/samples/XX] Description for sample changes
```

### Ennen lähettämistä

**Sisällön muutoksille:**
- Esikatsele kaikki muokatut Markdown-tiedostot
- Varmista, että linkit ja kuvat toimivat
- Tarkista kirjoitusvirheet ja kielioppivirheet

**Esimerkkikoodin muutoksille (Moduuli08/esimerkit/08):**
```bash
npm run lint
npm test
```

**Python-esimerkkien muutoksille:**
- Testaa, että esimerkki toimii onnistuneesti
- Varmista virheenkäsittelyn toimivuus
- Tarkista yhteensopivuus Foundry Localin kanssa

### Tarkistusprosessi

- Opetussisällön muutokset tarkistetaan tarkkuuden ja selkeyden osalta
- Koodiesimerkit testataan toimivuuden osalta
- Käännöspäivitykset hoidetaan automaattisesti GitHub Actionsin avulla

## Käännösjärjestelmä

**TÄRKEÄÄ:** Tämä arkisto käyttää automatisoitua käännöstä GitHub Actionsin kautta.

- Käännökset ovat `/translations/`-hakemistossa (yli 50 kieltä)
- Automatisoitu `co-op-translator.yml`-työnkulun avulla
- **ÄLÄ muokkaa käännöstiedostoja manuaalisesti** - ne korvataan automaattisesti
- Muokkaa vain englanninkielisiä lähdetiedostoja juurihakemistossa ja moduulikansioissa
- Käännökset luodaan automaattisesti, kun `main`-haaraan tehdään push

## Foundry Local -integraatio

Useimmat Moduuli08:n esimerkit vaativat Microsoft Foundry Localin käynnissä:

### Foundry Localin käynnistäminen
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Foundry Localin tarkistaminen
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Ympäristömuuttujat esimerkeille

Useimmat esimerkit käyttävät näitä ympäristömuuttujia:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Rakentaminen ja käyttöönotto

### Sisällön käyttöönotto

Tämä arkisto on pääasiassa dokumentaatiota - sisällölle ei vaadita rakennusprosessia.

### Esimerkkisovellusten rakentaminen

**Electron-sovellus (Moduuli08/esimerkit/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python-esimerkit:**
Ei rakennusprosessia - esimerkit suoritetaan suoraan Python-tulkilla.

## Yleiset ongelmat ja vianmääritys

### Foundry Local ei ole käynnissä
**Ongelma:** Esimerkit epäonnistuvat yhteysvirheiden vuoksi

**Ratkaisu:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Python-virtuaaliympäristön ongelmat
**Ongelma:** Moduulin tuontivirheet

**Ratkaisu:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron-rakennusongelmat
**Ongelma:** npm install- tai rakennusvirheet

**Ratkaisu:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Käännöstyönkulun ristiriidat
**Ongelma:** Käännös-PR on ristiriidassa muutostesi kanssa

**Ratkaisu:**
- Muokkaa vain englanninkielisiä lähdetiedostoja
- Anna automatisoidun käännöstyönkulun hoitaa käännökset
- Jos ristiriitoja ilmenee, yhdistä `main` haarasi jälkeen, kun käännökset on yhdistetty

## Lisäresurssit

### Oppimispolut
- **Aloittelijapolku:** Moduulit 01-02 (7-9 tuntia)
- **Keskitaso:** Moduulit 03-04 (9-11 tuntia)
- **Edistynyt polku:** Moduulit 05-07 (12-15 tuntia)
- **Asiantuntijapolku:** Moduuli 08 (8-10 tuntia)

### Keskeinen moduulisisältö
- **Moduuli01:** EdgeAI:n perusteet ja tosielämän tapaustutkimukset
- **Moduuli02:** Pienten kielimallien (SLM) perheet ja arkkitehtuurit
- **Moduuli03:** Paikalliset ja pilvikäyttöönoton strategiat
- **Moduuli04:** Mallien optimointi eri kehysten avulla
- **Moduuli05:** SLMOps - tuotantotoiminnot
- **Moduuli06:** AI-agentit ja funktioiden kutsuminen
- **Moduuli07:** Alustakohtaiset toteutukset
- **Moduuli08:** Foundry Local -työkalupakki ja 10 kattavaa esimerkkiä

### Ulkoiset riippuvuudet
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Paikallinen AI-mallien suoritusympäristö
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimointikehys
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Mallien optimointityökalu
- [OpenVINO](https://docs.openvino.ai/) - Intelin optimointityökalu

## Projektikohtaiset huomiot

### Moduuli08:n esimerkkisovellukset

Arkisto sisältää 10 kattavaa esimerkkisovellusta:

1. **01-REST Chat Quickstart** - Perus OpenAI SDK -integraatio
2. **02-OpenAI SDK Integration** - Edistyneet SDK-ominaisuudet
3. **03-Model Discovery & Benchmarking** - Mallien vertailutyökalut
4. **04-Chainlit RAG Application** - Hakuun perustuva generointi
5. **05-Multi-Agent Orchestration** - Perus agenttien koordinointi
6. **06-Models-as-Tools Router** - Älykäs mallien reititys
7. **07-Direct API Client** - Matalan tason API-integraatio
8. **08-Windows 11 Chat App** - Natiivinen Electron-työpöytäsovellus
9. **09-Advanced Multi-Agent System** - Monimutkainen agenttien koordinointi
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel -integraatio

Jokainen esimerkki havainnollistaa eri puolia Edge AI -kehityksestä Foundry Localin avulla.

### Suorituskykyhuomiot

- SLM:t on optimoitu reunakäyttöön (2-16GB RAM)
- Paikallinen inferenssi tarjoaa 50-500ms vasteajat
- Kvantisointitekniikat saavuttavat 75% koon pienennyksen 85% suorituskyvyn säilyttämisellä
- Reaaliaikaiset keskustelumahdollisuudet paikallisilla malleilla

### Turvallisuus ja yksityisyys

- Kaikki käsittely tapahtuu paikallisesti - ei tietojen lähettämistä pilveen
- Sopii yksityisyyttä vaativiin sovelluksiin (terveydenhuolto, rahoitus)
- Täyttää tietosuvereniteetin vaatimukset
- Foundry Local toimii täysin paikallisella laitteistolla

---

**Tämä on opetuskäyttöön tarkoitettu arkisto, joka keskittyy Edge AI -kehityksen opettamiseen. Pääasiallinen kontribuutiomalli on opetussisällön parantaminen ja esimerkkisovellusten lisääminen/täydentäminen, jotka havainnollistavat Edge AI -konsepteja.**

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.