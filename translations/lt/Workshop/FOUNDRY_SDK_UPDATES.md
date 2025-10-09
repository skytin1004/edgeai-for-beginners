<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-09T21:06:07+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "lt"
}
-->
# Foundry Local SDK Atnaujinimai

## Apžvalga

Atnaujinti Workshop užrašai ir įrankiai, kad tinkamai naudotų **oficialų Foundry Local Python SDK**, laikantis šių šablonų:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Pakeisti failai

### 1. `Workshop/samples/workshop_utils.py`

**Pakeitimai:**
- ✅ Pridėtas importavimo klaidų apdorojimas `foundry-local-sdk` paketui
- ✅ Patobulinta dokumentacija su oficialiais SDK šablonais
- ✅ Pagerintas žurnalizavimas naudojant Unicode simbolius (✓, ✗, ⚠)
- ✅ Pridėti išsamūs docstring su pavyzdžiais
- ✅ Patobulintos klaidų žinutės su CLI komandų nuorodomis
- ✅ Atnaujinti komentarai, kad atitiktų oficialią SDK dokumentaciją

**Pagrindiniai patobulinimai:**

#### Importavimo klaidų apdorojimas
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Patobulinta `get_client()` funkcija
- Pridėta išsami dokumentacija apie SDK inicializavimo šabloną
- Paaiškinta, kad `FoundryLocalManager` automatiškai paleidžia paslaugą
- Paaiškintas modelio aliasų priskyrimas optimizuotiems aparatūros variantams
- Pagerintas žurnalizavimas su galinių taškų informacija
- Patobulintos klaidų žinutės su siūlymais, kaip spręsti problemas

#### Patobulinta `chat_once()` funkcija
- Pridėtas išsamus docstring su naudojimo pavyzdžiais
- Paaiškintas OpenAI SDK suderinamumas
- Dokumentuotas srautinio perdavimo palaikymas (per kwargs)
- Patobulintos klaidų žinutės su CLI komandų pasiūlymais
- Pridėtos pastabos apie modelio prieinamumo tikrinimą

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Pakeitimai:**
- ✅ Atnaujintos visos markdown ląstelės su SDK nuorodomis
- ✅ Patobulinti kodo komentarai su SDK šablonų paaiškinimais
- ✅ Pagerinta ląstelių dokumentacija ir paaiškinimai
- ✅ Pridėtos trikčių šalinimo gairės
- ✅ Atnaujintas modelių katalogas (pakeistas 'gpt-oss-20b' į 'phi-3.5-mini')
- ✅ Pagerintas išvesties formatavimas su vizualiniais indikatoriais
- ✅ Pridėtos SDK nuorodos ir nuorodos visame dokumente

**Ląstelių atnaujinimai:**

#### Ląstelė 1 (Pavadinimas)
- Pridėtos SDK dokumentacijos nuorodos
- Paminėtos oficialios GitHub saugyklos

#### Ląstelė 2 (Scenarijus)
- Performatuota su numeruotais žingsniais
- Paaiškintas ketinimų nukreipimo šablonas
- Pabrėžta vietinio vykdymo nauda

#### Ląstelė 3 (Priklausomybių diegimas)
- Pridėtas paaiškinimas, ką suteikia kiekvienas paketas
- Dokumentuotos SDK galimybės (aliasų priskyrimas, aparatūros optimizavimas)

#### Ląstelė 4 (Aplinkos nustatymas)
- Patobulinti funkcijų docstring
- Pridėti komentarai, paaiškinantys SDK šablonus
- Dokumentuota modelių katalogo struktūra
- Paaiškintas prioritetų/savybių atitikimas

#### Ląstelė 5 (Katalogo tikrinimas)
- Pridėti vizualiniai žymekliai (✓)
- Geriau suformatuota išvestis

#### Ląstelė 6 (Ketinimų aptikimo testas)
- Performatuota išvestis į lentelės stilių
- Rodo tiek ketinimą, tiek pasirinktą modelį

#### Ląstelė 7 (Nukreipimo funkcija)
- Išsamus SDK šablono paaiškinimas
- Dokumentuotas inicializavimo procesas
- Išvardytos visos funkcijos (pakartojimas, sekimas, klaidos)
- Pridėta SDK nuoroda

#### Ląstelė 8 (Partijos demonstracija)
- Patobulintas paaiškinimas, ko tikėtis
- Pridėta trikčių šalinimo skiltis
- Įtrauktos CLI komandos derinimui
- Geriau suformatuota išvesties rodymas

### 3. `Workshop/notebooks/session06_README.md` (Naujas failas)

**Sukurta išsami dokumentacija, apimanti:**

1. **Apžvalga**: Architektūros diagrama ir komponentų paaiškinimas
2. **SDK integracija**: Kodo pavyzdžiai pagal oficialius šablonus
3. **Reikalavimai**: Žingsnis po žingsnio nustatymo instrukcijos
4. **Naudojimas**: Kaip paleisti ir pritaikyti užrašų knygelę
5. **Modelių aliasai**: Aparatūros optimizuotų variantų paaiškinimas
6. **Trikčių šalinimas**: Dažniausios problemos ir sprendimai
7. **Plėtra**: Kaip pridėti ketinimus, modelius ir pritaikytą logiką
8. **Našumo patarimai**: Geriausia praktika gamybos naudojimui
9. **Ištekliai**: Nuorodos į oficialią dokumentaciją ir bendruomenę

## SDK šablono įgyvendinimas

### Oficiali schema (iš Foundry Local dokumentacijos)

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

### Mūsų įgyvendinimas (workshop_utils)

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

**Mūsų požiūrio privalumai:**
- ✅ Tiksliai atitinka oficialų SDK šabloną
- ✅ Prideda talpyklą, kad būtų išvengta pakartotinio inicializavimo
- ✅ Apima pakartojimo logiką gamybos patikimumui
- ✅ Palaiko žetonų naudojimo sekimą
- ✅ Suteikia geresnes klaidų žinutes
- ✅ Suderinamas su oficialiais pavyzdžiais

## Modelių katalogo pakeitimai

### Prieš
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Po
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Priežastis:** Pakeistas 'gpt-oss-20b' (nestandartinis aliasas) į 'phi-3.5-mini' (oficialus Foundry Local aliasas).

## Priklausomybės

### Atnaujintas requirements.txt

Workshop requirements.txt jau apima:
```
foundry-local-sdk
openai>=1.30.0
```

Tai vieninteliai paketai, reikalingi Foundry Local integracijai.

## Atnaujinimų testavimas

### 1. Patikrinkite, ar veikia Foundry Local

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Patikrinkite galimus modelius

```bash
foundry model ls
```

Įsitikinkite, kad šie modeliai yra prieinami arba bus automatiškai atsisiųsti:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Paleiskite užrašų knygelę

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Arba atidarykite VS Code ir paleiskite visas ląsteles.

### 4. Tikėtinas elgesys

**Ląstelė 1 (Diegimas):** Sėkmingai įdiegiami paketai  
**Ląstelė 2 (Nustatymas):** Be klaidų, importavimas veikia  
**Ląstelė 3 (Patikrinimas):** Rodo ✓ su modelių sąrašu  
**Ląstelė 4 (Ketinimų testas):** Rodo ketinimų aptikimo rezultatus  
**Ląstelė 5 (Nukreipimas):** Rodo ✓ Nukreipimo funkcija paruošta  
**Ląstelė 6 (Vykdymas):** Nukreipia užklausas į modelius, rodo rezultatus  

### 5. Trikčių šalinimas dėl ryšio klaidų

Jei matote `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Aplinkos kintamieji

Palaikomi šie aplinkos kintamieji:

| Kintamasis | Numatytasis | Aprašymas |
|------------|-------------|-----------|
| `SHOW_USAGE` | `0` | Nustatykite į `1`, kad būtų rodomas žetonų naudojimas |
| `RETRY_ON_FAIL` | `1` | Įjungti pakartojimo logiką |
| `RETRY_BACKOFF` | `1.0` | Pradinis pakartojimo delsimas (sekundėmis) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Perrašyti paslaugos galinį tašką |

### Naudojimo pavyzdžiai

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migracija iš senojo šablono

Jei turite esamą kodą, naudojantį tiesioginius API skambučius, štai kaip migruoti:

### Prieš (Tiesioginis API)
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

### Po (SDK)
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

### Migracijos privalumai
- ✅ Automatinis paslaugų valdymas
- ✅ Modelio aliasų priskyrimas
- ✅ Aparatūros optimizavimo pasirinkimas
- ✅ Geresnis klaidų apdorojimas
- ✅ OpenAI SDK suderinamumas
- ✅ Srautinio perdavimo palaikymas

## Nuorodos

### Oficiali dokumentacija
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local  
- **Python SDK šaltinis**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  
- **CLI nuoroda**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md  
- **Trikčių šalinimas**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md  

### Workshop ištekliai
- **6 sesijos README**: `Workshop/notebooks/session06_README.md`  
- **Workshop įrankiai**: `Workshop/samples/workshop_utils.py`  
- **Pavyzdinė užrašų knygelė**: `Workshop/notebooks/session06_models_router.ipynb`  

### Bendruomenė
- **Discord**: https://aka.ms/foundry-local-discord  
- **GitHub problemos**: https://github.com/microsoft/Foundry-Local/issues  

## Kiti žingsniai

1. **Peržiūrėkite pakeitimus**: Perskaitykite atnaujintus failus  
2. **Testuokite užrašų knygelę**: Paleiskite session06_models_router.ipynb  
3. **Patikrinkite SDK**: Įsitikinkite, kad įdiegtas foundry-local-sdk  
4. **Patikrinkite paslaugą**: Įsitikinkite, kad veikia Foundry Local  
5. **Naršykite dokumentaciją**: Perskaitykite naują session06_README.md  

## Santrauka

Šie atnaujinimai užtikrina, kad Workshop medžiaga tiksliai atitiktų **oficialius Foundry Local SDK šablonus**, kaip nurodyta GitHub saugykloje. Visi kodo pavyzdžiai, dokumentacija ir įrankiai dabar atitinka Microsoft rekomenduojamą geriausią praktiką vietiniam AI modelių diegimui.

Pakeitimai pagerina:
- ✅ **Tikslumą**: Naudojami oficialūs SDK šablonai  
- ✅ **Dokumentaciją**: Išsamūs paaiškinimai ir pavyzdžiai  
- ✅ **Klaidų apdorojimą**: Geresnės žinutės ir trikčių šalinimo gairės  
- ✅ **Priežiūrą**: Laikomasi oficialių konvencijų  
- ✅ **Naudotojo patirtį**: Aiškesnės instrukcijos ir pagalba derinant  

---

**Atnaujinta:** 2025 m. spalio 8 d.  
**SDK versija:** foundry-local-sdk (naujausia)  
**Workshop šaka:** Reactor  

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingą interpretaciją, atsiradusią dėl šio vertimo naudojimo.