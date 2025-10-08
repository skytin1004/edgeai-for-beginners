<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T13:58:55+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "hr"
}
-->
# Ažuriranja za Foundry Local SDK

## Pregled

Ažurirani Workshop bilježnici i alati kako bi se pravilno koristio **službeni Foundry Local Python SDK** prema uzorcima iz:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Izmijenjene datoteke

### 1. `Workshop/samples/workshop_utils.py`

**Promjene:**
- ✅ Dodano rukovanje greškama pri uvozu paketa `foundry-local-sdk`
- ✅ Poboljšana dokumentacija prema službenim SDK uzorcima
- ✅ Poboljšano logiranje s Unicode simbolima (✓, ✗, ⚠)
- ✅ Dodani sveobuhvatni docstringovi s primjerima
- ✅ Bolje poruke o greškama koje upućuju na CLI naredbe
- ✅ Ažurirani komentari kako bi se uskladili sa službenom SDK dokumentacijom

**Ključna poboljšanja:**

#### Rukovanje greškama pri uvozu
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Poboljšana funkcija `get_client()`
- Dodana detaljna dokumentacija o uzorku inicijalizacije SDK-a
- Objašnjeno da `FoundryLocalManager` automatski pokreće uslugu
- Objašnjeno rješavanje aliasa modela prema hardverski optimiziranim varijantama
- Poboljšano logiranje s informacijama o endpointu
- Bolje poruke o greškama s prijedlozima za rješavanje problema

#### Poboljšana funkcija `chat_once()`
- Dodan sveobuhvatan docstring s primjerima korištenja
- Pojašnjena kompatibilnost s OpenAI SDK-om
- Dokumentirana podrška za streaming (putem kwargs)
- Poboljšane poruke o greškama s prijedlozima CLI naredbi
- Dodane napomene o provjeri dostupnosti modela

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Promjene:**
- ✅ Ažurirane sve markdown ćelije s referencama na SDK
- ✅ Poboljšani komentari u kodu s objašnjenjima SDK uzoraka
- ✅ Poboljšana dokumentacija ćelija i objašnjenja
- ✅ Dodane smjernice za rješavanje problema
- ✅ Ažuriran katalog modela (zamijenjen 'gpt-oss-20b' s 'phi-3.5-mini')
- ✅ Bolje formatiranje izlaza s vizualnim indikatorima
- ✅ Dodane SDK poveznice i reference kroz cijeli dokument

**Ažuriranja po ćelijama:**

#### Ćelija 1 (Naslov)
- Dodane poveznice na SDK dokumentaciju
- Referencirani službeni GitHub repozitoriji

#### Ćelija 2 (Scenario)
- Preformatirano s numeriranim koracima
- Pojašnjen uzorak usmjeravanja temeljen na namjeri
- Naglašene prednosti lokalnog izvršavanja

#### Ćelija 3 (Instalacija ovisnosti)
- Dodano objašnjenje što svaki paket pruža
- Dokumentirane mogućnosti SDK-a (rješavanje aliasa, hardverska optimizacija)

#### Ćelija 4 (Postavljanje okruženja)
- Poboljšani docstringovi funkcija
- Dodani inline komentari koji objašnjavaju SDK uzorke
- Dokumentirana struktura kataloga modela
- Pojašnjeno podudaranje prioriteta/mogućnosti

#### Ćelija 5 (Provjera kataloga)
- Dodane vizualne oznake (✓)
- Bolje formatiran izlaz

#### Ćelija 6 (Test detekcije namjere)
- Preformatiran izlaz u stilu tablice
- Prikazuje i namjeru i odabrani model

#### Ćelija 7 (Funkcija usmjeravanja)
- Sveobuhvatno objašnjenje SDK uzorka
- Dokumentiran tok inicijalizacije
- Nabrojane sve značajke (ponavljanje, praćenje, greške)
- Dodana poveznica na SDK dokumentaciju

#### Ćelija 8 (Batch demo)
- Poboljšano objašnjenje što očekivati
- Dodana sekcija za rješavanje problema
- Uključene CLI naredbe za otklanjanje grešaka
- Bolje formatiran prikaz izlaza

### 3. `Workshop/notebooks/session06_README.md` (Nova datoteka)

**Stvorena sveobuhvatna dokumentacija koja pokriva:**

1. **Pregled**: Dijagram arhitekture i objašnjenje komponenti
2. **Integracija SDK-a**: Primjeri koda prema službenim uzorcima
3. **Preduvjeti**: Korak-po-korak upute za postavljanje
4. **Korištenje**: Kako pokrenuti i prilagoditi bilježnik
5. **Alias modeli**: Objašnjenje hardverski optimiziranih varijanti
6. **Rješavanje problema**: Uobičajeni problemi i rješenja
7. **Proširenje**: Kako dodati namjere, modele i prilagođenu logiku
8. **Savjeti za performanse**: Najbolje prakse za produkcijsku upotrebu
9. **Resursi**: Poveznice na službenu dokumentaciju i zajednicu

## Implementacija SDK uzorka

### Službeni uzorak (iz Foundry Local dokumentacije)

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

### Naša implementacija (u workshop_utils)

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

**Prednosti našeg pristupa:**
- ✅ Točno slijedi službeni SDK uzorak
- ✅ Dodaje caching kako bi se izbjegla ponovljena inicijalizacija
- ✅ Uključuje logiku ponavljanja za robusnost u produkciji
- ✅ Podržava praćenje korištenja tokena
- ✅ Pruža bolje poruke o greškama
- ✅ Ostaje kompatibilan sa službenim primjerima

## Promjene u katalogu modela

### Prije
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Poslije
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Razlog:** Zamijenjen 'gpt-oss-20b' (nestandardni alias) s 'phi-3.5-mini' (službeni Foundry Local alias).

## Ovisnosti

### Ažurirani requirements.txt

Workshop requirements.txt već uključuje:
```
foundry-local-sdk
openai>=1.30.0
```

Ovo su jedini paketi potrebni za integraciju s Foundry Local.

## Testiranje ažuriranja

### 1. Provjerite je li Foundry Local pokrenut

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Provjerite dostupne modele

```bash
foundry model ls
```

Provjerite jesu li dostupni ili će se automatski preuzeti:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Pokrenite bilježnik

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Ili otvorite u VS Code i pokrenite sve ćelije.

### 4. Očekivano ponašanje

**Ćelija 1 (Instalacija):** Uspješno instalira pakete  
**Ćelija 2 (Postavljanje):** Nema grešaka, uvozi rade  
**Ćelija 3 (Provjera):** Prikazuje ✓ s popisom modela  
**Ćelija 4 (Test namjere):** Prikazuje rezultate detekcije namjere  
**Ćelija 5 (Usmjeravanje):** Prikazuje ✓ Funkcija usmjeravanja spremna  
**Ćelija 6 (Izvršenje):** Usmjerava upite prema modelima, prikazuje rezultate  

### 5. Rješavanje problema s povezivanjem

Ako vidite `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Varijable okruženja

Podržane su sljedeće varijable okruženja:

| Varijabla | Zadano | Opis |
|-----------|--------|------|
| `SHOW_USAGE` | `0` | Postavite na `1` za ispis korištenja tokena |
| `RETRY_ON_FAIL` | `1` | Omogućite logiku ponavljanja |
| `RETRY_BACKOFF` | `1.0` | Početno kašnjenje ponavljanja (sekunde) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Prepišite endpoint usluge |

### Primjeri korištenja

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migracija sa starog uzorka

Ako imate postojeći kod koji koristi izravne API pozive, evo kako migrirati:

### Prije (Izravni API)
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

### Poslije (SDK)
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

### Prednosti migracije
- ✅ Automatsko upravljanje uslugom
- ✅ Rješavanje aliasa modela
- ✅ Odabir hardverske optimizacije
- ✅ Bolje rukovanje greškama
- ✅ Kompatibilnost s OpenAI SDK-om
- ✅ Podrška za streaming

## Reference

### Službena dokumentacija
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK Izvor**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **CLI Referenca**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Rješavanje problema**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Workshop resursi
- **Session 06 README**: `Workshop/notebooks/session06_README.md`
- **Workshop Alati**: `Workshop/samples/workshop_utils.py`
- **Primjer bilježnika**: `Workshop/notebooks/session06_models_router.ipynb`

### Zajednica
- **Discord**: https://aka.ms/foundry-local-discord
- **GitHub Problemi**: https://github.com/microsoft/Foundry-Local/issues

## Sljedeći koraci

1. **Pregledajte promjene**: Pročitajte ažurirane datoteke  
2. **Testirajte bilježnik**: Pokrenite session06_models_router.ipynb  
3. **Provjerite SDK**: Osigurajte da je foundry-local-sdk instaliran  
4. **Provjerite uslugu**: Potvrdite da je Foundry Local pokrenut  
5. **Istražite dokumentaciju**: Pročitajte novi session06_README.md  

## Sažetak

Ova ažuriranja osiguravaju da materijali Workshopa slijede **službene uzorke Foundry Local SDK-a** točno kako su dokumentirani u GitHub repozitoriju. Svi primjeri koda, dokumentacija i alati sada su usklađeni s Microsoftovim preporučenim najboljim praksama za lokalno postavljanje AI modela.

Promjene poboljšavaju:
- ✅ **Točnost**: Koristi službene SDK uzorke  
- ✅ **Dokumentaciju**: Sveobuhvatna objašnjenja i primjeri  
- ✅ **Rukovanje greškama**: Bolje poruke i smjernice za rješavanje problema  
- ✅ **Održavanje**: Slijedi službene konvencije  
- ✅ **Korisničko iskustvo**: Jasnije upute i pomoć pri otklanjanju grešaka  

---

**Ažurirano:** 8. listopada 2025.  
**SDK Verzija:** foundry-local-sdk (najnovija)  
**Workshop Grana:** Reactor  

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.