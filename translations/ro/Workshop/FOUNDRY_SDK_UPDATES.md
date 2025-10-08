<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T15:14:23+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "ro"
}
-->
# Actualizări SDK Local Foundry

## Prezentare Generală

Notebook-urile și utilitarele Workshop au fost actualizate pentru a utiliza corect **SDK-ul oficial Foundry Local pentru Python**, urmând modelele de la:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Fișiere Modificate

### 1. `Workshop/samples/workshop_utils.py`

**Modificări:**
- ✅ Adăugat gestionarea erorilor de import pentru pachetul `foundry-local-sdk`
- ✅ Documentație îmbunătățită cu modele oficiale SDK
- ✅ Logare îmbunătățită cu simboluri Unicode (✓, ✗, ⚠)
- ✅ Adăugate docstrings detaliate cu exemple
- ✅ Mesaje de eroare mai clare care fac referire la comenzi CLI
- ✅ Comentarii actualizate pentru a se potrivi cu documentația oficială SDK

**Îmbunătățiri Cheie:**

#### Gestionarea Erorilor de Import
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Funcția îmbunătățită `get_client()`
- Documentație detaliată despre modelul de inițializare SDK
- Clarificat că `FoundryLocalManager` pornește automat serviciul
- Explicat rezolvarea aliasurilor modelelor către variante optimizate hardware
- Logare îmbunătățită cu informații despre endpoint
- Mesaje de eroare mai bune care sugerează pași de depanare

#### Funcția îmbunătățită `chat_once()`
- Adăugat docstring detaliat cu exemple de utilizare
- Clarificat compatibilitatea SDK OpenAI
- Documentat suportul pentru streaming (prin kwargs)
- Mesaje de eroare îmbunătățite cu sugestii de comenzi CLI
- Adăugat note despre verificarea disponibilității modelelor

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Modificări:**
- ✅ Actualizat toate celulele markdown cu referințe SDK
- ✅ Comentarii de cod îmbunătățite cu explicații despre modele SDK
- ✅ Documentație și explicații îmbunătățite în celule
- ✅ Adăugat ghiduri de depanare
- ✅ Catalogul de modele actualizat (înlocuit 'gpt-oss-20b' cu 'phi-3.5-mini')
- ✅ Formatări mai bune ale ieșirii cu indicatori vizuali
- ✅ Adăugat linkuri și referințe SDK pe tot parcursul

**Actualizări Celulă cu Celulă:**

#### Celula 1 (Titlu)
- Adăugat linkuri către documentația SDK
- Referit la depozitele oficiale GitHub

#### Celula 2 (Scenariu)
- Reformulat cu pași numerotați
- Clarificat modelul de rutare bazat pe intenție
- Subliniat beneficiile execuției locale

#### Celula 3 (Instalare Dependențe)
- Adăugat explicații despre ce oferă fiecare pachet
- Documentat capabilitățile SDK (rezolvarea aliasurilor, optimizarea hardware)

#### Celula 4 (Configurare Mediu)
- Docstrings funcționale îmbunătățite
- Comentarii inline adăugate pentru a explica modelele SDK
- Documentat structura catalogului de modele
- Clarificat potrivirea priorității/capabilității

#### Celula 5 (Verificare Catalog)
- Adăugat marcaje vizuale (✓)
- Format ieșire îmbunătățit

#### Celula 6 (Testare Detectare Intenție)
- Format ieșire în stil tabel
- Afișează atât intenția, cât și modelul selectat

#### Celula 7 (Funcție de Rutare)
- Explicație cuprinzătoare a modelului SDK
- Documentat fluxul de inițializare
- Listat toate funcționalitățile (retry, tracking, erori)
- Adăugat link de referință SDK

#### Celula 8 (Demo Batch)
- Explicație îmbunătățită despre ce să așteptați
- Adăugat secțiune de depanare
- Inclus comenzi CLI pentru debugging
- Format ieșire afișare mai bun

### 3. `Workshop/notebooks/session06_README.md` (Fișier Nou)

**Documentație cuprinzătoare creată care acoperă:**

1. **Prezentare Generală**: Diagramă arhitecturală și explicația componentelor
2. **Integrare SDK**: Exemple de cod care urmează modelele oficiale
3. **Prerechizite**: Instrucțiuni pas cu pas pentru configurare
4. **Utilizare**: Cum să rulați și să personalizați notebook-ul
5. **Aliasuri Modele**: Explicația variantelor optimizate hardware
6. **Depanare**: Probleme comune și soluții
7. **Extindere**: Cum să adăugați intenții, modele și logică personalizată
8. **Sfaturi de Performanță**: Cele mai bune practici pentru utilizarea în producție
9. **Resurse**: Linkuri către documentația oficială și comunitate

## Implementarea Modelului SDK

### Model Oficial (din documentația Foundry Local)

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

### Implementarea Noastră (în workshop_utils)

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

**Beneficiile Abordării Noastre:**
- ✅ Urmează exact modelul oficial SDK
- ✅ Adaugă caching pentru a evita inițializările repetate
- ✅ Include logică de retry pentru robustețe în producție
- ✅ Suportă urmărirea utilizării token-urilor
- ✅ Oferă mesaje de eroare mai bune
- ✅ Rămâne compatibil cu exemplele oficiale

## Modificări Catalog Modele

### Înainte
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### După
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Motiv:** Înlocuit 'gpt-oss-20b' (alias non-standard) cu 'phi-3.5-mini' (alias oficial Foundry Local).

## Dependențe

### Actualizat requirements.txt

Fișierul requirements.txt al Workshop-ului include deja:
```
foundry-local-sdk
openai>=1.30.0
```

Acestea sunt singurele pachete necesare pentru integrarea Foundry Local.

## Testarea Actualizărilor

### 1. Verificați că Foundry Local Rulează

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Verificați Modelele Disponibile

```bash
foundry model ls
```

Asigurați-vă că aceste modele sunt disponibile sau se vor descărca automat:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Rulați Notebook-ul

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Sau deschideți în VS Code și rulați toate celulele.

### 4. Comportament Așteptat

**Celula 1 (Instalare):** Instalează pachetele cu succes  
**Celula 2 (Configurare):** Fără erori, importurile funcționează  
**Celula 3 (Verificare):** Afișează ✓ cu lista de modele  
**Celula 4 (Test Intenție):** Afișează rezultatele detectării intenției  
**Celula 5 (Router):** Afișează ✓ Funcția de rutare gata  
**Celula 6 (Executare):** Rutează prompturile către modele, afișează rezultatele  

### 5. Depanarea Erorilor de Conexiune

Dacă vedeți `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Variabile de Mediu

Următoarele variabile de mediu sunt suportate:

| Variabilă | Implicit | Descriere |
|-----------|----------|-----------|
| `SHOW_USAGE` | `0` | Setați la `1` pentru a afișa utilizarea token-urilor |
| `RETRY_ON_FAIL` | `1` | Activați logica de retry |
| `RETRY_BACKOFF` | `1.0` | Întârzierea inițială pentru retry (secunde) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Suprascrie endpoint-ul serviciului |

### Exemple de Utilizare

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migrare de la Modelul Vechi

Dacă aveți cod existent care folosește apeluri API directe, iată cum să migrați:

### Înainte (API Direct)
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

### După (SDK)
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

### Beneficiile Migrării
- ✅ Management automat al serviciului
- ✅ Rezolvarea aliasurilor modelelor
- ✅ Selectarea optimizării hardware
- ✅ Gestionarea erorilor mai bună
- ✅ Compatibilitate SDK OpenAI
- ✅ Suport pentru streaming

## Referințe

### Documentație Oficială
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local
- **Sursa SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Referință CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **API REST**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Depanare**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Resurse Workshop
- **README Sesiunea 06**: `Workshop/notebooks/session06_README.md`
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`
- **Notebook Exemplu**: `Workshop/notebooks/session06_models_router.ipynb`

### Comunitate
- **Discord**: https://aka.ms/foundry-local-discord
- **Probleme GitHub**: https://github.com/microsoft/Foundry-Local/issues

## Pași Următori

1. **Revizuiți Modificările**: Citiți fișierele actualizate  
2. **Testați Notebook-ul**: Rulați session06_models_router.ipynb  
3. **Verificați SDK-ul**: Asigurați-vă că foundry-local-sdk este instalat  
4. **Verificați Serviciul**: Confirmați că Foundry Local rulează  
5. **Explorați Documentația**: Citiți noul session06_README.md  

## Rezumat

Aceste actualizări asigură că materialele Workshop urmează **modelele oficiale SDK Foundry Local** exact așa cum sunt documentate în depozitul GitHub. Toate exemplele de cod, documentația și utilitarele sunt acum aliniate cu cele mai bune practici recomandate de Microsoft pentru implementarea locală a modelelor AI.

Modificările îmbunătățesc:
- ✅ **Corectitudinea**: Utilizează modelele oficiale SDK  
- ✅ **Documentația**: Explicații și exemple cuprinzătoare  
- ✅ **Gestionarea Erorilor**: Mesaje mai bune și ghiduri de depanare  
- ✅ **Menținerea**: Urmează convențiile oficiale  
- ✅ **Experiența Utilizatorului**: Instrucțiuni mai clare și ajutor pentru debugging  

---

**Actualizat:** 8 octombrie 2025  
**Versiune SDK:** foundry-local-sdk (ultima versiune)  
**Branch Workshop:** Reactor

---

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.