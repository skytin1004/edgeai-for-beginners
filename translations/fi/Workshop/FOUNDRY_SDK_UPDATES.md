<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T14:23:18+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "fi"
}
-->
# Foundry Local SDK Päivitykset

## Yleiskatsaus

Työpajan muistikirjat ja apuohjelmat on päivitetty käyttämään oikein **virallista Foundry Local Python SDK:ta** seuraavien mallien mukaisesti:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Muokatut tiedostot

### 1. `Workshop/samples/workshop_utils.py`

**Muutokset:**
- ✅ Lisätty virheenkäsittely `foundry-local-sdk`-paketin tuonnille
- ✅ Parannettu dokumentaatio virallisten SDK-mallien mukaisesti
- ✅ Parannettu lokitietoja Unicode-symbolien avulla (✓, ✗, ⚠)
- ✅ Lisätty kattavat docstringit esimerkkien kera
- ✅ Paremmat virheilmoitukset, joissa viitataan CLI-komentoihin
- ✅ Päivitetty kommentit vastaamaan virallista SDK-dokumentaatiota

**Keskeiset parannukset:**

#### Virheenkäsittely tuonnissa
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Parannettu `get_client()`-funktio
- Lisätty yksityiskohtainen dokumentaatio SDK:n alustamismallista
- Selvennetty, että `FoundryLocalManager` käynnistää palvelun automaattisesti
- Selitetty mallialiasien muuntaminen laitteistolle optimoituihin versioihin
- Parannettu lokitietoja päätepisteen tiedoilla
- Paremmat virheilmoitukset, joissa ehdotetaan vianetsintätoimenpiteitä

#### Parannettu `chat_once()`-funktio
- Lisätty kattava docstring käyttöesimerkkien kera
- Selvennetty OpenAI SDK -yhteensopivuutta
- Dokumentoitu suoratoistotuki (kwargs:n kautta)
- Parannettu virheilmoituksia CLI-komentoehdotuksilla
- Lisätty huomautuksia mallien saatavuuden tarkistamisesta

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Muutokset:**
- ✅ Päivitetty kaikki markdown-solut SDK-viittauksilla
- ✅ Parannettu koodikommentteja SDK-mallien selityksillä
- ✅ Parannettu solujen dokumentaatiota ja selityksiä
- ✅ Lisätty vianetsintäohjeita
- ✅ Päivitetty malliluettelo (korvattu 'gpt-oss-20b' mallilla 'phi-3.5-mini')
- ✅ Parempi tulostusmuotoilu visuaalisilla indikaattoreilla
- ✅ Lisätty SDK-linkkejä ja viittauksia kaikkialle

**Solukohtaiset päivitykset:**

#### Solu 1 (Otsikko)
- Lisätty SDK-dokumentaatiolinkit
- Viitattu virallisiin GitHub-repositorioihin

#### Solu 2 (Skenaario)
- Uudelleenmuotoiltu numeroiduilla vaiheilla
- Selvennetty tarkoituspohjainen reititysmalli
- Korostettu paikallisen suorittamisen etuja

#### Solu 3 (Riippuvuuksien asennus)
- Lisätty selitys siitä, mitä kukin paketti tarjoaa
- Dokumentoitu SDK:n ominaisuudet (aliasien muuntaminen, laitteisto-optimointi)

#### Solu 4 (Ympäristön asetus)
- Parannettu funktioiden docstringejä
- Lisätty sisäisiä kommentteja SDK-mallien selittämiseksi
- Dokumentoitu malliluettelon rakenne
- Selvennetty prioriteetti-/kykyjen yhteensovittamista

#### Solu 5 (Luettelon tarkistus)
- Lisätty visuaaliset tarkistusmerkit (✓)
- Parempi tulostusmuotoilu

#### Solu 6 (Tarkoituksen tunnistustesti)
- Uudelleenmuotoiltu tulostus taulukkomuotoon
- Näyttää sekä tarkoituksen että valitun mallin

#### Solu 7 (Reititysfunktio)
- Kattava SDK-mallin selitys
- Dokumentoitu alustuksen kulku
- Listattu kaikki ominaisuudet (uudelleenkokeilu, seuranta, virheet)
- Lisätty SDK-viittauslinkki

#### Solu 8 (Erädemonstrointi)
- Parannettu selitys odotettavasta tuloksesta
- Lisätty vianetsintäosio
- Sisällytetty CLI-komennot virheiden korjaamiseen
- Parempi tulostusmuotoilu

### 3. `Workshop/notebooks/session06_README.md` (Uusi tiedosto)

**Luotu kattava dokumentaatio, joka kattaa:**

1. **Yleiskatsaus**: Arkkitehtuurikaavio ja komponenttien selitys
2. **SDK-integraatio**: Koodiesimerkit virallisten mallien mukaisesti
3. **Edellytykset**: Vaiheittaiset asennusohjeet
4. **Käyttö**: Kuinka muistikirja suoritetaan ja mukautetaan
5. **Mallialiaset**: Laitteistolle optimoitujen versioiden selitys
6. **Vianetsintä**: Yleiset ongelmat ja ratkaisut
7. **Laajentaminen**: Kuinka lisätä tarkoituksia, malleja ja mukautettua logiikkaa
8. **Suorituskykyvinkit**: Parhaat käytännöt tuotantokäyttöön
9. **Resurssit**: Linkit virallisiin dokumentteihin ja yhteisöön

## SDK-mallin toteutus

### Virallinen malli (Foundry Local -dokumentaatiosta)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Meidän toteutuksemme (workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Meidän lähestymistapamme edut:**
- ✅ Noudattaa virallista SDK-mallia tarkasti
- ✅ Lisää välimuistia välttääkseen toistuvaa alustusta
- ✅ Sisältää uudelleenkokeilulogiikan tuotantokäytön luotettavuuden parantamiseksi
- ✅ Tukee tokenien käytön seurantaa
- ✅ Tarjoaa parempia virheilmoituksia
- ✅ Säilyttää yhteensopivuuden virallisten esimerkkien kanssa

## Malliluettelon muutokset

### Ennen
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Jälkeen
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Syy:** Korvattu 'gpt-oss-20b' (epästandardi alias) mallilla 'phi-3.5-mini' (virallinen Foundry Local -alias).

## Riippuvuudet

### Päivitetty requirements.txt

Workshopin requirements.txt sisältää jo:
```
foundry-local-sdk
openai>=1.30.0
```

Nämä ovat ainoat paketit, joita tarvitaan Foundry Local -integraatioon.

## Päivitysten testaus

### 1. Varmista, että Foundry Local toimii

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Tarkista saatavilla olevat mallit

```bash
foundry model ls
```

Varmista, että nämä mallit ovat saatavilla tai latautuvat automaattisesti:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Suorita muistikirja

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Tai avaa VS Codessa ja suorita kaikki solut.

### 4. Odotettu käyttäytyminen

**Solu 1 (Asennus):** Paketit asennetaan onnistuneesti  
**Solu 2 (Asetus):** Ei virheitä, tuonnit toimivat  
**Solu 3 (Tarkistus):** Näyttää ✓ malliluettelon kanssa  
**Solu 4 (Testaa tarkoitus):** Näyttää tarkoituksen tunnistustulokset  
**Solu 5 (Reititin):** Näyttää ✓ Reititysfunktio valmis  
**Solu 6 (Suorita):** Reitittää kehotteet malleihin, näyttää tulokset  

### 5. Vianetsintä yhteysvirheissä

Jos näet `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Ympäristömuuttujat

Seuraavat ympäristömuuttujat ovat tuettuja:

| Muuttuja | Oletus | Kuvaus |
|----------|---------|-------------|
| `SHOW_USAGE` | `0` | Aseta `1` tulostaaksesi tokenien käytön |
| `RETRY_ON_FAIL` | `1` | Ota uudelleenkokeilulogiikka käyttöön |
| `RETRY_BACKOFF` | `1.0` | Alustava viive uudelleenkokeilulle (sekunteina) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Ylikirjoita palvelun päätepiste |

### Käyttöesimerkit

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Siirtyminen vanhasta mallista

Jos sinulla on olemassa olevaa koodia, joka käyttää suoria API-kutsuja, tässä ohjeet siirtymiseen:

### Ennen (suora API)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### Jälkeen (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Siirtymisen edut
- ✅ Automaattinen palvelun hallinta
- ✅ Mallialiasien muuntaminen
- ✅ Laitteisto-optimoinnin valinta
- ✅ Parempi virheenkäsittely
- ✅ OpenAI SDK -yhteensopivuus
- ✅ Suoratoistotuki

## Viittaukset

### Virallinen dokumentaatio
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local  
- **Python SDK Lähde**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  
- **CLI-viite**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md  
- **Vianetsintä**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md  

### Workshop-resurssit
- **Session 06 README**: `Workshop/notebooks/session06_README.md`  
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`  
- **Esimerkkimuistikirja**: `Workshop/notebooks/session06_models_router.ipynb`  

### Yhteisö
- **Discord**: https://aka.ms/foundry-local-discord  
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues  

## Seuraavat askeleet

1. **Tarkista muutokset**: Lue päivitetyt tiedostot  
2. **Testaa muistikirja**: Suorita session06_models_router.ipynb  
3. **Varmista SDK**: Varmista, että foundry-local-sdk on asennettu  
4. **Tarkista palvelu**: Varmista, että Foundry Local toimii  
5. **Tutustu dokumentaatioon**: Lue uusi session06_README.md  

## Yhteenveto

Nämä päivitykset varmistavat, että Workshop-materiaalit noudattavat **virallisia Foundry Local SDK -malleja** täsmälleen kuten dokumentoitu GitHub-repositoriossa. Kaikki koodiesimerkit, dokumentaatio ja apuohjelmat ovat nyt linjassa Microsoftin suositeltujen parhaiden käytäntöjen kanssa paikallisten tekoälymallien käyttöönotossa.

Muutokset parantavat:
- ✅ **Tarkkuutta**: Käyttää virallisia SDK-malleja  
- ✅ **Dokumentaatiota**: Kattavat selitykset ja esimerkit  
- ✅ **Virheenkäsittelyä**: Paremmat viestit ja vianetsintäohjeet  
- ✅ **Ylläpidettävyyttä**: Noudattaa virallisia konventioita  
- ✅ **Käyttäjäkokemusta**: Selkeämmät ohjeet ja virheiden korjaus  

---

**Päivitetty:** 8. lokakuuta 2025  
**SDK-versio:** foundry-local-sdk (uusin)  
**Workshop-haara:** Reactor  

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.